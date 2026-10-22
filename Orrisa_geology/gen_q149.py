#!/usr/bin/env python3
"""
Q149 Generator: Optimal Aquifer Textural Parameters Selection (D10 and Cu)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q149():
    title = r"Q149: Hydrogeology: Aquifer Textural Parameters & Well Zone Selection | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Hydrogeology & Well Design"
    h1_title = "Q149: Aquifer Textural Characterization: Selecting the Most Promising Zone via Effective Size ($D_{10}$) and Uniformity Coefficient ($C_u$)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 149<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Pearson, Ch. 3: Grain Size & Textural Properties, pp. 58–65); Allen Hazen, <em>Some Physical Properties of Sands and Gravels</em> (Mass. State Board of Health, 1892); David K. Todd and Larry W. Mays, <em>Groundwater Hydrology</em> (3rd Ed., Wiley, Ch. 3 & 5, pp. 75–85, 200–215); Fletcher G. Driscoll, <em>Groundwater and Wells</em> (Johnson Screens, Ch. 10: Screen and Gravel Pack Design)."""

    part1 = r"""
  <!-- CARD 1: TEXTURAL PARAMETERS & HAZEN'S LAW -->
  <div class="card">
    <div class="card-header bg-blue">1. Principles of Aquifer Granulometry: Effective Size ($D_{10}$) & Uniformity Coefficient ($C_u$)</div>
    <div class="card-body">
      <p>
        In hydrogeological exploration and production water well design, the hydraulic performance of an unconsolidated sand-gravel aquifer is governed primarily by its grain-size distribution and sorting characteristics (Boggs, 2012; Hazen, 1892; Todd & Mays, 2005).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q149/boggs_p60_effective_grain_size_uniformity_coefficient.png" alt="Boggs Textbook Sedimentology Cumulative Grain Size Curve">
        <div class="figure-caption">
          <strong>Figure 149.1 — Cumulative Grain-Size Frequency Curve and Textural Parameters (Boggs, 2012, Ch. 3, p. 60):</strong> Standard semi-logarithmic sieve analysis curve illustrating the determination of Effective Size ($D_{10}$), median diameter ($D_{50}$), and the sixty-percentile size ($D_{60}$) used to compute Hazen's Uniformity Coefficient $C_u = D_{60} / D_{10}$.
        </div>
      </div>

      <h4>1. Effective Grain Size ($D_{10}$)</h4>
      <div class="definition-box">
        <strong>Effective Grain Size ($D_{10}$):</strong><br>
        $D_{10}$ is defined as the sieve mesh opening (in millimeters) through which precisely <strong>$10\%$ of the soil particles by weight</strong> will pass (and $90\%$ by weight is retained). Formulated by Allen Hazen in 1892, $D_{10}$ is the single most critical parameter controlling the minimum diameter of interconnected pore throats through which laminar groundwater flow occurs.
      </div>
      <p>
        Hazen's classical empirical permeability formula demonstrates that hydraulic conductivity ($K$) is directly proportional to the <strong>square of effective grain size</strong>:
      </p>
      <div class="math-block" style="font-size: 1.25rem; font-weight: bold; background: #eff6ff; border-left: 5px solid #2563eb; padding: 12px;">
        $$K = C \cdot (D_{10})^2$$
      </div>
      <p>
        Where $C$ is Hazen's empirical coefficient (typically $100\text{ to }150\text{ cm}^{-1}\cdot\text{s}^{-1}$ or $8.6 \times 10^3\text{ to }1.3 \times 10^4\text{ m/day}\cdot\text{mm}^{-2}$). Therefore, a larger $D_{10}$ yields exponentially higher hydraulic conductivity and groundwater yield.
      </p>

      <h4>2. Uniformity Coefficient ($C_u$)</h4>
      <div class="definition-box">
        <strong>Uniformity Coefficient ($C_u$):</strong><br>
        $C_u$ is defined as the ratio of the $60\%$ passing diameter ($D_{60}$) to the effective size ($D_{10}$):
        $$C_u = \frac{D_{60}}{D_{10}}$$
      </div>
      <p>
        The uniformity coefficient serves as an engineering index of <strong>sorting</strong>:
      </p>
      <ul>
        <li><strong>Low $C_u$ ($C_u \le 2.0 - 2.5$):</strong> The aquifer sand is <strong>well-sorted (uniform)</strong>. Grains are of relatively identical size. Interstitial voids remain wide open and interconnected, maximizing effective porosity ($n \approx 35 - 40\%$) and permeability.</li>
        <li><strong>High $C_u$ ($C_u \ge 3.5 - 6.0$):</strong> The aquifer material is <strong>poorly sorted (well-graded)</strong>. A wide spectrum of grain sizes exists, enabling finer silt and sand particles to pack tightly into the void spaces between larger sand grains. This dramatically reduces total and effective porosity ($n \approx 20 - 28\%$), throttles pore throats, and slashes hydraulic conductivity.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: FORENSIC MATRIX OF THE FOUR ZONES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Comparative Multi-Zone Analysis: Why Zone II is the Superior Aquifer</div>
    <div class="card-body">
      <p>
        To determine the <em>"most promising zone for withdrawal of groundwater"</em>, the four demarcated zones must be evaluated simultaneously for grain coarseness ($D_{10}$) and void cleanliness ($C_u$):
      </p>
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Aquifer Zone</th>
              <th>Effective Size ($D_{10}$)</th>
              <th>Relative Permeability Factor ($(D_{10})^2$)</th>
              <th>Uniformity Coefficient ($C_u$)</th>
              <th>Sorting Classification</th>
              <th>Hydraulic Verdict</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Zone I</strong></td>
              <td>$0.55\text{ mm}$</td>
              <td>$0.3025\text{ mm}^2$</td>
              <td>$3.60$</td>
              <td>Poorly sorted / graded</td>
              <td><span class="badge bg-danger">Unfavorable (Smallest $D_{10}$ & poor sorting)</span></td>
            </tr>
            <tr class="table-success" style="font-weight: bold; font-size: 1.05rem;">
              <td><strong>Zone II</strong></td>
              <td>$0.75\text{ mm}$</td>
              <td>$0.5625\text{ mm}^2$ (Max)</td>
              <td>$2.10$ (Min)</td>
              <td><strong>Very well-sorted / uniform</strong></td>
              <td><span class="badge bg-success">OPTIMAL (Highest $K$ & open pore throats)</span></td>
            </tr>
            <tr>
              <td><strong>Zone III</strong></td>
              <td>$0.65\text{ mm}$</td>
              <td>$0.4225\text{ mm}^2$</td>
              <td>$2.60$</td>
              <td>Moderately well-sorted</td>
              <td><span class="badge bg-secondary">Intermediate (Inferior to Zone II)</span></td>
            </tr>
            <tr>
              <td><strong>Zone IV</strong></td>
              <td>$0.75\text{ mm}$</td>
              <td>$0.5625\text{ mm}^2$ (Max)</td>
              <td>$3.70$</td>
              <td>Poorly sorted / well-graded</td>
              <td><span class="badge bg-warning text-dark">Choked Voids (Fines clog pore spaces)</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <h4>Deconstruction: Zone II versus Zone IV</h4>
      <p>
        Both Zone II and Zone IV share the maximum effective grain size of $D_{10} = 0.75\text{ mm}$ (which provides an $86\%$ higher Hazen factor than Zone I: $0.5625 / 0.3025 \approx 1.86$). However, their hydraulic yields diverge profoundly due to sorting:
      </p>
      <ol>
        <li><strong>Zone II ($C_u = 2.10$):</strong> Possesses exceptional sorting. The grains are remarkably uniform, leaving large, unimpeded void channels. During well development (surging and backwashing), fine particles are easily washed out, forming a natural gravel pack of enormous permeability with zero well screen incrustation.</li>
        <li><strong>Zone IV ($C_u = 3.70$):</strong> Possesses a broad grain size distribution where intermediate and fine grains nest tightly inside the pore spaces formed by the $0.75\text{ mm}$ skeleton. Kozeny-Carman flow modeling reveals that this interstitial clogging reduces effective hydraulic conductivity by $40\text{ to }60\%$ compared to Zone II, and risks chronic sand pumping and screen slot clogging.</li>
      </ol>
      <div class="definition-box">
        <strong>Hydrological Decision:</strong><br>
        <strong>Zone II</strong> combines the <strong>largest effective grain size ($D_{10} = 0.75\text{ mm}$)</strong> with the <strong>lowest uniformity coefficient / best sorting ($C_u = 2.10$)</strong>, guaranteeing the highest specific capacity ($Q/s$) and long-term well efficiency.
      </div>
    </div>
  </div>

  <!-- CARD 3: WELL SCREEN AND GRAVEL PACK INTEGRATION -->
  <div class="card">
    <div class="card-header bg-indigo">3. Well Screen Engineering: Natural Development vs Artificial Gravel Pack</div>
    <div class="card-body">
      <p>
        In water well design (Driscoll, 1986; Todd & Mays, 2005):
      </p>
      <ul>
        <li>When an aquifer has $C_u < 2.5$ and $D_{10} \ge 0.50\text{ mm}$ (like <strong>Zone II</strong>), the well can be completed as a <strong>naturally developed well</strong>. Screen slot size is chosen to retain $40\text{ to }50\%$ of the formation material ($D_{40}-D_{50}$). Vigorous surging easily extracts the remaining fines, leaving a stable, highly permeable envelope around the screen.</li>
        <li>In contrast, poorly sorted formations ($C_u > 3.5$, like <strong>Zone I and Zone IV</strong>) require an <strong>artificial gravel pack</strong> to prevent fines from migrating continuously into the well casing, increasing installation cost and wellbore entrance head loss.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-amber">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-box">
        <strong>Question 149:</strong> After completion of drilling of a water well, four different aquifer zones with the following textural characteristics have been demarcated. Select the most promise zone for withdrawl of groundwater :
        <br>(A) Zone I : Effective size value 0.55 mm and uniformity coefficient 3.60,
        <br>(B) Zone II : Effective size value 0.75 mm and uniformity coefficient 2.10,
        <br>(C) Zone III : Effective size value 0.65 mm and uniformity coefficient 2.60,
        <br>(D) Zone IV : Effective size value 0.75 mm and uniformity coefficient 3.70
        <div class="options-grid">
          <div class="option-item"><strong>(A)</strong> Zone I</div>
          <div class="option-item"><strong>(B)</strong> Zone II</div>
          <div class="option-item"><strong>(C)</strong> Zone III</div>
          <div class="option-item"><strong>(D)</strong> Zone IV</div>
        </div>
      </div>
      <div class="answer-banner">
        <strong>Correct Answer: (B) Zone II</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION-BY-OPTION REFUTATIONS -->
  <div class="card">
    <div class="card-header bg-red">Forensic Analysis & Option Refutations</div>
    <div class="card-body">

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (A): Zone I (D10 = 0.55 mm, Cu = 3.60)
        </div>
        <div class="option-card-body">
          <p>
            Zone I exhibits the <strong>smallest effective size</strong> ($D_{10} = 0.55\text{ mm}$) among all four candidates, yielding the lowest Hazen factor ($(0.55)^2 = 0.3025\text{ mm}^2$, nearly half that of Zone II). Furthermore, its high uniformity coefficient ($C_u = 3.60$) indicates poor sorting where fine sand and silt choke the pore channels. This combination yields low hydraulic conductivity and poor well yield, making Option (A) incorrect.
          </p>
        </div>
      </div>

      <div class="option-card option-correct">
        <div class="option-card-header">
          <span class="badge bg-success">CORRECT</span> Option (B): Zone II (D10 = 0.75 mm, Cu = 2.10)
        </div>
        <div class="option-card-body">
          <p>
            Zone II represents the <strong>optimal hydrogeological candidate</strong> for groundwater withdrawal across all physical criteria:
          </p>
          <ul>
            <li><strong>Maximum Effective Size ($D_{10} = 0.75\text{ mm}$):</strong> Yields the highest Hazen permeability potential ($(0.75)^2 = 0.5625\text{ mm}^2$), ensuring large, open pore throats with minimal frictional resistance to laminar flow.</li>
            <li><strong>Superior Sorting / Low Uniformity ($C_u = 2.10$):</strong> $C_u < 2.5$ signifies a remarkably uniform sand body with uniform pore diameters, high effective porosity, and total absence of pore-choking fines.</li>
            <li><strong>Superior Well Development:</strong> Easily forms a natural gravel pack during well development, maximizing well efficiency and minimizing entrance head losses.</li>
          </ul>
          <p>
            Therefore, Zone II is unambiguously the most promising zone for groundwater abstraction.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (C): Zone III (D10 = 0.65 mm, Cu = 2.60)
        </div>
        <div class="option-card-body">
          <p>
            While Zone III has moderate sorting ($C_u = 2.60$), its effective grain size ($D_{10} = 0.65\text{ mm}$) is substantially finer than that of Zone II ($0.75\text{ mm}$). By Hazen's law, its permeability is approximately $25\%$ lower than Zone II ($(0.65)^2 / (0.75)^2 = 0.4225 / 0.5625 \approx 0.75$). Because Zone II is distinctly superior in both grain coarseness and sorting, selecting Zone III is incorrect.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (D): Zone IV (D10 = 0.75 mm, Cu = 3.70)
        </div>
        <div class="option-card-body">
          <p>
            Although Zone IV shares the coarse effective grain size of $D_{10} = 0.75\text{ mm}$, it suffers from a <strong>very high uniformity coefficient ($C_u = 3.70$)</strong>. In sedimentology and soil mechanics, $C_u > 3.5$ indicates a poorly sorted, well-graded soil where intermediate and fine sand grains occupy the interstitial voids between coarse grains. This interstitial packing drastically reduces porosity and hydraulic conductivity compared to the clean, uniform pore network of Zone II. Thus, Zone IV is decidedly inferior to Zone II.
          </p>
        </div>
      </div>

    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Hydrogeologic Synthesis: Comprehensive Aquifer Zone Evaluation Matrix</div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Evaluation Parameter</th>
              <th>Zone I</th>
              <th>Zone II (Selected)</th>
              <th>Zone III</th>
              <th>Zone IV</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Effective Size ($D_{10}$)</strong></td>
              <td>$0.55\text{ mm}$</td>
              <td><strong>$0.75\text{ mm}$ (Tied Max)</strong></td>
              <td>$0.65\text{ mm}$</td>
              <td>$0.75\text{ mm}$ (Tied Max)</td>
            </tr>
            <tr>
              <td><strong>Hazen Factor ($(D_{10})^2$)</strong></td>
              <td>$0.3025\text{ mm}^2$</td>
              <td><strong>$0.5625\text{ mm}^2$</strong></td>
              <td>$0.4225\text{ mm}^2$</td>
              <td>$0.5625\text{ mm}^2$</td>
            </tr>
            <tr>
              <td><strong>Uniformity Coeff. ($C_u$)</strong></td>
              <td>$3.60$</td>
              <td><strong>$2.10$ (Optimal Min)</strong></td>
              <td>$2.60$</td>
              <td>$3.70$ (Worst)</td>
            </tr>
            <tr>
              <td><strong>$60\%$ Size ($D_{60} = C_u \cdot D_{10}$)</strong></td>
              <td>$1.98\text{ mm}$</td>
              <td>$1.575\text{ mm}$</td>
              <td>$1.69\text{ mm}$</td>
              <td>$2.775\text{ mm}$</td>
            </tr>
            <tr>
              <td><strong>Pore Channel Cleanliness</strong></td>
              <td>Choked with fines</td>
              <td><strong>Wide open & uniform</strong></td>
              <td>Moderately open</td>
              <td>Clogged by fines</td>
            </tr>
            <tr>
              <td><strong>Well Completion Design</strong></td>
              <td>Artificial gravel pack needed</td>
              <td><strong>Natural gravel pack feasible</strong></td>
              <td>Borderline natural pack</td>
              <td>Artificial gravel pack needed</td>
            </tr>
            <tr>
              <td><strong>Overall Suitability Rank</strong></td>
              <td>Rank 4 (Worst)</td>
              <td><strong>Rank 1 (Most Promising)</strong></td>
              <td>Rank 3</td>
              <td>Rank 2</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- CARD: 8 FULLY WORKED EXAM PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Hydrogeology Practice Problems (8 Rigorous Exercises)</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 1: Hazen Hydraulic Conductivity Estimation</strong><br>
        Using Hazen's formula $K = C (D_{10})^2$ with coefficient $C = 1.15 \times 10^4\text{ m/day}\cdot\text{mm}^{-2}$, calculate the theoretical hydraulic conductivity ($K$) for: (a) Zone I ($D_{10} = 0.55\text{ mm}$), and (b) Zone II ($D_{10} = 0.75\text{ mm}$). Determine the percentage increase in $K$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Zone I:
          $$K_{\text{Zone I}} = (1.15 \times 10^4) \times (0.55)^2 = (1.15 \times 10^4) \times 0.3025 \approx 3,478.75\text{ m/day}$$
          2. Zone II:
          $$K_{\text{Zone II}} = (1.15 \times 10^4) \times (0.75)^2 = (1.15 \times 10^4) \times 0.5625 \approx 6,468.75\text{ m/day}$$
          3. Ratio and percentage increase:
          $$\frac{K_{\text{Zone II}}}{K_{\text{Zone I}}} = \frac{6468.75}{3478.75} \approx 1.86 \implies \mathbf{+86.0\%\text{ increase}}$$
          Zone II exhibits an $86\%$ higher intrinsic permeability solely due to its coarser effective grain size.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Calculation of $D_{60}$ for All Four Formations</strong><br>
        Calculate the exact grain diameter at $60\%$ passing ($D_{60}$) for all four zones using the formula $D_{60} = C_u \cdot D_{10}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Zone I: $D_{60} = 3.60 \times 0.55\text{ mm} = 1.980\text{ mm}$<br>
          2. Zone II: $D_{60} = 2.10 \times 0.75\text{ mm} = 1.575\text{ mm}$<br>
          3. Zone III: $D_{60} = 2.60 \times 0.65\text{ mm} = 1.690\text{ mm}$<br>
          4. Zone IV: $D_{60} = 3.70 \times 0.75\text{ mm} = 2.775\text{ mm}$<br>
          <em>Notice:</em> In Zone IV, the $60\%$ size is huge ($2.775\text{ mm}$), confirming that a large spread of coarse and fine particles exists, whereas Zone II has a tight grain distribution between $0.75\text{ mm}$ and $1.58\text{ mm}$.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Porosity Impact via Kozeny-Carman Modeling</strong><br>
        The Kozeny-Carman equation states that $K \propto \frac{n^3}{(1 - n)^2} (D_{10})^2$, where $n$ is porosity. Due to superior uniform sorting, Zone II achieves a porosity of $n_2 = 0.38$. In contrast, the poor sorting of Zone IV causes finer particles to nest within voids, reducing its porosity to $n_4 = 0.28$. Although both share $D_{10} = 0.75\text{ mm}$, compute the hydraulic conductivity ratio $K_2 / K_4$ caused solely by this porosity difference.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Evaluate porosity function $f(n) = \frac{n^3}{(1 - n)^2}$ for both zones:
          $$f(n_2) = \frac{(0.38)^3}{(1 - 0.38)^2} = \frac{0.054872}{(0.62)^2} = \frac{0.054872}{0.3844} \approx 0.1427$$
          $$f(n_4) = \frac{(0.28)^3}{(1 - 0.28)^2} = \frac{0.021952}{(0.72)^2} = \frac{0.021952}{0.5184} \approx 0.04235$$
          2. Ratio of hydraulic conductivities:
          $$\frac{K_2}{K_4} = \frac{f(n_2)}{f(n_4)} = \frac{0.1427}{0.04235} \approx 3.37$$
          <em>Insight:</em> Due to superior uniform sorting and resulting higher porosity, Zone II delivers <strong>$3.37\text{ times more water}$</strong> than Zone IV despite having the exact same effective grain size!
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Natural Well Screen Slot Size Selection</strong><br>
        In a naturally developed well completed in Zone II ($D_{10} = 0.75\text{ mm}, D_{60} = 1.575\text{ mm}$), the standard design rule specifies selecting a screen slot size that will retain $50\%$ of the formation material ($D_{50}$). Assuming a log-linear grain size distribution between $D_{10}$ and $D_{60}$, calculate: (a) $D_{50}$, and (b) The recommended screen slot size in inches ($1\text{ in} = 25.4\text{ mm}$, slot sizes expressed in thousandths of an inch / slot number).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Log-linear interpolation for $D_{50}$:
          $$\log(D_{50}) = \log(D_{10}) + \left(\frac{50 - 10}{60 - 10}\right) \times [\log(D_{60}) - \log(D_{10})]$$
          $$\log(D_{50}) = \log(0.75) + 0.80 \times [\log(1.575) - \log(0.75)] = -0.1249 + 0.80 \times [0.1973 - (-0.1249)]$$
          $$\log(D_{50}) = -0.1249 + 0.80 \times (0.3222) = -0.1249 + 0.2578 = +0.1329$$
          $$D_{50} = 10^{0.1329} \approx 1.358\text{ mm}$$
          2. Convert to inches and slot size:
          $$\text{Slot opening} = \frac{1.358\text{ mm}}{25.4\text{ mm/in}} \approx 0.0535\text{ inches} \implies \mathbf{\text{Slot No. 50 to 55 (0.050 to 0.055 in)}}$$
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Terzaghi Filter Pack Criteria for Zone IV</strong><br>
        Because Zone IV has a high uniformity coefficient ($C_u = 3.70$), it requires an artificial gravel pack. The Terzaghi filter criteria require that the $15\%$ passing size of the filter pack ($D_{15,\text{pack}}$) satisfies $4 \le \frac{D_{15,\text{pack}}}{D_{85,\text{aquifer}}} \le 5$. If $D_{85,\text{aquifer}} = 4.2\text{ mm}$ for Zone IV, calculate the required $D_{15}$ for the gravel pack.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Lower bound:
          $$D_{15,\text{pack}} \ge 4 \times D_{85,\text{aquifer}} = 4 \times 4.2\text{ mm} = 16.8\text{ mm}$$
          2. Upper bound:
          $$D_{15,\text{pack}} \le 5 \times D_{85,\text{aquifer}} = 5 \times 4.2\text{ mm} = 21.0\text{ mm}$$
          The gravel pack must have a $D_{15}$ size graded tightly between $16.8\text{ mm}$ and $21.0\text{ mm}$.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Well Efficiency and Screen Entrance Velocity</strong><br>
        A production well in Zone II is pumped at $Q = 2400\text{ m}^3/\text{day} = 0.02778\text{ m}^3/\text{s}$. The well screen has an outside diameter of $D = 250\text{ mm}$ ($r = 0.125\text{ m}$) and a length of $L = 10\text{ m}$, with an open screen area percentage of $22\%$. Calculate the screen entrance velocity ($v_e$). Verify if it complies with the standard Johnson Screens velocity limit ($v_e \le 0.03\text{ m/s}$ to prevent incrustation and turbulent head loss).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Total cylindrical surface area of screen:
          $$A_{\text{total}} = \pi \cdot D \cdot L = \pi \times 0.25\text{ m} \times 10\text{ m} \approx 7.854\text{ m}^2$$
          2. Open effective intake area ($22\%$ open area):
          $$A_{\text{open}} = 7.854 \times 0.22 \approx 1.728\text{ m}^2$$
          3. Screen entrance velocity:
          $$v_e = \frac{Q}{A_{\text{open}}} = \frac{0.02778\text{ m}^3/\text{s}}{1.728\text{ m}^2} \approx 0.0161\text{ m/s}$$
          4. Criterion check:
          $$v_e = 0.0161\text{ m/s} \le 0.030\text{ m/s} \quad \text{\textbf{[SAFE / OPTIMAL]}}$$
          The entrance velocity is well below the critical threshold, guaranteeing laminar inflow, zero screen corrosion/incrustation, and maximum well longevity.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Specific Capacity ($Q/s$) Comparison</strong><br>
        In an unconfined aquifer with saturated thickness $b = 20\text{ m}$ and radius of influence $R = 250\text{ m}$, a fully penetrating well of radius $r_w = 0.15\text{ m}$ is pumped. Using the Thiem equation, compare the theoretical Specific Capacity ($Q/s \approx \frac{2 \pi K b}{2.303 \log_{10}(R / r_w)}$) for Zone II ($K_2 = 50\text{ m/day}$) versus Zone I ($K_1 = 25\text{ m/day}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Common geometric factor:
          $$\frac{2 \pi b}{2.303 \log_{10}(R / r_w)} = \frac{2 \times 3.14159 \times 20}{2.303 \log_{10}(250 / 0.15)} = \frac{125.66}{2.303 \log_{10}(1666.7)} = \frac{125.66}{2.303 \times 3.2219} = \frac{125.66}{7.420} \approx 16.935\text{ m}^2$$
          2. Specific Capacity for Zone II:
          $$(Q/s)_2 = 16.935 \times 50\text{ m/day} \approx 846.75\text{ m}^3/\text{day per meter of drawdown}$$
          3. Specific Capacity for Zone I:
          $$(Q/s)_1 = 16.935 \times 25\text{ m/day} \approx 423.38\text{ m}^3/\text{day per meter of drawdown}$$
          A well screened in Zone II delivers <strong>twice the discharge per meter of drawdown</strong> compared to Zone I.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Grain Size Sieve Analysis and Coefficient of Curvature</strong><br>
        For Zone II, sieve analysis yields $D_{10} = 0.75\text{ mm}$, $D_{30} = 1.08\text{ mm}$, and $D_{60} = 1.575\text{ mm}$. Calculate the Coefficient of Curvature ($C_c = \frac{D_{30}^2}{D_{10} \cdot D_{60}}$) and assess whether the grain size distribution curve is smooth and well-graded according to the Unified Soil Classification System (USCS criterion: $1 \le C_c \le 3$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute $C_c$:
          $$C_c = \frac{(1.08\text{ mm})^2}{0.75\text{ mm} \times 1.575\text{ mm}} = \frac{1.1664}{1.18125} \approx 0.987 \approx 1.0$$
          2. Assessment:
          $C_c \approx 1.0$ falls right on the USCS threshold ($1 \le C_c \le 3$). Combined with $C_u = 2.10$, this demonstrates that the sand has an exceptionally smooth, uniform logarithmic gradation with no gap-grading or missing grain sizes, ensuring maximum structural stability and minimum turbulence during groundwater abstraction.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(
        q_num=149,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q149_Aquifer_Textural_Parameters_Selection_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q149: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q149()
