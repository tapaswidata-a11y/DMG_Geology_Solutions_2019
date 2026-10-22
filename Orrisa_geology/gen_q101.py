#!/usr/bin/env python3
"""
Q101 Generator: Folk & Ward (1957) Graphic Kurtosis Mathematical Formulation
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q101():
    title = r"Q101: Sedimentology: Folk & Ward (1957) Graphic Kurtosis Mathematical Formulation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentology & Granulometry"
    h1_title = "Q101: Folk and Ward (1957) Graphic Kurtosis: Formula, Derivation & Verbal Scales"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 101<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 3: Grain Size, pp. 55–75; Fig. 3.4 / p. 75); Robert L. Folk and William C. Ward (1957), <em>Brazos River Bar: A Study in the Significance of Grain Size Parameters</em> (Journal of Sedimentary Petrology, Vol. 27, No. 1, pp. 3–26); R.L. Folk (1980), <em>Petrology of Sedimentary Rocks</em> (Hemphill Publishing Co.)."""

    part1 = r"""
  <!-- CARD 1: MATHEMATICAL FORMULATION AND DERIVATION OF GRAPHIC KURTOSIS -->
  <div class="card">
    <div class="card-header bg-blue">1. Folk and Ward (1957) Formulation of Graphic Kurtosis ($K_G$)</div>
    <div class="card-body">
      <p>
        In quantitative granulometry and statistical sedimentology (Folk & Ward, 1957; Boggs, 2014, p. 75), <strong>kurtosis</strong> (from the Greek $\kappa\upsilon\rho\tau\acute{o}\varsigma$, meaning "bulging" or "convex") measures the ratio between the sorting in the tails of a grain-size frequency curve and the sorting in the central body of the distribution.
      </p>
      <p>
        To quantify departure from a standard Gaussian normal bell curve, Robert L. Folk and William C. Ward (1957, p. 13) derived the <strong>Graphic Kurtosis ($K_G$)</strong> defined explicitly by the mathematical formula:
      </p>
      $$\mathbf{K_G = \frac{\phi_{95} - \phi_5}{2.44(\phi_{75} - \phi_{25})}}$$
      <p>
        where $\phi_5, \phi_{25}, \phi_{75}, \text{and } \phi_{95}$ represent the respective 5th, 25th, 75th, and 95th percentiles determined from the cumulative weight percentage frequency curve plotted on the Wentworth phi scale ($\phi = -\log_2 d_{\text{mm}}$).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q101/boggs_p75_folk_ward_graphic_kurtosis_formula.png" alt="Folk and Ward Graphic Size Parameters from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 101.1 — Folk and Ward (1957) Statistical Grain-Size Formulae and Kurtosis Scale:</strong> Authentic textbook table from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 75). Contains the exact mathematical definition of Graphic Kurtosis ($K_G$) and its verbal classification scale.
        </div>
      </div>

      <h4>Mathematical Derivation of the Constant $2.44$</h4>
      <p>
        The denominator coefficient $2.44$ is not an empirical arbitrary number, but a rigorously derived theoretical constant:
      </p>
      <ol>
        <li>For an idealized, perfectly normal Gaussian distribution:
          <ul>
            <li>The spread of the outer $90\%$ of the distribution ($\phi_{95} - \phi_5$) encompasses exactly $3.29$ standard deviations ($2 \times 1.6449\sigma \approx 3.2897\sigma$).</li>
            <li>The interquartile range ($\phi_{75} - \phi_{25}$) encompasses exactly $1.35$ standard deviations ($2 \times 0.6745\sigma \approx 1.3490\sigma$).</li>
          </ul>
        </li>
        <li>The ratio of these two percentile spreads in a standard normal curve is:
          $$\frac{\phi_{95} - \phi_5}{\phi_{75} - \phi_{25}} = \frac{3.2897\sigma}{1.3490\sigma} \approx 2.4386 \approx \mathbf{2.44}$$
        </li>
        <li>By dividing this ratio by $2.44$, Folk and Ward normalized the formula such that a perfectly normal Gaussian grain-size distribution yields:
          $$K_G = \frac{2.44}{2.44} = \mathbf{1.00}\quad (\text{Mesokurtic})$$
        </li>
      </ol>
    </div>
  </div>

  <!-- CARD 2: VERBAL SCALES & HYDRODYNAMIC SIGNIFICANCE -->
  <div class="card">
    <div class="card-header bg-emerald">2. Folk and Ward Verbal Kurtosis Scale & Hydrodynamic Mixing Models</div>
    <div class="card-body">
      <h4>Verbal Classification Scale for Graphic Kurtosis ($K_G$)</h4>
      <p>
        Folk and Ward (1957) and Folk (1980) established the standard verbal scale for interpreting calculated $K_G$ values:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>$K_G$ Range</th>
            <th>Verbal Classification</th>
            <th>Frequency Curve Geometry</th>
            <th>Hydrodynamic / Depositional Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$< 0.67$</strong></td>
            <td><strong>Very Platykurtic</strong></td>
            <td>Flat-topped, broad, bimodal saddle</td>
            <td>Equal mixing of two distinct sub-equal grain-size populations (e.g., gravel + sand).</td>
          </tr>
          <tr>
            <td><strong>$0.67\text{ to } 0.90$</strong></td>
            <td><strong>Platykurtic</strong></td>
            <td>Flat, broad central peak</td>
            <td>Sub-equal mixing of two populations; tails are better sorted than the center.</td>
          </tr>
          <tr>
            <td><strong>$0.90\text{ to } 1.11$</strong></td>
            <td><strong>Mesokurtic</strong></td>
            <td>Standard normal bell curve ($K_G \approx 1.0$)</td>
            <td>Unimodal sediment deposited under steady, unimodal hydrodynamic conditions.</td>
          </tr>
          <tr>
            <td><strong>$1.11\text{ to } 1.50$</strong></td>
            <td><strong>Leptokurtic</strong></td>
            <td>Excessively peaked, narrow central body</td>
            <td>Dominant unimodal population with a minor ($5\text{--}15\%$) subordinate tail of fine or coarse grains.</td>
          </tr>
          <tr>
            <td><strong>$1.50\text{ to } 3.00$</strong></td>
            <td><strong>Very Leptokurtic</strong></td>
            <td>Extremely sharp, narrow central spike</td>
            <td>Central $70\text{--}80\%$ is exceptionally well-sorted, with a tiny, poorly sorted tail.</td>
          </tr>
          <tr>
            <td><strong>$> 3.00$</strong></td>
            <td><strong>Extremely Leptokurtic</strong></td>
            <td>Hyper-peaked; needle-like central body</td>
            <td>Extreme unimodality with minute extraneous infiltration.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 101:</strong> Formulae and verbal scales for graphic size parameters are provided by Folk and Ward (1957). As per the relation, inclusive graphic kurtosis is calculated by which formula ?
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> KG = (phi95 - phi5) / [2.44 (phi75 - phi25)]</div>
        <div class="option-item"><strong>(B)</strong> KG = (phi95 - phi5) / [2.44 (phi75 - phi95)]</div>
        <div class="option-item"><strong>(C)</strong> KG = (phi95 - phi5) / [1.44 (phi5 - phi25)]</div>
        <div class="option-item"><strong>(D)</strong> Both (A) and (B) are correct</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) KG = (phi95 - phi5) / [2.44 (phi75 - phi25)]</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Canonical Formula</div>
        <p>
          <strong>Correct:</strong> By exact mathematical definition in Folk and Ward (1957, p. 13) and Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 75), the formula for <strong>Graphic Kurtosis ($K_G$)</strong> is:
          $$K_G = \frac{\phi_{95} - \phi_5}{2.44(\phi_{75} - \phi_{25})}$$
          The numerator $(\phi_{95} - \phi_5)$ measures the total spread of the distribution tails ($90\%$ of the sediment), while the denominator interquartile range $(\phi_{75} - \phi_{25})$ measures the spread of the central body ($50\%$ of the sediment), scaled by the normal curve constant $2.44$.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Erroneous Denominator Term</div>
        <p>
          <strong>Incorrect:</strong> The denominator in (B) contains the term $(\phi_{75} - \phi_{95})$. This is mathematically nonsensical: because phi percentiles increase monotonically ($\phi_5 < \phi_{25} < \phi_{75} < \phi_{95}$), subtracting a larger percentile ($\phi_{95}$) from a smaller percentile ($\phi_{75}$) yields a <strong>negative value</strong>, which would result in a negative kurtosis for all normal positive sediments. Furthermore, it completely omits the 25th percentile ($\phi_{25}$).
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Erroneous Constant & Subtraction Order</div>
        <p>
          <strong>Incorrect:</strong> Option (C) substitutes an incorrect constant ($1.44$ instead of $2.44$) and inverts the subtraction $(\phi_5 - \phi_{25})$, which also produces a negative spread. It bears no mathematical or historical validity in sedimentology.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Fallacious Dual Option</div>
        <p>
          <strong>Incorrect:</strong> Because Option (B) is mathematically and dimensionally erroneous, Option (D) is entirely invalid. The official answer key verified by the examination authorities unambiguously affirms <strong>(A)</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Summary of Folk and Ward (1957) Four Graphic Size Parameters</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Parameter Name</th>
            <th>Symbol</th>
            <th>Mathematical Formula</th>
            <th>Normal Gaussian Curve Value</th>
            <th>Verbal Classification Extremes</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Graphic Mean</strong></td>
            <td>$M_z$</td>
            <td>$$\frac{\phi_{16} + \phi_{50} + \phi_{84}}{3}$$</td>
            <td>Equals median ($\phi_{50}$)</td>
            <td>Fine ($> 4\phi$) to Coarse ($< -1\phi$)</td>
          </tr>
          <tr>
            <td><strong>Inclusive Graphic Standard Deviation</strong></td>
            <td>$\sigma_I$</td>
            <td>$$\frac{\phi_{84} - \phi_{16}}{4} + \frac{\phi_{95} - \phi_5}{6.6}$$</td>
            <td>$1.00\sigma$</td>
            <td>Very well sorted ($< 0.35\phi$) to Very poorly sorted ($> 2.0\phi$)</td>
          </tr>
          <tr>
            <td><strong>Inclusive Graphic Skewness</strong></td>
            <td>$Sk_I$</td>
            <td>$$\frac{\phi_{16} + \phi_{84} - 2\phi_{50}}{2(\phi_{84} - \phi_{16})} + \frac{\phi_5 + \phi_{95} - 2\phi_{50}}{2(\phi_{95} - \phi_5)}$$</td>
            <td>$0.00$</td>
            <td>Very fine-skewed ($> +0.3$) to Very coarse-skewed ($< -0.3$)</td>
          </tr>
          <tr>
            <td><strong>Graphic Kurtosis</strong></td>
            <td>$K_G$</td>
            <td>$$\frac{\phi_{95} - \phi_5}{2.44(\phi_{75} - \phi_{25})}$$</td>
            <td><strong>$1.00$</strong></td>
            <td>Very platykurtic ($< 0.67$) to Very leptokurtic ($> 1.50$)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Practice Problems & Analytical Derivations</div>
    <div class="card-body">
      <div class="problem-box">
        <h4>Practice Problem 1</h4>
        <p>A river sediment sample yields the following percentile values from its cumulative frequency curve: $\phi_5 = 0.50$, $\phi_{25} = 1.60$, $\phi_{75} = 2.40$, and $\phi_{95} = 3.90$. Calculate the Graphic Kurtosis ($K_G$) and classify it according to Folk's verbal scale.</p>
        <p><strong>Solution:</strong>
          Applying Folk and Ward's formula:
          $$K_G = \frac{\phi_{95} - \phi_5}{2.44(\phi_{75} - \phi_{25})}$$
          Substituting values:
          $$K_G = \frac{3.90 - 0.50}{2.44(2.40 - 1.60)} = \frac{3.40}{2.44 \times 0.80} = \frac{3.40}{1.952} \approx \mathbf{1.74}$$
          According to Folk's verbal scale, a $K_G$ value between $1.50$ and $3.00$ is classified as <strong>Very Leptokurtic</strong>. This indicates an excessively peaked central body with an outlying tail of poorly sorted grains.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Show mathematically why a bimodal sediment composed of $50\%$ coarse gravel ($\phi = -2$) and $50\%$ fine sand ($\phi = +3$) exhibits a Platykurtic ($K_G < 0.90$) distribution.</p>
        <p><strong>Solution:</strong>
          In an equal 50:50 bimodal mixture, the cumulative curve rises in two distinct steps separated by a flat terrace across the intermediate sizes. Consequently, the interquartile body ($\phi_{75} - \phi_{25}$) spans across the entire wide gap between the two modes, making the denominator $(\phi_{75} - \phi_{25})$ abnormally large relative to the outer tails $(\phi_{95} - \phi_5)$. When divided by $2.44(\phi_{75} - \phi_{25})$, the resulting $K_G$ drops well below $0.90$ (often $0.55\text{--}0.65$), producing a <strong>very platykurtic (flat-topped or saddle-shaped)</strong> frequency distribution.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is the transformed kurtosis metric $K'_G$ proposed by Folk and Ward, and why was it introduced?</p>
        <p><strong>Solution:</strong>
          Because $K_G$ values are severely non-normal and positively skewed (ranging from $0.40$ to infinity, with normal at $1.00$), Folk and Ward introduced the <strong>Transformed Kurtosis ($K'_G$)</strong>:
          $$K'_G = \frac{K_G}{1 + K_G}$$
          This mathematical transformation normalizes the scale into a bounded range between $0.0$ and $1.0$, where a normal Gaussian curve corresponds to:
          $$K'_G = \frac{1.0}{1 + 1.0} = \mathbf{0.50}$$
          enabling rigorous linear regression and multivariate statistical testing.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>A coastal geologist tests a beach dune sand and finds $\phi_{95} - \phi_5 = 2.44\phi$ and $\phi_{75} - \phi_{25} = 1.00\phi$. Calculate $K_G$ and identify the distribution type.</p>
        <p><strong>Solution:</strong>
          $$K_G = \frac{2.44}{2.44 \times 1.00} = \frac{2.44}{2.44} = \mathbf{1.00}$$
          A $K_G$ of exactly $1.00$ corresponds to a <strong>Mesokurtic</strong> distribution. The ratio of tail sorting to central body sorting matches that of a perfectly symmetrical, standard Gaussian normal distribution.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why do natural sediments that have undergone prolonged sorting by wind in desert dunes frequently exhibit Leptokurtic kurtosis ($K_G > 1.11$)?</p>
        <p><strong>Solution:</strong>
          In eolian dune environments, steady wind velocities selectively transport and concentrate a very narrow, uniform grain size in the central $70\text{--}80\%$ of the sediment (the saltation population, creating an exceptionally well-sorted central body). However, occasional wind gusts roll a few oversized coarse grains (creep population) and light breezes trap a few silt dust grains, forming extended, poorly sorted tails. This contrast—an ultra-well-sorted central mode flanked by minor poorly sorted tails—forces $K_G$ into the <strong>leptokurtic</strong> field.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Compare the percentile coverage of the Folk & Ward (1957) kurtosis formula with the earlier Trask (1932) kurtosis index.</p>
        <p><strong>Solution:</strong>
          Parker D. Trask (1932) defined a crude geometric kurtosis based solely on quartile spreads: $K = \frac{Q_1 Q_3}{2 M}$. This formula evaluates only the middle $50\%$ of the distribution and completely ignores the critical outer $90\%$ tails. Folk and Ward's formula incorporated $\phi_5$ and $\phi_{95}$, capturing the sorting behavior of $90\%$ of the sediment volume and making it far more sensitive to hydrodynamic mixing and bi-modality.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>If a cumulative curve has $\phi_5 = 0.8$, $\phi_{25} = 1.5$, $\phi_{75} = 2.0$, and $\phi_{95} = 3.6$, calculate $K_G$ and determine whether the central body or the tails are better sorted.</p>
        <p><strong>Solution:</strong>
          $$K_G = \frac{3.6 - 0.8}{2.44(2.0 - 1.5)} = \frac{2.8}{2.44 \times 0.5} = \frac{2.8}{1.22} \approx \mathbf{2.30}$$
          Because $K_G = 2.30 \gg 1.00$ (Very Leptokurtic), the central body $(\phi_{75} - \phi_{25} = 0.5\phi)$ is <strong>far better sorted</strong> than the distant tails $(\phi_{95} - \phi_5 = 2.8\phi)$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>In a Friedman (1961, 1967) bivariate scatter plot for environmental discrimination, what two Folk & Ward parameters are plotted against each other to distinguish river sands from beach sands?</p>
        <p><strong>Solution:</strong>
          Gerald M. Friedman plotted <strong>Inclusive Graphic Skewness ($Sk_I$)</strong> against <strong>Inclusive Graphic Standard Deviation (Sorting, $\sigma_I$)</strong>, or Mean ($M_z$) vs. Skewness. Beach sands plot in the negative skewness ($Sk_I < 0$) and very well-sorted ($\sigma_I < 0.5\phi$) field, whereas river sands plot predominantly in the positive skewness ($Sk_I > 0$) and moderately sorted ($\sigma_I > 0.7\phi$) field.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=101,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q101_Folk_Ward_Kurtosis_Formula_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q101: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q101()
