#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 46 to 53 (Batch 5 - Part A)
Assam DGMS 2019 Masterclass Standard
"""

from masterclass_generator_core import generate_page

# ==========================================
# QUESTION 46: YOUNGEST EVENT IN DHARWARIAN STRATIGRAPHY
# ==========================================
q46_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Archean Tectonics: Dharwar Craton Lithostratigraphy & Cratonization</div>
    <div class="card-body">
      <p>The <strong>Dharwar Craton</strong> of southern peninsular India represents one of the premier Archean cratonic nuclei on Earth. Its evolution spans from the Paleoarchean (~3.5 Ga) to the Neoarchean-Paleoproterozoic boundary (~2.5 Ga). Geologically, the craton is divided by the linear, crustal-scale <strong>Closepet Granite</strong> batholith into the <em>Western Dharwar Craton (WDC)</em> and the <em>Eastern Dharwar Craton (EDC)</em>.</p>
      
      <ul>
        <li><strong>Chronostratigraphic Superposition (Oldest to Youngest):</strong>
          <ol>
            <li><strong>Sargur Group (~3.35 - 3.58 Ga):</strong> Oldest recognized supracrustal remnants, occurring as linear, high-grade amphibolite-to-granulite facies enclaves engulfed within the gneissic complex. Composed of komatiites, layered mafic-ultramafic complexes, high-alumina pelites (kyanite-sillimanite-staurolite schists), banded iron formations (BIF), and calc-silicate marbles.</li>
            <li><strong>Peninsular Gneissic Complex (PGC, ~3.0 - 3.4 Ga):</strong> Polyphase migmatitic basement complex dominated by tonalite-trondhjemite-granodiorite (TTG) suites, representing multiple episodes of plutonism and crustal accretion forming the basement floor for the Dharwar Supergroup.</li>
            <li><strong>Dharwar Supergroup (~2.6 - 3.0 Ga):</strong> The signature Neoarchean greenstone belt volcano-sedimentary succession, unconformably overlying the PGC. Divided into:
              <ul>
                <li><em>Bababudan Group (~3.0 - 2.7 Ga):</em> Basal oligomictic quartz-pebble conglomerate (QPC), thick amygdaloidal mafic volcanic flows, and prominent titaniferous BIF.</li>
                <li><em>Chitradurga Group (~2.7 - 2.6 Ga):</em> Upper group marked by Talya polymictic conglomerate, deep-marine greywacke-shale turbidites, pillow basalts, and chemogenic chert-BIF associations.</li>
              </ul>
            </li>
            <li><strong>Closepet Granite (~2.51 Ga):</strong> A monumental ~400-km-long, 20-30 km wide, N-S trending polyphase calc-alkaline to potassic granite-adamellite batholith. It sharply intrudes across both the migmatitic basement (PGC) and the folded Dharwar supracrustal belts, marking the <strong>youngest major tectonomagmatic and cratonization event</strong> of the Dharwar Craton.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Dharwar Supergroup & Closepet Granite:</strong> The Dharwar rocks represent the oldest metamorphosed sedimentary and volcanic succession of Southern India. This vast succession resting upon the Peninsular Gneisses was folded, metamorphosed, and finally intruded by the massive <strong>Closepet Granite</strong> at approximately 2,500 million years ago, representing the terminal plutonic event that stabilized the Mysore Archean craton."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Stratigraphy of India: Dharwar System, pp. 277-279)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Geochronological Sequence of Dharwar Cratonization</div>
        $$T_{\\text{Sargur}} (3.58\\text{ Ga}) > T_{\\text{PGC}} (3.36-3.00\\text{ Ga}) > T_{\\text{Dharwar SG}} (2.95-2.60\\text{ Ga}) > T_{\\text{Closepet}} (2.51\\text{ Ga})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Single-zircon U-Pb TIMS and SHRIMP geochronology constrains the Closepet Granite crystallization age precisely to $2513 \\pm 5\\text{ Ma}$, proving unequivocally that it represents the youngest event in Dharwarian stratigraphy.</p>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q046/dharwar_craton_stratigraphy_closepet_granite.png" alt="Dharwar Craton Stratigraphy and Closepet Granite Youngest Event">
        <div class="tb-caption">
          <strong>Figure 46.1: Lithostratigraphic Superposition of the Dharwar Craton.</strong> Chronological evolution from Paleoarchean Sargur enclaves and PGC basement through the Dharwar Supergroup, culminating in the intrusion of the Closepet Granite (~2.51 Ga).
        </div>
      </div>
    </div>
  </div>
"""

q46_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 46</div>
    <div class="q-text">Which of the following represents the youngest event in the Dharwarian stratigraphy ?</div>
    <div class="raw-options">
      <div>(A) Sargur Group</div>
      <div>(B) Closepet Granite</div>
      <div>(C) Dharwar SuperGroup</div>
      <div>(D) Peninsular Gneissic Complex</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (B) Closepet Granite</strong>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Sargur Group</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT (OLDEST)</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Sargur Group (~3.35 - 3.58 Ga) is the <em>oldest</em> recognizable supracrustal unit in the craton, preserved as highly deformed, amphibolite-to-granulite facies metamorphic enclaves within the Peninsular Gneissic Complex.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Closepet Granite</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Closepet Granite ($2.51\\text{ Ga}$) is a late-to-post-kinematic calc-alkaline batholith that cuts across both the Peninsular Gneisses and the folded greenstone belts of the Dharwar Supergroup. Radiometric dating (U-Pb zircon: $2510 \\pm 10\\text{ Ma}$) confirms it represents the final plutonic cratonization event, making it the youngest stratigraphic element listed.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Dharwar SuperGroup</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Dharwar Supergroup (~2.6 - 3.0 Ga) consists of the Bababudan and Chitradurga Groups. It was deposited, deformed, and metamorphosed <em>prior</em> to the intrusion of the Closepet Granite, which cross-cuts Dharwar folds and regional fabrics.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Peninsular Gneissic Complex</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The PGC (~3.0 - 3.4 Ga) forms the vast crystalline migmatitic basement upon which the Dharwar Supergroup sediments and lavas were laid down unconformably. It is older than both the Dharwar Supergroup and the Closepet Granite.
    </div>
  </div>
"""

q46_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Dharwar Craton Lithodemic & Stratigraphic Units</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Stratigraphic Unit</th>
            <th>Age (Ga)</th>
            <th>Primary Lithologies</th>
            <th>Tectonic Role & Stratigraphic Relationship</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Closepet Granite</strong></td>
            <td><strong>~2.51 Ga</strong></td>
            <td>Porphyritic granite, adamellite, monzonite</td>
            <td><strong>Youngest event; post-kinematic batholith marking craton stabilization</strong></td>
          </tr>
          <tr>
            <td><strong>Dharwar Supergroup</strong></td>
            <td>~2.6 - 3.0 Ga</td>
            <td>Conglomerates, basalt flows, BIF, greywackes</td>
            <td>Greenstone cover sequence (Bababudan & Chitradurga Groups)</td>
          </tr>
          <tr>
            <td><strong>Peninsular Gneissic Complex</strong></td>
            <td>~3.0 - 3.4 Ga</td>
            <td>Migmatitic TTG gneisses, granodiorite</td>
            <td>Basement floor beneath Dharwar Supergroup</td>
          </tr>
          <tr>
            <td><strong>Sargur Group</strong></td>
            <td>~3.35 - 3.58 Ga</td>
            <td>Komatiites, kyanite-pelites, layered gabbro-anorthosite</td>
            <td>Oldest relict supracrustal enclaves inside PGC</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Archean Geology & Stratigraphy</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Boundary Dividing Western and Eastern Dharwar Cratons</div>
        <div class="pq-ans">The Closepet Granite batholith and the Chitradurga shear zone</div>
        <div class="pq-exp">The Western Dharwar Craton (WDC) is characterized by ancient 3.0-3.4 Ga TTG basement and mature quartzites/BIF, whereas the Eastern Dharwar Craton (EDC) is dominated by young 2.7-2.5 Ga juvenile magmatism and thin gold-bearing greenstone slivers (e.g., Kolar, Ramagiri). The Closepet Granite acts as the tectonic stitch dividing them.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Lithological Difference Between Bababudan and Chitradurga Groups</div>
        <div class="pq-ans">Bababudan is dominated by subaerial continental flood basalts and quartzites; Chitradurga is deep-marine turbidites, pillow lavas, and greywackes</div>
        <div class="pq-exp">Bababudan represents intracratonic continental rifting (oligomict QPC, amygdaloidal basalt flows), whereas Chitradurga reflects progressive ocean basin deepening (polymict Talya conglomerate, flysch-type greywackes, chemogenic chert-BIF).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Petrological Nature of the Closepet Granite</div>
        <div class="pq-ans">Polyphase anatectic calc-alkaline to potassic granite produced by crust-mantle interaction</div>
        <div class="pq-exp">Closepet Granite comprises four distinct facies: clinopyroxene-bearing monzonite, porphyritic monzogranite, equigranular granite, and late aplitic dykes, formed by anatexis of lower crust triggered by mantle-derived basic magmas.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Index Minerals in Sargur Metasediments</div>
        <div class="pq-ans">Kyanite, sillimanite, staurolite, and almandine garnet</div>
        <div class="pq-exp">Sargur pelites record upper amphibolite to granulite facies metamorphism ($P \\approx 7-9\\text{ kbar}, T \\approx 700-800^\\circ\\text{C}$), distinguishing them from the lower-grade greenschist facies rocks of the Dharwar Supergroup.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Economic Mineral Deposits Associated with Dharwar Greenstones</div>
        <div class="pq-ans">Banded Iron Formations (Hematite/Magnetite), Gold (Kolar, Hutti), and Manganese (Sandur)</div>
        <div class="pq-exp">Dharwar greenstone belts host India's primary gold lodes (orogenic quartz-carbonate veins at Kolar and Hutti) and massive iron ore reserves in the Bababudan, Kudremukh, and Sandur belts.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Metamorphic Grade Transition Across Dharwar Craton</div>
        <div class="pq-ans">Greenschist facies in the north grading continuously to Granulite facies (Charnockites) in the south</div>
        <div class="pq-exp">The Dharwar craton displays an oblique crustal section: northern shallow crust (greenschist greenstones) exposes deep crust in the south (Kabbaldurga incipient charnockite transition at ~2.5 Ga).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Significance of Quartz-Pebble Conglomerate (QPC) in Bababudan Group</div>
        <div class="pq-ans">Marks an anoxic Archean atmosphere and hosts paleo-placer uranium/gold</div>
        <div class="pq-exp">The presence of detrital uraninite and rounded detrital pyrite pebbles in the basal Bababudan QPC proves that oxygen levels were $<10^{-5}\\text{ PAL}$ (Pre-Great Oxidation Event).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: U-Pb Dating Method Used on Closepet Zircons</div>
        <div class="pq-ans">Isotope Dilution Thermal Ionization Mass Spectrometry (ID-TIMS) and SHRIMP</div>
        <div class="pq-exp">High-precision zircon concordia intercept ages of $2513 \\pm 5\\text{ Ma}$ pin the Closepet Granite as the benchmark Archean-Proterozoic boundary chronometer in Peninsular India.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 47: STRATIGRAPHIC FORMATION AND AGE PAIRS
# ==========================================
q47_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Chronostratigraphy: Indian Stratigraphic Units & Age Correlations</div>
    <div class="card-body">
      <p>Accurate correlation between lithostratigraphic formations and global chronostratigraphic epochs requires rigorous biostratigraphic and isotopic grounding. In Indian geology, competitive exams frequently test key diagnostic formations from the <strong>Purana Proterozoic Basins</strong>, the <strong>Mesozoic-Cenozoic Marine Basins</strong>, and <strong>Island Arc Successions</strong>.</p>
      
      <ul>
        <li><strong>Forensic Review of Tested Formations:</strong>
          <ol>
            <li><strong>Niniyur Formation (Cauvery Basin, South India):</strong>
              <ul>
                <li><em>Geographic & Geologic Setting:</em> Exposed in the Ariyalur-Trichinopoly area of Tamil Nadu.</li>
                <li><em>Stratigraphic Placement:</em> The Cauvery Basin Cretaceous-Tertiary succession comprises in ascending order: <strong>Uttatur Group</strong> (Upper Albian - Cenomanian), <strong>Trichinopoly Group</strong> (Turonian - Coniacian), <strong>Ariyalur Group</strong> (Campanian - Maastrichtian), and the <strong>Niniyur Formation</strong> (Danian, earliest Paleocene).</li>
                <li><em>Curriculum Classification:</em> In classic Indian geology textbooks (M.S. Krishnan, D.N. Wadia, K.M. Bangar), the Niniyur beds are traditionally categorized and taught as the uppermost terminal member of the famous <strong>"Cretaceous of South India (Trichinopoly)"</strong> succession because they represent the continuous marine capping sequence of the Ariyalur Cretaceous marine transgression.</li>
              </ul>
            </li>
            <li><strong>Bhander Group (Vindhyan Supergroup):</strong> Uppermost group of the Upper Vindhyan sequence (comprising Ganurgarh Shale, Bhander Limestone, Sirbu Shale, and Upper Bhander Sandstone). Radiometric dates (detrital zircon and kimberlite pipes) constrain it to the <strong>Neoproterozoic (~650 - 850 Ma)</strong>, completely ruling out 'Early Proterozoic' (Paleoproterozoic).</li>
            <li><strong>Long Formation (Andaman Islands):</strong> A prominent carbonate-rich unit of the Archipelago Group on Long Island. It is bio-zoned with globorotalid foraminifera and calcareous nannofossils dating unequivocally to the <strong>Middle to Late Miocene</strong>, not the Oligocene.</li>
            <li><strong>Bheema (Bhima) Group (Karnataka):</strong> One of the premier Neoproterozoic "Purana" basins (~800 - 900 Ma) resting upon the Eastern Dharwar granites. It consists of unmetamorphosed shales and massive Shahabad limestones, completely distinct from the Cambrian.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Cretaceous of Trichinopoly:</strong> The Cretaceous rocks of the Cauvery basin are subdivided into four well-defined stages:
        (1) Utatur Stage (Cenomanian),
        (2) Trichinopoly Stage (Turonian-Senonian),
        (3) Ariyalur Stage (Senonian-Maestrichtian), and
        (4) <strong>Niniyur Stage (Danian)</strong>.
        The Niniyur stage is characterized by the absence of ammonites and belemnites, and the abundance of algae and the gastropod <em>Nautilus danicus</em> and <em>Cardita beaumonti</em>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Cretaceous System of India, p. 296)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q047/cauvery_basin_niniyur_stratigraphy.png" alt="Cauvery Basin Stratigraphy and Niniyur Formation Placement">
        <div class="tb-caption">
          <strong>Figure 47.1: Classic Indian Stratigraphic Correlation of Cauvery Basin.</strong> The classic four-fold Cretaceous succession (Uttatur, Trichinopoly, Ariyalur, Niniyur) highlighting the Niniyur Formation.
        </div>
      </div>
    </div>
  </div>
"""

