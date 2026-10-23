#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 9 Part B (Q114 - Q120)
Engineering Geology: Grouting Rectification, Anisotropic Bedding Strength, Dam Foundations,
Granite Properties, Road Metal Aggregates, Stone Workability, and Roofing Slate.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q114: Geological Structure Rectified by Grouting -> Joints
# -----------------------------------------------------------------------------
def gen_q114():
    q_num = 114
    filename = "Q114_Geological_Structure_Rectified_By_Grouting_Is_Joints_Complete_Guide.html"
    title = "Q114: Engineering Geology - Foundation Grouting & Rectification of Joints"
    badge = "OPSC 2019 Geology Paper-II • Question 114 • Engineering Geology & Dam Foundations"
    h1_title = "Foundation Treatment: Pressure Grouting for Rectification of Open Rock Joints"
    meta_text = "<strong>Topic:</strong> Dam & Tunnel Foundation Treatment • <strong>Key Concept:</strong> Consolidation & Curtain Grouting of Rock Joints • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 312); Krynine & Judd (1957); F.G. Bell"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Mechanics of Rock Mass Grouting</div>
      <p>In geotechnical and dam foundation engineering, <strong>grouting</strong> is the process of injecting fluid cementitious, clay-bentonite, asphaltic, or chemical slurries under controlled hydraulic pressure via drilled boreholes into subsurface rock discontinuities. Among the primary geological structures, <strong>joints</strong> (open, interconnected tensile or shear fractures without displacement) are the principal structural defects routinely and completely <strong>rectified by grouting</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Geological Structure</th>
              <th>Physical Nature of Discontinuity</th>
              <th>Amenability to Grouting Rectification</th>
              <th>Primary Engineering Remedy</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>JOINTS (Open Fractures)</strong> (Option A)</td>
              <td><strong>Discrete, interconnected planar apertures (0.1 mm to several cm) without shear offset</strong></td>
              <td><strong>IDEAL / DIRECTLY RECTIFIED: Grout penetrates open joint networks, sealing seepage paths and monolithically bonding blocks</strong></td>
              <td><strong>Consolidation (Blanket) Grouting &amp; Curtain Grouting (IS: 6066)</strong></td>
            </tr>
            <tr>
              <td>Folds (Anticlines / Synclines) (Option B)</td>
              <td>Regional or local ductile-brittle curvature of rock strata</td>
              <td>Cannot "rectify" curvature of folded strata by grouting; only associated axial-plane tension joints can be grouted</td>
              <td>Re-align tunnel or dam axis relative to fold limbs and synclinal troughs</td>
            </tr>
            <tr>
              <td>Faults &amp; Shear Zones (Option C)</td>
              <td>Tectonic displacement planes filled with impermeable clay gouge, mylonite, or breccia</td>
              <td>Clay gouge blocks grout penetration; active faults cannot be stopped by cement injection</td>
              <td>Dental treatment (excavation of fault zone and backfilling with concrete plug) or seismic design</td>
            </tr>
            <tr>
              <td>Inclined Strata (Option D)</td>
              <td>Regional homoclinal dip of sedimentary beds</td>
              <td>Attitude (strike and dip) of strata is a geometric property that cannot be altered by grouting</td>
              <td>Rock bolting, cable anchoring, or orienting dam axis parallel to strike</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Joints</strong> are the most universal structural defects encountered in bedrock at dam, reservoir, and tunnel sites. Because open joints drastically reduce the bearing capacity of the rock mass and act as high-velocity conduits for water leakage and uplift pressure, they are systematically <strong>rectified by pressure grouting</strong>. By pumping cement-water slurry into boreholes intersecting the joint network, the voids are sealed and the jointed rock is transformed into an impervious, monolithic mass."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 15: Dams and Reservoirs, p. 312)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">Lugeon Permeability Criterion &amp; Groutability Ratio</div>
        $$\text{1 Lugeon (LU)} = \frac{1\text{ Litre of water loss}}{\text{minute} \times \text{metre of borehole}} \quad \text{at } P = 10\text{ bars (1 MPa)}$$
        $$\text{Groutability Ratio (Rock Apertures): } N_r = \frac{\text{Fissure/Joint Width } (b)}{\text{Maximum Grain Size of Cement } (D_{95})} > 3$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">When bedrock hydraulic conductivity exceeds $1\text{--}3\text{ Lugeons}$ due to open joints, foundation grouting is mandatory. Ordinary Portland Cement (OPC) grout effectively seals joints wider than $0.1\text{--}0.2\text{ mm}$, while microfine cement or chemical (silicate/acrylamide) grouts penetrate hairline joints down to $0.01\text{ mm}$.</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Consolidation vs. Curtain Grouting in Jointed Foundations</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Consolidation (Blanket) Grouting:</strong> Executed via shallow holes ($5\text{ to }15\text{ m}$ deep) drilled in a grid pattern across the entire footprint of a dam foundation at low pressures ($1.5\text{ to }3.5\text{ kg/cm}^2$). It seals near-surface relaxation and unloading joints, increases the Young's modulus of deformation ($E_m$), and prevents differential settlement.</li>
        <li><strong>Curtain (Cutoff) Grouting:</strong> Executed via a single or double line of deep boreholes ($30\text{ to }100+\text{ m}$ deep) near the upstream heel of a dam at high pressures ($5\text{ to }20+\text{ kg/cm}^2$). It creates a deep, continuous impermeable barrier across deep-seated joint systems, cutting off under-seepage and dissipating dangerous hydraulic uplift pressure ($U$) beneath the dam base.</li>
        <li><strong>Contact &amp; Backfill Grouting in Tunnels:</strong> Seals open radial joints in the blast-damaged excavation disturbed zone (EDZ) and fills overbreak cavities behind the concrete tunnel lining.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q114/grouting_rectification_rock_joints_dam_foundation.png" alt="Foundation Grouting of Rock Joints in Dam Engineering">
        <div class="fig-cap">Figure 114.1: Engineering geological cross-section of a concrete gravity dam resting on jointed bedrock, illustrating shallow grid Consolidation Grouting (strengthening jointed rock mass) and deep upstream Curtain Grouting (cutting off seepage and reducing hydraulic uplift pressure).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q114.</strong> Which type of geological structure can be rectified by grouting ?<br>
        (A) Joints<br>
        (B) Folds<br>
        (C) Faults<br>
        (D) Inclined strata
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (A) &mdash; Joints</strong>
      </div>

      <div class="option-grid">
        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">Joints</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> <strong>Joints</strong> are divisional planes or fractures in rocks along which there has been no appreciable shear displacement parallel to the fracture surface. Because joints create open apertures that weaken the rock mass and allow water leakage, they are directly and completely <strong>rectified by pressure grouting</strong>. Injecting cement or chemical grout fills the joint voids, binds individual rock blocks into a rigid monolithic mass, restores compressive strength, and makes the bedrock watertight.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">Folds</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Folds</strong> are macroscopic bends or undulations in layered rocks resulting from compressional tectonic stresses. Grouting cannot unbend or rectify the synclinal or anticlinal geometry of folded strata (though tension joints along a fold crest may be grouted locally).
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">Faults</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Faults</strong> are major fracture zones along which relative displacement has occurred, usually containing impermeable clay fault gouge, crushed breccia, or mylonite, and carrying potential for future seismic slip. Fault zones are treated by <em>dental treatment</em> (excavating soft gouge and plugging with reinforced concrete) rather than simple grouting, and active fault displacement cannot be stopped by grouting.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">Inclined strata</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Inclined strata</strong> represent tilted sedimentary beds dipping at an angle to the horizontal. Dip angle is a regional geometric attitude of the formation that cannot be altered or rectified by injecting grout.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Foundation Defect Treatment Methods in Engineering Geology</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Treatment Method</th>
              <th>Target Geological Defect</th>
              <th>Injection / Excavation Depth</th>
              <th>Primary Engineering Objective</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Consolidation (Blanket) Grouting</strong></td><td><strong>Near-surface open joints &amp; unloading fractures</strong></td><td>$5\text{ to }15\text{ m}$ (Grid pattern)</td><td><strong>Increase rock mass modulus ($E_m$) and bearing capacity</strong></td></tr>
            <tr><td><strong>Curtain (Cutoff) Grouting</strong></td><td><strong>Deep interconnected joint networks</strong></td><td>$30\text{ to }100+\text{ m}$ (Upstream line)</td><td><strong>Arrest under-seepage and reduce uplift pressure ($U$)</strong></td></tr>
            <tr><td>Dental Treatment (Concrete Plug)</td><td>Fault zones &amp; clay-filled shear seams</td><td>$1.5\text{ to }3\times$ width of fault seam</td><td>Excavate weak clay gouge and transfer load across fault</td></tr>
            <tr><td>Rock Bolting &amp; Cable Anchoring</td><td>Daylighting bedding planes &amp; wedge blocks</td><td>$3\text{ to }25\text{ m}$ tensioned steel</td><td>Increase normal stress ($\sigma_n$) and shear resistance along planes</td></tr>
            <tr><td>Drainage Galleries &amp; Relief Wells</td><td>Downstream seepage pressure behind grout curtain</td><td>Drilled from dam foundation gallery</td><td>Relieve residual pore water pressure downstream of curtain</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the difference between a Joint and a Fault?</div>
        <div class="pq-ans">Answer: A joint is a fracture with zero (or negligible) shear displacement parallel to the plane; a fault is a fracture showing measurable shear displacement.</div>
        <div class="pq-exp">Both are brittle fractures, but displacement across the fracture plane distinguishes a fault from a joint.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. How is the Lugeon unit defined in dam foundation investigations?</div>
        <div class="pq-ans">Answer: Water loss of 1 litre per minute per metre length of test borehole under a constant injection pressure of 10 bars (1 MPa or ~10 kg/cm²).</div>
        <div class="pq-exp">Introduced by Maurice Lugeon (1933), the Lugeonpacker test determines whether rock joints require grouting (typically required when LU &gt; 3).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Where is a grout curtain located beneath a concrete gravity dam, and why?</div>
        <div class="pq-ans">Answer: Near the upstream heel of the dam, just upstream of the foundation drainage curtain.</div>
        <div class="pq-exp">Placing the grout curtain at the upstream heel blocks reservoir water entry immediately, minimizing hydraulic head and uplift pressure across the entire dam base.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the "split-spacing" method of drilling and grouting?</div>
        <div class="pq-ans">Answer: Drilling and grouting primary holes at wide spacing (e.g., 12 m), then halving the interval with secondary (6 m), tertiary (3 m), and quaternary (1.5 m) holes until grout intake drops to zero.</div>
        <div class="pq-exp">Split-spacing systematically closes first the widest master joints and progressively seals tighter fractures while verifying closure.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why must grouting pressure be carefully limited during shallow consolidation grouting?</div>
        <div class="pq-ans">Answer: Excessive grouting pressure exceeding the overburden stress causes hydraulic jacking (uplift and heaving of horizontal bedding planes).</div>
        <div class="pq-exp">Rule of thumb: safe grouting pressure in bars is roughly $0.23\text{ to }0.33\text{ bar per metre}$ of overburden depth in stratified rock.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is "Dental Treatment" (Shasta Formula) in dam foundation engineering?</div>
        <div class="pq-ans">Answer: Excavating weak fault gouge or weathered shear zones to a calculated depth ($d$) and backfilling with monolithic concrete.</div>
        <div class="pq-exp">By the USBR Shasta formula, for a fault seam of width $b$ (in metres) under a dam of height $H$: $d = 0.00656 \cdot b \cdot H + 1.5\text{ m}$ (for $H \ge 45\text{ m}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Which type of grout is used to seal wide solution cavities carrying fast-flowing water in karstic limestone?</div>
        <div class="pq-ans">Answer: Hot asphalt (bitumen) grout or sanded thick cement-bentonite-accelerating mortar.</div>
        <div class="pq-exp">Thin cement slurry is washed away by turbulent flowing water; hot asphalt solidifies rapidly on contact with cold water to plug large karst channels.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. How is Rock Quality Designation (RQD) affected by closely spaced joints?</div>
        <div class="pq-ans">Answer: Closely spaced joints ($< 10\text{ cm}$ spacing) reduce RQD drastically because only intact core pieces $\ge 10\text{ cm}$ long are summed.</div>
        <div class="pq-exp">$\text{RQD} = \frac{\sum \text{Length of core pieces } \ge 10\text{ cm}}{\text{Total core run length}} \times 100\%$. Consolidation grouting seals these joints in situ.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q115: Strength of Compact Rock Always Greater -> Normal to Bedding Planes
# -----------------------------------------------------------------------------
def gen_q115():
    q_num = 115
    filename = "Q115_Strength_Of_Compact_Rock_Greater_Normal_To_Bedding_Planes_Complete_Guide.html"
    title = "Q115: Rock Mechanics - Anisotropic Strength Normal to Bedding Planes"
    badge = "OPSC 2019 Geology Paper-II • Question 115 • Rock Mechanics & Strength Anisotropy"
    h1_title = "Mechanical Anisotropy: Maximum Compressive Strength Normal to Bedding Planes"
    meta_text = "<strong>Topic:</strong> Strength Anisotropy of Stratified Rocks • <strong>Key Concept:</strong> Donath's U-Shaped Curve &amp; Loading Normal to Bedding • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 287); F.A. Donath (1961); Jaeger, Cook &amp; Zimmerman"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Transverse Isotropy &amp; Strength Anisotropy in Rocks</div>
      <p>Stratified sedimentary rocks (sandstones, shales, limestones) and foliated metamorphic rocks (slates, phyllites, schists, gneisses) exhibit pronounced <strong>mechanical anisotropy</strong> (specifically <em>transverse isotropy</em>). Their compressive strength ($\sigma_c$) varies systematically with the orientation angle ($\beta$) between the major principal compressive stress ($\sigma_1$) and the bedding or foliation planes. In compact stratified rocks, the <strong>compressive strength is always greatest when the applied compressive stresses act normal (perpendicular, $\beta = 90^\circ$) to the bedding planes</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Stress Orientation Relative to Bedding</th>
              <th>Angle $\beta$ (Between $\sigma_1$ and Bedding Plane)</th>
              <th>Dominant Failure Mechanism</th>
              <th>Relative Compressive Strength ($\sigma_c$)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>STRESSES NORMAL TO BEDDING PLANES</strong> (Option A)</td>
              <td><strong>$\beta = 90^\circ$ (Perpendicular)</strong></td>
              <td><strong>Shear fracture must cut across intact mineral grains and all strong layers; bedding planes are pressed tightly shut</strong></td>
              <td><strong>MAXIMUM STRENGTH ($\sigma_{c,\max}$)</strong></td>
            </tr>
            <tr>
              <td>Stresses Parallel to Bedding Planes (Option B)</td>
              <td>$\beta = 0^\circ$ (Parallel)</td>
              <td>Axial tensile splitting along weak bedding interfaces and Euler buckling of thin individual laminae</td>
              <td>High-to-Intermediate ($\approx 0.70\text{--}0.85\,\sigma_{c,90^\circ}$), susceptible to splitting</td>
            </tr>
            <tr>
              <td>Stresses Inclined at $45^\circ$ to Bedding (Option C)</td>
              <td>$\beta = 45^\circ$</td>
              <td>High resolved shear stress ($\tau = \frac{1}{2}\sigma_1 \sin 2\beta$) directly along weak bedding planes triggers slip</td>
              <td>Very Low Strength (Near the trough of the U-curve)</td>
            </tr>
            <tr>
              <td>Stresses Inclined at $60^\circ$ (or $30^\circ$ to $\sigma_1$) (Option D)</td>
              <td>$\beta \approx 30^\circ\text{--}45^\circ$ to $\sigma_1$</td>
              <td>Critical Mohr-Coulomb slip angle ($\beta_{\text{crit}} = 45^\circ - \phi_j/2 \approx 30^\circ$): pure sliding along bedding</td>
              <td><strong>ABSOLUTE MINIMUM STRENGTH ($\sigma_{c,\min}$)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "In stratified and laminated rocks, the compressive strength depends strongly on the direction of loading relative to the bedding planes. <strong>The strength of a compact rock is always greatest when the compressive stresses are applied normal (perpendicular) to the bedding planes</strong>, because the compressive load closes the bedding planes rather than splitting them apart, forcing any rupture surface to shear across the full thickness of the rock layers."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 13: Engineering Properties of Rocks, p. 287)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">Jaeger's Single Plane of Weakness Theory (1960) &amp; Anisotropy Index</div>
        $$\sigma_1 - \sigma_3 = \frac{2\left(c_j + \sigma_3 \tan\phi_j\right)}{\left(1 - \tan\phi_j \cot\beta\right)\sin 2\beta}$$
        $$\text{Minimum Strength Angle: } \beta_{\min} = 45^\circ - \frac{\phi_j}{2} \approx 25^\circ\text{--}35^\circ \quad \text{(to }\sigma_1\text{)}$$
        $$\text{Strength Anisotropy Ratio: } R_c = \frac{\sigma_{c(90^\circ)}}{\sigma_{c(\min)}}$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">Here $c_j$ and $\phi_j$ are the cohesion and friction angle of the bedding plane. When $\sigma_1$ is applied <strong>normal to bedding ($\beta = 90^\circ$)</strong>, $\sin 2\beta = 0$, making sliding along the bedding plane impossible ($\sigma_1 \to \infty$ for bedding slip), so failure is governed entirely by the much higher intact rock matrix strength ($c_m, \phi_m$).</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Engineering Application: Placing Stones on Their "Natural Bed"</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Masonry &amp; Dam Pier Construction ("Natural Bed" Rule):</strong> In civil engineering and stone masonry, dressed sedimentary and metamorphic blocks (sandstone, limestone, gneiss) must always be laid with their <strong>bedding planes horizontal (i.e., normal to the vertical compressive gravity load)</strong>.</li>
        <li><strong>Consequence of Face-Bedding ($\beta = 0^\circ$):</strong> If stone blocks are placed with bedding planes vertical and parallel to load ("face-bedded"), moisture penetration and axial compressive stress cause tensile delamination, buckling, and spalling of outer rock sheets.</li>
        <li><strong>Consequence of Oblique Bedding ($\beta = 30^\circ\text{--}60^\circ$):</strong> Maximum resolved shear stress acts along the bedding planes, leading to premature shear sliding at a fraction ($20\%\text{--}50\%$) of the intact rock strength.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q115/anisotropic_rock_strength_stress_vs_bedding.png" alt="Anisotropic Rock Strength vs Bedding Orientation (Donath U-Curve)">
        <div class="fig-cap">Figure 115.1: Jaeger-Donath U-shaped strength anisotropy curve plotting Unconfined Compressive Strength ($\sigma_c$) against bedding inclination angle ($\beta$), showing peak strength when stress is applied normal to bedding ($\beta = 90^\circ$) and minimum strength at oblique shear inclinations ($\beta \approx 30^\circ\text{--}45^\circ$).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q115.</strong> When is the strength of a compact rock always greater ?<br>
        (A) When stresses are normal to bedding planes<br>
        (B) When stresses are parallel to bedding planes<br>
        (C) When stresses are inclined at 45° to bedding planes<br>
        (D) When stresses are inclined at 60° to bedding planes
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (A) &mdash; When stresses are normal to bedding planes</strong>
      </div>

      <div class="option-grid">
        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">When stresses are normal to bedding planes</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> When compressive stresses act <strong>normal (perpendicular, $90^\circ$) to the bedding planes</strong>, the normal stress across the bedding interfaces is maximized while resolved shear stress along the bedding planes is zero ($\tau = 0$). The bedding planes are compressed tightly together, preventing delamination or slip, and forcing the rock to fail only by shearing across the strong intact mineral grains. Hence, compressive strength is always greatest normal to bedding.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">When stresses are parallel to bedding planes</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> When compressive stress acts <strong>parallel to bedding planes</strong> ($\beta = 0^\circ$), lateral Poisson expansion induces tensile stress perpendicular to the bedding planes, causing premature axial splitting (cleavage delamination) and buckling of individual laminae.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">When stresses are inclined at 45° to bedding planes</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> At $45^\circ$ inclination, the resolved shear stress ($\tau = \frac{1}{2}\sigma_1 \sin 90^\circ = 0.5\,\sigma_1$) reaches its theoretical maximum along the weak bedding planes, causing easy shear sliding and very low compressive strength.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">When stresses are inclined at 60° to bedding planes</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> When the normal to the bedding plane is at $60^\circ$ (meaning $\sigma_1$ is inclined at $30^\circ$ to the bedding plane, $\beta = 45^\circ - \phi/2$), Mohr-Coulomb frictional sliding occurs along the bedding plane at the absolute lowest stress on Donath's U-curve.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Ramamurthy (1993) Classification of Rock Strength Anisotropy</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Anisotropy Class</th>
              <th>Anisotropy Ratio $R_c = \sigma_{c(90^\circ)} / \sigma_{c(\min)}$</th>
              <th>Typical Rock Lithologies</th>
              <th>Engineering Behaviour</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Isotropic</td><td>$1.0 - 1.1$</td><td>Massive Granite, Gabbro, Basalt, Pure Quartzite</td><td>Strength independent of loading direction</td></tr>
            <tr><td>Fairly Anisotropic</td><td>$1.1 - 2.0$</td><td>Thick-bedded Sandstone, Massive Limestone</td><td>Moderate strength peak at $\beta = 90^\circ$</td></tr>
            <tr><td>Moderately Anisotropic</td><td>$2.0 - 4.0$</td><td>Laminated Siltstone, Shale, Banded Gneiss</td><td>Distinct U-shaped curve; must load normal to bedding</td></tr>
            <tr><td><strong>Highly / Very Highly Anisotropic</strong></td><td><strong>$4.0 - >6.0$</strong></td><td><strong>Slate, Phyllite, Mica Schist, Graphitic Schist</strong></td><td><strong>Severe weakness at $\beta = 30^\circ\text{--}45^\circ$; highest strength at $\beta = 90^\circ$</strong></td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is meant by placing a building stone on its "natural bed" in masonry construction?</div>
        <div class="pq-ans">Answer: Laying the stone so that its original sedimentary bedding planes are horizontal and perpendicular (normal) to the vertical line of compressive load.</div>
        <div class="pq-exp">This maximizes compressive strength and prevents exfoliation or splitting of outer stone faces.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. How should stones be placed in a masonry arch or cornice?</div>
        <div class="pq-ans">Answer: In an arch, bedding planes should be oriented radial (so that tangential arch thrust acts normal to the bedding planes).</div>
        <div class="pq-exp">Because the line of thrust in an arch follows the curve of the ring, radial bedding ensures compressive forces always act perpendicular to the bedding planes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. At what angle $\beta$ between $\sigma_1$ and a weak cleavage plane does a slate exhibit its minimum compressive strength?</div>
        <div class="pq-ans">Answer: At $\beta = 45^\circ - \phi_j/2$, which typically lies between $25^\circ$ and $35^\circ$ to the direction of $\sigma_1$.</div>
        <div class="pq-exp">Proven experimentally by F.A. Donath (1961) on Martinsburg slate and theoretically by J.C. Jaeger (1960).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. If a laminated sandstone has $\sigma_{c(90^\circ)} = 90\text{ MPa}$ and $\sigma_{c(30^\circ)} = 30\text{ MPa}$, what is its Strength Anisotropy Ratio ($R_c$)?</div>
        <div class="pq-ans">Answer: $R_c = 90 / 30 = 3.0$ (Moderately Anisotropic).</div>
        <div class="pq-exp">$R_c = \sigma_{c(90^\circ)} / \sigma_{c(\min)} = 90 / 30 = 3.0$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why is compressive strength at $\beta = 90^\circ$ consistently higher than at $\beta = 0^\circ$?</div>
        <div class="pq-ans">Answer: At $\beta = 90^\circ$, failure requires shearing across all layers; at $\beta = 0^\circ$, layers fail at lower stress by tensile axial splitting and buckling of thin laminae.</div>
        <div class="pq-exp">Even without sliding along bedding, parallel loading ($\beta = 0^\circ$) suffers from column buckling of individual laminations.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What happens to the strength anisotropy of a foliated rock as confining pressure ($\sigma_3$) is increased to very high levels?</div>
        <div class="pq-ans">Answer: Strength anisotropy decreases as high confining pressure suppresses slip along weak planes and induces ductile flow.</div>
        <div class="pq-exp">Under high $\sigma_3$, frictional resistance ($\sigma_n \tan\phi_j$) across bedding increases markedly, reducing the depth of the U-curve trough.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. In point load testing ($I_{s(50)}$) of anisotropic rock cores, how is the Point Load Strength Anisotropy Index ($I_{a(50)}$) defined?</div>
        <div class="pq-ans">Answer: The ratio of mean $I_{s(50)}$ measured perpendicular to planes of weakness (axial test) to mean $I_{s(50)}$ measured parallel to planes of weakness (diametral test).</div>
        <div class="pq-exp">$I_{a(50)} = I_{s(50)\perp} / I_{s(50)\parallel}$ according to ISRM suggested methods.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. How does bedding dip affect foundation bearing capacity beneath a dam?</div>
        <div class="pq-ans">Answer: Horizontal beds (normal to vertical dam weight) provide the highest vertical bearing capacity, though gently upstream-dipping beds ($10^\circ\text{--}30^\circ$) are best for resisting resultant inclined thrust.</div>
        <div class="pq-exp">Resultant force of dam weight ($\downarrow W$) and horizontal reservoir water thrust ($\rightarrow P$) is inclined downstream, so beds dipping gently upstream meet the resultant force nearly at $90^\circ$ (normal to bedding!).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q116: Best Site for Dam Construction -> A site with a granitic bedrock
