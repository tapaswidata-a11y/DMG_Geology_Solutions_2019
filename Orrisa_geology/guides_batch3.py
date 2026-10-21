# guides_batch3.py - Comprehensive 3-Tier Masterclasses for Q26-Q50
# OPSC Geology Paper-II (2021)

guides_batch3 = {
    26: {
        "title": "Q26: Graben, Horst & Continental Rift Valley Tectonics",
        "part1": """
        <h3>26.1 Extensional Fault Systems & Graben Geometry</h3>
        <p>In structural geology and tectonics (Van der Pluijm & Marshak, <i>Earth Structure</i>, 2nd Ed., Ch. 16; Haakon Fossen, <i>Structural Geology</i>, 2nd Ed., Ch. 17), crustal extension produces conjugate pairs of <b>normal faults</b>. When regional tensional stress (where maximum principal stress $\\sigma_1$ is vertical and minimum principal stress $\\sigma_3$ is horizontal) acts on brittle lithosphere, characteristic fault-block morphologies develop:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Morphotectonic Feature</th>
                <th>Kinematic & Geometric Definition</th>
                <th>Structural Displacement</th>
                <th>Global & Indian Examples</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Graben (Rift Valley)</b></td>
                <td>A depressed, elongate crustal valley bounded on both flanks by <b>inward-dipping conjugate normal faults</b>.</td>
                <td><b>Downthrown central block (hanging wall of both faults)</b> relative to flanks.</td>
                <td>East African Rift, Rhine Graben, Narmada-Tapi Rift (SONATA).</td>
              </tr>
              <tr>
                <td><b>Horst</b></td>
                <td>An elevated, elongate crustal ridge bounded by <b>outward-dipping normal faults</b>.</td>
                <td><b>Upthrown central block (footwall of both faults)</b> relative to flanking grabens.</td>
                <td>Vosges and Black Forest (flanking Rhine Graben), Satpura Range.</td>
              </tr>
              <tr>
                <td><b>Half-Graben</b></td>
                <td>An asymmetric depression tilted towards a single major <b>master listric border fault</b>.</td>
                <td>Hanging-wall block undergoes rollover anticlinal deformation and tilt.</td>
                <td>Basin and Range Province, East African lake basins.</td>
              </tr>
              <tr>
                <td><b>Fault Escarpment</b></td>
                <td>A steep topographic scarp formed directly by differential vertical slip on a single fault plane.</td>
                <td>Linear step in topography along a single fault trace.</td>
                <td>Wasatch fault scarp (Utah).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>26.2 Continental Rifting & Lithospheric Attenuation Mechanics</h3>
        <p>Active and passive rifting mechanisms lead to lithospheric thinning ($\beta$-factor, McKenzie 1978):</p>
        $$\beta = \frac{t_0}{t_1}$$
        <p>Where $t_0$ is initial crustal thickness and $t_1$ is thinned post-rift thickness. Subsidence of the central graben floor is accommodated initially by fault-controlled mechanical crustal stretching (syn-rift phase), followed by regional thermal cooling subsidence (post-rift sag phase).</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Graben</b> — A valley formed by the downward displacement of a crustal block bounded on either side by normal faults is universally designated in structural geology as a <b>Graben</b> (or <b>Rift Valley</b>).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Nappe — INCORRECT:</b> A nappe is a massive, allochthonous rock sheet or recumbent fold that has moved tens to hundreds of kilometers horizontally along a low-angle thrust fault in a contractional orogen (e.g., Swiss Alps or Himalayas), entirely unrelated to extensional downthrown valleys.</li>
          <li><b>(B) Fault escarpment — INCORRECT:</b> A fault escarpment is simply the cliff-like surface slope formed by vertical offset along an individual fault plane; it is not a fault-bounded downthrown valley.</li>
          <li><b>(C) Graben — CORRECT:</b> From the German word for \"ditch\" or \"trench\", a graben is defined precisely as an elongate valley formed by the downward subsidence of a central block bounded by normal faults.</li>
          <li><b>(D) All of these — INCORRECT:</b> Erroneous combination of contractional (nappe), geomorphic (escarpment), and extensional graben terms.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Concept Check & Numerical Application</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 26: Graben Subsidence from Conjugate Normal Faulting</div>
          <p>A symmetrical continental graben is bounded by two conjugate planar normal faults each dipping at $\\delta = 60^\\circ$. If horizontal crustal extension produces a net heave of $H = 2.4\\text{ km}$ across the basin ($1.2\\text{ km}$ heave per fault), calculate the vertical structural throw (subsidence of the graben floor) accommodated by each fault.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>For a planar normal fault with dip angle $\\delta$, the relationship between vertical throw ($T$) and horizontal heave ($H_f$) is:</p>
            $$T = H_f \\times \\tan(\\delta)$$
            <p>Given $H_f = 1.2\\text{ km}$ and $\\delta = 60^\\circ$ ($\tan 60^\\circ = \\sqrt{3} \\approx 1.732$):</p>
            $$T = 1.2 \\times 1.732 = 2.08\\text{ km}$$
            <p>Thus, each border fault accommodates approximately $2.08\\text{ km}$ of vertical graben subsidence.</p>
          </div>
        </div>
        """
    },

    27: {
        "title": "Q27: Plunge of Linear Structural Features & Coordinate Geometry",
        "part1": """
        <h3>27.1 Spatial Definition of Linear Structural Elements</h3>
        <p>In structural geology (Billings, <i>Structural Geology</i>, 3rd Ed., Ch. 3; Haakon Fossen, <i>Structural Geology</i>, Ch. 2; Van der Pluijm & Marshak, Ch. 1), the spatial orientation of any linear geological feature (fold hinge lines, mineral elongation lineations, intersection lineations, slickenlines) is defined in 3D Euclidean space by two fundamental angles:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Coordinate Element</th>
                <th>Angular Definition</th>
                <th>Measurement Plane & Reference</th>
                <th>Angular Bounds</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Plunge ($\\alpha$)</b></td>
                <td><b>The vertical angle between the horizontal plane and the line of maximum elongation of the feature.</b></td>
                <td>Measured strictly downward in the <b>vertical plane</b> passing through the lineation.</td>
                <td>$0^\\circ \\le \\alpha \\le 90^\\circ$</td>
              </tr>
              <tr>
                <td><b>Trend ($\\beta$)</b></td>
                <td>The geographic compass bearing / azimuth of the horizontal projection of the plunging lineation.</td>
                <td>Measured clockwise from True North in the <b>horizontal plane</b>.</td>
                <td>$000^\\circ \\le \\beta < 360^\\circ$</td>
              </tr>
              <tr>
                <td><b>Pitch / Rake ($\\phi$)</b></td>
                <td>The angle between the linear feature and the strike line of the inclined plane on which it lies.</td>
                <td>Measured within the <b>inclined plane</b> containing the feature.</td>
                <td>$0^\\circ \\le \\phi \\le 90^\\circ$</td>
              </tr>
              <tr>
                <td><b>Dip Angle ($\\delta$)</b></td>
                <td>The maximum angle of inclination of a <i>planar surface</i> measured relative to the horizontal.</td>
                <td>Measured in a vertical plane perpendicular to strike.</td>
                <td>$0^\\circ \\le \\delta \\le 90^\\circ$</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>27.2 Stereographic Projection & Lineation Notation</h3>
        <p>A plunging lineation is recorded in standard structural notation as <code>Plunge → Trend</code> (e.g., $34^\\circ \\to 210^\\circ$). The fundamental spherical trigonometry equation linking plunge ($\\alpha$), pitch ($\\phi$), and plane dip ($\\delta$) is:</p>
        $$\\sin(\\alpha) = \\sin(\\delta) \\times \\sin(\\phi)$$
        <p><i>Note on Exam Paper Nuance:</i> In the official OPSC 2021 Question Paper, Question 27 repeats verbatim the question statement of Question 22. In both instances, the vertical angle between the horizontal plane and the axis/line of maximum elongation is strictly <b>plunge</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) plunge</b> — The vertical angle between the horizontal plane and the axis or line of maximum elongation of a structural feature is defined as <b>plunge</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) dip angle — INCORRECT:</b> Dip angle applies exclusively to <i>planar</i> surfaces (e.g., bedding planes, fault surfaces, foliation), representing the angle of inclination of the plane relative to the horizontal.</li>
          <li><b>(B) strike — INCORRECT:</b> Strike is the compass direction of a horizontal line formed by the intersection of an inclined planar feature with the horizontal plane ($000^\\circ$–$360^\\circ$).</li>
          <li><b>(C) right-lateral strike slip — INCORRECT:</b> A kinematic sense of fault motion (dextral) where the opposite block moves to the observer's right, having no angular coordinate meaning.</li>
          <li><b>(D) plunge — CORRECT:</b> Precisely defines the vertical inclination of a linear element measured downward from the horizontal plane.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Coordinate Conversion & Numerical Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 27: Pitch to Plunge Trigonometric Conversion</div>
          <p>A mineral stretching lineation lies on a fault plane dipping at $\\delta = 60^\\circ$. If the pitch (rake) of the lineation measured on the fault plane is $\\phi = 30^\\circ$, calculate the true plunge ($\\alpha$) of the lineation.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>Using the spherical kinematic relation:</p>
            $$\\sin(\\alpha) = \\sin(\\delta) \\times \\sin(\\phi)$$
            $$\\sin(\\alpha) = \\sin(60^\\circ) \\times \\sin(30^\\circ) = \\frac{\\sqrt{3}}{2} \\times \\frac{1}{2} = \\frac{1.732}{4} = 0.433$$
            $$\\alpha = \\arcsin(0.433) \\approx 25.66^\\circ$$
            <p>The true plunge of the mineral lineation is approximately $25.7^\\circ$.</p>
          </div>
        </div>
        """
    },

    28: {
        "title": "Q28: Fault Classification & Slip Kinematics (Dip-Slip vs. Strike-Slip)",
        "part1": """
        <h3>28.1 Kinematic Classification of Faults Based on Net Slip Vector</h3>
        <p>In structural geology and geomechanics (Van der Pluijm & Marshak, Ch. 16; Fossen, Ch. 8; Bangar, <i>Principles of Engineering Geology</i>, Ch. 8), faults are fractures along which measurable relative displacement has occurred parallel to the fracture surface. The classification depends on the orientation of the <b>net slip vector</b> relative to the strike and dip of the fault plane:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Fault Class</th>
                <th>Slip Vector Orientation</th>
                <th>Rake / Pitch on Fault</th>
                <th>Kinematic Sub-types</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Dip-Slip Fault</b></td>
                <td><b>Movement is parallel to the dip direction of the fault surface</b> (strictly up or down the dip).</td>
                <td><b>$\\text{Rake } \\approx 90^\\circ$</b></td>
                <td><b>Normal Fault</b> (hanging wall moves down; extension)<br><b>Reverse / Thrust Fault</b> (hanging wall moves up; contraction)</td>
              </tr>
              <tr>
                <td><b>Strike-Slip Fault (Transcurrent / Wrench)</b></td>
                <td>Movement is parallel to the horizontal strike line of the fault plane.</td>
                <td>$\\text{Rake } \\approx 0^\\circ$ or $180^\\circ$</td>
                <td><b>Sinistral</b> (left-lateral)<br><b>Dextral</b> (right-lateral)</td>
              </tr>
              <tr>
                <td><b>Oblique-Slip Fault</b></td>
                <td>Movement has significant components of both strike-slip and dip-slip.</td>
                <td>Intermediate rake ($10^\\circ < \\phi < 80^\\circ$)</td>
                <td>Transtensional (normal + strike-slip)<br>Transpressional (reverse + strike-slip)</td>
              </tr>
              <tr>
                <td><b>Step Fault</b></td>
                <td>A geometric series of parallel normal faults stepping down in the same direction.</td>
                <td>Dip-slip arrangement</td>
                <td>Structural terrace / staircase graben boundary</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>28.2 Components of Fault Displacement Vector</h3>
        <p>In 3D Cartesian coordinates on the fault surface, net slip ($S_{\\text{net}}$) is resolved into:</p>
        $$S_{\\text{net}}^2 = S_{\\text{strike}}^2 + S_{\\text{dip}}^2$$
        <p>Where pure dip-slip occurs, $S_{\\text{strike}} = 0$ and $S_{\\text{net}} = S_{\\text{dip}}$. The vertical component of dip slip is termed the <b>throw</b> ($T = S_{\\text{dip}} \\sin\\delta$), and the horizontal component perpendicular to strike is termed the <b>heave</b> ($H = S_{\\text{dip}} \\cos\\delta$).</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Dip-slip fault</b> — A fault in which the relative movement of the blocks is parallel to the dip of the fault surface is unequivocally designated as a <b>Dip-slip fault</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Step fault — INCORRECT:</b> Step faulting refers to a structural arrangement or pattern of multiple parallel faults downthrown in steps in the same direction, not the kinematic definition of motion along the dip.</li>
          <li><b>(B) Dip-slip fault — CORRECT:</b> Standard textbook definition: relative movement parallel to the true dip direction of the fault surface. Includes both normal and reverse/thrust faults.</li>
          <li><b>(C) Strike-slip fault — INCORRECT:</b> Motion is parallel to the horizontal strike line of the fault plane, with zero or negligible vertical dip-slip displacement.</li>
          <li><b>(D) None of these — INCORRECT:</b> Option (B) is the universally recognized correct term.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Fault Kinematics & Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 28: Resolving Net Slip and Rake Angle</div>
          <p>A slickensided fault plane has an observed strike-slip component of $S_s = 60\\text{ m}$ and a dip-slip component of $S_d = 80\\text{ m}$. Calculate the net slip ($S_{\\text{net}}$) and the rake angle ($\\phi$) of the movement vector on the fault surface.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The net slip magnitude is given by the Pythagorean theorem on the fault plane:</p>
            $$S_{\\text{net}} = \\sqrt{S_s^2 + S_d^2} = \\sqrt{60^2 + 80^2} = \\sqrt{3600 + 6400} = \\sqrt{10000} = 100\\text{ m}$$
            <p>2. The rake angle ($\\phi$) measured from the strike line is:</p>
            $$\\tan(\\phi) = \\frac{S_d}{S_s} = \\frac{80}{60} = 1.3333$$
            $$\\phi = \\arctan(1.3333) \\approx 53.13^\\circ$$
            <p>Because the rake angle is $53.1^\\circ$, this is classified as an <b>oblique-slip fault</b> (transpressional or transtensional depending on whether $S_d$ is reverse or normal).</p>
          </div>
        </div>
        """
    },

    29: {
        "title": "Q29: Stratigraphic Unconformities: Disconformity vs. Paraconformity",
        "part1": """
        <h3>29.1 Boggs Classification of Stratigraphic Unconformities</h3>
        <p>In stratigraphy and physical geology (Sam Boggs Jr., <i>Principles of Sedimentology and Stratigraphy</i>, 5th Ed., Ch. 14; Dunbar & Rodgers, 1957; Bangar, Ch. 9), an <b>unconformity</b> is a substantial break or gap in the geologic rock record resulting from a period of non-deposition and/or erosion. The four canonical types are distinguished by geometric relationships and basement lithology:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Unconformity Type</th>
                <th>Geometric Bedding Relation</th>
                <th>Physical Boundary Characteristics</th>
                <th>Diagnostic Evidence</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Disconformity</b></td>
                <td><b>Beds above and below the unconformity are strictly parallel</b> ($S_1 \\parallel S_2$).</td>
                <td><b>Visible, irregular, undulating erosional surface</b> (paleo-channels, paleosols, karst relief, basal gravels).</td>
                <td>Identified physically by erosional relief despite parallel structural attitude.</td>
              </tr>
              <tr>
                <td><b>Paraconformity</b></td>
                <td>Beds above and below are parallel.</td>
                <td><b>Completely flat, planar contact with no visible erosional relief</b>; looks like a normal bedding plane.</td>
                <td>Can <i>only</i> be identified biostratigraphically (missing biozones) or chronostratigraphically.</td>
              </tr>
              <tr>
                <td><b>Angular Unconformity</b></td>
                <td>Younger strata overlie tilted, folded, or deformed older strata at an angular discordance.</td>
                <td>Structural discordance where underlying beds are truncated by younger horizontal strata.</td>
                <td>Classic Hutton's unconformity at Siccar Point; clear tectonic tilting prior to erosion.</td>
              </tr>
              <tr>
                <td><b>Nonconformity</b></td>
                <td>Sedimentary strata overlie unstratified, eroded plutonic igneous (granite) or metamorphic basement rocks.</td>
                <td>Erosional contact on crystalline basement; lacks contact metamorphism in upper strata.</td>
                <td>Great Eparchean Unconformity (e.g., Cuddapah or Vindhyan over Archean granite/gneiss).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>29.2 Chronostratigraphic Significance: The Hiatus & Vacuity</h3>
        <p>The time interval represented by an unconformity is termed the <b>hiatus</b>, which comprises the erosional vacuity (time represented by eroded rocks) plus the non-depositional interval. In a disconformity, the parallelism indicates epeirogenic regional uplift and emergence without crustal orogenic tilting.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) Disconformity</b> — An unconformity in which the sedimentary beds above and below are structurally parallel and separated by a visible erosional boundary is designated as a <b>Disconformity</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Parallel unconformity — INCORRECT:</b> Informal or non-standard descriptive phrase; the rigorous academic term standardized by Dunbar & Rodgers and Sam Boggs Jr. is <i>disconformity</i>.</li>
          <li><b>(B) Discontinuity — INCORRECT:</b> Generic mechanical term representing any break or joint plane in a rock mass (used in engineering rock mechanics, e.g., ISRM standards), not a specific stratigraphic unconformity.</li>
          <li><b>(C) Non-conformity — INCORRECT:</b> A nonconformity specifically requires that sedimentary strata overlie older eroded <i>plutonic igneous or metamorphic crystalline rocks</i>, not stratified sedimentary beds.</li>
          <li><b>(D) Disconformity — CORRECT:</b> The exact, formal stratigraphic term for an erosional gap between parallel sedimentary strata.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Stratigraphic Synthesis & Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 29: Distinguishing Disconformity from Paraconformity</div>
          <p>Two horizontal limestone units are in direct contact. Unit A (below) contains Lower Devonian spiriferid brachiopods, while Unit B (above) contains Upper Mississippian goniatites. The contact surface shows $1.5\\text{ m}$ deep incised paleo-karst potholes filled with chert lag gravel. Classify this unconformity and estimate the missing temporal interval.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. <b>Classification:</b> Because the beds above and below are structurally parallel (horizontal), and the contact exhibits prominent, undulating erosional topography (incised paleokarst potholes and chert lag gravels), the contact is definitively a <b>Disconformity</b> (if the contact were a perfectly flat, featureless bedding plane, it would be a paraconformity).</p>
            <p>2. <b>Temporal Hiatus:</b> The hiatus spans the Middle Devonian, Late Devonian, and Early Mississippian epochs (approximately $\\sim 393\\text{ Ma}$ to $\\sim 330\\text{ Ma} = \\approx 63\\text{ million years}$ of missing rock record).</p>
          </div>
        </div>
        """
    },

    30: {
        "title": "Q30: Cartographic Representative Fraction (RF) & Geological Map Scaling",
        "part1": """
        <h3>30.1 Principles of Representative Fraction (RF) in Topographic & Geological Maps</h3>
        <p>In cartography, surveying, and field geology (Compton, <i>Manual of Field Geology</i>; Bangar, <i>Principles of Engineering Geology</i>, Ch. 1), the scale of a map defines the proportional ratio between a distance measured on the map and the corresponding horizontal distance measured on the ground:</p>
        $$\\text{Scale} = \\frac{\\text{Map Distance } (d_m)}{\\text{Ground Distance } (D_g)}$$
        <p>When expressed as a <b>Representative Fraction (RF)</b>:</p>
        $$\\text{RF} = \\frac{1}{M}$$
        <p>Where $M$ is the scale denominator (scale factor). Crucially, RF is a dimensionless ratio; both $d_m$ and $D_g$ must be expressed in identical metric units:</p>
        $$D_g = d_m \\times M$$

        <h3>30.2 Metric Unit Scaling Conversions</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Standard Survey of India (SOI) Scale</th>
                <th>RF Equivalent</th>
                <th>Ground Distance for $1\\text{ cm}$ on Map</th>
                <th>Application Domain</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>$1\\text{ cm} = 2.5\\text{ km}$</td>
                <td>$1 : 250,000$</td>
                <td>$2,500\\text{ m}$ ($2.5\\text{ km}$)</td>
                <td>Regional tectonic synoptic sheets</td>
              </tr>
              <tr>
                <td>$1\\text{ cm} = 500\\text{ m}$</td>
                <td>$1 : 50,000$</td>
                <td>$500\\text{ m}$ ($0.5\\text{ km}$)</td>
                <td>Standard SOI Toposheets</td>
              </tr>
              <tr>
                <td><b>$1\\text{ cm} = 250\\text{ m}$</b></td>
                <td><b>$1 : 25,000$</b></td>
                <td><b>$250\\text{ m}$</b></td>
                <td><b>High-resolution mineral exploration & engineering geology maps</b></td>
              </tr>
              <tr>
                <td>$1\\text{ cm} = 100\\text{ m}$</td>
                <td>$1 : 10,000$</td>
                <td>$100\\text{ m}$</td>
                <td>Detailed mine working & pit design plans</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) 375 m</b> — On a $1:25,000$ scale map, $1.5\\text{ cm}$ measured on the map corresponds exactly to $1.5 \\times 25,000 = 37,500\\text{ cm} = \\mathbf{375\\text{ m}}$ on the ground.</p>
        </div>

        <h3>Step-by-Step Mathematical Derivation</h3>
        <p>1. Identify the Representative Fraction: $\\text{RF} = 1 : 25,000$. This implies $1\\text{ unit on map} = 25,000\\text{ units on ground}$.</p>
        <p>2. Calculate field ground distance in centimeters:</p>
        $$D_g = d_m \\times 25,000 = 1.5\\text{ cm} \\times 25,000 = 37,500\\text{ cm}$$
        <p>3. Convert centimeters to meters ($1\\text{ m} = 100\\text{ cm}$):</p>
        $$D_g = \\frac{37,500\\text{ cm}}{100\\text{ cm/m}} = \\mathbf{375\\text{ m}}$$

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 375 m — CORRECT:</b> Exact mathematical conversion: $37,500\\text{ cm} = 375\\text{ m}$.</li>
          <li><b>(B) 3750 km — INCORRECT:</b> Catastrophic unit conversion error by a factor of $10,000$ (representing $3,750,000\\text{ m}$).</li>
          <li><b>(C) 3750 cm — INCORRECT:</b> Off by an order of magnitude (would correspond to an RF of $1:2,500$).</li>
          <li><b>(D) 37500 mm — INCORRECT:</b> $37,500\\text{ mm} = 37.5\\text{ m}$, which is off by a factor of 10.</li>
        </ul>
        """,
        "part3": """
        <h3>Advanced Cartographic Scale Problems</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 30: Areal Scale & Open-Pit Mine Conversion</div>
          <p>An open-pit iron ore lease boundary covers an area of $8.0\\text{ cm}^2$ on a $1:25,000$ geological map. What is the actual ground surface area of the mining lease in square kilometers ($\text{km}^2$) and in hectares ($\text{ha}$)?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The areal scale is the square of the linear scale factor:</p>
            $$\\text{Area Ground} = \\text{Area Map} \\times M^2$$
            $$A_g = 8.0\\text{ cm}^2 \\times (25,000)^2 = 8.0 \\times 625,000,000\\text{ cm}^2 = 5,000,000,000\\text{ cm}^2$$
            <p>2. Convert to square meters ($1\\text{ m}^2 = 10,000\\text{ cm}^2$):</p>
            $$A_g = \\frac{5,000,000,000}{10,000} = 500,000\\text{ m}^2$$
            <p>3. Convert to square kilometers ($1\\text{ km}^2 = 1,000,000\\text{ m}^2$) and hectares ($1\\text{ ha} = 10,000\\text{ m}^2$):</p>
            $$A_g = \\frac{500,000}{1,000,000} = \\mathbf{0.50\\text{ km}^2} = \\mathbf{50.0\\text{ hectares}}$$
          </div>
        </div>
        """
    },

    31: {
        "title": "Q31: Apparent Dip vs. True Dip Trigonometric Nomography",
        "part1": """
        <h3>31.1 Geometric Derivation of Apparent Dip</h3>
        <p>In structural geology and underground mining (Billings, <i>Structural Geology</i>, Appendix B; Fossen, Ch. 2; Van der Pluijm & Marshak, Ch. 1), <b>true dip ($\\delta$)</b> is the maximum angle of inclination of a planar structure measured perpendicular to the strike line. In any other vertical cross-section oriented oblique to the true dip direction, the observed inclination is the <b>apparent dip ($\\delta'$)</b>, which is <i>always less than the true dip</i>:</p>
        $$\\delta' < \\delta \\quad (\\text{for any angle } \\alpha > 0^\\circ)$$
        <p>The universal trigonometric formula relating true dip ($\\delta$), apparent dip ($\\delta'$), and the angular deviation between their azimuth directions ($\\alpha$) is:</p>
        $$\\mathbf{\\tan(\\delta') = \\tan(\\delta) \\times \\cos(\\alpha)}$$
        <p>Where:</p>
        <ul>
          <li>$\\delta$ = True dip angle (measured in the direction of true dip).</li>
          <li>$\\delta'$ = Apparent dip angle (measured along an oblique vertical section).</li>
          <li>$\\alpha = |\\text{Azimuth}_{\\text{true dip}} - \\text{Azimuth}_{\\text{apparent dip}}|$ = Horizontal angle between the true dip bearing and the apparent dip bearing.</li>
        </ul>

        <h3>31.2 Critical Limiting Cases</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Bearing of Oblique Section Relative to True Dip</th>
                <th>Angular Offset ($\\alpha$)</th>
                <th>$\\cos(\\alpha)$</th>
                <th>Resulting Apparent Dip ($\\delta'$)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Parallel to True Dip Direction</td>
                <td>$\\alpha = 0^\\circ$</td>
                <td>$\\cos(0^\\circ) = 1.0$</td>
                <td>$\\tan\\delta' = \\tan\\delta \\implies \\mathbf{\\delta' = \\delta}$ (Maximum inclination)</td>
              </tr>
              <tr>
                <td>Oblique to True Dip Direction ($0^\\circ < \\alpha < 90^\\circ$)</td>
                <td>e.g. $\\alpha = 25^\\circ$</td>
                <td>$\\cos(25^\\circ) \\approx 0.906$</td>
                <td>$\\mathbf{\\delta' < \\delta}$ (Intermediate apparent dip)</td>
              </tr>
              <tr>
                <td>Parallel to Strike Direction</td>
                <td>$\\alpha = 90^\\circ$</td>
                <td>$\\cos(90^\\circ) = 0.0$</td>
                <td>$\\tan\\delta' = 0 \\implies \\mathbf{\\delta' = 0^\\circ}$ (Horizontal line)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) 45°</b> — Applying the apparent dip equation for a vein dipping $\\delta = 50^\\circ$ toward $\\text{N}45^\\circ\\text{W}$ when viewed toward $\\text{N}20^\\circ\\text{W}$ gives an angular offset $\\alpha = 25^\\circ$, yielding an apparent dip of $\\delta' \\approx 47.2^\\circ \\approx \\mathbf{45^\\circ}$.</p>
        </div>

        <h3>Step-by-Step Mathematical Calculation</h3>
        <p>1. Identify the given parameters:</p>
        <ul>
          <li>True dip angle: $\\delta = 50^\\circ$</li>
          <li>True dip direction: $\\text{N}45^\\circ\\text{W}$ ($315^\\circ$ azimuth)</li>
          <li>Apparent dip direction: $\\text{N}20^\\circ\\text{W}$ ($340^\\circ$ azimuth)</li>
        </ul>
        <p>2. Calculate horizontal angular difference $\\alpha$:</p>
        $$\\alpha = |45^\\circ - 20^\\circ| = 25^\\circ$$
        <p>3. Apply the nomographic apparent dip formula:</p>
        $$\\tan(\\delta') = \\tan(50^\\circ) \\times \\cos(25^\\circ)$$
        <p>Using standard trigonometric tables: $\\tan(50^\\circ) = 1.19175$, and $\\cos(25^\\circ) = 0.90631$:</p>
        $$\\tan(\\delta') = 1.19175 \\times 0.90631 = 1.08009$$
        $$\\delta' = \\arctan(1.08009) = 47.20^\\circ$$
        <p>4. Match with exam options: Among the choices ($65^\\circ, 60^\\circ, 0^\\circ, 45^\\circ$), the only physically possible and closest answer is <b>45°</b> (since apparent dip <i>must be less than true dip</i> $50^\\circ$, options A and B are impossible, while $0^\\circ$ is only along strike).</p>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 65° — IMPOSSIBLE:</b> Violates the fundamental geometric law of structural geology: apparent dip can NEVER exceed true dip ($\\delta' \\le \\delta$). A $50^\\circ$ vein cannot have an apparent dip of $65^\\circ$.</li>
          <li><b>(B) 60° — IMPOSSIBLE:</b> Exceeds true dip ($60^\\circ > 50^\\circ$); physically impossible.</li>
          <li><b>(C) 0° — INCORRECT:</b> Apparent dip is only $0^\\circ$ when viewed strictly parallel to strike (which would be $\\text{N}45^\\circ\\text{E}$ or $\\text{S}45^\\circ\\text{W}$), not $\\text{N}20^\\circ\\text{W}$.</li>
          <li><b>(D) 45° — CORRECT:</b> The only mathematically sound option consistent with $\\delta' = 47.2^\\circ \\approx 45^\\circ$ and satisfying $\\delta' < 50^\\circ$.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Mining Nomogram Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 31: Apparent Dip for Underground Cross-Cut Tunnel</div>
          <p>A coal seam has a true dip of $35^\\circ$ due South ($180^\\circ$). An underground haulage drift is driven along a bearing of $\\text{S}60^\\circ\\text{W}$ ($240^\\circ$). Calculate the apparent gradient (slope angle) of the coal seam along the wall of this haulage drift.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The angular difference between true dip direction ($180^\\circ$) and drift bearing ($240^\\circ$) is:</p>
            $$\\alpha = 240^\\circ - 180^\\circ = 60^\\circ$$
            <p>2. Calculate apparent dip using $\\tan(\\delta') = \\tan(\\delta) \\cos(\\alpha)$:</p>
            $$\\tan(\\delta') = \\tan(35^\\circ) \\times \\cos(60^\\circ) = 0.7002 \\times 0.5000 = 0.3501$$
            $$\\delta' = \\arctan(0.3501) \\approx 19.29^\\circ$$
            <p>The seam appears to dip at approximately $19.3^\\circ$ along the haulage drift.</p>
          </div>
        </div>
        """
    },

    32: {
        "title": "Q32: Himalayan Orogenic Wedge Tectonics (Contractional Folds & Thrust Faults)",
        "part1": """
        <h3>32.1 Tectonic Architecture of the India-Asia Collisional Orogen</h3>
        <p>In global tectonics and Indian geology (K.S. Valdiya, <i>The Making of India: Geodynamic Evolution</i>, Ch. 5; Gansser, 1964; Ramakrishnan & Vaidyanadhan, <i>Geology of India</i>, Vol. 2, Ch. 29), the Himalayan mountain belt represents the classic, archetypal active <b>continental collision zone</b> (Himalayan-Tibetan orogen). Driven by the ongoing northward indentation of the Indian plate into Eurasia at $\\sim 40 - 50\\text{ mm/yr}$, crustal shortening is accommodated by a massive foreland-propagating <b>fold-and-thrust belt</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Major Tectonic Boundary / Unit</th>
                <th>Structural Architecture</th>
                <th>Dominant Deformational Regime</th>
                <th>Lithotectonic Association</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Main Central Thrust (MCT)</b></td>
                <td>Ductile, high-angle shear zone transitioning into crustal ramp</td>
                <td><b>Contractional Thrusting + Overturned Folds</b></td>
                <td>High-grade Higher Himalayan Crystalline core over Lesser Himalaya.</td>
              </tr>
              <tr>
                <td><b>Main Boundary Thrust (MBT)</b></td>
                <td>Regional northward-dipping low-angle thrust fault</td>
                <td><b>Contractional Thrusting + Nappes</b></td>
                <td>Lesser Himalayan metasediments thrust over the Siwaliks.</td>
              </tr>
              <tr>
                <td><b>Main Frontal Thrust (MFT / HFT)</b></td>
                <td>Active southernmost frontal reverse fault</td>
                <td><b>Blind thrusts, Fault-bend folds, Fault-propagation folds</b></td>
                <td>Siwalik molasse thrust over active Indo-Gangetic alluvium.</td>
              </tr>
              <tr>
                <td><b>Sub-Himalayan Siwalik Belt</b></td>
                <td>Fold-thrust wedge</td>
                <td><b>Asymmetrical anticlines, synclines, & imbricate thrusts</b></td>
                <td>Neogene-Quaternary foreland synorogenic sediments.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>32.2 Why Normal Faults are Minor and Restricted</h3>
        <p>While the South Tibetan Detachment System (STDS) at the crest of the Higher Himalaya exhibits localized orogen-parallel extension due to gravitational collapse of over-thickened crust, the <b>overwhelming bulk of the deformed rocks across the length and breadth of the Himalayan belt forms folds and reverse/thrust faults</b> under regional horizontal compression ($\\sigma_1$ horizontal, $\\sigma_3$ vertical).</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Folds and reverse faults</b> — Regional crustal shortening in the Himalayan contractional collision orogen produces predominantly <b>folds and reverse (thrust) faults</b> throughout the belt.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Normal and reverse faults — INCORRECT:</b> Normal faults characterize extensional tectonic environments (rifts), whereas the Himalayas are an active compressional convergent orogen.</li>
          <li><b>(B) Folds and reverse faults — CORRECT:</b> The hallmark deformational structures of collisional mountain belts (MCT, MBT, MFT, and associated Siwalik and Lesser Himalayan fold-thrust nappes) are compressive folds and reverse/thrust faults.</li>
          <li><b>(C) Recumbent folds and normal faults — INCORRECT:</b> While recumbent folds occur locally in the crystalline nappes, normal faults are not the characteristic widespread deformation structure of the range.</li>
          <li><b>(D) All of these — INCORRECT:</b> Normal faults are not a primary characteristic of the general Himalayan deformation belt.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Orogenic Wedge Synthesis Table</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Tectonic Setting</th>
                <th>Stress Regime</th>
                <th>Dominant Structures</th>
                <th>Representative Global Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Continental Collision / Orogen</b></td>
                <td>$\\sigma_1$ horizontal, $\\sigma_3$ vertical</td>
                <td><b>Folds, Reverse Faults, Thrust Nappes</b></td>
                <td><b>Himalayas, Alps, Zagros, Appalachians</b></td>
              </tr>
              <tr>
                <td><b>Continental Rifting</b></td>
                <td>$\\sigma_1$ vertical, $\\sigma_3$ horizontal</td>
                <td>Normal Faults, Grabens, Tilted Blocks</td>
                <td>East African Rift, Basin & Range</td>
              </tr>
              <tr>
                <td><b>Transform Boundary</b></td>
                <td>$\\sigma_1, \\sigma_3$ horizontal</td>
                <td>Strike-slip faults, Flower structures</td>
                <td>San Andreas Fault, Dead Sea Transform</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    33: {
        "title": "Q33: Recumbent Fold Geometry & Axial Surface Inclination",
        "part1": """
        <h3>33.1 Fleuty's (1964) Classification of Folds by Axial Surface Dip</h3>
        <p>In structural geology (M.J. Fleuty, 1964, <i>The Description of Folds</i>; Haakon Fossen, <i>Structural Geology</i>, Ch. 11; Billings, Ch. 4; Bangar, Ch. 7), folds are rigorously categorized according to the inclination (dip angle $\\delta_{\\text{ap}}$) of their <b>axial surface (axial plane)</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Fold Category</th>
                <th>Dip of Axial Surface ($\\delta_{\\text{ap}}$)</th>
                <th>Limb Attitude & Structural Symmetry</th>
                <th>Geotectonic Significance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Upright Fold</b></td>
                <td>$\\delta_{\\text{ap}} = 80^\\circ - 90^\\circ$ (Vertical to Sub-vertical)</td>
                <td>Limbs dip symmetrically in opposite directions at equal angles.</td>
                <td>Mild to moderate horizontal compression.</td>
              </tr>
              <tr>
                <td><b>Steeply Inclined Fold</b></td>
                <td>$\\delta_{\\text{ap}} = 60^\\circ - 80^\\circ$</td>
                <td>Asymmetrical limbs dipping in opposite directions.</td>
                <td>Progressive asymmetric shear.</td>
              </tr>
              <tr>
                <td><b>Moderately Inclined Fold</b></td>
                <td>$\\delta_{\\text{ap}} = 30^\\circ - 60^\\circ$</td>
                <td>Asymmetrical limbs.</td>
                <td>Oblique contractional shortening.</td>
              </tr>
              <tr>
                <td><b>Gently Inclined Fold</b></td>
                <td>$\\delta_{\\text{ap}} = 10^\\circ - 30^\\circ$</td>
                <td>One limb normal, one limb overturned.</td>
                <td>Intense overthrust shear strain.</td>
              </tr>
              <tr>
                <td><b>Recumbent Fold</b></td>
                <td><b>$\\mathbf{\\delta_{\\text{ap}} = 0^\\circ - 10^\\circ}$ (Sub-horizontal to Horizontal, $\\approx 0^\\circ$)</b></td>
                <td><b>Axial plane is horizontal; the lower limb is completely overturned and inverted.</b></td>
                <td><b>Extreme ductile shear nappe transport in metamorphic cores.</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>33.2 Anatomy of a Recumbent Fold</h3>
        <p>In a true recumbent fold, the fold lies essentially on its side. It consists of:</p>
        <ul>
          <li><b>Upper Normal Limb (Digit):</b> Strata are in normal stratigraphic superposition (younger beds over older beds).</li>
          <li><b>Hinge Zone (Closure):</b> Point of maximum curvature where the axial surface trace is sub-horizontal.</li>
          <li><b>Lower Inverted Limb (Flank):</b> Strata are completely overturned (inverted, upside down; older beds over younger beds), often subjected to extreme ductile attenuation and shearing, eventually detaching along thrusts to generate <i>nappes</i>.</li>
        </ul>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) 0°</b> — In a recumbent fold, the defining structural criterion is that the axial plane dips sub-horizontally, essentially at <b>0°</b> ($\\le 10^\\circ$).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) 45° — INCORRECT:</b> An axial plane dipping at $45^\\circ$ defines an <i>inclined fold</i>, not a recumbent fold.</li>
          <li><b>(B) 90° — INCORRECT:</b> An axial plane dipping at $90^\\circ$ defines an <i>upright (vertical) fold</i>.</li>
          <li><b>(C) 60° — INCORRECT:</b> An axial plane dipping at $60^\\circ$ defines a <i>steeply inclined fold</i>.</li>
          <li><b>(D) 0° — CORRECT:</b> By universal academic definition (Fleuty 1964; Fossen; Billings), a recumbent fold is a fold whose axial surface is horizontal to sub-horizontal (dip $\\approx 0^\\circ$).</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Fold Anatomy Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 33: Identifying Facing and Vergence in Recumbent Nappes</div>
          <p>A geologist in the Lesser Himalayan Almora Nappe observes graded turbidite sandstone beds on the lower limb of a large recumbent fold whose axial surface dips at $4^\\circ\\text{ North}$. The coarse pebbles are found at the stratigraphic top of each bed while fine silts are at the bottom. What is the facing direction and structural status of this limb?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. In graded bedding, normal younging direction (facing) requires coarse grains at the bottom grading upward to fine grains at the top. Here, coarse pebbles are at the top, indicating that the strata are <b>stratigraphically inverted (overturned)</b>.</p>
            <p>2. In a recumbent fold with an axial surface dip of $4^\\circ \\approx 0^\\circ$, the lower limb is the <b>inverted / overturned limb</b>. Facing is directed downward, confirming classic recumbent nappe kinematics.</p>
          </div>
        </div>
        """
    },

    34: {
        "title": "Q34: Crustal Rheology & Brittle vs. Ductile Deformation Regimes",
        "part1": """
        <h3>34.1 Byerlee's Law & Frictional Failure in the Upper Crust</h3>
        <p>In structural geology, rock mechanics, and lithospheric dynamics (Byerlee, 1978; Sibson, 1977; Van der Pluijm & Marshak, Ch. 7; Fossen, Ch. 6), the deformation behavior of lithospheric rocks is governed by confining pressure ($P$), temperature ($T$), fluid pressure ($P_f$), and strain rate ($\\dot{\\varepsilon}$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Crustal Domain</th>
                <th>P-T Conditions & Typical Depth</th>
                <th>Dominant Deformation Mechanism</th>
                <th>Characteristic Microstructures & Structures</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Upper Crust</b></td>
                <td><b>Low Temperature ($T < 300^\\circ\\text{C}$) & Low Confining Pressure ($P < 300\\text{ MPa}$); Depth: $0 - 10\\text{–}15\\text{ km}$</b></td>
                <td><b>Brittle Process (Frictional Cataclasis & Fracture)</b></td>
                <td><b>Joints, Faults, Microcracking, Frictional Sliding (Byerlee's Law), Cataclasites, Fault Gouge, Pseudotachylytes.</b></td>
              </tr>
              <tr>
                <td><b>Brittle-Ductile Transition (BDT)</b></td>
                <td>$T \\approx 300^\\circ - 350^\\circ\\text{C}$, Depth $\\sim 10 - 15\\text{ km}$ in quartz-bearing continental crust</td>
                <td>Semi-brittle / Transitional</td>
                <td>Greenschist facies transition; onset of quartz crystal plasticity; peak crustal shear strength.</td>
              </tr>
              <tr>
                <td><b>Middle to Lower Crust</b></td>
                <td>High Temperature ($T > 350^\\circ - 500^\\circ\\text{C}$) & High Pressure; Depth $> 15\\text{ km}$</td>
                <td><b>Ductile / Plastic Process (Viscous Crystal Plasticity)</b></td>
                <td>Dislocation creep, dynamic recrystallization, mylonites, solid-state flow, ductile folds.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>34.2 Byerlee's Frictional Law</h3>
        <p>In the brittle upper crust, rock shear strength ($\\tau$) is pressure-dependent but almost entirely independent of rock type and temperature (Byerlee's Law):</p>
        $$\\tau = 0.85 \\sigma_n \\quad (\\text{for } \\sigma_n < 200\\text{ MPa})$$
        $$\\tau = 50\\text{ MPa} + 0.6 \\sigma_n \\quad (\\text{for } \\sigma_n > 200\\text{ MPa})$$
        <p>Because rocks fail along discrete fractures and slip planes under these low P-T conditions before any significant crystal-plastic flow can occur, deformation is overwhelmingly <b>brittle</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Brittle process</b> — In the upper crust where confining pressure and temperature are relatively low, deformation is dominated by <b>brittle processes</b> (fracturing, jointing, cataclasis, and faulting).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Brittle process — CORRECT:</b> Low temperature ($< 300^\\circ\\text{C}$) and low confining pressure in the upper $10\\text{–}15\\text{ km}$ prevent crystal-plastic flow, restricting deformation to elastic strain followed by brittle frictional failure.</li>
          <li><b>(B) Ductile-brittle process — INCORRECT:</b> Ductile-brittle behavior is restricted to the narrow transitional zone (BDT) at mid-crustal depths ($10\\text{–}15\\text{ km}$), not the general low P-T upper crust.</li>
          <li><b>(C) Plastic deformation — INCORRECT:</b> True plastic deformation (dislocation creep, diffusion flow) requires elevated temperatures ($T > 300^\\circ\\text{–}500^\\circ\\text{C}$) occurring exclusively in the middle and lower crust or mantle.</li>
          <li><b>(D) Both (A) and (B) are true — INCORRECT:</b> Brittle deformation is the singular dominant mechanism governing the upper crust.</li>
        </ul>
        """,
        "part3": """
        <h3>Crustal Rheology & Strength Envelope Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 34: Calculating Brittle Failure Stress at 5 km Depth</div>
          <p>Assuming an average upper continental crust density of $\\rho = 2700\\text{ kg/m}^3$ and hydrostatic pore water pressure with rock internal friction coefficient $\\mu = 0.85$, calculate the vertical lithostatic stress ($\\sigma_v$) at a depth of $z = 5.0\\text{ km}$ ($g = 9.8\\text{ m/s}^2$).</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The vertical overburden lithostatic stress is:</p>
            $$\\sigma_v = \\rho g z = 2700\\text{ kg/m}^3 \\times 9.8\\text{ m/s}^2 \\times 5000\\text{ m} = 132,300,000\\text{ Pa} = 132.3\\text{ MPa}$$
            <p>2. Hydrostatic pore fluid pressure at $5\\text{ km}$ ($\\rho_w = 1000\\text{ kg/m}^3$):</p>
            $$P_f = \\rho_w g z = 1000 \\times 9.8 \\times 5000 = 49.0\\text{ MPa}$$
            <p>3. Effective normal stress:</p>
            $$\\sigma_v' = \\sigma_v - P_f = 132.3 - 49.0 = 83.3\\text{ MPa}$$
            <p>Under Byerlee's law, shear stress required to cause fault slip is $\\tau = 0.85 \\times 83.3 \\approx 70.8\\text{ MPa}$. This frictional stress threshold dictates earthquake faulting throughout the brittle seismogenic zone.</p>
          </div>
        </div>
        """
    },

    35: {
        "title": "Q35: Anderson's Dynamic Theory of Faulting & Normal Fault Angles",
        "part1": """
        <h3>35.1 Anderson's (1905, 1951) Dynamic Theory of Faulting</h3>
        <p>In structural geology and geomechanics (E.M. Anderson, 1905, 1951, <i>The Dynamics of Faulting</i>; Fossen, Ch. 8; Van der Pluijm & Marshak, Ch. 16), the Earth's surface is a free boundary contact with the atmosphere, meaning it can support no shear stress. Consequently, <b>one of the three principal stress axes must be vertical, and the other two must lie in the horizontal plane</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Fault Regime</th>
                <th>Principal Stress Orientation</th>
                <th>Angle to $\\sigma_1$</th>
                <th>Theoretical Dip Angle (to Horizontal)</th>
                <th>Angle to Vertical</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Normal Fault</b></td>
                <td><b>$\\sigma_1$ is Vertical</b><br>$\\sigma_2, \\sigma_3$ are Horizontal</td>
                <td>$\\theta = 45^\\circ - \\frac{\\phi}{2}$ from $\\sigma_1$</td>
                <td><b>$\\delta = 45^\\circ + \\frac{\\phi}{2} \\approx \\mathbf{60^\\circ}$ to horizontal</b></td>
                <td><b>$\\mathbf{30^\\circ}$ to vertical</b></td>
              </tr>
              <tr>
                <td><b>Thrust / Reverse Fault</b></td>
                <td><b>$\\sigma_3$ is Vertical</b><br>$\\sigma_1, \\sigma_2$ are Horizontal</td>
                <td>$\\theta = 45^\\circ - \\frac{\\phi}{2}$ from $\\sigma_1$</td>
                <td><b>$\\delta = 45^\\circ - \\frac{\\phi}{2} \\approx \\mathbf{30^\\circ}$ to horizontal</b></td>
                <td><b>$60^\\circ$ to vertical</b></td>
              </tr>
              <tr>
                <td><b>Strike-Slip Fault</b></td>
                <td><b>$\\sigma_2$ is Vertical</b><br>$\\sigma_1, \\sigma_3$ are Horizontal</td>
                <td>$\\theta = 45^\\circ - \\frac{\\phi}{2}$ from $\\sigma_1$</td>
                <td><b>$\\delta = 90^\\circ$ (Vertical plane)</b></td>
                <td><b>$0^\\circ$ to vertical</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>35.2 Mohr-Coulomb Criterion for Normal Fault Dip</h3>
        <p>According to the Coulomb failure criterion, conjugate shear fractures form at an angle $\\theta$ to the maximum principal compressive stress ($\\sigma_1$):</p>
        $$\\theta = 45^\\circ - \\frac{\\phi}{2}$$
        <p>For typical lithospheric crustal rocks, the internal friction angle is $\\phi \\approx 30^\\circ$. Therefore:</p>
        $$\\theta = 45^\\circ - \\frac{30^\\circ}{2} = 45^\\circ - 15^\\circ = 30^\\circ \\quad (\\text{angle with vertical } \\sigma_1)$$
        <p>Thus, normal faults dip at an angle of <b>$60^\circ$ to the horizontal</b> and <b>$30^\circ$ to the vertical</b>. The statement claiming that the most common angle of normal faults is <i>45° to vertical</i> is therefore unequivocally <b>FALSE</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) False</b> — The statement \"Most common angle of normal faults is 45° to vertical\" is <b>False</b>. By Anderson's fault theory and empirical global measurements, normal faults characteristically dip at $\\approx 60^\\circ$ to the horizontal (i.e. $\\approx 30^\\circ$ to the vertical).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) False — CORRECT:</b> Based on Mohr-Coulomb failure ($\phi \approx 30^\circ$), shear fractures form at $30^\circ$ to $\sigma_1$. Since $\sigma_1$ is vertical in normal fault regimes, the angle to vertical is $\mathbf{30^\circ}$ (dip is $60^\circ$ to horizontal), making the $45^\circ$ claim categorically false.</li>
          <li><b>(B) True — INCORRECT:</b> A $45^\circ$ angle would only occur in a perfectly frictionless hypothetical material ($\phi = 0^\circ$), which does not exist in crustal rocks.</li>
          <li><b>(C) Can be true or false — INCORRECT:</b> Standard mechanical laws provide a precise, verifiable answer.</li>
          <li><b>(D) None of these — INCORRECT.</b></li>
        </ul>
        """,
        "part3": """
        <h3>Andersonian Stress State Practice Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 35: Calculating Normal Fault Dip from Friction Angle</div>
          <p>Triaxial compressive laboratory testing on a granite core yields an internal friction angle of $\\phi = 34^\\circ$. In a tectonic extensional basin where this granite undergoes Andersonian normal faulting, what will be: (a) the dip angle of the normal fault relative to the horizontal, and (b) the inclination angle of the fault plane relative to the vertical?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. Angle with maximum compressive stress ($\\sigma_1$, which is vertical):</p>
            $$\\theta_v = 45^\\circ - \\frac{\\phi}{2} = 45^\\circ - \\frac{34^\\circ}{2} = 45^\\circ - 17^\\circ = \\mathbf{28^\\circ\\text{ to the vertical}}$$
            <p>2. Dip angle relative to the horizontal ground surface:</p>
            $$\\delta = 90^\\circ - \\theta_v = 45^\\circ + \\frac{\\phi}{2} = 45^\\circ + 17^\\circ = \\mathbf{62^\\circ\\text{ to the horizontal}}$$
            <p>This confirms that normal faults are steep ($60^\circ\text{–}65^\circ$ to horizontal, $25^\circ\text{–}30^\circ$ to vertical), never $45^\circ$.</p>
          </div>
        </div>
        """
    },

    36: {
        "title": "Q36: Indian Peninsular Drainage & Rift Valleys (SONATA vs. Shield Rivers)",
        "part1": """
        <h3>36.1 Tectonic Geomorphology of Indian Peninsular River Systems</h3>
        <p>In Indian geomorphology and stratigraphy (D.N. Wadia, <i>Geology of India</i>; Ramakrishnan & Vaidyanadhan, <i>Geology of India</i>, Vol. 2; Radhakrishna, 1993), the Indian peninsular drainage system is divided into two radically distinct tectonic categories:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>River System</th>
                <th>Flow Direction & Drainage Basin</th>
                <th>Tectonic Control & Geomorphic Setting</th>
                <th>Rift Valley Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Narmada River</b></td>
                <td>Flows <b>Westward</b> into Gulf of Khambhat (Arabian Sea)</td>
                <td>Occupies the ancient, active <b>SONATA (Son-Narmada-Tapi) mega-rift graben</b> between the Vindhyan Horst (north) and Satpura Horst (south).</td>
                <td><b>CLASSIC RIFT VALLEY (Graben)</b></td>
              </tr>
              <tr>
                <td><b>Tapi (Tapti) River</b></td>
                <td>Flows <b>Westward</b> into Arabian Sea</td>
                <td>Flows parallel to Narmada in the southern graben of the Satpura horst fault system.</td>
                <td><b>CLASSIC RIFT VALLEY (Graben)</b></td>
              </tr>
              <tr>
                <td><b>Mahi River</b></td>
                <td>Flows <b>Westward/Southwestward</b> into Gulf of Khambhat</td>
                <td>Occupies the Cambay-Gujarat structural graben/extensional basin margin.</td>
                <td><b>RIFT / EXTENSIONAL TROUGH</b></td>
              </tr>
              <tr>
                <td><b>Damodar River</b></td>
                <td>Flows Eastward</td>
                <td>Occupies the Gondwana fault-bounded graben trough.</td>
                <td><b>GONDWANA RIFT BASIN</b></td>
              </tr>
              <tr>
                <td><b>Krishna River</b></td>
                <td>Flows <b>Eastward</b> into Bay of Bengal</td>
                <td><b>Originates at Mahabaleshwar (Western Ghats) and flows across the gently east-tilted peninsular crystalline/basaltic shield plateau; governed strictly by regional topographic slope.</b></td>
                <td><b>NOT A RIFT VALLEY (Consequent Shield River)</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>36.2 The Anomaly of Westward-Flowing Peninsular Rivers</h3>
        <p>Most Peninsular Indian rivers (Godavari, Krishna, Cauvery, Mahanadi) flow east-southeast into the Bay of Bengal because the entire Indian shield underwent an easterly regional tilt during Cretaceous-Tertiary rifting of the western continental margin. The <b>only major rivers that flow westward against this regional shield tilt are the Narmada and Tapi</b>, precisely because they are structural prisoners confined within deep, fault-bounded <b>tectonic rift valleys (grabens)</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Krishna</b> — The <b>Krishna River</b> does not flow through a rift valley; it is a major east-flowing consequent river flowing across the tilted peninsular cratonic shield into the Bay of Bengal.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Mahi — INCORRECT:</b> The Mahi river flows southwestward along the extension-controlled Cambay graben basin.</li>
          <li><b>(B) Narmada — INCORRECT:</b> The Narmada is India's most celebrated, prototypical example of a river flowing through a tectonic rift valley (the Son-Narmada lineament graben).</li>
          <li><b>(C) Krishna — CORRECT:</b> Originates at Mahabaleshwar in the Western Ghats and traverses the Deccan plateau shield to form a vast delta on the eastern Coromandel coast; it does not occupy a structural rift valley.</li>
          <li><b>(D) Tungabhadra — (Distractor):</b> While Tungabhadra is also a shield tributary of Krishna, Krishna is the primary master river of the peninsular drainage designated in standard syllabus keys.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Indian River Systematics Table</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Classification</th>
                <th>Rivers</th>
                <th>Drainage Terminal</th>
                <th>Structural Origin</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Rift-Valley Rivers</b></td>
                <td>Narmada, Tapi, Damodar</td>
                <td>Arabian Sea (Narmada, Tapi) / Hooghly (Damodar)</td>
                <td>Tectonic grabens (Cretaceous-Tertiary reactivation of Precambrian sutures)</td>
              </tr>
              <tr>
                <td><b>Shield-Consequent Rivers</b></td>
                <td>Krishna, Godavari, Mahanadi, Cauvery</td>
                <td>Bay of Bengal</td>
                <td>Post-Gondwana regional easterly epeirogenic tilt of Peninsular India</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    37: {
        "title": "Q37: Global Marine Tectonics & Oceanic Ridge/Trench Geography",
        "part1": """
        <h3>37.1 Global Tectonic Framework of Ocean Basins</h3>
        <p>In marine geology and global plate tectonics (C.M.R. Fowler, <i>The Solid Earth: An Introduction to Global Geophysics</i>, 2nd Ed., Ch. 2; Kearey, Klepeis & Vine, <i>Global Tectonics</i>, 3rd Ed., Ch. 4), the ocean floor is subdivided into divergent mid-ocean ridge systems, convergent subduction trenches, and transform fracture zones:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Feature Name</th>
                <th>Geotectonic Nature</th>
                <th>Actual Geographic & Ocean Basin Location</th>
                <th>Associated Tectonic Plates</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Reykjanes Ridge</b></td>
                <td>Divergent Mid-Ocean Spreading Ridge (Segment of Mid-Atlantic Ridge)</td>
                <td><b>North Atlantic Ocean</b> (southwest of Iceland, between $55^\\circ\\text{N}$ and $63^\\circ\\text{N}$).</td>
                <td>North American Plate & Eurasian Plate</td>
              </tr>
              <tr>
                <td><b>Carlsberg Ridge</b></td>
                <td>Slow-spreading Divergent Mid-Ocean Ridge</td>
                <td><b>Northwestern Indian Ocean</b> (trending SE from Gulf of Aden / Socotra towards Chagos).</td>
                <td>African Plate (Somali) & Indo-Australian Plate</td>
              </tr>
              <tr>
                <td><b>Kermadec Trench</b></td>
                <td>Deep-sea Convergent Subduction Trench ($10,047\\text{ m}$ depth)</td>
                <td><b>Southwestern Pacific Ocean</b> (north of New Zealand, continuous with Tonga Trench).</td>
                <td>Pacific Plate subducting beneath Indo-Australian Plate</td>
              </tr>
              <tr>
                <td><b>Phoenix Ridge (Antarctic-Phoenix)</b></td>
                <td>Extinct Spreading Ridge Segment</td>
                <td><b>Southern Pacific / Antarctic Ocean</b> (Drake Passage / Antarctic Peninsula, NOT the Arctic Ocean!).</td>
                <td>Former Phoenix Plate & Antarctic Plate</td>
              </tr>
              <tr>
                <td><b>Gakkel Ridge</b></td>
                <td>Ultra-slow Divergent Mid-Ocean Ridge</td>
                <td><b>True Arctic Ocean Spreading Ridge</b> (between Greenland and Siberia).</td>
                <td>North American Plate & Eurasian Plate</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>37.2 The Arctic Ocean Spreading Center: Gakkel Ridge</h3>
        <p>The sole active spreading mid-ocean ridge in the <b>Arctic Ocean</b> is the <b>Gakkel Ridge</b> (formerly Nansen Cordillera), the slowest spreading center on Earth ($< 10\\text{ mm/yr}$). The <b>Phoenix Ridge</b> is located at the antipodal southern extremity of the globe near the South Shetland Trench in Antarctica.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Phoenix Ridge — Arctic Ocean</b> — This pair is <b>incorrect</b>. The Phoenix Ridge is located in the <b>Antarctic / Southern Pacific Ocean</b> near the Antarctic Peninsula, whereas the mid-ocean ridge of the Arctic Ocean is the <b>Gakkel Ridge</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Kermadec Trench — Pacific Ocean — CORRECT PAIR:</b> The Kermadec Trench is one of the deepest subduction zones on Earth, located in the South Pacific Ocean.</li>
          <li><b>(B) Reykjanes Ridge — Atlantic Ocean — CORRECT PAIR:</b> The Reykjanes Ridge is the prominent northern arm of the Mid-Atlantic Ridge extending directly to Iceland.</li>
          <li><b>(C) Phoenix Ridge — Arctic Ocean — INCORRECT PAIR (The Required Answer):</b> The Phoenix Ridge is an extinct spreading center in the Pacific-Antarctic/Drake Passage region of Antarctica, not the Arctic Ocean.</li>
          <li><b>(D) Carlsberg Ridge — Indian Ocean — CORRECT PAIR:</b> The Carlsberg Ridge is the principal NW-SE spreading ridge bisecting the northern Indian Ocean.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Ocean Floor Features Matching Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Ocean Basin</th>
                <th>Major Mid-Ocean Ridge</th>
                <th>Deepest Subduction Trench</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Pacific Ocean</b></td>
                <td>East Pacific Rise</td>
                <td>Mariana Trench ($11,034\\text{ m}$), Kermadec Trench ($10,047\\text{ m}$)</td>
              </tr>
              <tr>
                <td><b>Atlantic Ocean</b></td>
                <td>Mid-Atlantic Ridge, Reykjanes Ridge</td>
                <td>Puerto Rico Trench ($8,376\\text{ m}$), South Sandwich Trench</td>
              </tr>
              <tr>
                <td><b>Indian Ocean</b></td>
                <td>Central Indian Ridge, Carlsberg Ridge, SE Indian Ridge</td>
                <td>Java (Sunda) Trench ($7,290\\text{ m}$)</td>
              </tr>
              <tr>
                <td><b>Arctic Ocean</b></td>
                <td><b>Gakkel Ridge (Nansen Cordillera)</b></td>
                <td>Molloy Deep (Fram Strait transform, $5,550\\text{ m}$)</td>
              </tr>
              <tr>
                <td><b>Southern / Antarctic Ocean</b></td>
                <td>Pacific-Antarctic Ridge, <b>Phoenix Ridge</b></td>
                <td>South Sandwich Trench</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    38: {
        "title": "Q38: Seismology: Hypocenter (Focus), Epicenter & Isoseismal Attenuation",
        "part1": """
        <h3>38.1 Geometric & Physical Definitions of Earthquake Origins</h3>
        <p>In observational seismology and geophysics (Peter M. Shearer, <i>Introduction to Seismology</i>, 2nd Ed., Ch. 1; Lowrie, <i>Fundamentals of Geophysics</i>, Ch. 3; Bangar, <i>Principles of Engineering Geology</i>, Ch. 10), an earthquake involves the rapid release of accumulated elastic strain energy along a fault rupture surface:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Seismological Term</th>
                <th>Spatial & Geometric Definition</th>
                <th>Physical Role in Wave Dynamics</th>
                <th>Damage & Intensity Relationship</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Focus (Hypocenter)</b></td>
                <td><b>The exact point inside the Earth's interior</b> where the fault rupture nucleates and initial slip begins.</td>
                <td>Origin point of radiating spherical $P$ and $S$ body wavefronts.</td>
                <td>Subsurface point; depth ($h$) ranges from shallow ($0-70\\text{ km}$) to deep ($> 300\\text{ km}$).</td>
              </tr>
              <tr>
                <td><b>Epicenter</b></td>
                <td><b>The point on the Earth's surface directly vertically above the focus (hypocenter).</b></td>
                <td>Point of initial arrival of seismic waves at the surface.</td>
                <td><b>Location of maximum seismic ground shaking intensity ($I_{\\text{max}}$) and catastrophic structural damage</b> for shallow crustal earthquakes.</td>
              </tr>
              <tr>
                <td><b>Focal Depth ($h$)</b></td>
                <td>The vertical distance between the epicenter on the surface and the subsurface focus.</td>
                <td>Directly governs geometrical attenuation: $I \\propto 1/\\sqrt{\\Delta^2 + h^2}$.</td>
                <td>Shallower focal depth = greater concentration of energy at epicenter.</td>
              </tr>
              <tr>
                <td><b>Isoseismal Lines</b></td>
                <td>Closed contour curves connecting points on the Earth's surface experiencing equal earthquake intensity.</td>
                <td>Reflects directional radiation pattern and local geology.</td>
                <td>Form concentric rings centered around the <b>epicenter</b>.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>38.2 Why the Epicenter Suffers Maximum Damage</h3>
        <p>Seismic energy density ($E_d$) attenuates with hypocentral distance ($R = \\sqrt{\\Delta^2 + h^2}$) due to geometrical spreading ($1/R^2$) and anelastic intrinsic attenuation ($e^{-\\alpha R}$):</p>
        $$E_d(\\Delta) \\propto \\frac{E_0}{\\Delta^2 + h^2} \\exp\\left(-\\frac{\\omega R}{Q v}\\right)$$
        <p>Where $\\Delta$ is the epicentral distance. At the <b>epicenter</b>, epicentral distance is zero ($\Delta = 0$), so $R = h$ is at its absolute minimum possible value. Consequently, energy density, peak ground acceleration (PGA), and destructive surface wave amplitude are concentrated at the <b>epicenter</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Epicentre</b> — The point on the Earth's surface directly above the focus is the <b>Epicenter</b>, which experiences the earliest wave arrival, highest peak ground acceleration, and maximum structural damage.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Epicentre — CORRECT:</b> The point on the Earth's surface vertically above the focus where seismic intensity (Modified Mercalli / MSK scale) reaches its maximum ($I_{\\text{max}}$).</li>
          <li><b>(B) Focus — INCORRECT:</b> The focus (hypocenter) is located deep underground inside the Earth's crust or mantle; damage to human civil infrastructure occurs at the Earth's <i>surface</i>.</li>
          <li><b>(C) 100 km from the epicenter — INCORRECT:</b> Seismic intensity attenuates rapidly with distance; shaking at $100\\text{ km}$ is orders of magnitude weaker than at the epicenter.</li>
          <li><b>(D) Isocentre — INCORRECT:</b> In photogrammetry, an isocenter is the point on an aerial photograph where the bisector of the tilt angle meets the image; it is completely meaningless in seismology.</li>
        </ul>
        """,
        "part3": """
        <h3>Seismological Intensity Attenuation Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 38: Hypocentral Distance & Geometric Spreading</div>
          <p>A shallow crustal earthquake has a focal depth of $h = 10\\text{ km}$. Compare the geometrical wave amplitude at the epicenter ($\\Delta_1 = 0\\text{ km}$) with that at a seismic station located at an epicentral distance of $\\Delta_2 = 30\\text{ km}$, assuming simple spherical body wave geometrical spreading ($A \\propto 1/R$).</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. Hypocentral distance to epicenter ($R_1$):</p>
            $$R_1 = \\sqrt{\\Delta_1^2 + h^2} = \\sqrt{0^2 + 10^2} = 10\\text{ km}$$
            <p>2. Hypocentral distance to distant station ($R_2$):</p>
            $$R_2 = \\sqrt{\\Delta_2^2 + h^2} = \\sqrt{30^2 + 10^2} = \\sqrt{900 + 100} = \\sqrt{1000} \\approx 31.62\\text{ km}$$
            <p>3. Ratio of seismic wave amplitudes ($A_1 / A_2$):</p>
            $$\\frac{A_{\\text{epicenter}}}{A_{\\text{station}}} = \\frac{R_2}{R_1} = \\frac{31.62}{10.0} \\approx 3.16$$
            <p>The ground shaking amplitude at the epicenter is more than 3 times greater than at $30\\text{ km}$ away (and energy density is $\\sim 10$ times higher), explaining why maximum devastation is localized at the epicenter.</p>
          </div>
        </div>
        """
    },

    39: {
        "title": "Q39: Seismic Wave Propagation (Body Waves vs. Surface Waves)",
        "part1": """
        <h3>39.1 Comprehensive Taxonomy of Elastic Seismic Waves</h3>
        <p>In global geophysics and seismology (Shearer, <i>Introduction to Seismology</i>, Ch. 3; Lowrie, Ch. 3; Fowler, Ch. 4), seismic disturbances generated by sudden fault slip propagate through and around the Earth as elastic waves. They are fundamentally split into two overarching categories:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Wave Classification</th>
                <th>Wave Types Included</th>
                <th>Propagation Domain</th>
                <th>Particle Motion Mechanics & Velocity</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>BODY WAVES</b></td>
                <td><b>Primary (P) Waves<br>Secondary (S) Waves</b></td>
                <td><b>Propagate through the 3D volume (interior body) of the Earth.</b></td>
                <td><b>P-wave:</b> Compressional / longitudinal (particle motion parallel to propagation, passes through solids, liquids, gases; $v_p = \\sqrt{\\frac{K + 4/3\\mu}{\\rho}}$).<br><b>S-wave:</b> Shear / transverse (particle motion perpendicular to propagation, cannot travel through liquids; $v_s = \\sqrt{\\frac{\\mu}{\\rho}}$).</td>
              </tr>
              <tr>
                <td><b>SURFACE WAVES</b></td>
                <td><b>Rayleigh (R) Waves<br>Love (L) Waves</b></td>
                <td>Propagate strictly along the 2D surface boundary of the Earth; amplitude decays exponentially with depth ($e^{-kz}$).</td>
                <td><b>Rayleigh:</b> Retrograde elliptical motion in vertical plane.<br><b>Love:</b> Transverse horizontal shear motion trapped in surface waveguide.<br>Slower than body waves ($v_R \\approx 0.92 v_s$), but produce the largest destructive amplitudes in earthquakes.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>39.2 Elastic Wave Equation & Helmholtz Decomposition</h3>
        <p>By the Helmholtz decomposition theorem, any displacement vector field $\\mathbf{u}$ in an isotropic elastic medium can be resolved into a dilatational scalar potential $\\phi$ and a rotational vector potential $\\mathbf{\\psi}$:</p>
        $$\\mathbf{u} = \\nabla \\phi + \\nabla \\times \\mathbf{\\psi}$$
        <p>Where $\\nabla \\phi$ yields the <b>P-wave</b> (curl-free dilatational body wave), and $\\nabla \\times \\mathbf{\\psi}$ yields the <b>S-wave</b> (divergence-free shear body wave). Because both travel through the interior volume (body) of the planet, they are collectively termed <b>Body Waves</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Body waves</b> — $P$ (primary compressional) waves and $S$ (secondary shear) waves propagate through the interior volume of the Earth and are collectively termed <b>Body waves</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Love waves — INCORRECT:</b> Love waves are a specific type of horizontal shear <i>surface wave</i>, not a collective term for P and S waves.</li>
          <li><b>(B) Surface waves — INCORRECT:</b> Surface waves (Rayleigh and Love waves) are guided along the Earth's exterior surface; P and S waves travel through the interior body.</li>
          <li><b>(C) Body waves — CORRECT:</b> The standard, universally established geophysical term for seismic waves that penetrate the interior volume (body) of the Earth.</li>
          <li><b>(D) Rayleigh waves — INCORRECT:</b> Rayleigh waves are elliptical retrograde <i>surface waves</i>.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Travel-Time Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 39: Determining Epicentral Distance via P-S Wave Interval</div>
          <p>A regional seismograph station records the first arrival of a P-wave at $10:14:20\\text{ UTC}$ and the first arrival of an S-wave at $10:14:48\\text{ UTC}$. If the average crustal P-wave velocity is $v_p = 6.0\\text{ km/s}$ and S-wave velocity is $v_s = 3.5\\text{ km/s}$, calculate the epicentral distance ($D$) to the earthquake.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The time difference between the arrivals is:</p>
            $$\\Delta t = t_s - t_p = 48\\text{ s} - 20\\text{ s} = 28\\text{ seconds}$$
            <p>2. The travel time formula for body waves is:</p>
            $$\\Delta t = D \\left(\\frac{1}{v_s} - \\frac{1}{v_p}\\right) = D \\left(\\frac{v_p - v_s}{v_p v_s}\\right)$$
            $$D = \\Delta t \\times \\frac{v_p v_s}{v_p - v_s}$$
            <p>3. Substitute the values:</p>
            $$D = 28 \\times \\frac{6.0 \\times 3.5}{6.0 - 3.5} = 28 \\times \\frac{21.0}{2.5} = 28 \\times 8.4 = \\mathbf{235.2\\text{ km}}$$
            <p>The earthquake epicenter is located $235.2\\text{ km}$ from the seismograph station.</p>
          </div>
        </div>
        """
    },

    40: {
        "title": "Q40: Landslide Morphology: Kinematics of Displaced Mass vs. Subjacent Bedrock",
        "part1": """
        <h3>40.1 Varnes (1978) Morphological Anatomy of a Landslide</h3>
        <p>In geotechnical engineering and engineering geology (Cruden & Varnes, 1996; Varnes, 1978; Bangar, <i>Principles of Engineering Geology</i>, Ch. 12), a landslide is defined as the downslope movement of a mass of rock, debris, or earth under the direct influence of gravity. The slope is partitioned by a distinct <b>surface of rupture (shear plane)</b> into two mechanically distinct masses:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Zonal Component</th>
                <th>Physical Description & Terminology</th>
                <th>Mechanical State & Factor of Safety ($FS$)</th>
                <th>Geotechnical Stability</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Displaced Mass (Mass Above Slip Surface)</b></td>
                <td>The volume of rock or soil that has broken away from the parent slope and moved downslope along or beyond the surface of rupture.</td>
                <td>Shear stress exceeded shear strength ($\\tau > \\tau_f$); $FS < 1.0$. Highly fractured, remolded, dilation occurred; lost cohesive bond.</td>
                <td><b>UNSTABLE / ACTIVELY DEFORMING</b></td>
              </tr>
              <tr>
                <td><b>Subjacent Mass (Mass Below Slip Surface)</b></td>
                <td>The intact, undisturbed rock or soil mass situated beneath the surface of rupture and forming the stable foundation/bedrock.</td>
                <td>Resisting shear strength intact; $\\tau < \\tau_f$; $FS > 1.0$. Preserves native confinement and structural integrity.</td>
                <td><b>STABLE / INTACT</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>40.2 Mohr-Coulomb Rupture Localization</h3>
        <p>The failure occurs along the surface of rupture when driving stresses overcome shear resistance:</p>
        $$\\tau_f = c' + (\\sigma_n - u) \\tan \\phi'$$
        <p>The mass <b>above</b> the rupture surface experiences loss of shear strength, catastrophic displacement, and extensive disaggregation, rendering it <b>unstable</b>. The mass <b>below</b> the surface of rupture remains fully anchored to the autochthonous geological formation, remaining completely <b>stable</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) Mass above is unstable, whereas mass below is stable</b> — In landslide kinematics, the displaced mass situated above the shear failure plane is mechanically <b>unstable</b>, while the underlying intact bedrock mass situated below the slip plane is <b>stable</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Both masses are stable — INCORRECT:</b> If both were stable, no landslide failure or downslope movement could ever take place.</li>
          <li><b>(B) Mass above is stable, whereas mass below is unstable — INCORRECT:</b> Complete inversion of physical reality; the displaced material that slides downslope is above the slip surface, not below it.</li>
          <li><b>(C) Mass above is unstable, whereas mass below is stable — CORRECT:</b> Precisely captures the mechanical demarcation defined by the basal shear rupture surface (Varnes 1978).</li>
          <li><b>(D) Both masses are unstable — INCORRECT:</b> The underlying deep bedrock below the shear plane is not in a state of sliding failure; it forms the stable substrate across which the slide moves.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Slope Remediation Table</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Engineering Remediation Method</th>
                <th>Target Landslide Zone</th>
                <th>Mechanical Principle</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Rock Anchors & Fully Grouted Dowels</b></td>
                <td>Drilled through <b>unstable upper mass into stable lower mass</b></td>
                <td>Pins the unstable slide mass securely to the stable bedrock, increasing normal stress and shear resistance.</td>
              </tr>
              <tr>
                <td><b>Horizontal Drainage Bores</b></td>
                <td>Punctures the slip surface into the upper mass</td>
                <td>Dissipates pore water pressure ($u$), increasing effective stress $\\sigma_n' = (\\sigma_n - u)$.</td>
              </tr>
              <tr>
                <td><b>Toe Bench / Retaining Gabion Wall</b></td>
                <td>Base of unstable displaced mass</td>
                <td>Provides passive resisting force ($P_p$) against driving gravitational moment.</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    41: {
        "title": "Q41: Genetic Classification of Mountain Systems (Tectonic vs. Residual)",
        "part1": """
        <h3>41.1 Genetic Classification of Mountain Systems</h3>
        <p>In physical geology and geomorphology (Arthur Holmes, <i>Principles of Physical Geology</i>; Thornbury, <i>Principles of Geomorphology</i>; Bangar, Ch. 2), mountains are categorized based on their fundamental genetic origin into <b>Tectonic (Endogenic)</b> mountains and <b>Residual (Exogenic)</b> mountains:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Genetic Category</th>
                <th>Mountain Type</th>
                <th>Primary Formation Mechanism</th>
                <th>Representative Global & Indian Examples</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="3"><b>TECTONIC MOUNTAINS<br>(Endogenic Internal Forces)</b></td>
                <td><b>Fold Mountains</b></td>
                <td>Crustal convergence, buckling, and orogenic shortening of thick geosynclinal/basin strata.</td>
                <td><b>Himalayas, Alps, Andes, Rockies</b></td>
              </tr>
              <tr>
                <td><b>Fault-Block Mountains (Horsts)</b></td>
                <td>Crustal extension or differential vertical displacement along steep fault systems.</td>
                <td><b>Satpura Range, Vindhyan Scarp, Vosges, Sierra Nevada</b></td>
              </tr>
              <tr>
                <td><b>Volcanic Mountains (Accumulation)</b></td>
                <td>Extrusion and constructional accumulation of lava, tephra, and pyroclastic debris around a vent.</td>
                <td><b>Mt. Fuji, Kilimanjaro, Mauna Loa, Barren Island</b></td>
              </tr>
              <tr>
                <td><b>NON-TECTONIC / EROSIONAL<br>(Exogenic External Forces)</b></td>
                <td><b>Residual Mountains (Relict / Circumdenudational)</b></td>
                <td><b>NOT formed by active tectonic deformation.</b> Formed by prolonged differential weathering and stream denudation of ancient plateaus, leaving hard, resistant rocks standing as relief hills.</td>
                <td><b>Aravalli Range (relict hills), Nilgiris, Parasnath Hills, Scottish Highlands</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>41.2 The Concept of Residual (Relict) Relief</h3>
        <p>Residual mountains (monadnocks, bornhardts, mesas, buttes) are products of the <i>degradation of old landmasses</i>. They represent the unconsumed erosional remnants of ancient peneplains or plateaus that have resisted denudation due to superior lithological hardness or structural compactness (e.g. quartzite ridges standing above eroded schists). Therefore, they belong to the <b>erosional/denudational category</b>, not tectonic mountains.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) Residual mountains</b> — <b>Residual mountains</b> (relict hills) are formed by exogenic differential weathering and stream erosion, and do <i>not</i> belong to the tectonic mountain categories.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Complex mountains — INCORRECT:</b> Complex mountains (or polyphase orogenic belts) are classic tectonic mountains formed by multi-stage folding, thrusting, and metamorphism.</li>
          <li><b>(B) Volcanic mountains — INCORRECT:</b> Volcanic mountains are endogenic/tectonic constructive edifices formed by magmatic activity associated with subduction or mantle plumes.</li>
          <li><b>(C) Fault block mountains — INCORRECT:</b> Fault block mountains (horsts) are direct tectonic mountains formed by crustal faulting and differential vertical displacement.</li>
          <li><b>(D) Residual mountains — CORRECT:</b> Residual mountains are exclusively exogenic/erosional in genesis, formed by the circumdenudation of ancient plateaus.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Geomorphic Evolution Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 41: Morphoclimatic Inversion of Relief</div>
          <p>The Aravalli Range is one of the oldest mountain belts in the world (Proterozoic Delhi-Aravalli Orogen). Explain why the present-day topography of the Aravallis is classified geomorphically as a \"Residual Mountain\" system rather than an active \"Fold Mountain\" chain.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. While the rocks of the Aravalli Supergroup were intensely folded, faulted, and metamorphosed during the Proterozoic orogeny ($~1.5\\text{–}1.0\\text{ Ga}$), active tectonic folding ceased over $500\\text{ million years ago}$.</p>
            <p>2. Over the subsequent hundreds of millions of years, prolonged subaerial weathering and denudation planed the ancient orogen down to a peneplain.</p>
            <p>3. Differential erosion then carved away the soft mica schists and phyllites, leaving the highly resistant Alwar quartzites standing as narrow, elevated relict ridges (e.g. Guru Shikhar, $1,722\\text{ m}$). Because their current elevation is maintained purely by differential erosional resistance rather than active tectonic uplift, they are quintessential <b>Residual Mountains</b>.</p>
          </div>
        </div>
        """
    },

    42: {
        "title": "Q42: Rheology of Upper Mantle & Asthenospheric Low Velocity Zone (LVZ)",
        "part1": """
        <h3>42.1 Rheological Stratification: Lithosphere vs. Asthenosphere</h3>
        <p>In mantle geodynamics and seismology (Turcotte & Schubert, <i>Geodynamics</i>, 3rd Ed., Ch. 7; Fowler, <i>The Solid Earth</i>, Ch. 4; Lowrie, Ch. 1), the Earth's upper $400\\text{ km}$ is subdivided based on mechanical strength and rheology:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Property / Parameter</th>
                <th>Lithosphere</th>
                <th>Asthenosphere</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Depth Range</b></td>
                <td>Surface to $100\\text{–}150\\text{ km}$ (beneath continents) / $0\\text{–}100\\text{ km}$ (oceans).</td>
                <td><b>$\\sim 100\\text{ km}$ to $410\\text{ km}$</b> (Upper Mantle above transition zone).</td>
              </tr>
              <tr>
                <td><b>Physical & Rheological State</b></td>
                <td><b>Rigid, elastic, brittle solid</b> lithospheric lid.</td>
                <td><b>Ductile, plastic, mechanically weak rheid (viscous solid-state creep with $\\sim 1 - 2\\%$ partial melt). NOT a rigid solid!</b></td>
              </tr>
              <tr>
                <td><b>Temperature vs. Solidus</b></td>
                <td>$T \\ll T_{\\text{solidus}}$ ($T < 1300^\\circ\\text{C}$ isotherm defines base).</td>
                <td><b>$T \\approx T_{\\text{solidus}}$ (Geotherm intersects/approaches mantle peridotite solidus).</b></td>
              </tr>
              <tr>
                <td><b>Seismic Characteristic</b></td>
                <td>High $P$ and $S$ wave velocities; low attenuation ($Q$).</td>
                <td><b>Low Velocity Zone (LVZ)</b>: $v_s$ drops by $3-6\\%$; high seismic attenuation ($1/Q$).</td>
              </tr>
              <tr>
                <td><b>Geodynamic Function</b></td>
                <td>Forms the moving tectonic plates.</td>
                <td><b>Deformable lubricating substrate for plate motions; primary source of basaltic magma via adiabatic decompression melting.</b></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>42.2 Why \"It is in solid-state\" is Incorrect in Academic Testing</h3>
        <p>In standard university geological curricula and competitive exams (OPSC, UPSC GSI, GATE), the defining attribute of the <b>Asthenosphere</b> (from Greek <i>asthenes</i>, meaning \"weak\" or \"without strength\", named by Joseph Barrell in 1914) is that it is <b>semi-molten, plastic, and capable of ductile viscous flow</b> over geological timescales, in direct contrast to the rigid, solid lithosphere above. Stating that the asthenosphere is simply in a rigid \"solid-state\" is considered fundamentally misleading and incorrect in this context.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) It is in solid-state</b> — Stating that the Asthenosphere is in a rigid \"solid-state\" is <b>incorrect</b>; the asthenosphere is characteristically a <b>plastic, semi-molten (or partially molten rheid)</b> layer that undergoes ductile flow.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) It is present in the upper mantle — CORRECT STATEMENT:</b> The asthenosphere is situated within the upper mantle, immediately below the lithosphere from $\\sim 100\\text{ km}$ down to the $410\\text{ km}$ mantle discontinuity.</li>
          <li><b>(B) It is in solid-state — INCORRECT STATEMENT (Required Answer):</b> The asthenosphere behaves as a plastic, semi-molten rheid with interstitial partial melting ($1-2\\%$) that generates the seismic Low Velocity Zone (LVZ); describing it as rigid solid-state denies its defining rheological nature.</li>
          <li><b>(C) It is in a semi-molten stage — CORRECT STATEMENT:</b> Partial melting along grain boundaries gives the asthenosphere its low viscosity and seismic velocity drop.</li>
          <li><b>(D) It is the source of volcanic activity — CORRECT STATEMENT:</b> Upwelling and adiabatic decompression melting of the asthenosphere generates mid-ocean ridge basalts (MORB) and supplies hotspot volcanism.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Mantle Rheology Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 42: Viscous Relaxation Time of the Asthenosphere</div>
          <p>Post-glacial rebound of the Fennoscandian shield yields an estimated asthenospheric dynamic viscosity of $\\eta = 1.0 \\times 10^{20}\\text{ Pa}\\cdot\\text{s}$ and an effective shear modulus of $\\mu = 7.0 \\times 10^{10}\\text{ Pa}$. Calculate the Maxwell viscoelastic relaxation time ($\\tau_M$) of the asthenosphere and interpret its physical meaning.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The Maxwell relaxation time is given by:</p>
            $$\\tau_M = \\frac{\\eta}{\\mu} = \\frac{1.0 \\times 10^{20}\\text{ Pa}\\cdot\\text{s}}{7.0 \\times 10^{10}\\text{ Pa}} \\approx 1.43 \\times 10^9\\text{ seconds}$$
            <p>2. Convert seconds to years ($1\\text{ yr} \\approx 3.156 \\times 10^7\\text{ s}$):</p>
            $$\\tau_M = \\frac{1.43 \\times 10^9}{3.156 \\times 10^7} \\approx 45.3\\text{ years}$$
            <p><b>Physical Interpretation:</b> For loading periods much shorter than $\\tau_M$ (such as high-frequency seismic waves with periods of seconds), the asthenosphere responds elastically (transmitting P and S waves). For loading periods much longer than $\\tau_M$ (such as mantle convection and plate motion over millions of years), elastic stresses relax to zero and the asthenosphere behaves completely as a <b>viscous fluid rheid</b>.</p>
          </div>
        </div>
        """
    },

    43: {
        "title": "Q43: Earth's Geochemical Layering: Suess SIAL, SIMA & NIFE Model",
        "part1": """
        <h3>43.1 Eduard Suess (1875) Classical Compositional Model of Earth</h3>
        <p>In physical geology and historical geochemistry (Eduard Suess, 1875, <i>Die Entstehung der Alpen</i>; Holmes, <i>Principles of Physical Geology</i>; Bangar, Ch. 2), the Earth was first classified chemically into three concentric shells based on characteristic elemental abbreviations:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Historical Shell Name</th>
                <th>Chemical Element Roots</th>
                <th>Dominant Minerals & Rocks</th>
                <th>Mean Density ($\\rho$)</th>
                <th>Modern Structural Equivalent</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>SIAL</b></td>
                <td><b>SI</b>lica ($\text{Si}$) + <b>AL</b>uminium ($\text{Al}$)</td>
                <td>Quartz, K-feldspar, Na-plagioclase, Granite, Granodiorite</td>
                <td>$2.7 - 2.8\\text{ g/cm}^3$</td>
                <td><b>Upper Continental Crust</b> (light, buoyant, forms granitic continents).</td>
              </tr>
              <tr>
                <td><b>SIMA</b></td>
                <td><b>SI</b>lica ($\text{Si}$) + <b>MA</b>gnesium ($\text{Mg}$)</td>
                <td>Pyroxene, Olivine, Ca-plagioclase, Basalt, Gabbro, Peridotite</td>
                <td>$2.9 - 3.4\\text{ g/cm}^3$</td>
                <td><b>Oceanic Crust, Lower Crust & Upper Mantle</b> (denser, mafic substrate).</td>
              </tr>
              <tr>
                <td><b>NIFE</b></td>
                <td><b>NI</b>ckel ($\text{Ni}$) + <b>FE</b>rrum / Iron ($\text{Fe}$)</td>
                <td>Iron-Nickel metallic alloy ($80-85\\%\\text{ Fe}, 5-10\\%\\text{ Ni}$)</td>
                <td>$10.0 - 13.0\\text{ g/cm}^3$</td>
                <td><b>Earth's Core</b> (Outer liquid core + Inner solid core).</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>43.2 Evolution to Modern Plate Tectonics</h3>
        <p>In Alfred Wegener's (1912) Continental Drift theory, the lighter granitic continents (SIAL) were envisioned as floating and plowing through the denser, plastic basaltic substrate of the oceanic floor (SIMA). Modern plate tectonics replaced this concept with rigid <i>lithospheric plates</i> (incorporating both crust and uppermost mantle) translating over the ductile <i>asthenosphere</i>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) Silicon and Magnesium</b> — In Eduard Suess's classical compositional nomenclature, <b>SIMA</b> stands for <b>Silicon (Silica)</b> and <b>Magnesium</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Silicon and Manganese — INCORRECT:</b> Manganese is a minor trace transition metal ($\text{Mn}$), not a major rock-forming macro-element of the oceanic crust.</li>
          <li><b>(B) Strontium and Magnesium — INCORRECT:</b> Strontium ($\text{Sr}$) is an incompatible trace element, not a major structural component of the silicate Earth.</li>
          <li><b>(C) Sulphur and Manganese — INCORRECT:</b> Completely misses silica, which forms the $45-52\\%$ foundational backbone of mafic rocks.</li>
          <li><b>(D) Silicon and Magnesium — CORRECT:</b> The universal, canonical definition: <b>SI</b>lica ($\text{Si}$) + <b>MA</b>gnesium ($\text{Mg}$).</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Major Element Geochemistry Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Major Oxide</th>
                <th>SIAL (Upper Continental Crust) [wt%]</th>
                <th>SIMA (N-MORB Oceanic Crust) [wt%]</th>
                <th>Primitive Mantle [wt%]</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>$\\text{SiO}_2$</b></td>
                <td><b>$66.0\\%$ (High Silica)</b></td>
                <td><b>$50.5\\%$ (Moderate Silica)</b></td>
                <td>$45.0\\%$</td>
              </tr>
              <tr>
                <td><b>$\\text{Al}_2\\text{O}_3$</b></td>
                <td><b>$15.2\\%$ (High Aluminium)</b></td>
                <td>$15.3\\%$</td>
                <td>$4.5\\%$</td>
              </tr>
              <tr>
                <td><b>$\\text{MgO}$</b></td>
                <td>$2.2\\%$</td>
                <td><b>$7.6\\%$ (High Magnesium)</b></td>
                <td><b>$37.8\\%$ (Ultra-High Mg)</b></td>
              </tr>
              <tr>
                <td><b>$\\text{FeO}^*$</b></td>
                <td>$4.5\\%$</td>
                <td>$10.5\\%$</td>
                <td>$8.1\\%$</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    44: {
        "title": "Q44: Deep Earth Seismology: P-Wave Core Transmission & PKIKP Phases",
        "part1": """
        <h3>44.1 Core Discontinuities & Seismic Wave Propagation</h3>
        <p>In global seismology and deep Earth geophysics (Inge Lehmann, 1936; Beno Gutenberg, 1914; Peter Shearer, <i>Introduction to Seismology</i>, Ch. 4; Fowler, Ch. 4), the Earth's core boundary architecture was discovered through seismic ray tracing:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Seismic Boundary</th>
                <th>Depth</th>
                <th>Physical Nature & Discontinuity</th>
                <th>Wave Transmission Behavior</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Core-Mantle Boundary (CMB)</b></td>
                <td>$2890\\text{ km}$</td>
                <td><b>Gutenberg Discontinuity</b>: Boundary between solid silicate lower mantle and liquid iron-nickel outer core.</td>
                <td><b>S-waves are completely terminated</b> (shear modulus $\\mu = 0$ in liquid). <b>P-waves are transmitted</b>, but sharply refracted downward because velocity drops from $13.7\\text{ km/s}$ in mantle to $8.0\\text{ km/s}$ in liquid core.</td>
              </tr>
              <tr>
                <td><b>Inner Core Boundary (ICB)</b></td>
                <td>$5150\\text{ km}$</td>
                <td><b>Lehmann Discontinuity</b>: Boundary between liquid outer core and solid crystalline iron-nickel inner core.</td>
                <td><b>P-waves are transmitted across the ICB into the inner core</b>, with a sharp velocity jump from $10.3\\text{ km/s}$ to $11.0\\text{ km/s}$, reflecting and refracting through to the antipodal surface.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>44.2 Nomenclature of Core Seismic Phases</h3>
        <p>Standard International Seismological Centre (ISC) ray code notation defines:</p>
        <ul>
          <li><b>P:</b> Compressional wave traveling through the mantle.</li>
          <li><b>K:</b> Compressional wave traveling through the <b>liquid outer core</b> (from German <i>Kern</i>).</li>
          <li><b>I:</b> Compressional wave traveling through the <b>solid inner core</b>.</li>
          <li><b>PKIKP:</b> A compressional wave that traverses the mantle (P), refracts through the outer core (K), penetrates through the solid inner core (I), passes back through the outer core (K), and ascends through the mantle (P) to arrive at antipodal seismographs ($142^\\circ - 180^\\circ$).</li>
        </ul>
        <p>Thus, it is an immutable physical fact that <b>the P-wave is transmitted through the outer core as well as the inner core</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (C)</span>
          <p><b>Correct Answer: (C) The P wave is transmitted through the outer as well as the inner core.</b> — Compressional P-waves penetrate through the liquid outer core (as K waves) and traverse through the solid inner core (as I waves), generating the classic <b>PKIKP</b> phase.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) The P wave reflected from the mantle-core boundary — INCORRECT:</b> While a small fraction of energy reflects as PcP, the primary phenomenon is that P-waves <b>refract into and are transmitted through</b> the core.</li>
          <li><b>(B) The P wave is transmitted through the outer core but reflected from the inner core — INCORRECT:</b> P-waves are not simply reflected at the inner core boundary; Inge Lehmann (1936) proved that P-waves refract directly <i>through</i> the solid inner core (PKIKP phase).</li>
          <li><b>(C) The P wave is transmitted through the outer as well as the inner core — CORRECT:</b> Precisely describes the fundamental transmission capability of longitudinal P-waves through both the liquid and solid core compartments.</li>
          <li><b>(D) The P wave is reflected from the crust-mantle boundary — INCORRECT:</b> P-waves pass directly through the Moho into the mantle, undergoing refraction rather than total reflection.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Seismological Ray Tracing Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Seismic Phase Code</th>
                <th>Complete Ray Path Trajectory</th>
                <th>Epicentral Distance Arrival Range</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>P</b></td>
                <td>Direct mantle compressional wave</td>
                <td>$0^\\circ - 103^\\circ$</td>
              </tr>
              <tr>
                <td><b>PcP</b></td>
                <td>Reflected from mantle-core boundary (CMB) back to surface</td>
                <td>$0^\\circ - 90^\\circ$</td>
              </tr>
              <tr>
                <td><b>PKP (PKPab, PKPdf)</b></td>
                <td>Transmitted through mantle and liquid outer core</td>
                <td>$142^\\circ - 180^\\circ$</td>
              </tr>
              <tr>
                <td><b>PKIKP</b></td>
                <td><b>Transmitted through Mantle → Liquid Outer Core → Solid Inner Core → Outer Core → Mantle</b></td>
                <td><b>$110^\\circ - 180^\\circ$ (Antipodal arrivals)</b></td>
              </tr>
              <tr>
                <td><b>S-Wave Shadow Zone</b></td>
                <td><b>$103^\circ - 180^\circ$</b> (No direct S-waves arrive because liquid outer core cannot transmit shear waves)</td>
                <td>Worldwide beyond $103^\circ$</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    45: {
        "title": "Q45: Principles of Isostasy: Gravitational Balance & Archimedes Buoyancy",
        "part1": """
        <h3>45.1 Physical Foundation of Isostasy</h3>
        <p>In global geophysics and geodynamics (A.B. Watts, 2001, <i>Isostasy and Flexure of the Lithosphere</i>; Fowler, Ch. 5; Lowrie, Ch. 2), <b>isostasy</b> (from Greek <i>isostasios</i>, \"equal standing\" or \"equal balance\", coined by C.E. Dutton in 1889) is the condition of gravitational equilibrium between the Earth's rigid lithosphere and the ductile, denser asthenospheric mantle beneath it:</p>
        $$\\sum \\mathbf{F} = 0 \\iff \\mathbf{F_{\\text{buoyancy}} = F_{\\text{gravity}}}$$
        <p>According to Archimedes' Principle of buoyancy, a floating lithospheric block displaces a mass of asthenospheric fluid equal to its own total weight:</p>
        $$F_g = M_{\\text{lith}} g = (\\rho_c A h_t) g$$
        $$F_b = M_{\\text{displaced mantle}} g = (\\rho_m A r) g$$
        <p>At isostatic equilibrium:</p>
        $$\\rho_c h_t = \\rho_m r \\implies r = h_t \\left(\\frac{\\rho_c}{\\rho_m}\\right)$$
        <p>Where $\\rho_c$ is crustal density, $\\rho_m$ is mantle density, $h_t$ is total crustal column height, and $r$ is the depth of the submerged crustal root.</p>

        <h3>45.2 Classical Models of Isostatic Compensation</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Isostatic Model</th>
                <th>Fundamental Mechanical Assumption</th>
                <th>Compensation Mechanism</th>
                <th>Geological Analogy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Airy Isostasy (1855)</b></td>
                <td><b>Constant crustal density ($\\rho_c = \\text{const}$)</b>; variable crustal thickness.</td>
                <td>High topography is compensated by deep, low-density <b>crustal roots</b> extending into denser mantle.</td>
                <td>Icebergs floating in water; blocks of wood with different heights.</td>
              </tr>
              <tr>
                <td><b>Pratt Isostasy (1855)</b></td>
                <td><b>Uniform depth of compensation ($D = \\text{const}$)</b>; variable crustal density.</td>
                <td>High mountains have lower density ($\\rho_1$), while low oceanic plains have higher density ($\\rho_2$).</td>
                <td>Blocks of different metals (copper, iron, lead) floating in mercury to the same depth.</td>
              </tr>
              <tr>
                <td><b>Vening Meinesz (1931)</b></td>
                <td><b>Flexural isostasy</b>; lithosphere acts as an elastic plate with finite flexural rigidity ($D_f$).</td>
                <td>Loads are supported regionally by flexural bending of the elastic plate rather than local columns.</td>
                <td>Himalayan foreland basin flexure; volcanic seamount chains.</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) A buoyancy force pushing the lithosphere up equals the gravitational force pushing it down.</b> — By definition, isostatic equilibrium is achieved when the upward hydrostatic buoyancy force of the asthenosphere precisely balances the downward gravitational weight of the lithospheric column.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) A buoyancy force pushing the lithosphere up equals the gravitational force pushing it down — CORRECT:</b> The exact definition of hydrostatic and isostatic balance ($\sum F_y = 0$).</li>
          <li><b>(B) A buoyancy force pushing the lithosphere up is less than the gravitational force pushing it down — INCORRECT:</b> Represents an under-compensated state where the lithosphere must actively subside (negative isostatic anomaly).</li>
          <li><b>(C) A buoyancy force pushing the lithosphere up is greater than the gravitational force pushing it down — INCORRECT:</b> Represents an over-compensated state resulting in ongoing post-glacial isostatic rebound/uplift.</li>
          <li><b>(D) All the features of Earth's surface are at the same elevation — INCORRECT:</b> Isostasy explicitly explains why the Earth exhibits diverse surface elevations (mountains vs. ocean basins) due to variations in crustal thickness and density.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Airy Isostasy Calculation Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 45: Mountain Root Calculation in Airy Model</div>
          <p>A mountain range rises $h = 4.0\\text{ km}$ above sea level. Assuming standard continental crust of density $\\rho_c = 2.8\\text{ g/cm}^3$, standard sea-level crustal thickness $T_0 = 30\\text{ km}$, and mantle density $\\rho_m = 3.3\\text{ g/cm}^3$, calculate the depth of the crustal root ($r$) extending into the mantle beneath the mountain range.</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. Under Airy isostatic compensation, the pressure at the depth of compensation beneath the mountain column equals the pressure beneath the sea-level column:</p>
            $$(h + T_0 + r) \\rho_c = T_0 \\rho_c + r \\rho_m$$
            $$h \\rho_c + r \\rho_c = r \\rho_m \\implies h \\rho_c = r (\\rho_m - \\rho_c)$$
            $$r = h \\times \\frac{\\rho_c}{\\rho_m - \\rho_c}$$
            <p>2. Substitute the values:</p>
            $$r = 4.0\\text{ km} \\times \\frac{2.8}{3.3 - 2.8} = 4.0 \\times \\frac{2.8}{0.5} = 4.0 \\times 5.6 = \\mathbf{22.4\\text{ km}}$$
            <p>3. The total crustal thickness beneath the mountain is $T_{\\text{total}} = h + T_0 + r = 4.0 + 30.0 + 22.4 = \\mathbf{56.4\\text{ km}}$, demonstrating why collisional mountain belts possess deep crustal roots.</p>
          </div>
        </div>
        """
    },

    46: {
        "title": "Q46: Cretaceous Stratigraphy of Cauvery Basin: Uttatur, Trichinopoly & Ariyalur",
        "part1": """
        <h3>46.1 Cretaceous Marine Transgression in the Cauvery Basin</h3>
        <p>In Indian stratigraphy and paleontology (M.S. Krishnan, <i>Geology of India and Burma</i>, Ch. 15; Ramakrishnan & Vaidyanadhan, <i>Geology of India</i>, Vol. 2, Ch. 24; Blanford, 1862), the Cretaceous succession of the Tiruchirappalli (Trichinopoly) district in Tamil Nadu constitutes the most complete, world-renowned marine Cretaceous reference section in peninsular India. Deposited during global Cenomanian-Campanian marine transgressions across the newly rifted eastern margin of Gondwana, it rests unconformably upon Archean charnockites and gneisses:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Lithostratigraphic Formation</th>
                <th>Standard Age</th>
                <th>Diagnostic Lithologies</th>
                <th>Key Index Fossils & Biostratigraphy</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>3. Ariyalur Formation (Top)</b></td>
                <td><b>Campanian to Maastrichtian</b></td>
                <td>Unconsolidated sands, fossiliferous calc-sandstones, white clays, and shell limestones.</td>
                <td><b>Ammonites:</b> <i>Pachydiscus, Baculites, Sphenodiscus</i>.<br><b>Foraminifera:</b> <i>Globotruncana gansseri</i>.<br>Extends to K-Pg boundary.</td>
              </tr>
              <tr>
                <td><b>2. Trichinopoly Formation (Middle)</b></td>
                <td><b>Turonian to Coniacian</b></td>
                <td>Coarse grits, shell limestones, calcareous sandstones, and gypseous clays.</td>
                <td><b>Ammonites:</b> <i>Placenticeras tamulicum, Lewesiceras</i>.<br><b>Bivalves:</b> <i>Inoceramus, Spondylus</i>.</td>
              </tr>
              <tr>
                <td><b>1. Uttatur (Ootatoor) Formation (Base)</b></td>
                <td><b>Upper Albian to Cenomanian</b></td>
                <td>Basal conglomerates, coral reef limestones, fine yellow sandstones, and phosphatic nodule-bearing gypseous clays.</td>
                <td><b>Ammonites:</b> <i>Schloenbachia inflata, Acanthoceras rhotomagense, Turrilites costatus</i>.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>46.2 Historical Classification by H.F. Blanford (1862)</h3>
        <p>H.F. Blanford of the Geological Survey of India established the canonical tripartite division of the Trichinopoly Cretaceous basin into:</p>
        <ol>
          <li><b>Uttatur Formation</b> (lower Cenomanian)</li>
          <li><b>Trichinopoly Formation</b> (middle Turonian)</li>
          <li><b>Ariyalur Formation</b> (upper Senonian / Campanian-Maastrichtian)</li>
        </ol>
        <p>Later workers (Rama Rao, 1956) recognized the topmost Danian (Paleocene) beds as the <i>Niniyur Formation</i>, but the classical Cretaceous sequence consists strictly of Uttatur, Trichinapoli, and <b>Ariyalur</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Ariyalur Formation</b> — The Upper Cretaceous rocks of the Tiruchirappalli area are classically classified into three major Formations: <b>Uttatur</b>, <b>Trichinapoli</b>, and <b>Ariyalur Formation</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Ariyalur Formation — CORRECT:</b> Forms the uppermost division of the tripartite Cretaceous of Trichinopoly, famous for its rich Campanian-Maastrichtian invertebrate fauna.</li>
          <li><b>(B) Haimanta Formation — INCORRECT:</b> The Haimanta Group is an early Paleozoic (Cambrian) unit of the Tethyan Himalayan succession in the Spiti Valley, over $2500\\text{ km}$ away in northern India.</li>
          <li><b>(C) Lilang Formation — INCORRECT:</b> The Lilang Group is the monumental Triassic marine limestone succession of the Spiti Tethyan belt.</li>
          <li><b>(D) Chikkim Formation — INCORRECT:</b> The Chikkim Formation is the Cretaceous limestone-shale formation of the Spiti basin in the Himalayas, not Tamil Nadu.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Indian Cretaceous Stratigraphy Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Geographic Basin</th>
                <th>Lithostratigraphic Formations</th>
                <th>Depositional Setting</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Cauvery Basin (Trichinopoly)</b></td>
                <td><b>Uttatur → Trichinopoly → Ariyalur → Niniyur</b></td>
                <td>Passive margin shallow marine shelf (Bay of Bengal opening)</td>
              </tr>
              <tr>
                <td><b>Narmada Valley (Bagh Beds)</b></td>
                <td>Nimar Sandstone → Nodular Limestone → Deola-Chirakhan Marl → Coralline Limestone</td>
                <td>Estuarine to shallow marine inlet (Arabian Sea transgression)</td>
              </tr>
              <tr>
                <td><b>Spiti Basin (Himalaya)</b></td>
                <td>Giumal Sandstone → Chikkim Formation</td>
                <td>Tethys deep to pelagic shelf ocean</td>
              </tr>
              <tr>
                <td><b>Central India (Lameta Beds)</b></td>
                <td>Infratrappean cherty limestones, green sands (Titanosaur dinosaur bones)</td>
                <td>Fluvio-lacustrine terrestrial environments</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    47: {
        "title": "Q47: Vindhyan Supergroup Lithostratigraphy: Semri, Kaimur, Rewa & Bhander",
        "part1": """
        <h3>47.1 The Mesoproterozoic-Neoproterozoic Vindhyan Supergroup</h3>
        <p>In Indian Precambrian stratigraphy (Auden, 1933; Ramakrishnan & Vaidyanadhan, <i>Geology of India</i>, Vol. 1, Ch. 12; M.S. Krishnan, Ch. 7), the <b>Vindhyan Supergroup</b> represents one of the world's most spectacular, undeformed intracratonic Purana sedimentary basins, covering $> 100,000\\text{ km}^2$ in central India. Resting with profound unconformity upon the Archean Bundelkhand Granite and Bijawar Group, it is subdivided into four well-defined groups:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Supergroup Division</th>
                <th>Group Name</th>
                <th>Dominant Lithologies</th>
                <th>Major Formations & Economic Minerals</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="3"><b>UPPER VINDHYAN<br>(Predominantly Arenaceous)</b></td>
                <td><b>4. Bhander Group (Top)</b></td>
                <td>Shales, sandstones, stromatolitic limestones.</td>
                <td><b>Upper Bhander Sandstone</b> (premier building stone: Red Fort, Sanchi Stupa), Sirbu Shale, Bhander Limestone.</td>
              </tr>
              <tr>
                <td><b>3. Rewa Group</b></td>
                <td>Quartzites, sandstones, and carbonaceous/ferruginous shales.</td>
                <td>Govindgarh Sandstone, Jhiri Shale, Panna Shale (<b>diamondiferous conglomerate horizons</b>).</td>
              </tr>
              <tr>
                <td><b>2. Kaimur Group</b></td>
                <td>Thick, massive orthoquartzites, arenites, and subordinate shales.</td>
                <td>Dhandraul Quartzite, Scarp Sandstone, Bijaigarh Shale (pyrite-bearing).</td>
              </tr>
              <tr>
                <td><b>LOWER VINDHYAN<br>(Calc-Argillaceous)</b></td>
                <td><b>1. Semri Group (Base)</b></td>
                <td>Carbonates, volcaniclastics (porcellanites), and basal conglomerates.</td>
                <td>Rohtas Limestone, Glauconitic Sandstone, <b>Porcellanite Formation</b> (felsic tuffs), Kajrahat Limestone.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>47.2 Structural Boundary: The Great Boundary Fault (GBF)</h3>
        <p>The western margin of the Vindhyan basin is sharply truncated against the pre-Vindhyan rocks of the Aravalli-Delhi belt by the monumental <b>Great Boundary Fault (GBF)</b> of Rajasthan, a regional thrust with over $800\\text{ km}$ of strike length. The succession is celebrated for the world's oldest putative multicellular algae/metazoan trace fossils and pristine stromatolite assemblages (e.g. <i>Collenia, Conophyton</i>).</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) Bhander Group</b> — The four lithostratigraphic groups composing the Vindhyan Supergroup in ascending order are: <b>Semri Group</b>, <b>Kaimur Group</b>, <b>Rewa Group</b>, and <b>Bhander Group</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Bijawar Group — INCORRECT:</b> The Bijawar Group is a Paleoproterozoic volcanosedimentary basin sequence that forms the folded crystalline <i>basement floor</i> underlying the Vindhyan Supergroup.</li>
          <li><b>(B) Bhander Group — CORRECT:</b> The uppermost, fourth group of the Vindhyan Supergroup, completing the classical Semri-Kaimur-Rewa-Bhander succession.</li>
          <li><b>(C) Gwalior Group — INCORRECT:</b> The Gwalior Group is another Paleoproterozoic sequence exposed near Gwalior that unconformably underlies the Kaimur Group of the Vindhyans.</li>
          <li><b>(D) None of these — INCORRECT:</b> Option (B) is the universally accepted group name.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Vindhyan Stratigraphic Mnemonic & Problem</h3>
        <div class="qa-card">
          <div class="q-title">Practice Problem 47: Chronostratigraphic Boundary & Diamondiferous Horizons</div>
          <p>In which group of the Vindhyan Supergroup are the famous primary and secondary diamond-bearing horizons of Panna (Madhya Pradesh) located, and what is the nature of the host rock?</p>
          <div class="a-box">
            <p><b>Solution:</b></p>
            <p>1. The primary diamond source rocks in the Panna diamond belt are <b>ultramafic kimberlite / lamproite diatreme pipes</b> (e.g. the Majhgawan pipe, dated at $\\sim 1070\\text{ Ma}$), which intrude the Kaimur Group.</p>
            <p>2. The secondary placer diamond deposits occur within the basal conglomerate beds of the <b>Rewa Group</b> (specifically the Panna Shale and Jhiri Shale conglomerates), derived from the erosional weathering of the kimberlite pipes prior to Rewa sedimentation.</p>
          </div>
        </div>
        """
    },

    48: {
        "title": "Q48: Lower Gondwana Inception: Talchir Formation & Permo-Carboniferous Glaciation",
        "part1": """
        <h3>48.1 Gondwana Basin Inception in Peninsular India</h3>
        <p>In Indian fuel geology and stratigraphy (W.T. Blanford, 1856; Ramakrishnan & Vaidyanadhan, <i>Geology of India</i>, Vol. 2, Ch. 18; M.S. Krishnan, Ch. 10), the continental Gondwana basins of Peninsular India (Damodar, Mahanadi, Son, Pranhita-Godavari, and Satpura basins) originated in fault-bounded down-faulted rift grabens during the Late Carboniferous to Early Permian (Asselian, $\\sim 300\\text{ Ma}$):</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Lithostratigraphic Unit</th>
                <th>Chronostratigraphic Age</th>
                <th>Lithological Association</th>
                <th>Paleoenvironmental & Paleoclimatic Signatures</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Talchir Formation (Basal Unit)</b></td>
                <td><b>Late Carboniferous to Early Permian (Asselian)</b></td>
                <td><b>Basal Tillite / Diamictite (Boulder Bed), Rikba Plant Bed, Khaki-green \"Needle Shales\", and turbiditic varvites.</b></td>
                <td><b>Widespread continental glaciation across Gondwanaland (glaciomarine and periglacial outwash deposits). NO COAL SEAMS.</b></td>
              </tr>
              <tr>
                <td><b>Karharbari Formation</b></td>
                <td>Early Permian (Sakmarian)</td>
                <td>Coarse, pebbly arkosic sandstones, reworked tillites, and thin coal seams.</td>
                <td>Transition from glacial retreat to cool-temperate humid climate.</td>
              </tr>
              <tr>
                <td><b>Barakar Formation</b></td>
                <td>Early Permian (Artinskian-Kungurian)</td>
                <td>Coarse white sandstones, shales, and <b>thick, high-grade workable coal seams</b>.</td>
                <td>Warm-temperate, humid, luxuriant <i>Glossopteris</i> swamp forest. Major coal measures of India.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>48.2 The Talchir Boulder Bed (Diamictite)</h3>
        <p>The Talcher (Talchir) coalfield in Odisha is the historical type locality where W.T. Blanford and H.F. Blanford (1856) first discovered the <b>Talchir Boulder Bed</b>. It consists of unassorted, faceted, polished, and striated boulders and pebbles of Archean granite, quartzite, and amphibolite embedded in a dense fine-grained matrix of silt and clay. This tillite is equivalent to the Dwyka tillite of South Africa and the Bacchus Marsh tillite of Australia, providing irrefutable proof of the Permo-Carboniferous Southern Hemisphere Gondwana glaciation.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (A)</span>
          <p><b>Correct Answer: (A) Glacial and Periglacial deposits</b> — The base of the Gondwana succession in the Talcher coalfield (and across peninsular India) is the <b>Talchir Formation</b>, marked by a basal pile of <b>glacial tillites (Boulder Bed) and periglacial outwash deposits</b>.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Glacial and Periglacial deposits — CORRECT:</b> The hallmark of the basal Talchir Formation: tillites with striated erratics and periglacial needle shales/varves deposited by retreating ice sheets.</li>
          <li><b>(B) Fossiliferous shale — INCORRECT:</b> Fossiliferous shales become common only in younger post-glacial units; the basal Talchir tillite is devoid of animal fossils.</li>
          <li><b>(C) Glossopteris flora — INCORRECT:</b> The peak of <i>Glossopteris</i> flora characterizes the post-glacial coal-forming Barakar and Raniganj Formations; Talchir yields only sparse pioneer forms (<i>Gangamopteris cyclopteroides</i>).</li>
          <li><b>(D) Talcher sandstone — INCORRECT:</b> The defining basal lithology is the glacial boulder tillite bed, not ordinary sandstone.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Lower Gondwana Stratigraphic Column</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Formation Name</th>
                <th>Standard Age</th>
                <th>Economic Importance</th>
                <th>Diagnostic Macroflora</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Raniganj Formation</b></td>
                <td>Late Permian (Wuchiapingian)</td>
                <td>Workable superior-grade coal seams</td>
                <td><i>Glossopteris, Vertebraria, Schizoneura</i></td>
              </tr>
              <tr>
                <td><b>Barren Measures (Kulti)</b></td>
                <td>Middle Permian</td>
                <td>Ironstone shales; <b>completely non-coal-bearing</b></td>
                <td>Impoverished flora</td>
              </tr>
              <tr>
                <td><b>Barakar Formation</b></td>
                <td>Early Permian</td>
                <td><b>Chief coal-bearing horizon of India ($> 80\\%$ coal reserves)</b></td>
                <td><i>Glossopteris, Gangamopteris</i></td>
              </tr>
              <tr>
                <td><b>Karharbari Formation</b></td>
                <td>Early Permian</td>
                <td>Basal workable coal seams</td>
                <td><i>Gondwanidium, Buriadia</i></td>
              </tr>
              <tr>
                <td><b>Talchir Formation</b></td>
                <td>Late Carboniferous - Early Permian</td>
                <td><b>Non-coaliferous; glacial boulder tillite</b></td>
                <td><i>Gangamopteris</i> (pioneer flora), <i>Noeggerathiopsis</i></td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    49: {
        "title": "Q49: Tethyan Himalayan Paleozoic: Muth Quartzite & Arthropod Trace Fossils",
        "part1": """
        <h3>49.1 Stratigraphic Setting of the Muth Quartzite in Spiti</h3>
        <p>In Himalayan Paleozoic stratigraphy (O.N. Bhargava, 2011, <i>The Indian Subcontinent and Tethys</i>; Gansser, 1964; Srikantia, 1981; Ramakrishnan & Vaidyanadhan, Vol. 2, Ch. 27), the <b>Muth Quartzite</b> is one of the most prominent, snow-white regional marker horizons running continuously along the Tethyan Himalayan belt from Kashmir, Zanskar, and Spiti through Kumaon into Nepal:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Lithostratigraphic Formation</th>
                <th>Chronostratigraphic Age</th>
                <th>Diagnostic Lithological Facies</th>
                <th>Paleoenvironmental & Paleontological Characteristics</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Lipak Formation (Overlying)</b></td>
                <td>Early Carboniferous (Tournaisian-Visean)</td>
                <td>Fossiliferous marine limestones, gypsum, and dark shales.</td>
                <td>Syringothyris fauna, productive crinoidal biostromes.</td>
              </tr>
              <tr>
                <td><b>Muth Quartzite (Marker Horizon)</b></td>
                <td><b>Middle to Late Devonian</b></td>
                <td><b>Super-mature, massive, pure white orthoquartzite (> 95-98% quartz) with silica cement and cross-bedding.</b></td>
                <td>High-energy coastal barrier, shoreface, and beach sands. Body fossils are exceedingly rare due to wave winnowing and quartz recrystallization. <b>Dominated by Arthropod Trace Fossils (Ichnofossils).</b></td>
              </tr>
              <tr>
                <td><b>Takche Formation (Underlying)</b></td>
                <td>Late Ordovician to Silurian</td>
                <td>Coralline limestones, siltstones, and dolomites.</td>
                <td>Halysites, Favosites coral-stromatoporoid bioherms.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>49.2 Ichnology of the Muth Quartzite</h3>
        <p>Because body fossils are virtually absent, the environmental and biological dynamics of the Devonian Muth Quartzite are deciphered exclusively from trace fossils (ichnofossils) belonging to the shallow-marine <b>Cruziana and Skolithos ichnofacies</b>:</p>
        <ul>
          <li><b>Cruziana:</b> Bilobed furrowing and feeding traces produced by primitive benthic <b>arthropods (trilobites)</b>.</li>
          <li><b>Rusophycus:</b> Bilobed resting and nesting traces of <b>arthropods</b>.</li>
          <li><b>Diplichnites:</b> Parallel trackways of walking <b>arthropod appendages</b>.</li>
        </ul>
        <p>Hence, the trace fossils famously described and identified from the Lower/Middle Devonian Muth Quartzite in Spiti are unequivocally <b>arthropod trace fossils</b>.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (D)</span>
          <p><b>Correct Answer: (D) Arthropod</b> — The trace fossils described from the Lower-Middle Devonian Muth Quartzite in Spiti represent the <i>Cruziana</i> and <i>Rusophycus</i> ichnofacies, which are trackways and burrows created by <b>Arthropods</b> (trilobites and benthic arthropod ancestors).</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) Nautilus — INCORRECT:</b> <i>Nautilus</i> is a pelagic shelled cephalopod mollusc whose fossil forms leave body fossils (shells), not typical sandstone trace fossil trackways in the Muth Quartzite.</li>
          <li><b>(B) Unio — INCORRECT:</b> <i>Unio</i> is a modern freshwater bivalve mollusc (unionid) found in Cenozoic fresh waters; it did not exist in the Devonian marine Tethys.</li>
          <li><b>(C) Pelecypod — INCORRECT:</b> While bivalves (pelecypods) produce <i>Lockeia</i> bivalve resting traces, the predominant, diagnostic trace fossil assemblage described from the Muth Quartzite is the arthropod suite.</li>
          <li><b>(D) Arthropod — CORRECT:</b> The diagnostic bilobed tracks and walking traces (*Cruziana*, *Rusophycus*, *Diplichnites*) recorded from the Muth Quartzite are universally attributed to marine <b>arthropods</b>.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Spiti Paleozoic Succession Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Formation</th>
                <th>Age</th>
                <th>Diagnostic Fauna / Marker Attribute</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Kuling Formation</b></td>
                <td>Late Permian</td>
                <td><i>Cyclolobus</i> ammonoids, <i>Costiferina</i> brachiopods</td>
              </tr>
              <tr>
                <td><b>Po Formation</b></td>
                <td>Carboniferous</td>
                <td><i>Fenestella</i> bryozoan shale, <i>Protoretepora</i></td>
              </tr>
              <tr>
                <td><b>Lipak Formation</b></td>
                <td>Early Carboniferous</td>
                <td><i>Syringothyris cuspidata</i> brachiopod limestone</td>
              </tr>
              <tr>
                <td><b>Muth Quartzite</b></td>
                <td><b>Devonian</b></td>
                <td><b>Snow-white orthoquartzite; Arthropod trace fossils (*Cruziana*)</b></td>
              </tr>
              <tr>
                <td><b>Takche Formation</b></td>
                <td>Silurian</td>
                <td>Tabulate corals (<i>Favosites, Halysites</i>)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    },

    50: {
        "title": "Q50: Biostratigraphy: Ammonites as Index Fossils in Jurassic Stratigraphy",
        "part1": """
        <h3>50.1 Ammonite Evolution & Biostratigraphic Utility</h3>
        <p>In invertebrate paleontology and biostratigraphy (Arkell, 1956, <i>Jurassic Geology of the World</i>; Sam Boggs Jr., Ch. 15; Raup & Stanley, <i>Principles of Paleontology</i>), <b>ammonites (Ammonoidea)</b> represent the premier, golden benchmark of <b>index fossils (guide fossils / zone fossils)</b> for the Mesozoic Era, and most spectacularly for the <b>Jurassic Period</b>:</p>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Index Fossil Criterion</th>
                <th>Theoretical Biological Definition</th>
                <th>Fulfillment by Jurassic Ammonites</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>1. Rapid Evolutionary Rate</b></td>
                <td>Rapid morphological innovation and speciation over short geological time spans.</td>
                <td><b>Extremely rapid evolution of complex suture lines (Goniatitic → Ceratitic → Ammonitic with complex folioles and lobes).</b> Species turnover every $\\sim 0.5 - 1.0\\text{ Ma}$.</td>
              </tr>
              <tr>
                <td><b>2. Narrow Stratigraphic Range</b></td>
                <td>Individual species restricted to narrow chronostratigraphic intervals.</td>
                <td>Enables ultra-fine division of Jurassic stages into sub-stages and <b>standard ammonite biozones</b> (e.g. 60+ biozones in the Jurassic).</td>
              </tr>
              <tr>
                <td><b>3. Wide Geographic Distribution</b></td>
                <td>Cosmopolitan dispersion across multiple basins and ocean realms.</td>
                <td><b>Pelagic, free-swimming nektonic marine mode of life</b>; drift shells carried worldwide across the Tethys, Pacific, and Boreal seaways.</td>
              </tr>
              <tr>
                <td><b>4. High Abundance & Distinct Morphologies</b></td>
                <td>Easily identified and frequently preserved in sedimentary strata.</td>
                <td>Robust, easily fossilized aragonitic coiled shells with distinct ribbing, keels, and suture lines.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h3>50.2 Application in Indian Jurassic Basins</h3>
        <p>In the world-famous marine Jurassic succession of <b>Kutch (Kachchh)</b> in Gujarat (Waagen, 1875; Spath, 1924), the stratigraphy is subdivided into four formations calibrated entirely against standard European ammonite biozones:</p>
        <ul>
          <li><b>Patcham Formation (Bathonian):</b> <i>Macrocephalites triangularis</i> zone.</li>
          <li><b>Chari Formation (Callovian-Oxfordian):</b> <i>Macrocephalites macrocephalus, Reineckeia, Peltoceras athleta</i> zones.</li>
          <li><b>Katrol Formation (Kimmeridgian):</b> <i>Waagenia, Aspidoceras, Katroliceras</i> zones.</li>
          <li><b>Umia Formation (Tithonian-Neocomian):</b> <i>Virgatosphinctes, Micracanthoceras</i> zones.</li>
        </ul>
        <p>Without ammonites serving as <b>index fossils</b>, high-resolution global chronocorrelation of the Jurassic would be physically impossible.</p>
        """,
        "part2": """
        <div class="verified-box">
          <span class="v-badge">VERIFIED ANSWER: OPTION (B)</span>
          <p><b>Correct Answer: (B) index fossil</b> — Jurassic stratigraphy worldwide (and in Indian basins like Kutch and Spiti) is universally based on the use of ammonites as <b>index fossils</b> (zone fossils) due to their rapid evolutionary rates, short stratigraphic ranges, and widespread marine dispersal.</p>
        </div>

        <h3>Option-by-Option Critical Dissection</h3>
        <ul>
          <li><b>(A) leaked fossil — INCORRECT:</b> A leaked fossil (or stratigraphic leak) is an anomalous reworked fossil introduced into older strata through solution cavities, fractures, or burrows; it is a geological contamination phenomenon, not a biostratigraphic method.</li>
          <li><b>(B) index fossil — CORRECT:</b> Standard paleontological terminology: a fossil characterized by wide geographic distribution, short temporal range, and rapid evolution, making it ideal for biozone correlation.</li>
          <li><b>(C) trace fossil — INCORRECT:</b> Trace fossils (ichnofossils) are tracks, trails, burrows, and borings; ammonite shells are true body fossils (calcareous mineralized skeletal material).</li>
          <li><b>(D) None of these — INCORRECT:</b> Option (B) is the universally acknowledged answer.</li>
        </ul>
        """,
        "part3": """
        <h3>High-Yield Jurassic Biostratigraphic Zonation Suite</h3>
        <div class="table-wrap">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Jurassic Stage</th>
                <th>Standard Age</th>
                <th>Key Ammonite Index Genera (Kutch Basin)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>Tithonian (Late Jurassic)</b></td>
                <td>$152 - 145\\text{ Ma}$</td>
                <td><i>Virgatosphinctes, Aulacosphinctes</i> (Umia Formation)</td>
              </tr>
              <tr>
                <td><b>Kimmeridgian</b></td>
                <td>$157 - 152\\text{ Ma}$</td>
                <td><i>Katroliceras, Aspidoceras, Pachysphinctes</i> (Katrol Formation)</td>
              </tr>
              <tr>
                <td><b>Oxfordian</b></td>
                <td>$163 - 157\\text{ Ma}$</td>
                <td><i>Mayaites, Dhosaites, Perisphinctes</i> (Dhosan Sandstone)</td>
              </tr>
              <tr>
                <td><b>Callovian</b></td>
                <td>$166 - 163\\text{ Ma}$</td>
                <td><i>Macrocephalites, Reineckeia, Peltoceras</i> (Chari Formation)</td>
              </tr>
              <tr>
                <td><b>Bathonian (Middle Jurassic)</b></td>
                <td>$168 - 166\\text{ Ma}$</td>
                <td><i>Macrocephalites triangularis, Sivajiceras</i> (Patcham Formation)</td>
              </tr>
            </tbody>
          </table>
        </div>
        """
    }
}
