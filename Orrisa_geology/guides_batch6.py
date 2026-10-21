# guides_batch6.py - Masterclasses for Questions 101 to 125
guides_batch6 = {
    101: {
        "title": "Q101: Folk & Ward (1957) Inclusive Graphic Kurtosis Formula",
        "part1": r"""
<h3>1. Question & Mathematical Formulation</h3>
<div class="question-box">
  <p><strong>Question 101:</strong> Formulae and verbal scales for graphic size parameters are provided by Folk and Ward (1957). As per the relation, inclusive graphic kurtosis is calculated by which formula ?</p>
  <ul>
    <li>(A) $K_G = (\phi_{95} - \phi_5) / [2.44 (\phi_{75} - \phi_{25})]$</li>
    <li>(B) $K_G = (\phi_{95} - \phi_5) / [2.44 (\phi_{75} - \phi_{95})]$</li>
    <li>(C) $K_G = (\phi_{95} - \phi_5) / [1.44 (\phi_5 - \phi_{25})]$</li>
    <li>(D) Both (A) and (B) are correct</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) $K_G = (\phi_{95} - \phi_5) / [2.44 (\phi_{75} - \phi_{25})]$</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Folk & Ward Graphic Size Parameters</h3>
<p>
Robert L. Folk and William C. Ward (1957) revolutionized statistical sedimentology by establishing graphical percentile equations to quantify the grain size frequency distribution of clastic sediments based on cumulative curves plotted in phi units ($\phi = -\log_2 d$):
</p>
<ul>
  <li><strong>Graphic Kurtosis ($K_G$):</strong> Kurtosis measures the ratio between the sorting in the "tails" of the distribution and the sorting in the "central portion". Folk & Ward defined <strong>Graphic Kurtosis ($K_G$)</strong> as:
    $$K_G = \frac{\phi_{95} - \phi_5}{2.44 (\phi_{75} - \phi_{25})}$$
    where:
    <ul>
      <li>$(\phi_{95} - \phi_5)$ represents the spread between the 5th and 95th percentiles (the tails).</li>
      <li>$(\phi_{75} - \phi_{25})$ represents the interquartile range (the central 50%).</li>
      <li>The factor $2.44$ normalizes a perfect Gaussian curve such that $K_G = 1.00$ (Mesokurtic).</li>
    </ul>
  </li>
  <li><strong>Kurtosis Verbal Classification Scale:</strong>
    <ul>
      <li>$K_G < 0.67$: Very Platykurtic (flat-peaked; bimodal tails)</li>
      <li>$0.67 - 0.90$: Platykurtic</li>
      <li>$0.90 - 1.11$: <strong>Mesokurtic</strong> (normal Gaussian distribution)</li>
      <li>$1.11 - 1.50$: Leptokurtic (excessively peaked)</li>
      <li>$1.50 - 3.00$: Very Leptokurtic</li>
      <li>$K_G > 3.00$: Extremely Leptokurtic</li>
    </ul>
  </li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A is correct:</strong> Exactly matches the standardized Folk and Ward (1957) equation: $K_G = \frac{\phi_{95} - \phi_5}{2.44 (\phi_{75} - \phi_{25})}$.</li>
  <li><strong>Option B:</strong> Denominator contains invalid percentile difference $(\phi_{75} - \phi_{95})$.</li>
  <li><strong>Option C:</strong> Erroneous normalization factor ($1.44$) and incorrect percentile subtraction $(\phi_5 - \phi_{25})$.</li>
  <li><strong>Option D:</strong> Distractor; only formula (A) is mathematically valid.</li>
</ul>
""",
    },
    102: {
        "title": "Q102: Sandstone Classification - Quartz Arenite, Arkose, and Litharenite",
        "part1": r"""
<h3>1. Question & Core Framework Identification</h3>
<div class="question-box">
  <p><strong>Question 102:</strong> Sandstone is categorized into three main types based on their variation in composition and cementing material, they include :<br>
  &bull; Quartz Sandstone<br>
  &bull; ____________<br>
  &bull; Litharenite or lithic sandstone</p>
  <ul>
    <li>(A) Arkose</li>
    <li>(B) Greywacke</li>
    <li>(C) Molasse</li>
    <li>(D) None of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) Arkose</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Q-F-L Sandstone Ternary</h3>
<p>
In the standard classification schemes of Pettijohn (1975) and Folk (1980), terrigenous sandstones with $<15\%$ matrix (arenites) are classified on a triangular diagram whose poles represent the three essential detrital framework components:
</p>
<table class="table">
  <thead>
    <tr>
      <th>Sandstone Family</th>
      <th>Framework Composition</th>
      <th>Tectonic & Climatic Significance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Quartz Sandstone (Quartz arenite)</strong></td>
      <td>$\ge 95\%$ Quartz</td>
      <td>Stable cratonic platform or passive margin; prolonged transport / multi-cycle recycling; supermature.</td>
    </tr>
    <tr>
      <td><strong>2. Arkose (Feldspathic arenite)</strong></td>
      <td><strong>$\ge 25\%$ Feldspar</strong> (K-feldspar &gt; Plagioclase)</td>
      <td>Rapid erosion of uplifted granitic basement / fault blocks in arid or high-relief tectonic settings (immature/submature).</td>
    </tr>
    <tr>
      <td><strong>3. Lithic Sandstone (Litharenite)</strong></td>
      <td>$\ge 25\%$ Unstable rock fragments (clasts)</td>
      <td>Orogenic foreland basins, trench wedges, or volcanic arcs; rapid deposition close to source.</td>
    </tr>
  </tbody>
</table>
<p>
<strong>Greywacke (Wacke):</strong> Defined by its high matrix content ($>15\%$ fine detrital silt/clay matrix), representing a separate textural class (wackes vs arenites).<br>
<strong>Molasse:</strong> A post-orogenic regional stratigraphic facies complex, not a petrographic compositional class.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (Arkose) is correct:</strong> The third cardinal member of the classic compositional arenite trinity (Quartz Arenite, Arkose, Litharenite).</li>
  <li><strong>Option B (Greywacke):</strong> Defined by abundant matrix ($>15\%$ matrix), not an arenite end-member.</li>
  <li><strong>Option C (Molasse):</strong> Stratigraphic basin facies term (foreland basin continental/shallow marine molasse).</li>
</ul>
""",
    },
    103: {
        "title": "Q103: Heavy Mineral Analysis and Sedimentary Provenance",
        "part1": r"""
<h3>1. Question & Analytical Objective</h3>
<div class="question-box">
  <p><strong>Question 103:</strong> The origin of many heavy mineral species is limited to rather specific rock types ; hence, heavies provide information concerning :</p>
  <ul>
    <li>(A) source rock</li>
    <li>(B) mineral dispersion pattern</li>
    <li>(C) quaternary sediments</li>
    <li>(D) provenance</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) provenance</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Heavy Minerals & Provenance Analysis</h3>
<p>
<strong>Heavy minerals</strong> are accessory detrital mineral grains possessing a specific gravity greater than standard bromoform / liquid separation media ($SG > 2.85\text{ g/cm}^3$):
</p>
<ul>
  <li><strong>Provenance Indicator:</strong> Provenance encompasses the complete history of a sedimentary rock, including the <strong>source rock lithology, tectonic setting, climate, and paleogeographic location</strong> of the parent landmass. Because specific heavy minerals originate in distinctive lithotectonic realms, they serve as the premier tool for provenance reconstruction:
    <ul>
      <li><em>Acid Plutonic (Granitic) Source:</em> Monazite, Euhedral Zircon, Tourmaline, Muscovite.</li>
      <li><em>Basic / Ultrabasic Igneous Source:</em> Chromite, Ilmenite, Enstatite, Augite, Olivine.</li>
      <li><em>Regional Metamorphic Source:</em> Kyanite, Sillimanite, Staurolite, Garnet, Glaucophane.</li>
      <li><em>Contact Metamorphic Source:</em> Andalusite, Cordierite, Epidote.</li>
    </ul>
  </li>
  <li><strong>Source Rock vs Provenance:</strong> While "source rock" (Option A) refers only to the parent lithology, <strong>provenance</strong> (Option D) is the comprehensive, universally accepted scientific term encompassing source terrain, tectonic setting, transport pathways, and weathering conditions.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D (provenance) is correct:</strong> The rigorous, overarching geological term for source area analysis using heavy mineral suites.</li>
  <li><strong>Option A (source rock):</strong> Incomplete subset of provenance; standard academic curricula (Boggs, Pettijohn) designate this study specifically as <em>provenance analysis</em>.</li>
  <li><strong>Option B & C:</strong> Narrow local applications, not the primary scientific objective of heavy mineral petrography.</li>
</ul>
""",
    },
    104: {
        "title": "Q104: Conglomerate Petrography - Rudaceous (Psephitic) Rocks",
        "part1": r"""
<h3>1. Question & Grain-Size Class</h3>
<div class="question-box">
  <p><strong>Question 104:</strong> Conglomerate belongs to which type of sedimentary rocks ?</p>
  <ul>
    <li>(A) Argillaceous</li>
    <li>(B) Arenaceous</li>
    <li>(C) Rudaceous</li>
    <li>(D) Both (B) and (C) are correct</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Rudaceous</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Clastic Grain Size Terminology</h3>
<p>
Clastic sedimentary rocks are classified based on the dominant diameter of their framework fragments according to the Wentworth size scale:
</p>
<table class="table">
  <thead>
    <tr>
      <th>Grain Size Class</th>
      <th>Clast Diameter ($d$)</th>
      <th>Latin / Greek Term</th>
      <th>Representative Rock Types</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Gravel / Boulder / Cobble / Pebble</strong></td>
      <td><strong>$> 2\text{ mm}$</strong></td>
      <td><strong>Rudaceous</strong> (Latin: <em>rudus</em>) / <strong>Psephitic</strong> (Greek: <em>psephos</em>)</td>
      <td><strong>Conglomerate</strong> (rounded clasts), <strong>Breccia</strong> (angular clasts), Tillite</td>
    </tr>
    <tr>
      <td><strong>Sand</strong></td>
      <td>$0.0625\text{ mm} - 2.0\text{ mm}$</td>
      <td><strong>Arenaceous</strong> (Latin: <em>arena</em>) / <strong>Psammitic</strong> (Greek: <em>psammos</em>)</td>
      <td>Sandstone, Quartz arenite, Arkose, Greywacke</td>
    </tr>
    <tr>
      <td><strong>Silt and Clay</strong></td>
      <td>$< 0.0625\text{ mm}$</td>
      <td><strong>Argillaceous</strong> (Latin: <em>argilla</em>) / <strong>Pelitic</strong> (Greek: <em>pelos</em>)</td>
      <td>Shale, Mudstone, Siltstone, Claystone</td>
    </tr>
  </tbody>
</table>
<p>
Because conglomerate is defined as a clastic rock composed predominantly of rounded gravel-sized fragments ($>2\text{ mm}$), it belongs unequivocally to the <strong>rudaceous</strong> class.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Rudaceous) is correct:</strong> Textual definition for gravel-sized rocks ($>2\text{ mm}$) including conglomerates.</li>
  <li><strong>Option A (Argillaceous):</strong> Silt/clay rocks ($<0.0625\text{ mm}$).</li>
  <li><strong>Option B (Arenaceous):</strong> Sand-sized rocks ($0.0625 - 2.0\text{ mm}$).</li>
  <li><strong>Option D:</strong> Conglomerate is strictly rudaceous, never arenaceous.</li>
</ul>
""",
    },
    105: {
        "title": "Q105: Folk (1962) Limestone Classification - Allochems and Intraclasts",
        "part1": r"""
<h3>1. Question & Framework Grain Identification</h3>
<div class="question-box">
  <p><strong>Question 105:</strong> Folk (1962) described the classes of limestone in which framework grains are called allochems which include (i) _________, (ii) oolites, (iii) fossils and (iv) pellets.</p>
  <ul>
    <li>(A) intraclasts</li>
    <li>(B) micrite</li>
    <li>(C) sparry calcite</li>
    <li>(D) All of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) intraclasts</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Folk's Carbonate Classification</h3>
<p>
Robert L. Folk (1959, 1962) classified limestones based on the volumetric proportions of three basic components: (1) <strong>Allochems</strong> (framework grains), (2) <strong>Micrite</strong> (microcrystalline carbonate mud matrix, $<4\,\mu\text{m}$), and (3) <strong>Sparite</strong> (sparry calcite pore-filling cement, $>10\,\mu\text{m}$).
</p>
<p>
Folk recognized exactly <strong>four types of allochems</strong>:
</p>
<ol>
  <li><strong>Intraclasts:</strong> Fragments of penecontemporaneous, semi-consolidated carbonate sediment torn up by wave or storm agitation from within the same depositional basin and redeposited (intrabasinal clasts).</li>
  <li><strong>Oolites (Ooids):</strong> Spherical, concentrically laminated grains formed by chemical or biological accretion of calcium carbonate around a nucleus in agitated shallow warm waters.</li>
  <li><strong>Fossils (Bioclasts):</strong> Whole or broken skeletal remains of calcareous organisms (shells, foraminifera, crinoids, algae).</li>
  <li><strong>Pellets (Peloids):</strong> Structureless, ovoid grains ($0.03 - 0.2\text{ mm}$) composed of microcrystalline calcite, commonly of fecal origin.</li>
</ol>
<p>
<em>Micrite</em> and <em>sparry calcite</em> are interstitial binding media (matrix and cement), NOT allochems!
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (intraclasts) is correct:</strong> The fourth cardinal allochem defined by Folk.</li>
  <li><strong>Option B (micrite):</strong> Microcrystalline matrix, strictly distinct from allochems.</li>
  <li><strong>Option C (sparry calcite):</strong> Secondary cement, not an allochem.</li>
  <li><strong>Option D (All of these):</strong> A fatal trap for candidates who confuse carbonate matrix/cement with framework grains.</li>
</ul>
""",
    },
    106: {
        "title": "Q106: Migmatite Genesis and High-Grade Metamorphic Anatexis",
        "part1": r"""
<h3>1. Question & Metamorphic Grade Boundary</h3>
<div class="question-box">
  <p><strong>Question 106:</strong> Migmatite consists of two or more constituents often layered repetitively forming a composite rock found in which metamorphic grade ?</p>
  <ul>
    <li>(A) Low to medium grade</li>
    <li>(B) Low grade</li>
    <li>(C) Medium and high-grade</li>
    <li>(D) High grade</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) High grade</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Migmatites and Anatexis</h3>
<p>
<strong>Migmatite</strong> (from Greek <em>migma</em> = mixture; Sederholm, 1907) is a composite mega-structured rock occurring in terranes of regional <strong>high-grade metamorphism</strong>, typically at the transition zone between high-grade metamorphic rocks and granite plutons:
</p>
<ul>
  <li><strong>Anatectic Melting:</strong> Migmatites form when crustal rocks (metapelites, quartzo-feldspathic gneisses) are subjected to ultra-high temperatures ($T > 650^\circ\text{C} - 800^\circ\text{C}$ at $P > 4 - 8\text{ kbar}$, upper amphibolite to granulite facies), reaching the water-saturated granite solidus curve. At this boundary, <strong>partial melting (anatexis)</strong> begins.</li>
  <li><strong>Two-Part Structural Anatomy:</strong>
    <ul>
      <li><strong>Leucosome:</strong> The light-colored, granitoid quartz-feldspar fraction crystallized from the partial melt.</li>
      <li><strong>Melanosome (Restite):</strong> The dark-colored, refractory residual layer enriched in mafic minerals (biotite, garnet, cordierite, sillimanite) left behind after melt extraction.</li>
      <li><strong>Mesosome (Paleosome):</strong> Remnant patches of un-melted parental metamorphic host rock.</li>
    </ul>
  </li>
  <li>Because partial melting of continental crust requires temperatures of upper amphibolite to granulite facies, migmatites are exclusively confined to <strong>high-grade</strong> metamorphic environments.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D (High grade) is correct:</strong> Anatexis and migmatization only occur at high metamorphic grades ($T > 650^\circ\text{C}$).</li>
  <li><strong>Option A & B (Low to medium grade):</strong> Low/medium grades (greenschist to lower amphibolite) cannot reach the temperatures required to melt quartz and feldspar in the presence of $H_2O$.</li>
  <li><strong>Option C:</strong> Medium-grade rocks (e.g., staurolite zone) remain entirely solid-state without leucosome melt segregations.</li>
</ul>
""",
    },
    107: {
        "title": "Q107: Protolith Identification - Shale as the Parental Rock of Slate",
        "part1": r"""
<h3>1. Question & Protolith Lineage</h3>
<div class="question-box">
  <p><strong>Question 107:</strong> Which will be the parental rock for Slate ?</p>
  <ul>
    <li>(A) Shale</li>
    <li>(B) Sandstone</li>
    <li>(C) Limestone</li>
    <li>(D) All of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) Shale</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Pelitic Metamorphic Progression</h3>
<p>
Metamorphic rocks are grouped by protolith (parent rock) composition. Pelitic rocks (mudrocks rich in aluminum and clay minerals) undergo a classic progressive sequence of regional metamorphism:
</p>
$$\text{Shale / Mudstone (Sedimentary Protolith)} \xrightarrow{\approx 200^\circ-300^\circ\text{C}} \textbf{Slate} \xrightarrow{300^\circ-400^\circ\text{C}} \text{Phyllite} \xrightarrow{400^\circ-550^\circ\text{C}} \text{Schist} \xrightarrow{>600^\circ\text{C}} \text{Gneiss}$$
<ul>
  <li><strong>Shale $\rightarrow$ Slate:</strong> Under incipient directed pressure and low temperature, clay minerals (illite, smectite) in shale recrystallize into microcrystalline white mica (muscovite/sericite) and chlorite oriented perpendicular to the maximum compressive stress direction, imparting excellent planar <em>slaty cleavage</em>.</li>
  <li><strong>Other Protoliths:</strong>
    <ul>
      <li><em>Sandstone</em> $\rightarrow$ Quartzite (non-foliated granoblastic texture).</li>
      <li><em>Limestone</em> $\rightarrow$ Marble (recrystallized calcite/dolomite).</li>
      <li><em>Basalt</em> $\rightarrow$ Greenschist $\rightarrow$ Amphibolite $\rightarrow$ Eclogite.</li>
    </ul>
  </li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (Shale) is correct:</strong> Slate is the low-grade metamorphic equivalent of fine-grained pelitic shale/mudstone.</li>
  <li><strong>Option B (Sandstone):</strong> Forms quartzite.</li>
  <li><strong>Option C (Limestone):</strong> Forms marble.</li>
</ul>
""",
    },
    108: {
        "title": "Q108: Foliation Development - Thermodynamic (Dynamothermal) Metamorphism",
        "part1": r"""
<h3>1. Question & Metamorphic Process</h3>
<div class="question-box">
  <p><strong>Question 108:</strong> Foliation in metamorphic rocks developed due to which metamorphic process ?</p>
  <ul>
    <li>(A) Thermal</li>
    <li>(B) Dynamic</li>
    <li>(C) Thermodynamic</li>
    <li>(D) All of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Thermodynamic</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Genesis of Metamorphic Foliation</h3>
<p>
<strong>Foliation</strong> is a pervasive, planar fabric in metamorphic rocks defined by the preferred parallel alignment of platy or elongate mineral grains (e.g., micas, chlorite, amphiboles) or by alternating compositional mineral banding:
</p>
<ul>
  <li><strong>Thermodynamic (Dynamothermal / Regional) Metamorphism:</strong> True penetrative metamorphic foliation requires the coupled action of:
    <ol>
      <li><strong>Thermal energy ($T$):</strong> Drives chemical reaction, solid-state diffusion, and crystal growth of metamorphic phyllosilicates.</li>
      <li><strong>Directed differential stress / Dynamic pressure ($\sigma_1 > \sigma_2 > \sigma_3$):</strong> Controls the geometric orientation of newly growing crystal lattices (perpendicular to $\sigma_1$) and drives ductile shearing, mechanical rotation, and pressure-solution cleavage.</li>
    </ol>
    Because both thermal and dynamic agents operate simultaneously, this is termed <strong>thermodynamic</strong> (or dynamo-thermal) metamorphism.
  </li>
  <li><strong>Pure Thermal Metamorphism:</strong> In contact aureoles around intrusions, heating occurs under quasi-hydrostatic (non-directed) stress; rocks develop unfoliated granoblastic hornfelsic textures.</li>
  <li><strong>Pure Dynamic Metamorphism:</strong> Occurs in narrow brittle fault zones at shallow depths (cataclasites, fault breccias) with minimal thermal recrystallization.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Thermodynamic) is correct:</strong> The combined thermal recrystallization and directed stress regime that produces pervasive schistosities and gneissose foliations.</li>
  <li><strong>Option A (Thermal):</strong> Generates non-foliated hornfels.</li>
  <li><strong>Option B (Dynamic):</strong> Tends toward brittle pulverization / cataclasis without sustained metamorphic crystal growth unless elevated temperatures are coupled.</li>
</ul>
""",
    },
    109: {
        "title": "Q109: Barrovian Metamorphic Grades - Garnet-Schist as the Highest Grade",
        "part1": r"""
<h3>1. Question & Metamorphic Zonation</h3>
<div class="question-box">
  <p><strong>Question 109:</strong> Amongst the following which is the highest grade of metamorphic rock ?</p>
  <ul>
    <li>(A) Talc-schist</li>
    <li>(B) Garnet-schist</li>
    <li>(C) Mica-schist</li>
    <li>(D) Chlorite-schist</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(B) Garnet-schist</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Barrovian Zonal Sequence</h3>
<p>
George Barrow (1893, 1912) established the classic sequence of metamorphic index minerals in pelitic rocks of the Scottish Highlands under intermediate-pressure regional metamorphism:
</p>
<table class="table">
  <thead>
    <tr>
      <th>Barrovian Zone</th>
      <th>Diagnostic Metamorphic Mineral</th>
      <th>Metamorphic Grade & Facies</th>
      <th>Approximate Temperature ($T$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Chlorite Zone</strong></td>
      <td>Chlorite + Muscovite + Albite</td>
      <td>Low Grade (Greenschist facies)</td>
      <td>$300^\circ - 350^\circ\text{C}$</td>
    </tr>
    <tr>
      <td><strong>2. Biotite Zone</strong></td>
      <td>Biotite + Chlorite + Muscovite</td>
      <td>Low Grade (Greenschist facies)</td>
      <td>$350^\circ - 450^\circ\text{C}$</td>
    </tr>
    <tr>
      <td><strong>3. Garnet Zone</strong></td>
      <td><strong>Almandine Garnet</strong> + Biotite + Muscovite</td>
      <td><strong>Medium-to-High Grade (Amphibolite facies)</strong></td>
      <td><strong>$450^\circ - 550^\circ\text{C}$</strong></td>
    </tr>
    <tr>
      <td><strong>4. Staurolite Zone</strong></td>
      <td>Staurolite + Garnet + Biotite</td>
      <td>Medium Grade (Amphibolite facies)</td>
      <td>$550^\circ - 600^\circ\text{C}$</td>
    </tr>
    <tr>
      <td><strong>5. Kyanite Zone</strong></td>
      <td>Kyanite + Garnet + Biotite</td>
      <td>High Grade (Amphibolite facies)</td>
      <td>$600^\circ - 650^\circ\text{C}$</td>
    </tr>
    <tr>
      <td><strong>6. Sillimanite Zone</strong></td>
      <td>Sillimanite + K-feldspar / Quartz</td>
      <td>High Grade (Upper Amphibolite / Granulite)</td>
      <td>$> 650^\circ\text{C}$</td>
    </tr>
  </tbody>
</table>
<p>
Talc-schist is a hydrated ultrabasic metamorphic rock of the greenschist facies ($300-400^\circ\text{C}$). Chlorite-schist marks the lowest greenschist grade ($300^\circ\text{C}$). General mica-schist spans greenschist to lower amphibolite. Therefore, <strong>Garnet-schist</strong> represents the highest metamorphic grade among the listed choices.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option B (Garnet-schist) is correct:</strong> The appearance of almandine garnet marks the transition into the amphibolite facies ($T \approx 450-550^\circ\text{C}$), the highest grade in the list.</li>
  <li><strong>Option D (Chlorite-schist):</strong> Low-grade greenschist facies ($300^\circ\text{C}$).</li>
  <li><strong>Option A (Talc-schist):</strong> Low-grade greenschist alteration of ultramafic protoliths.</li>
  <li><strong>Option C (Mica-schist):</strong> Broad category; when unqualified, it precedes or encompasses the biotite zone prior to garnet entry.</li>
</ul>
""",
    },
    110: {
        "title": "Q110: Greenschist Metamorphic Conditions - Low Temperature and Regional Stress",
        "part1": r"""
<h3>1. Question & Metamorphic P-T Setting</h3>
<div class="question-box">
  <p><strong>Question 110:</strong> Low grade schist is formed under which metamorphic conditions ?</p>
  <ul>
    <li>(A) High temperature and local metamorphism</li>
    <li>(B) Low temperature and regional metamorphism</li>
    <li>(C) Low temperature and local metamorphism</li>
    <li>(D) All of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(B) Low temperature and regional metamorphism</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Greenschist Facies and Regional Metamorphism</h3>
<p>
Schists are characterized by <strong>schistosity</strong>—a planar tectonic fabric formed by the parallel alignment of visible, coarse phyllosilicates.
</p>
<ul>
  <li><strong>Regional Scale Requirement:</strong> Schistosity cannot form under purely "local" contact metamorphism because localized thermal aureoles lack the regional differential stress field necessary to rotate and align platy minerals across vast crustal tracts. Schists are diagnostic products of <strong>regional (orogenic) metamorphism</strong>.</li>
  <li><strong>Low-Grade P-T Range:</strong> "Low grade schist" corresponds to the <strong>greenschist facies</strong>:
    <ul>
      <li>Temperature: $300^\circ\text{C} - 450^\circ\text{C}$ (Low temperature).</li>
      <li>Pressure: $2 - 6\text{ kbar}$ (moderate crustal depths of $6 - 20\text{ km}$).</li>
      <li>Key Minerals: Chlorite, albite, actinolite, epidote, muscovite, quartz.</li>
    </ul>
  </li>
  <li>Hence, low grade schist is formed under <strong>low temperature and regional metamorphism</strong>.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option B is correct:</strong> Accurately pairs low metamorphic temperatures ($300-450^\circ\text{C}$) with large-scale regional metamorphism.</li>
  <li><strong>Option A & C (Local metamorphism):</strong> Local metamorphism (e.g., thermal contact aureoles) produces unfoliated hornfels, not regional schists.</li>
</ul>
""",
    },
    111: {
        "title": "Q111: The Metamorphic Triad - Contact, Regional, and Dynamic Metamorphism",
        "part1": r"""
<h3>1. Question & Metamorphic Types</h3>
<div class="question-box">
  <p><strong>Question 111:</strong> Three types of metamorphism are recognized e.g., Contact, ________ and Dynamic metamorphism. (Identify the missing type.)</p>
  <ul>
    <li>(A) Thermal</li>
    <li>(B) Static</li>
    <li>(C) Local</li>
    <li>(D) Regional</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) Regional</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Classical Triad of Metamorphism</h3>
<p>
In classical petrology (Barrow, Harker, Eskola, Turner, Bangar), metamorphism is divided into three primary genetic classes based on geological setting and dominant driving agents:
</p>
<table class="table">
  <thead>
    <tr>
      <th>Metamorphic Type</th>
      <th>Primary Driving Agent</th>
      <th>Geological Setting & Typical Scale</th>
      <th>Characteristic Rocks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>1. Contact Metamorphism</strong></td>
      <td><strong>Temperature ($T$)</strong> (Magmatic heat)</td>
      <td>Local aureoles surrounding cooling igneous plutons ($<1\text{--}2\text{ km}$)</td>
      <td>Hornfels, Skarn, Marble, Quartzite</td>
    </tr>
    <tr>
      <td><strong>2. Regional Metamorphism</strong></td>
      <td><strong>Directed Stress ($\sigma$) + Temperature ($T$)</strong></td>
      <td>Convergent plate boundaries and collisional orogens ($100\text{--}1000\text{ km}$)</td>
      <td>Slate, Phyllite, Schist, Gneiss, Amphibolite</td>
    </tr>
    <tr>
      <td><strong>3. Dynamic (Cataclastic) Metamorphism</strong></td>
      <td><strong>Differential Stress / Strain ($	au$)</strong></td>
      <td>Fault zones and narrow ductile shear zones</td>
      <td>Fault breccia, Cataclasite, Mylonite</td>
    </tr>
  </tbody>
</table>
<p>
Because "Thermal" is synonymous with Contact metamorphism and "Local" is a scale descriptor, <strong>Regional metamorphism</strong> is the universally accepted missing member of the triad.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D (Regional) is correct:</strong> The universal third pillar alongside Contact and Dynamic metamorphism.</li>
  <li><strong>Option A (Thermal):</strong> Redundant with Contact metamorphism.</li>
  <li><strong>Option B (Static):</strong> Burial / load metamorphism, a secondary subclass.</li>
  <li><strong>Option C (Local):</strong> Spatial descriptor, not a formal process class.</li>
</ul>
""",
    },
    112: {
        "title": "Q112: Metamorphic Reactions - The GASP Net-Transfer Barometer",
        "part1": r"""
<h3>1. Question & Reaction Stoichiometry</h3>
<div class="question-box">
  <p><strong>Question 112:</strong> Net-transfer reactions during metamorphic process involve chemical components being &ldquo;transferred&rdquo; from one phase or set of phases to new phases produced as old ones disappear. Find out the true example of such reaction from the following :</p>
  <ul>
    <li>(A) Anorthite = grossular + kyanite + quartz</li>
    <li>(B) Muscovite + quartz = K-feldspar + sillimanite + kyanite</li>
    <li>(C) Biotite + quartz = orthoclase + hematite + magnetite</li>
    <li>(D) None of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) Anorthite = grossular + kyanite + quartz</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Net-Transfer Reactions and the GASP Barometer</h3>
<p>
Metamorphic reactions are categorized into continuous solid-solution exchange reactions and discontinuous <strong>net-transfer reactions</strong>. In net-transfer reactions, modal proportions of reactant phases decrease to zero as entirely new product phases nucleate and grow through mass transfer across phase boundaries:
</p>
<ul>
  <li><strong>The GASP Barometer Reaction:</strong>
    $$3\,\text{CaAl}_2\text{Si}_2\text{O}_8\text{ (Anorthite in plagioclase)} \rightleftharpoons \text{Ca}_3\text{Al}_2\text{Si}_3\text{O}_{12}\text{ (Grossular in garnet)} + 2\,\text{Al}_2\text{SiO}_5\text{ (Kyanite)} + \text{SiO}_2\text{ (Quartz)}$$
    <ul>
      <li>This is the celebrated <strong>GASP (Garnet - Aluminosilicate - Silica - Plagioclase)</strong> reaction, the premier geobarometer for metapelites.</li>
      <li>Because grossular garnet and kyanite are much denser than calcic plagioclase, the reaction involves a large negative volume change ($\Delta V_r < 0$). Consequently, the equilibrium boundary has a very gentle $dP/dT$ slope, making it extraordinarily sensitive to pressure.</li>
    </ul>
  </li>
  <li><strong>Why Options B and C are Stoichiometrically False:</strong>
    <ul>
      <li><em>Option B:</em> The second-sillimanite breakdown is $\text{Muscovite} + \text{Quartz} = \text{K-feldspar} + \text{Al}_2\text{SiO}_5 + \text{H}_2\text{O}$. Having both sillimanite AND kyanite simultaneously as reaction products with no $H_2O$ is chemically and phase-rule invalid.</li>
      <li><em>Option C:</em> Biotite breakdown requires oxygen and water balancing and yields pyroxenes/garnet + orthoclase, not simultaneous hematite and magnetite without stoichiometry.</li>
    </ul>
  </li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A is correct:</strong> The classic, stoichiometrically balanced GASP net-transfer reaction: $3\,\text{Anorthite} = \text{Grossular} + 2\,\text{Kyanite} + \text{Quartz}$.</li>
  <li><strong>Option B:</strong> Erroneously includes two polymorphs on product side and omits liberated water.</li>
  <li><strong>Option C:</strong> Chemically unbalanced fiction.</li>
</ul>
""",
    },
    113: {
        "title": "Q113: Metamorphic Indicators - Index Minerals and Typomorphic Minerals",
        "part1": r"""
<h3>1. Question & Mineralogical Terminology</h3>
<div class="question-box">
  <p><strong>Question 113:</strong> Minerals that are characteristic for a certain metamorphic grade are called :</p>
  <ul>
    <li>(A) Typomorphic minerals</li>
    <li>(B) Barrovian minerals</li>
    <li>(C) Index minerals</li>
    <li>(D) Both (A) and (C) are correct</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) Both (A) and (C) are correct</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Index Minerals vs Typomorphic Minerals</h3>
<p>
In metamorphic petrology, minerals whose presence is diagnostic of a specific, narrow range of temperature and pressure conditions are designated by two formal terms:
</p>
<ul>
  <li><strong>Index Minerals:</strong> First introduced by George Barrow (1912), an <em>index mineral</em> marks the first appearance of a new mineral phase (isograd) in pelitic rocks as metamorphic grade increases (e.g., chlorite, biotite, garnet, staurolite, kyanite, sillimanite).</li>
  <li><strong>Typomorphic Minerals:</strong> Introduced by Friedrich Becke and formalized by Paul Niggli and V.M. Goldschmidt, <em>typomorphic minerals</em> are minerals that are chemically stable only within a restricted range of physical conditions (specific metamorphic facies or temperature-pressure sub-zones) and therefore serve as diagnostic "type" minerals of that metamorphic regime (e.g., glaucophane for blueschist facies; staurolite for medium-pressure amphibolite facies).</li>
  <li>Because both terms ("Typomorphic minerals" and "Index minerals") denote minerals characteristic of a specific metamorphic grade, option (D) is the strictly accurate answer.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D (Both A and C are correct) is correct:</strong> Typomorphic minerals (Becke/Eskola) and Index minerals (Barrow/Tilley) are standard accepted terms for metamorphic grade indicators.</li>
  <li><strong>Option B (Barrovian minerals):</strong> Refers specifically to the intermediate P/T sequence of the Scottish Dalradian, not the generic petrological classification term.</li>
</ul>
""",
    },
    114: {
        "title": "Q114: Thermodynamic Controls on Metamorphic Processes",
        "part1": r"""
<h3>1. Question & Factor Analysis</h3>
<div class="question-box">
  <p><strong>Question 114:</strong> The main factors that control metamorphic processes are :<br>
  (i) The mineral composition of the parent rock<br>
  (ii) The pressure and temperature at which metamorphism takes place<br>
  (iii) The types of prevailing fluids (mostly water) during metamorphism<br>
  (iv) The amount of time available for metamorphism<br>
  Find out the odd one from the listed factors :</p>
  <ul>
    <li>(A) (i) and (ii) are correct</li>
    <li>(B) (i), (ii) and (iii) are correct</li>
    <li>(C) (ii), (iii) and (iv) are correct</li>
    <li>(D) All of the above are true explanations</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) All of the above are true explanations</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Four Fundamental Controls on Metamorphism</h3>
<p>
Metamorphism represents solid-state mineralogical and textural re-equilibration in response to changes in environmental conditions. All petrological textbooks (Winter, Turner & Verhoogen, Yardley, Bangar) establish four interdependent parameters that dictate metamorphic processes:
</p>
<ol>
  <li><strong>Protolith Chemistry (Parent Rock Composition):</strong> Metamorphism is predominantly isochemical (excluding volatile loss). The chemical bulk composition of the protolith strictly limits what minerals can nucleate (e.g., pelite yields aluminosilicates; limestone yields calc-silicates; basalt yields amphiboles).</li>
  <li><strong>Pressure ($P$) and Temperature ($T$):</strong> Temperature drives dehydration/decarbonation reactions and solid-state diffusion; lithostatic pressure promotes dense phases, while differential stress imparts foliation and lineation.</li>
  <li><strong>Fluid Activity ($a_{\text{H}_2\text{O}}, a_{\text{CO}_2}$):</strong> Intergranular pore fluids catalyze ion diffusion, facilitate dissolution-precipitation creep, and control dehydration equilibrium temperatures.</li>
  <li><strong>Reaction Time (Kinetics / Duration):</strong> Metamorphic reactions require geological time ($10^5 - 10^7\text{ years}$) for sluggish solid-state diffusion and crystal growth to achieve thermodynamic equilibrium.</li>
</ol>
<p>
Since all four parameters are valid, recognized primary controls on metamorphism, statement (D) ("All of the above are true explanations") is the correct option.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D is correct:</strong> All four parameters (protolith, P-T, fluids, and time) are universally recognized controls in metamorphic thermodynamics and kinetics.</li>
  <li><strong>Options A, B, and C:</strong> Incomplete subsets that exclude one or more vital parameters.</li>
</ul>
""",
    },
    115: {
        "title": "Q115: Blueschist Facies Metamorphism - Subduction along Continental Margins",
        "part1": r"""
<h3>1. Question & Geodynamic Setting</h3>
<div class="question-box">
  <p><strong>Question 115:</strong> The characteristic locale for blueschist type of metamorphism appears to be along a ________ being underthrust by an oceanic plate.</p>
  <ul>
    <li>(A) mid-oceanic ridge</li>
    <li>(B) continental margin</li>
    <li>(C) transform boundary</li>
    <li>(D) Both (A) and (C) are correct</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(B) continental margin</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: High-Pressure / Low-Temperature (HP-LT) Blueschist Facies</h3>
<p>
<strong>Blueschist facies</strong> metamorphism is characterized by the sodic amphibole <strong>glaucophane</strong> (which imparts a distinctive lavender-blue color), accompanied by lawsonite, jadeitic pyroxene, and aragonite:
</p>
<ul>
  <li><strong>The Subduction Refrigeration Mechanism:</strong> Blueschist metamorphism requires an anomalous geotherm characterized by <strong>high pressure ($P > 6 - 12\text{ kbar}$, depths $>20 - 40\text{ km}$) but low temperature ($T = 200^\circ - 400^\circ\text{C}$)</strong>:
    <ul>
      <li>In a subduction zone, cold, dense oceanic lithosphere is underthrust rapidly beneath a <strong>continental margin</strong> or island arc.</li>
      <li>The subducting slab descends into the mantle faster than conductive heat can warm it from the surrounding mantle wedge ("refrigeration effect").</li>
      <li>Consequently, rocks reach enormous pressures while remaining unusually cold, forming the diagnostic blueschist and eclogite suites.</li>
    </ul>
  </li>
  <li><strong>Mid-Ocean Ridges:</strong> Exhibit extremely high heat flow ($>100^\circ\text{C/km}$), generating low-pressure hydrothermal ocean-floor metamorphism (zeolite to greenschist/amphibolite facies), the exact opposite of blueschist conditions.</li>
  <li><strong>Transform Boundaries:</strong> Sites of shallow strike-slip faulting and localized cataclasis without deep subduction underthrusting.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option B (continental margin) is correct:</strong> The classic subduction trench along an active continental margin (e.g., Franciscan Complex of California) where oceanic crust is underthrust beneath continental crust.</li>
  <li><strong>Option A (mid-oceanic ridge):</strong> Low-pressure, high-temperature hydrothermal metamorphism.</li>
  <li><strong>Option C (transform boundary):</strong> Strike-slip shearing without subduction underthrusting.</li>
</ul>
""",
    },
    116: {
        "title": "Q116: Granulite Facies Petrography - Charnockite and Orthopyroxene",
        "part1": r"""
<h3>1. Question & Granulite Rock Classification</h3>
<div class="question-box">
  <p><strong>Question 116:</strong> Granulite facies quartzo-feldspathic plutonic rocks characterized by the presence of hypersthenes often designated as :</p>
  <ul>
    <li>(A) Charnockite</li>
    <li>(B) Orthoamphibolite</li>
    <li>(C) Paramphibolite</li>
    <li>(D) Greenalite</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) Charnockite</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Charnockite Suite</h3>
<p>
<strong>Charnockite</strong> was named by Sir Thomas Holland (1900) after Job Charnock, founder of Kolkata, whose tombstone was carved from this rock near St. Thomas Mount, Chennai:
</p>
<ul>
  <li><strong>Petrological Definition:</strong> A quartzo-feldspathic granulite facies rock characterized essentially by the presence of <strong>orthopyroxene (hypersthene)</strong> alongside quartz, alkali feldspar (microperthite), and plagioclase. It typically displays a dark, greasy, brownish-green or bluish appearance in hand specimen due to micro-inclusions in feldspar.</li>
  <li><strong>Granulite Facies Conditions:</strong> Forms under deep crustal anhydrous conditions ($T > 750^\circ - 900^\circ\text{C}$, $P > 6 - 10\text{ kbar}$, low $a_{\text{H}_2\text{O}}$ buffered by $CO_2$-rich fluid infiltration or melt extraction), causing the breakdown of hydrous biotite and amphibole into orthopyroxene:
    $$\text{Biotite} + 3\,\text{Quartz} \rightleftharpoons 3\,\text{Hypersthene} + \text{K-feldspar} + \text{H}_2\text{O}$$
  </li>
  <li><strong>Amphibolites vs Charnockite:</strong> Amphibolites (ortho- or para-) are dominated by hornblende and plagioclase in the medium-grade amphibolite facies. Greenalite is a hydrated serpentine-group iron silicate mineral found in banded iron formations, not a granulite rock.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (Charnockite) is correct:</strong> The definitive name for hypersthene-bearing quartzo-feldspathic granulites.</li>
  <li><strong>Option B & C (Ortho/Paramphibolite):</strong> Hydrous amphibole-plagioclase rocks of the amphibolite facies.</li>
  <li><strong>Option D (Greenalite):</strong> Iron-rich serpentine-group mineral ($Fe_3Si_2O_5(OH)_4$) in sedimentary BIFs.</li>
</ul>
""",
    },
    117: {
        "title": "Q117: Metamorphic Structures - Augen Gneiss and Eye-Shaped Porphyroclasts",
        "part1": r"""
<h3>1. Question & Microstructural Definition</h3>
<div class="question-box">
  <p><strong>Question 117:</strong> A metamorphic structure consisting of minerals like feldspar, quartz, or garnet that have been squeezed into elliptical or lens-shaped forms resembling eyes, called :</p>
  <ul>
    <li>(A) Orthogneiss</li>
    <li>(B) Paragneiss</li>
    <li>(C) Augen gneiss</li>
    <li>(D) Biotite gneiss</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Augen gneiss</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Augen Structure (Eye-Shaped Porphyroclasts)</h3>
<p>
<strong>Augen gneiss</strong> (from the German word <em>Augen</em>, meaning "eyes") is a coarsely foliated metamorphic rock characterized by prominent, lens-shaped or elliptical megacrysts (termed <strong>augen</strong> or porphyroclasts), typically of potash feldspar, plagioclase, quartz, or garnet:
</p>
<ul>
  <li><strong>Kinematic Formation Mechanism:</strong> During intense ductile shear and regional thermodynamic metamorphism, large pre-existing crystals (phenocrysts in an igneous protolith or porphyroblasts in a metamorphic rock) resist ductile deformation better than the surrounding finer-grained groundmass.</li>
  <li><strong>Asymmetric Strain Shadows:</strong> The micaceous and quartzose matrix flows plastically around these rigid feldspar knots, wrapping around their rounded margins and tapering into recrystallized tails (strain shadows or wings). This imparts the classic lenticular "eye" appearance.</li>
  <li><strong>Orthogneiss vs Paragneiss:</strong> Refer to genetic protoliths (orthogneiss = igneous parent; paragneiss = sedimentary parent), regardless of whether they display auge fabric. Augen gneiss is the specific descriptive term for this structural geometry.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Augen gneiss) is correct:</strong> German <em>Augen</em> specifically denotes eye-shaped lens structures in gneiss.</li>
  <li><strong>Option A (Orthogneiss):</strong> Gneiss derived from an igneous protolith (granite).</li>
  <li><strong>Option B (Paragneiss):</strong> Gneiss derived from a sedimentary protolith.</li>
  <li><strong>Option D (Biotite gneiss):</strong> Mineralogical variety of gneiss lacking the diagnostic lenticular eye-shaped porphyroclasts.</li>
</ul>
""",
    },
    118: {
        "title": "Q118: Hydrothermal Metamorphism and Metasomatism",
        "part1": r"""
<h3>1. Question & Synonymous Nomenclature</h3>
<div class="question-box">
  <p><strong>Question 118:</strong> The other name of hydrothermal metamorphism in geological literature is :</p>
  <ul>
    <li>(A) Autochemical metamorphism</li>
    <li>(B) Allochemical metamorphism</li>
    <li>(C) Metasomatism</li>
    <li>(D) All of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Metasomatism</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Hydrothermal Metamorphism and Metasomatism</h3>
<p>
Metamorphism that is mediated and driven by the pervasive percolation of hot aqueous fluids ($H_2O$-rich solutions carrying dissolved ionic species) is termed <strong>hydrothermal metamorphism</strong>:
</p>
<ul>
  <li><strong>Metasomatism:</strong> In standard geological literature (Lindgren, Eskola, Turner, Winter), hydrothermal metamorphism is universally equated with <strong>metasomatism</strong> (from Greek <em>meta</em> = change, <em>soma</em> = body). Metasomatism is defined as a solid-state process where the bulk chemical composition of a rock is substantially altered by the introduction and removal of non-volatile chemical components via hydrothermal fluids.</li>
  <li><strong>Allochemical vs Autochemical:</strong>
    <ul>
      <li><em>Allochemical Metamorphism:</em> Metamorphism where bulk chemical composition changes (a broad descriptive category encompassing metasomatism).</li>
      <li><em>Autochemical (Isochemical) Metamorphism:</em> Standard metamorphism where bulk composition remains constant except for the loss of $H_2O$ and $CO_2$.</li>
    </ul>
  </li>
  <li>In standard geological textbooks (e.g., Bangar, Mahapatra), "Metasomatism" is universally cited as the direct synonym for hydrothermal metamorphism.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Metasomatism) is correct:</strong> The classical, universally accepted geological equivalent of hydrothermal metamorphism.</li>
  <li><strong>Option A (Autochemical):</strong> Strictly preserves chemical composition, the opposite of hydrothermal alteration.</li>
  <li><strong>Option D (All of these):</strong> Incorrect because autochemical directly contradicts hydrothermal metasomatism.</li>
</ul>
""",
    },
    119: {
        "title": "Q119: Contact Metamorphism - Temperature Regimes of Hornfels",
        "part1": r"""
<h3>1. Question & Thermal Boundary Conditions</h3>
<div class="question-box">
  <p><strong>Question 119:</strong> Common temperatures for the formation of hornfels range from about :</p>
  <ul>
    <li>(A) 700&deg; to 800&deg;C</li>
    <li>(B) &gt; 1000&deg;C</li>
    <li>(C) 1000-1200&deg;C</li>
    <li>(D) None of these</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) 700&deg; to 800&deg;C</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Thermal Aureoles and Hornfels Facies</h3>
<p>
<strong>Hornfels</strong> is a fine-grained, tough, unfoliated contact metamorphic rock composed of a mosaic of equidimensional grains (granoblastic/hornfelsic texture), formed in the thermal aureole surrounding hot plutonic igneous intrusions:
</p>
<ul>
  <li><strong>Contact Facies Temperatures:</strong>
    <ul>
      <li><em>Albite-Epidote Hornfels Facies:</em> Outer aureole, $T \approx 300^\circ - 500^\circ\text{C}$.</li>
      <li><em>Hornblende Hornfels Facies:</em> Intermediate aureole, $T \approx 500^\circ - 650^\circ\text{C}$.</li>
      <li><em>Pyroxene Hornfels Facies:</em> Inner aureole immediately adjacent to basic or intermediate intrusions, <strong>$T \approx 650^\circ - 800^\circ\text{C}$</strong> (the peak common temperature for hornfels formation).</li>
      <li><em>Sanidinite Facies:</em> Rare, extreme contact conditions ($T > 800^\circ - 1000^\circ\text{C}$) occurring only in narrow xenoliths or contacts with high-temperature mafic/ultramafic lavas.</li>
    </ul>
  </li>
  <li>Among the provided exam options, <strong>$700^\circ\text{ to }800^\circ\text{C}$</strong> accurately captures the upper temperature range of inner hornfels aureoles. Temperatures exceeding $1000^\circ\text{C}$ represent ultra-high temperature volcanic xenolith melting (sanidinite), far exceeding common hornfels aureoles.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (700&deg; to 800&deg;C) is correct:</strong> Matches peak contact metamorphic temperatures for pyroxene hornfels in plutonic aureoles.</li>
  <li><strong>Option B & C (>1000&deg;C):</strong> Far too hot for common hornfels; at $1000^\circ-1200^\circ\text{C}$, typical crustal rocks undergo total melting (anatexis) or represent volcanic basalt magmatic temperatures.</li>
</ul>
""",
    },
    120: {
        "title": "Q120: Contact Metasomatism - Skarn Formation in Carbonate Bedrock",
        "part1": r"""
<h3>1. Question & Calc-Silicate Metasomatic Rocks</h3>
<div class="question-box">
  <p><strong>Question 120:</strong> Metamorphic zone developed in the contact area around igneous rock intrusions when carbonate sedimentary rocks are invaded called :</p>
  <ul>
    <li>(A) Carbonatites</li>
    <li>(B) Metamorphites</li>
    <li>(C) Skarn</li>
    <li>(D) Hornblendite</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Skarn</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Skarn Petrology and Contact Metasomatism</h3>
<p>
<strong>Skarn</strong> (an old Swedish mining term originally applied to silicate gangue associated with iron ores) refers to calcium-iron-magnesium-aluminum rich silicate rocks produced by the interaction of silica- and volatile-rich magmatic fluids with <strong>carbonate sedimentary rocks</strong> (limestone or dolomite):
</p>
<ul>
  <li><strong>Reaction Mechanism:</strong>
    <ul>
      <li>When a granitic or dioritic intrusion invades limestone ($CaCO_3$) or dolostone ($CaMg(CO_3)_2$), intense thermal decarbonation occurs, releasing $CO_2$.</li>
      <li>Simultaneously, hot hydrothermal fluids carrying silica ($SiO_2$), alumina ($Al_2O_3$), and iron from the cooling magma invade the carbonate wall rock.</li>
      <li>This intense two-way mass exchange (metasomatism) crystallizes a distinctive calc-silicate assemblage dominated by <strong>andradite-grossular garnet, diopside-hedenbergite pyroxene, wollastonite, epidote, tremolite, and vesuvianite</strong>.</li>
    </ul>
  </li>
  <li><strong>Distinctions:</strong>
    <ul>
      <li><em>Carbonatites</em> are true igneous rocks crystallized from mantle-derived carbonate melts ($>50\%$ primary carbonate).</li>
      <li><em>Hornblendite</em> is an ultramafic igneous rock composed almost entirely of hornblende.</li>
      <li><em>Metamorphite</em> is an archaic, non-specific general word for any metamorphic rock.</li>
    </ul>
  </li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Skarn) is correct:</strong> The definitive geological term for contact metasomatic zones developed in invaded carbonate rocks (tactite / skarn).</li>
  <li><strong>Option A (Carbonatites):</strong> Mantle igneous rocks, not contact metamorphic contact zones.</li>
  <li><strong>Option D (Hornblendite):</strong> Ultramafic igneous rock.</li>
</ul>
""",
    },
    121: {
        "title": "Q121: Engineering Rock Mechanics - Unconfined Compressive Strength (UCS)",
        "part1": r"""
<h3>1. Question & Engineering Index Property</h3>
<div class="question-box">
  <p><strong>Question 121:</strong> Which type of compressive strength is taken as the most important index property of stones ?</p>
  <ul>
    <li>(A) Confined</li>
    <li>(B) Drained</li>
    <li>(C) Undrained</li>
    <li>(D) Unconfined</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(D) Unconfined</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Unconfined Compressive Strength (UCS)</h3>
<p>
In engineering geology and rock mechanics (IS: 9143, ISRM Suggested Methods, Bieniawski's RMR, and Hoek-Brown failure criterion), the <strong>Unconfined Compressive Strength (UCS, $\sigma_c$)</strong>—also termed <em>uniaxial compressive strength</em>—is unanimously recognized as the single most critical index property of intact rock:
</p>
<ul>
  <li><strong>Testing Protocol:</strong> A prepared cylindrical rock core (length-to-diameter ratio $L/D = 2.0 - 2.5$) is placed between steel platens and axially loaded to failure without lateral confinement ($\sigma_2 = \sigma_3 = 0$):
    $$\sigma_c = \frac{P_{\text{failure}}}{A}$$
    where $P_{\text{failure}}$ is the peak axial load at catastrophic failure, and $A$ is the cross-sectional area.</li>
  <li><strong>Why UCS is the Cardinal Index:</strong>
    <ul>
      <li>It governs rock mass classification systems (RMR, Q-system, GSI).</li>
      <li>It dictates bearing capacity for dam foundations, bridge piers, and high-rise footings.</li>
      <li>It controls tunnel drillability, excavatability, and stability of underground openings.</li>
    </ul>
  </li>
  <li><em>Confined, drained, and undrained</em> strengths are specialized parameters measured in triaxial cells primarily for soft cohesive soils, weak clays, or deep reservoir conditions, whereas UCS is the universal standard index for building stones.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option D (Unconfined) is correct:</strong> UCS is the universal index parameter used across engineering specifications (Bangar p. 186; IS 9143).</li>
  <li><strong>Option A (Confined):</strong> Requires specialized triaxial cells ($\sigma_3 > 0$); used for deep rock mass modeling, not routine stone index characterization.</li>
  <li><strong>Option B & C (Drained / Undrained):</strong> Soil mechanics terms governing pore water drainage states.</li>
</ul>
""",
    },
    122: {
        "title": "Q122: Rock Mechanics - Transverse (Flexural / Bending) Strength",
        "part1": r"""
<h3>1. Question & Flexural Load Definition</h3>
<div class="question-box">
  <p><strong>Question 122:</strong> Capacity of a stone to withstand bending loads is termed as :</p>
  <ul>
    <li>(A) Bending strength</li>
    <li>(B) Shear strength</li>
    <li>(C) Transverse strength</li>
    <li>(D) Lateral strength</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Transverse strength</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Transverse Strength (Modulus of Rupture)</h3>
<p>
In engineering geology, civil engineering specifications, and Indian Standards (IS: 1706 / IS: 3316), the capacity of a structural stone or rock slab to withstand transverse bending forces without fracturing is formally designated as its <strong>Transverse strength</strong> (or <em>flexural strength / modulus of rupture</em>):
</p>
<ul>
  <li><strong>Testing Principle (Three-Point Bending Test):</strong> A rectangular stone beam or slab of width $b$, depth $d$, and span length $L$ is supported at both ends and subjected to a central concentrated vertical load $W$:
    $$f_b = \frac{3 W L}{2 b d^2}$$
    where $f_b$ is the transverse strength (modulus of rupture).</li>
  <li><strong>Engineering Importance:</strong>
    <ul>
      <li>Critical for flagstones, lintels, roof slabs, pavements, and cantilever stone structures where loads act perpendicularly to the longitudinal axis, inducing compressive stress on the upper surface and tensile stress on the lower surface.</li>
      <li>Because rock is notoriously weak in tension ($\sigma_t \approx 10\%\,\sigma_c$), failure in bending always initiates at the lower tensile surface.</li>
    </ul>
  </li>
  <li>In standard engineering geology textbooks (e.g., Bangar, p. 187; Mahapatra, p. 280), this property is officially titled <strong>Transverse strength</strong>.</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Transverse strength) is correct:</strong> The formal, standardized technical term in engineering geology for resistance to bending loads.</li>
  <li><strong>Option A (Bending strength):</strong> Colloquial term, but "Transverse strength" is the established engineering designation.</li>
  <li><strong>Option B (Shear strength):</strong> Resistance to sliding along internal slip planes.</li>
  <li><strong>Option D (Lateral strength):</strong> Non-standard descriptive term.</li>
</ul>
""",
    },
    123: {
        "title": "Q123: Rock Poromechanics - Void Ratio vs Porosity",
        "part1": r"""
<h3>1. Question & Volumetric Phase Ratio</h3>
<div class="question-box">
  <p><strong>Question 123:</strong> The ratio of the total volume of the pore spaces to the total volume of the solid rock mass is termed as :</p>
  <ul>
    <li>(A) Void ratio</li>
    <li>(B) Porosity</li>
    <li>(C) Pores ratio</li>
    <li>(D) Effective porosity</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(A) Void ratio</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Void Ratio ($e$) vs Porosity ($n$)</h3>
<p>
In rock mechanics, soil mechanics, and hydrogeology, the pore geometry of a geological material is rigorously defined by two distinct volume ratios:
</p>
<table class="table">
  <thead>
    <tr>
      <th>Property</th>
      <th>Definition Formula</th>
      <th>Denominator</th>
      <th>Range & Usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Void Ratio ($e$)</strong></td>
      <td><strong>$e = \frac{V_v}{V_s}$</strong></td>
      <td><strong>Volume of Solid rock / mineral skeleton ($V_s$)</strong></td>
      <td>Can exceed $1.0$ ($0 < e < \infty$); preferred in mechanics because solid volume $V_s$ remains constant during compaction.</td>
    </tr>
    <tr>
      <td><strong>Porosity ($n$)</strong></td>
      <td>$n = \frac{V_v}{V_t} \times 100$</td>
      <td><strong>Total volume of the rock ($V_t = V_s + V_v$)</strong></td>
      <td>Always $< 100\%$ (expressed as a fraction or percentage); preferred in hydrogeology and reservoir engineering.</td>
    </tr>
    <tr>
      <td><strong>Effective Porosity ($n_e$)</strong></td>
      <td>$n_e = \frac{V_{\text{interconnected voids}}}{V_t}$</td>
      <td>Total volume ($V_t$)</td>
      <td>Only measures interconnected void channels that permit fluid transmission.</td>
    </tr>
  </tbody>
</table>
<p>
The mathematical relationship linking them is:
$$e = \frac{n}{1 - n} \quad \Longleftrightarrow \quad n = \frac{e}{1 + e}$$
Because the question explicitly specifies the ratio of the volume of pore spaces ($V_v$) to the volume of the <strong>solid rock mass ($V_s$)</strong>, it is by definition the <strong>Void ratio ($e$)</strong>.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option A (Void ratio) is correct:</strong> $e = V_v / V_s$ (ratio of voids to solid skeleton).</li>
  <li><strong>Option B (Porosity):</strong> The ratio of voids to <em>total volume</em> ($V_v / V_t$), the classic trap!</li>
  <li><strong>Option C (Pores ratio):</strong> Fabricated distractor.</li>
  <li><strong>Option D (Effective porosity):</strong> Ratio of interconnected voids to total volume.</li>
</ul>
""",
    },
    124: {
        "title": "Q124: Rock Mechanics - Bulk Density and Natural Moisture Content",
        "part1": r"""
<h3>1. Question & Density Formulation</h3>
<div class="question-box">
  <p><strong>Question 124:</strong> The mass per unit volume of a rock sample with natural moisture content is its :</p>
  <ul>
    <li>(A) Dry density</li>
    <li>(B) Wet density</li>
    <li>(C) Bulk density</li>
    <li>(D) Natural density</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) Bulk density</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: Rock Density Classifications</h3>
<p>
In engineering geology and ISRM rock characterization, density definitions reflect different fluid saturation states:
</p>
<ul>
  <li><strong>Bulk Density ($\rho_b$):</strong> Defined as the total mass of the rock sample (including solid mineral grains plus whatever natural moisture/water is retained in its pore spaces in the in-situ state) per unit total volume ($V_t$):
    $$\rho_b = \frac{M_{\text{natural}}}{V_t} = \frac{M_s + M_w}{V_t}$$
    This is the fundamental design value used for computing overburden stresses, retaining wall thrusts, and foundation settlements under field conditions.</li>
  <li><strong>Dry Density ($\rho_d$):</strong> The mass of the rock skeleton after oven drying at $105^\circ\text{C}$ to complete dehydration, per unit total volume:
    $$\rho_d = \frac{M_s}{V_t}$$</li>
  <li><strong>Saturated Density ($\rho_{\text{sat}}$):</strong> Mass per unit volume when 100% of pore spaces are fully filled with water under vacuum saturation.</li>
  <li><strong>Grain / Solid Density ($\rho_s$):</strong> Mass of solid mineral particles divided exclusively by the volume of solids ($M_s / V_s$), excluding all pore volume.</li>
</ul>
<p>
In standard engineering textbooks (Bangar, p. 187; IS: 13030), the mass per unit volume under natural in-situ moisture conditions is formally termed <strong>Bulk density</strong>.
</p>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C (Bulk density) is correct:</strong> The standardized engineering and geotechnical term for total in-situ mass per unit volume.</li>
  <li><strong>Option A (Dry density):</strong> Oven-dried rock devoid of moisture.</li>
  <li><strong>Option B & D (Wet / Natural density):</strong> Informal non-standard vernacular; IS codes and ISRM universally utilize the term <em>Bulk density</em>.</li>
</ul>
""",
    },
    125: {
        "title": "Q125: In-Situ Rock Testing - Schmidt Hammer Rebound Hardness",
        "part1": r"""
<h3>1. Question & Statement Analysis</h3>
<div class="question-box">
  <p><strong>Question 125:</strong> Find out the incorrect statement regarding Schmidt Hammer :</p>
  <ul>
    <li>(A) It is concrete test hammer originally designed for carrying out in-situ tests on the hardness of concrete.</li>
    <li>(B) The instrument measures the distance of rebound of a controlled impact on a rock surface.</li>
    <li>(C) The distance of rebound (R) gives an absolute measure of surface hardness or strength.</li>
    <li>(D) Schmidt hammer rebound values have been found to correlate well with other measures of rock strength, including Young&rsquo;s Modulus and Uniaxial Strength.</li>
  </ul>
  <p><strong>Correct Answer:</strong> <strong>(C) The distance of rebound (R) gives an absolute measure of surface hardness or strength.</strong></p>
</div>
""",
        "part2": r"""
<h3>2. Detailed Geological Masterclass: The Schmidt Rebound Hammer (ISRM Standards)</h3>
<p>
The <strong>Schmidt Hammer</strong> (Type L or Type N) is a portable, non-destructive mechanical apparatus widely employed in engineering geology and geotechnical site characterization:
</p>
<ul>
  <li><strong>Operating Principle:</strong> A spring-loaded mass impacts a plunger pressed against the rock or concrete surface. Upon impact, the mass rebounds. The rebound distance ($R$) is recorded on a linear scale from 10 to 100 (Statements A and B are TRUE).</li>
  <li><strong>Relative Empirical Index (NOT an Absolute Measure):</strong>
    <ul>
      <li>The rebound value $R$ does <strong>NOT</strong> provide an <em>absolute</em> measure of rock strength or surface hardness (Statement C is FALSE, hence the correct answer).</li>
      <li>$R$ is purely an <strong>empirical, dimensionless relative index</strong>. To deduce compressive strength or modulus, $R$ must be multiplied by rock bulk density and referenced against empirical correlation charts (e.g., Deere & Miller, 1966).</li>
      <li>$R$ is highly sensitive to surface roughness, weathering rinds, moisture content, hammer inclination (vertical, horizontal, overhead), and core specimen clamping.</li>
    </ul>
  </li>
  <li><strong>Correlations:</strong> Extensive empirical studies (ISRM, Barton & Choubey) confirm that properly calibrated Schmidt rebound values correlate strongly with Uniaxial Compressive Strength (UCS) and dynamic Young's Modulus (Statement D is TRUE).</li>
</ul>
""",
        "part3": r"""
<h3>3. Critical Option Elimination & Exam Traps</h3>
<ul>
  <li><strong>Option C is the incorrect statement (hence correct answer):</strong> Rebound $R$ is an empirical relative index, never an "absolute measure".</li>
  <li><strong>Option A is true:</strong> Originally invented by Ernst Schmidt in 1948 for non-destructive concrete testing.</li>
  <li><strong>Option B is true:</strong> Measures rebound travel distance of the spring-driven hammer mass.</li>
  <li><strong>Option D is true:</strong> Widely verified correlations exist for UCS and modulus estimation.</li>
</ul>
""",
    },
}
