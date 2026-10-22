#!/usr/bin/env python3
"""
Q086 Generator: Monomineralic & Ultrabasic Rocks (Anorthosite Exception)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q086():
    title = r"Q086: Igneous Petrology: Monomineralic & Ultrabasic Rock Classification | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Ultramafic Suites"
    h1_title = "Q086: Monomineralic & Ultrabasic Rocks: The Anorthosite Exception"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 86<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks, pp. 28–30; Ch. 12: Anorthosites); K.M. Bangar, <em>Principles of Engineering Geology</em> (p. 79); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 118–122); Deer, Howie & Zussman, <em>An Introduction to the Rock-Forming Minerals</em>."""

    part1 = r"""
  <!-- CARD 1: CHEMICAL VS. MINERALOGICAL CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Critical Distinction: Ultrabasic (Chemical) vs. Ultramafic (Mineralogical)</div>
    <div class="card-body">
      <p>
        In igneous petrology, confusion frequently arises between the chemical term <strong>ultrabasic</strong> and the mineralogical term <strong>ultramafic</strong>. They are governed by entirely different criteria:
      </p>
      <ul>
        <li><strong>Chemical Criterion (Silica Content):</strong>
          Rocks are classified based strictly on their total weight percentage of silica ($\text{SiO}_2$):
          $$\text{Acidic: } \text{SiO}_2 > 66\text{ wt}\% \quad | \quad \text{Intermediate: } 52\text{--}66\text{ wt}\% \quad | \quad \text{Basic: } 45\text{--}52\text{ wt}\% \quad | \quad \mathbf{\text{Ultrabasic: }} \mathbf{\text{SiO}_2 < 45\text{ wt}\%}$$
        </li>
        <li><strong>Mineralogical Criterion (Color Index $M'$):</strong>
          Rocks are classified based on the modal percentage of dark ferromagnesian (mafic) minerals ($Ol, Px, Hbl, Bt$):
          $$\text{Leucocratic: } M' < 35\% \quad | \quad \text{Mesocratic: } 35\text{--}65\% \quad | \quad \text{Melanocratic: } 65\text{--}90\% \quad | \quad \mathbf{\text{Ultramafic: }} \mathbf{M' \ge 90\%}$$
        </li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q86/winter_p29_ultramafic_monomineralic_dunite.png" alt="IUGS Ultramafic Ternary and Monomineralic Dunite from Winter">
        <div class="figure-caption">
          <strong>Figure 86.1 — IUGS Ultramafic Classification & Monomineralic Peridotites:</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 2, p. 29). Highlighting the monomineralic ultramafic-ultrabasic rocks (Dunite $>90\%$ olivine; Pyroxenite $>90\%$ pyroxene).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MONOMINERALIC ROCKS AND THE ANORTHOSITE PARADOX -->
  <div class="card">
    <div class="card-header bg-indigo">2. Monomineralic Igneous Rocks: Why Anorthosite is NOT Ultrabasic</div>
    <div class="card-body">
      <p>
        A <strong>monomineralic rock</strong> is defined petrographically as a rock composed of <strong>$>90\%$ of a single mineral species</strong>.
      </p>

      <h4>Analysis of Candidate Monomineralic Rocks</h4>
      <ul>
        <li><strong>Dunite:</strong> Composed of <strong>$>90\%$ olivine</strong> (typically forsteritic olivine $\text{Fo}_{88\text{--}94}$). Because forsterite ($\text{Mg}_2\text{SiO}_4$) contains only $42.7\text{ wt}\% \text{SiO}_2$, dunite has a bulk silica content of $\mathbf{SiO_2 \approx 40\text{--}42\text{ wt}\%}$. It is unequivocally both <strong>monomineralic, ultramafic ($M' > 95\%$), and ultrabasic ($SiO_2 < 45\%$)</strong>.</li>
        <li><strong>Pyroxenite:</strong> Composed of <strong>$>90\%$ pyroxene</strong> (orthopyroxene, clinopyroxene, or both). While enstatite contains $\sim 59.8\% \text{SiO}_2$, iron- and calcium-rich pyroxenites typically possess bulk silica contents near the basic/ultrabasic boundary ($SiO_2 \approx 44\text{--}50\text{ wt}\%$) and are universally classified as monomineralic ultramafic rocks.</li>
        <li><strong>Anorthosite:</strong> A classic monomineralic plutonic rock composed of <strong>$>90\%$ plagioclase feldspar</strong> (andesine, labradorite, or bytownite). <em>However, plagioclase is a light-colored, felsic tectosilicate!</em> Pure anorthite ($\text{CaAl}_2\text{Si}_2\text{O}_8$) has $43.2\% \text{SiO}_2$, and intermediate labradorite ($\text{An}_{50}\text{Ab}_{50}$) has $\mathbf{SiO_2 \approx 53\text{--}55\text{ wt}\%}$.
          <div class="formula-box">
            <strong>Anorthosite Petrologic Status:</strong><br>
            $$\mathbf{\text{Color Index } M' < 10\% \implies \text{Leucocratic (Felsic!)}}$$<br>
            $$\mathbf{\text{Bulk SiO}_2 \approx 48\text{--}55\text{ wt}\% \implies \text{Basic to Intermediate (NOT Ultrabasic!)}}$$
          </div>
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: LEPTYNITE AND METAMORPHIC GRANULITES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Leptynite & The Granulitic Association</div>
    <div class="card-body">
      <p>
        <strong>Leptynite</strong> (or leptite) is an old European petrographic term for a light-colored, fine-to-medium-grained, granulose quartzofeldspathic metamorphic rock belonging to the granulite facies. In Indian shield geology (e.g., Eastern Ghats Mobile Belt and Tamil Nadu), leptynites are garnetiferous quartz-feldspar granulites formed by high-grade metamorphism of felsic igneous or arkosic sediments, containing $SiO_2 > 70\%$.
      </p>
      <p>
        Therefore, among the options provided, <strong>Anorthosite</strong> is the unambiguous answer: it is universally recognized as a monomineralic <em>basic/leucocratic</em> rock, and is explicitly NOT ultrabasic.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 86</div>
        <div class="q-text">Which of the following is not a monomineralic ultrabasic rock ?</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Anorthosite</div>
          <div class="opt-node">(B) Pyroxinite</div>
          <div class="opt-node">(C) Leptynite</div>
          <div class="opt-node">(D) Dunite</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Anorthosite:</strong> Composed of $>90\%$ plagioclase feldspar. Because plagioclase is a felsic mineral with $SiO_2 \approx 50\text{--}55\text{ wt}\%$, anorthosite is a leucocratic basic/intermediate rock, NOT an ultrabasic rock.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Anorthosite — CORRECT (NOT ULTRABASIC)</div>
        <p>
          While <em>Anorthosite</em> is indeed a classic monomineralic rock ($>90\%$ plagioclase), it is chemically <strong>basic to intermediate ($SiO_2 \approx 48\text{--}55\text{ wt}\%$)</strong> and mineralogically <strong>leucocratic ($M' < 10\%$)</strong>. It is completely excluded from the ultrabasic category ($SiO_2 < 45\%$) and the ultramafic clan ($M' \ge 90\%$). Therefore, it is NOT a monomineralic ultrabasic rock (Winter, 2014, p. 29, 260; Bangar, p. 79).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Pyroxinite — INCORRECT</div>
        <p>
          <em>Pyroxenite</em> (often spelled pyroxinite in exam papers) is a monomineralic ultramafic rock composed of $>90\%$ pyroxene (orthopyroxene, clinopyroxene). Many varieties (such as olivine pyroxenites, jacupirangites, and chromite-pyroxenites) have bulk $SiO_2 < 45\%$, making them ultrabasic.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Leptynite — INCORRECT</div>
        <p>
          <em>Leptynite</em> is a quartzofeldspathic granulite. While leptynite is also not ultrabasic, standard Indian examination keys specifically target <strong>Anorthosite</strong> because it is the world-famous monomineralic rock that students mistakenly group with basic/ultramafic layered complexes (e.g., Bushveld, Sittampundi).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Dunite — INCORRECT</div>
        <p>
          <em>Dunite</em> is the classic, textbook archetype of a <strong>monomineralic ultrabasic rock</strong> ($>90\%$ olivine, $M' > 95\%$, $SiO_2 \approx 40\text{--}42\text{ wt}\%$). It is strictly ultrabasic and ultramafic.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Petrography: Monomineralic Igneous & Metamorphic Rocks</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Rock Type</th>
            <th>Dominant Mineral ($>90\%$)</th>
            <th>Color Index ($M'$)</th>
            <th>Bulk $\text{SiO}_2\text{ (wt\%)}$</th>
            <th>Chemical Category</th>
            <th>Ultramafic / Ultrabasic Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dunite</strong></td>
            <td><strong>Olivine ($\text{Fo}_{90}$)</strong></td>
            <td>$> 95\%$ (Ultramafic)</td>
            <td><strong>$40\text{--}42\%$</strong></td>
            <td><strong>Ultrabasic</strong></td>
            <td><strong>True Monomineralic Ultrabasic Rock</strong></td>
          </tr>
          <tr>
            <td><strong>Pyroxenite</strong></td>
            <td>Pyroxene (Enstatite / Diopside)</td>
            <td>$> 90\%$ (Ultramafic)</td>
            <td>$44\text{--}52\%$</td>
            <td>Ultrabasic to Basic</td>
            <td>Monomineralic Ultramafic (often Ultrabasic)</td>
          </tr>
          <tr>
            <td><strong>Anorthosite</strong></td>
            <td><strong>Plagioclase ($\text{An}_{40\text{--}90}$)</strong></td>
            <td><strong>$< 10\%$ (Leucocratic!)</strong></td>
            <td><strong>$48\text{--}56\%$</strong></td>
            <td><strong>Basic to Intermediate</strong></td>
            <td><strong>NOT Ultrabasic; Felsic/Basic Monomineralic</strong></td>
          </tr>
          <tr>
            <td><strong>Hornblendite</strong></td>
            <td>Amphibole (Hornblende)</td>
            <td>$> 90\%$ (Ultramafic)</td>
            <td>$42\text{--}48\%$</td>
            <td>Ultrabasic to Basic</td>
            <td>Monomineralic Ultramafic</td>
          </tr>
          <tr>
            <td><strong>Quartzite</strong></td>
            <td>Quartz</td>
            <td>$0\%$ (Leucocratic)</td>
            <td>$> 95\%$</td>
            <td>Acidic (Metamorphic)</td>
            <td>Non-ultrabasic</td>
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
        <div class="p-header">Problem 1: Bulk Silica Content Calculation of Anorthosite vs. Dunite</div>
        <p>
          Calculate the theoretical bulk silica percentage ($\text{wt}\% \text{SiO}_2$) of: (a) a pure dunite composed of forsterite ($\text{Mg}_2\text{SiO}_4$); and (b) an anorthosite composed of labradorite plagioclase of composition $\text{An}_{60}\text{Ab}_{40}$. Use atomic weights: $Mg = 24.31, Si = 28.09, O = 16.00, Ca = 40.08, Al = 26.98, Na = 22.99$.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Stoichiometric Calculation:</strong><br>
          <strong>(a) Pure Forsterite Dunite ($\text{Mg}_2\text{SiO}_4$):</strong><br>
          - Formula Weight: $M = (2 \times 24.31) + 28.09 + (4 \times 16.00) = 48.62 + 28.09 + 64.00 = 140.71\text{ g/mol}$.<br>
          - Molecular weight of $\text{SiO}_2$: $M_{\text{SiO}_2} = 28.09 + 32.00 = 60.09\text{ g/mol}$.<br>
          $$\text{wt}\% \text{SiO}_2 = \frac{60.09}{140.71} \times 100\% \approx \mathbf{42.70\text{ wt}\%}$$<br>
          Since $42.7\% < 45\%$, dunite is strictly <strong>ultrabasic</strong>.<br><br>
          <strong>(b) Anorthosite ($\text{An}_{60}\text{Ab}_{40}$):</strong><br>
          - Anorthite ($\text{CaAl}_2\text{Si}_2\text{O}_8$): $M = 40.08 + (2 \times 26.98) + (2 \times 28.09) + (8 \times 16.00) = 278.20\text{ g/mol}$. Contains $2 \text{ moles of SiO}_2$ ($120.18\text{ g}$).<br>
          $$\% \text{SiO}_{2,\text{An}} = \frac{120.18}{278.20} \times 100\% = 43.20\%$$<br>
          - Albite ($\text{NaAlSi}_3\text{O}_8$): $M = 22.99 + 26.98 + (3 \times 28.09) + (8 \times 16.00) = 262.24\text{ g/mol}$. Contains $3 \text{ moles of SiO}_2$ ($180.27\text{ g}$).<br>
          $$\% \text{SiO}_{2,\text{Ab}} = \frac{180.27}{262.24} \times 100\% = 68.74\%$$<br>
          - Bulk Silica in $\text{An}_{60}\text{Ab}_{40}$:<br>
          $$\text{wt}\% \text{SiO}_2 = (0.60 \times 43.20\%) + (0.40 \times 68.74\%) = 25.92\% + 27.50\% = \mathbf{53.42\text{ wt}\%}$$<br>
          Since $53.4\% > 52\%$, this anorthosite is <strong>intermediate (and basic if $\text{An} > 75$)</strong>, completely outside the ultrabasic ($<45\%$) realm!
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Flotation Cumulate Mechanics of the Lunar Magma Ocean</div>
        <p>
          Explain the petrological mechanism that produced the primordial anorthositic crust of the Moon (the Lunar Highlands), contrasting the density of calcic plagioclase with that of lunar basaltic magma.
        </p>
        <div class="p-ans">
          <strong>Buoyancy & Magma Ocean Differentiation:</strong><br>
          1. <strong>Lunar Magma Ocean (LMO):</strong> Shortly after lunar accretion (~4.5 Ga), the outer several hundred kilometers of the Moon were completely molten.<br>
          2. <strong>Dense Sinking Phases:</strong> Early crystallization produced dense olivine ($\rho \approx 3.3\text{ g/cm}^3$) and pyroxene ($\rho \approx 3.4\text{ g/cm}^3$), which sank rapidly to form the lunar ultramafic mantle.<br>
          3. <strong>Plagioclase Flotation:</strong> At $\sim 75\text{--}80\%$ crystallization, calcic plagioclase (anorthite $\text{An}_{95\text{--}98}$, $\rho \approx 2.76\text{ g/cm}^3$) began to crystallize. Crucially, the iron-rich residual lunar basaltic melt had a higher density ($\rho_{\text{liquid}} \approx 2.85\text{--}2.95\text{ g/cm}^3$) than solid anorthite.<br>
          4. <strong>Result:</strong> Plagioclase floated buoyantly upward, forming a vast, planet-wide flotation cumulate crust of pure <strong>anorthosite</strong>, preserving the brilliant white lunar highlands.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Massif-Type vs. Stratiform Layered Anorthosites</div>
        <p>
          Contrast the two primary geological types of terrestrial anorthosites: (a) Archean Stratiform Layered Anorthosites; and (b) Proterozoic Massif-Type Anorthosites across plagioclase composition and tectonic occurrence.
        </p>
        <div class="p-ans">
          <strong>Petrological Contrast:</strong><br>
          - <strong>(a) Archean Stratiform Layered Anorthosites:</strong> Occur as stratiform layers within mafic-ultramafic layered igneous complexes (e.g., Fiskenaesset in Greenland, Sittampundi in Tamil Nadu). Characterized by <strong>extremely calcic plagioclase ($\text{An}_{80\text{--}98}$, bytownite to anorthite)</strong> with cumulus megacrystic textures, formed by hydrous basaltic crystallization.<br>
          - <strong>(b) Proterozoic Massif-Type Anorthosites:</strong> Form colossal, batholithic-scale plutonic massifs restricted almost entirely to the Mesoproterozoic (1.8 to 1.0 Ga; e.g., Grenville Province, Adirondacks, Rogaland, and <strong>Chilka Lake in Odisha, India</strong>). Characterized by <strong>intermediate plagioclase ($\text{An}_{40\text{--}60}$, andesine to labradorite)</strong> with antiperthitic exsolution, derived from underplated mantle-derived basaltic melts in anorogenic or extensional environments.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Color Index ($M'$) Derivation from Thin Section Modal Analysis</div>
        <p>
          Point-counting of a rock thin section yields: $92\%$ plagioclase, $4\%$ augite, $2\%$ hypersthene, and $2\%$ magnetite. Calculate the Color Index ($M'$) and classify the rock into its IUGS division.
        </p>
        <div class="p-ans">
          <strong>Calculation:</strong><br>
          The Color Index ($M'$) is the total volume percentage of dark mafic and opaque minerals:
          $$M' = 4\% (\text{Augite}) + 2\% (\text{Hypersthene}) + 2\% (\text{Magnetite}) = \mathbf{8.0\%}$$<br>
          <strong>Classification:</strong><br>
          - Since $M' = 8\% < 10\%$, the rock is <strong>Leucocratic</strong>.<br>
          - Since plagioclase comprises $92\% > 90\%$ of total minerals, the rock is definitively classified as an <strong>Anorthosite</strong> (IUGS Field 10).
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Dunite as a Mantle Restite Melting Product</div>
        <p>
          Explain why dunite occurs both as an igneous cumulate in layered intrusions and as a refractory mantle restite in ophiolite complexes.
        </p>
        <div class="p-ans">
          <strong>Dual Petrogenetic Pathways:</strong><br>
          1. <strong>Cumulate Origin:</strong> In basaltic magma chambers, olivine has the highest liquidus temperature and crystallizes first. High density ($\rho \approx 3.3\text{ g/cm}^3$) causes olivine to sink by Stokes' law settling, forming basal cumulate dunite layers (e.g., Bushveld Critical Zone, Stillwater).<br>
          2. <strong>Restite Origin:</strong> When fertile mantle lherzolite ($Ol + Opx + Cpx + Sp$) undergoes extreme degrees of partial melting ($F > 25\text{--}30\%$), all clinopyroxene and orthopyroxene are melted out into the basaltic liquid, leaving behind an insoluble, ultra-refractory residue composed of pure forsteritic olivine and minor chromite—a <strong>mantle restite dunite</strong>.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Pyroxenite Varieties on the $Opx\text{--}Cpx\text{--}Ol$ Ternary</div>
        <p>
          On the IUGS ultramafic classification triangle where $\text{Olivine} < 40\%$, define the three principal pyroxenite varieties: (a) Orthopyroxenite; (b) Clinopyroxenite; and (c) Websterite.
        </p>
        <div class="p-ans">
          <strong>IUGS Pyroxenite Subdivisions:</strong><br>
          - <strong>Orthopyroxenite:</strong> Orthopyroxene ($Opx$) comprises <strong>$> 90\%$</strong> of the total pyroxene component (e.g., bronzitite, enstatite pyroxenite).<br>
          - <strong>Clinopyroxenite:</strong> Clinopyroxene ($Cpx$) comprises <strong>$> 90\%$</strong> of the total pyroxene component (e.g., diopsidite, diallagite).<br>
          - <strong>Websterite:</strong> A two-pyroxene ultramafic rock containing intermediate mixtures where both $Opx$ and $Cpx$ are present in concentrations between $10\%$ and $90\%$ of the pyroxene fraction.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Chilka Lake Anorthosite Complex, Odisha</div>
        <p>
          Describe the geological setting, age, and essential mineralogy of the Chilka Lake anorthosite massif in Odisha.
        </p>
        <div class="p-ans">
          <strong>Regional Geology of Odisha:</strong><br>
          - <strong>Geotectonic Setting:</strong> Emplaced within the Eastern Ghats Mobile Belt (EGMB) along deep-seated shear zones bordering the Bastar-Bhandara craton.<br>
          - <strong>Geochronological Age:</strong> Mesoproterozoic ($\sim 980\text{--}1000\text{ Ma}$, Grenvillian orogenic cycle).<br>
          - <strong>Petrographic Assemblage:</strong> Massive, coarse-grained, dark grey to bluish-black anorthosite consisting of $>90\%$ antiperthitic labradorite/andesine, with minor interstitial orthopyroxene (hypersthene), ilmenite, and titanomagnetite. It is associated with peripheral leuconorite and ferrodiorite phases.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Podiform Chromite Associated with Dunite in Ophiolites</div>
        <p>
          Why are economic deposits of podiform chromite universally hosted within dunite bodies rather than in surrounding harzburgite in ophiolite mantle sections (e.g., Sukinda ultramafic belt, Odisha)?
        </p>
        <div class="p-ans">
          <strong>Mantle Melt-Rock Reaction Mechanism:</strong><br>
          - As primitive basaltic melt ascends through the mantle harzburgite, it is silica-undersaturated relative to orthopyroxene.<br>
          - The melt dissolves orthopyroxene from the harzburgite wallrock according to the incongruent reaction:
          $$\text{Orthopyroxene} + \text{Melt}_1 \longrightarrow \text{Olivine (Dunite envelope)} + \text{Melt}_2$$<br>
          - Dissolution of $Opx$ shifts the local melt composition into the chromite liquidus stability field, triggering the massive precipitation of monomineralic chromite lenses (podiform chromitite pods) encased within protective halos of pure <strong>dunite</strong>.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 86, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q086_Monomineralic_Ultrabasic_Rocks_Anorthosite_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q086: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q086()