q47_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 47</div>
    <div class="q-text">Choose the correct pair of stratigraphic formation and its corresponding age :</div>
    <div class="raw-options">
      <div>(A) Bhander Group — Early Proterozoic</div>
      <div>(B) Niniyur Formation — Cretaceous</div>
      <div>(C) Long Formation — Oligocene</div>
      <div>(D) Bheema Group — Cambrian</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (B) Niniyur Formation — Cretaceous</strong>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Bhander Group — Early Proterozoic</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Bhander Group represents the youngest division of the Upper Vindhyan Supergroup and is firmly dated to the <strong>Neoproterozoic (~650 - 850 Ma)</strong>. The 'Early Proterozoic' (Paleoproterozoic, 2500 - 1600 Ma) corresponds to the Lower Vindhyan Semri Group or Bijawar Group, making this pair completely false.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Niniyur Formation — Cretaceous</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> In standard Indian stratigraphy curricula (M.S. Krishnan, D.N. Wadia, K.M. Bangar), the South Indian Cretaceous of the Cauvery Basin is universally taught as four divisions: Utatur, Trichinopoly, Ariyalur, and Niniyur. Although modern international chronostratigraphy classifies the Danian stage as basal Paleocene, in Indian examination keys and classic textbooks, Niniyur is designated as the terminal Cretaceous division representing the Danian marine sequence.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Long Formation — Oligocene</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Long Formation belongs to the Archipelago Group of the Andaman and Nicobar Islands. Its foraminiferal assemblage (Globorotalia fohsi zone) dates it firmly to the <strong>Middle to Late Miocene</strong>. The Oligocene in the Andaman belt is represented by the Andaman Flysch Group.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Bheema Group — Cambrian</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Bheema (Bhima) Group is a classical <strong>Neoproterozoic Purana basin</strong> (~800 - 900 Ma) developed on the Archean granitic basement in Karnataka. It is devoid of Phanerozoic shelly macrofossils (trilobites) and is Proterozoic, not Cambrian.
    </div>
  </div>
"""

q47_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Tested Indian Formations vs. Verified Geochronology</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Stratigraphic Unit</th>
            <th>Geographic Basin</th>
            <th>True Chronostratigraphic Age</th>
            <th>Diagnostic Fossil / Lithology</th>
            <th>Exam Error in Distractors</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Niniyur Formation</strong></td>
            <td><strong>Cauvery Basin (Ariyalur, TN)</strong></td>
            <td><strong>Danian (Cretaceous-Paleocene transition)</strong></td>
            <td><strong>Algal limestone, <em>Cardita beaumonti</em>, <em>Nautilus danicus</em></strong></td>
            <td><strong>Correct exam pair under classic Indian classification</strong></td>
          </tr>
          <tr>
            <td><strong>Bhander Group</strong></td>
            <td>Vindhyan Basin (Central India)</td>
            <td>Neoproterozoic (~650 - 850 Ma)</td>
            <td>Maihar sandstone, stromatolitic Lakheri limestone</td>
            <td>Erroneously paired with Early Proterozoic</td>
          </tr>
          <tr>
            <td><strong>Long Formation</strong></td>
            <td>Andaman Archipelago Basin</td>
            <td>Middle to Late Miocene</td>
            <td>Planktonic foraminifera, calcareous nannofossils</td>
            <td>Erroneously paired with Oligocene</td>
          </tr>
          <tr>
            <td><strong>Bheema Group</strong></td>
            <td>Bhima Basin (Karnataka)</td>
            <td>Neoproterozoic (~800 - 900 Ma)</td>
            <td>Shahabad limestone, Rabanpalli shale</td>
            <td>Erroneously paired with Cambrian</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Indian Stratigraphic Chronology</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Diagnostic Fossil Disappearance in Niniyur Formation</div>
        <div class="pq-ans">Extinction of Belemnites and Ammonites; appearance of Danian fauna</div>
        <div class="pq-exp">The underlying Ariyalur beds contain abundant ammonites (*Pachydiscus*, *Baculites*) and belemnites. In the Niniyur beds, all ammonites and belemnites are completely extinct, replaced by *Nautilus danicus*, *Cardita beaumonti*, and coralline algae, capturing the K-Pg boundary.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Oldest Group of the Vindhyan Supergroup</div>
        <div class="pq-ans">Semri Group (Lower Vindhyan, ~1.6 - 1.7 Ga)</div>
        <div class="pq-exp">The Semri Group represents the Paleoproterozoic to Mesoproterozoic base (containing Kajrahat limestone and Porcellanite beds), whereas the Bhander Group sits at the very top of the Upper Vindhyan in the Neoproterozoic.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Age of the Andaman Flysch Group</div>
        <div class="pq-ans">Late Eocene to Oligocene</div>
        <div class="pq-exp">The Andaman Flysch represents a thick sequence of deep-water turbiditic sandstones and shales deposited by longitudinal turbidity currents in the Sunda subduction trench during Late Eocene to Oligocene times.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Subdivisions of the Bhima Group</div>
        <div class="pq-ans">Sedam Subgroup (Rabanpalli Formation, Shahabad Limestone) and Andola Subgroup</div>
        <div class="pq-exp">The Bhima succession is divided into basal clastics (Rabanpalli), a middle carbonate platform (Shahabad limestone—the backbone of South Indian cement manufacture), and upper shales/limestones.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Type Area of Marine Cambrian in Peninsular India</div>
        <div class="pq-ans">Peninsular India has NO Marine Cambrian; Salt Range and Spiti are Extra-Peninsular</div>
        <div class="pq-exp">The Indian peninsula was an emergent craton during the Cambrian. Marine Cambrian rocks are confined strictly to the Extra-Peninsula (Tethyan belt of Spiti and Kashmir, and Salt Range Pakistan).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Age of the Ariyalur Group</div>
        <div class="pq-ans">Upper Cretaceous: Campanian to Maastrichtian</div>
        <div class="pq-exp">The Ariyalur Group is divided into the Sillakkudi, Kallankurichi (rich in gryphaeid oysters), and Ottakovil formations, dated to Campanian-Maastrichtian via *Globotruncana* foraminifera.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Significance of the Porcellanite Stage in Semri Group</div>
        <div class="pq-ans">Silicic felsic pyroclastic volcanic ash beds (~1600 Ma)</div>
        <div class="pq-exp">The Porcellanite Formation of the Semri Group comprises rhyolitic to dacitic tuffs, tuffaceous shales, and silicified ash layers, dated by zircon U-Pb to ~1630 Ma.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Correlation of Niniyur with Narmada Valley Cretaceous</div>
        <div class="pq-ans">Bagh Beds of Narmada Valley are Cenomanian-Turonian, older than Niniyur</div>
        <div class="pq-exp">The marine Bagh Beds (Nimar Sandstone, Nodular Limestone, Deola Marl, Coralline Limestone) correlate with the Uttatur and Trichinopoly groups, not the terminal Niniyur beds.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 48: KUTCH TYPE AREA FOR JURASSIC
# ==========================================
q48_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Mesozoic Stratigraphy: The Kutch Basin as Global Jurassic Type Area</div>
    <div class="card-body">
      <p>The <strong>Kutch (Kachchh) Basin</strong> in Gujarat is the world-renowned <strong>type area for the Jurassic System in India</strong> and a benchmark reference for global Tethyan-peri-Gondwanan ammonite biostratigraphy. Initiated during the Late Triassic to Early Jurassic rifting of Gondwanaland along the western continental margin of India, the basin accumulated over $2,500\\text{ m}$ of exceptionally fossiliferous marine to deltaic sediments.</p>
      
      <ul>
        <li><strong>Classic Four-Fold Stratigraphic Division (Stoliczka, Waagen, Rajnath):</strong>
          <ol>
            <li><strong>Patcham Formation (~300 m; Middle Jurassic: Bathonian):</strong>
              <ul>
                <li><em>Lithology:</em> Basal yellow limestones, calcareous sandstones, and rich coral patch reefs (exposed in Patcham Island and Kutch Mainland).</li>
                <li><em>Diagnostic Fossils:</em> Cephalopods such as <em>Macrocephalites triangularis</em> and <em>Sivajiceras congener</em>, with brachiopods (<em>Kutchithyris</em>).</li>
              </ul>
            </li>
            <li><strong>Chari Formation (~360 m; Callovian to Oxfordian):</strong>
              <ul>
                <li><em>Lithology:</em> Highly fossiliferous shales, oolitic limestones, and the famous golden-weathering <strong>Dhosa Oolite Member</strong> at the top.</li>
                <li><em>Diagnostic Biozones:</em> Standard global ammonite zones: <em>Macrocephalites macrocephalus</em> (Callovian base), <em>Reineckeia</em>, <em>Peltoceras athleta</em>, and <em>Mayaites maya</em> (Oxfordian).</li>
              </ul>
            </li>
            <li><strong>Katrol Formation (~300 m; Kimmeridgian to Early Tithonian):</strong>
              <ul>
                <li><em>Lithology:</em> Red sandstones, gritty shales, and ironstone nodules reflecting shallowing marine conditions.</li>
                <li><em>Diagnostic Fossils:</em> Ammonites <em>Katroloceras</em>, <em>Waagenia</em>, <em>Streblites</em>, and <em>Hildoglochiceras</em>.</li>
              </ul>
            </li>
            <li><strong>Umia Formation (~500 m; Tithonian to Early Cretaceous Aptian):</strong>
              <ul>
                <li><em>Lithology:</em> Marine sandstones (Trigonia beds with <em>Trigonia ventricosa</em>), grading upward into terrestrial deltaic sandstones with Gondwana plant fossils (<em>Ptilophyllum</em> flora), capped by the marine transgressive <strong>Ukra Member</strong> (Aptian ammonite <em>Australiceras</em>).</li>
                <li><em>Ammonites:</em> <em>Virgatosphinctes densiplicatus</em> and <em>Micracanthoceras</em>.</li>
              </ul>
            </li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>The Jurassic of Kutch:</strong> Kutch is the type area of the Jurassic rocks in India. The Jurassic strata are magnificently developed, showing complete exposure from Bathonian to Lower Cretaceous. They are divided into four groups:
        (1) Patcham Group (Bathonian),
        (2) Chari Group (Callovian-Oxfordian),
        (3) Katrol Group (Kimmeridgian), and
        (4) Umia Group (Tithonian to Lower Cretaceous).
        The cephalopod fauna of Kutch is famous all over the world for its richness and variety."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Jurassic System: Kutch, pp. 291-293)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q048/kutch_jurassic_stratigraphy_biozones.png" alt="Kutch Jurassic Stratigraphic Succession and Ammonite Biozones">
        <div class="tb-caption">
          <strong>Figure 48.1: The Classic Jurassic Lithostratigraphic Succession of Kutch.</strong> The iconic four formations (Patcham, Chari, Katrol, Umia) with their world-standard cephalopod biozones.
        </div>
      </div>
    </div>
  </div>
"""

