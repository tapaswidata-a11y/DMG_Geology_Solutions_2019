#!/usr/bin/env python3
"""
Q084 Generator: Bysmalith Igneous Pluton Architecture & Emplacement Mechanics
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q084():
    title = r"Q084: Igneous Petrology: Forms of Intrusions — Bysmalith Mechanics & Morphology | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Pluton Emplacement"
    h1_title = "Q084: Bysmalith: Fault-Bounded Cylindrical Igneous Intrusion"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 84<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Ch. 5: Petrology / Igneous Intrusions, pp. 55, 168–170); Joseph P. Iddings (1898, <em>Journal of Geology</em>, "Bysmaliths"); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 115–118); John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (Ch. 4: Pluton Emplacement, pp. 53–70)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND STRUCTURAL ANATOMY OF A BYSMALITH -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition & Structural Anatomy of a Bysmalith</div>
    <div class="card-body">
      <p>
        The term <strong>bysmalith</strong> was coined in 1898 by the distinguished American petrologist <strong>Joseph Paxon Iddings</strong> (derived from the ancient Greek <em>bysma</em> = plug or stopper, and <em>lithos</em> = stone) while studying the complex intrusive volcanic-plutonic architecture of Mt. Holmes in Yellowstone National Park.
      </p>
      <p>
        A <strong>bysmalith</strong> is defined as a more or less <strong>vertical, cylindrical or plug-shaped igneous pluton that cross-cuts adjacent sedimentary strata and is bounded on its lateral margins by steep, circular faults or shear fractures</strong>. The magma intrudes forcibly, punching the overlying cylindrical block of country rock vertically upward like a mechanical piston.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q84/bangar_p168_bysmalith_laccolith_forms.png" alt="Forms of Igneous Intrusions: Bysmalith and Laccolith from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 84.1 — Morphological Architecture of Plutons:</strong> Authentic textbook diagram from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 168). Demonstrating the structural geometry of concordant laccoliths versus fault-bounded discordant bysmaliths, sills, and dikes.
        </div>
      </div>

      <h4>Diagnostic Anatomical Criteria of a Bysmalith</h4>
      <ul>
        <li><strong>Cross-Sectional Geometry:</strong> Sub-circular to elliptical in plan view, extending vertically as a steep, cylindrical or downward-tapering plug.</li>
        <li><strong>Discordant, Fault-Bounded Margins:</strong> Unlike concordant laccoliths whose margins pinch out smoothly along bedding planes, the perimeter of a bysmalith is defined by <strong>steep ring faults or reverse faults</strong> along which the roof has been forcibly sheared and elevated.</li>
        <li><strong>Piston-Like Roof Displacement:</strong> The roof strata are displaced vertically upwards en masse, with minimal horizontal spreading of the magma body.</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q84/bangar_p55_bysmalith_laccolith_forms.png" alt="Mechanics of Bysmalith Punching from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 84.2 — Mechanical Evolution from Laccolith to Bysmalith:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 55). Showing how high magmatic overpressure causes flexural failure of the roof strata, creating marginal shear faults.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: MECHANICAL EVOLUTION: LACCOLITH TO BYSMALITH TRANSITION -->
  <div class="card">
    <div class="card-header bg-indigo">2. Geomechanical Evolution: The Laccolith-to-Bysmalith Transition</div>
    <div class="card-body">
      <p>
        In physical volcanology and structural geology (Corry, 1988), a bysmalith represents the <strong>structural failure end-member of a laccolith</strong>:
      </p>
      <ol>
        <li><strong>Initial Sill Injection:</strong> Magma ascends along vertical conduits (dikes) and spreads horizontally along a bedding plane where lithostatic overburden equals magma pressure.</li>
        <li><strong>Laccolithic Doming:</strong> As magma continues to pump into the sill, the pressure exceeds lithostatic overburden ($P_{\text{magma}} > \sigma_v$). The overlying sedimentary layers bend upward elastically and plastically like an blister or dome, producing a <strong>concordant laccolith</strong> with a flat floor and arched roof.</li>
        <li><strong>Shear Failure of the Roof:</strong> If magma injection is exceptionally rapid or the magma is highly viscous (e.g., dacitic, rhyolitic, or phonolitic), the magmatic overpressure ($\Delta P = P_{\text{magma}} - \sigma_v$) exceeds the shear strength ($\tau_{\text{rock}}$) of the overburden rock:
          $$\Delta P > \frac{2 \tau_{\text{rock}} \cdot h}{r}$$
          where $h$ is overburden thickness and $r$ is pluton radius.</li>
        <li><strong>Bysmalith Formation (Piston Punching):</strong> The roof strata rupture along circumferential vertical faults, and the central cylinder of rock is punched straight upward, transforming the dome into a <strong>steep-sided, fault-bounded bysmalith</strong>.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE CLASSIFICATION OF INTRUSIVE FORMS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Comparative Petrology: Concordant vs. Discordant Igneous Plutons</div>
    <div class="card-body">
      <p>
        Igneous intrusions are systematically categorized based on their geometric concordance with host rock stratification:
      </p>
      <ul>
        <li><strong>Concordant Intrusions (Parallel to Bedding):</strong>
          <ul>
            <li><strong>Sill:</strong> Tabular, sheet-like intrusion parallel to bedding planes.</li>
            <li><strong>Laccolith:</strong> Plano-convex, mushroom-shaped intrusion with a flat floor and arched roof.</li>
            <li><strong>Lopolith:</strong> Colossal, saucer-shaped or basin-shaped intrusion depressed in the center (e.g., Bushveld, Sudbury, Duluth).</li>
            <li><strong>Phacolith:</strong> Crescent-shaped intrusion located along the hinge zones (crests of anticlines or troughs of synclines) of folded strata.</li>
          </ul>
        </li>
        <li><strong>Discordant Intrusions (Cross-cutting Bedding):</strong>
          <ul>
            <li><strong>Dike:</strong> Steeply dipping to vertical tabular intrusion cutting across bedding planes.</li>
            <li><strong>Bysmalith:</strong> Vertical, cylindrical, fault-bounded plug punching through country rocks.</li>
            <li><strong>Batholith:</strong> Colossal discordant plutonic body with an outcrop area exceeding $100\text{ km}^2$, expanding indefinitely downward without an observable floor.</li>
            <li><strong>Stock:</strong> A discordant pluton similar to a batholith but with an exposed surface area $< 100\text{ km}^2$.</li>
            <li><strong>Chonolith (Conolith):</strong> An irregular, chaotic intrusive body of undetermined or complex shape that does not conform to any standard geometric category (Daly, 1905).</li>
            <li><strong>Volcanic Neck (Plug):</strong> Cylindrical conduit of an eroded volcano filled with consolidated lava or agglomeratic pyroclastic breccia.</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 84</div>
        <div class="q-text">An igneous pluton which is more or less vertical and cylindrical that cross-cuts adjacent sediments and is bounded by steep faults is termed as :</div>
        <div class="q-options">
          <div class="opt-node">(A) Laccolith</div>
          <div class="opt-node correct">(B) Bysmalith</div>
          <div class="opt-node">(C) Lopolith</div>
          <div class="opt-node">(D) Conolith</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (B)</div>
        <div><strong>Bysmalith:</strong> A vertical, cylindrical igneous intrusion that cross-cuts surrounding sedimentary strata and is bounded on its lateral margins by steep ring faults along which the roof has been punched upward.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Laccolith — INCORRECT</div>
        <p>
          A <em>laccolith</em> is a <strong>concordant</strong>, dome-shaped intrusion characterized by a flat floor and an arched, convex-upward roof. It deforms overlying strata by gentle flexural arching without cutting across them or being bounded by steep marginal faults.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(B) Bysmalith — CORRECT</div>
        <p>
          A <em>bysmalith</em> (Iddings, 1898) is the precise, unambiguous term for an igneous pluton that is <strong>more or less vertical and cylindrical, cross-cuts adjacent sediments, and is bounded by steep faults</strong>. It is mechanically a faulted laccolith where the central core has punched upward like a piston (Bangar, p. 55, 168; Mahapatra, p. 116).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Lopolith — INCORRECT</div>
        <p>
          A <em>lopolith</em> (Grout, 1918) is a colossal, <strong>concordant, saucer-shaped or basin-shaped intrusion</strong> that is depressed in the center due to gravitational sagging under the immense weight of dense mafic/ultramafic magma (e.g., Bushveld Complex, South Africa). It is not vertical or cylindrical, nor is it bounded by steep faults.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Conolith — INCORRECT</div>
        <p>
          A <em>conolith</em> (or more accurately <em>chonolith</em>, coined by R.A. Daly in 1905) is an igneous body of <strong>irregular, chaotic, or undefinable shape</strong> that cannot be classified as a dike, sill, laccolith, or bysmalith. It does not possess a specific vertical cylindrical geometry bounded by steep faults.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification of Igneous Intrusive Bodies</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Pluton Type</th>
            <th>Structural Concordance</th>
            <th>Morphology & Geometry</th>
            <th>Boundary Relationship</th>
            <th>Classic Global / Indian Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bysmalith</strong></td>
            <td><strong>Discordant</strong></td>
            <td><strong>Vertical, cylindrical plug or piston</strong></td>
            <td><strong>Steep, circular peripheral faults</strong></td>
            <td><strong>Mt. Holmes (Yellowstone, USA); Black Hills (South Dakota)</strong></td>
          </tr>
          <tr>
            <td><strong>Laccolith</strong></td>
            <td>Concordant</td>
            <td>Plano-convex, mushroom-shaped; flat floor, arched roof</td>
            <td>Ductile bending of roof strata without faulting</td>
            <td>Henry Mountains (Utah); Girnar Hills (Gujarat)</td>
          </tr>
          <tr>
            <td><strong>Lopolith</strong></td>
            <td>Concordant</td>
            <td>Basin-shaped, saucer-like, sunken central depression</td>
            <td>Conformable to sagging layered floor and roof</td>
            <td>Bushveld Complex (South Africa); Duluth Gabbro (USA)</td>
          </tr>
          <tr>
            <td><strong>Phacolith</strong></td>
            <td>Concordant</td>
            <td>Crescent-shaped, lens-like along fold hinges</td>
            <td>Fills anticlinal crests and synclinal troughs</td>
            <td>Corndon Hill (Shropshire, UK); Dalhousie (Himalaya)</td>
          </tr>
          <tr>
            <td><strong>Batholith</strong></td>
            <td>Discordant</td>
            <td>Colossal, irregular ($> 100\text{ km}^2$), expanding downward</td>
            <td>Steep discordant cross-cutting walls, no visible floor</td>
            <td>Ladakh Batholith (Himalaya); Bundelkhand Granite (Central India)</td>
          </tr>
          <tr>
            <td><strong>Chonolith (Conolith)</strong></td>
            <td>Discordant</td>
            <td>Irregular, chaotic, asymmetric injection body</td>
            <td>Highly irregular cross-cutting contacts</td>
            <td>Various subvolcanic complex injections</td>
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
        <div class="p-header">Problem 1: Critical Magmatic Overpressure for Shear Punching (Bysmalith Formation)</div>
        <p>
          A cylindrical magma body of radius $R = 1,500\text{ meters}$ is ponded at depth $H = 2,000\text{ meters}$ beneath horizontal sandstone beds ($\rho = 2,500\text{ kg/m}^3$). The shear strength of the overburden sandstone along vertical circular fault planes is $\tau_s = 25\text{ MPa}$. Calculate the minimum magmatic pressure ($P_{\text{magma}}$) required to shear the overburden and punch the block upward as a bysmalith ($g = 9.81\text{ m/s}^2$).
        </p>
        <div class="p-ans">
          <strong>Force Balance Derivation:</strong><br>
          For the central cylinder of rock to be punched upward, the upward vertical force exerted by magma pressure on the basal area must overcome both the downward gravitational weight of the overburden and the frictional shear resistance along the cylindrical fault perimeter:<br>
          $$F_{\text{up}} \ge F_{\text{weight}} + F_{\text{shear}}$$<br>
          $$P_{\text{magma}} \cdot (\pi R^2) \ge (\rho \cdot g \cdot H) \cdot (\pi R^2) + \tau_s \cdot (2\pi R \cdot H)$$<br>
          Dividing both sides by $\pi R^2$:
          $$P_{\text{magma}} \ge \rho g H + \frac{2 \tau_s H}{R}$$<br>
          1. <strong>Lithostatic Overburden ($\sigma_v$):</strong>
          $$\sigma_v = 2500 \times 9.81 \times 2000 = 4.905 \times 10^7\text{ Pa} = 49.05\text{ MPa}$$<br>
          2. <strong>Shear Resistance Term:</strong>
          $$\Delta P_{\text{shear}} = \frac{2 \times (25\text{ MPa}) \times 2000\text{ m}}{1500\text{ m}} = \frac{100,000}{1500} \approx \mathbf{33.33\text{ MPa}}$$<br>
          3. <strong>Total Required Magma Pressure:</strong>
          $$P_{\text{magma}} \ge 49.05\text{ MPa} + 33.33\text{ MPa} = \mathbf{82.38\text{ MPa}}$$<br>
          <strong>Interpretation:</strong> The magma must maintain an overpressure of at least <strong>$33.3\text{ MPa}$ above lithostatic pressure</strong> ($P_{\text{magma}} > 82.4\text{ MPa}$) to rupture the roof along vertical faults and emplace as a bysmalith.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Geomechanical Role of Viscosity in Bysmalith Emplacement</div>
        <p>
          Explain why bysmaliths and laccoliths are almost universally composed of high-silica, viscous magmas (rhyolite, dacite, phonolite, trachyte) rather than low-viscosity basaltic magmas.
        </p>
        <div class="p-ans">
          <strong>Fluid Dynamics of Pluton Growth:</strong><br>
          1. <strong>Low-Viscosity Basaltic Magma ($\eta \approx 10\text{--}100\text{ Pa}\cdot\text{s}$):</strong> Flows easily along narrow bedding planes, spreading laterally over vast horizontal distances to form extensive, thin <strong>sills</strong> without building significant vertical thickness or localized overpressure.<br>
          2. <strong>High-Viscosity Felsic Magma ($\eta \approx 10^6\text{--}10^9\text{ Pa}\cdot\text{s}$):</strong> Flow resistance along narrow bedding conduits is immense ($Q \propto 1/\eta$). The magma cannot spread far laterally; instead, it ponds locally, building up massive vertical hydrodynamic pressure at the feeder vent. This forces the roof to dome upward into a laccolith and, upon shear failure, punch straight upward as a bysmalith.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Iddings' Yellowstone Mt. Holmes Archetype</div>
        <p>
          Describe the structural architecture of the type bysmalith described by J.P. Iddings (1898) at Mt. Holmes in Yellowstone National Park.
        </p>
        <div class="p-ans">
          <strong>Historical Type Description:</strong><br>
          - At Mt. Holmes in the Gallatin Range, Iddings mapped a steep, plug-shaped intrusive mass of porphyritic rhyolite/granite porphyry.<br>
          - The intrusion punched through Cambrian and Carboniferous sedimentary formations.<br>
          - Instead of bending the strata into a gentle dome as seen in the nearby laccoliths of the Henry Mountains, the Mt. Holmes body is bounded by vertical, circular faults where the adjacent sedimentary beds are sharply truncated, dragged, and shattered by vertical shear.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Bysmalith vs. Cauldron Subsidence (Piston Up vs. Piston Down)</div>
        <p>
          Compare the kinematics of a bysmalith with that of a cauldron subsidence (caldera collapse). Contrast their fault bounding geometries and displacement vectors.
        </p>
        <div class="p-ans">
          <strong>Kinematic Contrast:</strong><br>
          - <strong>Bysmalith (Piston Upward):</strong> Driven by <strong>positive magmatic overpressure</strong> ($\Delta P > 0$). The magma acts as a hydraulic jack, forcing a central cylindrical rock cylinder <strong>vertically upward</strong> along outward-dipping or vertical reverse ring faults.<br>
          - <strong>Cauldron Subsidence (Piston Downward):</strong> Driven by <strong>negative magmatic pressure</strong> (underpressure, $\Delta P < 0$) following catastrophic volcanic eruption. The cylindrical block of roof rock sinks <strong>downward</strong> into the depleted magma chamber along inward-dipping normal ring faults (e.g., Glen Coe, Scotland; Ossipee, New Hampshire).
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Lopolith Centripetal Subsidence Mechanics</div>
        <p>
          Explain why lopoliths (e.g., Bushveld, Sudbury) possess a saucer-shaped form with layers dipping inward toward the center, whereas laccoliths have convex-upward roofs.
        </p>
        <div class="p-ans">
          <strong>Mechanical Loading Explanation:</strong><br>
          1. <strong>High Density of Ultramafic Magma:</strong> Lopoliths are formed by immense volumes of dense mafic-to-ultramafic magma ($\rho_{\text{melt}} \approx 2,750\text{--}2,850\text{ kg/m}^3$) intruding into less dense continental crust ($\rho_{\text{crust}} \approx 2,650\text{ kg/m}^3$).<br>
          2. <strong>Isostatic & Thermal Sag:</strong> The colossal weight of the ponded magma exceeds the isostatic buoyancy of the floor rocks. As crystallization proceeds, the floor sags downward into the crust while the roof collapses centripetally, producing an inward-dipping, saucer-shaped lopolith.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Phacolith Emplacement in Folded Orogenic Belts</div>
        <p>
          Why do phacoliths emplace preferentially along the crests of anticlines and troughs of synclines, rather than along the fold limbs?
        </p>
        <div class="p-ans">
          <strong>Structural Mechanics (Saddle Reef Mechanism):</strong><br>
          - During flexural-slip folding of stratified sedimentary rocks, bed-parallel slippage produces <strong>extensional dilation and low-pressure zones</strong> at the hinge regions (anticlinal crests and synclinal troughs).<br>
          - In contrast, the fold limbs experience intense compressive shear stress.<br>
          - Magma follows minimum pressure gradients ($\nabla P$), migrating selectively into the dilated hinge crests and troughs to crystallize as concordant, crescent-shaped bodies termed <strong>phacoliths</strong> (Harker, 1909).
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Chonolith (Conolith) Definition and Diagnostic Ambiguity</div>
        <p>
          In a geological survey report, an intrusive body is described as a "chonolith". Explain what this term signifies and why it is used as a term of last resort.
        </p>
        <div class="p-ans">
          <strong>Petrological Definition:</strong><br>
          - <strong>Chonolith:</strong> Coined by R.A. Daly (1905), derived from Greek <em>choane</em> = melting pot or funnel. It designates an igneous intrusion of <strong>irregular, chaotic, or undefinable shape</strong> whose contacts are discordant and which cannot be fitted into the neat geometric categories of dikes, sills, laccoliths, bysmaliths, or lopoliths.<br>
          - <strong>Term of Last Resort:</strong> It indicates that the intrusion was injected along complex, multi-directional joint sets, faults, or unconformities, or that structural exposure is insufficient to reconstruct its geometric architecture.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Contact Metamorphic Aureole around a Bysmalith</div>
        <p>
          How does the contact metamorphic aureole around a bysmalith differ from that around a concordant sill or laccolith?
        </p>
        <div class="p-ans">
          <strong>Structural and Thermal Aureole Criteria:</strong><br>
          - <strong>Laccolith / Sill:</strong> Contact metamorphism is purely thermal, developing hornfels with granoblastic, non-foliated textures parallel to the concordant bedding contacts.<br>
          - <strong>Bysmalith:</strong> Shows an intense superposition of <strong>dynamic deformation and high shear strain</strong> along its peripheral ring faults. Country rocks adjacent to the cylindrical plug are intensely dragged upward, brecciated, and transformed into mylonitic or cataclastic fault gouge overprinted by pyrometamorphism (buchites/hornfels).
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 84, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q084_Bysmalith_Igneous_Pluton_Forms_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q084: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q084()
