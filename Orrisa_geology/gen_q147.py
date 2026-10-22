#!/usr/bin/env python3
"""
Q147 Generator: Cooper-Jacob Method Validity Limits (u <= 0.05 Criterion)
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q147():
    title = r"Q147: Hydrogeology: Cooper-Jacob Method Validity Limits | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Hydrogeology & Well Hydraulics"
    h1_title = r"Q147: Cooper-Jacob Straight-Line Method: Mathematical Limits of Validity ($u \le 0.05$)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 147<br>
<strong>Authoritative References:</strong> Hilton H. Cooper and C.E. Jacob, <em>A Generalized Graphical Method for Evaluating Formation Constants and Summarizing Well-Field History</em> (Trans. AGU, 1946, Vol. 27, pp. 526–534); David K. Todd and Larry W. Mays, <em>Groundwater Hydrology</em> (3rd Ed., Wiley, Ch. 4: Well Hydraulics, pp. 140–152); C.W. Fetter, <em>Applied Hydrogeology</em> (4th Ed., Prentice Hall, Ch. 5, pp. 170–182); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 3: Hydrogeology, p. 34)."""

    part1 = r"""
  <!-- CARD 1: THEIS EQUATION AND TAYLOR TRUNCATION -->
  <div class="card">
    <div class="card-header bg-blue">1. Theis Well Function & The Cooper-Jacob Semilog Simplification</div>
    <div class="card-body">
      <p>
        In 1935, <strong>Charles V. Theis</strong> derived the exact non-equilibrium equation for transient radial groundwater flow to a pumping well in a confined, homogeneous, isotropic aquifer:
      </p>
      <div class="math-block">
        $$s = \frac{Q}{4 \pi T} W(u)$$
        $$\text{where } u = \frac{r^2 S}{4 T t}$$
      </div>
      <p>
        Here, $s$ is drawdown, $Q$ is constant pumping discharge, $T$ is aquifer transmissivity, $S$ is storativity, $r$ is radial distance to the observation well, $t$ is elapsed pumping time, and $W(u)$ is the exponential integral (the <strong>Theis Well Function</strong>), expandable as an infinite convergent Taylor-Maclaurin series:
      </p>
      <div class="math-block">
        $$W(u) = -0.57721566 - \ln(u) + u - \frac{u^2}{2 \cdot 2!} + \frac{u^3}{3 \cdot 3!} - \frac{u^4}{4 \cdot 4!} + \dots$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q147/cooper_jacob_validity_condition_theis_comparison.png" alt="Cooper Jacob Validity Condition Theis Comparison">
        <div class="figure-caption">
          <strong>Figure 147.1 — Theis Type Curve vs Cooper-Jacob Straight-Line Approximation:</strong> Comparison of exact Theis $W(u)$ against Cooper-Jacob semilog straight line. For small $u \le 0.05$ (large $t$ or small $r$), the two models merge seamlessly (error $< 2\%$). For large $u > 0.05$ (short test duration or distant piezometer), the Cooper-Jacob line diverges severely into non-linear deviation.
        </div>
      </div>

      <h4>The Cooper-Jacob Straight-Line Formula (1946)</h4>
      <p>
        In 1946, <strong>Hilton H. Cooper and C.E. Jacob</strong> noted that when the dimensionless argument $u$ is sufficiently small ($u \le 0.05$ or $u \le 0.01$), all higher-order polynomial terms in the expansion ($u - u^2/4 + \dots$) become negligibly small and can be dropped without significant loss of accuracy:
      </p>
      <div class="math-block">
        $$W(u) \approx -\ln(u) - 0.5772 = \ln\left(\frac{1}{u}\right) - \ln(1.781) = \ln\left(\frac{1}{1.781 u}\right) = \ln\left(\frac{0.5615}{u}\right) = \ln\left(\frac{2.25}{4 u}\right)$$
        $$W(u) \approx \ln\left(\frac{2.25 T t}{r^2 S}\right) = 2.303 \log_{10}\left(\frac{2.25 T t}{r^2 S}\right)$$
      </div>
      <p>
        Substituting this into the drawdown equation gives the <strong>Cooper-Jacob Semilog Equation</strong>:
      </p>
      <div class="math-block" style="font-size: 1.25rem; font-weight: bold; background: #eff6ff; border-left: 5px solid #2563eb; padding: 12px;">
        $$s = \frac{2.303 Q}{4 \pi T} \log_{10}\left(\frac{2.25 T t}{r^2 S}\right)$$
      </div>
      <p>
        Plotting drawdown $s$ on an arithmetic scale against elapsed time $t$ on a logarithmic scale yields a straight line with slope $\Delta s$ (drawdown per log cycle of time):
      </p>
      <div class="math-block">
        $$T = \frac{2.303 Q}{4 \pi \Delta s} \quad \text{and} \quad S = \frac{2.25 T t_0}{r^2}$$
      </div>
    </div>
  </div>

  <!-- CARD 2: MATHEMATICAL BREAKDOWN & CRITICAL INVALIDITY CONDITIONS -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Critical Invalidity Criterion ($u > 0.05$): When Cooper-Jacob CANNOT Be Used</div>
    <div class="card-body">
      <div class="figure-box">
        <img src="../../figures_Q147/bangar_p34_cooper_jacob_method_conditions.png" alt="Bangar Textbook Hydrogeology Cooper Jacob Conditions Scan">
        <div class="figure-caption">
          <strong>Figure 147.2 — Facsimile from K.M. Bangar (Principles of Engineering Geology, Ch. 3, p. 34):</strong> Derivation of the Cooper-Jacob modification, explicit definition of the dimensionless variable $u$, and the mathematical threshold condition $u < 0.05$ restricting valid semilog graphical analysis.
        </div>
      </div>

      <h4>The Fundamental Limit of Validity</h4>
      <p>
        The Cooper-Jacob straight-line approximation is mathematically valid <strong>if and only if</strong>:
      </p>
      <div class="math-block" style="font-size: 1.2rem; font-weight: bold; background: #ecfdf5; border-left: 5px solid #059669; padding: 12px;">
        $$u = \frac{r^2 S}{4 T t} \le 0.05 \quad (\text{or } u \le 0.01 \text{ for } < 1\% \text{ error})$$
      </div>
      <p>
        Conversely, the Cooper-Jacob method <strong>CANNOT BE USED</strong> whenever:
      </p>
      <div class="math-block" style="font-size: 1.2rem; font-weight: bold; background: #fef2f2; border-left: 5px solid #dc2626; padding: 12px;">
        $$u = \frac{r^2 S}{4 T t} > 0.05$$
      </div>

      <h4>Deconstruction of the Inequality</h4>
      <p>
        Examining the algebraic structure of the fraction $u = \frac{r^2 S}{4 T t}$ reveals exactly what physical test conditions cause $u$ to exceed $0.05$:
      </p>
      <ol>
        <li><strong>Condition (i) — When the pump test is of SHORT duration ($t$ is small):</strong><br>
          Because elapsed pumping time $t$ resides in the <em>denominator</em>, when $t$ is small (during early test stages or short-duration pumping), the quotient $\frac{r^2 S}{4 T t}$ becomes large ($u \gg 0.05$). The higher-order terms in the series cannot be neglected, the semilog plot is non-linear and curved, and applying Cooper-Jacob results in catastrophic errors. <strong>(Method cannot be used!)</strong>
        </li>
        <li><strong>Condition (iii) — When the observation well is situated FAR AWAY from the main well ($r$ is large):</strong><br>
          Because radial distance $r$ resides in the <em>numerator as a squared term ($r^2$)</em>, any increase in $r$ dramatically magnifies $u$. For a distant piezometer, the cone of depression has not sufficiently developed, making $u \gg 0.05$ throughout most or all of the test. <strong>(Method cannot be used!)</strong>
        </li>
      </ol>

      <h4>Why Conditions (ii) and (iv) FAVOR the Cooper-Jacob Method</h4>
      <ul>
        <li><strong>Condition (ii) — When the pump test is of LONG duration ($t$ is large):</strong> As $t \to \infty$, the denominator grows enormous, driving $u \to 0$ ($u \ll 0.01$). This makes Cooper-Jacob <em>maximally accurate and fully valid</em>!</li>
        <li><strong>Condition (iv) — When the observation well is situated NEAR to the main well ($r$ is small):</strong> A small radial distance $r$ minimizes the $r^2$ numerator, ensuring that $u \le 0.01$ is achieved almost immediately after pumping begins. This makes Cooper-Jacob <em>ideally suited</em>.</li>
      </ul>
      <div class="definition-box">
        <strong>Definitive Exam Conclusion:</strong><br>
        The Cooper-Jacob method <strong>CANNOT</strong> be used under <strong>(i) short duration</strong> and <strong>(iii) distant observation well</strong>, because both conditions force $u = \frac{r^2 S}{4 T t} > 0.05$.
      </div>
    </div>
  </div>

  <!-- CARD 3: NUMERICAL TRUNCATION ERROR TABLE -->
  <div class="card">
    <div class="card-header bg-indigo">3. Quantitative Error Progression as a Function of $u$</div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Dimensionless Variable $u$</th>
              <th>Exact Theis $W(u)$</th>
              <th>Cooper-Jacob Approximation $\ln(2.25 / u)$</th>
              <th>Truncation Error (%)</th>
              <th>Applicability Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>$0.001$</td>
              <td>$6.3315$</td>
              <td>$6.3324$</td>
              <td>$+0.01\%$</td>
              <td><span class="badge bg-success">Perfect</span></td>
            </tr>
            <tr>
              <td>$0.010$</td>
              <td>$4.0379$</td>
              <td>$4.0395$</td>
              <td>$+0.04\%$</td>
              <td><span class="badge bg-success">Excellent ($< 1\%$ error)</span></td>
            </tr>
            <tr>
              <td>$0.050$</td>
              <td>$2.4679$</td>
              <td>$2.5157$</td>
              <td>$+1.94\%$</td>
              <td><span class="badge bg-primary">Standard Cutoff Limit ($< 2\%$ error)</span></td>
            </tr>
            <tr>
              <td>$0.100$</td>
              <td>$1.8229$</td>
              <td>$1.9363$</td>
              <td>$+6.22\%$</td>
              <td><span class="badge bg-warning">Marginal (Error $> 5\%$)</span></td>
            </tr>
            <tr>
              <td>$0.200$</td>
              <td>$1.2227$</td>
              <td>$1.3787$</td>
              <td>$+12.76\%$</td>
              <td><span class="badge bg-danger">INVALID (Error $> 12\%$)</span></td>
            </tr>
            <tr>
              <td>$0.500$</td>
              <td>$0.5598$</td>
              <td>$0.7675$</td>
              <td>$+37.10\%$</td>
              <td><span class="badge bg-danger">FATALLY INVALID (Error $> 37\%$)</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-amber">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-box">
        <strong>Question 147:</strong> Conditions under which Jacob-Cooper method cannot be used for analysis of pump test data :
        <br>(i) When the pump test is of short duration,
        <br>(ii) When the pump test is of long duration,
        <br>(iii) When the observation well is situated far away from the main well,
        <br>(iv) When the observation well is situated nearer to the main well.
        <br>Choose the correct set of answer from the following :
        <div class="options-grid">
          <div class="option-item"><strong>(A)</strong> (i) and (iii)</div>
          <div class="option-item"><strong>(B)</strong> (ii) and (iii)</div>
          <div class="option-item"><strong>(C)</strong> (ii) and (iv)</div>
          <div class="option-item"><strong>(D)</strong> (i) and (iv)</div>
        </div>
      </div>
      <div class="answer-banner">
        <strong>Correct Answer: (A) (i) and (iii)</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION-BY-OPTION REFUTATIONS -->
  <div class="card">
    <div class="card-header bg-red">Forensic Analysis & Option Refutations</div>
    <div class="card-body">

      <div class="option-card option-correct">
        <div class="option-card-header">
          <span class="badge bg-success">CORRECT</span> Option (A): (i) and (iii)
        </div>
        <div class="option-card-body">
          <p>
            Option (A) combines the exact two physical conditions that violate the mathematical validity criterion of the Cooper-Jacob semilog method ($u = \frac{r^2 S}{4 T t} \le 0.05$):
          </p>
          <ul>
            <li><strong>Condition (i) — Short Duration ($t$ small):</strong> When the pump test has run for only a brief period, $t$ is small, causing the denominator $4 T t$ to be small, driving $u > 0.05$. The drawdown curve on semilog paper is strongly concave and has not yet straightened.</li>
            <li><strong>Condition (iii) — Distant Observation Well ($r$ large):</strong> Because distance enters as $r^2$, locating the piezometer far away magnifies the numerator enormously, forcing $u > 0.05$. For distant wells, hours or days of pumping are needed before the straight-line approximation becomes valid.</li>
          </ul>
          <p>
            Because both (i) and (iii) invalidate the straight-line assumption, Option (A) is the indisputably correct answer.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (B): (ii) and (iii)
        </div>
        <div class="option-card-body">
          <p>
            Option (B) includes Condition (ii) ("When the pump test is of long duration"). Long duration means $t$ is large, which drives $u = \frac{r^2 S}{4 T t} \to 0$ ($u \ll 0.01$). This is precisely the operational condition under which the Cooper-Jacob method is <strong>most reliable, accurate, and recommended</strong>! Because Condition (ii) is a condition of validity rather than invalidity, Option (B) is incorrect.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (C): (ii) and (iv)
        </div>
        <div class="option-card-body">
          <p>
            Option (C) pairs Condition (ii) (long duration) with Condition (iv) (observation well situated near to the main well). This represents the <strong>gold standard, ideal operational domain</strong> for applying the Cooper-Jacob method: small $r$ minimizes the numerator while large $t$ maximizes the denominator, producing $u < 0.001$ where truncation error is less than $0.01\%$. Claiming the method cannot be used under these conditions is completely contrary to hydrogeologic science.
          </p>
        </div>
      </div>

      <div class="option-card option-wrong">
        <div class="option-card-header">
          <span class="badge bg-danger">INCORRECT</span> Option (D): (i) and (iv)
        </div>
        <div class="option-card-body">
          <p>
            While Condition (i) is an invalidating condition, Condition (iv) ("When the observation well is situated nearer to the main well") dramatically assists validity because a small $r$ keeps $r^2$ small, helping $u$ drop below $0.05$ very rapidly. Therefore, Condition (iv) is not a condition under which the method cannot be used, refuting Option (D).
          </p>
        </div>
      </div>

    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Hydrogeologic Synthesis: Pumping Test Analytical Methods Comparison</div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-bordered table-striped text-center">
          <thead class="table-dark">
            <tr>
              <th>Analytical Method</th>
              <th>Mathematical Formulation</th>
              <th>Plot Coordinates</th>
              <th>Validity Limits / Constraints</th>
              <th>Best Field Domain</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Theis Type Curve (1935)</strong></td>
              <td>$$s = \frac{Q}{4 \pi T} W(u)$$</td>
              <td>$\log s$ vs $\log(t / r^2)$</td>
              <td><strong>Universal:</strong> Valid for all values of $u$ ($0 < u < \infty$); requires curve superposition.</td>
              <td>Short-duration tests, early pumping data, and distant observation wells ($u > 0.05$).</td>
            </tr>
            <tr>
              <td><strong>Cooper-Jacob Semilog (1946)</strong></td>
              <td>$$s = \frac{2.303 Q}{4 \pi T} \log_{10}\left(\frac{2.25 T t}{r^2 S}\right)$$</td>
              <td>$s$ vs $\log t$ or $s$ vs $\log r$</td>
              <td><strong>Restricted:</strong> Valid ONLY when $u \le 0.05$ (fails when $t$ is small or $r$ is large).</td>
              <td>Late-time pumping data ($t > t_{\min}$), near observation wells, and single-well production tests.</td>
            </tr>
            <tr>
              <td><strong>Chow Method (1952)</strong></td>
              <td>$$F(u) = \frac{s}{\Delta s}, \quad W(u) = 4 \pi \frac{s \cdot T}{Q}$$</td>
              <td>$s$ vs $\log t$ nomograph</td>
              <td>Valid for all $u$, but avoids curve matching by calculating slope $F(u)$ at any chosen point.</td>
              <td>Quick parameter estimation without requiring full Theis curve overlay sheets.</td>
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
        <strong>Problem 1: Minimum Time ($t_{\min}$) Calculation for Cooper-Jacob Validity</strong><br>
        A pumping test is conducted in a confined aquifer with Transmissivity $T = 360\text{ m}^2/\text{day}$ and Storativity $S = 2.0 \times 10^{-4}$. An observation well is located at distance $r = 60\text{ m}$ from the pumping well. Calculate the minimum elapsed pumping time ($t_{\min}$) in minutes after which the Cooper-Jacob method can be legitimately applied under the standard criterion $u \le 0.05$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Validity threshold formula:
          $$u = \frac{r^2 S}{4 T t} \le 0.05 \implies t \ge \frac{r^2 S}{4 T \times 0.05} = \frac{r^2 S}{0.20 T} = \frac{5 r^2 S}{T}$$
          2. Substitute given values:
          $$t_{\min} = \frac{5 \times (60\text{ m})^2 \times (2.0 \times 10^{-4})}{360\text{ m}^2/\text{day}} = \frac{5 \times 3600 \times (2.0 \times 10^{-4})}{360} = \frac{3.6}{360} = 0.010\text{ days}$$
          3. Convert to minutes:
          $$t_{\min} = 0.010\text{ days} \times 1440\text{ min/day} = 14.4\text{ minutes}$$
          <em>Conclusion:</em> For the first $14.4\text{ minutes}$ of pumping, $u > 0.05$ and Cooper-Jacob CANNOT be used. Only time-drawdown data collected after $t \ge 14.4\text{ min}$ may be fitted to the straight line.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Maximum Distance ($r_{\max}$) for Short Pumping Duration</strong><br>
        Due to mechanical failure, a pump test must be terminated after only $t = 30\text{ minutes} = 0.02083\text{ days}$. The aquifer has $T = 500\text{ m}^2/\text{day}$ and $S = 1.5 \times 10^{-4}$. Calculate the maximum radial distance ($r_{\max}$) of an observation well that can be analyzed using the Cooper-Jacob method ($u \le 0.05$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Rearrange $u \le 0.05$ for radial distance $r$:
          $$r^2 \le \frac{0.05 \times 4 T t}{S} = \frac{0.20 T t}{S}$$
          $$r_{\max} = \sqrt{\frac{0.20 \times 500\text{ m}^2/\text{day} \times 0.02083\text{ days}}{1.5 \times 10^{-4}}} = \sqrt{\frac{2.083}{1.5 \times 10^{-4}}} = \sqrt{13,886.7} \approx 117.8\text{ meters}$$
          Any observation well located beyond $118\text{ meters}$ has $u > 0.05$ and cannot be interpreted via the Cooper-Jacob method for this short test.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Numerical Error Analysis at $u = 0.20$</strong><br>
        A hydrogeologist uses the Cooper-Jacob equation to estimate drawdown at a point where $u = 0.20$. Exact Theis well function is $W(0.20) = 1.2227$. (a) Calculate the Cooper-Jacob approximation $W_{\text{CJ}} = \ln(2.25 / 0.20)$. (b) Determine the percentage overestimation error.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Cooper-Jacob approximation:
          $$W_{\text{CJ}} = \ln\left(\frac{2.25}{0.20}\right) = \ln(11.25) \approx 2.4204 - 0.5772 = 1.3787$$
          2. Error calculation:
          $$\text{Absolute Error} = 1.3787 - 1.2227 = +0.1560$$
          $$\text{Percentage Error} = \left(\frac{0.1560}{1.2227}\right) \times 100\% \approx +12.76\%$$
          Using Cooper-Jacob when $u = 0.20$ overestimates drawdown by nearly $13\%$, leading to severe errors in calculated aquifer transmissivity.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Complete Cooper-Jacob Time-Drawdown Parameter Evaluation</strong><br>
        A well is pumped at $Q = 1800\text{ m}^3/\text{day}$. An observation well at $r = 40\text{ m}$ produces a semilog time-drawdown plot whose valid straight-line portion ($u \le 0.05$) yields a drawdown per log cycle of $\Delta s = 1.12\text{ m}$ and intersects the zero-drawdown axis at $t_0 = 1.8\text{ minutes} = 1.25 \times 10^{-3}\text{ days}$. Calculate: (a) Transmissivity ($T$), and (b) Storativity ($S$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Transmissivity:
          $$T = \frac{2.303 Q}{4 \pi \Delta s} = \frac{2.303 \times 1800}{4 \times 3.14159 \times 1.12} = \frac{4145.4}{14.074} \approx 294.54\text{ m}^2/\text{day}$$
          2. Storativity:
          $$S = \frac{2.25 T t_0}{r^2} = \frac{2.25 \times 294.54 \times (1.25 \times 10^{-3})}{40^2} = \frac{0.8284}{1600} \approx 5.18 \times 10^{-4}$$
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Verification of Data Points Excluded by $u \le 0.05$ Rule</strong><br>
        For the test in Problem 4 ($T = 294.54\text{ m}^2/\text{day}$, $S = 5.18 \times 10^{-4}$, $r = 40\text{ m}$), verify whether drawdown recorded at $t = 5\text{ minutes}$ ($0.00347\text{ days}$) can be included in the Cooper-Jacob straight line.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute $u$ at $t = 5\text{ minutes}$:
          $$u = \frac{r^2 S}{4 T t} = \frac{(40)^2 \times (5.18 \times 10^{-4})}{4 \times 294.54 \times 0.00347} = \frac{1600 \times (5.18 \times 10^{-4})}{4.088} = \frac{0.8288}{4.088} \approx 0.2027$$
          2. Evaluate criterion:
          $$u = 0.2027 > 0.05$$
          <em>Conclusion:</em> Because $u > 0.05$, the 5-minute data point <strong>MUST BE EXCLUDED</strong> from the straight line fit. The minimum valid time is $t_{\min} = \frac{5 r^2 S}{T} = \frac{5 \times 0.8288}{294.54} = 0.01407\text{ days} = 20.3\text{ minutes}$.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Delayed Drainage Plateau in Unconfined Aquifers</strong><br>
        Explain why the Cooper-Jacob straight line method fails in unconfined aquifers during intermediate pumping times ($10\text{ min} < t < 4\text{ hours}$), even though $t$ appears sufficiently large.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. The Cooper-Jacob method assumes strictly horizontal, 2-dimensional radial flow with constant storativity $S$.<br>
          2. In an unconfined aquifer during intermediate pumping times, <strong>delayed gravity drainage</strong> occurs as pore water drains vertically down from the descending capillary fringe.<br>
          3. This creates strong vertical flow components ($v_z \ne 0$) and a temporary flattening (plateau) in the drawdown curve where drawdown ceases to follow a logarithmic line.<br>
          4. Only after late time ($t > 4\text{ hours}$), when vertical gradients vanish and full specific yield ($S_y$) is mobilized, does a second, parallel Cooper-Jacob straight line emerge.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Impermeable Fault Boundary Slope Doubling</strong><br>
        During a Cooper-Jacob pumping test, the initial straight line slope is $\Delta s_1 = 0.80\text{ m}$. At $t = 120\text{ minutes}$, the cone of depression intersects a planar impermeable normal fault. (a) What will be the new slope $\Delta s_2$ of the semilog straight line at late time? (b) Explain the mathematical cause using image well theory.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. By Image Well Theory, an impermeable barrier boundary is mathematically equivalent to placing an imaginary discharge well pumping at identical rate $+Q$ located symmetrically across the fault barrier.<br>
          2. At late time, both real and image wells contribute equal drawdown to the observation well:
          $$s_{\text{total}} = s_{\text{real}} + s_{\text{image}} = \frac{2.303 Q}{4 \pi T} \log(t) + \frac{2.303 Q}{4 \pi T} \log(t) = \frac{2.303 (2Q)}{4 \pi T} \log(t)$$
          3. The slope exactly doubles:
          $$\Delta s_2 = 2 \times \Delta s_1 = 2 \times 0.80\text{ m} = 1.60\text{ meters per log cycle}$$
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Recharge Boundary Stabilization</strong><br>
        If the cone of depression intersects a fully penetrating perennial river instead of an impermeable fault, describe the behavior of the Cooper-Jacob semilog drawdown curve at late time.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. An open surface water body acts as a <strong>constant-head recharge boundary</strong> ($s = 0$ along the riverline).<br>
          2. By image well theory, this is modeled by an imaginary recharge well injecting water at rate $-Q$.<br>
          3. At late time, the recharge cancels all further expansion of the cone of depression. Drawdown stabilizes to a steady-state value ($ds/dt = 0$), and the slope of the semilog curve becomes <strong>zero (horizontal straight line)</strong>.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(
        q_num=147,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q147_Cooper_Jacob_Method_Validity_Conditions_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q147: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q147()