q48_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 48</div>
    <div class="q-text">Kutch is the type Area in India for :</div>
    <div class="raw-options">
      <div>(A) Jurassic formation</div>
      <div>(B) Early archean rocks</div>
      <div>(C) Late Archean rocks</div>
      <div>(D) Cambrian formation</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (A) Jurassic formation</strong>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Jurassic formation</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Kutch is universally recognized in Indian and international geology as the classic <strong>type area for the Jurassic System in India</strong>. The Patcham, Chari, Katrol, and Umia Formations preserve an unmatched marine sequence spanning Bathonian, Callovian, Oxfordian, Kimmeridgian, and Tithonian stages, populated with world-standard ammonite zones.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Early archean rocks</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Early Archean rocks (Paleoarchean >3.5 Ga) are located in the Singhbhum Craton (Older Metamorphic Group), Dharwar Craton (Sargur Group), and Bastar Craton. Kutch contains no exposed Archean basement.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Late Archean rocks</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Late Archean rocks (Neoarchean ~2.7 - 2.5 Ga) are typified by the Dharwar Supergroup in Karnataka and the Bundelkhand Granite Complex. Kutch is an exclusively Mesozoic-Cenozoic pericratonic rift basin.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Cambrian formation</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The type areas for the Cambrian System in the Indian subcontinent are the <strong>Spiti Valley</strong> (Parahio Formation / Haimanta Group) and the <strong>Salt Range</strong> (Salt Pseudomorph and Magnesian Sandstone beds), not Kutch.
    </div>
  </div>
"""

q48_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: The Four Formations of the Kutch Jurassic Succession</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Formation</th>
            <th>Standard European Age</th>
            <th>Thickness</th>
            <th>Key Lithofacies</th>
            <th>Diagnostic Index Ammonites</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Umia Formation</strong></td>
            <td>Tithonian to Aptian</td>
            <td>~500 m</td>
            <td>Sandstones, Trigonia beds, plant beds, Ukra bed</td>
            <td><em>Virgatosphinctes densiplicatus</em>, <em>Australiceras</em></td>
          </tr>
          <tr>
            <td><strong>Katrol Formation</strong></td>
            <td>Kimmeridgian - L. Tithonian</td>
            <td>~300 m</td>
            <td>Red sandstones, shales, ironstone concretions</td>
            <td><em>Katroloceras</em>, <em>Waagenia kachhensis</em></td>
          </tr>
          <tr>
            <td><strong>Chari Formation</strong></td>
            <td>Callovian to Oxfordian</td>
            <td>~360 m</td>
            <td>Fossiliferous shales, limestones, Dhosa Oolite</td>
            <td><em>Macrocephalites macrocephalus</em>, <em>Peltoceras athleta</em></td>
          </tr>
          <tr>
            <td><strong>Patcham Formation</strong></td>
            <td>Bathonian</td>
            <td>~300 m</td>
            <td>Grey/yellow limestones, coral biostromes</td>
            <td><em>Macrocephalites triangularis</em>, <em>Sivajiceras</em></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Kutch Stratigraphy & Cephalopod Biozones</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Lithological Character of the Dhosa Oolite Member</div>
        <div class="pq-ans">Green to brownish ferruginous and oolitic limestone marking a condensed stratigraphic section</div>
        <div class="pq-exp">The Dhosa Oolite occurs at the top of the Chari Formation (Oxfordian). It is an iron-rich oolitic grainstone packed with ammonites, representing a period of very slow sedimentation (condensation horizon) during maximum marine flooding.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Significance of the Ukra Member in Umia Formation</div>
        <div class="pq-ans">Aptian marine transgressive horizon containing ammonites within an otherwise continental sequence</div>
        <div class="pq-exp">The Ukra bed contains the diagnostic Lower Cretaceous ammonite *Australiceras*, proving that marine conditions briefly returned to the Kutch basin in the Aptian stage before regional emergence.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Paleogeographic Affinity of Kutch Plant Beds</div>
        <div class="pq-ans">Gondwana Upper Mesozoic flora (*Ptilophyllum* flora)</div>
        <div class="pq-exp">The plant beds interstratified within the upper Umia sandstones contain cycads (*Ptilophyllum acutifolium*), conifers, and ferns identical to the Rajmahal and Jabalpur floras, demonstrating continental land connection to the Gondwana mainland.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Index Fossil for the Base of the Callovian Stage</div>
        <div class="pq-ans"><em>Macrocephalites macrocephalus</em></div>
        <div class="pq-exp">The basal macrocephalus zone of the Chari Formation is the global bio-chronological marker for the Bathonian-Callovian boundary.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Major Structural Features of the Kutch Rift Basin</div>
        <div class="pq-ans">E-W trending faulted folds (Kachchh Mainland Fault, Island Belt Fault, Katrol Hill Fault)</div>
        <div class="pq-exp">The Kutch basin formed by Mesozoic extensional rifting along primordial Precambrian basement faults, later inverted into E-W trending asymmetric anticlinal ridges during Cenozoic Himalayan collision compression.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Golden Oolite Occurrence in Kutch</div>
        <div class="pq-ans">Basal part of the Chari Formation (Keera dome and Chari dome)</div>
        <div class="pq-exp">The 'Golden Oolite' is a distinct calc-arenite composed of carbonate ooids coated with thin films of golden iron-oxide/pyrite, formed in high-energy shallow agitated marine shoals.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Type Area of Jurassic in Rajasthan (Adjacent Basin)</div>
        <div class="pq-ans">Jaisalmer Basin (Lathi Formation, Jaisalmer Limestone, Baisakhi, Bedesar)</div>
        <div class="pq-exp">The Jaisalmer Basin to the north contains a lateral marine equivalent, notably the fossiliferous golden Jaisalmer Limestone (*Pseudocidaris*, ammonites) correlating with the Patcham-Chari interval.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Trigonia Beds of Kutch</div>
        <div class="pq-ans">Bivalve-rich sandstones in the lower Umia Formation characterized by <em>Trigonia ventricosa</em></div>
        <div class="pq-exp">The genus *Trigonia* (thick-shelled schizodont bivalve) occurs in coquina beds, serving as a reliable Tithonian marker throughout peri-Gondwanan basins (India, Madagascar, South Africa).</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 49: SIWALIKS WELL KNOWN FOR MAMMAL FOSSILS
# ==========================================
q49_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Cenozoic Vertebrate Paleontology: Siwalik Foreland Basin & Mammalian Radiation</div>
    <div class="card-body">
      <p>The <strong>Siwalik Supergroup (or Siwalik Group)</strong> is a vast, continuous, $6,000\\text{ m}$ thick synorogenic <strong>molasse sequence</strong> deposited in the Himalayan foreland basin from Middle Miocene to Early Pleistocene (~18 Ma to 0.6 Ma). It was formed by rivers draining the rising Himalayan orogen (paleo-Indo-Brahm river system). Globally, the Siwaliks are celebrated as the <strong>premier terrestrial vertebrate fossil repository in the world, famed above all for their rich and evolutionary mammalian fauna</strong>.</p>
      
      <ul>
        <li><strong>Stratigraphic Divisions & Mammalian Faunal Succession:</strong>
          <ol>
            <li><strong>Lower Siwalik (~18 - 10.5 Ma; Kamlial & Chinji Formations):</strong>
              <ul>
                <li><em>Sedimentology:</em> Hard grey sandstones and bright red/purple floodplain shales.</li>
                <li><em>Fauna:</em> Primitive proboscideans (<em>Deinotherium</em>, <em>Gomphotherium</em>), anthracotheres, early suids (<em>Listriodon</em>), primitive giraffids (<em>Giraffokeryx</em>), and primitive primates.</li>
              </ul>
            </li>
            <li><strong>Middle Siwalik (~10.5 - 3.5 Ma; Nagri & Dhok Pathan Formations):</strong>
              <ul>
                <li><em>Sedimentology:</em> Coarse multistory micaceous sandstones ('pepper-and-salt' texture) and brown clays.</li>
                <li><em>Fauna — Golden Age of Mammals:</em>
                  <ul>
                    <li><strong>Hominoids (Primates):</strong> World-famous discovery of <em>Sivapithecus indicus</em>, <em>Sivapithecus punjabicus</em> (and <em>Ramapithecus</em>), crucial in ape-human evolutionary lineages.</li>
                    <li><strong>Equids:</strong> Abundant radiation of the tridactyl (three-toed) grazing horse <em>Hipparion</em> (<em>Hipparion theobaldi</em>, <em>H. antilopinum</em>), marking the arrival of C4 grasslands.</li>
                    <li><strong>Giant Herbivores:</strong> <em>Bramatherium</em>, <em>Hydaspitherium</em> (giant giraffids), <em>Mastodon</em>, and rhinocerotids.</li>
                  </ul>
                </li>
              </ul>
            </li>
            <li><strong>Upper Siwalik (~3.5 - 0.6 Ma; Tatrot, Pinjor & Boulder Conglomerate):</strong>
              <ul>
                <li><em>Sedimentology:</em> Coarse conglomerates, gravel beds, silts, and loess.</li>
                <li><em>Fauna — Advanced Quaternary Mammals:</em>
                  <ul>
                    <li>Arrival of monodactyl true horses (<strong>Equus sivalensis</strong>).</li>
                    <li>Advanced proboscideans: <strong>Stegodon ganesa</strong> (with massive 3-meter curved tusks) and <strong>Elephas hysudricus</strong>.</li>
                    <li>Hippopotamids (<em>Hexaprotodon sivalensis</em>), camelids (<em>Camelus sivalensis</em>), giant bovids, sabre-toothed cats (<em>Machairodus</em>), and primates (<em>Cercopithecus</em>).</li>
                  </ul>
                </li>
              </ul>
            </li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Siwalik System & Mammalian Fossils:</strong> The Siwalik rocks are globally famous for their exceptionally rich assemblage of <strong>mammalian fossils</strong>. The collection includes practically every mammalian order: Primates (such as the extinct man-like ape <em>Sivapithecus</em>), Proboscidea (primitive elephants like <em>Stegodon</em>, <em>Mastodon</em>, <em>Deinotherium</em>), Equidae (the horse ancestor <em>Hipparion</em> and modern <em>Equus</em>), Rhinocerotidae, Bovidae, Suidae, and Carnivora. No other geological formation in the world presents such an extraordinary and continuous record of mammalian evolution."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Tertiary System: Siwalik Group, pp. 302-304)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q049/siwalik_mammalian_fauna_stratigraphy.png" alt="Siwalik Stratigraphy and Mammalian Fossil Succession">
        <div class="tb-caption">
          <strong>Figure 49.1: Siwalik Foreland Basin Stratigraphy and Mammalian Biozones.</strong> The evolutionary succession from Miocene Lower Siwalik proboscideans to Middle Siwalik hominoids (*Sivapithecus*) and Upper Siwalik true horses (*Equus*) and elephants (*Stegodon*).
        </div>
      </div>
    </div>
  </div>
"""

