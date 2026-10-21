#!/usr/bin/env python3
import json
import os

with open('/home/tapaswi/Mines_Geology/Orrisa_geology/data/geology_2021.json') as f:
    questions = json.load(f)

# Comprehensive 3-Tier Guides Content for Q1-Q10
guides = {
    1: {
        "title": "Q1: Slope Stability, Mass Movement vs. Landslide & Shear Plane Mechanics",
        "part1": """
        <h3>1.1 Fundamental Distinction: Mass Wasting vs. True Landslides</h3>
        <p>In classical geomorphology and engineering geology (Varnes, 1978; Cruden & Varnes, 1996; Bangar, <i>Principles of Engineering Geology</i>, Ch. 12), the downslope displacement of earth materials is categorized under the comprehensive umbrella of <b>mass movement (mass wasting)</b>.</p>
        <p>However, engineering geology establishes a critical mechanical demarcation based on the existence of a <b>discrete shear surface (slip plane)</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Classification Criteria</th>
                <th>Mass Movement (Sensu Lato)</th>
                <th>Landslide (Sensu Stricto)</th>
                <th>Creep</th>
                <th>Avalanche</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Shear Plane</b></td>
                <td>May be absent, diffuse, internal, or discrete</td>
                <td><b>Discrete, well-defined shear failure plane</b></td>
                <td>No discrete shear plane; continuous internal viscous strain</td>
                <td>Turbulent fluid-like flow, cushion of compressed air</td>
              </tr>
              <tr>
                <td><b>Displacement Mechanics</b></td>
                <td>Falls, topples, slides, spreads, flows</td>
                <td><b>Rigid or semi-rigid shear slide (rotational or translational)</b></td>
                <td>Slow, imperceptible seasonal ratchet strain</td>
                <td>Extremely rapid, airborne turbulent granular flow</td>
              </tr>
              <tr>
                <td><b>Mohr-Coulomb Failure</b></td>
                <td>Variable</td>
                <td>$\\tau_f = c' + \\sigma_n' \\tan \\phi'$ localized on basal surface</td>
                <td>Low-stress distributed shear strain $(\\dot{\\gamma})$</td>
                <td>Fluidized granular dispersion</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>1.2 Kinematic Classifications of Landslides (Varnes, 1978)</h3>
        <p>A true landslide occurs when the shear stress $(\\tau)$ along a potential failure surface exceeds the shear strength $(\\tau_f)$ of the rock or soil mass. The two primary categories defined by the geometry of the shear plane are:</p>
        <ul>
          <li><b>Rotational Slides (Slumps):</b> The shear plane is concave upward (spoon-shaped). The movement involves backward tilting of the slip block towards the scarp.</li>
          <li><b>Translational Slides:</b> The shear plane is approximately planar or undulating, often controlled by structural discontinuities (bedding planes, foliation, joints, or fault surfaces).</li>
        </ul>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Landslide</b> — Downward movement of slope-forming material resulting from shear failure along a <i>well-defined shear plane</i> is strictly defined as a <b>Landslide</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Mass movement — INCORRECT (Distractor / Over-generalization):</b> Mass movement is the broad generic term that includes falls, topples, slides, flows, and creep. It is not restricted to movements with a well-defined shear plane (e.g. mudflows and creep lack a distinct shear plane).</li>
          <li><b>(B) Landslide — CORRECT:</b> In international engineering geology terminology (Varnes 1978; IAEG Commission on Landslides), a landslide is explicitly defined as shear failure localized along a recognizable, well-defined shear plane or zone of rupture.</li>
          <li><b>(C) Creep — INCORRECT:</b> Soil creep or rock creep is an extremely slow, imperceptible, continuous deformation occurring throughout the entire thickness of the soil without a discrete shear failure surface.</li>
          <li><b>(D) Avalanche — INCORRECT:</b> An avalanche is a rapid, turbulent downrush of snow, ice, or shattered rock debris supported by dynamic flow or air cushioning rather than sliding on a stationary shear plane.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Concept Check & Numerical Applications</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 1: Factor of Safety on a Planar Slip Surface</div>
          <p>A translational landslide occurs along a planar bedding plane inclined at $\\theta = 30^\\circ$. The cohesive strength $c' = 15\\text{ kPa}$, effective normal stress $\\sigma_n' = 80\\text{ kPa}$, and internal friction angle $\\phi' = 25^\\circ$. If the driving shear stress along the slip plane is $\\tau_d = 45\\text{ kPa}$, calculate the Factor of Safety ($FS$) and determine slope stability.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>The resisting shear strength along the shear plane is given by the Mohr-Coulomb criterion:</p>
            $$\\tau_f = c' + \\sigma_n' \\tan \\phi' = 15 + 80 \\tan(25^\\circ) = 15 + 80(0.4663) = 15 + 37.3 = 52.3\\text{ kPa}$$
            <p>The Factor of Safety ($FS$) is the ratio of resisting shear strength to driving shear stress:</p>
            $$FS = \\frac{\\tau_f}{\\tau_d} = \\frac{52.3}{45.0} \\approx 1.16$$
            <p>Since $FS > 1.0$, the slope is conditionally stable, but vulnerable to failure if pore water pressure reduces $\\sigma_n'$.</p>
          </div>
        </div>
        """
    },
    2: {
        "title": "Q2: Fluvial Channel Sinuosity Index & Meandering Thresholds",
        "part1": """
        <h3>2.1 Mathematical Definition of Sinuosity Index</h3>
        <p>In fluvial geomorphology and sedimentology (Leopold & Wolman, 1957; Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i>, 5th Ed., Ch. 8), <b>channel sinuosity ($S$ or $P$)</b> is defined as the ratio of channel length measured along the thalweg to the down-valley axial distance:</p>
        $$\\text{Sinuosity Index } (S) = \\frac{L_{\\text{channel}}}{L_{\\text{valley}}}$$
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Sinuosity Range</th>
                <th>Channel Planform Category</th>
                <th>Sediment Transport & Hydraulic Regime</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>$S < 1.05$</td>
                <td><b>Straight Channel</b></td>
                <td>Rare in natural systems; steep gradient, coarse bedload</td>
              </tr>
              <tr>
                <td>$1.05 \\le S < 1.50$</td>
                <td><b>Sinuous Channel</b></td>
                <td>Moderate gradient, alternating side bars / riffles</td>
              </tr>
              <tr>
                <td><b>$S \\ge 1.50$</b></td>
                <td><b>Meandering Channel</b></td>
                <td><b>Threshold value for true meandering rivers</b>; high suspended load, low slope, active point-bar accretion & neck cutoffs</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>2.2 The Leopold-Wolman Gradient-Discharge Continuum</h3>
        <p>Meandering rivers plot below the braided-meandering threshold line on a slope ($S$) vs. discharge ($Q$) diagram:</p>
        $$S_{\\text{crit}} = 0.06 Q^{-0.44}$$
        <p>Where channel slope exceeds this critical threshold, braided planforms with multiple active thalwegs and mid-channel longitudinal bars develop.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) 1.5</b> — By standard academic definition (Leopold & Wolman 1957; Sam Boggs Jr.), a river channel is classified as officially <b>meandering</b> when its Sinuosity Index exceeds the threshold value of <b>1.5</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 1.4 — INCORRECT:</b> A channel with sinuosity of 1.4 is classified as "sinuous" or "moderately sinuous", but has not crossed the internationally accepted geomorphic threshold of 1.5.</li>
          <li><b>(B) 1.5 — CORRECT:</b> The universal empirical boundary separating sinuous rivers from true meandering rivers is $S = 1.5$.</li>
          <li><b>(C) 1.6 — INCORRECT:</b> While meandering rivers frequently exceed 1.6 (often reaching 2.0 to 2.5), 1.6 is not the defining threshold.</li>
          <li><b>(D) 1.2 — INCORRECT:</b> Channels with sinuosity between 1.05 and 1.2 are simply low-sinuosity transitional streams.</li>
        </ul>
        """,
        "part3": """
        <h3>Fluvial Systematics & Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 2: Sinuosity Calculation & Planform Identification</div>
          <p>A river reach flowing across an alluvial plain covers an actual channel length of $42.6\\text{ km}$ between two bridge points whose straight valley distance is $24.2\\text{ km}$. Calculate the Sinuosity Index and classify the stream channel.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$S = \\frac{L_{\\text{channel}}}{L_{\\text{valley}}} = \\frac{42.6}{24.2} = 1.76$$
            <p>Since $S = 1.76 > 1.5$, the river reach is definitively classified as a <b>Meandering river</b> with well-developed point bars and meander bends.</p>
          </div>
        </div>
        """
    },
    3: {
        "title": "Q3: Aeolian Activity Dynamic Controls (Transport Capacity, Supply & Availability)",
        "part1": """
        <h3>3.1 The Kocurek-Lancaster Aeolian System Triad</h3>
        <p>In modern process sedimentology (Kocurek & Lancaster, 1999; Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i>, Ch. 9), aeolian dynamics and dune development are governed by the interaction of three core variables:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Core Variable</th>
                <th>Physical Definition & Governing Factors</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>(i) Transport Capacity ($T_c$)</b></td>
                <td>The potential rate of sand transport by wind, governed by shear velocity ($u_*$) and fluid threshold: $q \\propto u_*^3$.</td>
              </tr>
              <tr>
                <td><b>(ii) Sediment Supply ($G_s$)</b></td>
                <td>The total inventory and volume of erodible sediment present in the upwind source basin (e.g. desiccated lake beds, outwash plains).</td>
              </tr>
              <tr>
                <td><b>(iv) Sediment Availability ($A_s$)</b></td>
                <td>The fraction of supply susceptible to wind entrainment, limited by surface moisture, clay crusts, salt efflorescence, water table depth, and vegetation cover.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>3.2 Why \"Hot Desertic Conditions\" is Not a Universal Physical Requirement</h3>
        <p>While vast erg systems exist in the Sahara and Arabian deserts, aeolian processes are <b>not strictly limited to hot deserts</b>:</p>
        <ul>
          <li><b>Periglacial & Cold Deserts:</b> Extensive active aeolian sand dunes and loess sheets form in the McMurdo Dry Valleys of Antarctica, Arctic Alaska, and the cold deserts of Tibet and Ladakh.</li>
          <li><b>Pleistocene Loess:</b> The massive loess plateau deposits of China and Europe were produced during cold, arid glacial maxima, not under hot climatic regimes.</li>
          <li><b>Coastal Dune Fields:</b> Form along temperate and sub-polar coasts regardless of temperature.</li>
        </ul>
        <p>Therefore, the triad of physical control is universally <b>(i) Transport capacity, (ii) Sediment supply, and (iv) Sediment availability</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) (i), (ii), (iv)</b> — Aeolian activity is fundamentally controlled by <b>Transport capacity</b>, <b>Sediment supply</b>, and <b>Sediment availability</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) (i), (ii), (iii) — INCORRECT:</b> Excludes sediment availability (iv), which is mandatory to account for moisture and crusting limiting factors, while erroneously including hot desert conditions (iii).</li>
          <li><b>(B) (i), (ii), (iv) — CORRECT:</b> Precisely identifies the canonical triad established by Kocurek & Lancaster (1999) and textbook aeolian physics.</li>
          <li><b>(C) (i), (iii), (iv) — INCORRECT:</b> Omits sediment supply (ii); without a reservoir of sand, high wind capacity produces deflation lags or bedrock ventifacts rather than dune fields.</li>
          <li><b>(D) (i), (ii), (iii), (iv) — INCORRECT:</b> Erroneously includes (iii); temperature is a secondary modifying factor, not a primary controlling prerequisite.</li>
        </ul>
        """,
        "part3": """
        <h3>Grain Entrainment Threshold Formula & Practice</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 3: Bagnold's Fluid Threshold for Sand Transport</div>
          <p>According to Bagnold's equation, what is the relationship between the threshold shear velocity ($u_{*t}$) required to initiate sand grain movement and grain diameter ($D$)?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>Bagnold's fluid threshold velocity equation is:</p>
            $$u_{*t} = A \\sqrt{\\frac{\\rho_s - \\rho_a}{\\rho_a} g D}$$
            <p>Where $A \\approx 0.1$ for grains $> 0.1\\text{ mm}$, $\\rho_s$ is quartz density ($2650\\text{ kg/m}^3$), $\\rho_a$ is air density ($1.22\\text{ kg/m}^3$), $g$ is gravity, and $D$ is grain diameter. For typical medium dune sand ($D = 0.25\\text{ mm}$), $u_{*t} \\approx 0.22\\text{ m/s}$.</p>
          </div>
        </div>
        """
    },
    4: {
        "title": "Q4: Quantitative Morphotectonic Indices for Drainage Basin Analysis",
        "part1": """
        <h3>4.1 The Keller-Pinter Framework for Morphotectonic Analysis</h3>
        <p>In tectonic geomorphology and active fault studies (Keller & Pinter, 2002, <i>Active Tectonics: Earthquakes, Uplift, and Landscape</i>, Ch. 5; Burbank & Anderson, 2011), four quantitative indices are systematically computed to assess relative tectonic activity ($I_{at}$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Index Name & Symbol</th>
                <th>Mathematical Formula</th>
                <th>Tectonic Significance & Diagnostic Signatures</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>1. Drainage Basin Asymmetry ($AF$)</b></td>
                <td>$AF = 100 \\left(\\frac{A_r}{A_t}\\right)$</td>
                <td>Detects tectonic tilt perpendicular to trunk stream. $AF = 50$ indicates symmetric equilibrium; significant deviation from 50 reveals active structural tilting.</td>
              </tr>
              <tr>
                <td><b>2. Stream Length-Gradient ($SL$)</b></td>
                <td>$SL = \\left(\\frac{\\Delta H}{\\Delta L}\\right) L$</td>
                <td>Sensitive to changes in river gradient caused by active fault scarps, tectonic knickpoints, or contrasting rock resistance. High $SL$ values highlight active uplift.</td>
              </tr>
              <tr>
                <td><b>3. Mountain-Front Sinuosity ($S_{mf}$)</b></td>
                <td>$S_{mf} = \\frac{L_{mf}}{L_s}$</td>
                <td>Reflects balance between active uplift and stream embayment along front faults. $S_{mf} < 1.4$ indicates high tectonic activity (straight front); $S_{mf} > 2.0$ indicates quiescence.</td>
              </tr>
              <tr>
                <td><b>4. Valley Floor Width to Height Ratio ($V_f$)</b></td>
                <td>$V_f = \\frac{2 V_{fw}}{(E_{ld} - E_{sc}) + (E_{rd} - E_{sc})}$</td>
                <td>Distinguishes actively uplifting deep V-shaped canyons ($V_f \\ll 1.0$) from flat, tectonically inactive wide-bottomed valleys ($V_f \\gg 1.0$).</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) (i), (ii), (iii) and (iv)</b> — All four listed indices ($AF$, $SL$, $S_{mf}$, $V_f$) are standard, recognized <b>Tectonic Activity Indices</b> used in morphotectonic drainage basin analysis.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) (i), (ii) and (iv) — INCORRECT:</b> Omission of Mountain-front sinuosity ($S_{mf}$), which is one of the most critical indices used to distinguish active Range-bounding fault fronts.</li>
          <li><b>(B) (ii) and (iv) — INCORRECT:</b> Omits basin asymmetry and mountain front sinuosity.</li>
          <li><b>(C) (i), (ii), (iii) and (iv) — CORRECT:</b> Captures the complete, canonical four-index morphotectonic suite formalized by Keller & Pinter (2002).</li>
          <li><b>(D) (ii), (iii) and (iv) — INCORRECT:</b> Omits basin asymmetry ($AF$).</li>
        </ul>
        """,
        "part3": """
        <h3>Worked Morphotectonic Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 4: Calculation of Mountain Front Sinuosity ($S_{mf}$)</div>
          <p>Along an active mountain front fault in the Eastern Ghats, the measured length along the topographic break-in-slope of the mountain front is $L_{mf} = 14.8\\text{ km}$, while the straight-line distance along the fault front is $L_s = 12.0\\text{ km}$. Calculate $S_{mf}$ and interpret the tectonic activity class.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$S_{mf} = \\frac{L_{mf}}{L_s} = \\frac{14.8}{12.0} = 1.23$$
            <p>According to Keller & Pinter classification: Class 1 (Highly Active): $S_{mf} < 1.4$. Since $S_{mf} = 1.23 < 1.4$, the mountain front is classified as <b>Tectonically Active (Class 1)</b> with rapid uplift rates outcompeting stream erosion and embayment.</p>
          </div>
        </div>
        """
    },
    5: {
        "title": "Q5: Pedestal Rocks & Mushroom Rocks (Differential Wind Abrasion)",
        "part1": """
        <h3>5.1 Genesis of Pedestal & Mushroom Rocks</h3>
        <p>In arid geomorphology (Arthur Holmes, <i>Principles of Physical Geology</i>; K.M. Bangar, <i>Principles of Engineering Geology</i>, Ch. 5), isolated rock outcrops exhibiting a slender basal stem supporting an expanded, mushroom-like cap are termed <b>pedestal rocks</b> or <b>mushroom rocks</b> (German: <i>Pilzfelsen</i>).</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Feature</th>
                <th>Mushroom / Pedestal Rock</th>
                <th>Balanced Rock</th>
                <th>Perched Block</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Morphology</b></td>
                <td>Slender neck/column supporting an overarching wider cap</td>
                <td>Rounded corestone or boulder poised delicately on a bedrock pedestal</td>
                <td>Alien boulder resting abruptly on bedrock or high ridge</td>
              </tr>
              <tr>
                <td><b>Primary Process</b></td>
                <td><b>Differential wind abrasion (sandblasting) + basal chemical weathering</b></td>
                <td>Spheroidal weathering, sub-surface joint etching, and wash</td>
                <td><b>Glacial transport (erratic)</b> or catastrophic rockfall</td>
              </tr>
              <tr>
                <td><b>Maximum Abrasion Height</b></td>
                <td>Concentrated in the basal zone: $0.3 - 1.0\\text{ m}$ above desert surface</td>
                <td>N/A</td>
                <td>N/A</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>5.2 Physics of Saltation and Basal Undercutting</h3>
        <p>Wind-driven sand transport occurs overwhelmingly via <b>saltation</b>. Heavy quartz sand grains rarely bounce higher than <b>$1\\text{ to }1.5\\text{ meters}$</b> above the desert floor. Consequently, wind abrasion (sandblasting) reaches maximum kinetic intensity near ground level, actively undercutting rock bases into slender necks while higher portions remain uncarved.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) (i) and (ii)</b> — An isolated rock mass comprising a slender stem supporting a wider cap is synonymously designated as <b>Pedestal rocks</b> and <b>Mushroom rocks</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(i) Pedestal rocks — TRUE:</b> Standard geomorphic term for mushroom-shaped undercut residual rock towers.</li>
          <li><b>(ii) Mushroom rocks — TRUE:</b> Universal colloquial and academic synonym (Pilzfelsen).</li>
          <li><b>(iii) Balanced rocks — FALSE:</b> Balanced rocks lack a slender carved erosional stem; they are tor blocks or corestones perched on tiny contact points.</li>
          <li><b>(iv) Perched blocks — FALSE:</b> Perched blocks are glacial erratics stranded atop foreign bedrock during ice retreat.</li>
        </ul>
        """,
        "part3": """
        <h3>Concept Check: Ventifacts vs. Yardangs vs. Zeugen</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 5: Comparative Aeolian Erosional Landforms</div>
          <p>Distinguish between a <b>Zeugen</b> and a <b>Yardang</b> in terms of bedrock structure and wind alignment.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <ul>
              <li><b>Zeugen:</b> Formed on horizontally bedded strata where a hard, resistant rock layer caps an underlying soft rock layer. Wind opens joints into ridge-and-furrow table forms.</li>
              <li><b>Yardang:</b> Formed on vertically or steeply tilted alternating hard and soft strata that run parallel to the prevailing wind direction, carved into streamlined, keel-like ridges.</li>
            </ul>
          </div>
        </div>
        """
    },
    6: {
        "title": "Q6: Optically Stimulated Luminescence (OSL) Dating Methodology",
        "part1": """
        <h3>6.1 Principles of Luminescence Dating (OSL & TL)</h3>
        <p>In geochronology and Quaternary geology (Aitken, 1998; William M. White, <i>Geochemistry</i>, Ch. 8), <b>Optically Stimulated Luminescence (OSL)</b> measures the time that has elapsed since mineral grains (quartz or potassium feldspar) were last exposed to sunlight or heat:</p>
        $$\\text{Age (years)} = \\frac{\\text{Equivalent Dose } (D_e) \\text{ [Grays]}}{\\text{Environmental Dose Rate } (D_r) \\text{ [Grays/year]}}$$
        
        <h3>6.2 The \"Bleaching\" (Zeroing) Mechanism</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Material Type</th>
                <th>Bleaching / Zeroing Event</th>
                <th>Suitability for OSL Dating</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>(i) Naturally occurring sediments</b></td>
                <td><b>Exposure to daylight</b> during aeolian, fluvial, or coastal transport drains all trapped electrons</td>
                <td><b>EXCELLENT</b> (Dune sand, beach ridges, loess, floodplain silt)</td>
              </tr>
              <tr>
                <td><b>(ii) Man-made materials (Pottery, Bricks)</b></td>
                <td><b>Thermal heating</b> in kiln firing (> 500 °C) drains trapped electrons to zero</td>
                <td><b>EXCELLENT</b> (Universal method for archaeological ceramic dating)</td>
              </tr>
              <tr>
                <td><b>(iii) Intrusive igneous rocks</b></td>
                <td>Cooled slowly at depth without daylight exposure; traps saturated from geologic time</td>
                <td><b>UNSUITABLE</b> (Cannot record surface burial age; use U-Pb, Rb-Sr, K-Ar)</td>
              </tr>
              <tr>
                <td><b>(iv) Metasedimentary rocks</b></td>
                <td>Metamorphic recrystallization at depth; no daylight zeroing event</td>
                <td><b>UNSUITABLE</b> (Use metamorphic mineral isochrons)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) (i) and (ii)</b> — OSL dating is specifically applicable to <b>(i) Naturally occurring sediments</b> (zeroed by sunlight) and <b>(ii) Man-made materials like pottery</b> (zeroed by firing heat).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) (i), (ii) and (iii) — INCORRECT:</b> Fails because intrusive igneous rocks cannot be dated by OSL (they lack a daylight bleaching event).</li>
          <li><b>(B) (i) and (ii) — CORRECT:</b> Accurately pairs the two classic luminescence applications: daylight-bleached sedimentary grains and kiln-fired pottery.</li>
          <li><b>(C) (iii) and (iv) — INCORRECT:</b> Both crystalline rock categories are completely incompatible with OSL dating.</li>
          <li><b>(D) (i) and (iii) — INCORRECT:</b> Erroneously includes intrusive igneous rocks.</li>
        </ul>
        """,
        "part3": """
        <h3>Worked OSL Age Calculation Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 6: Calculating the Burial Age of a Coastal Paleodune</div>
          <p>A quartz sample collected from a paleodune in coastal Odisha yielded a laboratory paleodose (equivalent dose) of $D_e = 48.0\\text{ Gy}$. Gamma spectrometry of the surrounding sediment indicates a total environmental dose rate of $D_r = 1.6\\text{ mGy/year}$. Calculate the burial age of the dune sand.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            $$\\text{Age} = \\frac{D_e}{D_r} = \\frac{48.0\\text{ Gy}}{0.0016\\text{ Gy/year}} = 30,000\\text{ years} = 30\\text{ ka}$$
            <p>The sand grains were deposited and buried from daylight approximately <b>30,000 years ago</b> (Late Pleistocene).</p>
          </div>
        </div>
        """
    },
    7: {
        "title": "Q7: Fluvial Megafans vs. Alluvial Fans in Foreland Basins",
        "part1": """
        <h3>7.1 Diagnostic Differences: Fluvial Megafans vs. Alluvial Fans</h3>
        <p>In modern basin analysis (Leier et al., 2005; Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i>, Ch. 8), <b>fluvial megafans</b> (such as the modern Kosi, Gandak, and Pilcomayo fans) represent distinct macro-depositional systems:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Diagnostic Parameter</th>
                <th>Alluvial Fans (Sensu Stricto)</th>
                <th>Fluvial Megafans</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Areal Footprint</b></td>
                <td>Small: typically $< 100\\text{ km}^2$ (rarely up to $500\\text{ km}^2$)</td>
                <td><b>Massive: $> 10^3\\text{ to } 10^5\\text{ km}^2$ (radial length $> 100\\text{ km}$)</b></td>
              </tr>
              <tr>
                <td><b>Topographic Slope</b></td>
                <td>Steep: typically $1.5^\\circ - 10^\\circ$ ($> 0.02$)</td>
                <td><b>Extremely low gradient: $< 0.1^\\circ$ ($< 0.001$, often $0.1 - 0.5\\text{ m/km}$)</b></td>
              </tr>
              <tr>
                <td><b>Feeding River Source</b></td>
                <td>Small mountain catchments, ephemeral torrents</td>
                <td><b>Large, perennial mountain rivers (continental drainages)</b></td>
              </tr>
              <tr>
                <td><b>Dominant Sedimentary Process</b></td>
                <td>Debris flows, sheetfloods, gravelly sieve deposits</td>
                <td><b>Unconfined multichannel braided/meandering channel avulsion</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>7.2 Critical Analysis of Question Statements</h3>
        <ul>
          <li><b>Statement (i) — TRUE:</b> Megafans constitute volumetrically significant depositional elements of retroarc and peripheral foreland basins adjacent to orogenic belts (e.g., Himalayan foreland, Andean Chaco).</li>
          <li><b>Statement (ii) — TRUE:</b> They are directly generated when a large, sediment-laden mountain river emerges from a confined bedrock gorge onto a low-relief alluvial plain.</li>
          <li><b>Statement (iii) — FALSE:</b> They are <b>not</b> identical to alluvial fans; modern sedimentology explicitly separates megafans as a distinct class due to hydraulic, sedimentological, and architectural differences.</li>
          <li><b>Statement (iv) — TRUE:</b> They are definitively distinguished from alluvial fans by their vastly greater size and much lower slope.</li>
        </ul>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) (i), (ii), (iv)</b> — Statements (i), (ii), and (iv) are correct. Statement (iii) is incorrect because sedimentology explicitly differentiates fluvial megafans from alluvial fans.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) (i), (ii), (iii) — INCORRECT:</b> Erroneously includes (iii), equating megafans with classic alluvial fans.</li>
          <li><b>(B) (ii), (iii), (iv) — INCORRECT:</b> Erroneously includes (iii) and omits (i).</li>
          <li><b>(C) (i), (ii), (iv) — CORRECT:</b> Precisely identifies the true statements while rejecting the false synonymy of (iii).</li>
          <li><b>(D) (i), (iii), (iv) — INCORRECT:</b> Includes (iii) and omits (ii).</li>
        </ul>
        """,
        "part3": """
        <h3>Sedimentological Synthesis Table</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 7: Foreland Basin Megafan Architecture</div>
          <p>Name the world's most famous modern active fluvial megafan and describe its characteristic channel migration process.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>The <b>Kosi Megafan</b> of northern Bihar (Indo-Gangetic foreland basin). Over the past 250 years, the Kosi River has swept westward across its megafan by more than $110\\text{ km}$ through catastrophic episodic nodal avulsions driven by massive aggradation and sediment overloading.</p>
          </div>
        </div>
        """
    },
    8: {
        "title": "Q8: Trellis Drainage Pattern in Dipping and Folded Formations",
        "part1": """
        <h3>8.1 Drainage Patterns Governed by Geological Structure</h3>
        <p>In structural geomorphology (Arthur N. Strahler, <i>Physical Geology</i>; K.M. Bangar, <i>Principles of Engineering Geology</i>, Ch. 4; G.B. Mahapatra, Ch. 3), drainage patterns reflect the underlying bedrock lithology and structural deformation:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Drainage Pattern</th>
                <th>Underlying Structural & Lithologic Control</th>
                <th>Tributary Junction Angles</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Trellis</b></td>
                <td><b>Alternating bands of resistant and weak dipping/folded strata</b>. Primary streams align with strike valleys; secondary tributaries flow down dip and scarp slopes.</td>
                <td><b>Orthogonal / Right angles ($~90^\\circ$)</b></td>
              </tr>
              <tr>
                <td><b>Parallel</b></td>
                <td>Steep, uniformly dipping planar slopes (e.g. young fault blocks, volcanic cones).</td>
                <td>Parallel, acute low angles</td>
              </tr>
              <tr>
                <td><b>Rectangular</b></td>
                <td>Heavily jointed or faulted homogeneous crystalline bedrock (granite, basalt).</td>
                <td>Sharp right-angle bends along intersecting joint sets</td>
              </tr>
              <tr>
                <td><b>Dendritic</b></td>
                <td>Homogeneous, isotropic bedrock or flat-lying horizontal sedimentary strata.</td>
                <td>Irregular, acute branch-like branching</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>8.2 Strike and Dip Stream Classification</h3>
        <ul>
          <li><b>Subsequent Streams:</b> Flow along the strike of softer, easily erodible formations (forming the trunk parallel valleys).</li>
          <li><b>Consequent & Resequent Streams:</b> Flow down the original regional dip slope of the formation.</li>
          <li><b>Obsequent Streams:</b> Flow down the steep scarp slope opposite to the formation dip direction.</li>
        </ul>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Trellis</b> — When a network of parallel streams develops along the strike and dip of tilted or folded formations, the drainage pattern is designated as a <b>Trellis drainage pattern</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Parallel — INCORRECT:</b> Parallel networks occur on uniform steep slopes without orthogonal strike-dip tributary grids.</li>
          <li><b>(B) Rectangular — INCORRECT:</b> Rectangular patterns are governed by intersecting joint and fault fractures in uniform rock, not alternating strike-dip sedimentary cuestas.</li>
          <li><b>(C) Trellis — CORRECT:</b> The textbook definition of a trellis pattern is an orthogonal network where main subsequent streams follow the strike of soft strata and short tributaries follow the dip and scarp directions.</li>
          <li><b>(D) Dendritic — INCORRECT:</b> Dendritic patterns resemble branching tree roots and form only in structurally isotropic or horizontal rock formations.</li>
        </ul>
        """,
        "part3": """
        <h3>Drainage Systematics Concept Card</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 8: Appalachian Type Folded Belt Drainage</div>
          <p>In the Appalachian Valley and Ridge Province, what type of drainage pattern overwhelmingly dominates, and which structural features control it?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p><b>Trellis pattern</b>. It is controlled by plunging anticlines and synclines where hard ridge-forming sandstones/quartzites alternate with soft valley-forming shales and limestones.</p>
          </div>
        </div>
        """
    },
    9: {
        "title": "Q9: Fanglomerate Lithification & Alluvial Fan Facies",
        "part1": """
        <h3>9.1 Origin and Definition of \"Fanglomerate\"</h3>
        <p>In sedimentary petrology (Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i>, 5th Ed., Ch. 5; F.J. Pettijohn, <i>Sedimentary Rocks</i>, 3rd Ed.), the term <b>Fanglomerate</b> was coined by A.C. Lawson (1913) to designate the <b>lithified, consolidated rock equivalent of alluvial fan gravels and debris flows</b>.</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Term</th>
                <th>Geological Definition & Nature</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Fanglomerate</b></td>
                <td><b>Lithified alluvial fan conglomerate</b>; characterized by extreme textural immaturity, poor sorting, polymodal grain size, angular to sub-rounded clasts, and matrix-supported or clast-supported fabrics.</td>
              </tr>
              <tr>
                <td><b>Bajada</b></td>
                <td>A <b>geomorphic landform</b> (not a lithified rock) consisting of a continuous apron formed by the lateral coalescence of adjacent alluvial fans along a mountain front.</td>
              </tr>
              <tr>
                <td><b>Agglomerate</b></td>
                <td>A <b>pyroclastic volcanic rock</b> composed predominantly of coarse, angular or rounded volcanic bombs ($> 64\\text{ mm}$) ejected during explosive volcanism.</td>
              </tr>
              <tr>
                <td><b>Orthoconglomerate</b></td>
                <td>A texturally mature, <b>clast-supported conglomerate</b> with $< 15\\%$ fine matrix, typically well-rounded and deposited by turbulent fluvial channel currents.</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Fanglomerate</b> — The lithified portion of an alluvial fan is strictly classified in sedimentary petrology as a <b>Fanglomerate</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Bajada — INCORRECT:</b> Bajada is a geomorphic depositional surface (a compound alluvial fan apron), not a consolidated rock type.</li>
          <li><b>(B) Agglomerate — INCORRECT:</b> Agglomerate is an igneous pyroclastic rock formed of volcanic bombs, not alluvial sediment.</li>
          <li><b>(C) Fanglomerate — CORRECT:</b> The classical, authoritative sedimentary rock designation for consolidated alluvial fan deposits.</li>
          <li><b>(D) Orthoconglomerate — INCORRECT:</b> Orthoconglomerates are stream-deposited, clast-supported conglomerates with minimal matrix, not debris-flow dominated fan facies.</li>
        </ul>
        """,
        "part3": """
        <h3>Sedimentology Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 9: Paraconglomerate vs. Orthoconglomerate</div>
          <p>How does a fanglomerate deposited by an alluvial fan debris flow classify under Pettijohn's matrix-clast fabric scheme?</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>It classifies as a <b>Paraconglomerate</b> (matrix-supported conglomerate, $> 15\\%$ matrix), because laminar debris flow slurries transport boulders suspended within a cohesive mud-sand-water matrix.</p>
          </div>
        </div>
        """
    },
    10: {
        "title": "Q10: Hogback vs. Cuesta vs. Mesa Morphometrics in Dipping Strata",
        "part1": """
        <h3>10.1 Structural Control on Ridge Topography</h3>
        <p>In structural geomorphology (K.M. Bangar, <i>Principles of Engineering Geology</i>, Ch. 8; Fossen, <i>Structural Geology</i>; G.B. Mahapatra, Ch. 4), differential erosion of sedimentary strata with varying dip angles produces three diagnostic landform types:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Landform</th>
                <th>Strata Dip Angle ($\\theta$)</th>
                <th>Slope Morphology & Symmetry</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Hogback</b></td>
                <td><b>Steeply dipping: $\\theta > 30^\\circ - 45^\\circ$ (up to vertical)</b></td>
                <td><b>Symmetrical or near-symmetrical</b>: Narrow, sharp crest with <b>steep slopes of nearly equal inclination on both flanks</b> (dip slope $\\approx$ scarp slope).</td>
              </tr>
              <tr>
                <td><b>Cuesta</b></td>
                <td>Gently dipping: $\\theta < 20^\\circ$ (typically $5^\\circ - 15^\\circ$)</td>
                <td><b>Asymmetrical</b>: Gentle dip slope (concordant with strata) and an abrupt, steep escarpment/scarp slope on the opposite flank.</td>
              </tr>
              <tr>
                <td><b>Mesa</b></td>
                <td>Horizontal / Flat-lying: $\\theta \\approx 0^\\circ$</td>
                <td>Flat tableland capped by a horizontal resistant stratum with steep perimeter cliffs.</td>
              </tr>
              <tr>
                <td><b>Butte</b></td>
                <td>Horizontal / Flat-lying: $\\theta \\approx 0^\\circ$</td>
                <td>Isolated steep-sided pinnacled hill, narrower than a mesa (width is less than height).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>10.2 Geometric Proof of Slope Symmetry</h3>
        <p>When strata dip gently (Cuesta, $\\theta \\approx 10^\\circ$), the dip slope is bounded by the dip angle ($10^\\circ$), while the opposite scarp slope erodes along joint-controlled near-vertical cliff faces ($> 60^\\circ$).</p>
        <p>When strata dip steeply (Hogback, $\\theta \\approx 45^\\circ - 60^\\circ$), the dip slope angle becomes equal to or steeper than the natural angle of repose of the talus, causing both the dip flank and the scarp flank to exhibit steep, nearly equal slope inclinations.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Hogback</b> — A narrow, steep ridge with slopes of nearly equal inclination on both flanks created by differential erosion of steeply dipping strata is a <b>Hogback</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Cuesta — INCORRECT:</b> A cuesta is distinctly asymmetrical, possessing a gentle dip slope on one side and a steep escarpment on the other.</li>
          <li><b>(B) Hogback — CORRECT:</b> Precisely matches the morphological definition: steep inclination of nearly equal angles on both flanks due to steep structural dip.</li>
          <li><b>(C) Mesa — INCORRECT:</b> A mesa is a broad, flat-topped tableland formed on horizontal beds.</li>
          <li><b>(D) Butte — INCORRECT:</b> A butte is a smaller, pillar-like remnant of a mesa formed on horizontal beds.</li>
        </ul>
        """,
        "part3": """
        <h3>Worked Geomorphology Comparison</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 10: Structural Transition Cuesta to Hogback</div>
          <p>Explain how the landscape changes as one traverses from the gentle foreland flank towards the core of an asymmetrical mountain fold where bed dips increase from $8^\\circ$ to $55^\\circ$.</p>
          <div class="a-box">
            <p><b>Answer:</b></p>
            <p>At $8^\\circ$ dip, the landscape displays broad, sweeping <b>Cuestas</b> with extensive gentle dip slopes. As the beds steepen towards $55^\\circ$ near the fold hinge, the cuestas compress into sharp, knife-edge, symmetrical <b>Hogbacks</b> with near-equal steep slopes on both flanks.</p>
          </div>
        </div>
        """
    }
}

