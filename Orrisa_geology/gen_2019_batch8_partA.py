#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 8 Part A (Q091 - Q098)
Sedimentary Petrology: Sandstone Petrography, Grain Sizes, Structures, and Diagenesis.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q091: Arkose Sandstone - Feldspar Content (>25%)
# -----------------------------------------------------------------------------
def gen_q091():
    q_num = 91
    filename = "Q091_Arkose_Contains_More_Than_25_Percent_Feldspars_Complete_Guide.html"
    title = "Q091: Sedimentary Petrology - Arkose Sandstone & Feldspar Content"
    badge = "OPSC 2019 Geology Paper-II • Question 91 • Sedimentary Petrology"
    h1_title = "Arkose Sandstone Petrography: The 25% Feldspar Criterion and Provenance"
    meta_text = "<strong>Topic:</strong> Sandstone Classification & Petrography • <strong>Key Concept:</strong> Feldspar-Rich Arenites & Tectonic Provenance • <strong>Textbooks:</strong> F.J. Pettijohn (1975); R.L. Folk (1968); K.M. Bangar (p. 136)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Sandstone Classification & Arkose Systematics</div>
      <p>In sedimentary petrology, terrigenous clastic sandstones are classified on the ternary <strong>QFL Diagram</strong> (Quartz &ndash; Feldspar &ndash; Lithic rock fragments) pioneered by <strong>R.L. Folk (1968)</strong> and <strong>F.J. Pettijohn (1975)</strong>. A sandstone is formally designated as an <strong>Arkose</strong> (or arkosic arenite) when its detrital framework contains <strong>more than 25% feldspar</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sandstone Class</th>
              <th>Quartz Content ($Q\%$)</th>
              <th>Feldspar Content ($F\%$)</th>
              <th>Lithic Fragments ($L\%$)</th>
              <th>Tectonic Provenance & Climatic Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>ARKOSE</strong> (Option C)</td>
              <td>&lt; 75%</td>
              <td><strong>&gt; 25% Feldspar</strong> ($F / L > 3:1$)</td>
              <td>&lt; 25% Lithics</td>
              <td>Rapid erosion of granitic/gneissic basements in fault-bounded rift basins (graben); arid or cold climate.</td>
            </tr>
            <tr>
              <td>Subarkose</td>
              <td>75% &ndash; 95%</td>
              <td>5% &ndash; 25% Feldspar</td>
              <td>&lt; 25% Lithics</td>
              <td>Moderately mature sands; slight chemical weathering or mixed quartzose provenance.</td>
            </tr>
            <tr>
              <td>Quartzarenite</td>
              <td>&gt; 95%</td>
              <td>&lt; 5%</td>
              <td>&lt; 5%</td>
              <td>Ultra-mature stable cratonic platforms; multiple cycles of reworking and chemical leaching.</td>
            </tr>
            <tr>
              <td>Lithic Arenite</td>
              <td>&lt; 75%</td>
              <td>&lt; 25%</td>
              <td>&gt; 25% Lithics ($L / F > 3:1$)</td>
              <td>Active orogenic belts, island arcs, and collision suture zones (recycled orogen provenance).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "An <strong>arkose</strong> is a sandstone composed of quartz and <strong>more than 25 percent feldspar</strong> (chiefly orthoclase, microcline, or sodic plagioclase). The grains are generally poorly sorted, angular to sub-angular, and cemented by calcite, iron oxides, or silica. The presence of abundant fresh feldspar indicates that the source rocks (granites or gneisses) underwent rapid mechanical disintegration under arid, semi-arid, or high-relief tectonic conditions before chemical decomposition could destroy the feldspars."
        <div class="quote-author">&mdash; F.J. Pettijohn, <em>Sedimentary Rocks</em> (3rd Ed., Harper & Row, p. 214)</div>
      </div>

      <div class="formula-box">
        $$\text{Folk (1968) Arkose Definition: Framework Grains } (Q + F + L = 100\%)$$
        $$\mathbf{Feldspar\ (F) > 25\%} \quad \text{and} \quad \frac{\text{Feldspar}}{\text{Lithics}} > 3 \implies \mathbf{Arkose\ (Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q091/arkose_sandstone_folk_ternary_feldspar.png" alt="Arkose Sandstone Folk Ternary Feldspar" class="figure-img">
        <div class="figure-caption">Figure 91: Folk (1968) QFL ternary classification of sandstones highlighting the Arkose field defined by &gt; 25% feldspar and F/L &gt; 3:1.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 91</div>
        <div class="raw-q-text">Arkose contain more than 25% of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Micas</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Amphiboles</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Feldspars</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Chlorite</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Feldspars)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Feldspars</div>
          <p>By international consensus across all modern sandstone classifications (Folk, 1968; Pettijohn, 1975; Dickinson, 1985; Bangar, p. 136), an <strong>arkose</strong> is strictly defined as a sandstone containing <strong>more than 25% feldspar</strong> (mostly pink potash feldspars such as microcline and orthoclase). This gives arkose its typical pink, red, or salmon-colored appearance.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Micas</div>
          <p>Micas (biotite and muscovite) may occur as subordinate accessories (typically 1% to 5%) in arkosic sandstones, but never exceed 25%. A sandstone rich in micas is termed a micaceous sandstone or flagstone.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Amphiboles</div>
          <p>Amphiboles are unstable ferromagnesian minerals that weather rapidly during surface transport. They occur only in trace quantities as heavy mineral accessories, never exceeding 25% in sandstones.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Chlorite</div>
          <p>Chlorite is a common green sheet-silicate mineral found in the matrix of <em>greywackes</em> and low-grade metamorphic rocks. It does not constitute the framework grain defining an arkose.</p>
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
              <th>Sandstone Type</th>
              <th>Essential Diagnostic Mineral</th>
              <th>Compositional Threshold</th>
              <th>Matrix Abundance</th>
              <th>Color & Appearance</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Arkose</strong> (Option C)</td><td><strong>Feldspar</strong> (Microcline / Orthoclase)</td><td><strong>&gt; 25% Feldspar</strong></td><td>&lt; 15% (Clean Arenite)</td><td>Pink, reddish, or buff (salmon-pink)</td></tr>
            <tr><td>Subarkose</td><td>Feldspar</td><td>5% &ndash; 25% Feldspar</td><td>&lt; 15%</td><td>Pale yellow to pinkish-grey</td></tr>
            <tr><td>Quartzarenite (Orthoquartzite)</td><td>Quartz</td><td>&gt; 95% Monocrystalline Quartz</td><td>&lt; 15%</td><td>White, light grey, or vitreous</td></tr>
            <tr><td>Greywacke (Wacke)</td><td>Clay matrix + Quartz + Feldspar + Lithics</td><td>&gt; 15% Clay/Chlorite Matrix</td><td>15% &ndash; 50% Matrix</td><td>Dark greenish-grey to black ('dirty sand')</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What two climatic/tectonic factors preserve high percentages of feldspar in arkose against chemical weathering?</div>
        <div class="pq-ans">Answer: Arid / frigid cold climate and high topographic relief with rapid tectonic uplift and burial.</div>
        <div class="pq-exp">Chemical weathering hydrolyzes feldspars to clay; an arid or freezing climate, combined with rapid erosion and burial, halts hydrolysis.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which potash feldspar is recognized by its distinctive 'tartan' or 'cross-hatched' twinning in arkose thin sections?</div>
        <div class="pq-ans">Answer: Microcline</div>
        <div class="pq-exp">Microcline exhibits prominent gridiron (albite + pericline) cross-hatched twinning under crossed nicols, diagnostic of granitic basement provenance.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What prominent Indian sedimentary formation contains basal arkosic sandstones overlying Archaean granitic basements?</div>
        <div class="pq-ans">Answer: The Talchir Formation (basal Gondwana Supergroup) and Cuddapah Basin basal Gulcheru quartzites/arkoses.</div>
        <div class="pq-exp">Glacial and periglacial erosion of granites during early Gondwana times formed boulder beds and feldspathic arkoses.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the difference between an arkosic arenite and an arkosic wacke?</div>
        <div class="pq-ans">Answer: Arkosic arenite has &lt;15% fine matrix; arkosic wacke has 15% to 50% fine matrix.</div>
        <div class="pq-exp">Gilbert (1954) and Dott (1964) divide all sandstones at the 15% matrix boundary into arenites and wackes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is 'grus' in weathering petrology?</div>
        <div class="pq-ans">Answer: Coarse, angular granitic sand produced by in-situ granular disintegration of granite, forming the direct precursor to arkose.</div>
        <div class="pq-exp">Mechanical spalling of quartz and feldspar crystals in desert granites generates grus, which upon transport lithifies into arkose.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What provenance field on the Dickinson (1985) QFL diagram plots typical arkoses?</div>
        <div class="pq-ans">Answer: Continental Block Provenance (specifically Basement Uplift)</div>
        <div class="pq-exp">Dickinson's triangular provenance model links arkoses directly to fault-bounded continental basement uplifts exposing granitic plutons.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What cement commonly binds arkose grains giving it a red or brownish color?</div>
        <div class="pq-ans">Answer: Hematite (iron oxide) and Calcite</div>
        <div class="pq-exp">Oxidizing continental groundwater precipitates iron oxide coatings (hematite) around feldspar grains, producing red-bed arkoses.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the feldspar threshold for classifying a sandstone as a 'subarkose'?</div>
        <div class="pq-ans">Answer: 5% to 25% feldspar</div>
        <div class="pq-exp">Subarkose occupies the transitional field between quartzarenite (&lt;5% feldspar) and true arkose (&gt;25% feldspar).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q092: Silt Grade Particle Size Range (1/16 mm to 1/256 mm)
# -----------------------------------------------------------------------------
def gen_q092():
    q_num = 92
    filename = "Q092_Silt_Grade_Detrital_Sediments_Size_Range_1_16_To_1_256_mm_Complete_Guide.html"
    title = "Q092: Udden-Wentworth Scale - Silt Grade Grain Size Range"
    badge = "OPSC 2019 Geology Paper-II • Question 92 • Sedimentary Petrology"
    h1_title = "The Udden-Wentworth Grain-Size Scale: Silt Grade Detrital Sediments (1/16 to 1/256 mm)"
    meta_text = "<strong>Topic:</strong> Clastic Sediment Granulometry • <strong>Key Concept:</strong> Udden-Wentworth Logarithmic Scale & Phi Units • <strong>Textbooks:</strong> C.K. Wentworth (1922); W.C. Krumbein (1934); K.M. Bangar (p. 131)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Udden-Wentworth Scale & Silt Fraction</div>
      <p>The quantitative classification of detrital (clastic) sediments is based on the geometric particle-size scale formulated by J.A. Udden (1898) and modified by <strong>Chester K. Wentworth (1922)</strong>. In 1934, <strong>W.C. Krumbein</strong> introduced the logarithmic transformation <strong>phi ($\phi$) scale</strong> ($\phi = -\log_2 d_{\text{mm}}$) to enable rigorous statistical analysis:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Grain Size Grade</th>
              <th>Millimeter Range ($d_{\text{mm}}$)</th>
              <th>Micrometer Range ($\mu\text{m}$)</th>
              <th>Krumbein Phi Range ($\phi$)</th>
              <th>Indurated Sedimentary Rock</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Gravel / Pebble</td>
              <td>&gt; 2 mm</td>
              <td>&gt; 2000 $\mu\text{m}$</td>
              <td>$&lt; -1.0\ \phi$</td>
              <td>Conglomerate / Breccia</td>
            </tr>
            <tr>
              <td>Sand (Very Coarse to Very Fine)</td>
              <td>2 mm &ndash; 1/16 mm</td>
              <td>2000 &ndash; 62.5 $\mu\text{m}$</td>
              <td>$-1.0\ \phi$ to $+4.0\ \phi$</td>
              <td>Sandstone (Arenite / Wacke)</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>SILT GRADE (Option A)</strong></td>
              <td><strong>1/16 mm to 1/256 mm</strong></td>
              <td><strong>62.5 to 3.9 $\mu\text{m}$</strong></td>
              <td><strong>$+4.0\ \phi$ to $+8.0\ \phi$</strong></td>
              <td><strong>Siltstone</strong></td>
            </tr>
            <tr>
              <td>&bull; Coarse Silt</td>
              <td>1/16 &ndash; 1/32 mm</td>
              <td>62.5 &ndash; 31.2 $\mu\text{m}$</td>
              <td>$+4.0\ \phi$ to $+5.0\ \phi$</td>
              <td>Coarse Siltstone</td>
            </tr>
            <tr>
              <td>&bull; Medium Silt</td>
              <td>1/32 &ndash; 1/64 mm</td>
              <td>31.2 &ndash; 15.6 $\mu\text{m}$</td>
              <td>$+5.0\ \phi$ to $+6.0\ \phi$</td>
              <td>Medium Siltstone</td>
            </tr>
            <tr>
              <td>&bull; Fine Silt</td>
              <td>1/64 &ndash; 1/128 mm</td>
              <td>15.6 &ndash; 7.8 $\mu\text{m}$</td>
              <td>$+6.0\ \phi$ to $+7.0\ \phi$</td>
              <td>Fine Siltstone</td>
            </tr>
            <tr>
              <td>&bull; Very Fine Silt</td>
              <td>1/128 &ndash; 1/256 mm</td>
              <td>7.8 &ndash; 3.9 $\mu\text{m}$</td>
              <td>$+7.0\ \phi$ to $+8.0\ \phi$</td>
              <td>Very Fine Siltstone</td>
            </tr>
            <tr>
              <td>Clay Grade</td>
              <td>&lt; 1/256 mm</td>
              <td>&lt; 3.9 $\mu\text{m}$</td>
              <td>$&gt; +8.0\ \phi$</td>
              <td>Claystone / Shale / Mudstone</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "According to the Wentworth grade scale, <strong>silt</strong> comprises all mineral fragments with diameters between <strong>1/16 mm and 1/256 mm</strong> (or 0.0625 mm to 0.0039 mm). Particles larger than 1/16 mm are sand, while particles finer than 1/256 mm are classified as clay. Silt-grade grains are barely visible under a hand lens but feel gritty between the fingers or teeth, distinguishing them from smooth, plastic clays."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Rocks, pp. 130&ndash;132)</div>
      </div>

      <div class="formula-box">
        $$\text{Krumbein Phi Transformation: } \phi = -\log_2 (d_{\text{mm}})$$
        $$\text{Upper Limit of Silt: } d = \frac{1}{16}\text{ mm} = 0.0625\text{ mm} \implies \phi = -\log_2(2^{-4}) = \mathbf{+4.0\ \phi}$$
        $$\text{Lower Limit of Silt: } d = \frac{1}{256}\text{ mm} = 0.0039\text{ mm} \implies \phi = -\log_2(2^{-8}) = \mathbf{+8.0\ \phi}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q092/udden_wentworth_grain_size_scale_silt_grade.png" alt="Udden Wentworth Grain Size Scale Silt Grade" class="figure-img">
        <div class="figure-caption">Figure 92: The Udden-Wentworth grain size scale highlighting the exact Silt Grade range (1/16 mm to 1/256 mm / +4 phi to +8 phi) bounded by Sand and Clay.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 92</div>
        <div class="raw-q-text">The silt grade detrital sediments would have a size range of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 1/16 mm to 1/256 mm</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Less than 1/256 mm</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 1/16 mm to 2 mm</div>
          <div class="raw-opt"><span class="opt-letter">D</span> 2 mm to 1 mm</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (1/16 mm to 1/256 mm)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">1/16 mm to 1/256 mm</div>
          <p>By international geological standards (Wentworth, 1922; Krumbein, 1934; Pettijohn; Bangar), the <strong>silt grade</strong> detrital sediment is defined as particles ranging in diameter from <strong>1/16 mm to 1/256 mm</strong> (0.0625 mm to 0.0039 mm, or $+4\phi$ to $+8\phi$).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Less than 1/256 mm</div>
          <p>Particles having a diameter less than 1/256 mm ($< 0.0039\text{ mm}$, or $> +8\phi$) belong to the <strong>clay grade</strong>, which consists of colloidal phyllosilicates and mud.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">1/16 mm to 2 mm</div>
          <p>The size range from 1/16 mm to 2 mm defines the <strong>sand grade</strong> (from very fine sand at 0.0625 mm up to very coarse sand at 2 mm), not silt.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">2 mm to 1 mm</div>
          <p>This range corresponds exclusively to <strong>very coarse sand</strong> (1 mm to 2 mm), which lies near the gravel boundary.</p>
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
              <th>Wentworth Grade</th>
              <th>Millimeter Limits</th>
              <th>Micrometer ($\mu\text{m}$) Limits</th>
              <th>Phi ($\phi$) Range</th>
              <th>Sensory / Field Identification</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Gravel</td><td>&gt; 2 mm</td><td>&gt; 2000 $\mu\text{m}$</td><td>$&lt; -1.0\ \phi$</td><td>Distinct pebbles visible to naked eye</td></tr>
            <tr><td>Sand</td><td>2 mm &ndash; 1/16 mm</td><td>2000 &ndash; 62.5 $\mu\text{m}$</td><td>$-1.0\ \phi$ to $+4.0\ \phi$</td><td>Gritty feel on fingers; grains easily visible</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Silt (Option A)</strong></td><td><strong>1/16 mm &ndash; 1/256 mm</strong></td><td><strong>62.5 &ndash; 3.9 $\mu\text{m}$</strong></td><td><strong>$+4.0\ \phi$ to $+8.0\ \phi$</strong></td><td>Gritty on teeth, smooth on fingers; barely visible under 10x lens</td></tr>
            <tr><td>Clay</td><td>&lt; 1/256 mm</td><td>&lt; 3.9 $\mu\text{m}$</td><td>$&gt; +8.0\ \phi$</td><td>Completely smooth/buttery on teeth; plastic when wet</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the phi value ($\phi$) of a grain having a diameter of exactly 0.0625 mm (1/16 mm)?</div>
        <div class="pq-ans">Answer: $+4.0\ \phi$</div>
        <div class="pq-exp">$\phi = -\log_2(0.0625) = -\log_2(2^{-4}) = -(-4) = +4.0\ \phi$. This marks the exact sand-silt boundary.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What aeolian wind-blown deposit consists almost entirely of well-sorted quartz silt?</div>
        <div class="pq-ans">Answer: Loess</div>
        <div class="pq-exp">Loess is an unstratified, buff-colored, calcareous deposit of wind-blown glacial or peridesert quartz silt (20 to 50 $\mu\text{m}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the primary mineral constituent of detrital silt?</div>
        <div class="pq-ans">Answer: Quartz ($SiO_2$)</div>
        <div class="pq-exp">Quartz is chemically inert and mechanically durable; physical abrasion crushes quartz grains down to a natural cleavage limit of ~20 to 4 $\mu\text{m}$ (silt size).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How can a field geologist immediately distinguish siltstone from claystone without a microscope?</div>
        <div class="pq-ans">Answer: The 'bite test' (chewing a tiny speck): siltstone feels distinctly gritty between the teeth, whereas claystone feels buttery smooth.</div>
        <div class="pq-exp">Human teeth are exceptionally sensitive tactile sensors capable of detecting particles down to ~10 $\mu\text{m}$ (silt), whereas clay (<4 $\mu\text{m}$) cannot be felt.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What physical law governs the settling velocity of silt particles in calm water?</div>
        <div class="pq-ans">Answer: Stokes' Law ($v = \frac{2}{9}\frac{(\rho_s - \rho_f) g r^2}{\eta}$)</div>
        <div class="pq-exp">Particles smaller than 0.1 mm (including all silt and clay) settle via laminar viscous drag described by Stokes' Law.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the millimeter size equivalent of $-1\ \phi$?</div>
        <div class="pq-ans">Answer: 2.0 mm (the gravel-sand boundary)</div>
        <div class="pq-exp">$d = 2^{-\phi} = 2^{-(-1)} = 2^1 = 2.0\text{ mm}$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is mud in sedimentary terminology?</div>
        <div class="pq-ans">Answer: A mixture of silt and clay grade particles (all detritus finer than 1/16 mm).</div>
        <div class="pq-exp">Mudrock / mudstone is the collective term for fine-grained clastic rocks containing both silt (1/16-1/256 mm) and clay (<1/256 mm).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the millimeter diameter of the boundary separating granules from pebbles in Wentworth's scale?</div>
        <div class="pq-ans">Answer: 4.0 mm</div>
        <div class="pq-exp">Granules range from 2 mm to 4 mm; pebbles range from 4 mm to 64 mm.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q093: Clay Galls (Hardened Clay Leaves in Sand)
# -----------------------------------------------------------------------------
def gen_q093():
    q_num = 93
    filename = "Q093_Leaves_Of_Hardened_Clay_In_Sand_Are_Clay_Galls_Complete_Guide.html"
    title = "Q093: Sedimentary Structures - Clay Galls (Mud Rip-Up Clasts)"
    badge = "OPSC 2019 Geology Paper-II • Question 93 • Sedimentary Petrology"
    h1_title = "Clay Galls (Mud Rip-Up Clasts): Genesis, Morphology, and Sedimentary Significance"
    meta_text = "<strong>Topic:</strong> Intraformational Structures • <strong>Key Concept:</strong> Desiccation, Mud-Flake Ripping & Lenticular Redeposition • <strong>Textbooks:</strong> F.J. Pettijohn (1975); K.M. Bangar (p. 134); G.B. Mahapatra"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Genesis & Morphology of Clay Galls</div>
      <p>In clastic sedimentology, <strong>clay galls</strong> (also termed <em>mud galls</em>, <em>mud rip-up clasts</em>, or <em>intraformational mud chips</em>) are flat, lenticular, or leaf-like structures of hardened, desiccated clay embedded within beds of sandstone or siltstone. They represent intraformational clasts produced through a distinctive cyclical sedimentary process:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Genesis Stage</th>
              <th>Physical / Environmental Action</th>
              <th>Sedimentary Feature Formed</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1. Low-Water Deposition</td>
              <td>Quiescent settling in temporary pools, floodplains, lagoons, or tidal mudflats during low-water stage.</td>
              <td>Thin lamina of coherent, fine-grained plastic mud/clay.</td>
            </tr>
            <tr>
              <td>2. Subaerial Desiccation</td>
              <td>Subaerial exposure to sun and atmospheric drying; clay contracts, forming polygonal mudcracks.</td>
              <td>Hardened, curled-up thin flakes resembling dried leaves (<em>leaves of clay</em>).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>3. Turbulent Inundation</strong></td>
              <td>Sudden high-energy flood surge (crevasse splay, storm wave, or flash flood) carrying abrasive sand.</td>
              <td><strong>Rips up the dried clay flakes, rolls and rounds them slightly, and deposits them in sand</strong>.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>4. Compaction & Lithification</strong></td>
              <td>Overburden pressure flattens the soft mud clasts into disc-like or lenticular shapes within the sandstone matrix.</td>
              <td><strong>★ CLAY GALLS (Option D) ★</strong> (often weathering out into hollow cavities on exposed rock faces).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Leaves of hardened clay deposited in a sand or similar sediment as flat or lens-shaped structures are called <strong>clay galls</strong> (or mud galls). They are formed when mud layers dry out under the sun, crack into curled flakes, and are subsequently torn up and swept away by sudden torrents of sand-laden water. In weathered sandstone outcrops, clay galls easily wash out, leaving characteristic pitted or hollow depressions."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Structures, p. 134)</div>
      </div>

      <div class="formula-box">
        $$\text{Cycle of Clay Gall Formation: Mud Layer } \xrightarrow{\text{Sun Desiccation}} \text{Curled Clay Leaves} \xrightarrow{\text{Flood Surge}} \mathbf{Clay\ Galls\ (Lenticular\ Clasts\ in\ Sand)}$$
        $$\text{Sedimentary Classification: } \mathbf{Intraformational\ Rip\text{-}Up\ Clasts \equiv Clay\ Galls\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q093/clay_galls_mud_rip_up_clasts_sandstone.png" alt="Clay Galls Mud Rip Up Clasts Sandstone" class="figure-img">
        <div class="figure-caption">Figure 93: Schematic cross-section of sandstone containing flat, lens-shaped clay galls (mud rip-up clasts) formed by desiccation, erosion, and rapid redeposition.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 93</div>
        <div class="raw-q-text">The leaves of hardened clay deposited in a sand or similar sediment as flat or lense shaped structure are called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Clay flakes</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Clay balls</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Clay stones</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Clay galls</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Clay galls)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Clay galls</div>
          <p>By standard textbook definition (Pettijohn, 1975; Bangar, p. 134; G.B. Mahapatra), the flat or lens-shaped fragments of hardened, desiccated clay leaves enclosed within a sandstone matrix are formally known as <strong>clay galls</strong> (or mud galls). They are classic indicators of shallow-water, ephemeral, or subaerially exposed environments.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Clay flakes</div>
          <p>'Clay flakes' refers to the uncompacted, loose microscopic phyllosilicate platelets or desiccated surface crust fragments before being transported and incorporated into an indurated sandstone as galls.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Clay balls</div>
          <p>Clay balls (specifically <em>armored mud balls</em>) are spherical or subspherical balls of sticky mud rolled along a streambed that pick up an outer armour of pebbles and sand grains. They are spherical, not flat or lens-shaped.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Clay stones</div>
          <p>Claystone is an indurated, massive, non-fissile sedimentary rock composed entirely of clay-sized particles, not a discrete lenticular inclusion within sandstone.</p>
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
              <th>Mud-Derived Structure</th>
              <th>Morphology & Shape</th>
              <th>Transport Mechanism</th>
              <th>Depositional Host</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Clay Galls (Option D)</strong></td><td>Flat, disc-like, or lenticular 'leaves'</td><td>Ripped up by sudden flood surge and deposited</td><td>Sandstone / Siltstone beds</td></tr>
            <tr><td>Armored Mud Balls</td><td>Spherical to subspherical balls</td><td>Rolled along gravelly riverbeds; armoured with pebbles</td><td>High-energy fluvial gravels</td></tr>
            <tr><td>Mud Cracks (Desiccation cracks)</td><td>Polygonal network of V-shaped fissures</td><td>In-situ shrinkage due to subaerial drying</td><td>Mudstone / Shale surfaces</td></tr>
            <tr><td>Flame Structures</td><td>Tongue-like or flame-like upward projections</td><td>Hydrodynamic liquefaction under sediment load</td><td>Boundary between mud and overlying sand</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What type of conglomerate is formed when a current tears up semi-consolidated clay galls from its own bed and redeposits them locally?</div>
        <div class="pq-ans">Answer: Intraformational Conglomerate (or Intraformational Mud-Pebble Conglomerate)</div>
        <div class="pq-exp">Intraformational conglomerates consist of clasts derived from within the same depositional basin, virtually contemporaneous with the host sediment.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What happens to clay galls on exposed weathered sandstone cliffs?</div>
        <div class="pq-ans">Answer: They weather and wash out rapidly, leaving hollow depressions (pitted sandstone or 'tafoni-like' cavities).</div>
        <div class="pq-exp">Clay is much softer and more easily eroded by rainwater than the surrounding quartz sandstone, creating a pitted outcrop surface.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What environmental condition is conclusively demonstrated by the presence of clay galls in a fluvial sandstone?</div>
        <div class="pq-ans">Answer: Episodic drying (subaerial exposure) followed by high-energy turbulent flooding.</div>
        <div class="pq-exp">Clay galls require subaerial desiccation to harden the mud flakes so they do not immediately disaggregate into suspension when flooded.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is an armored mud ball?</div>
        <div class="pq-ans">Answer: A chunk of sticky clay rolled along a torrential streambed that becomes coated with pebbles, gravel, and coarse sand.</div>
        <div class="pq-exp">Armored mud balls form in flash floods and mountain streams where cohesive mud rolls across pebble-covered bars.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why do clay galls orient themselves parallel to the bedding planes?</div>
        <div class="pq-ans">Answer: Hydrodynamic settling and post-depositional lithostatic compaction flatten them horizontally along bedding.</div>
        <div class="pq-exp">Flat disc-shaped clasts settle with their maximum projection area parallel to flow and are further flattened during burial compaction.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the difference between an intraformational and an extraformational clast?</div>
        <div class="pq-ans">Answer: Intraformational clasts originate from within the depositional basin; extraformational clasts are eroded from outside source rocks.</div>
        <div class="pq-exp">Clay galls are intraformational; granitic or quartzite pebbles transported from mountains are extraformational.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is another common sedimentological term for clay galls in turbidites?</div>
        <div class="pq-ans">Answer: Rip-up clasts (or shale rip-ups)</div>
        <div class="pq-exp">High-velocity turbidity currents erode the underlying muddy sea floor, incorporating shale rip-up clasts into the basal $T_a$ division.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which Gondwana formation in India frequently displays clay galls in cross-bedded river sandstones?</div>
        <div class="pq-ans">Answer: The Barakar Formation (Damodar and Mahanadi Valley basins)</div>
        <div class="pq-exp">Braided channel Barakar sandstones commonly carry intraformational shale clasts and clay galls derived from cannibalized overbank muds.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q094: Cobble Size Range (64 mm to 256 mm)
# -----------------------------------------------------------------------------
def gen_q094():
    q_num = 94
    filename = "Q094_Rounded_Clast_64_To_256_mm_Is_Cobble_Complete_Guide.html"
    title = "Q094: Udden-Wentworth Scale - Cobble Clast Classification"
    badge = "OPSC 2019 Geology Paper-II • Question 94 • Sedimentary Petrology"
    h1_title = "Coarse Clast Granulometry: Classification of Cobbles (64 mm to 256 mm)"
    meta_text = "<strong>Topic:</strong> Conglomerate & Gravel Granulometry • <strong>Key Concept:</strong> Udden-Wentworth Size Limits (Cobble vs Pebble vs Boulder) • <strong>Textbooks:</strong> C.K. Wentworth (1922); F.J. Pettijohn; K.M. Bangar (p. 131)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Coarse Clastic Granulometry</div>
      <p>In the Udden-Wentworth classification of coarse detrital sediments (Wentworth, 1922), rudaceous (gravel-grade) clasts ($> 2\text{ mm}$) are precisely categorized based on intermediate diameter measurements. A rounded to sub-rounded clast with a diameter between <strong>64 mm and 256 mm</strong> is designated as a <strong>Cobble</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Clast Grade</th>
              <th>Millimeter Diameter Range</th>
              <th>Inches Range (Approx.)</th>
              <th>Krumbein Phi Range ($\phi$)</th>
              <th>Lithified Rock Equivalent (Rounded Clasts)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Boulder</td>
              <td>&gt; 256 mm</td>
              <td>&gt; 10.1 inches</td>
              <td>$&lt; -8.0\ \phi$</td>
              <td>Boulder Conglomerate</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>COBBLE (Option C)</strong></td>
              <td><strong>64 mm to 256 mm</strong></td>
              <td><strong>2.5 to 10.1 inches</strong></td>
              <td><strong>$-6.0\ \phi$ to $-8.0\ \phi$</strong></td>
              <td><strong>Cobble Conglomerate</strong></td>
            </tr>
            <tr>
              <td>Pebble</td>
              <td>4 mm to 64 mm</td>
              <td>0.16 to 2.5 inches</td>
              <td>$-2.0\ \phi$ to $-6.0\ \phi$</td>
              <td>Pebble Conglomerate</td>
            </tr>
            <tr>
              <td>&bull; Coarse Pebble</td>
              <td>16 mm to 64 mm</td>
              <td>0.63 to 2.5 inches</td>
              <td>$-4.0\ \phi$ to $-6.0\ \phi$</td>
              <td>Coarse Pebble Conglomerate</td>
            </tr>
            <tr>
              <td>&bull; Fine Pebble</td>
              <td>4 mm to 16 mm</td>
              <td>0.16 to 0.63 inches</td>
              <td>$-2.0\ \phi$ to $-4.0\ \phi$</td>
              <td>Fine Pebble Conglomerate</td>
            </tr>
            <tr>
              <td>Granule</td>
              <td>2 mm to 4 mm</td>
              <td>0.08 to 0.16 inches</td>
              <td>$-1.0\ \phi$ to $-2.0\ \phi$</td>
              <td>Granule Conglomerate / Grit</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "In petrology, coarse detrital fragments are classified by size. A <strong>boulder</strong> has a diameter greater than 256 mm. A <strong>cobble</strong> has a diameter ranging from <strong>64 mm to 256 mm</strong> (roughly grapefruit to human-head size). A <strong>pebble</strong> ranges from 4 mm to 64 mm, and a <strong>granule</strong> from 2 mm to 4 mm. A sedimentary rock formed of consolidated, rounded cobbles is a cobble conglomerate."
        <div class="quote-author">&mdash; F.J. Pettijohn, <em>Sedimentary Rocks</em> (Gravels and Conglomerates, p. 153)</div>
      </div>

      <div class="formula-box">
        $$\text{Udden-Wentworth Size Rule: } \mathbf{64\text{ mm} \le \text{Diameter} < 256\text{ mm}} \implies \mathbf{COBBLE\ (Option\ C)}$$
        $$\phi = -\log_2(64) = -6\ \phi \quad \text{to} \quad \phi = -\log_2(256) = -8\ \phi$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q094/clast_size_classification_cobble_pebble_boulder.png" alt="Clast Size Classification Cobble Pebble Boulder" class="figure-img">
        <div class="figure-caption">Figure 94: Clast size scale comparing Boulder (>256 mm), Cobble (64 to 256 mm), Pebble (4 to 64 mm), and Granule (2 to 4 mm).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 94</div>
        <div class="raw-q-text">Rounded to sub-rounded clast with a diameter between 64 and 256 mm is generally known as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Gravel</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Pebble</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Cobble</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Boulder</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Cobble)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Cobble</div>
          <p>By Wentworth's (1922) authoritative sedimentological scale, clasts having a diameter between <strong>64 mm and 256 mm</strong> are uniquely designated as <strong>cobbles</strong>. Rounded clasts in this size range form <em>cobble conglomerates</em>, typical of high-energy braided rivers and storm-tossed beaches.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Gravel</div>
          <p>'Gravel' is an overarching collective term encompassing all unconsolidated detrital clasts larger than 2 mm in diameter (including granules, pebbles, cobbles, and boulders), not the specific 64&ndash;256 mm size class.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Pebble</div>
          <p>A pebble is strictly defined as a clast having a diameter between <strong>4 mm and 64 mm</strong>. Clasts larger than 64 mm are cobbles.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Boulder</div>
          <p>A boulder is defined as a clast with a diameter <strong>greater than 256 mm</strong> ($> 10.1\text{ inches}$).</p>
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
              <th>Grain Size Term</th>
              <th>Diameter Range</th>
              <th>Natural Analog Example</th>
              <th>Lithified Sedimentary Rock (Rounded)</th>
              <th>Lithified Sedimentary Rock (Angular)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Boulder</td><td>&gt; 256 mm</td><td>Basketball to giant car-sized blocks</td><td>Boulder Conglomerate</td><td>Boulder Breccia</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Cobble (Option C)</strong></td><td><strong>64 &ndash; 256 mm</strong></td><td>Grapefruit / coconut / fist sized</td><td>Cobble Conglomerate</td><td>Cobble Breccia</td></tr>
            <tr><td>Pebble</td><td>4 &ndash; 64 mm</td><td>Marble to walnut sized</td><td>Pebble Conglomerate</td><td>Pebble Breccia</td></tr>
            <tr><td>Granule</td><td>2 &ndash; 4 mm</td><td>Match head / coarse grit sized</td><td>Granule Conglomerate (Grit)</td><td>Granule Breccia</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between a conglomerate and a sedimentary breccia?</div>
        <div class="pq-ans">Answer: A conglomerate is composed of rounded to sub-rounded clasts; a breccia is composed of sharp, angular clasts.</div>
        <div class="pq-exp">Rounding reflects prolonged fluvial or beach transport; angularity indicates minimal transport (talus scree, faulting).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What hydrodynamic transport regime is required to transport 64 to 256 mm cobbles?</div>
        <div class="pq-ans">Answer: High-energy upper flow regime (torrential flash floods, steep mountain streams, or severe marine storm breakers).</div>
        <div class="pq-exp">Hjulstr&ouml;m's diagram demonstrates that entraining and rolling cobbles requires bottom current velocities exceeding 2 to 4 m/s.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is an oligomictic conglomerate vs. a polymictic conglomerate?</div>
        <div class="pq-ans">Answer: Oligomictic contains clasts of a single rock type (e.g., pure vein quartz); polymictic contains diverse clasts (granite, basalt, quartzite).</div>
        <div class="pq-exp">Oligomictic conglomerates reflect intense chemical weathering destroying unstable clasts; polymictic reflects rapid mechanical erosion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the term for a conglomerate where clasts touch each other, with sand/mud filling the interstices?</div>
        <div class="pq-ans">Answer: Clast-supported (or Orthoconglomerate)</div>
        <div class="pq-exp">When clasts float in a muddy matrix without touching, it is matrix-supported (paraconglomerate or diamictite).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is imbrication in cobble gravels?</div>
        <div class="pq-ans">Answer: The preferred shingle-like overlapping alignment of flat cobbles dipping gently upstream against the current.</div>
        <div class="pq-exp">Imbrication provides a definitive palaeocurrent vector: the long $a-b$ planes dip upstream into the paleoflow.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the phi ($\phi$) value corresponding to the 64 mm cobble-pebble boundary?</div>
        <div class="pq-ans">Answer: $-6.0\ \phi$</div>
        <div class="pq-exp">$\phi = -\log_2(64) = -\log_2(2^6) = -6.0\ \phi$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What famous Siwalik group member in the Himalayan foothills consists of massive boulder and cobble conglomerates?</div>
        <div class="pq-ans">Answer: The Upper Siwalik Boulder Conglomerate Formation (Pleistocene)</div>
        <div class="pq-exp">The Upper Siwalik Boulder Conglomerate represents syn-orogenic alluvial fans shed off the rising Greater and Lesser Himalayas.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is Zingg's clast shape classification based on?</div>
        <div class="pq-ans">Answer: Ratios of the three orthogonal axes: $a$ (long), $b$ (intermediate), and $c$ (short).</div>
        <div class="pq-exp">Zingg (1935) categorized cobbles into Equant (spherical), Oblate (discoid), Prolate (rod-shaped), and Triaxial (bladed).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q095: Current Bedding (Cross-Bedding)