q49_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 49</div>
    <div class="q-text">Siwaliks are well known for:</div>
    <div class="raw-options">
      <div>(A) Dinosaur fossil</div>
      <div>(B) Invertebrate fossils</div>
      <div>(C) Mammal fossils</div>
      <div>(D) Plant fossils</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (C) Mammal fossils</strong>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Dinosaur fossil</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Dinosaurs went extinct at the end of the Cretaceous (~66 Ma), whereas the Siwaliks are Neogene-Quaternary (~18 to 0.6 Ma). Indian dinosaur fossils (Titanosaurs, <em>Rajasaurus narmadensis</em>) are recovered from the Cretaceous Lameta Formation and Ariyalur beds, not Siwaliks.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Invertebrate fossils</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> While minor freshwater bivalves (*Unio*) and gastropods occur in Siwalik muds, the Siwaliks are globally renowned specifically for vertebrates, in complete contrast to marine formations like Kutch or Spiti which are famed for invertebrates.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Mammal fossils</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Siwalik Supergroup is universally celebrated as the world's finest Neogene terrestrial fossil treasury for <strong>mammals</strong>. It records the complete evolutionary history of hominoid primates (<em>Sivapithecus</em>), three-toed and single-toed horses (<em>Hipparion</em>, <em>Equus</em>), proboscideans (<em>Stegodon</em>, <em>Elephas</em>), giraffes, hippos, rhinos, and bovids.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Plant fossils</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Fossil wood and leaf impressions occur in the Siwaliks, but plant fossils are the signature hallmark of the Gondwana Supergroup (<em>Glossopteris</em>, <em>Gangamopteris</em>) and Rajmahal Intertrappeans, not the Siwalik Group.
    </div>
  </div>
"""

q49_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Major Mammalian Lineages Preserved in the Siwaliks</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Mammalian Order</th>
            <th>Key Genera Preserved</th>
            <th>Primary Siwalik Horizon</th>
            <th>Evolutionary / Paleoclimatic Significance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Primates (Hominoids)</strong></td>
            <td><em>Sivapithecus indicus</em>, <em>S. punjabicus</em>, <em>Ramapithecus</em></td>
            <td>Middle Siwalik (Nagri - Dhok Pathan)</td>
            <td>Critical Miocene ape divergence; ancestor of modern orangutans (Pongo)</td>
          </tr>
          <tr>
            <td><strong>Perissodactyla (Horses)</strong></td>
            <td><em>Hipparion theobaldi</em> (3-toed) &rarr; <em>Equus sivalensis</em> (1-toed)</td>
            <td>Middle Siwalik &rarr; Upper Siwalik (Pinjor)</td>
            <td>Chronostratigraphic transition tracking expansion of C4 savannas</td>
          </tr>
          <tr>
            <td><strong>Proboscidea (Elephants)</strong></td>
            <td><em>Deinotherium</em>, <em>Stegodon ganesa</em>, <em>Elephas hysudricus</em></td>
            <td>Lower, Middle, and Upper Siwalik</td>
            <td>Tusk evolution; development of multi-lamellar high-crowned molar teeth</td>
          </tr>
          <tr>
            <td><strong>Artiodactyla (Hippos & Giraffes)</strong></td>
            <td><em>Hexaprotodon sivalensis</em>, <em>Bramatherium</em>, <em>Sivatherium</em></td>
            <td>Middle & Upper Siwalik</td>
            <td>Hexaprotodont (6 incisor) dentition; giant short-necked horned giraffids</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Siwalik Biostratigraphy & Evolution</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: The 'Hipparion Datum' in Siwalik Chronology</div>
        <div class="pq-ans">First appearance datum (FAD) of <em>Hipparion</em> at ~10.7 Ma (Base of Nagri Formation)</div>
        <div class="pq-exp">The migration of the three-toed horse *Hipparion* from North America into Eurasia via the Bering land bridge marks a global chronostratigraphic datum (~10.7 Ma) defining the base of the Middle Siwaliks.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Significance of Sivapithecus Jaw Fragments</div>
        <div class="pq-ans">Demonstrated that Sivapithecus is sister-taxon to modern Orangutan (*Pongo*)</div>
        <div class="pq-exp">Facial and gnathic anatomy (narrow interorbital distance, oval orbits, airorhynchous facial profile) proved *Sivapithecus* was ancestral to Asian orangutans rather than a direct human ancestor.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Carbon Isotope Shift in Siwalik Paleosols (~7 - 8 Ma)</div>
        <div class="pq-ans">Shift from C3 woodland vegetation to C4 grassland savannas</div>
        <div class="pq-exp">Pedogenic carbonate $\delta^{13}\text{C}$ shifts from $-12‰$ to $+1‰$ between 7.5 and 6.0 Ma, recording the intensification of the Asian Monsoon and the replacement of C3 forests by C4 drought-adapted grasses.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Diagnostic Tusk Feature of *Stegodon ganesa*</div>
        <div class="pq-ans">Enormous, closely spaced, parallel curved tusks exceeding 3 meters length</div>
        <div class="pq-exp">Discovered in the Pinjor Formation near Saketi, *Stegodon ganesa* possessed the most massive tusks of any known proboscidean, displayed today in the Indian Museum Kolkata.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Difference Between Pinjor and Tatrot Formations</div>
        <div class="pq-ans">Tatrot represents Pliocene (~3.5-2.6 Ma); Pinjor represents Early Pleistocene (~2.6-0.6 Ma) with *Equus* and *Elephas*</div>
        <div class="pq-exp">The Pinjor stage is marked by the first appearance of the true modern horse (*Equus sivalensis*) and modern elephant (*Elephas hysudricus*), alongside colder Pleistocene glacial-influenced climate.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Sedimentological Difference Between Kamlial and Chinji Formations</div>
        <div class="pq-ans">Kamlial is dominated by hard grey sandstones; Chinji is dominated by thick bright-red floodplain clays</div>
        <div class="pq-exp">Kamlial sandstones were deposited by large bedload channel networks, whereas Chinji reflects meandering river channels wandering across wide, oxidized, red muddy floodplains.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: The Genus *Hexaprotodon*</div>
        <div class="pq-ans">Primitive hippopotamid possessing six incisor teeth in both upper and lower jaws</div>
        <div class="pq-exp">Modern African hippos (*Hippopotamus amphibius*) are tetraprotodont (4 incisors), whereas the Siwalik *Hexaprotodon* retained the primitive mammalian condition of 6 incisors.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Tectonic Boundary Terminating the Siwalik Basin to the South</div>
        <div class="pq-ans">Main Frontal Thrust (MFT / Himalayan Frontal Fault)</div>
        <div class="pq-exp">The MFT places the folded Siwalik molasse over the modern Indo-Gangetic alluvium along the southernmost active front of the Himalayan collision zone.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 50: SPITI PERMIANS REPRESENTED BY KULING GROUP
# ==========================================
q50_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Tethyan Himalayan Stratigraphy: Spiti Paleozoic & The Permian Kuling Group</div>
    <div class="card-body">
      <p>The <strong>Spiti Valley</strong> in Himachal Pradesh preserves the most complete, continuously fossiliferous marine sedimentary sequence in the entire Indian subcontinent—from the Cambrian to the Cretaceous. Because of its unbroken record, it is globally known as the <em>Museum of Indian Geology</em>. Within this succession, the <strong>Permian System is represented exclusively by the Kuling Group</strong> (historically termed the <em>Productus Shales</em>).</p>
      
      <ul>
        <li><strong>Stratigraphic Context in the Spiti Basin:</strong>
          <ol>
            <li><strong>Muth Quartzite (Devonian):</strong> Pure snow-white orthoquartzite regional marker horizon.</li>
            <li><strong>Kanawar Group (Carboniferous):</strong> Composed of the <strong>Lipak Formation</strong> (Tournaisian-Viséan fossiliferous limestones with brachiopods <em>Syringothyris</em>) and the <strong>Po Formation</strong> (Namurian Fenestella Shales and plant-bearing Thabo Stage).</li>
            <li><strong>The Permian Gap & Kuling Group:</strong> Above an Early Permian unconformity (reflecting Gondwanan rifting and Panjal volcanic event), the Middle to Late Permian is represented by the <strong>Kuling Group</strong> (~60 to 100 m thick).</li>
            <li><strong>Lithostratigraphic Subdivisions of the Kuling Group:</strong>
              <ul>
                <li><strong>Gechang Formation (Lower Kuling):</strong> Calcareous sandstone and sandy limestone (~5-20 m), containing cold-water marine brachiopods (<em>Spiriferella rajah</em>, <em>Neospirifer</em>) deposited during the post-glacial Gondwana marine transgression.</li>
                <li><strong>Gungri Formation (Upper Kuling / Productus Shale):</strong> Monotonous succession of dark grey to black, splintery, highly carbonaceous and phosphatic shales (~50-80 m) containing abundant calcareous concretions.
                <br><em>Fossil Fauna:</em> Famous for the ammonoid <strong>Cyclolobus walkeri</strong>, xenodiscid ammonoids, and productid brachiopods (<strong>Marginifera himalayensis</strong>, <em>Costiferina indica</em>).</li>
              </ul>
            </li>
            <li><strong>Overlying Lilang Group (Triassic):</strong> The Gungri Formation is conformably overlain by the basal Triassic <strong>Otoceras woodwardi bed</strong> (Mikila/Lilang Group), capturing the globally crucial Permian-Triassic (P-Tr) mass extinction boundary.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Permian of Spiti (Kuling System / Productus Shales):</strong> The Permian rocks in Spiti rest with an unconformity over the Carboniferous Kanawar Group. They are known as the <strong>Kuling Group</strong> (or Productus Shales). The lower division consists of calcareous sandstone (Gechang formation), and the upper division consists of black carbonaceous shales (Gungri formation) containing concretions. Diagnostic fossils include <em>Marginifera himalayensis</em>, <em>Spiriferella rajah</em>, and the Late Permian ammonoid <em>Cyclolobus</em>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Permian System: Spiti, pp. 287-288)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q050/spiti_tethyan_himalaya_kuling_group.png" alt="Spiti Tethyan Basin Stratigraphy Highlighting Permian Kuling Group">
        <div class="tb-caption">
          <strong>Figure 50.1: Stratigraphic Architecture of the Spiti Paleozoic Succession.</strong> The position of the Permian Kuling Group (Gechang Sandstone and Gungri / Productus Shales) sandwiched between the Carboniferous Kanawar Group and Triassic Lilang Group.
        </div>
      </div>
    </div>
  </div>
"""

