#!/usr/bin/env python3
"""
Q102 Generator: Sandstone Ternary Classification & Arkose Petrography
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q102():
    title = r"Q102: Sedimentary Petrology: Sandstone Q-F-L Ternary Classification & Arkose | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Classification"
    h1_title = "Q102: Sandstone Classification: The Fundamental Q-F-L Triad (Quartz Sandstone, Arkose, Litharenite)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 102<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Sandstones, pp. 142–148; Fig. 5.9); F.J. Pettijohn, P.E. Potter, and R. Siever, <em>Sand and Sandstone</em> (Springer-Verlag); Robert L. Folk, <em>Petrology of Sedimentary Rocks</em> (Hemphill); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 70–73, 172)."""

    part1 = r"""
  <!-- CARD 1: THE FUNDAMENTAL Q-F-L TERNARY CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Q-F-L Petrographic Framework & The Sandstone Triad</div>
    <div class="card-body">
      <p>
        In modern sedimentary petrology (Pettijohn, 1975; Folk, 1980; Boggs, 2014, pp. 142–148), sandstones containing less than $15\%$ detrital matrix (arenites) are classified according to the relative abundance of their three primary framework grain constituents recalculated to $100\%$:
      </p>
      <ul>
        <li><strong>$\mathbf{Q}$ (Quartz):</strong> Monocrystalline and polycrystalline quartz and chert grains.</li>
        <li><strong>$\mathbf{F}$ (Feldspar):</strong> Potassium feldspar (orthoclase, microcline, sanidine) and plagioclase feldspar.</li>
        <li><strong>$\mathbf{L}$ (Lithic Fragments):</strong> Unstable rock fragments of volcanic, metamorphic, or older sedimentary origin.</li>
      </ul>
      <p>
        This compositional ternary diagram establishes the canonical tripartite division of sandstones:
      </p>
      <ol>
        <li><strong>Quartz Sandstone (Quartzarenite):</strong> $> 90\text{ to } 95\%$ quartz framework grains; highly mature, multicyclic cratonic or stable passive margin sheet sands.</li>
        <li><strong>Arkose (Feldspathic Sandstone / Subarkose):</strong> $> 25\%$ feldspar framework grains (with $F > L$); typically derived from the erosion of uplifted crystalline granitic/gneissic basement blocks.</li>
        <li><strong>Litharenite (Lithic Sandstone / Sublitharenite):</strong> $> 25\%$ lithic rock fragments (with $L > F$); derived from rapidly eroding collision orogens, volcanic arcs, or fold-and-thrust belts.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q102/boggs_p145_sandstone_ternary_arkose_litharenite.png" alt="Q-F-L Ternary Sandstone Classification from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 102.1 — Q-F-L Ternary Classification of Sandstones:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 145). Illustrates the three main sandstone fields: Quartz arenite, Arkose (feldspathic arenite), and Litharenite (lithic arenite), bounded by the $Q, F, \text{and } L$ poles.
        </div>
      </div>

      <h4>Petrographic Characteristics of Arkose</h4>
      <p>
        The term <strong>arkose</strong> was introduced by the French geologist Alexandre Brongniart in 1826:
      </p>
      <ul>
        <li><strong>Mineralogy:</strong> Characterized by $> 25\%$ detrital feldspar (predominantly potassic K-feldspar: orthoclase and microcline, showing diagnostic cross-hatched "tartan" twinning under crossed nicols, and subordinate plagioclase), quartz, and accessory biotite, muscovite, and granite rock fragments.</li>
        <li><strong>Color:</strong> Typically pink, reddish-orange, or salmon-colored owing to the abundance of flesh-colored K-feldspars and iron-oxide coatings.</li>
        <li><strong>Grain Texture:</strong> Commonly coarse-grained to gritty, angular to sub-angular, and moderately to poorly sorted, indicating rapid erosion and short fluvial transport.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: PALEOCLIMATIC AND TECTONIC IMPLICATIONS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Tectonic Provenance & Climatic Controls on Arkose Formation</div>
    <div class="card-body">
      <h4>Dickinson & Suczek (1979) Tectonic Provenance Provenance</h4>
      <p>
        In global plate tectonic reconstructions, sandstones plot into distinct provenance regimes on Q-F-L space:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sandstone Class</th>
            <th>Dominant Framework Pole</th>
            <th>Tectonic Provenance (Dickinson, 1985)</th>
            <th>Paleogeographic Basin Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Quartz Sandstone</strong></td>
            <td>$\mathbf{Q}$ Pole ($> 95\%$)</td>
            <td><strong>Continental Interior / Craton</strong></td>
            <td>Stable cratonic platforms, passive continental margins, polycyclic reworking.</td>
          </tr>
          <tr>
            <td><strong>Arkose</strong></td>
            <td>$\mathbf{F}$ Pole ($> 25\%, F > L$)</td>
            <td><strong>Basement Uplift / Block Faulting</strong></td>
            <td>Rift basins, aulacogens, fault-bounded grabens (e.g., East African Rift, New Red Sandstone).</td>
          </tr>
          <tr>
            <td><strong>Litharenite</strong></td>
            <td>$\mathbf{L}$ Pole ($> 25\%, L > F$)</td>
            <td><strong>Recycled Orogen / Magmatic Arc</strong></td>
            <td>Foreland basins, trench-slope basins, suture zones (e.g., Siwalik Group, Molasse).</td>
          </tr>
        </tbody>
      </table>

      <h4>Climatic Factor: Krynine's Climatic Classification of Arkoses</h4>
      <p>
        Because feldspar is chemically unstable and decomposes rapidly to clay under warm, humid conditions via chemical hydrolysis ($2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \rightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 + 4\text{H}_4\text{SiO}_4 + 2\text{K}^+$), the preservation of abundant fresh feldspar requires:
      </p>
      <ul>
        <li><strong>Tectonic Control (High Relief):</strong> High topographic relief where erosion rates vastly outpace chemical weathering rates, allowing fresh feldspar to be shed mechanically regardless of climate.</li>
        <li><strong>Climatic Control (Aridity / Cold):</strong> Very dry (arid/semi-arid) or very cold (glacial/periglacial) climates where lack of liquid water or freezing temperatures shuts down chemical hydrolysis, preserving fresh feldspar.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 102:</strong> Sandstone is categorized into three main types based on their variation in composition and cementing material, they include : • Quartz Sandstone, • ___________, • Litharenite or lithic sandstone.
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> Arkose</div>
        <div class="option-item"><strong>(B)</strong> Greywacke</div>
        <div class="option-item"><strong>(C)</strong> Molasse</div>
        <div class="option-item"><strong>(D)</strong> None of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) Arkose</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Arkose (Feldspathic Arenite)</div>
        <p>
          <strong>Correct:</strong> In all authoritative sedimentary petrology textbooks (Boggs, 2014, p. 142; Pettijohn, 1975; Folk, 1980; Bangar, p. 70), sandstones are divided into three fundamental compositional end-members based on framework mineralogy ($Q\text{-}F\text{-}L$ triad): <strong>Quartz Sandstone</strong>, <strong>Arkose (feldspathic sandstone)</strong>, and <strong>Litharenite (lithic sandstone)</strong>. Arkose completes this tripartite classification scheme.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Greywacke</div>
        <p>
          <strong>Incorrect:</strong> A <strong>greywacke</strong> (or wacke) is distinguished fundamentally by its <strong>matrix content</strong> (containing $> 15\%$ detrital clay/silt matrix), representing a texturally immature, matrix-rich class. The triad listed in the question represents the three primary <em>compositional arenite classes</em> ($< 15\%$ matrix) defined by the three corners of the Q-F-L ternary diagram. Greywacke is not an apex of the framework ternary diagram.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Molasse</div>
        <p>
          <strong>Incorrect:</strong> <strong>Molasse</strong> is not a compositional sandstone type, but a <strong>tectonic-sedimentary lithofacies</strong> or mega-facies. It refers to thick wedges of shallow-marine and non-marine (fluvial, alluvial, lacustrine) post-orogenic clastic deposits shed into a foreland basin during and after the final uplift of an orogenic mountain belt (e.g., the Alpine Molasse or Himalayan Siwaliks). Molasse contains varied lithologies (conglomerates, lithic sandstones, siltstones, shales).
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — None of These</div>
        <p>
          <strong>Incorrect:</strong> Because Arkose is the precise textbook term completing the trio, Option (D) is false.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Matrix: The Canonical Sandstone Triad (Q-F-L)</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sandstone Class</th>
            <th>Primary Framework Composition</th>
            <th>Diagnostic Detrital Minerals</th>
            <th>Maturity Level</th>
            <th>Diagnostic Geotectonic Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Quartz Sandstone (Quartzarenite)</strong></td>
            <td>$> 90\text{--}95\%$ Quartz</td>
            <td>Monocrystalline quartz, chert; ZTR heavy minerals</td>
            <td>Supermature (texturally and mineralogically)</td>
            <td>Stable cratons, passive continental margins, beach/eolian ergs</td>
          </tr>
          <tr>
            <td><strong>Arkose (Feldspathic Sandstone)</strong></td>
            <td>$> 25\%$ Feldspar ($F > L$)</td>
            <td>Microcline (cross-hatched), orthoclase, perthite, quartz, biotite</td>
            <td>Submature to immature (chemically labile feldspars preserved)</td>
            <td>Block-faulted basement uplifts, continental rifts, granitic grabens</td>
          </tr>
          <tr>
            <td><strong>Litharenite (Lithic Sandstone)</strong></td>
            <td>$> 25\%$ Rock Fragments ($L > F$)</td>
            <td>Basalt/andesite lithics, phyllite/schist fragments, chert clasts</td>
            <td>Immature to submature</td>
            <td>Active collision orogens, volcanic island arcs, fold-and-thrust belts</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Practice Problems & Analytical Derivations</div>
    <div class="card-body">
      <div class="problem-box">
        <h4>Practice Problem 1</h4>
        <p>Point-counting of a sandstone thin section yields the following framework grain percentages: Quartz = $55\%$, K-feldspar = $28\%$, Plagioclase = $7\%$, Metamorphic lithics = $10\%$, Detrital matrix = $4\%$. Classify this sandstone according to Pettijohn's (1975) and Folk's (1980) systems.</p>
        <p><strong>Solution:</strong>
          1. Matrix check: Matrix is $4\% < 15\%$, so the rock is an <strong>arenite</strong>.
          2. Recalculate framework grains to $100\%$:
             - Total $Q + F + L = 55 + (28 + 7) + 10 = 55 + 35 + 10 = 100\%$.
             - $Q = 55\%$, $F = 35\%$, $L = 10\%$.
          3. Evaluate classification criteria:
             - Feldspar ($F = 35\%$) exceeds $25\%$, and $F (35\%) > L (10\%)$.
             - Therefore, the sandstone is classified unambiguously as an <strong>Arkose</strong> (or <em>feldspathic arenite</em>).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain why microcline is more common than plagioclase in ancient cratonic arkoses, referencing the Goldich Weathering Series.</p>
        <p><strong>Solution:</strong>
          In S.S. Goldich's (1938) chemical weathering series, primary silicates follow the reverse order of Bowen's reaction series:
          $$\text{Calcic Plagioclase} > \text{Sodic Plagioclase} \gg \text{K-feldspar (Orthoclase / Microcline)} > \text{Quartz}$$
          Calcic and sodic plagioclase weather significantly faster due to the weaker bonding of $\text{Ca}^{2+}$ and $\text{Na}^+$ and higher $\text{Al/Si}$ substitution ratios. K-feldspar (especially ordered microcline) possesses a more stable framework structure and resists weathering far longer, selectively surviving prolonged diagenesis and concentrating in ancient arkoses.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is a "subarkose" in Folk's sandstone classification scheme, and what are its quantitative boundaries?</p>
        <p><strong>Solution:</strong>
          In Folk's (1980) classification, a <strong>subarkose</strong> is an intermediate composition plotting between quartz arenite and arkose. It is defined as an arenite ($< 15\%$ matrix) containing:
          - Quartz ($Q$) between $75\%$ and $95\%$.
          - Feldspar ($F$) greater than lithic fragments ($F > L$).
          - Feldspar content between $5\%$ and $25\%$.
          It represents a moderately mature sandstone derived from granitic terrain that has experienced moderate chemical weathering or recycling.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>How do Dickinson Q-F-L ternary plots differentiate between a "Magmatic Arc" provenance and a "Basement Uplift" provenance?</p>
        <p><strong>Solution:</strong>
          William R. Dickinson established that:
          - <strong>Basement Uplift (Continental Block):</strong> Plots near the $F$ pole and $Q\text{-}F$ boundary (arkosic suite), reflecting deep erosional unroofing of granitic plutons and gneisses in fault-bounded rift blocks.
          - <strong>Magmatic Arc:</strong> Plots near the $L$ and $F$ poles (volcaniclastic litharenites and feldspathic wackes), characterized by unstable volcanic lithic clasts, plagioclase phenocrysts, and very low quartz.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why do arkosic sandstones typically exhibit a distinct salmon-pink or reddish-orange macroscopic coloration in hand specimen?</p>
        <p><strong>Solution:</strong>
          The characteristic pink color arises from two independent factors:
          1. <strong>Intrinsic Mineral Color:</strong> Detrital potassic feldspars (orthoclase and microcline) naturally exhibit pink to flesh-red hues due to sub-microscopic exsolution of hematite lamellae and structurally incorporated traces of $\text{Fe}^{3+}$.
          2. <strong>Oxidizing Diagenesis:</strong> Because arkoses commonly accumulate in well-aerated, continental fault-trough environments (alluvial fans/braided streams), diagenetic groundwater precipitates fine authigenic hematite pigment coatings on quartz and feldspar grain boundaries.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Distinguish between "Flysch" and "Molasse" in terms of depositional environment, tectonic timing, and typical sandstone types.</p>
        <p><strong>Solution:</strong>
          - <strong>Flysch:</strong> Pre- to syn-orogenic deep-marine turbidite succession deposited in an actively subsiding trench or foredeep basin prior to main mountain uplift; sandstones are typically <em>greywackes</em> interbedded with dark pelagic shales.
          - <strong>Molasse:</strong> Post-orogenic shallow-marine to continental (fluvial, alluvial fan, lacustrine) clastic wedge deposited in a foreland basin during and after the final phase of mountain collision; sandstones are typically <em>litharenites</em>, <em>arkoses</em>, and conglomerates.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What petrographic evidence in an arkose indicates that it was formed under conditions of rapid tectonic unroofing rather than severe climatic aridity?</p>
        <p><strong>Solution:</strong>
          If tectonic unroofing is the primary driver, the arkose will contain both fresh K-feldspars and abundant <strong>labile plagioclase along with unstable ferromagnesian minerals (biotite, hornblende)</strong>, and associated mudrocks will contain illite and chlorite rather than kaolinite. If formed purely under climate control without intense tectonism, the sedimentation rate is slow, allowing plagioclase to degrade while only resistant K-feldspar survives.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Under a polarizing microscope, how does a petrographer definitively distinguish detrital microcline from orthoclase and plagioclase?</p>
        <p><strong>Solution:</strong>
          - <strong>Microcline:</strong> Exhibits diagnostic <strong>cross-hatched (gridiron or "tartan") polysynthetic twinning</strong> resulting from combined albite and pericline twinning under crossed nicols.
          - <strong>Orthoclase:</strong> Typically exhibits simple <strong>Carlsbad twinning</strong> (two sub-equal halves with different extinction angles) or is untwinned.
          - <strong>Plagioclase:</strong> Displays parallel, multiple lamellar <strong>albite twinning</strong> (alternating dark and bright extinction stripes).
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=102,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q102_Sandstone_Classification_Arkose_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q102: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q102()