# Template for standalone HTML solution guide
html_guide_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | OPSC Geology 2021 Masterclass</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background: #f1f5f9;
    color: #0f172a;
    line-height: 1.65;
    padding: 24px 16px;
  }}
  .page {{ max-width: 960px; margin: 0 auto; }}
  
  @page {{ size: A4; margin: 14mm; }}
  @media print {{
    body {{ background: #fff; padding: 0; }}
    .no-print {{ display: none !important; }}
    .part-banner {{ break-before: page; }}
    .first-part {{ break-before: avoid !important; }}
  }}
  
  .header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: #fff;
    border-radius: 12px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  }}
  .badge {{
    display: inline-block;
    background: #0284c7;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    border-radius: 4px;
    padding: 4px 10px;
    margin-bottom: 12px;
  }}
  .header h1 {{ font-size: 23px; font-weight: 800; line-height: 1.35; }}
  .header .meta {{ font-size: 13.5px; color: #94a3b8; margin-top: 10px; }}
  
  .back-nav {{
    margin-bottom: 16px;
  }}
  .back-link {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #0284c7;
    text-decoration: none;
    font-size: 13.5px;
    font-weight: 600;
  }}
  .back-link:hover {{ text-decoration: underline; }}

  .part-banner {{
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    color: #fff;
    border-radius: 10px;
    padding: 16px 24px;
    margin: 28px 0 20px 0;
    box-shadow: 0 3px 10px rgba(37, 99, 235, 0.2);
  }}
  .part-banner.green {{
    background: linear-gradient(135deg, #065f46 0%, #059669 100%);
    box-shadow: 0 3px 10px rgba(5, 150, 105, 0.2);
  }}
  .part-banner.purple {{
    background: linear-gradient(135deg, #581c87 0%, #7c3aed 100%);
    box-shadow: 0 3px 10px rgba(124, 58, 237, 0.2);
  }}
  .part-banner h2 {{ font-size: 18px; font-weight: 700; }}
  
  .content-card {{
    background: #fff;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
    padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 20px;
  }}
  .content-card h3 {{ font-size: 17px; font-weight: 700; color: #1e293b; margin: 18px 0 10px 0; }}
  .content-card p {{ margin-bottom: 12px; font-size: 14.5px; color: #334155; }}
  .content-card ul {{ margin: 10px 0 16px 24px; font-size: 14.5px; color: #334155; }}
  .content-card li {{ margin-bottom: 8px; }}

  .q-box {{
    background: #f8fafc;
    border-left: 4px solid #0284c7;
    border-radius: 0 8px 8px 0;
    padding: 18px 22px;
    margin-bottom: 20px;
  }}
  .q-stmt {{ font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 14px; line-height: 1.5; }}
  .options-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }}
  .opt-item {{
    background: #fff;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 14px;
    font-weight: 500;
  }}
  .opt-item.correct {{
    background: #f0fdf4;
    border-color: #16a34a;
    color: #15803d;
    font-weight: 700;
  }}
  
  .verified-box {{
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-left: 5px solid #10b981;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 18px 0;
  }}
  .v-badge {{
    display: inline-block;
    background: #10b981;
    color: #fff;
    font-size: 11.5px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 8px;
  }}
  
  .table-wrap {{ overflow-x: auto; margin: 16px 0; }}
  .spec-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    text-align: left;
  }}
  .spec-table th {{
    background: #0f172a;
    color: #fff;
    padding: 10px 14px;
    font-weight: 600;
  }}
  .spec-table td {{
    padding: 10px 14px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }}
  .spec-table tr:nth-child(even) td {{ background: #f8fafc; }}

  .qa-card {{
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    border-radius: 8px;
    padding: 18px 22px;
    margin-bottom: 16px;
  }}
  .q-title {{ font-size: 15px; font-weight: 700; color: #6b21a8; margin-bottom: 8px; }}
  .a-box {{
    background: #fff;
    border-left: 3px solid #7c3aed;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin-top: 10px;
    font-size: 14px;
  }}

  /* ── Figure Styles ── */
  .tb-figure {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 14px;
    margin: 20px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    page-break-inside: avoid;
    break-inside: avoid;
  }}
  .tb-figure img {{
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    display: block;
    margin: 0 auto 12px auto;
  }}
  .tb-figure figcaption {{
    font-size: 13px;
    color: #475569;
    line-height: 1.5;
    text-align: justify;
    padding: 8px 12px;
    background: #f8fafc;
    border-radius: 6px;
    border-top: 1px solid #e2e8f0;
  }}
  .tb-figure figcaption strong {{ color: #0f172a; font-weight: 700; }}
</style>
</head>
<body>
<div class="page">
  <div class="back-nav no-print">
    <a href="../../index.html" class="back-link">← Back to Odisha Master Portal</a>
  </div>
  
  <div class="header">
    <div class="badge">{paper_code} • {section}</div>
    <h1>{title}</h1>
    <div class="meta">
      <strong>Exam:</strong> {paper_name} &nbsp;|&nbsp; 
      <strong>Authoritative Reference:</strong> {textbook_ref}
    </div>
  </div>

  <!-- PART I -->
  <div class="part-banner first-part">
    <h2>Part I: Theoretical Foundation & Concept Masterclass</h2>
  </div>
  <div class="content-card">
    {part1}
  </div>

  <!-- PART II -->
  <div class="part-banner green">
    <h2>Part II: Official Question & Critical Option Dissection</h2>
  </div>
  <div class="content-card">
    <div class="q-box">
      <div class="q-stmt">Q{q}. {question_stmt}</div>
      <div class="options-grid">
        <div class="opt-item {opt_a_cls}"><strong>(A)</strong> {opt_a}</div>
        <div class="opt-item {opt_b_cls}"><strong>(B)</strong> {opt_b}</div>
        <div class="opt-item {opt_c_cls}"><strong>(C)</strong> {opt_c}</div>
        <div class="opt-item {opt_d_cls}"><strong>(D)</strong> {opt_d}</div>
      </div>
    </div>
    {part2}
  </div>

  <!-- PART III -->
  <div class="part-banner purple">
    <h2>Part III: Synthesis Reference Tables & High-Yield Practice</h2>
  </div>
  <div class="content-card">
    {part3}
  </div>
</div>
</body>
</html>
"""

# Generate standalone guides for Q1-Q10
for q_meta in questions:
    q_num = q_meta['q']
    if q_num in guides:
        g = guides[q_num]
        opt = q_meta['options']
        corr = q_meta['correct_option']
        html_content = html_guide_template.format(
            title=g['title'],
            paper_code=q_meta['paper_code'],
            section=q_meta['section'],
            paper_name=q_meta['paper_name'],
            textbook_ref=q_meta['textbook_ref'],
            part1=g['part1'],
            q=q_num,
            question_stmt=q_meta['question'],
            opt_a=opt['A'],
            opt_b=opt['B'],
            opt_c=opt['C'],
            opt_d=opt['D'],
            opt_a_cls='correct' if corr == 'A' else '',
            opt_b_cls='correct' if corr == 'B' else '',
            opt_c_cls='correct' if corr == 'C' else '',
            opt_d_cls='correct' if corr == 'D' else '',
            part2=g['part2'],
            part3=g['part3']
        )
        file_path = os.path.join('/home/tapaswi/Mines_Geology/Orrisa_geology', q_meta['file_html'])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as out_f:
            out_f.write(html_content)
        print(f"Generated standalone guide: {q_meta['file_html']}")

print("All standalone guides built successfully!")