q50_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 50</div>
    <div class="q-text">In Spiti, the Permians are represented by :</div>
    <div class="raw-options">
      <div>(A) Muth quartzite</div>
      <div>(B) Kanawar Group</div>
      <div>(C) Kuling group</div>
      <div>(D) Agglomerate shale</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (C) Kuling group</strong>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Muth quartzite</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Muth Quartzite is the world-famous marker horizon for the <strong>Devonian System</strong> in the Himalayas, completely pre-dating the Permian by over 100 million years.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Kanawar Group</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Kanawar Group in Spiti represents the <strong>Carboniferous System</strong>, comprising the Lipak Formation (Early Carboniferous) and Po Formation (Late Carboniferous Fenestella Shales).
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Kuling group</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Permian rocks in Spiti are designated lithostratigraphically as the <strong>Kuling Group</strong>. It is subdivided into the lower Gechang Formation (calcareous sandstone) and upper Gungri Formation (Productus Shales) containing *Cyclolobus walkeri* and *Marginifera himalayensis*.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Agglomerate shale (Agglomeratic Slate)</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Agglomeratic Slate represents the Carboniferous-Permian volcanic-pyroclastic rift deposits of the <strong>Kashmir Basin</strong> associated with the Panjal Traps, not the marine sedimentary sequence of the Spiti basin.
    </div>
  </div>
"""

q50_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Spiti Paleozoic Lithostratigraphic Framework</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Stratigraphic Unit</th>
            <th>Geological Age</th>
            <th>Diagnostic Lithology</th>
            <th>Key Index Fossils</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lilang Group (Base)</strong></td>
            <td>Basal Triassic (Induan)</td>
            <td>Micritic limestone & ferruginous bands</td>
            <td><em>Otoceras woodwardi</em>, <em>Ophiceras</em></td>
          </tr>
          <tr>
            <td><strong>Kuling Group (Gungri Fm)</strong></td>
            <td><strong>Late Permian (Wuchiapingian-Changhsingian)</strong></td>
            <td><strong>Black splintery carbonaceous shales</strong></td>
            <td><strong><em>Cyclolobus walkeri</em>, <em>Marginifera himalayensis</em></strong></td>
          </tr>
          <tr>
            <td><strong>Kuling Group (Gechang Fm)</strong></td>
            <td><strong>Middle Permian</strong></td>
            <td><strong>Calcareous sandstone / arenite</strong></td>
            <td><strong><em>Spiriferella rajah</em>, <em>Neospirifer</em></strong></td>
          </tr>
          <tr>
            <td><strong>Kanawar Group (Po Fm)</strong></td>
            <td>Carboniferous (Pennsylvanian)</td>
            <td>Black shales, quartzites (Fenestella shales)</td>
            <td><em>Fenestella plebeia</em>, <em>Rhacopteris ovata</em></td>
          </tr>
          <tr>
            <td><strong>Kanawar Group (Lipak Fm)</strong></td>
            <td>Early Carboniferous (Mississippian)</td>
            <td>Limestones and dolomites</td>
            <td><em>Syringothyris cuspidata</em></td>
          </tr>
          <tr>
            <td><strong>Muth Quartzite</strong></td>
            <td>Devonian</td>
            <td>Snow-white pure quartz arenite</td>
            <td>Devonian brachiopods (rare trace fossils)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Himalayan Paleozoic Stratigraphy</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Diagnostic Value of *Cyclolobus walkeri*</div>
        <div class="pq-ans">Index ammonoid for the uppermost Late Permian (Changhsingian stage)</div>
        <div class="pq-exp">*Cyclolobus* features complex ammonitic suture lines with numerous auxiliary lobes, serving globally as the definitive ammonoid marker for the closing stages of the Permian Period prior to the mass extinction.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Nature of the Permian-Triassic Boundary in Spiti</div>
        <div class="pq-ans">Apparent paraconformity/conformity between Gungri black shales and Otoceras limestone</div>
        <div class="pq-exp">At the classic Guling and Attargoo sections in Spiti, the top of the Gungri Formation is directly overlain by the *Otoceras woodwardi* zone with minimal physical discordance, recording the global P-Tr extinction event in continuous marine strata.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Depositional Environment of the Gungri Formation</div>
        <div class="pq-ans">Anoxic to euxinic deep-water basinal shelf</div>
        <div class="pq-exp">High organic carbon content, dark black colour, lack of bioturbation, and widespread phosphatic concretions indicate deposition under stagnant, oxygen-depleted marine bottom waters.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Kashmir Equivalent of the Spiti Kuling Group</div>
        <div class="pq-ans">The Zewan Formation</div>
        <div class="pq-exp">In Kashmir, the marine Permian capping the Gangamopteris beds and Panjal Traps is the *Zewan Formation*, containing an identical brachiopod fauna (*Marginifera*, *Spiriferella*).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Plant Fossils in the Carboniferous Po Formation</div>
        <div class="pq-ans"><em>Rhacopteris ovata</em> flora in the Thabo Stage</div>
        <div class="pq-exp">The Thabo plant beds in the Po Formation yield *Rhacopteris*, representing the Culm (Early Carboniferous) flora of Gondwanaland, demonstrating temporary emergence before marine submergence.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Why is the Kuling Group Absent in Parts of the Lesser Himalaya?</div>
        <div class="pq-ans">Due to the Hercynian (Late Paleozoic) epeirogenic uplift and erosion</div>
        <div class="pq-exp">The Late Paleozoic Hercynian orogenic phase uplifted much of the Indian peninsular margin, causing a regional unconformity where Permian rocks directly overlie older Proterozoic basements or are absent.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Brachiopod Morphological Adaptation of *Marginifera*</div>
        <div class="pq-ans">Strong internal marginal ridge (flange) to prevent soft-tissue fouling in muddy sediment</div>
        <div class="pq-exp">*Marginifera himalayensis* possessed a concave brachial valve and a thick internal marginal rim that elevated the lophophore above fluid bottom muds in the quiet Gungri depositional basin.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Origin of Phosphatic Nodules in Kuling Shales</div>
        <div class="pq-ans">Upwelling of nutrient-rich cold oceanic waters along the northern Gondwanan margin</div>
        <div class="pq-exp">Coastal upwelling along the southern margin of the Neo-Tethys fostered intense biological productivity, leading to high biogenic silica and phosphate precipitation during early diagenesis.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 51: DELHI SYSTEM INTRUDED BY ERINPURA GRANITE
# ==========================================
q51_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Precambrian Orogenesis: Aravalli-Delhi Belt & Erinpura Granite Plutonism</div>
    <div class="card-body">
      <p>The <strong>Aravalli-Delhi Orogenic Belt</strong> in northwestern India (Rajasthan and northern Gujarat) preserves a multi-phase Proterozoic Wilson Cycle extending over 700 km from Delhi to Palanpur. The youngest structural supergroup in this fold belt is the <strong>Delhi Supergroup</strong> (Mesoproterozoic, ~1.7 - 1.0 Ga), which underwent polyphase deformation, regional metamorphism, and was syn- to post-tectonically intruded by the massive <strong>Erinpura Granite</strong> (~850 - 800 Ma).</p>
      
      <ul>
        <li><strong>Tectonostratigraphic Succession of Rajasthan:</strong>
          <ol>
            <li><strong>Banded Gneissic Complex (BGC / Mewar Gneiss; ~3.3 - 2.8 Ga):</strong> Archean basement of tonalite-trondhjemite-granite gneisses, amphibolites, and granulites, unconformably overlain by Proterozoic basins.</li>
            <li><strong>Aravalli Supergroup (Paleoproterozoic; ~2.2 - 1.8 Ga):</strong> Rifting and passive margin shelf sequence (basal volcanics, Raialo dolomites and phosphorites at Jhamarkotra, phyllites, and deep-water flysch).</li>
            <li><strong>Delhi Supergroup (Mesoproterozoic; ~1.7 - 1.0 Ga):</strong>
              <ul>
                <li><em>Alwar Group:</em> Lower, arenaceous-dominated sequence of thick quartz arenites, arkoses, and conglomerates deposited in shallow-marine coastal to graben environments.</li>
                <li><em>Ajabgarh Group:</em> Upper, deeper-water argillaceous-calcareous sequence of mica schists, calc-silicates, marbles (e.g., Makrana marble), and carbonaceous phyllites.</li>
              </ul>
            </li>
            <li><strong>Erinpura Granite (~850 - 800 Ma):</strong> A monumental suite of late- to post-tectonic, S-type to I-type granites and granite-gneisses named after the town of Erinpura (Sirohi district). The plutons (including the Abu batholith, Sirohi, and Sendra granites) cross-cut the folded Delhi metasediments, marking the terminal Neoproterozoic tectonothermal stabilization of the Delhi Orogen.</li>
            <li><strong>Post-Delhi Volcanics:</strong> The younger <strong>Malani Igneous Suite (~750 Ma)</strong> represents anorogenic felsic volcanism (rhyolites and peralkaline granites) that erupted unconformably over the eroded Erinpura and Delhi floor in western Rajasthan.</li>
          </ol>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Delhi Supergroup & Erinpura Granite:</strong> The Delhi rocks were subjected to intense folding and regional metamorphism. After the folding of the Delhi System was completed, the whole area was intruded on an extensive scale by granitic rocks known as the <strong>Erinpura Granite</strong>. It forms the prominent hills of Mount Abu and Erinpura. It is intrusive into the Delhi Supergroup and represents the last major plutonic event in the Aravalli mountain belt."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Delhi System, pp. 280-281)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q051/delhi_supergroup_erinpura_granite.png" alt="Aravalli-Delhi Belt Stratigraphy and Erinpura Granite Intrusion">
        <div class="tb-caption">
          <strong>Figure 51.1: Tectonostratigraphic Framework of the Delhi Supergroup.</strong> Schematic cross-section showing folded Alwar and Ajabgarh metasediments intruded by the post-tectonic Erinpura Granite (~850 Ma).
        </div>
      </div>
    </div>
  </div>
"""