# -----------------------------------------------------------------------------
def gen_q116():
    q_num = 116
    filename = "Q116_Best_Site_For_Dam_Construction_Granitic_Bedrock_Complete_Guide.html"
    title = "Q116: Dam Engineering Geology - Ideal Foundation on Granitic Bedrock"
    badge = "OPSC 2019 Geology Paper-II • Question 116 • Dam Site Selection & Foundation Geology"
    h1_title = "Dam Foundation Geology: Why Massive Granitic Bedrock Is the Premier Site"
    meta_text = "<strong>Topic:</strong> Geological Investigation of Dam Sites • <strong>Key Concept:</strong> Bearing Capacity, Impermeability &amp; Solubility of Bedrock • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 302); Parbin Singh; Krynine &amp; Judd"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Geological Criteria for Dam Foundations</div>
      <p>A major concrete gravity, arch, or embankment dam imposes immense vertical dead loads (up to $3\text{--}6\text{ MPa}$), horizontal reservoir water thrusts, and high hydraulic head gradients on its foundation. An ideal dam site requires bedrock with <strong>high unconfined compressive strength (bearing capacity), negligible primary permeability, zero chemical solubility, and high resistance to sliding and erosion</strong>. Among the given geological settings, <strong>a site with a granitic bedrock</strong> (massive plutonic igneous rock) is universally the <strong>best site for dam construction</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Candidate Dam Site Bedrock</th>
              <th>Unconfined Compressive Strength ($\sigma_c$)</th>
              <th>Permeability &amp; Seepage Hazard</th>
              <th>Suitability for Dam Construction</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>SITE WITH GRANITIC BEDROCK</strong> (Option A)</td>
              <td><strong>Very High ($100\text{--}250\text{ MPa}$)</strong></td>
              <td><strong>Impervious crystalline fabric ($\phi < 1\%$); chemically insoluble in water</strong></td>
              <td><strong>BEST / IDEAL FOUNDATION: Supports highest concrete gravity and arch dams</strong></td>
            </tr>
            <tr>
              <td>Site with Good Shear Fractures (Option B)</td>
              <td>Severely reduced along shear planes ($c \to 0$)</td>
              <td>High secondary permeability and piping of fault gouge</td>
              <td>Hazardous: Prone to sliding failure, differential settlement, and leakage</td>
            </tr>
            <tr>
              <td>Lateritic Zone (Option C)</td>
              <td>Low &amp; variable ($2\text{--}25\text{ MPa}$; softens when saturated)</td>
              <td>Highly porous, vesicular/vermicular cavities; high seepage</td>
              <td>Unsuitable for major masonry/concrete dams; requires deep stripping to fresh rock</td>
            </tr>
            <tr>
              <td>Site with Limestone Bedrock (Option D)</td>
              <td>Moderate-to-High intact ($50\text{--}120\text{ MPa}$), but cavernous</td>
              <td>Severe karstic solution channels, caverns, and sinkholes ($\text{CaCO}_3$ dissolution)</td>
              <td>Highly problematic: Prone to catastrophic reservoir leakage and foundation collapse</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Massive igneous rocks such as granites, syenites, diorites, and gabbros are the strongest and most desirable foundation rocks for any type of dam.</strong> Fresh, unweathered granitic bedrock possesses an interlocking crystalline texture with compressive strength far exceeding any load imposed by the tallest dam, is virtually impervious to water, and is completely immune to solution by percolating reservoir water."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 15: Dams and Reservoirs, p. 302)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">Dam Stability Safety Factors on Granitic Bedrock</div>
        $$\text{Sliding Safety Factor: } F_s = \frac{c \cdot A + (W - U)\tan\phi}{P_w} > 1.5\text{--}4.0$$
        $$\text{Bearing Capacity Check: } \sigma_{\max} = \frac{W}{B}\left(1 + \frac{6e}{B}\right) \le q_{\text{allowable}} \approx \frac{\text{UCS}}{F}$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">Here $W$ is dam weight, $U$ is hydraulic uplift force, $P_w$ is horizontal water pressure, $c$ is concrete-rock bond cohesion, and $\phi$ is friction angle. Fresh granite offers high friction ($\phi \approx 45^\circ\text{--}55^\circ$), strong concrete-to-quartz/feldspar bond cohesion ($c \approx 1.5\text{--}3.0\text{ MPa}$), and allowable bearing capacity $> 5\text{--}10\text{ MPa}$.</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Why Limestone, Laterite, and Sheared Rock Fail as Ideal Dam Foundations</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Karstic Limestone Hazard (Option D):</strong> Carbonic acid in natural water dissolves calcite ($\text{CaCO}_3 + \text{H}_2\text{O} + \text{CO}_2 \rightleftharpoons \text{Ca}^{2+} + 2\text{HCO}_3^-$), enlarging joints into subterranean caverns and solution conduits. Famous engineering disasters/remediations (e.g., Hales Bar Dam, Camarasa Dam, Kopili Dam) occurred because reservoirs built on limestone drained through underground karst networks.</li>
        <li><strong>Shear Fractures Hazard (Option B):</strong> Shear zones contain slickensided clay gouge with very low residual friction ($\phi_r \approx 12^\circ\text{--}20^\circ$), creating potential sliding planes beneath the dam heel and toe.</li>
        <li><strong>Lateritic Zone Hazard (Option C):</strong> Laterite is a deeply leached tropical residual weathering profile rich in hydrous iron and aluminium oxides with vermicular tubular voids and underlying soft kaolinitic saprolite ("lithomarge" clay) that loses strength upon saturation.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q116/granitic_bedrock_dam_site_engineering.png" alt="Comparative Dam Foundation Geology: Granitic Bedrock vs Limestone, Shear Zone, and Laterite">
        <div class="fig-cap">Figure 116.1: Engineering geological evaluation of four candidate dam foundations: (A) Massive Granitic Bedrock (ideal interlocking, high-strength, impervious foundation) vs. hazardous alternatives (B) Sheared fracture zone, (C) Porous lateritic profile, and (D) Cavernous karstic limestone.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q116.</strong> Which of the following could be the best site for a dam construction ?<br>
        (A) A site with a granitic bedrock<br>
        (B) A site with good shear fractures<br>
        (C) Lateritic zone<br>
        (D) A site with limestone bedrock
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (A) &mdash; A site with a granitic bedrock</strong>
      </div>

      <div class="option-grid">
        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">A site with a granitic bedrock</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> <strong>Granite</strong> is a holocrystalline, coarse-grained plutonic igneous rock with an interlocking texture of quartz and feldspar. It provides very high crushing strength ($100\text{--}250\text{ MPa}$), high shear resistance, near-zero primary porosity/permeability, and complete insolubility in water. Hence, a site with granitic bedrock is universally the best and safest site for constructing any major dam.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">A site with good shear fractures</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Shear fractures represent planes of tectonic rupture with crushed rock and slickensided clay gouge. They drastically lower the shear strength and bearing capacity of the foundation and create pathways for piping and sliding failure.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">Lateritic zone</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Laterite is a porous, cavernous residual soil/duricrust often underlain by soft, plastic lithomargic clay. It has high permeability, low compressive strength, and undergoes severe settlement under heavy structural loads.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">A site with limestone bedrock</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Limestone ($\text{CaCO}_3$) is soluble in carbonated water and develops karst topography (solution cavities, sinkholes, and underground channels). Dams built on limestone risk severe reservoir leakage and foundation subsidence unless massive grouting remediation is undertaken.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Engineering Evaluation of Major Indian Dam Foundations</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Major Indian Dam</th>
              <th>River &amp; State</th>
              <th>Foundation Bedrock Lithology</th>
              <th>Geotechnical Characteristics &amp; Treatment</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Mettur Dam &amp; Krishnarajasagar</strong></td><td>Cauvery (TN / Karnataka)</td><td><strong>Archaean Granitic Gneiss &amp; Charnockite</strong></td><td><strong>Massive crystalline bedrock; exceptional bearing capacity &amp; minimal seepage</strong></td></tr>
            <tr><td><strong>Hirakud Dam</strong></td><td>Mahanadi (Odisha)</td><td><strong>Precambrian Granite, Gneiss &amp; Quartzite</strong></td><td><strong>Strong granitic/gneissic foundation; local fault/joint zones sealed by grouting</strong></td></tr>
            <tr><td><strong>Nagarjuna Sagar Dam</strong></td><td>Krishna (Telangana/AP)</td><td><strong>Archaean Peninsular Granite-Gneiss</strong></td><td><strong>World's largest masonry dam supported safely on massive granitic basement</strong></td></tr>
            <tr><td>Bhakra Dam</td><td>Sutlej (Himachal Pradesh)</td><td>Siwalik Sandstone alternating with Claystone/Siltstone</td><td>Soft claystone seams required deep dental concrete plugging and extensive grouting</td></tr>
            <tr><td>Kopili Hydroelectric Dam</td><td>Kopili (Assam)</td><td>Eocene Sylhet Karstic Limestone</td><td>Severe karstic caverns and acidic reservoir leakage problems</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What are the two most common modes of failure of a concrete gravity dam resting on weak bedrock?</div>
        <div class="pq-ans">Answer: (1) Sliding failure along horizontal bedding or shear planes, and (2) Overturning / Toe crushing due to excessive hydraulic uplift pressure.</div>
        <div class="pq-exp">Granitic bedrock prevents both by providing high frictional resistance against sliding and high crushing strength at the dam toe.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why is limestone bedrock particularly hazardous for reservoir water retention?</div>
        <div class="pq-ans">Answer: Because limestone dissolves in weak carbonic acid to form interconnected subterranean karst channels, sinkholes, and caverns that drain the reservoir.</div>
        <div class="pq-exp">Even if intact limestone cores show high UCS, solution-widened master joints can bypass the dam entirely.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. If a dam must be built across sedimentary strata, which dip direction of beds is safest for the dam foundation?</div>
        <div class="pq-ans">Answer: Beds dipping gently upstream ($10^\circ\text{ to }30^\circ$).</div>
        <div class="pq-exp">Upstream dip directs the resultant load nearly perpendicular to bedding and forces any seepage water to travel downward against the hydraulic gradient, preventing both sliding and leakage.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why are beds dipping gently downstream ($10^\circ\text{--}30^\circ$) the most dangerous configuration for a dam foundation?</div>
        <div class="pq-ans">Answer: The resultant force of dam weight and water pressure acts parallel to the downstream-dipping bedding planes, promoting sliding failure and downstream water leakage.</div>
        <div class="pq-exp">The tragic Malpasset Dam failure (1959) and Austin Dam failure involved downstream-dipping foliation/bedding planes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What geological precaution must still be checked when selecting a granitic bedrock site for a dam?</div>
        <div class="pq-ans">Answer: Depth of spheroidal weathering (kaolinized regolith) and presence of sheet joints (unloading fractures) parallel to the valley slopes.</div>
        <div class="pq-exp">While fresh granite is ideal, weathered granite (grus) and sheet joints must be excavated to fresh rock and consolidated by blanket grouting.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Which type of dam requires the strongest, soundest rock not only in the valley floor but also in the valley walls (abutments)?</div>
        <div class="pq-ans">Answer: Arch Dam (such as Idukki Dam in Kerala, built on massive charnockitic/granitic gneiss).</div>
        <div class="pq-exp">An arch dam transfers the majority of reservoir water load laterally by arch action into the canyon abutment walls.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is "piping" in dam foundation engineering?</div>
        <div class="pq-ans">Answer: Progressive backward internal erosion of soil or fault gouge particles beneath a dam caused by high exit hydraulic gradients ($i_{\text{exit}} \ge i_{\text{crit}}$).</div>
        <div class="pq-exp">Crystalline granitic bedrock is completely immune to piping erosion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which type of dam is preferred when the foundation consists of deep, unconsolidated alluvial sand and gravel where solid bedrock is too deep to reach?</div>
        <div class="pq-ans">Answer: Earthfill or Rockfill Embankment Dam with a wide base and an impervious clay core / cutoff trench.</div>
        <div class="pq-exp">Embankment dams distribute their weight over a very wide footprint, keeping bearing pressures low enough for soil foundations.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q117: True about Granite -> It has very high crushing strength
