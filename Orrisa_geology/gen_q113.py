#!/usr/bin/env python3
"""
Q113 Generator: Index Minerals & Typomorphic Minerals in Metamorphism
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q113():
    title = r"Q113: Metamorphic Petrology: Index Minerals & Typomorphic Minerals | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Mineralogy"
    h1_title = "Q113: Metamorphic Grade Indicators: Index Minerals vs. Typomorphic Minerals"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 113<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: An Introduction to Metamorphic Petrology / Index Minerals, pp. 420–428; Fig. 21.2); Pentti Eskola (1915, 1920), <em>The Mineral Facies of Rocks</em>; Francis J. Turner and John Verhoogen, <em>Igneous and Metamorphic Petrology</em> (McGraw-Hill); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS OF INDEX AND TYPOMORPHIC MINERALS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definitions, Historical Genesis & Concepts: Index Minerals and Typomorphic Minerals</div>
    <div class="card-body">
      <p>
        In metamorphic geology and petrogenesis (Winter, 2014, pp. 420–428; Turner & Verhoogen, 1960; Bucher & Grapes, 2011), the reconstruction of temperature and pressure regimes relies on minerals whose chemical stability fields are restricted to specific thermodynamic boundaries:
      </p>
      <ol>
        <li><strong>Index Minerals:</strong> First introduced by George Barrow (1893, 1912) in the Scottish Highlands, an <strong>index mineral</strong> is a specific metamorphic mineral whose <em>first appearance</em> (entry isograd) across a metamorphic terrane marks the beginning of a new, higher metamorphic zone or grade under prograde conditions (e.g., Chlorite $\rightarrow$ Biotite $\rightarrow$ Garnet $\rightarrow$ Staurolite $\rightarrow$ Kyanite $\rightarrow$ Sillimanite).</li>
        <li><strong>Typomorphic Minerals:</strong> Formulated in the foundational metamorphic facies theory of Pentti Eskola (1915, 1920) and V.M. Goldschmidt, a <strong>typomorphic mineral</strong> (from Greek <em>typos</em> = type + <em>morphe</em> = form) is a mineral whose occurrence is strictly limited to and diagnostic of a particular metamorphic grade, facies, or $P\text{-}T$ field. For instance, <em>glaucophane</em> is typomorphic of the blueschist facies; <em>omphacite</em> is typomorphic of the eclogite facies; <em>sillimanite</em> is typomorphic of the upper amphibolite to granulite facies.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q113/winter_p425_index_and_typomorphic_minerals.png" alt="Index Minerals and Metamorphic Isograds from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 113.1 — Barrovian Index Minerals and Typomorphic Facies Assemblages:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 425). Illustrates the spatial distribution of index minerals and typomorphic metamorphic mineral stability fields in regional orogenic terranes.
        </div>
      </div>

      <h4>Comparison of Index Minerals vs. Typomorphic Minerals</h4>
      <p>
        While both terms designate minerals characteristic of a specific metamorphic grade, they emphasize distinct methodological perspectives:
      </p>
      <ul>
        <li><strong>Index Mineral:</strong> An operational field-mapping concept. Geologists map the <em>isograd line</em> connecting the first points of macroscopic emergence of the mineral in pelitic rocks.</li>
        <li><strong>Typomorphic Mineral:</strong> A rigorous thermodynamic and facies concept. It represents a phase that crystallizes exclusively under the restricted $P\text{-}T\text{-}X$ conditions of that particular facies, vanishing at higher or lower grades.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: CANONICAL EXAMPLES & FACIES PARAGENESIS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Canonical Catalog of Index and Typomorphic Minerals across Facies</div>
    <div class="card-body">
      <h4>Typomorphic Minerals Diagnostic of Major Metamorphic Facies</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Facies</th>
            <th>Governing P-T Regime</th>
            <th>Typomorphic / Index Minerals</th>
            <th>Protolith Expression</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Zeolite Facies</strong></td>
            <td>Very Low $T$ ($100\text{--}250^\circ\text{C}$), Low $P$</td>
            <td><strong>Laumontite, Heulandite, Wairakite</strong></td>
            <td>Burial metamorphism of volcanic greywackes / basalts</td>
          </tr>
          <tr>
            <td><strong>Prehnite-Pumpellyite</strong></td>
            <td>Low $T$ ($200\text{--}300^\circ\text{C}$), Mod. $P$</td>
            <td><strong>Prehnite, Pumpellyite</strong></td>
            <td>Hydrothermal / burial alteration of mafic volcanics</td>
          </tr>
          <tr>
            <td><strong>Greenschist Facies</strong></td>
            <td>Low $T$ ($300\text{--}450^\circ\text{C}$), Mod. $P$</td>
            <td><strong>Chlorite, Actinolite, Epidote, Albite</strong></td>
            <td>Regional metamorphism of pelites and basalts</td>
          </tr>
          <tr>
            <td><strong>Amphibolite Facies</strong></td>
            <td>Medium-High $T$ ($500\text{--}700^\circ\text{C}$), Mod. $P$</td>
            <td><strong>Hornblende, Almandine Garnet, Staurolite, Kyanite</strong></td>
            <td>Medium-grade regional collision orogens</td>
          </tr>
          <tr>
            <td><strong>Granulite Facies</strong></td>
            <td>High $T$ ($700\text{--}900^\circ\text{C}$), Moderate-High $P$</td>
            <td><strong>Orthopyroxene (Hypersthene), Sillimanite, Peritectic Garnet</strong></td>
            <td>Deep anhydrous lower continental crust</td>
          </tr>
          <tr>
            <td><strong>Blueschist Facies</strong></td>
            <td>Low $T$ ($200\text{--}400^\circ\text{C}$), High $P$ ($> 6\text{--}12\text{ kbar}$)</td>
            <td><strong>Glaucophane, Lawsonite, Jadeite, Aragonite</strong></td>
            <td>Subduction zones, underthrust oceanic slabs</td>
          </tr>
          <tr>
            <td><strong>Eclogite Facies</strong></td>
            <td>Moderate-High $T$, Ultra-High $P$ ($> 12\text{--}30\text{ kbar}$)</td>
            <td><strong>Omphacite (Na-pyroxene) + Pyrope-rich Garnet</strong></td>
            <td>Deep subducted oceanic crust, mantle lithosphere</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 113:</strong> Minerals that are characteristic for a certain metamorphic grade are called :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Typomorphic minerals</div>
        <div class="option-item"><strong>(B)</strong> Barrovian minerals</div>
        <div class="option-item"><strong>(C)</strong> Index minerals</div>
        <div class="option-item correct-option"><strong>(D)</strong> Both (A) and (C) are correct</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) Both (A) and (C) are correct</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Evaluated — Typomorphic Minerals</div>
        <p>
          <strong>Partially Correct but Incomplete:</strong> In Pentti Eskola's metamorphic facies theory and classic European petrology (Turner & Verhoogen, 1960), minerals whose occurrence is restricted to and diagnostic of a specific metamorphic grade or facies are explicitly designated as <strong>typomorphic minerals</strong>. However, selecting (A) alone fails to recognize that "Index minerals" is an equally valid, widely recognized term for this exact concept.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Barrovian Minerals</div>
        <p>
          <strong>Incorrect:</strong> "Barrovian minerals" is an informal colloquial term referring strictly to George Barrow's specific sequence of six pelitic minerals in the Scottish Highlands (chlorite, biotite, garnet, staurolite, kyanite, sillimanite). It is not the formal scientific definition for minerals characteristic of a metamorphic grade in general (which applies across all metamorphic facies, Buchan series, and mafic/carbonate protoliths).
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Evaluated — Index Minerals</div>
        <p>
          <strong>Partially Correct but Incomplete:</strong> In British and American geological literature (Winter, 2014, p. 420; Bangar, p. 85), minerals whose appearance marks a specific metamorphic grade are formally called <strong>index minerals</strong>. However, because "typomorphic minerals" is also canonically correct, choosing (C) alone misses the unified composite option.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — Both (A) and (C) are Correct</div>
        <p>
          <strong>Correct:</strong> Both <strong>Typomorphic minerals</strong> (Eskola's facies concept) and <strong>Index minerals</strong> (Barrow's zonal concept) are standard, authoritative geological designations for minerals that are characteristic of a specific metamorphic grade. Therefore, Option <strong>(D) Both (A) and (C) are correct</strong> is the comprehensive, official verified answer.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis: Typomorphic Minerals vs. Index Minerals vs. Persistent Minerals</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Mineral Designation</th>
            <th>Scientific Definition</th>
            <th>Historical Proponent</th>
            <th>Diagnostic Behavior Across P-T Space</th>
            <th>Classic Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Typomorphic Mineral</strong></td>
            <td>A mineral phase whose thermodynamic stability field is strictly restricted to and diagnostic of a specific metamorphic grade or facies.</td>
            <td>Pentti Eskola (1915, 1920); V.M. Goldschmidt</td>
            <td>Disappears at higher or lower grades outside the specific facies boundary.</td>
            <td>Glaucophane (Blueschist), Lawsonite, Staurolite, Omphacite (Eclogite).</td>
          </tr>
          <tr>
            <td><strong>Index Mineral</strong></td>
            <td>A mineral whose initial macroscopic appearance (entry isograd) marks the attainment of a defined metamorphic grade during prograde metamorphism.</td>
            <td>George Barrow (1893, 1912)</td>
            <td>Defines the lower temperature boundary (isograd) of a metamorphic zone.</td>
            <td>Biotite, Almandine Garnet, Kyanite, Sillimanite.</td>
          </tr>
          <tr>
            <td><strong>Persistent (Ubiquitous) Mineral</strong></td>
            <td>A mineral possessing an enormous thermodynamic stability field, remaining stable across virtually all metamorphic grades without alteration.</td>
            <td>Classical Mineralogy</td>
            <td>Provides zero information regarding metamorphic grade or temperature.</td>
            <td>Quartz ($\text{SiO}_2$), Calcite ($\text{CaCO}_3$, up to high-T decarbonation), Magnetite.</td>
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
        <p>Explain why quartz is never used as an index mineral or typomorphic mineral in metamorphic petrology, despite being the most abundant mineral in pelitic schists and gneisses.</p>
        <p><strong>Solution:</strong>
          An index or typomorphic mineral must have a <strong>restricted thermodynamic stability field</strong> with sharp, well-defined entry or exit reactions in $P\text{-}T$ space. Low-quartz is chemically stable from surface weathering temperatures ($25^\circ\text{C}$) up to $573^\circ\text{C}$ (where it inverts to high-quartz), remaining stable up to $870^\circ\text{C}$ (tridymite) across all crustal pressures. Because quartz persists unchanged from un-metamorphosed shale through slate, phyllite, schist, and granulite, its mere presence provides <strong>zero diagnostic information regarding metamorphic grade</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>What is an "isograd" and how is it related to the concept of index minerals on a regional geological map?</p>
        <p><strong>Solution:</strong>
          An <strong>isograd</strong> (introduced by C.E. Tilley in 1924) is a mapped line of equal metamorphic grade on a geological map representing the <strong>first appearance (entry isograd) of a specific index mineral</strong> in rocks of appropriate bulk composition (e.g., the "garnet isograd" marks the locus of points where almandine garnet first crystallizes from chlorite and muscovite). An isograd physically represents a continuous thermodynamic reaction boundary in $P\text{-}T$ space.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>State the typomorphic mineral pair that definitively defines the Eclogite facies in metamorphosed basaltic crust.</p>
        <p><strong>Solution:</strong>
          The Eclogite facies is defined by the coexistence of two typomorphic minerals:
          1. <strong>Omphacite:</strong> A sodic clinopyroxene solid solution between diopside ($\text{CaMgSi}_2\text{O}_6$) and jadeite ($\text{NaAlSi}_2\text{O}_6$).
          2. <strong>Pyrope-rich Garnet:</strong> A magnesium-rich garnet ($\text{(Mg,Fe,Ca)}_3\text{Al}_2\text{Si}_3\text{O}_{12}$).
          Crucially, <strong>plagioclase feldspar is completely absent</strong> in eclogite, having broken down under extreme pressure ($P > 12\text{--}15\text{ kbar}$) into omphacite and quartz.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Why can staurolite serve as an index mineral only in "pelitic" rocks (aluminous shales) and not in metabasites or impure limestones?</p>
        <p><strong>Solution:</strong>
          Metamorphic mineral assemblages are governed simultaneously by physical conditions ($P, T$) and <strong>bulk rock chemical composition ($X_{bulk}$)</strong>. Staurolite ($\text{Fe}_2\text{Al}_9\text{O}_6(\text{SiO}_4)_4(\text{O,OH})_2$) is an ultra-aluminous, iron-rich silicate. It can crystallize only in rocks possessing high $\text{Al}_2\text{O}_3$ and $\text{FeO}$ relative to $\text{MgO}, \text{CaO}$, and $\text{K}_2\text{O}$—a chemical signature unique to pelitic shales. Metabasites are rich in $\text{Ca, Mg}$, and poor in excess $\text{Al}$, crystallizing hornblende and plagioclase instead.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>What is a "bathozone" and how does it relate to index minerals?</p>
        <p><strong>Solution:</strong>
          A <strong>bathozone</strong> (Carmichael, 1978) is a metamorphic pressure zone delineated by the invariant intersections and relative stability order of index minerals in $P\text{-}T$ space (specifically the $\text{Al}_2\text{SiO}_5$ polymorphs and their reactions with staurolite, muscovite, and garnet). For example, Carmichael divided metamorphic crust into six bathozones (Bathozone 1 to 6), where higher bathozones indicate progressively deeper crustal burial during regional metamorphism.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>In low-pressure / high-temperature metamorphism (Buchan / Abukuma type), what index mineral sequence replaces the Barrovian Staurolite-Kyanite sequence?</p>
        <p><strong>Solution:</strong>
          Under Buchan low-pressure conditions ($P < 3.5\text{ kbar}$), high geothermal gradients bypass the stability fields of staurolite and kyanite. Instead, the prograde index sequence is:
          $$\text{Biotite} \rightarrow \mathbf{\text{Cordierite}} \rightarrow \mathbf{\text{Andalusite}} \rightarrow \text{Sillimanite} \pm \text{K-feldspar}$$
          Here, <strong>cordierite and andalusite</strong> serve as the diagnostic low-pressure typomorphic index minerals.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>How does the presence of "chloritoid" vs. "staurolite" differentiate lower-grade from medium-grade pelites?</p>
        <p><strong>Solution:</strong>
          <strong>Chloritoid</strong> ($\text{(Fe,Mg)}_2\text{Al}_4\text{O}_2(\text{SiO}_4)_2(\text{OH})_4$) is a typomorphic index mineral of the <strong>upper greenschist to epidote-amphibolite facies ($T \approx 350\text{--}500^\circ\text{C}$)</strong>. At $T \approx 500\text{--}550^\circ\text{C}$, chloritoid breaks down via terminal dehydration: $\text{Chloritoid} + \text{Quartz} \rightarrow \text{Staurolite} + \text{Almandine Garnet} + \text{H}_2\text{O}$. Thus, chloritoid marks lower grades, and its replacement by staurolite marks the transition into the amphibolite facies.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>What is a "relict mineral" and why must petrographers distinguish relict minerals from true typomorphic index minerals?</p>
        <p><strong>Solution:</strong>
          A <strong>relict mineral</strong> (or porphyroclast) is a metastable mineral crystal inherited from an earlier, lower-grade metamorphic episode (or original igneous/sedimentary protolith) that failed to react during peak metamorphism due to sluggish reaction kinetics (e.g., detrital quartz cores, or relict kyanite armored inside garnet during retrograde sillimanite growth). If a relict mineral is mistaken for a coexisting typomorphic phase, it leads to erroneous overestimates of phase equilibrium variance and invalid $P\text{-}T$ calculations.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=113,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q113_Index_and_Typomorphic_Minerals_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q113: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q113()