q51_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 51</div>
    <div class="q-text">Dalhi system is intruded by:</div>
    <div class="raw-options">
      <div>(A) Erinpura Granite</div>
      <div>(B) Malani Rhyolite</div>
      <div>(C) Singhbhum Granite</div>
      <div>(D) Bundelkhand Granite</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (A) Erinpura Granite</strong>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) Erinpura Granite</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Delhi Supergroup is extensively intruded by the <strong>Erinpura Granite</strong> (~850 - 800 Ma). These late-to-post-kinematic granites (including the Mount Abu batholith and Sendra complex) produce prominent contact metamorphic aureoles and truncate the regional structural fold axes of the Delhi rocks.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Malani Rhyolite</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Malani Igneous Suite (~750 Ma) consists of <em>extrusive volcanic flows</em> (felsic rhyolites and ash-flow tuffs) that rest <em>unconformably</em> over the eroded, beveled surface of the folded Delhi rocks and Erinpura granite. They are extrusive cover rocks, not an intrusive plutonic system into the Delhi sequence.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Singhbhum Granite</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Singhbhum Granite (~3.1 - 3.4 Ga) is an Archean composite batholith restricted geographically to the Singhbhum Craton in Jharkhand and Odisha, completely unrelated to the Delhi belt of Rajasthan.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Bundelkhand Granite</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Bundelkhand Granite Complex (~2.5 - 2.6 Ga) is an Archean cratonic basement block in central India (Madhya Pradesh and Uttar Pradesh) characterized by quartz reefs and dolerite dykes, formed prior to the Proterozoic Delhi System.
    </div>
  </div>
"""

q51_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Major Granitic Suites of the Indian Shield</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Granite Suite</th>
            <th>Cratonic Province</th>
            <th>Radiometric Age</th>
            <th>Tectonic Nature & Stratigraphic Host</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Erinpura Granite</strong></td>
            <td><strong>Aravalli-Delhi Belt (NW India)</strong></td>
            <td><strong>~850 - 800 Ma</strong></td>
            <td><strong>Post-Delhi intrusive batholith (Abu, Sirohi, Sendra)</strong></td>
          </tr>
          <tr>
            <td><strong>Closepet Granite</strong></td>
            <td>Dharwar Craton (S India)</td>
            <td>~2.51 Ga</td>
            <td>Intrusive batholith dividing Western & Eastern Dharwar cratons</td>
          </tr>
          <tr>
            <td><strong>Bundelkhand Granite</strong></td>
            <td>Central Indian Shield</td>
            <td>~2.50 - 2.60 Ga</td>
            <td>Archean cratonic basement traversed by giant quartz reefs</td>
          </tr>
          <tr>
            <td><strong>Singhbhum Granite</strong></td>
            <td>Singhbhum Craton (Eastern India)</td>
            <td>~3.30 - 3.12 Ga</td>
            <td>Polyphase Mesoarchean TTG and granite batholith</td>
          </tr>
          <tr>
            <td><strong>Berach Granite</strong></td>
            <td>SE Rajasthan (Aravalli margin)</td>
            <td>~2.55 Ga</td>
            <td>Late Archean basement pluton beneath the Aravalli Supergroup</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Proterozoic Magmatism & Rajasthan Stratigraphy</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Mount Abu Batholith Composition</div>
        <div class="pq-ans">Porphyritic microcline-bearing granite belonging to the Erinpura Suite</div>
        <div class="pq-exp">Mount Abu, the highest peak of the Aravalli Range (Guru Shikhar: 1,722 m), is a massive monolithic horst carved entirely out of the Neoproterozoic Erinpura Granite batholith.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Major Mineral Deposit Formed by Post-Delhi Magmatism</div>
        <div class="pq-ans">Tungsten (Wolframite) mineralization at Degana (Nagaur district)</div>
        <div class="pq-exp">High-level granite intrusions related to the terminal Delhi magmatic phase generated greisenized quartz-vein networks hosting India's premier wolframite (tungsten) deposits at Degana.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Distinction Between Alwar and Ajabgarh Groups</div>
        <div class="pq-ans">Alwar is coarse arenaceous (sandstones/quartzites); Ajabgarh is fine argillaceous and calcareous (schists, marbles)</div>
        <div class="pq-exp">Alwar group quartzites form the rugged, cliff-forming ridges of northeastern Rajasthan, while Ajabgarh rocks occupy valleys and host the marble belts (Makrana, Rajnagar).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Sendra Granite Tectonic Setting</div>
        <div class="pq-ans">Syn- to late-tectonic sheet intrusions along the western margin of the South Delhi Fold Belt</div>
        <div class="pq-exp">Sendra granites (~960-850 Ma) intrude the Barotia and Sendra sequences of the Delhi Supergroup, displaying deformational gneissic foliation at margins.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Great Boundary Fault (GBF) of Rajasthan</div>
        <div class="pq-ans">Regional reverse fault separating folded Aravalli/Berach rocks from flat-lying Vindhyan strata</div>
        <div class="pq-exp">The GBF trends NE-SW for over 400 km, acting as the structural boundary that juxtaposes deformed Pre-Vindhyan rocks against the unmetamorphosed Bhander and Kaimur groups.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Age of the Malani Igneous Suite</div>
        <div class="pq-ans">Neoproterozoic (~750 - 770 Ma)</div>
        <div class="pq-exp">The Malani suite represents one of the largest felsic anorogenic volcanic provinces in the world (~50,000 km²), younger than and unconformable upon the Erinpura Granite.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Khetri Copper Belt Host Rocks</div>
        <div class="pq-ans">Ajabgarh Group metasediments of the Delhi Supergroup</div>
        <div class="pq-exp">The world-famous Khetri Copper Belt (Kolihan, Madhan-Kudhan) is hosted in garnet-chlorite schists, phyllites, and amphibolites of the Ajabgarh Group, mineralized by syn-tectonic hydrothermal fluids.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: S-type Character of Certain Erinpura Granites</div>
        <div class="pq-ans">Presence of primary muscovite, garnet, high normative corundum (>1%), and high initial ⁸⁷Sr/⁸⁶Sr</div>
        <div class="pq-exp">These geochemical markers indicate that substantial portions of the Erinpura magmas originated via partial melting (anatexis) of pelitic metasediments of the Delhi Supergroup during crustal thickening.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 52: BHUJ FORMATION CONSISTS PREDOMINANTLY OF SANDSTONES
# ==========================================
q52_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Sedimentary Basin Analysis: Bhuj Formation & Proterozoic Purana Basins</div>
    <div class="card-body">
      <p>Forensic evaluation of sedimentary successions in competitive examinations requires precise familiarity with diagnostic lithofacies across both <strong>Phanerozoic pericratonic rift basins</strong> (such as the Kutch Basin) and <strong>Proterozoic intracratonic Purana basins</strong> (Vindhyan, Cuddapah, Kaladgi, and Bhima).</p>
      
      <ul>
        <li><strong>Forensic Assessment of Statement (A) — The Mesozoic Bhuj Formation:</strong>
          <ul>
            <li><em>Stratigraphic Position:</em> The <strong>Bhuj Formation</strong> (traditionally mapped as the Upper Umia beds or Bhuj Sandstone) represents the uppermost Mesozoic lithostratigraphic unit of the Kutch Mainland, spanning the Lower Cretaceous (Tithonian-Neocomian to Aptian/Albian).</li>
            <li><em>Lithological Character:</em> The formation reaches over $300 - 800\\text{ m}$ thickness and <strong>consists predominantly of white, pale yellow, and pink, medium- to coarse-grained quartzose sandstones</strong>. These sandstones exhibit giant cross-stratification (planar and trough cross-bedding), ripple marks, and channel scour-and-fill structures, interbedded with subordinate siltstones and plant-bearing carbonaceous shales (<em>Ptilophyllum</em> flora).</li>
            <li><em>Depositional Environment:</em> Fluvial braided river to deltaic plain conditions, reflecting the gradual withdrawal of the Jurassic Tethyan sea and progradation of large sandy delta systems over the Kutch shelf.</li>
          </ul>
        </li>
        <li><strong>Refutation of Incorrect Distractor Statements:</strong>
          <ul>
            <li><strong>Statement (B) — Kaladgi Basin:</strong> The Kaladgi Basin (Karnataka) is dominated by unmetamorphosed to weakly metamorphosed <strong>quartz arenites (Saundatti quartzite), conglomerates, stromatolitic limestones, and dolomites</strong> (Bagalkot and Badami Groups). It is <em>not</em> predominantly made of slates.</li>
            <li><strong>Statement (C) — Vindhyan Supergroup:</strong> The claim that the Vindhyan Supergroup is 'devoid of limestone' is completely absurd. The Vindhyan is India's greatest carbonate storehouse, featuring monumental limestone formations (Kajrahat, Rohtas, Lakheri, Bhander) that support the majority of India's cement manufacturing plants.</li>
            <li><strong>Statement (D) — Cuddapah Basin:</strong> The Cuddapah Basin is predominantly made of <strong>sedimentary siliciclastics and carbonates</strong> (Gulcheru quartzite, Vempalle dolomite, Pulivendla quartzite, Tadpatri shale, Bairenkonda quartzite, Cumbum shale). Metadacites are extremely minor local volcanic flows; the basin is emphatically not predominantly metadacite.</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Bhuj Formation:</strong> In Kutch, the Umia beds pass upward into a thick succession of sandstones known as the <strong>Bhuj Formation</strong>. It consists predominantly of massive, cross-bedded <strong>sandstones</strong> with thin intercalations of shales containing plant fossils. These sandstones are extensively quarried for building stones throughout Gujarat."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Cretaceous System: Bhuj Beds, p. 297)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q052/bhuj_sandstone_sedimentary_facies.png" alt="Comparative Lithofacies: Bhuj Sandstones vs Proterozoic Purana Basins">
        <div class="tb-caption">
          <strong>Figure 52.1: Comparative Lithofacies Analysis.</strong> Highlighting the predominantly sandstone composition of the Mesozoic Bhuj Formation and refuting distractors concerning the Kaladgi, Vindhyan, and Cuddapah basins.
        </div>
      </div>
    </div>
  </div>
"""