# -----------------------------------------------------------------------------
def gen_q117():
    q_num = 117
    filename = "Q117_True_About_Granite_Very_High_Crushing_Strength_Complete_Guide.html"
    title = "Q117: Building Stones - Engineering Properties & Crushing Strength of Granite"
    badge = "OPSC 2019 Geology Paper-II • Question 117 • Engineering Geology & Building Stones"
    h1_title = "Granite as a Dimension & Engineering Stone: Crushing Strength, Porosity, and Durability"
    meta_text = "<strong>Topic:</strong> Engineering Properties of Building Stones • <strong>Key Concept:</strong> Interlocking Holocrystalline Texture &amp; Crushing Strength of Granite • <strong>Textbooks:</strong> K.M. Bangar (p. 296); IS: 3316 (1974); Parbin Singh"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Petrological &amp; Engineering Properties of Granite</div>
      <p><strong>Granite</strong> is an acid, plutonic (intrusive) igneous rock composed essentially of quartz ($20\%\text{--}40\%$), alkali feldspar (orthoclase/microcline), and sodic plagioclase, with minor biotite or hornblende. Because it crystallizes slowly at depth under high confining pressure, its mineral grains develop a tight, <strong>holocrystalline, equigranular interlocking (hypidiomorphic granular) texture</strong>. This microstructure gives granite <strong>very high crushing (compressive) strength</strong>, extremely low porosity, superior durability, and the ability to take a mirror-like polish:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Engineering Property</th>
              <th>Standard Value for Fresh Granite</th>
              <th>Governing Mineralogical / Textural Cause</th>
              <th>Evaluation of Exam Options</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>CRUSHING (COMPRESSIVE) STRENGTH</strong></td>
              <td><strong>$1000\text{ to }2500\text{ kg/cm}^2$ ($100\text{--}250\text{ MPa}$)</strong></td>
              <td><strong>Interlocking 3D framework of hard quartz (Mohs 7) and feldspar (Mohs 6) crystals</strong></td>
              <td><strong>OPTION (A) IS TRUE: Very high crushing strength</strong></td>
            </tr>
            <tr>
              <td>Polishing Quality</td>
              <td>Takes an exquisite, durable mirror-like polish</td>
              <td>Uniform high hardness ($H = 6\text{--}7$) and zero intergranular pore cavities</td>
              <td>Option (B) ("takes poor polish") is FALSE</td>
            </tr>
            <tr>
              <td>Porosity ($n$) &amp; Water Absorption</td>
              <td>Extremely low porosity ($0.1\%\text{ to }0.8\%$); absorption $< 0.5\%$ by weight</td>
              <td>Holocrystalline plutonic solidification leaves almost no void space</td>
              <td>Option (C) ("highly porous rock") is FALSE</td>
            </tr>
            <tr>
              <td>Weathering Resistance &amp; Durability</td>
              <td>Exceptionally durable; resists frost, salt, and atmospheric decay for centuries</td>
              <td>High quartz content (chemically inert) and minimal moisture ingress</td>
              <td>Option (D) ("weathers out faster") is FALSE</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Granite</strong> is one of the strongest, hardest, and most durable of all building stones. Owing to its holocrystalline, interlocking granular texture and the predominance of hard minerals like quartz and feldspar, <strong>it possesses a very high crushing strength ranging from $1000\text{ to }2500\text{ kg/cm}^2$</strong> ($100\text{--}250\text{ MPa}$). Its porosity is less than $1\%$, it weathers extremely slowly, and it takes an excellent, lasting polish, making it ideal for bridge piers, dam foundations, heavy masonry, and decorative monumental work."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 14: Building Stones, p. 296)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">IS: 3316 (1974) Specifications for Structural Granite</div>
        $$\text{Crushing Strength: } \sigma_c = \frac{F_{\max}}{A} \ge 1000\text{ kg/cm}^2 \text{ (100 MPa)} \quad \text{(Typical: } 130\text{--}220\text{ MPa)}$$
        $$\text{Specific Gravity: } G = 2.63\text{ to }2.75 \quad \big|\quad \text{Water Absorption (24 hr)} < 0.50\%$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">Fine-grained granites display even higher crushing strength ($180\text{--}250\text{ MPa}$) than coarse-grained pegmatitic varieties ($100\text{--}150\text{ MPa}$) in accordance with the Hall-Petch grain-size strengthening relationship ($\sigma_c \propto d^{-1/2}$).</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Engineering Applications &amp; One Notable Limitation of Granite</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Heavy Load-Bearing Structures:</strong> Bridge piers, abutments, lighthouses, sea walls, dockyards, and dam foundations where immense crushing loads and hydraulic abrasion act continuously.</li>
        <li><strong>Dimension &amp; Monumental Facing Stone:</strong> Because feldspar and quartz take a brilliant, high-gloss polish and resist acid rain far better than marble or limestone, polished granite slabs are the premier architectural cladding material.</li>
        <li><strong>Fire Resistance Limitation:</strong> The one engineering weakness of granite is <em>poor fire resistance</em>. Under intense fire ($> 573^\circ\text{C}$, the $\alpha \to \beta$ quartz inversion point), quartz undergoes a sudden $0.85\%$ volumetric expansion and differential thermal expansion relative to feldspar, causing granite blocks to crack, spall, and decrepitate when doused with water.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q117/granite_crushing_strength_and_durability.png" alt="Engineering Properties of Granite: High Crushing Strength, Low Porosity, High Polish, Durability">
        <div class="fig-cap">Figure 117.1: Petrological and geotechnical summary of granite, showing its interlocking quartz-feldspar-biotite crystal fabric, superior crushing strength ($100\text{--}250\text{ MPa}$), ultra-low porosity ($< 1\%$), and high resistance to weathering.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q117.</strong> Which of the following is true about granite ?<br>
        (A) It has very high crushing strength<br>
        (B) It takes poor polish<br>
        (C) It is a highly porous rock<br>
        (D) It weathers out faster
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (A) &mdash; It has very high crushing strength</strong>
      </div>

      <div class="option-grid">
        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">It has very high crushing strength</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> <strong>Granite possesses a very high crushing (unconfined compressive) strength</strong> of $1000\text{ to }2500\text{ kg/cm}^2$ ($100\text{--}250\text{ MPa}$). Its interlocking holocrystalline fabric of hard quartz ($H=7$) and feldspar ($H=6$) crystals resists intergranular slip and compressive rupture better than almost any sedimentary rock.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">It takes poor polish</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Granite takes an <strong>excellent, mirror-like, long-lasting polish</strong> because of its dense, non-porous interlocking crystals of hard quartz and feldspar. That is why polished granite is used worldwide for countertops, monuments, and building facades.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">It is a highly porous rock</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Fresh granite is an <strong>extremely compact, non-porous rock</strong> with total porosity typically under $0.5\%\text{ to }1\%$ and water absorption below $0.5\%$.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">It weathers out faster</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> Granite is rich in quartz (the most stable mineral on Goldich's weathering stability series) and K-feldspar, and has negligible porosity to admit water. Therefore, it <strong>weathers very slowly</strong> and exhibits outstanding durability.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Engineering Comparison of Common Indian Building Stones</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Building Stone</th>
              <th>Crushing Strength ($\text{kg/cm}^2$)</th>
              <th>Porosity ($\%$)</th>
              <th>Specific Gravity ($G$)</th>
              <th>Best Civil Engineering Application</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Granite</strong></td><td><strong>$1000 - 2500$</strong></td><td><strong>$0.1 - 0.8\%$</strong></td><td><strong>$2.63 - 2.75$</strong></td><td><strong>Bridge piers, dams, sea walls, polished slabs, ballast</strong></td></tr>
            <tr><td>Basalt &amp; Trap</td><td>$1500 - 3000$</td><td>$0.1 - 1.0\%$</td><td>$2.80 - 3.00$</td><td>Road metal (aggregate), railway ballast, paving setts</td></tr>
            <tr><td>Sandstone</td><td>$350 - 1200$</td><td>$5.0 - 20.0\%$</td><td>$2.20 - 2.60$</td><td>General ashlar masonry, forts, carving, fire-resistant walls</td></tr>
            <tr><td>Limestone</td><td>$400 - 1000$</td><td>$2.0 - 15.0\%$</td><td>$2.50 - 2.70$</td><td>Flooring, cement manufacture, general building blocks</td></tr>
            <tr><td>Marble</td><td>$600 - 1200$</td><td>$0.5 - 2.0\%$</td><td>$2.65 - 2.85$</td><td>Ornamental interior carving, flooring, monumental work</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. According to Indian Standards (IS: 1121), what is the minimum crushing strength required for a stone to be classified as a good structural building stone?</div>
        <div class="pq-ans">Answer: At least $1000\text{ kg/cm}^2$ ($\approx 100\text{ MPa}$) for heavy-duty masonry; granite easily exceeds this ($1000\text{--}2500\text{ kg/cm}^2$).</div>
        <div class="pq-exp">Granite, basalt, quartzite, and charnockite all surpass the $1000\text{ kg/cm}^2$ benchmark.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why do fine-grained granites possess higher crushing strength than coarse-grained (porphyritic or pegmatitic) granites?</div>
        <div class="pq-ans">Answer: Smaller grain size restricts the initial length of Griffith microcracks along grain boundaries and cleavage planes ($\sigma_c \propto d^{-1/2}$).</div>
        <div class="pq-exp">Fine, equigranular interlocking crystals distribute stress more uniformly and arrest microcrack propagation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Why does granite have poor fire resistance despite its high crushing strength?</div>
        <div class="pq-ans">Answer: Quartz undergoes sudden volumetric expansion at $573^\circ\text{C}$ ($\alpha\text{-quartz} \to \beta\text{-quartz}$), and unequal thermal expansion of quartz and feldspar shatters the rock.</div>
        <div class="pq-exp">Compact sandstone (with siliceous cement) has much better fire resistance than granite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What should be the maximum permissible water absorption (by weight after 24 hours immersion) for a first-class building stone like granite?</div>
        <div class="pq-ans">Answer: Less than $0.5\%\text{ to }1\%$ for granite (and strictly never exceeding $5\%$ for any acceptable building stone).</div>
        <div class="pq-exp">Low water absorption guarantees immunity against freeze-thaw frost wedging and salt crystallization damage.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why does polished granite retain its exterior gloss in urban atmospheres much longer than polished marble?</div>
        <div class="pq-ans">Answer: Granite is composed of silicate minerals (quartz and feldspar, $H=6\text{--}7$) immune to weak acids, whereas marble is calcite ($\text{CaCO}_3, H=3$) which is etched by acidic rain ($\text{H}_2\text{SO}_4, \text{H}_2\text{CO}_3$).</div>
        <div class="pq-exp">Silicate minerals resist both wind-blown quartz dust abrasion and urban acid rain dissolution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What causes dark brown or rusty stains on some inferior granite building blocks over time?</div>
        <div class="pq-ans">Answer: Oxidation and hydration of accessory iron-bearing minerals such as pyrite ($\text{FeS}_2$) or abundant biotite/magnetite into limonite.</div>
        <div class="pq-exp">Dimension granites must be free of pyrite nodules to prevent unsightly rust staining and sulphuric acid release.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the typical specific gravity of granite and what does a lower value ($< 2.55$) indicate?</div>
        <div class="pq-ans">Answer: Fresh granite has $G = 2.63\text{--}2.75$; a lower value indicates incipient kaolinization (weathering of feldspars) and micro-fracturing.</div>
        <div class="pq-exp">Weathering alters dense feldspar ($G \approx 2.6$) into porous kaolinite clay ($G \approx 2.2\text{--}2.4$), reducing bulk density and strength.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. How are Rift and Grain utilized when quarrying massive granite?</div>
        <div class="pq-ans">Answer: Rift (easiest splitting plane) and Grain (second easiest plane, perpendicular to rift) are microscopic fluid-inclusion microcrack alignments used by quarrymen to split rectangular granite blocks cleanly.</div>
        <div class="pq-exp">Even though granite lacks sedimentary bedding, orthogonal rift, grain, and hardway planes allow clean dressing of blocks.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q118: Not a desirable property for road metal -> Strongly sheared / Highly porous
# -----------------------------------------------------------------------------
def gen_q118():
    q_num = 118
    filename = "Q118_Not_Desirable_Property_For_Road_Metal_Strongly_Sheared_Porous_Complete_Guide.html"
    title = "Q118: Highway Materials - Undesirable Properties of Road Metal Aggregates"
    badge = "OPSC 2019 Geology Paper-II • Question 118 • Engineering Geology & Highway Aggregates"
    h1_title = "Road Metal (Highway Aggregates): Desirable vs. Undesirable Geotechnical Properties"
    meta_text = "<strong>Topic:</strong> Geological Selection of Road Metal &amp; Pavement Aggregates • <strong>Key Concept:</strong> Crushing Strength, Hydrophobicity, Porosity &amp; Shear Defects • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 299); Parbin Singh; IRC / IS: 2386"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Desirable vs. Undesirable Properties of Road Metal</div>
      <p><strong>Road metal</strong> (crushed stone aggregate used in flexible bituminous and rigid concrete highway pavements) is subjected to intense wheel impact loads, mutual inter-particle abrasion, surface tire attrition, and moisture-induced stripping of bitumen. According to standard Indian engineering geology textbooks (e.g., <em>K.M. Bangar</em> and <em>Parbin Singh</em>) and Indian Roads Congress (IRC) specifications, road metal must be <strong>strong, tough, hard, hydrophobic (water-repelling, bitumen-loving), and non-porous/impermeable</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Aggregate Property</th>
              <th>Physical &amp; Engineering Meaning</th>
              <th>Impact on Highway Pavement Performance</th>
              <th>Desirable or Undesirable?</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Should be Hydrophobic (Option A)</td>
              <td>Repels water and exhibits strong affinity (adhesion) for asphalt/bitumen binder (e.g., basalt, dolerite, limestone)</td>
              <td>Prevents moisture "stripping" of bitumen film from aggregate surfaces during monsoon rains</td>
              <td><span style="color:#16a34a; font-weight:700;">HIGHLY DESIRABLE</span></td>
            </tr>
            <tr>
              <td>Sufficient Crushing Strength (Option B)</td>
              <td>High UCS ($> 100\text{--}150\text{ MPa}$) and Aggregate Crushing Value ($\text{ACV} < 30\%$)</td>
              <td>Withstands heavy roller compaction and axle wheel loads without pulverizing</td>
              <td><span style="color:#16a34a; font-weight:700;">HIGHLY DESIRABLE</span></td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>STRONGLY SHEARED / HIGHLY POROUS &amp; PERMEABLE</strong> (Options C &amp; D)</td>
              <td><strong>Option C: Tectonically sheared rock (flaky, pre-fractured, weak)<br>Option D: High porosity &amp; permeability (absorbs water &amp; wastes bitumen)</strong></td>
              <td><strong>Option C shatters into flaky splinters under rollers; Option D absorbs water, softens, and wastes expensive bitumen</strong></td>
              <td><span style="color:#dc2626; font-weight:700;">NOT DESIRABLE (CORRECT ANSWERS)</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "A good <strong>road metal</strong> must possess: (1) <strong>Sufficient crushing strength</strong>, hardness, and toughness to resist traffic impact and abrasion; (2) <strong>Hydrophobic character</strong> (affinity for bitumen over water) so the bituminous binder does not strip off in wet weather; (3) <strong>Low porosity and impermeability</strong>, because a <em>highly porous and permeable</em> rock absorbs water and excessive bitumen and disintegrates under wheel loads; and (4) Sound, equidimensional cubical breakage, free from <em>strongly sheared</em>, foliated, or flaky planes of weakness."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 14: Road Metals, pp. 299&ndash;300)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">IS: 2386 &amp; IRC Standard Test Limits for Road Metal Aggregates</div>
        $$\text{Aggregate Impact Value (AIV)} \le 30\% \text{ (Wearing Course)} \quad \big|\quad \text{Aggregate Crushing Value (ACV)} \le 30\%$$
        $$\text{Los Angeles Abrasion Value (LAAV)} \le 30\% \quad \big|\quad \text{Water Absorption} \le 2.0\% \text{ (Strictly non-porous)}$$
        $$\text{Combined Flakiness &amp; Elongation Index} \le 35\% \quad \text{(Rejects sheared/schistose rocks)}$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">Note on OPSC Exam Key &amp; Textbook Verbatim Source: In standard Indian geology MCQ banks (derived verbatim from Bangar/Parbin Singh's list of road metal properties where <em>"Porosity: Road metal should NOT be porous and permeable"</em> is a dedicated heading, alongside structural soundness against sheared/flaky stones), both <strong>Option (D) "Should be highly porous and permeable"</strong> and <strong>Option (C) "Should be strongly sheared"</strong> are demonstrably false/undesirable statements. Below we provide complete forensic analysis for both so candidates are 100% covered under either key interpretation.</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Hydrophobic vs. Hydrophilic Aggregates in Bituminous Roads</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Hydrophobic Rocks (Basic Rocks &amp; Limestones):</strong> Basalt, dolerite (Deccan Trap), gabbro, and compact limestone carry positive surface charges that bond strongly with negatively charged naphthenic acids in bitumen. They repel water and resist binder stripping.</li>
        <li><strong>Hydrophilic Rocks (Acidic Siliceous Rocks):</strong> Pure quartzite, sandstone, and granite have high free $\text{SiO}_2$ ($> 65\%$) carrying negative surface charges. They attract polar water molecules more strongly than bitumen, causing the bitumen film to peel off ("stripping") when submerged in rainwater unless anti-stripping amine additives are used.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q118/road_metal_aggregate_desirable_properties.png" alt="Desirable vs Undesirable Properties of Road Metal Aggregates">
        <div class="fig-cap">Figure 118.1: Engineering comparison of road metal properties: Desirable qualities (hydrophobic bitumen adhesion and high crushing strength) vs. Undesirable defects (strongly sheared/flaky rock and highly porous/permeable rock).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q118.</strong> Which of the following is not a desirable property for a road metal ?<br>
        (A) Should be hydrophobic<br>
        (B) Should have sufficient crushing strength<br>
        (C) Should be strongly sheared<br>
        (D) Should be highly porous and permeable
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (D) &mdash; Should be highly porous and permeable (and Option C &mdash; Should be strongly sheared)</strong>
      </div>

      <div class="option-grid">
        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">Should be hydrophobic</span>
            <span class="opt-badge">DESIRABLE PROPERTY</span>
          </div>
          <div class="opt-body">
            <strong>Why this IS desirable:</strong> A road metal <strong>must be hydrophobic</strong> (water-repelling, like basalt and dolerite) so that it adheres tightly to bituminous/asphalt binders and resists stripping of the bitumen coating in the presence of rainwater.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">Should have sufficient crushing strength</span>
            <span class="opt-badge">DESIRABLE PROPERTY</span>
          </div>
          <div class="opt-body">
            <strong>Why this IS desirable:</strong> A road metal <strong>must possess high crushing strength</strong> (typically $> 1000\text{ kg/cm}^2$, Aggregate Crushing Value $< 30\%$) to withstand heavy steamrollers and commercial axle loads without crushing into powder.
          </div>
        </div>

        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">Should be strongly sheared</span>
            <span class="opt-badge">UNDESIRABLE (CORRECT)</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification (Option C):</strong> A <strong>strongly sheared</strong> rock contains pervasive closely-spaced slickensides, micro-fractures, and foliation planes. When crushed for road aggregate, sheared rocks break into weak, flaky, and elongated splinters (high Flakiness Index) that snap immediately under traffic loads. Therefore, being strongly sheared is completely undesirable.
          </div>
        </div>

        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">Should be highly porous and permeable</span>
            <span class="opt-badge">UNDESIRABLE (CORRECT)</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification (Option D):</strong> A road metal must <strong>never be highly porous and permeable</strong> (IRC limits water absorption to $\le 2\%$). Highly porous and permeable aggregates absorb rainwater (losing mechanical strength and causing freeze-thaw or pore-pressure failure) and soak up large quantities of expensive liquid bitumen into internal pores without contributing to inter-particle binding.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Standard Laboratory Tests for Road Metal Aggregates (IS: 2386)</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Laboratory Test</th>
              <th>Mechanical Property Measured</th>
              <th>Testing Apparatus</th>
              <th>IRC Limit for Bituminous Wearing Course</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Aggregate Crushing Test</strong></td><td><strong>Resistance to gradual compressive crushing load</strong></td><td>Compression machine ($40\text{ tonnes}$ in $10\text{ min}$)</td><td><strong>$\text{ACV} \le 30\%$</strong></td></tr>
            <tr><td><strong>Aggregate Impact Test</strong></td><td><strong>Toughness (resistance to sudden shock/impact)</strong></td><td>Impact hammer ($13.5\text{--}14\text{ kg}$, $38\text{ cm}$ drop, $15\text{ blows}$)</td><td><strong>$\text{AIV} \le 30\%$</strong></td></tr>
            <tr><td><strong>Los Angeles Abrasion Test</strong></td><td><strong>Hardness &amp; resistance to attrition/wear</strong></td><td>Rotating steel drum with cast-iron spheres ($500\text{ rev}$)</td><td><strong>$\text{LAAV} \le 30\%$</strong></td></tr>
            <tr><td><strong>Stripping Value Test</strong></td><td><strong>Hydrophobic adhesion to bitumen in water</strong></td><td>Immersion of bitumen-coated aggregate at $40^\circ\text{C}$ for $24\text{ hr}$</td><td><strong>Stripping $\le 5\%$</strong></td></tr>
            <tr><td><strong>Water Absorption Test</strong></td><td><strong>Effective Porosity &amp; Permeability</strong></td><td>$24\text{ hr}$ immersion &amp; oven drying</td><td><strong>Absorption $\le 2.0\%$</strong></td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Distinguish between "Hydrophobic" and "Hydrophilic" road aggregates with examples.</div>
        <div class="pq-ans">Answer: Hydrophobic aggregates (basalt, dolerite, limestone) have stronger affinity for bitumen than water; hydrophilic aggregates (quartzite, granite, sandstone) attract water over bitumen, causing binder stripping.</div>
        <div class="pq-exp">Basic igneous rocks and carbonate rocks are naturally hydrophobic and superior for bituminous pavements.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which rock type in India is considered the single best all-round road metal and why?</div>
        <div class="pq-ans">Answer: Basalt and Dolerite ("Deccan Trap") because they are fine-grained, tough, hard, non-porous, break into angular cubical fragments, and are strongly hydrophobic.</div>
        <div class="pq-exp">Fine-grained basic igneous rocks combine high toughness (low AIV) with excellent bitumen adhesion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between "Attrition" and "Abrasion" in road aggregates?</div>
        <div class="pq-ans">Answer: Attrition is the mutual rubbing of aggregate stones against each other under traffic vibration (tested by Deval Attrition Test); abrasion is wear caused by external vehicle tires (tested by Dorry/Los Angeles Test).</div>
        <div class="pq-exp">The Los Angeles test measures combined abrasion, attrition, and impact.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why are flaky and elongated aggregate particles (formed from sheared or schistose rocks) rejected in road construction?</div>
        <div class="pq-ans">Answer: They orient horizontally during rolling and fracture easily across their thin dimension under traffic wheel loads, reducing pavement stability and interlock.</div>
        <div class="pq-exp">A particle is flaky if its least dimension is less than $0.6\times$ its mean dimension; elongated if its greatest dimension exceeds $1.8\times$ its mean dimension.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Why is highly porous rock doubly disadvantageous in bituminous road construction?</div>
        <div class="pq-ans">Answer: (1) It has low mechanical crushing/impact strength, and (2) its open pores absorb large quantities of expensive bitumen that does not contribute to surface bonding.</div>
        <div class="pq-exp">Additionally, absorbed water causes freeze-thaw disintegration and hydraulic pore-pressure stripping under fast wheel loads.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the ideal particle shape for road metal aggregates?</div>
        <div class="pq-ans">Answer: Angular and approximately equidimensional (cubical / tetrahedral) with rough micro-texture.</div>
        <div class="pq-exp">Angular cubical fragments provide maximum mechanical interlocking (high angle of internal friction $\phi$) and high surface area for binder adhesion.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why are rounded river gravels unsuitable for the wearing course of heavy-duty roads unless crushed?</div>
        <div class="pq-ans">Answer: Smooth, rounded pebbles lack angular edges for mechanical interlocking and slip past one another under horizontal wheel braking forces.</div>
        <div class="pq-exp">Crushing river boulders creates fresh, rough, angular fracture faces required for stability.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the "Polished Stone Value" (PSV) of a road aggregate and why is pure limestone avoided in the top skid-resistant surface of expressways?</div>
        <div class="pq-ans">Answer: PSV measures resistance of aggregate to polishing under rubber tires; pure monomineralic limestone ($H=3$) polishes smooth quickly, reducing wet skid resistance.</div>
        <div class="pq-exp">Rocks composed of minerals with contrasting hardness (e.g., dolerite or gritstone) maintain micro-roughness and high PSV as they wear differentially.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q119: Ease with which stone can be extracted and dressed -> Workability
