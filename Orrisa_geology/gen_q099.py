#!/usr/bin/env python3
"""
Q099 Generator: Sedimentary Maturity, ZTR Index & Geochemical Ratios
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q099():
    title = r"Q099: Sedimentary Petrology: Textural & Mineralogical Maturity & ZTR Index | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Provenance"
    h1_title = "Q099: Sedimentary Maturity: Textural Evolution, Geochemical Indices & The ZTR Heavy Mineral Index"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 99<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Sandstones / Maturity Concepts, pp. 138–144; Fig. 5.7); J.F. Hubert (1962), <em>A Zircon-Tourmaline-Rutile Maturity Index and the Interdependence of the Composition of Heavy-Mineral Assemblages with the Gross Composition and Texture of Sandstones</em> (Journal of Sedimentary Petrology); R.L. Folk (1951), <em>Stages of Textural Maturity in Sedimentary Rocks</em>; F.J. Pettijohn, P.E. Potter, and R. Siever, <em>Sand and Sandstone</em>."""

    part1 = r"""
  <!-- CARD 1: DUAL CONCEPTS OF SEDIMENTARY MATURITY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Dual Framework of Sedimentary Maturity: Textural vs. Mineralogical</div>
    <div class="card-body">
      <p>
        In clastic sedimentology (Boggs, 2014, pp. 138–144; Folk, 1951; Pettijohn et al., 1987), the concept of <strong>sedimentary maturity</strong> refers to the extent to which a clastic sediment has evolved along the pathway toward ultimate physical and chemical equilibrium with the Earth's surface environment.
      </p>
      <p>
        Sedimentary maturity is evaluated across two fundamentally independent dimensions:
      </p>
      <ol>
        <li><strong>Textural Maturity (Folk's Stages of Maturity):</strong> Reflects the expenditure of kinetic mechanical energy in the depositional environment (wave/current winnowing and grain abrasion). It monitors:
          <ul>
            <li>The elimination of fine-grained interstitial detrital clay matrix ($< 0.03\text{ mm}$).</li>
            <li>The degree of hydrodynamic grain-size sorting (measured by graphic standard deviation $\sigma_I$).</li>
            <li>The degree of particle roundness (abrasion of sharp edges and corners into rounded spheres).</li>
          </ul>
        </li>
        <li><strong>Mineralogical (Compositional) Maturity:</strong> Reflects the degree to which unstable, chemically labile, and mechanically weak minerals (e.g., ferromagnesian pyroxenes, amphiboles, olivine, calcic plagioclase, lithic rock fragments) have been destroyed by prolonged chemical weathering and hydrodynamic attrition, leaving a residual concentration of the most inert, ultra-durable phases—predominantly <strong>monocrystalline quartz ($\text{SiO}_2$)</strong> and the ultra-stable heavy mineral trio: <strong>Zircon, Tourmaline, and Rutile (ZTR)</strong>.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q99/boggs_p140_ztr_index_mineralogical_maturity.png" alt="Sedimentary Maturity and ZTR Heavy Mineral Index from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 99.1 — Textural and Mineralogical Maturity Scales of Siliciclastic Sediments:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 140). Depicts the 4-stage textural maturity evolution (immature to supermature) alongside Hubert's ZTR heavy mineral index and Q-F-L mineralogical maturity trends.
        </div>
      </div>

      <h4>Folk's Four Stages of Textural Maturity</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Maturity Stage</th>
            <th>Clay Matrix Content</th>
            <th>Grain Sorting ($\sigma_I$)</th>
            <th>Grain Roundness</th>
            <th>Hydrodynamic Energy Regime</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Immature</strong></td>
            <td>High ($> 5\%$)</td>
            <td>Poorly to very poorly sorted ($\sigma_I > 1.0\phi$)</td>
            <td>Angular to sub-angular</td>
            <td>Low-energy, rapid dumping (alluvial fans, turbidity currents)</td>
          </tr>
          <tr>
            <td><strong>Submature</strong></td>
            <td>Low ($< 5\%$, matrix winnowed away)</td>
            <td>Poorly sorted ($\sigma_I > 0.5\phi$)</td>
            <td>Angular to sub-angular</td>
            <td>Moderate energy; winnowing active but sorting incomplete</td>
          </tr>
          <tr>
            <td><strong>Mature</strong></td>
            <td>Negligible ($< 5\%$)</td>
            <td>Well-sorted ($\sigma_I < 0.5\phi$)</td>
            <td>Sub-angular to sub-rounded</td>
            <td>High sustained energy (fluvial bars, marine shelves)</td>
          </tr>
          <tr>
            <td><strong>Supermature</strong></td>
            <td>Zero ($< 1\%$)</td>
            <td>Very well-sorted ($\sigma_I < 0.35\phi$)</td>
            <td><strong>Well-rounded to rounded</strong></td>
            <td>Prolonged, intense polycyclic reworking (eolian dunes, beach surf zones)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: THE ZTR INDEX & GEOCHEMICAL PROXIES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Hubert's ZTR Index & Geochemical Signatures of High Sedimentary Maturity</div>
    <div class="card-body">
      <h4>Hubert's ZTR Heavy Mineral Maturity Index (1962)</h4>
      <p>
        In clastic provenance and maturity analysis, John F. Hubert established that the non-opaque, transparent heavy mineral fraction ($specific\text{ gravity} > 2.85$) provides an extraordinarily sensitive gauge of mineralogical maturity.
      </p>
      <p>
        Among detrital heavy minerals, <strong>Zircon ($\text{ZrSiO}_4$)</strong>, <strong>Tourmaline (complex borosilicate)</strong>, and <strong>Rutile ($\text{TiO}_2$)</strong> are distinguished by their exceptional mechanical hardness ($Mohs\text{ 7 to 8}$) and near-total chemical inertness under surficial weathering and diagenetic conditions. Hubert's <strong>ZTR Index</strong> is mathematically defined as:
      </p>
      $$\text{ZTR Index (\%)} = \left( \frac{\text{Zircon} + \text{Tourmaline} + \text{Rutile}}{\sum \text{Total Non-Opaque Transparent Heavy Minerals}} \right) \times 100$$
      <ul>
        <li><strong>Low Maturity ($\text{ZTR} < 25\%$):</strong> Assemblages dominated by unstable, labile heavy minerals—such as olivine, calcic clinopyroxenes, hornblende, hypersthene, and apatite—indicating first-cycle, rapid erosion of crystalline bedrock.</li>
        <li><strong>Moderate Maturity ($\text{ZTR} = 25\text{--}75\%$):</strong> Partially altered assemblages with intermediate-stability species (epidote, staurolite, garnet).</li>
        <li><strong>High Maturity ($\text{ZTR} > 75\text{--}90\%$):</strong> Assemblages where all unstable ferromagnesian minerals have been entirely eliminated, leaving almost exclusively zircon, tourmaline, and rutile. When combined with $> 95\%$ quartz framework grains and well-rounded clasts, it establishes <strong>high to supermature maturity</strong>, characteristic of polycyclic cratonic quartz arenites.</li>
      </ul>

      <h4>Geochemical Maturity Indicators</h4>
      <ul>
        <li><strong>$\text{SiO}_2 / \text{Al}_2\text{O}_3$ Ratio:</strong> As sediments mature, quartz ($\text{SiO}_2$) concentrates while aluminous clay minerals and feldspars are winnowed or destroyed. In immature graywackes, $\text{SiO}_2/\text{Al}_2\text{O}_3 \approx 3\text{ to } 5$; in mature quartz arenites, $\text{SiO}_2/\text{Al}_2\text{O}_3 > 20\text{ to } 100+$.</li>
        <li><strong>Chemical Index of Alteration (CIA):</strong> Introduced by Nesbitt and Young (1982):
          $$\text{CIA} = \left[ \frac{\text{Al}_2\text{O}_3}{\text{Al}_2\text{O}_3 + \text{CaO}^* + \text{Na}_2\text{O} + \text{K}_2\text{O}} \right] \times 100$$
          Fresh crystalline bedrock has $\text{CIA} \approx 45\text{--}55$, whereas highly mature, intensively weathered residues (kaolinite/gibbsite) reach $\text{CIA} \approx 90\text{--}100$.
        </li>
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
        <strong>Question 99:</strong> High SiO2, Al2O3, rounded clasts and high ZTR index indicate _____ maturity of sediments.
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> low</div>
        <div class="option-item correct-option"><strong>(B)</strong> high</div>
        <div class="option-item"><strong>(C)</strong> moderate</div>
        <div class="option-item"><strong>(D)</strong> None of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) high</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Low Maturity</div>
        <p>
          <strong>Incorrect:</strong> Low-maturity sediments (such as first-cycle arkoses, lithic graywackes, or glacial tills) are characterized by the exact <em>reverse</em> of the parameters described: they have <strong>low $\text{SiO}_2$</strong> (abundant unstable rock fragments and labile mafic minerals), <strong>angular to sub-angular clasts</strong> (minimal abrasion), poor sorting with $> 15\%$ mud matrix (textural immaturity), and an extremely <strong>low ZTR index</strong> (typically $< 15\%$, dominated by chemically unstable pyroxenes, amphiboles, and olivine).
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — High Maturity</div>
        <p>
          <strong>Correct:</strong> By universal petrological principles (Boggs, 2014, p. 140; Hubert, 1962; Folk, 1951), the convergence of:
          (1) <strong>High $\text{SiO}_2$ and $\text{Al}_2\text{O}_3$ residual concentration:</strong> indicating profound chemical weathering that leached all soluble base cations ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Na}^+$);
          (2) <strong>Rounded clasts:</strong> demonstrating prolonged hydrodynamic transport, intense abrasion, and high textural maturity; and
          (3) <strong>High ZTR Index ($> 75\text{--}90\%$):</strong> proving that virtually all unstable heavy minerals have been eliminated, leaving only the ultra-stable trio (Zircon, Tourmaline, Rutile);
          unequivocally diagnoses a <strong>high (to supermature) maturity of sediments</strong>.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Moderate Maturity</div>
        <p>
          <strong>Incorrect:</strong> Moderate (submature) sediments exhibit partially rounded or sub-rounded clasts, intermediate $\text{SiO}_2$ contents, and moderate ZTR indices ($25\text{--}60\%$) with persistent intermediate-stability heavy minerals (e.g., epidote, garnet, staurolite). When a sediment reaches the threshold of rounded clasts alongside high $\text{SiO}_2$ and high ZTR, it has advanced fully into the high maturity classification.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — None of These</div>
        <p>
          <strong>Incorrect:</strong> Option (D) is false because "high" maturity is the well-established, mathematically and empirically validated answer in all standard sedimentary petrology curricula.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Matrix: Textural & Mineralogical Maturity Spectral Comparison</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sedimentary Parameter</th>
            <th>Low Maturity (Immature)</th>
            <th>Moderate Maturity (Submature / Mature)</th>
            <th>High Maturity (Supermature)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Quartz Content ($\text{SiO}_2$)</strong></td>
            <td>Low to Moderate ($35\text{--}65\%$)</td>
            <td>Moderate to High ($65\text{--}85\%$)</td>
            <td><strong>Very High ($> 90\text{--}99\%$, Quartz Arenite)</strong></td>
          </tr>
          <tr>
            <td><strong>Feldspar & Lithic Content</strong></td>
            <td>Very High ($> 25\text{--}50\%$, labile clasts abundant)</td>
            <td>Moderate ($10\text{--}25\%$)</td>
            <td><strong>Negligible ($< 1\text{--}5\%$, chemically stripped)</strong></td>
          </tr>
          <tr>
            <td><strong>Clast Roundness (Powers Scale)</strong></td>
            <td>Very angular to angular ($\rho = 0.12\text{--}0.25$)</td>
            <td>Sub-angular to sub-rounded ($\rho = 0.25\text{--}0.45$)</td>
            <td><strong>Rounded to well-rounded ($\rho = 0.60\text{--}0.90$)</strong></td>
          </tr>
          <tr>
            <td><strong>Matrix Content ($< 0.03\text{ mm}$)</strong></td>
            <td>High ($> 15\%$, Wacke clan)</td>
            <td>Low ($2\text{--}10\%$)</td>
            <td><strong>Zero / Trace ($< 1\%$, Arenite clan)</strong></td>
          </tr>
          <tr>
            <td><strong>Hubert's ZTR Index</strong></td>
            <td>Low ($< 25\%$; pyroxene, amphibole, olivine rich)</td>
            <td>Moderate ($25\text{--}70\%$; garnet, epidote present)</td>
            <td><strong>High ($> 75\text{--}95\%$; Zircon + Tourmaline + Rutile)</strong></td>
          </tr>
          <tr>
            <td><strong>Depositional Archetype</strong></td>
            <td>Alluvial fan, glacial till, proximal turbidite</td>
            <td>Fluvial point bar, deltaic distributary channel</td>
            <td><strong>Cratonic beach surf zone, eolian ergs, polycyclic sheets</strong></td>
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
        <p>A heavy mineral separation yields the following grain counts for the non-opaque transparent fraction: Zircon = 145 grains, Tourmaline = 85 grains, Rutile = 50 grains, Garnet = 12 grains, Epidote = 6 grains, Apatite = 2 grains. Calculate the ZTR Index and determine the mineralogical maturity of this sandstone.</p>
        <p><strong>Solution:</strong>
          Total non-opaque transparent heavy minerals:
          $$\sum = 145 + 85 + 50 + 12 + 6 + 2 = 300\text{ grains}$$
          Sum of Zircon + Tourmaline + Rutile:
          $$\text{ZTR} = 145 + 85 + 50 = 280\text{ grains}$$
          Hubert's ZTR Index:
          $$\text{ZTR Index} = \left( \frac{280}{300} \right) \times 100 = 93.33\%$$
          Since the ZTR Index exceeds $90\%$, the sandstone possesses an <strong>exceptionally high mineralogical maturity</strong>, indicative of polycyclic recycling or extreme chemical weathering in a stable cratonic setting.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain why a sediment can be texturally mature yet mineralogically immature, and provide a real-world geological example.</p>
        <p><strong>Solution:</strong>
          Textural and mineralogical maturity are decoupled:
          - <strong>Textural maturity</strong> is governed by mechanical energy, winnowing, and abrasion time.
          - <strong>Mineralogical maturity</strong> is governed by chemical weathering kinetics and climate.
          A real-world example is an <strong>arkosic beach sand or eolian dune sand in an arid desert</strong> (e.g., modern beach sands along the Gulf of California or Red Sea). High wave or wind energy thoroughly winnows out all clay matrix and produces very well-sorted, rounded sand grains (<strong>supermature texturally</strong>), yet because the hyper-arid climate lacks moisture for chemical hydrolysis, $35\text{--}45\%$ fresh, unweathered feldspars survive (<strong>mineralogically immature</strong>).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Calculate the Chemical Index of Alteration (CIA) for an unweathered granodiorite parent rock with molar proportions: $\text{Al}_2\text{O}_3 = 15.2$, $\text{CaO}^* = 3.8$, $\text{Na}_2\text{O} = 4.1$, $\text{K}_2\text{O} = 2.4$, and compare it to its weathered residual clay residue with $\text{Al}_2\text{O}_3 = 38.5$, $\text{CaO}^* = 0.2$, $\text{Na}_2\text{O} = 0.3$, $\text{K}_2\text{O} = 0.8$.</p>
        <p><strong>Solution:</strong>
          The formula for CIA is:
          $$\text{CIA} = \left[ \frac{\text{Al}_2\text{O}_3}{\text{Al}_2\text{O}_3 + \text{CaO}^* + \text{Na}_2\text{O} + \text{K}_2\text{O}} \right] \times 100$$
          - For unweathered parent granodiorite:
          $$\text{CIA}_{parent} = \frac{15.2}{15.2 + 3.8 + 4.1 + 2.4} \times 100 = \frac{15.2}{25.5} \times 100 \approx 59.6\%$$
          - For weathered clay residue:
          $$\text{CIA}_{residue} = \frac{38.5}{38.5 + 0.2 + 0.3 + 0.8} \times 100 = \frac{38.5}{39.8} \times 100 \approx 96.7\%$$
          The jump from $59.6\%$ to $96.7\%$ quantitatively documents the transition to extreme chemical/mineralogical maturity via base leaching.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Why are Zircon, Tourmaline, and Rutile the three minerals chosen by Hubert for the ZTR maturity index rather than other common accessories like magnetite or garnet?</p>
        <p><strong>Solution:</strong>
          Zircon ($\text{ZrSiO}_4$), Tourmaline, and Rutile ($\text{TiO}_2$) occupy the pinnacle of <strong>both chemical resistance and mechanical abrasion durability</strong>:
          1. <strong>Chemical Durability:</strong> They are virtually insoluble in all natural groundwater conditions (acidic, alkaline, or reducing).
          2. <strong>Mechanical Hardness:</strong> They have high Mohs hardness ($7\text{ to } 8$), resisting attrition during thousands of kilometers of fluvial or eolian transport.
          In contrast, magnetite is opaque (excluded from transparent counts) and alters to hematite/limonite; garnet is mechanically brittle and readily etches or dissolves in deep burial diagenesis (forming skeletal etched dodecahedra).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Define "polycyclic sediments" and explain their role in generating high-maturity quartz arenites.</p>
        <p><strong>Solution:</strong>
          <strong>Polycyclic (multicycle) sediments</strong> are sedimentary rocks composed of grains that have undergone multiple successive cycles of erosion, deposition, lithification, uplift, and re-erosion from older sedimentary strata rather than direct erosion from crystalline basement. A single sedimentary cycle under temperate conditions is rarely sufficient to eliminate all feldspars and round quartz grains; but repeating this cycle $3\text{ to } 5\text{ times}$ across hundreds of millions of years on a stable craton systematically eliminates all labile minerals, yielding pure quartz arenites ($> 99\%\text{ SiO}_2$) with $\text{ZTR} > 95\%$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Under Folk's textural maturity classification, why does the presence of only $6\%$ clay matrix immediately demote a sandstone with perfectly rounded, spherical quartz grains to the "Immature" category?</p>
        <p><strong>Solution:</strong>
          Folk's classification is hierarchical: <strong>Matrix winnowing is Step 1</strong>. If a sediment contains $> 5\%$ clay matrix, it indicates that current or wave action at the final depositional site was too sluggish or weak to wash away fine suspension mud. Even if the framework grains were rounded during a prior eolian cycle, the final depositional environment was low-energy (e.g., a quiet lagoon or turbidity flow), classifying it texturally as <strong>Immature (texturally inverted)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is a "textural inversion" in sedimentary petrology?</p>
        <p><strong>Solution:</strong>
          A <strong>textural inversion</strong> occurs when a sediment displays contradictory textural attributes that violate normal hydrodynamic equilibrium—such as:
          (a) Well-rounded sand grains floating in an abundant ($> 15\%$) fine clay matrix (e.g., tillites or pebbly mudstones).
          (b) A bimodal mixture of well-rounded large grains mixed with angular fine grains.
          Textural inversions indicate the mixing of sediments from two distinct energy regimes (e.g., eolian rounded dune grains blown into a quiet muddy lagoon, or polycyclic rounded grains dumped into a turbidite).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>How does the Plagioclase Index of Alteration (PIA) complement the CIA in assessing feldspar weathering maturity?</p>
        <p><strong>Solution:</strong>
          The Plagioclase Index of Alteration (PIA; Fedo et al., 1995) specifically monitors the destruction of plagioclase feldspar:
          $$\text{PIA} = \left[ \frac{\text{Al}_2\text{O}_3 - \text{K}_2\text{O}}{(\text{Al}_2\text{O}_3 - \text{K}_2\text{O}) + \text{CaO}^* + \text{Na}_2\text{O}} \right] \times 100$$
          Because calcic and sodic plagioclase weather significantly faster than potassic K-feldspar, PIA reaches near $100\%$ before K-feldspar is completely eliminated, allowing geochemists to isolate the early and intermediate stages of chemical weathering maturity in basin provenance studies.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=99,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q099_Sedimentary_Maturity_ZTR_Index_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q099: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q099()