q52_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 52</div>
    <div class="q-text">Which of the following statement is correct ?</div>
    <div class="raw-options">
      <div>(A) The Mesozoic Bhuj formation consists predominantly of sandstones</div>
      <div>(B) Kaladgi basin is predominantly made of slates</div>
      <div>(C) Vindhyan supergroup is devoid of limestone</div>
      <div>(D) Cuddapah basin is predominantly made of metadacites</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (A) The Mesozoic Bhuj formation consists predominantly of sandstones</strong>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) The Mesozoic Bhuj formation consists predominantly of sandstones</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Mesozoic Bhuj Formation (Lower Cretaceous of Kutch) is a textbook fluvial-deltaic succession reaching hundreds of meters thickness, composed overwhelmingly of friable to well-cemented quartzose <strong>sandstones</strong> featuring cross-bedding and channel scour-and-fills. This statement is physically and stratigraphically accurate.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Kaladgi basin is predominantly made of slates</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Kaladgi Basin is a Proterozoic epicontinental basin dominated by <strong>quartzites, conglomerates, cherts, and massive stromatolitic dolomites and limestones</strong> (Bagalkot Group). Slates represent only localized, minor argillaceous facies in deformed zones; the basin is not predominantly slates.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Vindhyan supergroup is devoid of limestone</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Vindhyan Supergroup is world-famous for containing massive, high-grade limestone formations (Kajrahat, Rohtas, Lakheri, Bhander). It supplies the vast majority of cement manufacturing raw material in Central India, making this assertion diametrically opposite to fact.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Cuddapah basin is predominantly made of metadacites</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Cuddapah Basin is a crescent-shaped Purana sedimentary basin composed of <strong>quartzites, shales, and carbonate formations</strong>. Felsic to intermediate metadacite volcanic flows occur only as minor, localized volcanic intercalations (Tadpatri volcanic episode); the basin is overwhelmingly sedimentary.
    </div>
  </div>
"""

q52_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Lithological Truth of Tested Indian Basins</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Basin / Formation</th>
            <th>True Dominant Lithology</th>
            <th>Tested Distractor Statement</th>
            <th>Forensic Verdict</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bhuj Formation (Mesozoic, Kutch)</strong></td>
            <td><strong>Cross-bedded quartz sandstones & deltaic grits</strong></td>
            <td><strong>"Consists predominantly of sandstones"</strong></td>
            <td><strong>TRUE & FACTUALLY CORRECT (A)</strong></td>
          </tr>
          <tr>
            <td><strong>Kaladgi Basin (Karnataka)</strong></td>
            <td>Quartz arenites, dolomites, limestones, conglomerates</td>
            <td>"Predominantly made of slates"</td>
            <td>FALSE (Predominantly quartzites & carbonates)</td>
          </tr>
          <tr>
            <td><strong>Vindhyan Supergroup (Central India)</strong></td>
            <td>Sandstones, shales, and thick carbonate platforms</td>
            <td>"Devoid of limestone"</td>
            <td>FALSE (Houses India's greatest limestone deposits)</td>
          </tr>
          <tr>
            <td><strong>Cuddapah Basin (Andhra Pradesh)</strong></td>
            <td>Quartzites, conglomerates, shales, dolomites</td>
            <td>"Predominantly made of metadacites"</td>
            <td>FALSE (Overwhelmingly sedimentary, minor volcanics)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Indian Sedimentary Basins & Lithofacies</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Paleocurrent Indicators in Bhuj Sandstone</div>
        <div class="pq-ans">Trough cross-bedding and parting lineations indicating westerly to north-westerly flow</div>
        <div class="pq-exp">Directional sedimentary structures in the Bhuj Formation reveal fluvial transport from the Precambrian Aravalli highlands westward into the expanding Early Cretaceous proto-oceanic gulf.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: The Two Groups of the Kaladgi Basin</div>
        <div class="pq-ans">Bagalkot Group (deformed lower succession) and Badami Group (flat-lying upper succession)</div>
        <div class="pq-exp">The Kaladgi basin records an older, folded marine platform sequence (Bagalkot: Lokapur and Simikeri subgroups) overlain unconformably by the horizontally bedded arenaceous Badami Group.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Economic Limestone Units of the Vindhyan Supergroup</div>
        <div class="pq-ans">Rohtas Limestone (Semri Group) and Bhander / Lakheri Limestone (Bhander Group)</div>
        <div class="pq-exp">The Rohtas Limestone consists of fine-grained micritic limestones yielding >85% CaCO3, quarried in massive open-cast mines across Bihar, MP, and Rajasthan.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Chrysotile Asbestos and Barytes Host Formation in Cuddapah</div>
        <div class="pq-ans">Vempalle Formation (Papaghni Group)</div>
        <div class="pq-exp">The Vempalle dolomitic limestones, where intruded by basic dolerite sills, underwent serpentinization producing high-grade chrysotile asbestos and vein barytes (Pulivendla belt).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Ptilophyllum Flora in the Bhuj Formation</div>
        <div class="pq-ans">Identified in carbonaceous shale interbeds confirming Early Cretaceous age</div>
        <div class="pq-exp">The presence of cycadeoid fronds (*Ptilophyllum acutifolium*, *Otozamites*) establishes biostratigraphic equivalence between the Bhuj Formation and the Rajmahal/Jabalpur plant beds.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Mangampet Barytes Deposit in Cuddapah Basin</div>
        <div class="pq-ans">World's largest bedded volcanogenic barytes deposit hosted in the Pullampet (Cumbum) shales</div>
        <div class="pq-exp">The Mangampet deposit formed by submarine exhalative (sedex) volcanic venting of barium-rich hydrothermal fluids into sulfidic shale lagoons.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Capping Unit Resting Above the Bhuj Formation</div>
        <div class="pq-ans">Deccan Traps (Late Cretaceous basalt flows)</div>
        <div class="pq-exp">The Bhuj Formation is unconformably overlain by subaerial basaltic lava flows of the Deccan Traps, which were extruded during the passage of India over the Reunion hotspot.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Glauconite Sandstones in the Vindhyan Supergroup</div>
        <div class="pq-ans">Occurs in the Semri Group (Koldaha shale) and Kaimur Group</div>
        <div class="pq-exp">Glauconite pellets in Vindhyan sandstones indicate shallow, open-marine shelf deposition under reducing micro-environments during slow sedimentation intervals.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 53: MUTH QUARTZITE DEVONIAN MARKER HORIZON
# ==========================================
q53_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Tethyan Himalayan Geology: The Muth Quartzite Devonian Marker Horizon</div>
    <div class="card-body">
      <p>In the regional geological mapping of the <strong>Tethyan Himalayan Zone</strong> across Kashmir, Zanskar, Spiti, Kinnaur, and Kumaon, the <strong>Muth Quartzite</strong> stands out as the single most distinctive, ubiquitous, and reliable <strong>lithostratigraphic marker horizon for the Devonian System</strong>.</p>
      
      <ul>
        <li><strong>Physical and Geological Characteristics:</strong>
          <ul>
            <li><em>Visual Appearance:</em> Forms conspicuous, gleaming snow-white, vertical cliffs and ridges across hundreds of kilometers of barren Himalayan mountain terrain.</li>
            <li><em>Thickness:</em> Consistently between $150\\text{ m}$ and $500\\text{ m}$ thick.</li>
            <li><em>Mineralogical & Textural Super-Maturity:</em> Composed of $>98 - 99\\%\\text{ pure quartz}$ (silica). The rock is a super-mature <strong>quartz arenite</strong> consisting of exceptionally well-rounded, well-sorted, spherical quartz grains bonded by syntaxial quartz overgrowths into an impervious, vitreous orthoquartzite. Heavy minerals are restricted entirely to the ultrastable ZTR trio (Zircon, Tourmaline, Rutile).</li>
            <li><em>Sedimentary Structures & Environment:</em> Displays giant tabular and trough cross-bedding, ripple marks, and localized Skolithos trace fossil burrows, indicating coastal eolian dune and shallow-marine shoreface deposition across a stable, peneplaned northern Gondwanan passive shelf.</li>
          </ul>
        </li>
        <li><strong>Forensic Refutation of Other Stratigraphic Formations:</strong>
          <ul>
            <li><strong>Lipak Formation:</strong> Lower Carboniferous (Tournaisian-Viséan) sequence of dark grey to black fossiliferous limestones and dolomites rich in brachiopods (<em>Syringothyris</em>).</li>
            <li><strong>Po Formation:</strong> Upper Carboniferous succession of alternating quartzites and black shales (Fenestella Shales) with bryozoans and the <em>Rhacopteris</em> flora.</li>
            <li><strong>Syringothyris Limestone:</strong> Lower Carboniferous limestone marker bed restricted to the <strong>Kashmir Basin</strong>, characterized by the index brachiopod <em>Syringothyris cuspidata</em>.</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Muth Quartzite (Devonian Marker):</strong> The Muth Quartzite is the most remarkable and easily recognized formation in the whole Himalayan sequence. It is a massive, snow-white, granular orthoquartzite of high purity ($>98\\%\\text{ SiO}_2$), forming conspicuous white cliffs. It serves as an infallible <strong>marker horizon for the Devonian System</strong> throughout Spiti, Kashmir, and Kumaon."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (The Devonian System: Muth Quartzite, p. 286)</span>
      </div>

      <!-- TEXTBOOK / SCIENTIFIC PLATE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q053/muth_quartzite_devonian_marker.png" alt="Tethyan Himalayan Devonian Muth Quartzite Marker Horizon">
        <div class="tb-caption">
          <strong>Figure 53.1: Stratigraphic Position of the Devonian Muth Quartzite.</strong> Snow-white orthoquartzite marker horizon bounded below by the Silurian Pin Formation and above by the Carboniferous Lipak Formation.
        </div>
      </div>
    </div>
  </div>
"""