# -----------------------------------------------------------------------------
def gen_q119():
    q_num = 119
    filename = "Q119_Ease_With_Which_Stone_Extracted_And_Dressed_Is_Workability_Complete_Guide.html"
    title = "Q119: Building Stones - Definition & Economics of Stone Workability"
    badge = "OPSC 2019 Geology Paper-II • Question 119 • Engineering Geology & Dimension Stones"
    h1_title = "Workability of Building Stones: Ease of Quarrying, Extraction, Dressing, and Carving"
    meta_text = "<strong>Topic:</strong> Selection Criteria for Dimension &amp; Building Stones • <strong>Key Concept:</strong> Workability vs. Hardness &amp; Economic Cost • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 295); Parbin Singh; R.K. Rajput"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Workability of Building Stones</div>
      <p>In engineering geology and masonry construction, the <strong>ease with which a stone can be extracted (quarried) from its natural outcrop and subsequently dressed (cut, chiseled, shaped, and planed) into required dimensions and architectural forms</strong> is formally defined as its <strong>Workability</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Term in Options</th>
              <th>Technical Definition in Geology / Civil Engineering</th>
              <th>Relevance to Stone Quarrying &amp; Dressing</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>WORKABILITY</strong> (Option B)</td>
              <td><strong>The ease and economy with which a stone can be extracted from the quarry, split, chiseled, dressed, and carved into desired shapes and sizes</strong></td>
              <td><strong>EXACT DEFINITION (Correct Answer)</strong></td>
            </tr>
            <tr>
              <td>Consistency (Option A)</td>
              <td>Degree of firmness or resistance to deformation of cohesive soils/clays (Atterberg limits: liquid, plastic, semi-solid, solid states) or fresh concrete slump</td>
              <td>Applies to cohesive soils and wet concrete paste, not hard rock dressing</td>
            </tr>
            <tr>
              <td>Easability (Option C)</td>
              <td>Non-standard colloquial distractor term; not an established geotechnical or rock mechanics property</td>
              <td>Invalid distractor</td>
            </tr>
            <tr>
              <td>Permeability (Option D)</td>
              <td>Capacity of a porous rock or soil to transmit fluids under a hydraulic gradient (Darcy's coefficient $k$)</td>
              <td>Hydraulic flow property, unrelated to mechanical dressing</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Workability:</strong> A stone is said to be workable when the effort required in its extraction (quarrying), dressing, cutting, and shaping into blocks of required size is small and economical. <strong>The ease with which a stone can be extracted and dressed is called its workability.</strong> Notice that workability and strength/hardness often oppose each other: very hard, compact igneous rocks like granite and basalt have poor workability (expensive to dress), whereas softer, bedded rocks like sandstone, limestone, and laterite possess high workability."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 14: Building Stones, p. 295)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">Geological Controls on Stone Workability &amp; Cost Optimization</div>
        $$\text{Workability} \propto \frac{\text{Regularity of Bedding / Cleavage / Rift-Grain}}{\text{Mineral Hardness } (H) \times \text{Interlocking Toughness } (T_i)}$$
        $$\text{Total Masonry Cost} = C_{\text{quarrying}} + C_{\text{dressing}} + C_{\text{transport}}$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">A phenomenon known as <strong>"Quarry Sap"</strong> (natural pore moisture present in freshly quarried sandstone, limestone, and laterite) significantly enhances workability: stones are much softer and easier to dress and carve immediately after extraction while still moist with quarry sap; once the quarry sap evaporates and dissolved silica/calcite precipitates in the outer pores ("seasoning"), the stone becomes hard, durable, and weather-resistant.</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Comparative Workability of Major Indian Dimension Stones</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>High Workability Stones (Freestones):</strong> Thick-bedded, uniform-grained <strong>Sandstones</strong> (e.g., Vindhyan sandstone of Chunar, Agra, and Jodhpur; Athgarh/Khandolite stones in Odisha) and <strong>Limestones/Marbles</strong> (e.g., Makrana marble) that cut cleanly in any direction without splintering are called <em>"freestones"</em>. <strong>Laterite</strong> when freshly quarried is cut easily with a pickaxe and hardens on exposure to air.</li>
        <li><strong>Low Workability Stones:</strong> <strong>Granite, Basalt, Trap, and Quartzite</strong> are extremely hard and tough; dressing them with hand chisels is slow and costly, restricting their traditional use to rubble masonry or mechanically sawed/polished slabs.</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q119/workability_stone_extraction_dressing.png" alt="Workability of Building Stones: Extraction, Quarry Sap, and Dressing">
        <div class="fig-cap">Figure 119.1: Engineering concept of Stone Workability, illustrating extraction along natural joints/bedding, ease of chisel dressing while containing fresh "quarry sap", and the inverse trade-off between mechanical hardness/strength and workability across rock types.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q119.</strong> Ease with which a stone can be extracted and dressed is called :<br>
        (A) Consistency<br>
        (B) Workability<br>
        (C) Easability<br>
        (D) Permeability
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (B) &mdash; Workability</strong>
      </div>

      <div class="option-grid">
        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">Consistency</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Consistency</strong> refers to the relative ease with which a cohesive soil (clay) can be deformed (quantified by Atterberg limits: Liquid Limit, Plastic Limit, Shrinkage Limit) or the fluidity/slump of freshly mixed concrete.
          </div>
        </div>

        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">Workability</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> In building stone technology and engineering geology, <strong>Workability</strong> is the exact technical term for the ease and economy with which a stone can be extracted from its quarry bed and dressed (cut, chiseled, shaped, and carved) into desired building blocks.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">Easability</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> "Easability" is a coined distractor word and not a valid engineering or geological term.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">Permeability</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Permeability</strong> measures the ability of interconnected pores or fractures in a rock to transmit fluids under a hydraulic gradient.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Workability vs. Strength Trade-off in Dimension Stones</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Type</th>
              <th>Mohs Hardness of Dominant Minerals</th>
              <th>Structural Planes Aiding Extraction</th>
              <th>Workability Rating</th>
              <th>Typical Architectural Use</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Fresh Laterite</strong></td><td>$2.5 - 3.5$ (Soft hydrous oxides)</td><td>Sectile cellular fabric when moist</td><td><strong>Very High (Cut with pickaxe)</strong></td><td>Local building blocks (Odisha/Kerala); hardens on exposure</td></tr>
            <tr><td><strong>Sandstone (Freestone)</strong></td><td>$7.0$ (Grains held by softer cement)</td><td>Regular bedding &amp; orthogonal master joints</td><td><strong>High (Easily chiseled &amp; carved)</strong></td><td>Ashlar masonry, temples, palaces, intricate carvings</td></tr>
            <tr><td><strong>Limestone &amp; Marble</strong></td><td>$3.0$ (Calcite)</td><td>Bedding / homogeneous granoblastic fabric</td><td><strong>High (Ideal for fine sculpture)</strong></td><td>Monumental carving (Taj Mahal), flooring, decorative panels</td></tr>
            <tr><td><strong>Khondalite (Odisha)</strong></td><td>$6.0 - 7.0$ (Quartz-Sillimanite-Garnet)</td><td>Gneissic foliation</td><td><strong>Moderate-to-High</strong></td><td>Famous Konark &amp; Jagannath Puri temple architecture</td></tr>
            <tr><td><strong>Granite &amp; Basalt</strong></td><td>$6.0 - 7.0$ (Interlocking crystals)</td><td>Only microscopic rift &amp; grain</td><td><strong>Low (Difficult &amp; costly to dress)</strong></td><td>Heavy engineering piers, dams, diamond-sawed slabs</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is "Quarry Sap" and why must stones be dressed before it dries out?</div>
        <div class="pq-ans">Answer: Quarry sap is the natural ground moisture containing dissolved mineral salts present in freshly quarried stone; the stone is much softer and more workable while moist, and hardens permanently once the sap evaporates at the surface.</div>
        <div class="pq-exp">Seasoning of stone (6 to 12 months in open air sheds) is performed *after* dressing so the hardened outer crust is never chiseled off.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why should a seasoned building stone never be re-dressed after seasoning is complete?</div>
        <div class="pq-ans">Answer: Evaporation of quarry sap deposits a tough, weather-resistant mineral crust on the outer surface; re-dressing strips away this protective skin and exposes the softer interior to rapid decay.</div>
        <div class="pq-exp">All cutting, carving, and dressing must be completed while the stone is green (fresh from the quarry).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a "Freestone" in masonry terminology?</div>
        <div class="pq-ans">Answer: Any fine-grained, thick-bedded sandstone or limestone that can be cut, sawed, and chiseled freely in any direction without splitting or splintering.</div>
        <div class="pq-exp">Vindhyan sandstones (Chunar, Mirzapur, Dholpur) and Gondwana Athgarh sandstones are classic Indian freestones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. How does the relationship between Workability and Durability create an optimization problem in civil engineering?</div>
        <div class="pq-ans">Answer: Soft, clayey, or porous stones have high workability (cheap to dress) but low durability and strength, whereas dense igneous stones have high durability/strength but poor workability (expensive to dress).</div>
        <div class="pq-exp">Engineers select intermediate freestones (like siliceous/ferruginous sandstone or marble) when intricate dressing and durability are both required.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which rocks were famously used in the construction of the Sun Temple at Konark and Lingaraj Temple in Bhubaneswar, Odisha?</div>
        <div class="pq-ans">Answer: Khondalite (quartz-manganese-garnet-sillimanite gneiss) for the main structure and carving, Laterite for core foundations/enclosures, and Chlorite/Serpentinite (Muguni stone) for fine doorway sculptures.</div>
        <div class="pq-exp">Chlorite schist/serpentinite is soft ($H = 2.5\text{--}3$) with exceptional workability for intricate statuary, while laterite served for foundation blocks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the difference between "Quarrying by Wedging" and "Quarrying by Blasting"?</div>
        <div class="pq-ans">Answer: Wedging uses steel plugs and feathers along natural joints/bedding to extract intact, crack-free dimension blocks; blasting uses explosives to shatter rock into irregular fragments for road metal or aggregate.</div>
        <div class="pq-exp">Blasting induces internal micro-cracks and ruins dimension building blocks, so wedging or wire-sawing is used for building stones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why is laterite exceptionally popular as a local building block in coastal Odisha, Malabar, and Konkan?</div>
        <div class="pq-ans">Answer: In the quarry bed, moist laterite is soft and sectile (easily cut into rectangular bricks with a spade/axe), and upon exposure to air, dehydration of iron hydroxides irreversibly hardens it into stone.</div>
        <div class="pq-exp">Francis Buchanan-Hamilton coined the term "Laterite" (from Latin *later* = brick) in 1807 in southern India specifically because of this property!</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which test checks whether a stone contains soluble clay or mud that reduces its durability despite high initial workability?</div>
        <div class="pq-ans">Answer: Smith's Test (agitating stone chips in clear water to check for muddy turbidity).</div>
        <div class="pq-exp">If the water remains clear, the stone is free of soluble earthy matter; if cloudy, it contains poorly cemented clay.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q120: Material Generally Used as a Roofing Slab -> Slate
# -----------------------------------------------------------------------------
def gen_q120():
    q_num = 120
    filename = "Q120_Material_Generally_Used_As_Roofing_Slab_Is_Slate_Complete_Guide.html"
    title = "Q120: Building Stones - Slate and Slaty Cleavage for Roofing Slabs"
    badge = "OPSC 2019 Geology Paper-II • Question 120 • Engineering Geology & Metamorphic Building Stones"
    h1_title = "Roofing Slate: Low-Grade Metamorphism, Slaty Cleavage, and Impervious Roofing Slabs"
    meta_text = "<strong>Topic:</strong> Metamorphic Building Materials • <strong>Key Concept:</strong> Slaty Cleavage, Splits into Thin Impervious Sheets &amp; Roofing Slabs • <strong>Textbooks:</strong> K.M. Bangar (Principles of Engineering Geology, p. 298); IS: 6250 (1981); Parbin Singh"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Why Slate Is the Universal Natural Roofing Slab</div>
      <p><strong>Slate</strong> is a fine-grained, low-grade regionally metamorphosed pelitic rock derived from shale or mudstone under directed tectonic compression (greenschist/sub-greenschist facies). During metamorphism, clay minerals recrystallize into microscopically aligned, parallel flakes of <strong>muscovite (sericite), illite, and chlorite</strong> oriented perpendicular to the maximum compressive stress ($\sigma_1$). This imparts an extraordinary penetrative fabric known as <strong>slaty cleavage</strong>, enabling slate to be split effortlessly into thin ($4\text{--}10\text{ mm}$), flat, smooth, light, and completely impervious sheets ideal for <strong>roofing slabs (roofing tiles)</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Material</th>
              <th>Fabric &amp; Splitting Behaviour</th>
              <th>Weight &amp; Water Absorption</th>
              <th>Suitability as a Roofing Slab</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>SLATE</strong> (Option A)</td>
              <td><strong>Perfect penetrative slaty cleavage; splits into thin ($4\text{--}10\text{ mm}$), flat, uniform sheets</strong></td>
              <td><strong>Lightweight in thin sheets; extremely low water absorption ($< 0.4\%$), high transverse flexural strength</strong></td>
              <td><strong>UNIVERSAL ROOFING SLAB / TILE (Correct Answer)</strong></td>
            </tr>
            <tr>
              <td>Granite (Option B)</td>
              <td>Massive, non-foliated interlocking plutonic fabric; cannot be split into thin sheets</td>
              <td>Heavy massive blocks ($2.65\text{--}2.75\text{ g/cm}^3$); zero cleavage</td>
              <td>Unsuitable for pitched roofing tiles; used for heavy foundations &amp; piers</td>
            </tr>
            <tr>
              <td>Marble (Option C)</td>
              <td>Granoblastic (non-foliated) interlocking calcite mosaic; lacks cleavage planes</td>
              <td>Heavy slabs; soluble in acid rain and prone to thermal warping</td>
              <td>Used for interior flooring, wall cladding, and statuary</td>
            </tr>
            <tr>
              <td>Gneiss (Option D)</td>
              <td>Coarse gneissic banding (segregated quartzo-feldspathic and mafic bands); poor splitting</td>
              <td>Breaks into thick, rough slabs ($> 5\text{--}15\text{ cm}$); too heavy for roof trusses</td>
              <td>Used for heavy masonry, paving setts, and road aggregates</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Slate</strong> is an extremely fine-grained metamorphic rock formed from shales and clays. Its most valuable engineering property is its perfect <strong>slaty cleavage</strong>, by virtue of which it can be split into very thin, smooth, tough, and flat sheets of uniform thickness. Because slate also possesses negligible porosity (water absorption $< 0.5\%$), high transverse bending strength, and complete resistance to frost and atmospheric weathering, <strong>it is universally used as a roofing slab</strong>, damp-proof course (DPC), electrical switchboard panel, and school slate."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Chapter 14: Building Stones, p. 298)</div>
      </div>

      <div class="formula-card">
        <div class="formula-title">IS: 6250 (1981) Specifications for Roofing Slate Tiles</div>
        $$\text{Water Absorption (after 24 hr boiling)} \le 0.30\%\text{ to }0.40\% \quad \text{(Virtually Impervious)}$$
        $$\text{Modulus of Rupture (Flexural Bending Strength): } \sigma_f = \frac{3PL}{2bd^2} \ge 40\text{--}70\text{ MPa}$$
        $$\text{Specific Gravity: } G = 2.75\text{ to }2.89 \quad \big|\quad \text{Acid Immersion Test: Zero Delamination in } \text{H}_2\text{SO}_4$$
        <p style="font-size:0.88rem; color:#475569; margin-top:8px;">Because a roofing slab spans between wooden or steel purlins/battens and supports wind uplift, snow loads, and maintenance foot traffic as a thin plate ($d \approx 5\text{--}8\text{ mm}$), a high <strong>Modulus of Rupture (flexural tensile strength)</strong> along the cleavage plane is essential.</p>
      </div>

      <div class="card-title" style="margin-top:22px;">2. Key Indian Occurrences &amp; Quality Tests of Roofing Slate</div>
      <ul style="margin-left:20px; line-height:1.8;">
        <li><strong>Famous Indian Slate Belts:</strong>
          <ul style="margin-left:20px;">
            <li><strong>Himachal Pradesh:</strong> Kangra (Dharamshala, Khaniara), Mandi, and Chamba districts (premier Himalayan roofing slates).</li>
            <li><strong>Haryana &amp; Rajasthan:</strong> Rewari, Kund, and Alwar (Delhi Supergroup slates).</li>
            <li><strong>Andhra Pradesh:</strong> Markapur belt in Prakasam district (Cumbum Formation, Nallamalai Group of Cuddapah Supergroup).</li>
            <li><strong>Bihar:</strong> Munger (Kharagpur Hills).</li>
          </ul>
        </li>
        <li><strong>Field Quality Ring Test:</strong> A first-class roofing slate gives a sharp, clear <em>metallic ringing sound</em> when struck lightly with a knuckle or hammer, does not feel greasy to the touch, and shows zero free carbonate ($\text{CaCO}_3$) effervescence with dilute $\text{HCl}$ (since calcite dissolves in acid rain and ruins the roof).</li>
      </ul>

      <div class="fig-box">
        <img src="../../figures_2019_Q120/slate_roofing_slab_slaty_cleavage.png" alt="Slate Roofing Slabs and Microscopic Slaty Cleavage Mechanism">
        <div class="fig-cap">Figure 120.1: Formation of penetrative slaty cleavage by tectonic alignment of mica/chlorite platelets perpendicular to $\sigma_1$, allowing slate to be split into thin, impervious, high-flexural-strength roofing slabs, contrasted with massive granite, granoblastic marble, and coarse-banded gneiss.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">Official OPSC 2019 Question &amp; Forensic Option Analysis</div>
      <div class="question-box">
        <strong>Q120.</strong> Which of the following materials is generally used as a roofing slab ?<br>
        (A) Slate<br>
        (B) Granite<br>
        (C) Marble<br>
        (D) Gneiss
      </div>

      <div class="ans-banner">
        <span>&#10004;</span> Verified Correct Answer: <strong>Option (A) &mdash; Slate</strong>
      </div>

      <div class="option-grid">
        <div class="option correct">
          <div class="opt-header">
            <span class="opt-letter">A</span>
            <span class="opt-title">Slate</span>
            <span class="opt-badge">CORRECT ANSWER</span>
          </div>
          <div class="opt-body">
            <strong>Forensic Verification:</strong> <strong>Slate</strong> is universally used as a natural <strong>roofing slab (roofing tile)</strong> because its perfect <em>slaty cleavage</em> allows it to be split into very thin ($4\text{--}10\text{ mm}$), flat, light, and smooth rectangular sheets that are completely impervious to rainwater (absorption $< 0.4\%$) and possess high transverse bending strength.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">B</span>
            <span class="opt-title">Granite</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Granite</strong> is a massive, unfoliated plutonic rock lacking cleavage planes. It cannot be split into thin sheets and is far too heavy for pitched roofing tiles.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">C</span>
            <span class="opt-title">Marble</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Marble</strong> is a non-foliated granoblastic metamorphic rock composed of interlocking calcite crystals. It lacks rock cleavage, cannot be split into thin tiles, and dissolves/etches in acid rain.
          </div>
        </div>

        <div class="option wrong">
          <div class="opt-header">
            <span class="opt-letter">D</span>
            <span class="opt-title">Gneiss</span>
            <span class="opt-badge">INCORRECT</span>
          </div>
          <div class="opt-body">
            <strong>Why this is wrong:</strong> <strong>Gneiss</strong> is a coarse-grained, high-grade metamorphic rock with discontinuous compositional banding (gneissosity). Its foliation is rough and poorly fissile, breaking only into thick, heavy slabs unsuitable for roofing tiles.
          </div>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">Synthesis: Progressive Metamorphism of Pelites (Shale) &amp; Engineering Uses</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Metamorphic Rock</th>
              <th>Metamorphic Grade</th>
              <th>Characteristic Fabric</th>
              <th>Splitting Thickness</th>
              <th>Primary Engineering / Industrial Use</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>Slate</strong></td><td><strong>Very Low / Low Grade (Sub-greenschist to Greenschist)</strong></td><td><strong>Perfect Planar Slaty Cleavage (Micro-mica/chlorite)</strong></td><td><strong>$4 - 10\text{ mm}$</strong></td><td><strong>Roofing slabs/tiles, damp-proof courses (DPC), electrical switchboards, billiard tables</strong></td></tr>
            <tr><td>Phyllite</td><td>Low-to-Medium Grade (Greenschist)</td><td>Silkylustrous phyllitic cleavage (often crenulated/corrugated)</td><td>$10 - 25\text{ mm}$</td><td>Local flagging stone; softer and more corrugated than true slate</td></tr>
            <tr><td>Mica Schist</td><td>Medium Grade (Epidote-Amphibolite)</td><td>Coarse wavy schistosity (visible muscovite/biotite flakes)</td><td>Breaks irregularly</td><td>Poor building stone (weak and flaky along mica layers)</td></tr>
            <tr><td>Gneiss</td><td>High Grade (Amphibolite to Granulite)</td><td>Gneissic banding (alternating felsic &amp; mafic layers)</td><td>$> 50 - 150\text{ mm}$</td><td>Heavy foundation masonry, pitching stone, crushed aggregate</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between sedimentary "Fissility" in shale and metamorphic "Slaty Cleavage" in slate?</div>
        <div class="pq-ans">Answer: Fissility in shale is always parallel to original depositional bedding; slaty cleavage in slate is formed by tectonic recrystallization perpendicular to $\sigma_1$ and usually cuts across the original bedding planes at an angle.</div>
        <div class="pq-exp">Furthermore, shale softens and slakes in water, whereas metamorphism binds slate into a hard, waterproof sheet.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Why is slate also widely used for electrical switchboards and laboratory tabletops?</div>
        <div class="pq-ans">Answer: Pure slate (free of magnetite or pyrite veins) is an excellent electrical insulator, chemically inert to acids, non-absorbent, and easily machined into perfectly flat panels.</div>
        <div class="pq-exp">Wait-free flatness and high dielectric resistance make non-metallic slate ideal for precision benches and switchboards.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What causes the different natural colors of roofing slates (black, grey, purple, green)?</div>
        <div class="pq-ans">Answer: Black/dark grey is caused by finely disseminated carbonaceous matter; red/purple by ferric oxide (hematite, $\text{Fe}_2\text{O}_3$); and green by ferrous iron silicate (chlorite).</div>
        <div class="pq-exp">Mineralogical pigments in the parent mudstone control the color of the resulting slate.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why are calcareous slates (containing $\text{CaCO}_3$) and pyritiferous slates (containing $\text{FeS}_2$) rejected by IS: 6250 for roofing?</div>
        <div class="pq-ans">Answer: Pyrite oxidizes in rain to form sulphuric acid ($\text{H}_2\text{SO}_4$) and rusty holes, while calcite reacts with the acid to form gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$), which swells and delaminates the slate.</div>
        <div class="pq-exp">The IS: 6250 sulphuric acid immersion test specifically detects calcareous and pyritic impurities.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which sedimentary stone in Rajasthan is also widely split along bedding planes for flooring and flat-roof slabs ("Patti")?</div>
        <div class="pq-ans">Answer: Kota Stone (fine-grained flaggy siliceous limestone from the Semri/Bhander Group of the Vindhyan Supergroup) and Jodhpur/Karauli flaggy sandstone.</div>
        <div class="pq-exp">While flaggy sandstones/limestones are used for thick flat-roof beams ("pattis"), true thin pitched roofing tiles are made of metamorphic **Slate**.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is a "Damp-Proof Course" (DPC) in building construction and why is slate ideal for it?</div>
        <div class="pq-ans">Answer: A horizontal barrier placed at plinth level in brick/stone walls to stop capillary rise of ground moisture; slate is ideal because its water absorption is under $0.4\%$ and its crushing strength exceeds wall loads.</div>
        <div class="pq-exp">Two overlapping courses of slate laid in cement mortar form a permanent, indestructible damp-proof barrier.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Along which plane of the strain ellipsoid ($X \ge Y \ge Z$) does slaty cleavage develop?</div>
        <div class="pq-ans">Answer: Parallel to the $XY$ plane of maximum flattening, which is strictly perpendicular to the shortest principal strain axis ($Z$, parallel to $\sigma_1$).</div>
        <div class="pq-exp">Deformed reduction spots in Welsh and Himalayan slates confirm approximately $60\%\text{--}70\%$ shortening along $Z$ perpendicular to slaty cleavage.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. Which famous stratigraphic formation in Andhra Pradesh yields the Markapur roofing slates?</div>
        <div class="pq-ans">Answer: The Cumbum Formation of the Nallamalai Group (Proterozoic Cuddapah Supergroup).</div>
        <div class="pq-exp">The Cumbum slates and phyllites around Markapur (Prakasam district) are one of Peninsular India's largest commercial slate deposits.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 9 Part B (Q114 - Q120)...")
    gen_q114()
    gen_q115()
    gen_q116()
    gen_q117()
    gen_q118()
    gen_q119()
    gen_q120()
    print("Batch 9 Part B successfully generated!")
