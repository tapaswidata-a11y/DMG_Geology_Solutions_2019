#!/usr/bin/env python3
"""
Q141 Generator: Flow Net Theory & Groundwater Seepage Discharge Computation
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q141():
    title = r"Q141: Hydrogeology: Flow Net Seepage Discharge Computation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Hydrogeology & Groundwater Hydraulics"
    h1_title = "Q141: Flow Net Seepage Calculation: Hydraulic Conductivity, Head Loss, and Geometric Shape Factor"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 141<br>
<strong>Authoritative References:</strong> David K. Todd and Larry W. Mays, <em>Groundwater Hydrology</em> (3rd Ed., Wiley, Ch. 3: Groundwater Movement & Flow Nets, pp. 63–105); R. Allan Freeze and John A. Cherry, <em>Groundwater</em> (Prentice Hall, Ch. 5: Flow Nets); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 3: Hydrogeology, p. 28); C.W. Fetter, <em>Applied Hydrogeology</em> (4th Ed., Ch. 4)."""

    part1 = r"""
  <!-- CARD 1: WORKING PRINCIPLES OF FLOW NETS -->
  <div class="card">
    <div class="card-header bg-blue">1. Principles of Flow Net Theory & The Governing Seepage Equation</div>
    <div class="card-body">
      <p>
        In hydrogeology, groundwater hydraulics, and dam geotechnical engineering, a <strong>Flow Net</strong> is a curvilinear orthogonal grid formed by the intersection of two families of mutually perpendicular curves: <strong>Flow Lines (Streamlines)</strong> and <strong>Equipotential Lines</strong> (Todd & Mays, 2005; Freeze & Cherry, 1979; Bangar, p. 28).
      </p>
      <p>
        The flow net represents a graphical or numerical solution to the 2-dimensional <strong>Laplace Equation for steady-state groundwater flow</strong> in a homogeneous, isotropic porous medium:
      </p>
      <div class="math-block">
        $$\frac{\partial^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial z^2} = 0$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q141/flownet_seepage_calculation_darcy_mesh.png" alt="Flow Net Seepage Calculation and Darcy Mesh">
        <div class="figure-caption">
          <strong>Figure 141.1 — Orthogonal Flow Net Geometry for Groundwater Seepage:</strong> Intersecting streamtubes ($n_f$ flow channels) and equipotential drops ($n_d$ potential intervals) beneath a hydraulic structure. Illustrates how discharge through an elemental curvilinear square ($\Delta q = K \cdot \Delta h \cdot \frac{b}{l}$) integrates across the entire flow net.
        </div>
      </div>

      <h4>Derivation of the Total Flow Net Discharge Equation</h4>
      <p>
        Consider an elemental "curvilinear square" within the flow net bounded by two adjacent flow lines spaced by average width $b$, and two adjacent equipotential lines spaced by average length $l$ along the flow path:
      </p>
      <ol>
        <li>According to Darcy's Law, the seepage flow $\Delta q$ passing through a single flow channel per unit width perpendicular to the section is:
          $$\Delta q = K \cdot A \cdot i = K \cdot (b \times 1) \cdot \left(\frac{\Delta h}{l}\right) = K \cdot \Delta h \cdot \left(\frac{b}{l}\right)$$
        </li>
        <li>By rigorous flow net construction rules, the grid is drawn as <strong>curvilinear squares</strong>, meaning the ratio of width to length is maintained constant everywhere ($b / l \approx 1.0$). Therefore:
          $$\Delta q = K \cdot \Delta h$$
        </li>
        <li>Let the total hydraulic head loss across the entire system be $H$ (or $\Delta H$), subdivided into $n_d$ equal potential drops. The head drop per field is:
          $$\Delta h = \frac{H}{n_d}$$
        </li>
        <li>Let the total number of flow channels in the net be $n_f$. Because all $n_f$ channels run in parallel, the <strong>total flow rate ($Q$)</strong> per unit width is the sum of discharge across all channels:
          $$\text{Total Seepage Discharge: } Q = n_f \cdot \Delta q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right)$$
        </li>
      </ol>

      <div class="math-block">
        $$Q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right)$$
        $$\text{where: } K = \text{Hydraulic Conductivity (ii)}, \quad H = \text{Total Head Loss (iv)}, \quad \frac{n_f}{n_d} = \text{Geometry / Shape Factor of the Flow Net (i)}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q141/bangar_p28_flow_net_groundwater_discharge.png" alt="Flow Net Groundwater Discharge from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 141.2 — Flow Net Computation in Hydrogeology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 28). Verifies the exact parameters: <em>"The total flow in any section of a water table contour map with flow nets can be computed directly using: (i) Geometry of the flow nets ($n_f/n_d$), (ii) Hydraulic conductivity ($K$), and (iv) Head loss ($H$)."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: WHY SPECIFIC YIELD IS EXCLUDED -->
  <div class="card">
    <div class="card-header bg-emerald">2. Why Specific Yield (iii) is Irrelevant to Steady-State Flow Nets</div>
    <div class="card-body">
      <h4>Steady-State Flow vs. Transient Storage Depletion</h4>
      <p>
        The central analytical distinction in groundwater mechanics separates <strong>steady-state flow</strong> from <strong>transient storage release</strong>:
      </p>
      <ul>
        <li><strong>Flow Net Assumptions:</strong> Classical flow nets are drawn exclusively for <strong>steady-state seepage</strong> where the hydraulic head distribution ($\partial h / \partial t = 0$) and the shape of the phreatic surface or piezometric surface remain invariant over time. Water entering any elemental cell exactly equals water exiting ($\text{Inflow} = \text{Outflow}$). No water is added to or released from aquifer storage!</li>
        <li><strong>Physical Nature of Specific Yield ($S_y$):</strong> Specific yield is defined as the volume of water released from storage per unit surface area of an unconfined aquifer per unit decline of the water table:
          <div class="math-block">
            $$S_y = \frac{V_w \text{ (drained by gravity)}}{V_{\text{aquifer}} \text{ (total dewatered)}}$$
          </div>
          Specific yield governs transient pumping drawdown tests (Theis / Neuman unsteady-state equations: $S \frac{\partial h}{\partial t} = T \nabla^2 h$), but has <strong>zero mathematical presence in the steady-state Laplace equation ($\nabla^2 h = 0$)</strong>.
        </li>
      </ul>
      <p>
        Therefore, parameter <strong>(iii) Specific Yield</strong> is entirely excluded from the computation of total flow net discharge, confirming that only <strong>(i), (ii), and (iv)</strong> are utilized.
      </p>
    </div>
  </div>

  <!-- CARD 3: ANISOTROPIC AQUIFERS & TRANSFORMED FLOW NETS -->
  <div class="card">
    <div class="card-header bg-indigo">3. Anisotropic Formations and The Transformed Flow Net Protocol</div>
    <div class="card-body">
      <p>
        In natural sedimentary aquifers, horizontal hydraulic conductivity ($K_x$) is typically much higher than vertical conductivity ($K_z$) ($K_x / K_z \approx 2 - 10$ due to horizontal bedding planes). The governing equation becomes:
      </p>
      <div class="math-block">
        $$K_x \frac{\partial^2 h}{\partial x^2} + K_z \frac{\partial^2 h}{\partial z^2} = 0$$
      </div>
      <p>
        To construct an orthogonal flow net in an anisotropic medium:
      </p>
      <ol>
        <li>Transform the horizontal coordinate axis using the scale contraction factor:
          $$x_t = x \sqrt{\frac{K_z}{K_x}}$$
        </li>
        <li>Draw a standard orthogonal flow net with curvilinear squares on the transformed section.</li>
        <li>Calculate total seepage using the <strong>equivalent effective hydraulic conductivity ($K'$):</strong>
          $$K' = \sqrt{K_x \cdot K_z}$$
          $$Q = \sqrt{K_x \cdot K_z} \cdot H \cdot \left(\frac{n_f}{n_d}\right)$$
        </li>
      </ol>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 141</div>
      <div class="question-text">
        The total flow in any section of a water table contour map, in which the flow nets are drawn, can be directly computed with the help of the :<br>
        (i) Geometry of the flow nets<br>
        (ii) Hydraulic conductivity<br>
        (iii) Specific yield<br>
        (iv) Head loss<br>
        Choose the correct set of answer from the following :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> (i), (ii), (iii)</li>
        <li class="option-item"><strong>(B)</strong> (i), (iii), (iv)</li>
        <li class="option-item"><strong>(C)</strong> (ii), (iii), (iv)</li>
        <li class="option-item correct"><strong>(D)</strong> (i), (ii), (iv)</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (D) (i), (ii), (iv)</strong> — Seepage discharge through a flow net is governed strictly by the formula $Q = K \cdot H \cdot (n_f / n_d)$, which requires (i) Geometry of the flow nets ($n_f / n_d$), (ii) Hydraulic conductivity ($K$), and (iv) Head loss ($H$). Specific yield (iii) is a transient storage property not involved in steady-state flow net discharge.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): (i), (ii), (iii) — Incorrect Inclusion of Specific Yield & Omission of Head Loss</div>
        <p>
          Option (A) mistakenly includes Specific Yield (iii), which is an unconfined storage parameter relevant only to transient water table decline during pumping. It simultaneously omits Head Loss (iv), without which Darcy's hydraulic gradient cannot be established ($i = \Delta H / L$). Zero head loss means zero flow, regardless of conductivity or geometry.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): (i), (iii), (iv) — Incorrect Inclusion of Specific Yield & Omission of Hydraulic Conductivity</div>
        <p>
          Option (B) includes Specific Yield (iii) and fatally omits Hydraulic Conductivity (ii). Groundwater seepage velocity is directly proportional to hydraulic conductivity ($v = -K \nabla h$). Without $K$, discharge cannot be dimensionally resolved into volumetric flow units ($\text{m}^3\text{/s}$).
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): (ii), (iii), (iv) — Incorrect Inclusion of Specific Yield & Omission of Geometry</div>
        <p>
          Option (C) includes Specific Yield (iii) while omitting the Geometry of the flow nets (i) ($n_f / n_d$). A flow net is fundamentally a geometric representation; without the ratio of flow channels ($n_f$) to equipotential drops ($n_d$), the graphical solution cannot be scaled to total discharge.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (D): (i), (ii), (iv) — Fully Verified & Rigorously Correct</div>
        <p>
          In classical groundwater hydrology and engineering geology (Bangar, p. 28; Todd & Mays, Ch. 3; Freeze & Cherry), total discharge through a flow net is computed using:
          $$Q = K \cdot \Delta H \cdot \frac{n_f}{n_d}$$
        </p>
        <ol>
          <li><strong>(i) Geometry of the flow nets:</strong> Provides the dimensionless shape factor ($n_f / n_d$), the ratio of flow paths to potential drops.</li>
          <li><strong>(ii) Hydraulic conductivity ($K$):</strong> The transmission capacity of the aquifer medium ($\text{m/s}$).</li>
          <li><strong>(iv) Head loss ($H$ or $\Delta H$):</strong> The driving hydraulic energy dissipation across the section ($\text{m}$).</li>
        </ol>
        <p>Specific yield (iii) is not involved because flow net analysis assumes steady-state conditions where storage is unchanging. Thus, Option (D) is the unique correct set.</p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Hydrogeological Parameters: Steady-State Flow Nets vs. Transient Aquifer Storage</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Role in Flow Net Analysis ($Q = K \cdot H \cdot \frac{n_f}{n_d}$)</th>
            <th>Governing Physical Law</th>
            <th>Included in Steady-State Seepage?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>(i) Flow Net Geometry ($n_f / n_d$)</strong></td>
            <td>Dimensionless shape factor; ratios of parallel channels to series potential steps.</td>
            <td>Laplace Equation ($\nabla^2 h = 0$)</td>
            <td><strong>YES (Essential)</strong></td>
          </tr>
          <tr>
            <td><strong>(ii) Hydraulic Conductivity ($K$)</strong></td>
            <td>Material transmission capacity for water ($\text{m/s}$ or $\text{m/day}$).</td>
            <td>Darcy's Law ($q = -K \nabla h$)</td>
            <td><strong>YES (Essential)</strong></td>
          </tr>
          <tr>
            <td><strong>(iii) Specific Yield ($S_y$)</strong></td>
            <td>Volume of water released by gravity drainage per unit aquifer decline.</td>
            <td>Transient Continuity ($S \frac{\partial h}{\partial t} = \nabla \cdot (T \nabla h)$)</td>
            <td><strong>NO (Irrelevant to steady-state flow)</strong></td>
          </tr>
          <tr>
            <td><strong>(iv) Total Head Loss ($H$)</strong></td>
            <td>Driving potential energy difference between inlet and outlet boundaries ($\text{m}$).</td>
            <td>Bernoulli / Hydraulic Potential Energy</td>
            <td><strong>YES (Essential)</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD: 8 PRACTICE PROBLEMS WITH FULL STEP-BY-STEP DERIVATIONS -->
  <div class="card">
    <div class="card-header bg-purple">8 Advanced Practice Problems & Fully Worked Solutions</div>
    <div class="card-body">
      <!-- PROBLEM 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Seepage Discharge Beneath a Sheet Pile Wall</strong><br>
        A flow net constructed beneath an impervious sheet pile wall driven into an isotropic sandy silt aquifer has $n_f = 4\text{ flow channels}$ and $n_d = 10\text{ equipotential drops}$. The total differential head across the sheet pile is $H = 5.0\text{ m}$, and the hydraulic conductivity of the silt is $K = 2.5 \times 10^{-5}\text{ m/s}$. Calculate the seepage discharge per meter length of the wall ($q$) in $\text{m}^3/\text{day/m}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Apply the flow net discharge formula:
          $$q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right)$$
          2. Substitute given values:
          $$q = (2.5 \times 10^{-5}\text{ m/s}) \times 5.0\text{ m} \times \left(\frac{4}{10}\right) = (1.25 \times 10^{-4}) \times 0.40 = 5.0 \times 10^{-5}\text{ m}^3/\text{s per meter}$$
          3. Convert to $\text{m}^3/\text{day/m}$:
          $$q = 5.0 \times 10^{-5}\text{ m}^3/\text{s} \times 86,400\text{ s/day} = 4.32\text{ m}^3/\text{day per meter}$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Total Seepage Under a Concrete Gravity Dam</strong><br>
        A concrete gravity dam of crest length $L_{\text{dam}} = 120.0\text{ m}$ retains an upstream water depth of $h_{\text{up}} = 24.0\text{ m}$ with tailwater depth $h_{\text{down}} = 2.0\text{ m}$. A flow net drawn through the foundation bedrock shows $n_f = 5$ and $n_d = 16$. The foundation rock mass has hydraulic conductivity $K = 4.0 \times 10^{-6}\text{ m/s}$. Calculate the total seepage loss from the reservoir in liters per second ($\text{L/s}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Total driving head loss $H$:
          $$H = h_{\text{up}} - h_{\text{down}} = 24.0\text{ m} - 2.0\text{ m} = 22.0\text{ m}$$
          2. Seepage per unit width ($q$):
          $$q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right) = (4.0 \times 10^{-6}\text{ m/s}) \times 22.0\text{ m} \times \left(\frac{5}{16}\right) = 8.8 \times 10^{-5} \times 0.3125 = 2.75 \times 10^{-5}\text{ m}^3/\text{s/m}$$
          3. Total seepage for entire dam length ($L_{\text{dam}} = 120\text{ m}$):
          $$Q_{\text{total}} = q \times L_{\text{dam}} = 2.75 \times 10^{-5}\text{ m}^3/\text{s/m} \times 120.0\text{ m} = 3.30 \times 10^{-3}\text{ m}^3/\text{s}$$
          Convert to liters per second:
          $$Q_{\text{total}} = 3.30 \times 10^{-3} \times 1000\text{ L/m}^3 = 3.30\text{ L/s}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Exit Gradient & Boiling / Quicksand Factor of Safety</strong><br>
        At the downstream toe of the dam in Problem 2, the length of the final curvilinear square field adjacent to the exit face is measured as $\Delta l = 1.8\text{ m}$. The total head loss is $H = 22.0\text{ m}$ across $n_d = 16$ drops. The submerged buoyant unit weight of the foundation sand is $\gamma' = 10.2\text{ kN/m}^3$ and $\gamma_w = 9.81\text{ kN/m}^3$. Calculate: (a) the exit hydraulic gradient ($i_{\text{exit}}$), (b) the critical hydraulic gradient ($i_c$), and (c) the Factor of Safety against boiling ($\text{FoS} = i_c / i_{\text{exit}}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Head drop per equipotential step $\Delta h$:
          $$\Delta h = \frac{H}{n_d} = \frac{22.0\text{ m}}{16} = 1.375\text{ m}$$
          2. Exit gradient at the toe:
          $$i_{\text{exit}} = \frac{\Delta h}{\Delta l} = \frac{1.375\text{ m}}{1.8\text{ m}} = 0.7639$$
          3. Critical hydraulic gradient $i_c$:
          $$i_c = \frac{\gamma'}{\gamma_w} = \frac{10.2\text{ kN/m}^3}{9.81\text{ kN/m}^3} = 1.0398$$
          4. Factor of Safety against quicksand:
          $$\text{FoS} = \frac{i_c}{i_{\text{exit}}} = \frac{1.0398}{0.7639} = 1.36$$
          <em>Geotechnical Warning:</em> A safety factor of $1.36 < 4.0$ is dangerously low; an engineered inverted gravel filter or downstream cutoff sheet pile must be installed to prevent piping failure.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Pore Water Uplift Pressure Under a Dam Base</strong><br>
        A dam base of width $B = 30.0\text{ m}$ sits on an unconfined permeable stratum. The total head drop is $H = 18.0\text{ m}$ across $n_d = 12$ equipotential drops. A piezometer installed at the base of the dam intersects Equipotential Line number 4 (measured from the upstream reservoir, where total head $h_0 = 20.0\text{ m}$ above the base datum). Calculate: (a) the total hydraulic head at the piezometer, and (b) the uplift pore-water pressure ($u$) in $\text{kPa}$ assuming elevation head $z = 0$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Head loss per drop $\Delta h$:
          $$\Delta h = \frac{H}{n_d} = \frac{18.0\text{ m}}{12} = 1.50\text{ m}$$
          2. Head remaining at Equipotential Line 4:
          $$h_4 = h_0 - 4 \times \Delta h = 20.0\text{ m} - (4 \times 1.50\text{ m}) = 20.0 - 6.0 = 14.0\text{ m}$$
          3. Uplift pore-water pressure ($u = \rho_w g \cdot h_4$):
          $$u = 9.81\text{ kN/m}^3 \times 14.0\text{ m} = 137.34\text{ kPa}$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Seepage Discharge in Anisotropic Stratified Ground</strong><br>
        A stratified alluvial valley has horizontal hydraulic conductivity $K_x = 9.0 \times 10^{-5}\text{ m/s}$ and vertical conductivity $K_z = 1.0 \times 10^{-5}\text{ m/s}$ ($K_x / K_z = 9.0$). A transformed flow net constructed with coordinate scaling $x_t = x \sqrt{K_z / K_x}$ yields $n_f = 6$ and $n_d = 15$ for a total head loss $H = 10.0\text{ m}$. Calculate the true seepage discharge per meter width ($q$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate equivalent effective hydraulic conductivity $K'$:
          $$K' = \sqrt{K_x \cdot K_z} = \sqrt{(9.0 \times 10^{-5}) \times (1.0 \times 10^{-5})} = \sqrt{9.0 \times 10^{-10}} = 3.0 \times 10^{-5}\text{ m/s}$$
          2. Compute discharge using transformed flow net parameters:
          $$q = K' \cdot H \cdot \left(\frac{n_f}{n_d}\right) = (3.0 \times 10^{-5}\text{ m/s}) \times 10.0\text{ m} \times \left(\frac{6}{15}\right) = (3.0 \times 10^{-4}) \times 0.40 = 1.20 \times 10^{-4}\text{ m}^3/\text{s per meter}$$
          Convert to $\text{m}^3/\text{day/m}$:
          $$q = 1.20 \times 10^{-4} \times 86,400 = 10.37\text{ m}^3/\text{day per meter}$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Groundwater Basin Discharge from Water Table Contour Map</strong><br>
        A regional water table contour map reveals a recharge zone at elevation $h_1 = 320.0\text{ m}$ draining to a river at elevation $h_2 = 280.0\text{ m}$ ($H = 40.0\text{ m}$). Flow lines drawn across the aquifer basin partition the flow into $n_f = 8\text{ flow tubes}$ with $n_d = 20\text{ equipotential intervals}$. The aquifer has average thickness $b = 25.0\text{ m}$ and hydraulic conductivity $K = 15.0\text{ m/day}$. Calculate the annual groundwater discharge into the river in cubic meters per year ($\text{m}^3\text{/year}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. 2D flow net discharge per unit aquifer thickness:
          $$q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right) = 15.0\text{ m/day} \times 40.0\text{ m} \times \left(\frac{8}{20}\right) = 600.0 \times 0.40 = 240.0\text{ m}^3/\text{day per meter depth}$$
          2. Multiply by aquifer thickness $b = 25.0\text{ m}$:
          $$Q_{\text{daily}} = 240.0\text{ m}^3/\text{day/m} \times 25.0\text{ m} = 6000.0\text{ m}^3/\text{day}$$
          3. Annual groundwater discharge ($365\text{ days}$):
          $$Q_{\text{annual}} = 6000.0\text{ m}^3/\text{day} \times 365\text{ days} = 2,190,000\text{ m}^3/\text{year} \approx 2.19\text{ Million m}^3/\text{yr}$$
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Fractional Flow Channel Geometry</strong><br>
        In drawing a flow net around an irregular cofferdam, the boundary constraints leave a fractional flow channel of width $b_1 = 0.40 l_1$ in addition to 3 full channels ($b = l$). There are $n_d = 8$ equal potential drops, total head loss $H = 6.0\text{ m}$, and $K = 5.0 \times 10^{-5}\text{ m/s}$. Calculate: (a) the effective number of flow channels ($n_f$), and (b) the seepage discharge $q$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Effective flow channels $n_f$:
          $$n_f = 3\text{ full channels} + 0.40\text{ fractional channel} = 3.40$$
          2. Seepage discharge:
          $$q = K \cdot H \cdot \left(\frac{n_f}{n_d}\right) = (5.0 \times 10^{-5}\text{ m/s}) \times 6.0\text{ m} \times \left(\frac{3.40}{8}\right) = (3.0 \times 10^{-4}) \times 0.425 = 1.275 \times 10^{-4}\text{ m}^3/\text{s/m}$$
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Proof that Specific Yield Cancels in Steady-State Continuity</strong><br>
        The general 2D transient unconfined groundwater flow equation (Boussinesq equation) is:
        $$K \left[\frac{\partial}{\partial x}\left(h \frac{\partial h}{\partial x}\right) + \frac{\partial}{\partial y}\left(h \frac{\partial h}{\partial y}\right)\right] = S_y \frac{\partial h}{\partial t}$$
        Prove mathematically why Specific Yield ($S_y$) has no influence on the configuration of flow nets under steady-state conditions.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Steady-state condition is mathematically defined by the absence of time-dependent variations in hydraulic head:
          $$\frac{\partial h}{\partial t} = 0$$
          2. Substitute $\frac{\partial h}{\partial t} = 0$ into the right-hand side of the Boussinesq equation:
          $$S_y \frac{\partial h}{\partial t} = S_y \times 0 = 0$$
          3. The equation reduces to the steady-state form:
          $$\frac{\partial}{\partial x}\left(h \frac{\partial h}{\partial x}\right) + \frac{\partial}{\partial y}\left(h \frac{\partial h}{\partial y}\right) = 0$$
          <em>Conclusion:</em> Because the entire term containing $S_y$ vanishes identically to zero when $\partial h / \partial t = 0$, specific yield has zero mathematical or physical effect on steady-state flow net geometry or discharge.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=141,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q141_Flow_Net_Discharge_Computation_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q141: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q141()