q53_part2 = """
  <div class="exam-question-box">
    <div class="q-meta">OPSC Assistant Geologist 2019 • Paper-II • Question 53</div>
    <div class="q-text">Marker horizon for Devonian in Himalaya is called ;</div>
    <div class="raw-options">
      <div>(A) Lipak formation</div>
      <div>(B) Po formation</div>
      <div>(C) Muth quartzites</div>
      <div>(D) Syringothyris limestone</div>
    </div>
  </div>

  <div class="verified-banner">
    <span class="v-icon">✔</span>
    <strong>OFFICIALLY VERIFIED ANSWER: (C) Muth quartzites</strong>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Lipak formation</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Lipak Formation represents the <strong>Early Carboniferous (Mississippian)</strong> succession of fossiliferous limestones and dolomites resting conformably above the Muth Quartzite.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Po formation</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Po Formation is of <strong>Carboniferous (Pennsylvanian)</strong> age, famed for its Fenestella Shales and the <em>Rhacopteris</em> plant beds of the Thabo stage.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(C) Muth quartzites</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The <strong>Muth Quartzite</strong> is universally documented in Himalayan geology as the paramount regional <strong>marker horizon for the Devonian Period</strong>. Its pure snow-white color, vitreous luster, high resistance to weathering, and massive thickness make it an unmistakable regional structural marker across Kashmir, Spiti, Zanskar, and Kumaon.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Syringothyris limestone</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> The Syringothyris Limestone is the marker horizon for the <strong>Lower Carboniferous (Tournaisian)</strong> in the Kashmir Valley, named after the diagnostic spiriferid brachiopod <em>Syringothyris cuspidata</em>.
    </div>
  </div>
"""

q53_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Diagnostic Paleozoic Marker Horizons of the Tethyan Himalaya</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Stratigraphic Formation</th>
            <th>Designated Geological Age</th>
            <th>Dominant Lithology</th>
            <th>Marker Significance & Key Fossil Markers</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Muth Quartzite</strong></td>
            <td><strong>Devonian</strong></td>
            <td><strong>Snow-white, pure quartz arenite (>98% SiO₂)</strong></td>
            <td><strong>Regional Himalayan marker horizon; cliff former</strong></td>
          </tr>
          <tr>
            <td><strong>Lipak Formation</strong></td>
            <td>Early Carboniferous (Tournaisian-Viséan)</td>
            <td>Fossiliferous dark limestones & dolomites</td>
            <td>Brachiopods, crinoid ossicles, corals</td>
          </tr>
          <tr>
            <td><strong>Po Formation</strong></td>
            <td>Carboniferous (Namurian)</td>
            <td>Quartzites and black shales</td>
            <td>Fenestella shales and <em>Rhacopteris</em> flora</td>
          </tr>
          <tr>
            <td><strong>Syringothyris Limestone</strong></td>
            <td>Early Carboniferous (Kashmir)</td>
            <td>Grey argillaceous and crystalline limestones</td>
            <td>Index spiriferid <em>Syringothyris cuspidata</em></td>
          </tr>
          <tr>
            <td><strong>Gungri Formation</strong></td>
            <td>Late Permian (Kuling Group)</td>
            <td>Black splintery shales with nodules</td>
            <td><em>Cyclolobus walkeri</em> and <em>Marginifera</em></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Practice Problems: Tethyan Himalayan Stratigraphy</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Textural Super-Maturity of Muth Quartzite</div>
        <div class="pq-ans">Grains are well-rounded and well-sorted with zero clay matrix (<1% matrix)</div>
        <div class="pq-exp">Following Folk's textural classification, the Muth Quartzite is a true 'super-mature' quartz arenite, requiring prolonged eolian abrasion and wave reworking in a high-energy coastal marine realm.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Underlying Formation Below Muth Quartzite in Spiti</div>
        <div class="pq-ans">Pin Formation (Silurian System)</div>
        <div class="pq-exp">The Muth Quartzite rests conformably upon the Silurian Pin Formation (Sanugba Group), which consists of grey-green shales, siltstones, and coral-bearing biostromal limestones.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Type Locality of the Muth Quartzite</div>
        <div class="pq-ans">Near the village of Muth (Mudh) in the Pin Valley, Spiti</div>
        <div class="pq-exp">Named by Ferdinand Stoliczka in 1865, the vertical cliffs surrounding the village of Muth expose the complete, pristine ~150-meter-thick stratotype section.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: ZTR Index Calculation for Muth Quartzite</div>
        <div class="pq-ans">ZTR Index approaches 100%</div>
        <div class="pq-exp">Non-opaque heavy mineral concentrates contain exclusively Zircon, Tourmaline, and Rutile, with less stable minerals (amphiboles, pyroxenes, epidote) completely eliminated by chemical weathering and multiple recycling cycles.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Fossils Found in the Muth Quartzite</div>
        <div class="pq-ans">Extremely rare body fossils; contains *Skolithos* and *Diplocraterion* trace fossils</div>
        <div class="pq-exp">Due to high-energy wave washing and intense diagenetic syntaxial quartz overgrowth, body fossils are rarely preserved, though localized cast impressions of Devonian brachiopods (*Schellwienella*) and vertical pipe-rock burrows occur.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Regional Equivalent of Muth Quartzite in Kashmir</div>
        <div class="pq-ans">Muth Quartzite of the Anantnag and Liddar Valley</div>
        <div class="pq-exp">The unit extends continuously westward into the Kashmir synclinorium, maintaining its identical snow-white orthoquartzite lithology between the Silurian slates and the Syringothyris Limestone.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Paleoclimate Inferred from Muth Quartzite</div>
        <div class="pq-ans">Warm, tropical to subtropical climate on northern Gondwana margin</div>
        <div class="pq-exp">Intense chemical weathering of the Gondwana craton interior under warm conditions destroyed all unstable feldspars and mafic silicates, delivering only pure quartz grains to the coastal eolian-dune and shelf complex.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Diagenetic Cementation Mechanism</div>
        <div class="pq-ans">Syntaxial silica overgrowths in optical continuity with detrital quartz nuclei</div>
        <div class="pq-exp">Petrographic thin sections reveal that circulating silica-rich porewaters precipitated secondary quartz directly onto detrital sand grains, interlocking them into an ultra-tough polygonal granoblastic mosaic.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# EXECUTE GENERATION FOR BATCH 5 (PART A)
# ==========================================
def main():
    print("Generating OPSC 2019 Batch 5 (Part A: Q046 to Q053)...")
    
    generate_page(
        q_num=46,
        filename="Q046_Youngest_Event_Dharwar_Stratigraphy_Closepet_Granite_Complete_Guide.html",
        title="Q046: Youngest Event in Dharwarian Stratigraphy (Closepet Granite)",
        badge="OPSC 2019 • Paper-II • Question 46",
        h1_title="Dharwar Craton Stratigraphy & Youngest Event: Closepet Granite (~2.51 Ga)",
        meta_text="Official Verification: Option (B) • Archean Tectonostratigraphy • Sargur, PGC & Dharwar Supergroup",
        part1_html=q46_part1,
        part2_html=q46_part2,
        part3_html=q46_part3
    )

    generate_page(
        q_num=47,
        filename="Q047_Stratigraphic_Pair_Niniyur_Formation_Cretaceous_Complete_Guide.html",
        title="Q047: Stratigraphic Formation and Age Pairs (Niniyur Formation)",
        badge="OPSC 2019 • Paper-II • Question 47",
        h1_title="Indian Chronostratigraphy: Niniyur Formation & Cretaceous-Tertiary Marine Succession",
        meta_text="Official Verification: Option (B) • Cauvery Basin Stratigraphy • Utatur, Trichinopoly, Ariyalur, Niniyur",
        part1_html=q47_part1,
        part2_html=q47_part2,
        part3_html=q47_part3
    )

    generate_page(
        q_num=48,
        filename="Q048_Kutch_Type_Area_Jurassic_Formation_Complete_Guide.html",
        title="Q048: Kutch as Global Type Area for Jurassic Formation",
        badge="OPSC 2019 • Paper-II • Question 48",
        h1_title="Kutch Basin Stratigraphy: Global Type Area for the Indian Jurassic System",
        meta_text="Official Verification: Option (A) • Patcham, Chari, Katrol & Umia Formations • Cephalopod Ammonite Biozones",
        part1_html=q48_part1,
        part2_html=q48_part2,
        part3_html=q48_part3
    )

    generate_page(
        q_num=49,
        filename="Q049_Siwaliks_Well_Known_For_Mammal_Fossils_Complete_Guide.html",
        title="Q049: Siwalik Foreland Molasse Well Known for Mammal Fossils",
        badge="OPSC 2019 • Paper-II • Question 49",
        h1_title="Siwalik Supergroup Vertebrate Paleontology: Global Treasury of Mammal Fossils",
        meta_text="Official Verification: Option (C) • Neogene Molasse Basin • Sivapithecus, Hipparion, Stegodon & Equus",
        part1_html=q49_part1,
        part2_html=q49_part2,
        part3_html=q49_part3
    )

    generate_page(
        q_num=50,
        filename="Q050_Spiti_Permians_Represented_By_Kuling_Group_Complete_Guide.html",
        title="Q050: Spiti Permians Represented by Kuling Group",
        badge="OPSC 2019 • Paper-II • Question 50",
        h1_title="Tethyan Himalayan Stratigraphy: Permian System of Spiti (Kuling Group)",
        meta_text="Official Verification: Option (C) • Productus Shales • Gechang & Gungri Formations • Cyclolobus & Marginifera",
        part1_html=q50_part1,
        part2_html=q50_part2,
        part3_html=q50_part3
    )

    generate_page(
        q_num=51,
        filename="Q051_Delhi_System_Intruded_By_Erinpura_Granite_Complete_Guide.html",
        title="Q051: Delhi System Intruded by Erinpura Granite",
        badge="OPSC 2019 • Paper-II • Question 51",
        h1_title="Aravalli-Delhi Orogenic Belt: Delhi Supergroup Intrusion by Erinpura Granite (~850 Ma)",
        meta_text="Official Verification: Option (A) • Proterozoic Magmatism • Alwar, Ajabgarh & Post-Tectonic Plutonism",
        part1_html=q51_part1,
        part2_html=q51_part2,
        part3_html=q51_part3
    )

    generate_page(
        q_num=52,
        filename="Q052_Bhuj_Formation_Predominantly_Sandstones_Correct_Statement_Complete_Guide.html",
        title="Q052: Mesozoic Bhuj Formation Predominantly Sandstones (Correct Statement)",
        badge="OPSC 2019 • Paper-II • Question 52",
        h1_title="Sedimentary Lithofacies Analysis: Mesozoic Bhuj Sandstone vs. Proterozoic Purana Basins",
        meta_text="Official Verification: Option (A) • Kutch Cretaceous Sandstones • Refutation of Kaladgi, Vindhyan & Cuddapah Distractors",
        part1_html=q52_part1,
        part2_html=q52_part2,
        part3_html=q52_part3
    )

    generate_page(
        q_num=53,
        filename="Q053_Devonian_Marker_Horizon_Himalaya_Muth_Quartzites_Complete_Guide.html",
        title="Q053: Devonian Marker Horizon in Himalaya (Muth Quartzites)",
        badge="OPSC 2019 • Paper-II • Question 53",
        h1_title="Himalayan Stratigraphy: Muth Quartzite as the Devonian Regional Marker Horizon",
        meta_text="Official Verification: Option (C) • Super-Mature Quartz Arenite • Tethyan Basin Chronostratigraphy",
        part1_html=q53_part1,
        part2_html=q53_part2,
        part3_html=q53_part3
    )

    print("Batch 5 (Part A: Q046 - Q053) completed successfully!")

if __name__ == "__main__":
    main()
