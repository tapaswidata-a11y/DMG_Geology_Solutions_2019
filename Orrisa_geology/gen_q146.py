#!/usr/bin/env python3
"""
Q146 Generator: Pumping Period vs Recovery Period Parameters (Residual Drawdown)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q146():
    title = r"Q146: Hydrogeology: Pumping Test Parameters & Residual Drawdown | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Hydrogeology & Well Hydraulics"
    h1_title = "Q146: Aquifer Hydraulics: Pumping Period vs Post-Pumping Residual Drawdown Recovery"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 146<br>
<strong>Authoritative References:</strong> Charles V. Theis, <em>The Relation Between the Lowering of the Piezometric Surface and the Rate and Duration of Discharge of a Well Using Ground-Water Storage</em> (Trans. AGU, 1935); David K. Todd and Larry W. Mays, <em>Groundwater Hydrology</em> (3rd Ed., Wiley, Ch. 4: Well Hydraulics, pp. 135–158); C.W. Fetter, <em>Applied Hydrogeology</em> (4th Ed., Prentice Hall, Ch. 5, pp. 175–188); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 3: Hydrogeology, p. 33)."""

    part1 = r"""
  <!-- CARD 1: WORKING PRINCIPLES OF WELL HYDRAULIC TESTING -->
  <div class="card">
    <div class="card-header bg-blue">1. Architecture of an Aquifer Pumping Test: Pumping Phase vs Recovery Phase</div>
    <div class="card-body">
      <p>
        In groundwater hydrology, an <strong>Aquifer Performance Test (Pumping Test)</strong> is the standard field methodology used to quantify the primary hydrodynamic parameters of an aquifer: <strong>Transmissivity ($T$)</strong> and <strong>Storativity ($S$)</strong> (Theis, 1935; Todd & Mays, 2005; Fetter, 2001; Bangar, p. 33).
      </p>
      <p>
        A complete pumping test consists of two distinct, mutually exclusive operational periods:
      </p>
      <ol>
        <li><strong>The Pumping Period:</strong> Water is continuously discharged from a production well at a measured rate $Q$ for a predetermined duration $t_p$. Hydraulic head declines throughout the surrounding formation, establishing a dynamic cone of depression.</li>
        <li><strong>The Recovery Period:</strong> The pump is abruptly shut down at time $t = t_p$. Groundwater flows inward from the outer edges of the cone of depression, causing piezometric levels in the well and surrounding piezometers to rise back toward the pre-pumping static equilibrium level.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q146/pumping_test_recovery_residual_drawdown_timeline.png" alt="Pumping Test Recovery Residual Drawdown Timeline">
        <div class="figure-caption">
          <strong>Figure 146.1 — Complete Pumping and Recovery Timeline:</strong> Evolution of water levels during continuous pumping (duration $t_p$) exhibiting active drawdown $s(t)$, followed by post-pumping recovery (elapsed recovery time $t'$) exhibiting <em>residual drawdown</em> $s'(t')$.
        </div>
      </div>

      <h4>Parameters Gathered During the Active Pumping Period</h4>
      <p>
        While the pump is actively operating ($0 \le t \le t_p$), hydrogeologists gather three fundamental datasets:
      </p>
      <ul>
        <li><strong>Drawdown ($s$):</strong> The instantaneous vertical decline in hydraulic head relative to the initial static water table ($s = h_0 - h$).</li>
        <li><strong>Time-Drawdown Data:</strong> A continuous time series recording the progressive deepening of drawdown $s$ against elapsed pumping time $t$ in individual observation wells.</li>
        <li><strong>Distance-Drawdown Data:</strong> Simultaneous measurements of drawdown $s$ recorded at the same elapsed time across multiple observation wells located at varying radial distances $r_1, r_2, \dots, r_n$ from the pumping center.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: THEIS RECOVERY & RESIDUAL DRAWDOWN -->
  <div class="card">
    <div class="card-header bg-emerald">2. Theis Recovery Method & Definition of Residual Drawdown ($s'$)</div>
    <div class="card-body">
      <div class="figure-box">
        <img src="../../figures_Q146/bangar_p33_pumping_test_residual_drawdown.png" alt="Bangar Textbook Hydrogeology Residual Drawdown Scan">
        <div class="figure-caption">
          <strong>Figure 146.2 — Facsimile from K.M. Bangar (Principles of Engineering Geology, Ch. 3, p. 33):</strong> Detailed treatment of well pumping hydraulics, the principle of superposition during recovery, and semilog analysis of residual drawdown $s'$ versus dimensionless time ratio $t/t'$.
        </div>
      </div>

      <h4>Definition of Residual Drawdown ($s'$)</h4>
      <div class="definition-box">
        <strong>Residual Drawdown ($s'$):</strong><br>
        During the recovery period after pumping has ceased, <strong>Residual Drawdown</strong> is defined as the difference between the original pre-pumping static water level ($h_0$) and the recovering water level ($h$) at elapsed recovery time $t'$:
        $$s' = h_0 - h(t') \quad [\text{meters}]$$
        Residual drawdown exists and is measured <strong>exclusively during the recovery period</strong>. It cannot exist during the active pumping period.
      </div>

      <h4>Theis Superposition Theorem for Recovery</h4>
      <p>
        In 1935, <strong>C.V. Theis</strong> demonstrated that recovery can be modeled mathematically by applying the <strong>Principle of Superposition</strong>:
      </p>
      <ul>
        <li>Assume the pumping well continues to discharge at rate $Q$ indefinitely from $t = 0$.</li>
        <li>At time $t = t_p$ (when the pump is actually shut off), an imaginary recharge well is introduced at the same location, injecting water into the aquifer at an identical rate $+Q$.</li>
      </ul>
      <p>
        The net residual drawdown $s'$ at any elapsed recovery time $t'$ (where total elapsed time from the start of pumping is $t = t_p + t'$) is the algebraic sum of the continuing drawdown minus the recharge buildup:
      </p>
      <div class="math-block">
        $$s' = \frac{Q}{4 \pi T} \left[ W(u) - W(u') \right]$$
        $$\text{where } u = \frac{r^2 S}{4 T t} \quad \text{and} \quad u' = \frac{r^2 S'}{4 T t'}$$
      </div>
      <p>
        For sufficiently long pumping and recovery times ($u, u' \le 0.05$), truncating the well function series yields the famous <strong>Theis Recovery Formula</strong>:
      </p>
      <div class="math-block" style="font-size: 1.25rem; font-weight: bold; background: #ecfdf5; border-left: 5px solid #059669; padding: 15px;">
        $$s' = \frac{2.303 Q}{4 \pi T} \log_{10}\left(\frac{t}{t'}\right)$$
      </div>
      <p>
        A plot of residual drawdown $s'$ on arithmetic scale versus the dimensionless time ratio $t/t'$ on logarithmic scale forms a straight line whose slope $\Delta s'$ yields Transmissivity ($T$):
      </p>
      <div class="math-block">
        $$T = \frac{2.303 Q}{4 \pi \Delta s'}$$
      </div>
    </div>
  </div>

  <!-- CARD 3: OPERATIONAL SUPERIORITY OF RECOVERY TESTING -->
  <div class="card">
    <div class="card-header bg-indigo">3. Why Hydrogeologists Prefer Recovery Analysis</div>
    <div class="card-body">
      <p>
        In hydrogeological practice, recovery test data are often considered <strong>far more reliable and precise</strong> than active pumping test data for determining formation transmissivity:
      </p>
      <ol>
        <li><strong>Absence of Discharge Fluctuations:</strong> During pumping, maintaining an exactly constant discharge $Q$ is difficult due to engine speed variations, generator cycling, and falling dynamic water levels. In recovery, $Q = 0$ is absolute and unvarying.</li>
        <li><strong>Elimination of Turbulent Well Losses:</strong> In an active pumping well, turbulent frictional head loss across the well screen and gravel pack ($s_w = B Q + C Q^2$) distorts water level readings. During recovery, no water is withdrawn, eliminating turbulent wellbore head loss entirely ($C Q^2 = 0$).</li>
        <li><strong>No Water Cascading or Entrained Air:</strong> Pumping water levels are often disrupted by cascading water from perforated casing sections above the pump inlet. Recovery levels rise smoothly under laminar conditions.</li>
      </ol>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-amber">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-box">
        <strong>Question 146:</strong> Find out the term which is not related to the pumping period of a well :
        <div class="options-grid">
          <div class="option-item"><strong>(A)</strong> Drawdown</div>
          <div class="option-item"><strong>(B)</strong> Time-drawdown data</div>
          <div class="option-item"><strong>(C)</strong> Residual drawdown</div>
          <div class="option-item"><strong>(D)</strong> Distance-drawdown data</div>
        </div>
      </div>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Residual drawdown</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION-BY-OPTION REFUTATIONS -->
  <div class="card">
    <div class="card-header bg-red">Forensic Analysis & Option Refutations</div>
    <div class="card-body">

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT SELECTION</span> Option (A): Drawdown
        </div>
        <div class="option-card-body">
          <p>
            Drawdown ($s = h_0 - h$) is the primary dependent physical variable measured throughout the <strong>active pumping period</strong> of a well. It quantifies the instantaneous head drop induced by groundwater extraction. Because drawdown is intimately and directly related to the pumping period, selecting Option (A) is incorrect.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT SELECTION</span> Option (B): Time-drawdown data
        </div>
        <div class="option-card-body">
          <p>
            Time-drawdown data consists of the progressive decline in piezometric head recorded against elapsed pumping time ($t$) from the start of pumping. It forms the empirical basis for the Theis curve-matching and Cooper-Jacob straight-line methods evaluated during the <strong>pumping period</strong>. Thus, Option (B) is a core pumping-phase parameter.
          </p>
        </div>
      </div>

      <div class="option-card option-correct">
        <div class="option-card-header">
          <span class="badge bg-success">CORRECT ANSWER</span> Option (C): Residual drawdown
        </div>
        <div class="option-card-body">
          <p>
            Option (C) is the single parameter that is <strong>NOT related to the pumping period</strong>:
          </p>
          <ul>
            <li>By standard hydrogeological definition (Theis, 1935; Todd & Mays; Fetter), <strong>Residual Drawdown ($s'$)</strong> is measured exclusively during the <strong>recovery period</strong> following complete pump shutdown ($t > t_p$).</li>
            <li>It represents the difference between the original pre-pumping static water level and the rising water level during recovery.</li>
            <li>While the pump is running, only active drawdown ($s$) exists. Residual drawdown cannot be observed until the pumping phase has fully terminated.</li>
          </ul>
          <p>
            Therefore, Option (C) is the unambiguous correct choice.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT SELECTION</span> Option (D): Distance-drawdown data
        </div>
        <div class="option-card-body">
          <p>
            Distance-drawdown data represents simultaneous measurements of drawdown across multiple observation wells located at various radial distances ($r$) from the pumping well at a specific time $t$ during the <strong>active pumping period</strong>. It is used to plot the cone of depression and calculate transmissivity and storativity via the Cooper-Jacob distance method ($s$ vs $\log r$). Hence, it belongs strictly to the pumping phase.
          </p>
        </div>
      </div>

    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Hydrogeologic Synthesis: Pumping Phase vs Recovery Phase Parameters</div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Hydraulic Parameter</th>
              <th>Test Period</th>
              <th>Mathematical Notation</th>
              <th>Governing Analytical Relationship</th>
              <th>Physical Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Active Drawdown</strong></td>
              <td>Pumping Phase ($t \le t_p$)</td>
              <td>$$s = h_0 - h(t)$$</td>
              <td>$$s = \frac{Q}{4 \pi T} W\left(\frac{r^2 S}{4 T t}\right)$$</td>
              <td>Total decline of piezometric head below static baseline during pumping.</td>
            </tr>
            <tr>
              <td><strong>Time-Drawdown Data</strong></td>
              <td>Pumping Phase ($t \le t_p$)</td>
              <td>$$s \text{ vs } t$$</td>
              <td>$$s = \frac{2.303 Q}{4 \pi T} \log_{10}\left(\frac{2.25 T t}{r^2 S}\right)$$</td>
              <td>Chronological progression of head drop in a single observation well.</td>
            </tr>
            <tr>
              <td><strong>Distance-Drawdown Data</strong></td>
              <td>Pumping Phase ($t \le t_p$)</td>
              <td>$$s \text{ vs } r$$</td>
              <td>$$s = \frac{2.303 Q}{2 \pi T} \log_{10}\left(\frac{r_0}{r}\right)$$</td>
              <td>Radial profile of the cone of depression across multiple piezometers at fixed $t$.</td>
            </tr>
            <tr>
              <td><strong>Residual Drawdown</strong></td>
              <td><strong>Recovery Phase ONLY ($t > t_p$)</strong></td>
              <td>$$s' = h_0 - h(t')$$</td>
              <td>$$s' = \frac{2.303 Q}{4 \pi T} \log_{10}\left(\frac{t}{t'}\right)$$</td>
              <td>Residual unrecovered head drop remaining after pump shutdown at recovery time $t'$.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- CARD: 8 FULLY WORKED EXAM PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Well Hydraulics Practice Problems (8 Rigorous Exercises)</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Transmissivity Determination from Theis Recovery Plot</strong><br>
        A well is pumped at a constant discharge of $Q = 1440\text{ m}^3/\text{day}$ for $t_p = 24\text{ hours}$ and then shut down. Measurements of residual drawdown $s'$ are plotted against $\log_{10}(t/t')$, where $t = t_p + t'$. The straight line fitted through the data reveals a drawdown change per log cycle of $\Delta s' = 0.92\text{ m}$. Calculate the Transmissivity ($T$) of the aquifer in: (a) $\text{m}^2/\text{day}$, and (b) $\text{m}^2/\text{s}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Theis recovery transmissivity formula:
          $$T = \frac{2.303 Q}{4 \pi \Delta s'} = \frac{2.303 \times 1440}{4 \times 3.14159 \times 0.92} = \frac{3316.32}{11.561} \approx 286.85\text{ m}^2/\text{day}$$
          2. Convert to $\text{m}^2/\text{s}$:
          $$T = \frac{286.85\text{ m}^2/\text{day}}{86,400\text{ s/day}} \approx 3.32 \times 10^{-3}\text{ m}^2/\text{s}$$
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Calculation of Expected Residual Drawdown</strong><br>
        A confined aquifer has $T = 400\text{ m}^2/\text{day}$. A well is pumped at $Q = 1200\text{ m}^3/\text{day}$ for $t_p = 10\text{ hours}$ ($600\text{ min}$). Calculate the theoretical residual drawdown $s'$ in an observation well after: (a) $t' = 30\text{ minutes}$ of recovery, and (b) $t' = 300\text{ minutes}$ of recovery.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Parameter coefficient:
          $$\frac{2.303 Q}{4 \pi T} = \frac{2.303 \times 1200}{4 \times 3.14159 \times 400} = \frac{2763.6}{5026.55} \approx 0.5498\text{ meters per log cycle}$$
          2. At $t' = 30\text{ min}$, total time $t = 600 + 30 = 630\text{ min}$:
          $$\frac{t}{t'} = \frac{630}{30} = 21 \implies \log_{10}(21) \approx 1.3222$$
          $$s'(30) = 0.5498 \times 1.3222 \approx 0.727\text{ meters}$$
          3. At $t' = 300\text{ min}$, total time $t = 600 + 300 = 900\text{ min}$:
          $$\frac{t}{t'} = \frac{900}{300} = 3.0 \implies \log_{10}(3.0) \approx 0.4771$$
          $$s'(300) = 0.5498 \times 0.4771 \approx 0.262\text{ meters}$$
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Hydrogeologic Boundary Diagnostics from Recovery Intercept</strong><br>
        In an ideal infinite, homogeneous, isotropic confined aquifer, the theoretical straight line of $s'$ vs $\log(t/t')$ extrapolates to zero residual drawdown ($s' = 0$) at precisely $t/t' = 1.0$. Explain what hydrogeologic conditions are indicated if field data extrapolate to: (a) $t/t' > 1.0$ at $s' = 0$, and (b) $t/t' < 1.0$ at $s' = 0$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. <strong>Case (a) $t/t' > 1.0$ at $s' = 0$:</strong> The recovering water level reaches static equilibrium before $t/t' = 1.0$. This signifies that the aquifer received <strong>recharge from an external source</strong> during the test (e.g., intersection with a recharge boundary such as a perennial river or lake, or downward leakage from an overlying formation).<br>
          2. <strong>Case (b) $t/t' < 1.0$ at $s' = 0$:</strong> The straight line extrapolates to a value of $t/t' < 1.0$, meaning that even after infinite recovery time ($t' \to \infty, t/t' \to 1.0$), some residual drawdown remains unrecovered. This indicates either an <strong>impermeable barrier boundary</strong> (fault, bedrock pinchout), aquifer depletive overdraft, or that storativity during recovery ($S'$) differs from storativity during pumping ($S$).
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Distance-Drawdown Determination of Storativity</strong><br>
        During the active pumping period of a test ($Q = 2000\text{ m}^3/\text{day}$, $t = 480\text{ minutes} = 0.333\text{ days}$), simultaneous drawdowns measured in two piezometers are $s_1 = 1.85\text{ m}$ at $r_1 = 20\text{ m}$, and $s_2 = 0.95\text{ m}$ at $r_2 = 80\text{ m}$. Calculate: (a) Aquifer Transmissivity ($T$), and (b) Aquifer Storativity ($S$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Distance-drawdown formula:
          $$s_1 - s_2 = \frac{2.303 Q}{2 \pi T} \log_{10}\left(\frac{r_2}{r_1}\right)$$
          $$1.85 - 0.95 = 0.90\text{ m} = \frac{2.303 \times 2000}{2 \times 3.14159 \times T} \log_{10}\left(\frac{80}{20}\right) = \frac{4606}{6.2832 T} \log_{10}(4)$$
          $$0.90 = \frac{733.06}{T} \times 0.60206 = \frac{441.35}{T} \implies T = \frac{441.35}{0.90} \approx 490.4\text{ m}^2/\text{day}$$
          2. Zero-drawdown radius ($r_0$):
          $$s_1 = \frac{2.303 Q}{2 \pi T} \log_{10}\left(\frac{r_0}{r_1}\right) \implies 1.85 = \frac{4606}{3081.2} \log_{10}\left(\frac{r_0}{20}\right) = 1.4948 \log_{10}\left(\frac{r_0}{20}\right)$$
          $$\log_{10}\left(\frac{r_0}{20}\right) = \frac{1.85}{1.4948} = 1.2376 \implies \frac{r_0}{20} = 10^{1.2376} \approx 17.28 \implies r_0 \approx 345.6\text{ m}$$
          3. Storativity:
          $$S = \frac{2.25 T t}{r_0^2} = \frac{2.25 \times 490.4 \times 0.333}{(345.6)^2} = \frac{367.43}{119,439} \approx 3.08 \times 10^{-3}$$
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Wellbore Storage Distortion at Very Early Recovery Time</strong><br>
        In a pumping well of casing radius $r_c = 0.15\text{ m}$, water level recovery is initially dominated by wellbore storage (casing refilling) rather than aquifer inflow. The critical time after which wellbore storage effects become negligible is given by Papadopulos and Cooper (1967) as $t'_c \ge \frac{25 r_c^2}{T}$. For $T = 150\text{ m}^2/\text{day}$, calculate $t'_c$ in seconds.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate $t'_c$ in days:
          $$t'_c = \frac{25 \times (0.15)^2}{150} = \frac{25 \times 0.0225}{150} = \frac{0.5625}{150} = 0.00375\text{ days}$$
          2. Convert to minutes and seconds:
          $$t'_c = 0.00375\text{ days} \times 1440\text{ min/day} = 5.4\text{ minutes} = 324\text{ seconds}$$
          Recovery data collected prior to $5.4\text{ minutes}$ reflect water filling the open casing rather than true Darcy flow through the aquifer formation.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Well Efficiency and Turbulent Skin Effect</strong><br>
        During pumping at $Q = 1500\text{ m}^3/\text{day}$, the total drawdown measured inside the pumped well is $s_w = 6.80\text{ m}$. Transmissivity computed from recovery analysis is $T = 320\text{ m}^2/\text{day}$, which predicts a theoretical laminar aquifer drawdown of $s_{\text{formation}} = 4.25\text{ m}$. (a) Calculate the well loss component ($s_{\text{well loss}}$). (b) Determine the Well Efficiency ($E_w$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Well loss due to screen entrance turbulence and gravel pack head loss:
          $$s_{\text{well loss}} = s_w - s_{\text{formation}} = 6.80\text{ m} - 4.25\text{ m} = 2.55\text{ meters}$$
          2. Well Efficiency:
          $$E_w = \left(\frac{s_{\text{formation}}}{s_w}\right) \times 100\% = \left(\frac{4.25}{6.80}\right) \times 100\% \approx 62.5\%$$
          Recovery testing uniquely isolated the true aquifer transmissivity without distortion from the $2.55\text{ m}$ well loss.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Residual Drawdown under Step-Drawdown Pumping History</strong><br>
        A well is pumped in two consecutive steps before shutdown: Step 1 at $Q_1 = 800\text{ m}^3/\text{day}$ for duration $t_1 = 4\text{ hours}$ ($240\text{ min}$), followed immediately by Step 2 at $Q_2 = 1400\text{ m}^3/\text{day}$ for duration $t_2 = 4\text{ hours}$ ($240\text{ min}$, total pumping $t_p = 480\text{ min}$). Formulate the generalized superposition recovery equation for residual drawdown $s'$ at recovery time $t'$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. By generalized multi-rate superposition:
          $$s'(t') = \frac{2.303}{4 \pi T} \left[ Q_1 \log_{10}\left(\frac{t_1 + t_2 + t'}{t_2 + t'}\right) + Q_2 \log_{10}\left(\frac{t_2 + t'}{t'}\right) \right]$$
          2. For $t' = 60\text{ min}$:
          $$s'(60) = \frac{2.303}{4 \pi T} \left[ 800 \log_{10}\left(\frac{240 + 240 + 60}{240 + 60}\right) + 1400 \log_{10}\left(\frac{240 + 60}{60}\right) \right]$$
          $$s'(60) = \frac{2.303}{4 \pi T} \left[ 800 \log_{10}\left(\frac{540}{300}\right) + 1400 \log_{10}(5) \right] = \frac{2.303}{4 \pi T} [ 800(0.2553) + 1400(0.6990) ]$$
          $$s'(60) = \frac{2.303}{4 \pi T} [ 204.24 + 978.60 ] = \frac{2.303 \times 1182.84}{4 \pi T}$$
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Comparison Between Pumping and Recovery Data Robustness</strong><br>
        A field pump test experiences an unmonitored generator throttle surge at $t = 180\text{ minutes}$ that increases discharge from $1000\text{ m}^3/\text{day}$ to $1150\text{ m}^3/\text{day}$. Explain why this generator failure invalidates Cooper-Jacob pumping curve analysis but leaves subsequent post-shutdown Theis recovery analysis unaffected if the final rate is recorded.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. <strong>Pumping Period Invalidation:</strong> Cooper-Jacob and Theis type-curve methods strictly assume a constant discharge $Q$. The $15\%$ jump in $Q$ creates a secondary pressure wave, causing drawdowns to deviate unpredictably from the standard logarithmic curve and producing erroneous values for $T$ and $S$.<br>
          2. <strong>Recovery Period Robustness:</strong> Once the pump is completely stopped, the discharge is exactly $Q = 0.000\text{ m}^3/\text{day}$ with zero fluctuations. The subsequent recovery curve converges to the late-time average discharge, allowing reliable evaluation of formation transmissivity.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(
        q_num=146,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q146_Residual_Drawdown_Recovery_Period_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q146: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q146()
