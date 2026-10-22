#!/usr/bin/env python3
"""
Q105 Generator: Folk (1959, 1962) Limestone Allochems & Intraclasts
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q105():
    title = r"Q105: Carbonate Petrology: Folk (1959, 1962) Limestone Classification & Allochems | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Carbonate Petrology & Petrography"
    h1_title = "Q105: Folk (1962) Limestone Petrography: The Four Allochems (Intraclasts, Oolites, Fossils, Pellets)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 105<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 6: Carbonate Rocks / Limestone Classification, pp. 180–195; Fig. 6.16); Robert L. Folk (1959, 1962), <em>Spectral Subdivision of Limestone Types</em> (AAPG Memoir 1, pp. 62–84); Maurice E. Tucker and V. Paul Wright, <em>Carbonate Sedimentology</em> (Blackwell Science); K.M. Bangar, <em>Principles of Engineering Geology</em> (pp. 75–78, 175)."""

    part1 = r"""
  <!-- CARD 1: FOLK'S DUAL PETROGRAPHIC FRAMEWORK FOR LIMESTONES -->
  <div class="card">
    <div class="card-header bg-blue">1. Folk's (1959, 1962) Petrographic Framework: Allochems vs. Orthochems</div>
    <div class="card-body">
      <p>
        In carbonate petrology, Robert L. Folk (1959, 1962) formulated a revolutionary, rigorous petrographic classification of limestones based on the conceptual analogy between carbonate rocks and siliciclastic sandstones.
      </p>
      <p>
        Folk recognized that limestones are composed of two fundamentally distinct categories of constituents:
      </p>
      <ol>
        <li><strong>Allochems (Framework Grains):</strong> Organized, discrete, particulate carbonate grains that originated by chemical or biochemical precipitation within the sedimentary basin and have undergone some degree of hydrodynamic movement or transport (analogous to the quartz, feldspar, and rock fragments in a sandstone).</li>
        <li><strong>Orthochems (Matrix & Cement):</strong> Normal chemical or biochemical precipitates formed directly in-situ within the interstitial void spaces without significant transport:
          <ul>
            <li><strong>Micrite (Microcrystalline Calcite Mud, $1\text{ to } 4\mu\text{m}$):</strong> Sub-microscopic, dull, semi-opaque lime mud acting as the depositional matrix (analogous to clay matrix in a wacke).</li>
            <li><strong>Sparite (Sparry Calcite Cement, $> 10\mu\text{m}$):</strong> Clear, crystalline, equant or fibrous calcite crystals precipitated from pore waters filling open intergranular pore spaces (analogous to silica or calcite cement in an arenite).</li>
          </ul>
        </li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q105/boggs_p186_folk_limestone_allochems_intraclasts.png" alt="Folk Limestone Allochems and Classification Scheme from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 105.1 — Folk's (1959, 1962) Classification of Limestones:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 186). Details the four fundamental allochems—Intraclasts, Ooids, Bioclasts (Fossils), and Peloids (Pellets)—combined with micrite and sparite to yield the canonical rock classes (Intrasparite, Oosparite, Biosparite, Pelmicrite, etc.).
        </div>
      </div>

      <h4>The Four Canonical Allochems Defined by Folk</h4>
      <p>
        Folk recognized precisely <strong>four distinct types of allochemical framework grains</strong>:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Allochem Type</th>
            <th>Prefix in Rock Name</th>
            <th>Size & Internal Microstructure</th>
            <th>Hydrodynamic & Depositional Genesis</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>(i) Intraclasts</strong></td>
            <td><strong>Intra-</strong> (e.g., <em>Intrasparite</em>)</td>
            <td>Sand to gravel size ($0.1\text{ to }> 10\text{ mm}$); irregular, angular to rounded fragments of older lime mud/sediment containing internal fossils, pellets, or laminations.</td>
            <td>Formed by the erosional tearing up and redeposition of penecontemporaneous, semi-consolidated carbonate mud from adjacent tidal flats, beach hardgrounds, or storm rip-up.</td>
          </tr>
          <tr>
            <td><strong>(ii) Oolites (Ooids)</strong></td>
            <td><strong>Oo-</strong> (e.g., <em>Oosparite</em>)</td>
            <td>Spherical to ellipsoidal grains ($< 2.0\text{ mm}$, typically $0.2\text{--}1.0\text{ mm}$) displaying concentric laminar cortex and/or radial fibrous calcite around a central nucleus (quartz grain or shell fragment).</td>
            <td>Precipitated by continuous rolling in warm, hypersaline, agitated shallow marine waters supersaturated with calcium carbonate (e.g., modern Bahamas banks).</td>
          </tr>
          <tr>
            <td><strong>(iii) Fossils (Bioclasts)</strong></td>
            <td><strong>Bio-</strong> (e.g., <em>Biosparite</em>)</td>
            <td>Variable size; whole or fragmented skeletal hard parts of marine organisms (foraminifera, brachiopods, mollusks, corals, echinoderms, algae).</td>
            <td>Direct biological metabolic secretion of calcite or aragonite hard parts in marine or lacustrine biofacies.</td>
          </tr>
          <tr>
            <td><strong>(iv) Pellets (Peloids)</strong></td>
            <td><strong>Pel-</strong> (e.g., <em>Pelmicrite</em>)</td>
            <td>Tiny ($0.03\text{ to } 0.15\text{ mm}$), uniform, structureless, ovoid to spherical microcrystalline calcite aggregates lacking internal concentric fabric.</td>
            <td>Primarily invertebrate <strong>fecal pellets</strong> excreted by benthic deposit-feeding organisms (gastropods, polychaetes, crustaceans) in quiet lagoonal mudflats.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: NOMENCLATURE & COMPARISON WITH DUNHAM -->
  <div class="card">
    <div class="card-header bg-emerald">2. Folk's Compound Nomenclature & Comparison with Dunham (1962)</div>
    <div class="card-body">
      <h4>Folk's Binary Petrographic Word Construction</h4>
      <p>
        Folk constructed limestone names systematically by combining the prefix for the dominant allochem with the root for the dominant orthochem:
      </p>
      <ul>
        <li><strong>Allochem Prefix + "sparite":</strong> Limestones formed in high-energy, wave-washed or current-swept environments where fine mud was winnowed away, leaving pores that were subsequently cemented by clear sparry calcite:
          <ul>
            <li><strong>Intrasparite:</strong> Intraclasts cemented by sparry calcite.</li>
            <li><strong>Oosparite:</strong> Oolites cemented by sparry calcite.</li>
            <li><strong>Biosparite:</strong> Skeletal fossil fragments cemented by sparry calcite.</li>
            <li><strong>Pelsparite:</strong> Pellets cemented by sparry calcite.</li>
          </ul>
        </li>
        <li><strong>Allochem Prefix + "micrite":</strong> Limestones formed in low-energy, quiet, sheltered environments (lagoons, protected bays, deep marine) where microcrystalline lime mud was trapped:
          <ul>
            <li><strong>Intramicrite, Oomicrite, Biomicrite, Pelmicrite.</strong></li>
          </ul>
        </li>
      </ul>

      <h4>Folk (1962) vs. Dunham (1962) Classification Paradigms</h4>
      <p>
        While Folk's system focuses on thin-section petrographic composition (allochems vs. orthochems), Robert J. Dunham's (1962) system focuses on <strong>depositional texture and framework-support mechanisms</strong>:
      </p>
      <ul>
        <li><strong>Mudstone:</strong> Mud-supported, contains $< 10\%$ grains.</li>
        <li><strong>Wackestone:</strong> Mud-supported, contains $> 10\%$ grains.</li>
        <li><strong>Packstone:</strong> Grain-supported, but contains interstitial mud matrix.</li>
        <li><strong>Grainstone:</strong> Grain-supported, completely devoid of mud matrix.</li>
        <li><strong>Boundstone:</strong> Original components bound organically in life (coral/stromatolite reefs).</li>
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
        <strong>Question 105:</strong> Folk (1962) described the classes of limestone in which framework grains are called allochems which include (i) _________, (ii) oolites, (iii) fossils and (iv) pellets.
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> intraclasts</div>
        <div class="option-item"><strong>(B)</strong> micrite</div>
        <div class="option-item"><strong>(C)</strong> sparry calcite</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) intraclasts</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Intraclasts</div>
        <p>
          <strong>Correct:</strong> In Robert L. Folk's (1959, 1962) classic classification of limestones, the four canonical types of <strong>allochems</strong> (framework grains) are explicitly: <strong>(1) intraclasts</strong>, <strong>(2) oolites (ooids)</strong>, <strong>(3) fossils (bioclasts)</strong>, and <strong>(4) pellets (peloids)</strong>. Intraclasts represent fragments of semi-consolidated carbonate mud ripped up from the sea floor and incorporated into younger strata. Thus, (A) is the exact missing term.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Micrite</div>
        <p>
          <strong>Incorrect:</strong> <strong>Micrite</strong> (microcrystalline calcite mud, crystal size $1\text{ to } 4\mu\text{m}$) is classified in Folk's scheme as an <strong>orthochem</strong>, specifically the fine depositional lime mud matrix. It is the fundamental <em>opposite</em> of an allochem; it forms by direct chemical/biochemical precipitation from quiet water, not as a transported framework grain.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Sparry Calcite</div>
        <p>
          <strong>Incorrect:</strong> <strong>Sparry calcite (sparite)</strong> is also an <strong>orthochem</strong>, representing the clear, crystalline calcite cement ($> 10\mu\text{m}$) precipitated diagenetically from supersaturated pore fluids into intergranular void spaces. It binds allochems together, but is never classified as an allochem itself.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because micrite and sparry calcite are orthochems (matrix and cement) and NOT allochems (framework grains), grouping them into allochems violates the core taxonomic foundation of carbonate petrology. The sole correct allochem among the choices is <strong>(A) intraclasts</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Structural Comparison: Folk's Limestone Components</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Component Category</th>
            <th>Folk (1962) Designation</th>
            <th>Specific Types</th>
            <th>Physical Nature & Petrographic Scale</th>
            <th>Genetic Function in Rock Architecture</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td rowspan="4"><strong>Allochems</strong></td>
            <td><strong>(i) Intraclasts</strong></td>
            <td>Rip-up clasts of semi-lithified lime mud ($0.1\text{ to }> 10\text{ mm}$)</td>
            <td>Penecontemporaneous basin floor reworkings</td>
            <td rowspan="4"><strong>Framework Grains</strong><br>(Provide structural framework; support hydrodynamic current sorting)</td>
          </tr>
          <tr>
            <td><strong>(ii) Oolites (Ooids)</strong></td>
            <td>Concentric spherical grains ($< 2.0\text{ mm}$)</td>
            <td>Agitated high-energy marine wave rollings</td>
          </tr>
          <tr>
            <td><strong>(iii) Fossils (Bioclasts)</strong></td>
            <td>Skeletal hard parts (shells, spines, plates)</td>
            <td>Biogenic secretion in varied ecosystems</td>
          </tr>
          <tr>
            <td><strong>(iv) Pellets (Peloids)</strong></td>
            <td>Structureless ovoid micro-aggregates ($30\text{--}150\mu\text{m}$)</td>
            <td>Invertebrate organism fecal excretions</td>
          </tr>
          <tr>
            <td rowspan="2"><strong>Orthochems</strong></td>
            <td><strong>Micrite</strong></td>
            <td>Microcrystalline calcite ($1\text{ to } 4\mu\text{m}$)</td>
            <td>Sub-microscopic murky lime mud</td>
            <td><strong>Depositional Matrix</strong> (fills interstitial spaces in low energy)</td>
          </tr>
          <tr>
            <td><strong>Sparite</strong></td>
            <td>Coarse crystalline calcite ($> 10\mu\text{m}$)</td>
            <td>Clear, interlocking equant spar crystals</td>
            <td><strong>Authigenic Cement</strong> (precipitated in open pores in high energy)</td>
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
        <p>A thin section of a limestone consists of $60\%$ spherical ooids exhibiting distinct concentric cortical laminations, $35\%$ clear equant crystalline sparry calcite cement filling intergranular voids, and $5\%$ lime mud. Name this rock using Folk's (1962) and Dunham's (1962) classifications.</p>
        <p><strong>Solution:</strong>
          - <strong>Folk (1962):</strong> The dominant allochem is oolites (prefix <em>Oo-</em>) and the dominant interstitial filling is sparry calcite cement (root <em>-sparite</em>). Because the rock contains $< 10\%$ micrite, it is classified as an <strong>Oosparite</strong>.
          - <strong>Dunham (1962):</strong> The rock is grain-supported (ooids in point contact) and contains virtually no interstitial mud ($< 5\%$, washed out by waves), classifying it as an <strong>Oolitic Grainstone</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain how "intraclasts" differ genetically from "extraclasts" in carbonate petrology.</p>
        <p><strong>Solution:</strong>
          - <strong>Intraclasts:</strong> Fragments of carbonate sediment that were deposited, semi-consolidated, and subsequently torn up from the seafloor, tidal flat, or hardground <em>within the same sedimentary basin</em> (penecontemporaneous) and redeposited into younger beds.
          - <strong>Extraclasts:</strong> Rock fragments derived from older, completely lithified rock formations located <em>outside the depositional basin</em> (e.g., eroded from an uplifted mountainous highland) and transported into the basin by rivers.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Under a petrographic microscope, how does a geologist distinguish between a "pellet" (peloid) and an "ooid" (oolite)?</p>
        <p><strong>Solution:</strong>
          - <strong>Ooid (Oolite):</strong> Possesses an organized, highly structured interior featuring a central nucleus (quartz grain or fossil speck) surrounded by <strong>concentric growth laminae (cortex)</strong> and/or radiating fibrous calcite crystals that produce a pseudo-uniaxial extinction cross under crossed polars.
          - <strong>Pellet (Peloid):</strong> Completely <strong>structureless and homogeneous</strong> throughout, consisting of a uniform, microcrystalline mosaic of dark micrite ($1\text{--}4\mu\text{m}$) without any concentric banding or radial fibrous structure.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What hydrodynamic energy regime is indicated by a "Biomicrite" compared to a "Biosparite" in Folk's environmental interpretation?</p>
        <p><strong>Solution:</strong>
          - <strong>Biosparite (High Energy):</strong> Indicates a high-energy depositional environment (e.g., wave-dominated shallow marine shoal or beach) where vigorous waves or tidal currents continuously washed and winnowed away all fine lime mud (micrite), allowing the open intergranular pore spaces to be filled post-depositionally by clean, clear sparry calcite cement.
          - <strong>Biomicrite (Low Energy):</strong> Indicates a low-energy, quiet, sheltered environment (e.g., deep quiet shelf, protected lagoon) where sluggish currents were unable to winnow fine suspension lime mud, allowing skeletal shells to settle directly into dense, murky micrite matrix.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>What is a "pisolite" (pisoid) and how is it distinguished quantitatively from an oolite (ooid)?</p>
        <p><strong>Solution:</strong>
          Both pisoids and ooids are spherical to ellipsoidal carbonate grains with concentric cortical laminations. The standard textbook distinction (Boggs, 2014, p. 183) is strictly <strong>grain diameter</strong>:
          - <strong>Ooid (Oolite):</strong> Diameter is <strong>$< 2.0\text{ mm}$</strong> (typically $0.2\text{ to } 1.0\text{ mm}$).
          - <strong>Pisoid (Pisolite):</strong> Diameter is <strong>$> 2.0\text{ mm}$</strong> (often $2\text{ to } 10\text{ mm}$ or larger), commonly formed in vadose caliche soils, hypersaline pans, or hot-spring caves (cave pearls).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>In Dunham's (1962) classification, define a "Boundstone" and explain why Folk gave such rocks the designation "Biolithite".</p>
        <p><strong>Solution:</strong>
          A <strong>Boundstone</strong> (Dunham, 1962) or <strong>Biolithite</strong> (Folk, 1959, 1962) is an autochthonous, in-situ organic reef limestone where the framework organisms (e.g., scleractinian corals, encrusting bryozoans, red coralline algae, stromatoporoids, stromatolites) grew in rigid mutual contact during life, erecting a self-supporting wave-resistant organic framework that passively trapped sediment rather than being deposited as mechanically transported particles.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "micritization" and what biological process drives this diagenetic alteration of allochems?</p>
        <p><strong>Solution:</strong>
          <strong>Micritization</strong> is the diagenetic process wherein the outer margin (or the entirety) of a skeletal bioclast or ooid is converted into sub-microscopic microcrystalline calcite mud (micrite), creating a dark, opaque <strong>micrite envelope</strong>. The process is driven by <strong>endolithic boring algae, fungi, and cyanobacteria</strong> that bore microscopic tunnels ($5\text{--}15\mu\text{m}$) into the carbonate grains. When the microbes die, their empty borings are backfilled by tiny precipitated micrite crystals.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Under Folk's textural maturity spectrum for limestones, arrange the following in order of increasing wave energy: Biosparite, Fossiliferous Micrite, Packed Biomicrite, Poorly Washed Biosparite.</p>
        <p><strong>Solution:</strong>
          In Folk's (1962) energy spectrum, the order of increasing wave energy and winnowing efficiency is:
          $$\text{Fossiliferous Micrite (lowest energy; mud dominant, } < 10\%\text{ shells)}$$
          $$\downarrow$$
          $$\text{Packed Biomicrite (moderate energy; shells touching, but mud completely fills pores)}$$
          $$\downarrow$$
          $$\text{Poorly Washed Biosparite (intermediate energy; incomplete mud winnowing, mix of spar and mud)}$$
          $$\downarrow$$
          $$\text{Biosparite (highest energy; complete mud removal, clean grain-supported spar cement)}$$
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=105,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q105_Folk_Limestone_Allochems_Intraclasts_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q105: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q105()
