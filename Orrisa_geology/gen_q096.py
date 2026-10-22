#!/usr/bin/env python3
"""
Q096 Generator: Red Beds Continental Strata & Arid Paleoclimate
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q096():
    title = r"Q096: Sedimentary Petrology: Red Beds & Arid Paleoclimate | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Paleoclimatology"
    h1_title = "Q096: Sedimentary Red Beds: Genesis, Pigmentation & Arid Continental Climates"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 96<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 6: Mudrocks / Red Beds, pp. 168–172; Fig. 6.12); T.R. Walker (1967, 1976), <em>Formation of Red Beds in Modern and Ancient Deserts</em> (GSA Bulletin); F.J. Pettijohn, <em>Sedimentary Rocks</em> (3rd Ed., Harper & Row); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PALEOCLIMATIC FRAMEWORK OF RED BEDS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Mineralogy & Paleoclimatic Framework of Red Beds</div>
    <div class="card-body">
      <p>
        In sedimentary geology and paleoclimatology (Boggs, 2014, pp. 168–172; Walker, 1967; Pettijohn, 1975), <strong>red beds</strong> are defined as thick, extensive sequences of continental (terrestrial) siliciclastic sedimentary rocks—predominantly sandstones, siltstones, mudrocks, and conglomerates—that possess a conspicuous, uniform <strong>red, reddish-brown, brick-red, or maroon coloration</strong>.
      </p>
      <p>
        This coloration is produced by microscopic coatings and grain-rimming films of authigenic <strong>ferric iron oxide (principally hematite, $\alpha\text{-Fe}_2\text{O}_3$)</strong> enclosing detrital quartz and feldspar grains or dispersed throughout the fine argillaceous matrix. In the global stratigraphic record (e.g., the Devonian Old Red Sandstone, Permian-Triassic New Red Sandstone, and the Gondwana continental beds), red beds are canonically diagnostic of <strong>arid to semi-arid, highly oxidizing continental climatic conditions</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q96/boggs_p170_sedimentary_red_beds_arid.png" alt="Genesis and Diagenesis of Continental Red Beds from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 96.1 — Petrogenesis and Diagenetic Evolution of Continental Red Beds:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 170). Illustrates the intrastratal dissolution of iron-bearing ferromagnesian silicates in oxidizing, alkaline desert groundwater, leading to the precipitation of pigmentary hematite coatings around framework grains.
        </div>
      </div>

      <h4>Mineralogical and Chemical Nature of the Red Pigment</h4>
      <ul>
        <li><strong>Coloring Agent:</strong> The vivid red coloration requires only a minuscule total iron concentration—as little as <strong>$0.5\text{ to } 2.0\text{ wt}\%\text{ Fe}_2\text{O}_3$</strong>—provided it is present as finely dispersed, sub-micron pigmentary <strong>hematite ($\alpha\text{-Fe}_2\text{O}_3$)</strong> coating grain surfaces. Coarser, specular hematite flakes appear metallic black/grey and do not impart a brick-red hue.</li>
        <li><strong>Absence of Organic Matter:</strong> In arid and desert environments, the sparse vegetation produces virtually zero humic or fulvic organic acids. Without organic carbon, anaerobic sulfate-reducing and iron-reducing bacteria cannot flourish; thus, iron remains locked in its oxidized ferric state ($\text{Fe}^{3+}$) rather than being reduced to soluble ferrous iron ($\text{Fe}^{2+}$) or sulfidized into pyrite ($\text{FeS}_2$), which would turn the rock green, grey, or black.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: GENETIC MODELS & INCLUDED ARID SUITES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Genetic Models: Walker's Diagenetic Model vs. Associated Arid Lithofacies</div>
    <div class="card-body">
      <h4>Diagenetic Intrastratal Alteration Model (Walker, 1967)</h4>
      <p>
        Historically, Paul D. Krynine (1949) argued that red beds represented detrital lateritic soil washed from tropical uplands into rapidly sinking basins. However, monumental field and petrographic work by <strong>T.R. Walker (1967, 1976)</strong> on modern desert basins (such as the Sonoran Desert and Baja California) conclusively established that:
      </p>
      <ol>
        <li>Sediments in arid basins are initially deposited as <strong>drab, greyish-tan, unpigmented sands and muds</strong> containing detrital ferromagnesian silicates (hornblende, augite, biotite, magnetite).</li>
        <li>In well-aerated, oxidizing, mildly alkaline desert groundwaters, these detrital silicates undergo slow post-depositional <strong>intrastratal dissolution</strong>:
          $$\text{Ferromagnesian Silicates} + \text{O}_2 + \text{H}_2\text{O} \rightarrow \text{Dissolved } \text{Fe}^{2+} \xrightarrow{\text{oxidation}} \text{Fe}^{3+} \rightarrow \text{Amorphous Ferrihydrite}$$
        </li>
        <li>Over thousands to millions of years, the metastable, amorphous ferric oxyhydroxides age and dehydrate spontaneously into stable microcrystalline <strong>hematite ($\alpha\text{-Fe}_2\text{O}_3$)</strong>:
          $$2\text{FeO(OH)} \rightarrow \text{Fe}_2\text{O}_3 + \text{H}_2\text{O}$$
        </li>
      </ol>

      <h4>Associated Sedimentary Features in Arid Red-Bed Basins</h4>
      <ul>
        <li><strong>Interbedded Evaporites:</strong> Red beds frequently grade laterally or vertically into bedded gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$), anhydrite, and halite deposits, confirming high evaporation-to-precipitation ratios ($E \gg P$).</li>
        <li><strong>Caliche / Calcrete Paleosols:</strong> Nodular carbonate horizons form within the vadose zone due to intense evaporative capillary draw of calcium-rich waters.</li>
        <li><strong>Eolian Cross-Bedding & Ventifacts:</strong> Large-scale tabular and trough cross-bedding (draa/seif dunes) and wind-abraded ventifact pebbles.</li>
        <li><strong>Desiccation Mudcracks:</strong> Sun-cracked polygonal mudstone horizons in ephemeral playa lake margins.</li>
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
        <strong>Question 96:</strong> Sedimentary rocks that are formed in arid climatic condition are classified as :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Ironstone</div>
        <div class="option-item correct-option"><strong>(B)</strong> Red beds</div>
        <div class="option-item"><strong>(C)</strong> Cherty sandstone</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) Red beds</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Ironstone</div>
        <p>
          <strong>Incorrect:</strong> In sedimentary petrology, an <strong>ironstone</strong> is defined strictly as a sedimentary rock containing greater than <strong>$15\text{ wt}\%\text{ iron}$</strong> (e.g., oolitic ironstones like the Minette ore of Lorraine or chamosite/siderite ironstones). Ironstones are predominantly <strong>shallow marine or brackish-lagoonal</strong> deposits formed in warm, humid, tropical or sub-tropical waters where intense chemical weathering on adjacent landmasses leaches iron and delivers it via rivers into restricted coastal basins. They are not characteristic of arid climatic conditions.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Red Beds</div>
        <p>
          <strong>Correct:</strong> By universal geological definition (Boggs, 2014, p. 168; Pettijohn, 1975; Walker, 1967), <strong>red beds</strong> are the quintessential sedimentary rock suites formed in <strong>arid to semi-arid continental climatic regimes</strong>. The combination of intense oxidizing conditions, lack of vegetative organic matter, eolian sand transport, ephemeral playa drainage, and intrastratal hematite pigmentation uniquely defines red-bed deposition in desert basins.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Cherty Sandstone</div>
        <p>
          <strong>Incorrect:</strong> A <em>cherty sandstone</em> is a sandstone cemented by microcrystalline quartz/chalcedony (chert) or containing abundant detrital chert pebbles. Chert cementation and chert pebble deposition occur in a wide variety of temperate, marine, and fluvial environments and have no unique or defining genetic association with arid climates.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because neither ironstones (which are marine/humid) nor cherty sandstones are genetically defined by or restricted to arid climates, option (D) is completely untenable. The official and scientific correct answer is exclusively <strong>(B) Red beds</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Petrographic & Paleoclimatic Analysis: Iron-Rich & Climatically Sensitive Strata</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sedimentary Rock Type</th>
            <th>Total Iron Content ($\text{Fe}$)</th>
            <th>Dominant Iron Mineralogy</th>
            <th>Primary Depositional Environment</th>
            <th>Diagnostic Paleoclimatic Regime</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Red Beds</strong></td>
            <td>Low ($0.5\text{ to } 3.0\text{ wt}\%$)</td>
            <td>Authigenic pigmentary Hematite ($\alpha\text{-Fe}_2\text{O}_3$)</td>
            <td>Continental: Alluvial fans, braided rivers, eolian dunes, playa mudflats</td>
            <td><strong>Arid to semi-arid, highly oxidizing, low rainfall</strong></td>
          </tr>
          <tr>
            <td><strong>Ironstone (Phanerozoic)</strong></td>
            <td>Very High ($> 15.0\text{ wt}\%$)</td>
            <td>Chamosite (Fe-chlorite), Siderite ($\text{FeCO}_3$), Goethite, Berthierine</td>
            <td>Shallow marine shelves, estuaries, restricted lagoons</td>
            <td><strong>Warm, humid tropical/subtropical with intense terrestrial leaching</strong></td>
          </tr>
          <tr>
            <td><strong>Banded Iron Formation (BIF)</strong></td>
            <td>Very High ($20\text{ to } 40\text{ wt}\%$)</td>
            <td>Alternating bands of Magnetite ($\text{Fe}_3\text{O}_4$) / Hematite and microcrystalline chert</td>
            <td>Precambrian deep marine basins and continental shelves</td>
            <td><strong>Anoxic Archean/Paleoproterozoic oceans before the Great Oxidation Event</strong></td>
          </tr>
          <tr>
            <td><strong>Bog Iron Ore</strong></td>
            <td>Moderate to High ($10\text{ to } 25\text{ wt}\%$)</td>
            <td>Limonite, Goethite, bacterial iron oxyhydroxides</td>
            <td>Freshwater peat swamps, bogs, and marshes</td>
            <td><strong>Cool-temperate, humid, waterlogged reducing-to-oxidizing interface</strong></td>
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
        <p>A thick succession of brick-red sandstones displays large-scale trough cross-bedding with foreset dips up to $34^\circ$, frosted quartz grains, and interbedded desiccation-cracked mudstones with nodular gypsum. Name the rock suite, identify the depositional environment, and specify the paleoclimate.</p>
        <p><strong>Solution:</strong> The succession represents a <strong>continental red bed suite</strong>. The high foreset dips ($34^\circ$, matching the angle of repose of dry sand), frosted quartz grains (aeolian impact pitting), desiccation mudcracks, and nodular gypsum indicate an <strong>eolian desert dune and ephemeral playa lake system</strong> formed under an <strong>arid to hyper-arid continental paleoclimate</strong>.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Why does a sediment require only $1\%$ hematite to become vivid brick-red, whereas a rock containing $10\%$ magnetite or siderite remains dull grey or green?</p>
        <p><strong>Solution:</strong>
          Hematite ($\alpha\text{-Fe}_2\text{O}_3$) in red beds occurs as ultra-fine, sub-micron colloidal particles ($< 0.1\mu\text{m}$) with an exceptionally high specific surface area, forming continuous thin optical pigment films coating thousands of translucent quartz grains. Its intense intrinsic absorption band in the blue-green spectrum and strong reflectance in the red spectrum produces maximum visual pigmentation. In contrast, magnetite and siderite occur as discrete, coarser crystals that do not form dispersive surface pigment rinds, keeping the rock grey or brownish-green.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Contrast T.R. Walker's intrastratal alteration model with P.D. Krynine's laterite model for the origin of red beds.</p>
        <p><strong>Solution:</strong>
          - <strong>Krynine's Model (Detrital/Laterite):</strong> Posited that the red hematite was formed in upland tropical lateritic soils under warm, humid climates and washed mechanically into adjacent sinking basins as detrital red muds.
          - <strong>Walker's Model (Diagenetic/In-Situ):</strong> Demonstrated that modern desert sands are deposited drab and unpigmented. In arid basins, oxidizing, alkaline groundwater decomposes detrital ferromagnesian minerals (hornblende, biotite) in-situ during post-depositional diagenesis, precipitating iron oxyhydroxides that dehydrate over geological time into pigmentary hematite. Walker's diagenetic model is now the accepted paradigm for most ancient arid red beds.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Why are red beds virtually absent in the Archean and early Paleoproterozoic geological record prior to $\sim 2.4\text{ Ga}$?</p>
        <p><strong>Solution:</strong>
          Formation of hematite ($\text{Fe}^{3+}$) requires atmospheric oxygen. Prior to the <strong>Great Oxidation Event (GOE)</strong> at $\sim 2.4\text{--}2.2\text{ Ga}$, Earth's atmosphere was anoxic ($P_{\text{O}_2} < 10^{-5}\text{ PAL}$). Under anoxic conditions, iron weathered from minerals remained in the soluble ferrous state ($\text{Fe}^{2+}$) and was washed into the oceans, preventing subaerial hematite pigmentation. The sudden appearance of continental red beds at $\sim 2.2\text{ Ga}$ serves as a primary geological benchmark for atmospheric oxygenation.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Explain the origin of green reduction spots (haloes) frequently observed in brick-red sandstones and shales.</p>
        <p><strong>Solution:</strong>
          Green reduction spots (often containing a tiny dark center) form during burial diagenesis where a localized speck of organic matter (e.g., plant spore, fragment of organic carbon) or a detrital radioactive mineral (uraninite) is embedded in the red sediment. The organic carbon provides a reducing micro-environment where anaerobic microbes reduce ferric iron back to soluble ferrous iron ($\text{Fe}^{3+} \rightarrow \text{Fe}^{2+}$), dissolving the red hematite coating and leaving the green color of ferrous silicate clays (chlorite, illite).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is "caliche" or "calcrete" and why is it a diagnostic paleoclimatic associate of sedimentary red beds?</p>
        <p><strong>Solution:</strong>
          Caliche (calcrete) is an authigenic pedogenic accumulation of calcium carbonate ($\text{CaCO}_3$) forming nodules, hardpans, or laminar crusts in the upper soil profile. It forms exclusively in <strong>arid to semi-arid climates (annual precipitation between $100\text{ and } 500\text{ mm}$)</strong> where seasonal rainfall dissolves surface carbonates, which are then drawn upward by intense solar evaporation and capillary action, precipitating in the vadose B-horizon. Its presence in red-bed sequences definitively confirms an arid paleoclimate.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is the difference between an "arkose" and an "orthoquartzite" in red bed basins, and what does the preservation of fresh feldspar signify about the climate?</p>
        <p><strong>Solution:</strong>
          An <strong>arkose</strong> contains $> 25\%$ feldspar, whereas an <strong>orthoquartzite</strong> contains $> 95\%$ quartz. In red bed basins, arkosic sandstones are extremely common (e.g., New Red Sandstone) because the <strong>arid climate lacks moisture</strong> to drive chemical hydrolysis ($2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \rightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 + \dots$). Consequently, chemically unstable detrital feldspars survive mechanical breakdown and are preserved fresh and unweathered in the sediment, directly confirming aridity.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>In paleomagnetism, why are red beds extensively sampled for magnetic polarity and continental drift reconstructions?</p>
        <p><strong>Solution:</strong>
          The fine pigmentary and specular hematite in red beds carries an exceptionally stable <strong>chemical remanent magnetization (CRM)</strong> and detrital remanent magnetization (DRM). Hematite has a very high Curie temperature ($T_c = 675^\circ\text{C}$) and extraordinarily high magnetic coercivity ($> 1\text{--}5\text{ Tesla}$), making it virtually immune to secondary viscous magnetic overprinting and preserving pristine paleomagnetic pole positions from deep geological time.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=96,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q096_Red_Beds_Arid_Paleoclimate_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q096: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q096()
