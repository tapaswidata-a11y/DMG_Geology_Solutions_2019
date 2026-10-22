#!/usr/bin/env python3
"""
Q145 Generator: Freshwater-Saline Water Parabolic Interface Geometry (Concave Upward)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q145():
    title = r"Q145: Hydrogeology: Coastal Freshwater-Saline Interface Geometry | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Hydrogeology & Coastal Aquifers"
    h1_title = "Q145: Freshwater-Saline Water Interface Geometry: Glover's Dynamic Parabolic Profile"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 145<br>
<strong>Authoritative References:</strong> Robert E. Glover, <em>The Pattern of Fresh-Water Flow in a Coastal Aquifer</em> (Journal of Geophysical Research, 1959, Vol. 64, No. 4, pp. 457–459); David K. Todd and Larry W. Mays, <em>Groundwater Hydrology</em> (3rd Ed., Wiley, Ch. 14: Saline Water Intrusion, pp. 555–578); C.W. Fetter, <em>Applied Hydrogeology</em> (4th Ed., Prentice Hall, Ch. 8, pp. 312–322); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 3: Hydrogeology, p. 32)."""

    part1 = r"""
  <!-- CARD 1: HYDROSTATIC GHYBEN-HERZBERG PRINCIPLE -->
  <div class="card">
    <div class="card-header bg-blue">1. The Ghyben-Herzberg Principle of Coastal Hydrostatic Balance</div>
    <div class="card-body">
      <p>
        In coastal aquifers, lighter freshwater ($\rho_f \approx 1.000\text{ g/cm}^3$) floats upon denser saline seawater ($\rho_s \approx 1.025\text{ g/cm}^3$). The fundamental relationship governing this equilibrium was independently formulated by Dutch engineer <strong>Willem Badon Ghyben (1888)</strong> and German engineer <strong>Baurat Alexander Herzberg (1901)</strong> (Todd & Mays, 2005; Fetter, 2001; Bangar, p. 32).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q145/ghyben_herzberg_saltwater_intrusion.png" alt="Ghyben-Herzberg Hydrostatic Principle">
        <div class="figure-caption">
          <strong>Figure 145.1 — Hydrostatic Equilibrium across Coastal Freshwater-Saltwater Systems:</strong> Balancing freshwater hydrostatic pressure $\rho_f g (h_f + z)$ against seawater hydrostatic pressure $\rho_s g z$ along the zero-velocity interface line at depth $z$ below mean sea level.
        </div>
      </div>

      <h4>Hydrostatic Derivation of the 40:1 Ratio</h4>
      <p>
        At any point along the interface at depth $z$ below mean sea level (MSL), hydrostatic pressure in the freshwater column of total height $(h_f + z)$ must balance the hydrostatic pressure of the saltwater column of depth $z$:
      </p>
      <div class="math-block">
        $$\rho_s \cdot g \cdot z = \rho_f \cdot g \cdot (h_f + z)$$
      </div>
      <p>
        Expanding and solving for interface depth $z$:
      </p>
      <div class="math-block">
        $$\rho_s z - \rho_f z = \rho_f h_f \implies z(\rho_s - \rho_f) = \rho_f h_f$$
        $$z = \left(\frac{\rho_f}{\rho_s - \rho_f}\right) h_f$$
      </div>
      <p>
        Substituting standard densities ($\rho_f = 1.000\text{ g/cm}^3$, $\rho_s = 1.025\text{ g/cm}^3$):
      </p>
      <div class="math-block" style="font-size: 1.2rem; font-weight: bold; background: #eff6ff; border-left: 5px solid #2563eb; padding: 12px;">
        $$z = \left(\frac{1.000}{1.025 - 1.000}\right) h_f = \frac{1.000}{0.025} h_f = 40 \cdot h_f$$
      </div>
      <p>
        Thus, for every <strong>$1\text{ meter}$</strong> that the freshwater table stands above mean sea level, the freshwater-saline water interface extends <strong>$40\text{ meters}$</strong> below sea level.
      </p>
    </div>
  </div>

  <!-- CARD 2: GLOVER'S DYNAMIC PARABOLIC SOLUTION -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Dynamic Hydrodynamic Flow & Glover's Parabolic Interface Solution (1959)</div>
    <div class="card-body">
      <div class="figure-box">
        <img src="../../figures_Q145/glover_coastal_parabolic_freshwater_interface.png" alt="Glover Coastal Parabolic Freshwater Interface">
        <div class="figure-caption">
          <strong>Figure 145.2 — Robert E. Glover's Dynamic Parabolic Interface Model (1959):</strong> Incorporating seaward freshwater discharge $Q$ and vertical equipotential convergence. The interface forms a smooth, upward-opening parabola with an offshore submarine discharge gap $x_0$, steepening at the coast and flattening inland.
        </div>
      </div>

      <h4>The Hydrostatic Paradox and the Seepage Gap</h4>
      <p>
        While the static Ghyben-Herzberg relation provides a first-order approximation, it suffers from a fatal physical paradox: at the shoreline where the water table intersects sea level ($h_f = 0$), the formula predicts $z = 0$. This would force the interface to intersect the shoreline exactly at the water surface, providing <strong>zero cross-sectional area for freshwater to discharge into the ocean</strong>, which violates continuity and Darcy's Law.
      </p>
      <p>
        In reality, freshwater flows continuously seaward toward the ocean. In 1959, <strong>Robert E. Glover</strong> formulated the exact hydrodynamic solution using complex potential theory for steady 2-dimensional flow in an unconfined coastal aquifer:
      </p>
      <div class="math-block" style="font-size: 1.25rem; font-weight: bold; background: #ecfdf5; border-left: 5px solid #059669; padding: 15px;">
        $$z^2 = \frac{2 Q}{\Delta \rho \cdot K} x + \left(\frac{Q}{\Delta \rho \cdot K}\right)^2$$
      </div>
      <p>
        Where:
      </p>
      <ul>
        <li>$z$ = Depth of the interface below mean sea level at distance $x$ inland ($\text{m}$).</li>
        <li>$x$ = Horizontal distance measured inland from the shoreline ($x \ge 0$) ($\text{m}$).</li>
        <li>$Q$ = Seaward freshwater discharge per unit length of coastline ($\text{m}^3/\text{day per m}$ or $\text{m}^2/\text{s}$).</li>
        <li>$K$ = Saturated hydraulic conductivity of the coastal aquifer ($\text{m/day}$ or $\text{m/s}$).</li>
        <li>$\Delta \rho = \frac{\rho_s - \rho_f}{\rho_f} \approx \frac{1.025 - 1.000}{1.000} = 0.025$ (dimensionless relative density difference).</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q145/bangar_p32_coastal_freshwater_saline_interface.png" alt="Bangar Textbook Hydrogeology Coastal Saline Interface">
        <div class="figure-caption">
          <strong>Figure 145.3 — Facsimile from K.M. Bangar (Principles of Engineering Geology, Ch. 3, p. 32):</strong> Coastal hydrogeology cross-section showing freshwater flow lines, the parabolic interface, and the upward curvature of the boundary separating fresh groundwater from underlying marine seawater.
        </div>
      </div>

      <h4>Mathematical Proof of the "Concave Upward" Geometry</h4>
      <p>
        The algebraic form $z^2 = 2 p x + p^2$ is the canonical equation of a <strong>parabola</strong> opening along the positive horizontal axis. Let us inspect its geometric curvature:
      </p>
      <ol>
        <li>Express depth $z$ as a function of horizontal distance $x$:
          $$z(x) = \sqrt{\frac{2 Q}{\Delta \rho K} x + \left(\frac{Q}{\Delta \rho K}\right)^2}$$
        </li>
        <li>The first derivative represents the interface slope:
          $$\frac{dz}{dx} = \frac{Q}{\Delta \rho K \cdot z} > 0$$
          Because $z$ increases with inland distance $x$, the slope is positive (the interface dips deeper inland).
        </li>
        <li>The second derivative represents the rate of change of slope (curvature):
          $$\frac{d^2 z}{dx^2} = -\frac{Q^2}{(\Delta \rho K)^2 \cdot z^3} < 0$$
        </li>
        <li>In standard geological and geographical cross-sections, elevation $y$ is plotted vertically upward ($y = -z$). Transforming into vertical Cartesian coordinates:
          $$\frac{d^2 y}{dx^2} = -\frac{d^2 z}{dx^2} = +\frac{Q^2}{(\Delta \rho K)^2 \cdot z^3} > 0$$
        </li>
      </ol>
      <div class="definition-box">
        <strong>Geometric Conclusion:</strong><br>
        Because $\frac{d^2 y}{dx^2} > 0$, the mathematical curve is strictly <strong>CONCAVE UPWARD</strong> (it forms a bowl-like profile that curves steeply upward near the shoreline and flattens out gradually inland).
      </div>
    </div>
  </div>

  <!-- CARD 3: SUBMARINE SEEPAGE GAP -->
  <div class="card">
    <div class="card-header bg-indigo">3. Submarine Discharge Gap ($x_0$) and Transition Zone Dynamics</div>
    <div class="card-body">
      <p>
        At the sea surface ($z = 0$), Glover's equation reveals that the interface extends seaward beyond the shoreline by an offshore distance $x_0$:
      </p>
      <div class="math-block">
        $$0 = \frac{2 Q}{\Delta \rho K} x_0 + \left(\frac{Q}{\Delta \rho K}\right)^2 \implies x_0 = -\frac{Q}{2 \Delta \rho K}$$
      </div>
      <p>
        This offshore distance represents the width of the <strong>submarine freshwater seepage gap</strong> through which freshwater discharges into the sea floor under the ocean, preventing seawater from choking the coastal aquifer.
      </p>
      <p>
        Under natural conditions, tidal pulsations, seasonal recharge fluctuations, and molecular diffusion blur the sharp interface into a brackish <strong>transition zone (zone of dispersion)</strong>, but the overarching structural envelope remains strictly concave upward.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-amber">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-box">
        <strong>Question 145:</strong> Choose the correct answer regarding the shape and the nature of the fresh water-saline water interface near to a coastal area from the options given below :
        <div class="options-grid">
          <div class="option-item"><strong>(A)</strong> Linear and horizontal</div>
          <div class="option-item"><strong>(B)</strong> Concave upward</div>
          <div class="option-item"><strong>(C)</strong> Linear and inclined</div>
          <div class="option-item"><strong>(D)</strong> Convex downward</div>
        </div>
      </div>
      <div class="answer-banner">
        <strong>Correct Answer: (B) Concave upward</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION-BY-OPTION REFUTATIONS -->
  <div class="card">
    <div class="card-header bg-red">Forensic Analysis & Option Refutations</div>
    <div class="card-body">

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (A): Linear and horizontal
        </div>
        <div class="option-card-body">
          <p>
            Option (A) posits that the interface is completely flat and horizontal. A horizontal interface would require hydrostatic conditions throughout the entire aquifer where the freshwater table is also perfectly flat and horizontal ($h_f = 0$ everywhere). Under such conditions, the hydraulic gradient is zero ($i = dh/dx = 0$), meaning zero groundwater flow towards the sea ($Q = 0$). In active coastal aquifers where precipitation recharges the hinterland and drives seaward discharge, a horizontal interface is physically impossible.
          </p>
        </div>
      </div>

      <div class="option-card option-correct">
        <div class="option-card-header">
          <span class="badge bg-success">CORRECT</span> Option (B): Concave upward
        </div>
        <div class="option-card-body">
          <p>
            Option (B) represents the exact, hydrodynamically proven geometric configuration of the freshwater-saline water boundary in coastal aquifers:
          </p>
          <ul>
            <li>Under Glover's exact potential flow solution (1959), the interface obeys the parabolic function $z^2 = \frac{2Q}{\Delta \rho K} x + \left(\frac{Q}{\Delta \rho K}\right)^2$.</li>
            <li>In vertical elevation coordinates ($y = -z$), the second derivative is positive ($\frac{d^2 y}{dx^2} > 0$), which mathematically defines a <strong>concave upward profile</strong>.</li>
            <li>Physically, flow lines converge near the coastal discharge gap, producing high vertical velocity gradients that cause the interface to plunge steeply near the coast and flatten asymptotically inland into a horizontal plateau.</li>
          </ul>
          <p>
            Thus, Option (B) is indisputably the correct hydrogeological answer.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (C): Linear and inclined
        </div>
        <div class="option-card-body">
          <p>
            Option (C) reflects a common elementary misconception that arises from applying the basic Ghyben-Herzberg ratio ($z = 40 h_f$) to an idealized planar water table ($h_f = c \cdot x$), which produces a straight sloping line ($z = 40 c x$). However, this crude model completely ignores the vertical flow components near the shoreline, the existence of the submarine seepage face ($x_0$), and the convergence of flow net equipotentials. Rigorous field measurements and hydrodynamic physics prove that the interface is parabolic and distinctly curved (concave upward), not a straight inclined line.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (D): Convex downward
        </div>
        <div class="option-card-body">
          <p>
            Option (D) claims the interface is "convex downward" (which would mean $\frac{d^2 y}{dx^2} < 0$). This inverted curvature would imply that the interface is nearly horizontal at the coastline and curves increasingly steeper as one moves further inland into the continental interior. This is the exact opposite of natural groundwater hydraulics: groundwater flow velocity is highest near the coastal discharge face (causing steep interface dip) and lowest inland where hydraulic gradients flatten. Hence, convex downward violates the fundamental laws of potential flow.
          </p>
        </div>
      </div>

    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Coastal Hydrogeology: Interface Models & Governing Equations</div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Model Formulation</th>
              <th>Interface Shape</th>
              <th>Governing Equation</th>
              <th>Assumptions & Boundary Physics</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Ghyben-Herzberg (1888/1901)</strong></td>
              <td>Linear inclined wedge (approximate)</td>
              <td>$$z = \left(\frac{\rho_f}{\rho_s - \rho_f}\right) h_f \approx 40 h_f$$</td>
              <td>Hydrostatic equilibrium; strictly horizontal flow; zero submarine discharge face ($z=0$ at coast).</td>
            </tr>
            <tr>
              <td><strong>Glover Solution (1959)</strong></td>
              <td><strong>Parabolic (Concave Upward)</strong></td>
              <td>$$z^2 = \frac{2 Q}{\Delta \rho K} x + \left(\frac{Q}{\Delta \rho K}\right)^2$$</td>
              <td>Exact hydrodynamic potential flow; steady 2D discharge $Q$; includes submarine seepage face $x_0$.</td>
            </tr>
            <tr>
              <td><strong>Henry Problem (1964)</strong></td>
              <td>Dispersive S-shaped transition zone</td>
              <td>$$\nabla \cdot (K \nabla h) = 0, \quad \nabla \cdot (D \nabla C) - \mathbf{v} \cdot \nabla C = 0$$</td>
              <td>Coupled density-dependent fluid flow and hydrodynamic salt solute dispersion; non-sharp interface.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- CARD: 8 FULLY WORKED EXAM PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Coastal Hydrogeology Practice Problems (8 Rigorous Exercises)</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Classic Ghyben-Herzberg Interface Depth</strong><br>
        In an unconfined coastal sand aquifer, an observation well situated $250\text{ m}$ from the sea records a water table elevation of $h_f = 2.40\text{ m}$ above mean sea level. Assuming freshwater density $\rho_f = 1.000\text{ g/cm}^3$ and seawater density $\rho_s = 1.025\text{ g/cm}^3$: (a) Calculate the depth to the saltwater interface below mean sea level ($z$). (b) What is the total freshwater saturated column thickness ($H$) at this location?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Interface depth below sea level:
          $$z = \frac{\rho_f}{\rho_s - \rho_f} h_f = \frac{1.000}{1.025 - 1.000} \times 2.40\text{ m} = 40 \times 2.40\text{ m} = 96.0\text{ meters}$$
          2. Total freshwater column thickness:
          $$H = h_f + z = 2.40\text{ m} + 96.0\text{ m} = 98.4\text{ meters}$$
          The entire column of $98.4\text{ m}$ consists of fresh potable water floating above dense saline seawater.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Glover Submarine Discharge Gap Calculation</strong><br>
        A coastal aquifer has a hydraulic conductivity of $K = 30\text{ m/day}$ and discharges freshwater into the ocean at a rate of $Q = 3.6\text{ m}^3/\text{day}$ per meter length of coastline. Taking relative density difference $\Delta \rho = 0.025$: (a) Calculate the seaward width of the submarine discharge gap ($x_0$). (b) What is the depth of the interface directly at the coastline ($x = 0$)?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate parameter term:
          $$\frac{Q}{\Delta \rho \cdot K} = \frac{3.6}{0.025 \times 30} = \frac{3.6}{0.75} = 4.8\text{ meters}$$
          2. Seaward gap width ($x_0$):
          $$x_0 = \frac{Q}{2 \Delta \rho K} = \frac{4.8}{2} = 2.4\text{ meters}$$
          Freshwater discharges through a strip extending $2.4\text{ m}$ offshore along the ocean floor.<br>
          3. Interface depth at the shoreline ($x = 0$):
          $$z(0) = \sqrt{0 + \left(\frac{Q}{\Delta \rho K}\right)^2} = \frac{Q}{\Delta \rho K} = 4.8\text{ meters}$$
          Unlike Ghyben-Herzberg which incorrectly predicts $z(0) = 0$, Glover's solution correctly shows the interface lies $4.8\text{ m}$ beneath the shoreline.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Glover Parabolic Profile Depth Inland</strong><br>
        Using the coastal aquifer parameters from Problem 2 ($Q/(\Delta \rho K) = 4.8\text{ m}$), calculate the interface depth $z$ at inland distances of: (a) $x = 50\text{ m}$, (b) $x = 200\text{ m}$, and (c) $x = 800\text{ m}$. Demonstrate that the rate of interface deepening flattens inland.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Formula: $z(x) = \sqrt{2(4.8)x + (4.8)^2} = \sqrt{9.6 x + 23.04}$<br>
          2. At $x = 50\text{ m}$:
          $$z(50) = \sqrt{9.6(50) + 23.04} = \sqrt{480 + 23.04} = \sqrt{503.04} \approx 22.43\text{ m}$$
          3. At $x = 200\text{ m}$:
          $$z(200) = \sqrt{9.6(200) + 23.04} = \sqrt{1920 + 23.04} = \sqrt{1943.04} \approx 44.08\text{ m}$$
          4. At $x = 800\text{ m}$:
          $$z(800) = \sqrt{9.6(800) + 23.04} = \sqrt{7680 + 23.04} = \sqrt{7703.04} \approx 87.77\text{ m}$$
          5. Slope evaluation:
          From $x = 0$ to $50\text{ m}$, $\Delta z / \Delta x = (22.43 - 4.8) / 50 = 0.353\text{ m/m}$ (very steep).<br>
          From $x = 200$ to $800\text{ m}$, $\Delta z / \Delta x = (87.77 - 44.08) / 600 = 0.0728\text{ m/m}$ ($5\times$ flatter).<br>
          This mathematically proves the <strong>concave upward</strong> nature of the profile.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Upconing Beneath a Pumping Well (Dagan-Bear Criterion)</strong><br>
        A production well in an unconfined coastal aquifer penetrates to a depth leaving a distance of $d = 20\text{ m}$ between the well bottom and the initial flat freshwater-saline interface. If $K = 25\text{ m/day}$ and $\Delta \rho = 0.025$, calculate the critical pumping rate ($Q_c$) above which the saltwater cone becomes unstable and surges directly into the well (upconing threshold $Q_c \approx 0.45 \pi d^2 K \Delta \rho$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Dagan & Bear (1968) critical upconing formula:
          $$Q_c = 0.45 \cdot \pi \cdot d^2 \cdot K \cdot \Delta \rho$$
          2. Substitute values:
          $$Q_c = 0.45 \times 3.14159 \times (20)^2 \times 25 \times 0.025 = 0.45 \times 3.14159 \times 400 \times 0.625$$
          $$Q_c = 565.49 \times 0.625 \approx 353.43\text{ m}^3/\text{day}$$
          Pumping at rates exceeding $353\text{ m}^3/\text{day}$ will cause the saline cusp to enter the well screen, ruining drinking water quality.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Variable Salinity and Estuarine Water Densities</strong><br>
        Calculate the Ghyben-Herzberg depth ratio $\alpha = \rho_f / (\rho_s - \rho_f)$ for three distinct coastal water bodies ($\rho_f = 1.000\text{ g/cm}^3$): (a) Open ocean ($\rho_s = 1.025\text{ g/cm}^3$), (b) Brackish coastal lagoon/estuary ($\rho_s = 1.012\text{ g/cm}^3$), and (c) Hypersaline tidal lagoon ($\rho_s = 1.036\text{ g/cm}^3$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Open ocean:
          $$\alpha_1 = \frac{1.000}{1.025 - 1.000} = \frac{1.000}{0.025} = 40.0$$
          2. Brackish lagoon:
          $$\alpha_2 = \frac{1.000}{1.012 - 1.000} = \frac{1.000}{0.012} \approx 83.33$$
          3. Hypersaline lagoon:
          $$\alpha_3 = \frac{1.000}{1.036 - 1.000} = \frac{1.000}{0.036} \approx 27.78$$
          <em>Physical Insight:</em> Along brackish estuaries, a $1\text{ m}$ head drop causes over $83\text{ m}$ of saline encroachment, making estuarine groundwater systems twice as sensitive to over-abstraction as open ocean coasts.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Sea Level Rise Impact on Interface Migration</strong><br>
        A coastal plain has a Regional water table slope of $i = dh/dx = 0.0015$ inland. Global climate change produces a projected sea level rise of $\Delta h_{\text{sea}} = 0.60\text{ meters}$. Assuming the regional freshwater table elevation remains unchanged, calculate the horizontal inland migration distance of the saltwater interface toe ($\Delta x$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Effective loss of freshwater head relative to new sea level:
          $$\Delta h_f = 0.60\text{ m}$$
          2. Horizontal distance needed to regain $0.60\text{ m}$ of water table head under slope $i = 0.0015$:
          $$\Delta x = \frac{\Delta h_f}{i} = \frac{0.60\text{ m}}{0.0015} = 400\text{ meters}$$
          A seemingly modest $60\text{ cm}$ sea level rise drives the saltwater wedge <strong>$400\text{ meters}$ further inland</strong>, contaminating coastal shallow wells across the aquifer.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Tidal Mixing & Dispersion Zone Thickness</strong><br>
        Instead of a knife-sharp interface, an unconfined coastal aquifer develops a transition zone governed by 1D advective-dispersive transport. If longitudinal dispersivity is $\alpha_L = 2.0\text{ m}$ and average pore velocity is $v = 0.4\text{ m/day}$, calculate: (a) The hydrodynamic dispersion coefficient ($D_L = \alpha_L v$), and (b) Estimate the transition zone width $W \approx 4 \sqrt{D_L t}$ after $t = 30\text{ days}$ of continuous tidal cycling.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Dispersion coefficient:
          $$D_L = \alpha_L \cdot v = 2.0\text{ m} \times 0.4\text{ m/day} = 0.8\text{ m}^2/\text{day}$$
          2. Transition zone thickness:
          $$W \approx 4 \sqrt{D_L t} = 4 \sqrt{0.8 \times 30} = 4 \sqrt{24} = 4 \times 4.899 \approx 19.6\text{ meters}$$
          Tidal action transforms the boundary into a $19.6\text{ m}$ wide zone of brackish water (salinity $1,000 - 30,000\text{ mg/L}$).
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Engineered Hydraulic Pressure Barrier</strong><br>
        To repel an advancing saline wedge, an injection well array is installed along the coast. If the required seaward gradient to halt saltwater movement is $i_{\text{req}} = 0.003$ and the coastal aquifer transmissivity is $T = 600\text{ m}^2/\text{day}$, calculate the continuous freshwater recharge rate ($q_{\text{inj}}$) required per kilometer of coastline.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Recharge discharge per meter width of coast:
          $$q' = T \cdot i_{\text{req}} = 600\text{ m}^2/\text{day} \times 0.003 = 1.8\text{ m}^3/\text{day per m}$$
          2. Total injection discharge per kilometer ($L = 1000\text{ m}$):
          $$Q_{\text{total}} = q' \times L = 1.8\text{ m}^3/\text{day/m} \times 1000\text{ m} = 1,800\text{ m}^3/\text{day}$$
          A line of injection wells recharging $1.8\text{ MLD}$ (million liters per day) creates a freshwater hydraulic pressure ridge that repels saltwater seaward.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(
        q_num=145,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q145_Coastal_Fresh_Saline_Interface_Geometry_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q145: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q145()