# -----------------------------------------------------------------------------
def gen_q095():
    q_num = 95
    filename = "Q095_Series_Of_Inclined_Bedding_Planes_Are_Current_Beds_Complete_Guide.html"
    title = "Q095: Sedimentary Structures - Current Bedding (Cross-Stratification)"
    badge = "OPSC 2019 Geology Paper-II • Question 95 • Sedimentary Petrology"
    h1_title = "Cross-Stratification: Architecture, Mechanics, and Significance of Current Beds"
    meta_text = "<strong>Topic:</strong> Primary Sedimentary Structures • <strong>Key Concept:</strong> Inclined Foreset Lamination & Palaeocurrent Direction • <strong>Textbooks:</strong> F.J. Pettijohn (1975); K.M. Bangar (p. 132); Sam Boggs Jr. (2014)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Mechanics of Current Bedding (Cross-Stratification)</div>
      <p><strong>Current bedding</strong> (also known as <em>cross-bedding</em>, <em>cross-stratification</em>, or <em>false bedding</em>) is one of the most fundamental primary depositional structures in sedimentary geology. It is defined as a series of inclined internal laminations (foresets) deposited at an angle to the main horizontal or master bedding planes, produced by the migration of ripples, sand waves, or dunes under moving water or wind currents:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Structural Element</th>
              <th>Morphology & Geometric Attitude</th>
              <th>Hydrodynamic Mechanism</th>
              <th>Geological / Geopetal Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Topset Beds</td>
              <td>Gently dipping or sub-horizontal upper strata; frequently truncated by erosion.</td>
              <td>Transport of bedload across the stoss side of migrating dunes.</td>
              <td>Top truncation indicates 'younging' / stratigraphic top (geopetal indicator).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>CURRENT BEDS (Foresets)</strong> (Option B)</td>
              <td><strong>Inclined planes dipping at angles up to 30&ndash;35&deg; (angle of repose) in the direction of current flow</strong>.</td>
              <td>Avalanching and grainfall down the steep lee side of migrating sand dunes or ripples.</td>
              <td><strong>Dip direction provides the definitive palaeocurrent flow vector</strong>.</td>
            </tr>
            <tr>
              <td>Bottomset Beds</td>
              <td>Sub-horizontal lower strata meeting the base tangentially (asymptotic contact).</td>
              <td>Suspension settling of finer grains in the flow separation zone at the dune toe.</td>
              <td>Tangential curved base proves the right-side-up (normal) stratigraphic orientation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "When a series of inclined bedding planes show an angular relationship to the main bedding planes and to the direction of current flow, they are termed <strong>current beds</strong> (or cross-beds). Formed by the migration of sand waves, dunes, or ripples in flowing water or wind, the inclined foresets dip down-current in the direction of flow. Current bedding is invaluable for determining palaeocurrent directions and identifying overturned beds."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Structures, p. 132)</div>
      </div>

      <div class="formula-box">
        $$\text{Current Bedding Dip Angle: } \theta \le \theta_{\text{angle of repose}} \approx 30^\circ\text{--}34^\circ \quad (\text{Subaqueous: } 20^\circ\text{--}30^\circ;\ \text{Aeolian: up to } 35^\circ)$$
        $$\text{Palaeocurrent Vector} \equiv \text{Down-dip Azimuth of Foreset (Current Bed) Laminae}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q095/current_bedding_cross_stratification_geometry.png" alt="Current Bedding Cross Stratification Geometry" class="figure-img">
        <div class="figure-caption">Figure 95: Cross-sectional architecture of current bedding, showing inclined foreset current beds dipping down-current between horizontal master bedding planes.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 95</div>
        <div class="raw-q-text">If a series of inclined bedding planes showing some angular relationship to the direction of current flow, then they are generally called as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Gradient beds</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Current beds</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Dipping beds</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Convolute beds</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Current beds)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Current beds</div>
          <p>By classical geological terminology (Bangar, p. 132; Mahapatra, p. 182; Pettijohn), inclined bedding planes formed within a larger sedimentary stratum at an angle to the current flow and the main horizontal bedding are formally termed <strong>current beds</strong> (or cross-beds / false beds).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Gradient beds</div>
          <p>'Gradient beds' is not a recognized geological term. The vertical variation in grain size is termed <em>graded bedding</em>, which consists of horizontal beds, not inclined cross-strata.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Dipping beds</div>
          <p>'Dipping beds' is a general structural geology term for any tilted rock stratum inclined to the horizontal plane due to tectonic deformation (tilting or folding), not a primary sedimentary current-formed structure.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Convolute beds</div>
          <p>Convolute bedding consists of intensely crumpled, folded, or deformed laminations formed by soft-sediment syn-sedimentary deformation, not regular inclined current beds.</p>
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
              <th>Cross-Bedding Type</th>
              <th>Bounding Geometry</th>
              <th>Crest Shape of Bedform</th>
              <th>Typical Sedimentary Environment</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Planar Cross-Bedding</strong></td><td>Planar parallel master surfaces</td><td>2D straight-crested sand dunes/bars</td><td>Fluvial sand bars, delta front sheets</td></tr>
            <tr><td><strong>Trough Cross-Bedding</strong></td><td>Curved, scoop-shaped erosional troughs</td><td>3D sinuous/lunate dunes</td><td>Braided river channels, tidal sand ridges</td></tr>
            <tr><td><strong>Herringbone Cross-Bedding</strong></td><td>Alternating opposing sets (180&deg; reversal)</td><td>Bipolar tidal bedforms</td><td>Intertidal flats, tidal inlets</td></tr>
            <tr><td><strong>Hummocky Cross-Stratification (HCS)</strong></td><td>Undulating hummocks and swales (&lt;15&deg;)</td><td>Storm wave oscillatory currents</td><td>Shallow marine shelf (between fairweather and storm wave base)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. How can cross-bedding be used as a 'way-up' (geopetal) structure to identify overturned strata?</div>
        <div class="pq-ans">Answer: Foreset beds are truncated sharply at the top by erosion and curve tangentially (asymptotically) into the bottomset at the base.</div>
        <div class="pq-exp">If the tangential curves are at the top and the sharp truncations are at the bottom, the bed has been tectonically overturned.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What type of cross-bedding is characterized by alternating sets that dip in opposite directions (180° apart)?</div>
        <div class="pq-ans">Answer: Herringbone cross-bedding</div>
        <div class="pq-exp">Herringbone structure forms in intertidal environments where flood currents and ebb currents reverse flow directions every 6 hours.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the maximum dip angle (angle of repose) for subaqueous current beds?</div>
        <div class="pq-ans">Answer: Approximately $30^\circ$ to $34^\circ$</div>
        <div class="pq-exp">Avalanching of sand grains down the lee slope cannot exceed the angle of internal friction of submerged sand ($~30-34^\circ$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the term for giant cross-bedding sets exceeding 5 to 20 meters in thickness?</div>
        <div class="pq-ans">Answer: Aeolian Draa / Dune cross-stratification (e.g., Navajo Sandstone, USA)</div>
        <div class="pq-exp">Desert sand dunes produce colossal cross-bedding sets, far thicker than subaqueous river dunes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What sedimentary structure forms when storm-induced oscillatory waves scour and deposit gently undulating mounds of fine sand?</div>
        <div class="pq-ans">Answer: Hummocky Cross-Stratification (HCS)</div>
        <div class="pq-exp">HCS is the diagnostic signature of storm-dominated shelf deposition below fairweather wave base.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In a river channel, which direction do the inclined current beds dip?</div>
        <div class="pq-ans">Answer: Downstream (in the down-current direction of stream flow).</div>
        <div class="pq-exp">Sediment grains migrate up the stoss side and tumble down the downstream-facing lee face.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is flaser bedding?</div>
        <div class="pq-ans">Answer: A cross-bedded sand structure in which mud streaks or lenses are preserved in the ripple troughs.</div>
        <div class="pq-exp">Flaser bedding reflects fluctuating energy in tidal flats: sand ripples migrate during currents, and mud settles in troughs during slack water.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between planar cross-bedding and trough cross-bedding?</div>
        <div class="pq-ans">Answer: Planar has flat bounding surfaces; trough cross-bedding has scoop-shaped, curved erosional bounding surfaces.</div>
        <div class="pq-exp">Planar cross-bedding forms from 2D straight dunes; trough cross-bedding forms from 3D curved/lunate dunes.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q096: Diagenesis (Compaction and Cementation)
# -----------------------------------------------------------------------------
def gen_q096():
    q_num = 96
    filename = "Q096_Compaction_And_Cementation_Occur_During_Diagenesis_Complete_Guide.html"
    title = "Q096: Sedimentary Diagenesis - Compaction & Cementation"
    badge = "OPSC 2019 Geology Paper-II • Question 96 • Sedimentary Petrology"
    h1_title = "Sedimentary Diagenesis: Physical Compaction, Chemical Cementation, and Lithification"
    meta_text = "<strong>Topic:</strong> Lithification & Post-Depositional Changes • <strong>Key Concept:</strong> P-T Boundary of Diagenesis vs. Metamorphism • <strong>Textbooks:</strong> Sam Boggs Jr. (2014); K.M. Bangar (p. 130); F.J. Pettijohn"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Spectrum of Diagenesis</div>
      <p><strong>Diagenesis</strong> (from Greek <em>dia</em> = through/across, and <em>genesis</em> = origin/creation) encompasses all physical, chemical, and biological processes that affect a sedimentary deposit after its initial deposition and through its progressive burial and lithification, up to the lowest boundary of metamorphism ($T \approx 200\text{--}250^\circ\text{C}, P \approx 1\text{--}2\text{ kbar}$):</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Diagenetic Realm</th>
              <th>Primary Physical / Chemical Process</th>
              <th>Effect on Porosity & Permeability</th>
              <th>Diagnostic Mineral Transformations</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Mechanical Compaction</strong></td>
              <td>Overburden loading expels pore water; grains reorient, rotate, and fracture.</td>
              <td>Primary porosity drops drastically (e.g., from 70% in mud to 20% in shale; 40% to 25% in sand).</td>
              <td>Dewatering; ductile grains (clay clasts, micas) squeeze into pseudo-matrix.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Chemical Cementation</strong></td>
              <td>Precipitation of authigenic minerals from supersaturated interstitial pore fluids.</td>
              <td>Pore throats occluded; loose grains bonded into rigid, consolidated rock (lithification).</td>
              <td>Calcite cement, quartz overgrowths, hematite coatings, authigenic clays (kaolinite, illite).</td>
            </tr>
            <tr>
              <td>Pressure Solution (Chemical Compaction)</td>
              <td>Intergranular pressure increases solubility at grain contact points.</td>
              <td>Grains interlock forming sutured, concavo-convex, or stylolitic contacts.</td>
              <td>Stylolites in carbonates; silica dissolved from contacts reprecipitates as quartz cement.</td>
            </tr>
            <tr>
              <td>Dissolution & Leaching</td>
              <td>Circulation of acidic or undersaturated pore waters dissolves unstable framework grains.</td>
              <td><strong>Creates secondary porosity</strong> (critical for petroleum and groundwater reservoirs).</td>
              <td>Leaching of feldspars and carbonate fossils leaving moldic and vuggy pores.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Diagenesis</strong> refers to all the physical and chemical changes that sediments undergo after deposition, prior to metamorphism. The two most important processes of diagenesis are <strong>compaction</strong> (the squeezing together of grains under overburden weight) and <strong>cementation</strong> (the binding of grains by precipitated mineral matter such as calcite, silica, or iron oxide). Together, compaction and cementation convert loose, unconsolidated sediment into solid rock."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Rocks, p. 130)</div>
      </div>

      <div class="formula-box">
        $$\text{Athys' Law of Compaction: } \Phi(z) = \Phi_0 e^{-c z} \quad (\text{Porosity } \Phi \text{ decreases exponentially with depth } z)$$
        $$\text{Lithification} \equiv \mathbf{Compaction\ (Mechanical\ Dewatering)} + \mathbf{Cementation\ (Chemical\ Authigenesis)} \subset \mathbf{Diagenesis\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q096/sedimentary_diagenesis_compaction_cementation.png" alt="Sedimentary Diagenesis Compaction Cementation" class="figure-img">
        <div class="figure-caption">Figure 96: Progressive stages of sedimentary diagenesis: from uncompacted loose grains at deposition, through mechanical compaction, to mineral cementation producing lithified sedimentary rock.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 96</div>
        <div class="raw-q-text">Compaction and cementation of sediments occur during :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Transportation</div>
          <div class="raw-opt"><span class="opt-letter">B</span> High temperature and pressure medium</div>
          <div class="raw-opt"><span class="opt-letter">C</span> High water pressure</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Diagenesis</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Diagenesis)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Diagenesis</div>
          <p>By unanimous sedimentological definition (Boggs, 2014; Pettijohn; Bangar, p. 130), <strong>compaction and cementation</strong> are the hallmark processes of <strong>diagenesis</strong>. They occur post-depositionally during burial at low to moderate temperatures and pressures, transforming loose sediments into solid, indurated sedimentary rocks.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Transportation</div>
          <p>Transportation is the movement of loose sediments by water, wind, or ice. It causes abrasion, rounding, and sorting, but cannot cause compaction or cementation, which require static burial.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">High temperature and pressure medium</div>
          <p>High temperature and high pressure ($T > 200\text{--}300^\circ\text{C}, P > 2\text{ kbar}$) define <strong>metamorphism</strong> (e.g., recrystallization of sandstone into quartzite or shale into schist), exceeding the realm of diagenesis.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">High water pressure</div>
          <p>Excessive pore water pressure (overpressuring) actually prevents compaction by holding grains apart, leading to undercompaction and fluid-escape structures rather than normal lithification.</p>
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
              <th>Sedimentary Stage</th>
              <th>Temperature & Pressure Regime</th>
              <th>Dominant Processes</th>
              <th>Physical State of Material</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Weathering & Transport</td><td>Surface ambient ($T < 40^\circ\text{C}, P = 1\text{ atm}$)</td><td>Disintegration, oxidation, sorting, abrasion</td><td>Loose, mobile clasts / ions in solution</td></tr>
            <tr><td>Deposition</td><td>Sediment-water interface</td><td>Gravitational settling, traction, suspension</td><td>Unconsolidated, water-saturated mud/sand</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Diagenesis (Option D)</strong></td><td><strong>Burial ($T: 20^\circ\text{--}200^\circ\text{C}, P < 2\text{ kbar}$)</strong></td><td><strong>Compaction, cementation, authigenesis, dissolution</strong></td><td><strong>Lithified sedimentary rock</strong></td></tr>
            <tr><td>Metamorphism</td><td>Deep burial / orogeny ($T > 200^\circ\text{C}, P > 2\text{ kbar}$)</td><td>Solid-state recrystallization, foliation, blastesis</td><td>Metasedimentary rock (Quartzite, Schist)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What are the three most common mineral cements in sandstones?</div>
        <div class="pq-ans">Answer: Calcite ($CaCO_3$), Silica ($SiO_2$, as syntaxial quartz overgrowths), and Iron Oxides (Hematite/Goethite).</div>
        <div class="pq-exp">Calcite and quartz are the dominant authigenic bonding agents, with hematite imparting classic red-bed coloration.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What optical continuity is displayed by syntaxial quartz overgrowth cement in sandstone thin sections?</div>
        <div class="pq-ans">Answer: The authigenic quartz overgrowth precipitates in optical continuity with the host quartz grain, extinguishing simultaneously.</div>
        <div class="pq-exp">A thin 'dust ring' of iron oxide or fluid inclusions typically marks the boundary between the original rounded grain and the new euhedral crystal facet.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a stylolite?</div>
        <div class="pq-ans">Answer: A serrated, irregular, suture-like surface of intergranular pressure dissolution lined with insoluble clay and organic residue.</div>
        <div class="pq-exp">Stylolites form predominantly in limestones during chemical compaction under high overburden stress.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the difference between eodiagenesis, mesodiagenesis, and telodiagenesis (Choquette & Pray, 1970)?</div>
        <div class="pq-ans">Answer: Eodiagenesis occurs near-surface; mesodiagenesis occurs during deep burial; telodiagenesis occurs upon tectonic uplift and meteoric unroofing.</div>
        <div class="pq-exp">This tripartite classification tracks sediments through early shallow deposition, deep thermal burial, and final exhumation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is secondary porosity?</div>
        <div class="pq-ans">Answer: Porosity generated post-depositionally by the chemical dissolution of mineral grains (e.g., feldspars, carbonate bioclasts) or fracturing.</div>
        <div class="pq-exp">Secondary dissolution porosity provides huge reservoirs for hydrocarbons in deeply buried sandstones and limestones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which clay mineral is typically converted to illite during deep burial diagenesis at temperatures above $100^\circ\text{C}$?</div>
        <div class="pq-ans">Answer: Smectite (Smectite-to-Illite transition)</div>
        <div class="pq-exp">The illitization of smectite releases substantial water, contributing to abnormal pore fluid overpressuring in deep shale basins.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How does mechanical compaction affect clay sediments differently from well-sorted quartz sands?</div>
        <div class="pq-ans">Answer: Clays compact enormously (up to 60-80% volume reduction), while rigid quartz sands lose only ~15-20% porosity prior to chemical compaction.</div>
        <div class="pq-exp">Platy clay flakes collapse readily under overburden, whereas quartz frameworks resist crushing until high pressures trigger pressure solution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What organic maturation parameter is used to gauge the thermal boundary between diagenesis and metamorphism?</div>
        <div class="pq-ans">Answer: Vitrinite Reflectance ($R_o \approx 2.0\text{--}2.5\%$) and Conodont Alteration Index (CAI = 5)</div>
        <div class="pq-exp">Vitrinite reflectance measures organic carbonization; values beyond 2.5% indicate the transition into the anchizone (lowest metamorphic grade).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q097: Oscillation Ripples in Beach Environment
# -----------------------------------------------------------------------------
def gen_q097():
    q_num = 97
    filename = "Q097_Oscillation_Ripples_Are_Formed_In_Beach_Environment_Complete_Guide.html"
    title = "Q097: Sedimentary Structures - Oscillation Ripples in Beach Environment"
    badge = "OPSC 2019 Geology Paper-II • Question 97 • Sedimentary Petrology"
    h1_title = "Oscillation (Wave) Ripples: Symmetrical Hydrodynamics and Beach Environments"
    meta_text = "<strong>Topic:</strong> Ripple Bedforms & Environmental Diagnostics • <strong>Key Concept:</strong> Symmetrical Crests & Bidirectional Orbital Motion • <strong>Textbooks:</strong> Sam Boggs Jr. (2014); K.M. Bangar (p. 133); Pettijohn"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Wave Mechanics & Oscillation Ripples</div>
      <p><strong>Oscillation ripples</strong> (also termed <em>wave ripples</em> or <em>symmetrical ripples</em>) are primary sedimentary structures characterized by straight, symmetrical, sharp or pointed crests separated by broad, rounded troughs. They are generated by the <strong>bidirectional, back-and-forth oscillatory water motion</strong> produced by surface gravity waves in shallow standing or shelf waters where wave orbital motion reaches the sediment bed:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Diagnostic Parameter</th>
              <th>Oscillation (Wave) Ripples</th>
              <th>Current (Unidirectional) Ripples</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Profile Symmetry</td>
              <td><strong>Strictly Symmetrical</strong> (both slopes have identical dip angles, typically $20^\circ\text{--}30^\circ$).</td>
              <td><strong>Markedly Asymmetrical</strong> (gentle up-current stoss slope $8^\circ\text{--}14^\circ$, steep down-current lee slope $30^\circ\text{--}34^\circ$).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td>Hydrodynamic Setting</td>
              <td><strong>Shallow Beach / Littoral Shelf / Lake Shores (Option B)</strong>; above fairweather wave base.</td>
              <td>Unidirectional flows: Fluvial channels, desert sand sheets, tidal estuaries, turbidity currents.</td>
            </tr>
            <tr>
              <td>Crest Morphology</td>
              <td>Sharp, narrow, continuous bifurcating crests with tuning-fork junctions.</td>
              <td>Straight, sinuous, linguoid, or lunate crests; non-bifurcating.</td>
            </tr>
            <tr>
              <td>Ripple Index ($L/H$)</td>
              <td><strong>Low: $L / H = 4 \text{ to } 8$</strong> (rarely up to 10; steep crests).</td>
              <td><strong>High: $L / H = 8 \text{ to } 15$</strong> (flatter, elongated profiles).</td>
            </tr>
            <tr>
              <td>Internal Lamination</td>
              <td>Chevron or bidirectional cross-laminae dipping in both directions.</td>
              <td>Unidirectional foreset laminae dipping down-current.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Oscillation ripples</strong> are symmetrical in cross-section with sharp narrow ridges and broad round hollows. They are formed by the back-and-forth oscillatory motion of water waves in shallow water bodies where wave action touches bottom, such as in the <strong>beach environment</strong>, shallow lakes, and nearshore marine shelves. Because the wave impulses in both directions are balanced, neither slope is steeper than the other."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Structures, p. 133)</div>
      </div>

      <div class="formula-box">
        $$\text{Symmetry Index: } \text{RSI} = \frac{\text{Stoss Length}}{\text{Lee Length}} \approx 1.0\ \mathbf{(Symmetrical \equiv Oscillation\ Wave\ Ripple)}$$
        $$\text{Ripple Index: } \text{RI} = \frac{\text{Wavelength } (L)}{\text{Height } (H)} \le 8\text{--}10 \implies \mathbf{Beach\ Environment\ (Option\ B)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q097/oscillation_ripples_symmetrical_wave_action.png" alt="Oscillation Ripples Symmetrical Wave Action" class="figure-img">
        <div class="figure-caption">Figure 97: Hydrodynamic formation of symmetrical oscillation wave ripples in shallow beach/nearshore waters, showing circular-to-elliptical orbital paths producing sharp crests and broad troughs.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 97</div>
        <div class="raw-q-text">Oscillation ripples are formed in :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Deep sea environment</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Beach environment</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Alluvial environment</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Desert environment</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Beach environment)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Beach environment</div>
          <p>Oscillation ripples are formed by the orbital back-and-forth motion of water waves where water depth is shallower than half the wavelength ($h < L_{\text{wave}}/2$). This occurs predominantly in the <strong>beach and nearshore littoral marine environment</strong> (as well as shallow lake margins), creating the quintessential symmetrical wave ripples seen on modern sandy shorelines.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Deep sea environment</div>
          <p>The deep sea (abyssal plain) lies far below storm wave base ($> 200\text{--}4000\text{ m}$ depth), completely sheltered from surface wave orbital motion. Sediments settle by pelagic suspension or are carried by unidirectional turbidity currents.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Alluvial environment</div>
          <p>Alluvial (river) environments are dominated by unidirectional downhill water flow, producing <strong>asymmetrical current ripples</strong>, never symmetrical oscillation wave ripples.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Desert environment</div>
          <p>Desert environments are characterized by unidirectional wind currents, producing <strong>asymmetrical aeolian ripples</strong> with coarse grains concentrated on the crests, rather than wave oscillation ripples.</p>
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
              <th>Ripple Feature</th>
              <th>Oscillation (Wave) Ripples</th>
              <th>Current (Fluvial) Ripples</th>
              <th>Aeolian (Desert) Ripples</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td>Depositional Realm</td><td><strong>Beach / Shallow Marine (Option B)</strong></td><td>Alluvial Rivers / Fluvial Channels</td><td>Desert Dunes / Sand Seas</td></tr>
            <tr><td>Hydrodynamic Motion</td><td>Bidirectional orbital wave motion</td><td>Unidirectional water flow</td><td>Unidirectional wind traction / saltation</td></tr>
            <tr><td>Cross-Sectional Shape</td><td>Symmetrical (Sharp crest, round trough)</td><td>Asymmetrical (Gentle stoss, steep lee)</td><td>Asymmetrical (Long stoss, short lee)</td></tr>
            <tr><td>Grain Sorting across Crest</td><td>Coarser grains in troughs</td><td>Coarser grains in troughs</td><td><strong>Coarsest grains on crests</strong> (impact sorting)</td></tr>
            <tr><td>Crest Pattern</td><td>Bifurcating 'tuning-fork' junctions</td><td>Non-bifurcating sinuous / linguoid</td><td>Extremely straight, long parallel ridges</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. How can oscillation ripples serve as a 'way-up' (geopetal) indicator in folded strata?</div>
        <div class="pq-ans">Answer: Sharp, pointed crests point toward the stratigraphic top (younging direction); broad rounded troughs face the base.</div>
        <div class="pq-exp">Wave dynamics naturally sharpen the crests upward and hollow out the troughs; if rounded surfaces point up, the bed is inverted.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What diagnostic junction pattern is unique to wave-formed oscillation ripples?</div>
        <div class="pq-ans">Answer: Tuning-fork bifurcation (crests split and rejoin in a Y-shaped pattern).</div>
        <div class="pq-exp">Interference and minor phase shifts in oscillatory wave trains cause ripple crests to bifurcate like tuning forks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. At what water depth limit does wave orbital motion cease to affect sediment on the sea floor?</div>
        <div class="pq-ans">Answer: Wave base, equal to approximately half the wavelength of surface waves ($h = L / 2$).</div>
        <div class="pq-exp">Below wave base, water orbit diameters diminish exponentially to zero, preventing oscillation ripple formation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the difference between fairweather wave base and storm wave base?</div>
        <div class="pq-ans">Answer: Fairweather wave base is ~5 to 15 m depth; storm wave base can reach 50 to 200 m depth during hurricanes.</div>
        <div class="pq-exp">Oscillation ripples on open beaches form above fairweather wave base; hummocky cross-stratification forms between the two wave bases.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the Ripple Symmetry Index (RSI) of an ideal oscillation ripple?</div>
        <div class="pq-ans">Answer: $\text{RSI} = 1.0$ (or between 1.0 and 1.5)</div>
        <div class="pq-exp">$\text{RSI} = \text{Stoss length} / \text{Lee length}$. Current ripples have $\text{RSI} > 2.0$; wave ripples are essentially 1.0.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why are the coarsest sand grains concentrated on the crests of desert aeolian ripples, but in the troughs of subaqueous ripples?</div>
        <div class="pq-ans">Answer: In wind ripples, saltating grains impact the surface and push coarse creep grains up to the crests; in water, turbulence winnows fines from troughs.</div>
        <div class="pq-exp">This grain distribution criterion is the absolute diagnostic test separating wind-blown sandstones from water-laid sandstones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a combined-flow ripple?</div>
        <div class="pq-ans">Answer: A ripple formed by the simultaneous action of unidirectional current flow and oscillatory wave motion.</div>
        <div class="pq-exp">Combined flow ripples show slightly asymmetrical profiles with rounded crests and internal cross-laminae dipping dominantly down-current.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What happens to beach sand ripples when the wave swash retreats down the beach face?</div>
        <div class="pq-ans">Answer: They are planed off, producing flat planar beds with parting lineations or washed into rhomboid ripples.</div>
        <div class="pq-exp">High-velocity sheet wash in the swash zone destroys ripples, producing upper flow regime planar lamination.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q098: Ferroan Calcite Cement - Deep Burial Diagenesis
# -----------------------------------------------------------------------------
def gen_q098():
    q_num = 98
    filename = "Q098_Ferroan_Calcite_Cement_Indicator_Of_Deep_Burial_Diagenesis_Complete_Guide.html"
    title = "Q098: Carbonate Diagenesis - Ferroan Calcite & Deep Burial Redox"
    badge = "OPSC 2019 Geology Paper-II • Question 98 • Sedimentary Petrology"
    h1_title = "Carbonate Diagenesis: Ferroan Calcite Cement as a Sentinel of Deep Burial Redox"
    meta_text = "<strong>Topic:</strong> Carbonate Petrology & Diagenesis • <strong>Key Concept:</strong> Ferrous Iron Incorporation in Anoxic Burial Phreatic Realms • <strong>Textbooks:</strong> M.E. Tucker & V.P. Wright (1990); P.A. Scholle (1978); Sam Boggs Jr."

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Geochemistry of Ferroan Calcite Cementation</div>
      <p>In carbonate sedimentology and diagenetic stratigraphy, the chemical composition of authigenic <strong>calcite cement</strong> ($\text{CaCO}_3$) records the oxidation-reduction potential ($Eh$), acidity ($pH$), and fluid provenance of the pore waters from which it precipitated. The incorporation of <strong>ferrous iron ($\text{Fe}^{2+}$)</strong> into the calcite crystal lattice to form <strong>ferroan calcite</strong> is a definitive geochemical signature of <strong>Deep Burial Diagenesis</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Diagenetic Environment</th>
              <th>Redox State & Oxygen Availability</th>
              <th>Iron Speciation</th>
              <th>Calcite Cement Chemistry & Staining</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Marine Phreatic (Sea floor)</td>
              <td>Oxygenated ($Eh > 0$)</td>
              <td>Insoluble $\text{Fe}^{3+}$ (ferric); cannot substitute into calcite.</td>
              <td>High-Mg Calcite or Aragonite; strictly <strong>non-ferroan</strong>.</td>
            </tr>
            <tr>
              <td>Meteoric Vadose (Above water table)</td>
              <td>Highly Oxidizing ($Eh \gg 0$)</td>
              <td>Precipitates as insoluble iron hydroxides (goethite/hematite dust).</td>
              <td>Equant low-Mg calcite; strictly <strong>non-ferroan</strong> (stains pink/red with Alizarin Red S).</td>
            </tr>
            <tr>
              <td>Meteoric Phreatic (Shallow below water table)</td>
              <td>Suboxic to mildly oxidizing</td>
              <td>Trace $\text{Fe}^{2+}$ only in stagnant zones; mostly $\text{Fe}^{3+}$.</td>
              <td>Zoned non-ferroan to trace ferroan luminescent calcite.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>DEEP BURIAL ZONE (Option A)</strong></td>
              <td><strong>Deeply Anoxic / Strongly Reducing ($Eh \ll 0$)</strong></td>
              <td><strong>Abundant soluble $\text{Fe}^{2+}$ (ferrous iron reduced by organic matter/bacteria)</strong>.</td>
              <td><strong>★ FERROAN CALCITE CEMENT ★</strong> ($\text{Fe}^{2+}$ substitutes for $\text{Ca}^{2+}$; stains <strong>purple to dark blue</strong> with potassium ferricyanide).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "The occurrence of <strong>ferroan calcite cement</strong> in a carbonate rock is an unambiguous indicator of <strong>deep burial diagenesis</strong>. Near the surface, oxygenated groundwaters keep iron in the insoluble ferric state ($\text{Fe}^{3+}$). With deeper burial and isolation from the atmosphere, bacterial degradation of organic matter and microbial sulphate reduction create strongly reducing (anoxic) conditions, reducing iron to the soluble ferrous state ($\text{Fe}^{2+}$), which readily substitutes for $\text{Ca}^{2+}$ in late-stage burial calcite cements."
        <div class="quote-author">&mdash; M.E. Tucker & V.P. Wright, <em>Carbonate Sedimentology</em> (Blackwell Scientific, Diagenesis Section, pp. 365&ndash;368)</div>
      </div>

      <div class="formula-box">
        $$\text{Ionic Radii: } r(\text{Ca}^{2+}) = 1.00\text{ \AA} \quad \longleftrightarrow \quad r(\text{Fe}^{2+}) = 0.78\text{ \AA} \quad (\text{Substitutes into calcite lattice})$$
        $$\text{Deep Burial Reduction: } \text{Fe}^{3+}\text{-oxides} + \text{Organic Carbon} \xrightarrow{\text{Anaerobic Burial}} \mathbf{Fe^{2+}\ (\text{Soluble})} \rightarrow \mathbf{(Ca,Fe)CO_3\ (Ferroan\ Calcite)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q098/ferroan_calcite_cement_deep_burial_diagenesis.png" alt="Ferroan Calcite Cement Deep Burial Diagenesis" class="figure-img">
        <div class="figure-caption">Figure 98: Carbonate diagenetic realms showing the transition from shallow oxidized non-ferroan cements to the deep burial reducing anoxic realm where ferroan calcite precipitates.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 98</div>
        <div class="raw-q-text">Occurrence of ferroan calcite cementing in a carbonate rock is an indicator of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Deep burial diagenesis</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Vadose diagenesis</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Phreatic diagenesis</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Sea floor diagenesis</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Deep burial diagenesis)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Deep burial diagenesis</div>
          <p>By established carbonate petrographic principles (Scholle, 1978; Tucker & Wright, 1990; Boggs), <strong>ferroan calcite cement</strong> precipitates only in anoxic, strongly reducing pore waters isolated from atmospheric oxygen, conditions that develop exclusively during <strong>deep burial diagenesis</strong>. The reduction of iron to its soluble divalent state ($\text{Fe}^{2+}$) allows it to substitute for $\text{Ca}^{2+}$ in late-stage blocky burial cements.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Vadose diagenesis</div>
          <p>The vadose zone lies above the water table and is in direct contact with air. The pore waters are highly oxygenated (oxidizing), forcing iron into insoluble $\text{Fe}^{3+}$ oxides/hydroxides; cements formed here are strictly <strong>non-ferroan</strong> (meniscus and pendant cements).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Phreatic diagenesis</div>
          <p>Shallow meteoric phreatic diagenetic waters are actively recharged by oxygenated surface runoff, precipitating non-ferroan isopachous or equant spar. Only deep, stagnant burial phreatic waters become sufficiently reducing for ferroan calcite.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Sea floor diagenesis</div>
          <p>Sea floor diagenesis occurs in normal oxygenated marine waters, precipitating high-Mg calcite fibrous fringes or aragonite botryoids. These cements are completely non-ferroan.</p>
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
              <th>Diagenetic Realm</th>
              <th>Oxygenation / Eh</th>
              <th>Iron Content in Calcite</th>
              <th>Staining Response (Dickson, 1966)</th>
              <th>Cathodoluminescence (CL)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Vadose (Meteoric)</td><td>Highly Oxidizing</td><td>Zero ($Fe^{3+}$ insoluble)</td><td>Pink to red (Non-ferroan)</td><td>Non-luminescent (Black)</td></tr>
            <tr><td>Shallow Phreatic (Meteoric)</td><td>Oxidizing to suboxic</td><td>Negligible</td><td>Pink to red</td><td>Bright yellow/orange ($Mn^{2+}$-activated)</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Deep Burial (Option A)</strong></td><td><strong>Deeply Reducing (Anoxic)</strong></td><td><strong>High ($\text{Fe}^{2+} > 0.5\text{--}2\text{ wt\%}$)</strong></td><td><strong>Purple to Royal Blue (Ferroan)</strong></td><td>Dull to quenched dark brown ($\text{Fe}^{2+}$-quenched)</td></tr>
            <tr><td>Sea Floor (Marine)</td><td>Oxidizing</td><td>Zero</td><td>Pink / unstained</td><td>Non-luminescent</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What chemical stain is used in carbonate petrography to distinguish ferroan calcite from non-ferroan calcite?</div>
        <div class="pq-ans">Answer: Potassium Ferricyanide $[K_3Fe(CN)_6]$ mixed with Alizarin Red S (Dickson's solution).</div>
        <div class="pq-exp">Potassium ferricyanide reacts with $\text{Fe}^{2+}$ in the crystal lattice to form Turnbull's Blue, staining ferroan calcite purple to deep blue.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why does $\text{Fe}^{2+}$ quench cathodoluminescence (CL) in burial calcite cements?</div>
        <div class="pq-ans">Answer: $Mn^{2+}$ activates luminescence, whereas $\text{Fe}^{2+}$ acts as an energy quencher, suppressing light emission.</div>
        <div class="pq-exp">When the $\text{Fe}/\text{Mn}$ ratio exceeds ~1.0, luminescence is suppressed, causing ferroan burial calcite to appear dull or dark under CL.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the typical crystalline morphology of late-stage deep burial calcite cement?</div>
        <div class="pq-ans">Answer: Coarse, equant 'blocky' spar or poikilotopic calcite filling central pore voids and fractures.</div>
        <div class="pq-exp">Slow crystallization from warm, sluggish burial brines produces large, clear, euhedral-to-subhedral blocky spar crystals.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the source of ferrous iron ($\text{Fe}^{2+}$) in deep burial carbonate waters?</div>
        <div class="pq-ans">Answer: Microbial reduction of iron oxides/hydroxides coupled with the anaerobic oxidation of organic matter, and clay mineral diagenesis (smectite-to-illite).</div>
        <div class="pq-exp">Dewatering shales adjacent to carbonate platforms expel iron-rich pore fluids into limestone aquifers during deep burial.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is a ferroan dolomite called?</div>
        <div class="pq-ans">Answer: Ankerite $[Ca(Mg,Fe)(CO_3)_2]$</div>
        <div class="pq-exp">When ferrous iron substitutes extensively for magnesium in dolomite, it forms the ferroan dolomite / ankerite solid-solution series.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does burial temperature affect oxygen isotope ratios ($\delta^{18}O$) in ferroan calcite cements?</div>
        <div class="pq-ans">Answer: Higher burial temperatures cause strong depletion in $^{18}O$, yielding highly negative $\delta^{18}O$ values (e.g., $-6\text{ to } -12\text{ \textperthousand}\text{ PDB}$).</div>
        <div class="pq-exp">The calcite-water oxygen isotope fractionation factor decreases with increasing temperature, a classic geochemical hallmark of deep burial.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is meniscus cement and in which diagenetic realm does it form?</div>
        <div class="pq-ans">Answer: Meniscus cement forms at grain contact points held by capillary water in the unsaturated meteoric vadose zone.</div>
        <div class="pq-exp">Meniscus and pendant (gravitational) cements are exclusive indicators of the vadose zone above the water table.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the significance of ferroan calcite cement in hydrocarbon reservoir exploration?</div>
        <div class="pq-ans">Answer: It marks the timing and depth of final primary porosity destruction before or during petroleum migration.</div>
        <div class="pq-exp">If oil migration precedes ferroan calcite precipitation, hydrocarbons preserve porosity by halting water-rock reactions.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 8 Part A (Q091 - Q098)...")
    gen_q091()
    gen_q092()
    gen_q093()
    gen_q094()
    gen_q095()
    gen_q096()
    gen_q097()
    gen_q098()
    print("Batch 8 Part A successfully generated!")
