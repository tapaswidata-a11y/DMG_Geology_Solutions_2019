#!/usr/bin/env python3
"""
Q136 Generator: GIS Accuracy: Source Data Quality vs. Encoded Processing Operations
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q136():
    title = r"Q136: GIS & Spatial Analysis: GIS Accuracy & Error Propagation | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q136: GIS Accuracy & Error Propagation: The Interdependence of Source Data and Encoded Processing"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 136<br>
<strong>Authoritative References:</strong> Peter A. Burrough and Rachael A. McDonnell, <em>Principles of Geographical Information Systems</em> (Ch. 9: Data Quality, Errors, and Natural Variation, pp. 220–245); Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (9th Ed., Ch. 14: Data Quality and Errors); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS, p. 221); Michael F. Goodchild and S. Gopal, <em>Accuracy of Spatial Databases</em> (Taylor & Francis)."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS AND THE DUAL ERROR SOURCES -->
  <div class="card">
    <div class="card-header bg-blue">1. Architecture of Spatial Data Quality: The Dual Pillars of GIS Accuracy</div>
    <div class="card-body">
      <p>
        In Geographic Information Science (GIScience), spatial statistics, and digital geoinformatics, <strong>the ultimate accuracy, reliability, and precision of any GIS output product depends inextricably on both the quality of the Source Data and the fidelity of the Encoded Processing operations</strong> (Burrough & McDonnell, 1998; Goodchild & Gopal, 1989; Bangar, p. 221).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q136/gis_accuracy_source_data_and_processing.png" alt="GIS Accuracy: Source Data and Encoded Processing">
        <div class="figure-caption">
          <strong>Figure 136.1 — Error Propagation in GIS:</strong> The dual-source error cascade showing how primary Inherent Source Errors (surveying inaccuracy, paper map stretching, digitization noise) propagate and compound with Operational Processing Errors (map projection distortion, raster resampling, polygon overlay slivers, numerical precision rounding) to govern final GIS accuracy.
        </div>
      </div>

      <h4>The Dual Determinants of GIS Accuracy</h4>
      <p>
        Standard spatial data quality frameworks (ISO 19157, FGDC Spatial Data Transfer Standard) categorize spatial errors into two interdependent domains:
      </p>
      <ol>
        <li>
          <strong>1. Source Data Quality (Inherent / Input Errors):</strong>
          Represents the intrinsic truth, resolution, and precision of the raw data before it enters any GIS operation:
          <ul>
            <li><em>Positional Inaccuracy:</em> Instrument errors in GPS/total station surveying, flight turbulence in photogrammetry, or paper shrinkage/stretching of historical mylar maps.</li>
            <li><em>Attribute Error:</em> Incorrect mineralogical rock type labeling, misclassified soil units, or out-of-date tenure records.</li>
            <li><em>Temporal Obsolescence:</em> Geological boundaries or stream shorelines mapped decades ago that have undergone natural erosion, mine excavation, or seismic displacement.</li>
            <li><em>Scale & Generalization Limits:</em> Using a coarse $1 : 250,000$ regional map to assess site-specific engineering foundations introduces gross spatial generalizations.</li>
          </ul>
        </li>
        <li>
          <strong>2. Encoded Processing Operations (Operational / Algorithmic Errors):</strong>
          Errors introduced, amplified, or propagated through computer algorithms during digital GIS data manipulation:
          <ul>
            <li><em>Map Projection Transformations:</em> Re-projecting between non-conformal or non-equivalent datums introduces angular and areal scale distortions.</li>
            <li><em>Raster Resampling & Cell Aggregation:</em> Nearest-neighbor, bilinear, or cubic convolution resampling introduces radiometric blurring and positional shift.</li>
            <li><em>Topological Overlay & Slivers:</em> Intersecting or unioning two polygon layers digitized at different times produces thousands of spurious, paper-thin "sliver polygons".</li>
            <li><em>Floating-Point Truncation:</em> Computational rounding errors during complex spatial coordinate geometric intersections.</li>
          </ul>
        </li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q136/bangar_p221_gis_accuracy_source_data_processing.png" alt="GIS Accuracy from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 136.2 — GIS Accuracy Factors:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 221). States clearly: <em>"GIS accuracy depends on both encoded processes and source data."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE GIGO PRINCIPLE AND ERROR PROPAGATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. The GIGO Principle & Taylor Series Error Propagation Modeling</div>
    <div class="card-body">
      <h4>The Classical "Garbage In, Garbage Out" (GIGO) Reality</h4>
      <p>
        Even the most sophisticated, mathematically rigorous GIS processing pipeline cannot produce an accurate output if the input source data is erroneous or low-resolution:
      </p>
      <div class="quote-box">
        <em>"No amount of sophisticated geoprocessing can extract truth from fundamentally flawed source data; conversely, flawed geoprocessing algorithms can rapidly degrade pristine, millimeter-accurate source data into useless noise."</em>
      </div>

      <h4>Mathematical Formulation of Error Propagation</h4>
      <p>
        According to Gauss's law of error propagation, if a derived GIS attribute or spatial index $U$ is computed from independent source variables $x_1, x_2, \dots, x_n$ via an encoded mathematical transformation $U = f(x_1, x_2, \dots, x_n)$:
      </p>
      <div class="math-block">
        $$\sigma_U^2 = \sum_{i=1}^n \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_{x_i}^2 + \sigma_{\text{proc}}^2$$
        $$\text{where: } \sigma_{x_i} = \text{Standard error in source data, } \sigma_{\text{proc}} = \text{Algorithm/rounding error in encoded process}$$
      </div>
      <p>
        This equation mathematically proves that final error variance ($\sigma_U^2$) is the composite sum of source data variance ($\sum (\partial f / \partial x_i)^2 \sigma_{x_i}^2$) and operational processing variance ($\sigma_{\text{proc}}^2$).
      </p>
    </div>
  </div>

  <!-- CARD 3: THE FIVE ELEMENTS OF SPATIAL DATA QUALITY -->
  <div class="card">
    <div class="card-header bg-indigo">3. Standardized Elements of Spatial Data Quality (ISO 19157 / FGDC)</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Quality Element</th>
            <th>Governing Domain</th>
            <th>Description & Criteria</th>
            <th>Primary Evaluation Metric</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Positional Accuracy</strong></td>
            <td>Source Data + Processing</td>
            <td>Closeness of coordinate values to their true ground positions.</td>
            <td>Root Mean Square Error ($\text{RMSE} = \sqrt{\frac{1}{N}\sum (\Delta X^2 + \Delta Y^2)}$).</td>
          </tr>
          <tr>
            <td><strong>Attribute Accuracy</strong></td>
            <td>Source Data</td>
            <td>Correctness of quantitative and qualitative non-spatial descriptors.</td>
            <td>Classification Error Matrix (Confusion Matrix), Cohen's Kappa ($\kappa$).</td>
          </tr>
          <tr>
            <td><strong>Logical Consistency</strong></td>
            <td>Encoded Processing</td>
            <td>Fidelity of topological relationships (no unclosed polygons, no self-intersections, no overshoots).</td>
            <td>Topological rule checks, Euler planar consistency.</td>
          </tr>
          <tr>
            <td><strong>Completeness</strong></td>
            <td>Source Data</td>
            <td>Absence of omissions (unmapped features) or commissions (spurious excess features).</td>
            <td>Percentage feature coverage against ground-truth census.</td>
          </tr>
          <tr>
            <td><strong>Lineage</strong></td>
            <td>Source Data + Processing</td>
            <td>Detailed documentation of source materials, transformations, software versions, and human operators.</td>
            <td>Formal XML metadata compliant with ISO 19139.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 136</div>
      <div class="question-text">
        GIS accuracy depends on :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Encoded processes</li>
        <li class="option-item"><strong>(B)</strong> Source data</li>
        <li class="option-item correct"><strong>(C)</strong> Both (A) and (B)</li>
        <li class="option-item"><strong>(D)</strong> None of these</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Both (A) and (B)</strong> — The overall accuracy and reliability of a GIS model depend critically on both the quality of the input Source Data and the precision and appropriateness of the Encoded Processing operations.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Encoded processes — Incomplete (Only One Component)</div>
        <p>
          Encoded processes (the mathematical algorithms, projection equations, resampling methods, and topological intersection routines) directly govern operational accuracy. However, flawless algorithmic processing cannot compensate for inaccurate, coarse, or outdated source data. Selecting (A) alone is incomplete.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Source data — Incomplete (Only One Component)</div>
        <p>
          Source data quality (surveying precision, GPS accuracy, scale, attribute veracity) provides the baseline foundation of any GIS database. However, pristine source data can be severely degraded by improper geoprocessing choices (e.g., using an incorrect datum transformation, coarse rasterization, or careless tolerance snapping). Selecting (B) alone is incomplete.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Both (A) and (B) — Fully Verified & Codified Textbook Fact</div>
        <p>
          In Geographic Information Systems literature (Bangar, p. 221; Burrough & McDonnell, Ch. 9; Chang, Ch. 14):
        </p>
        <ol>
          <li><strong>Source Data:</strong> Determines the maximum theoretical limit of information content, resolution, and positional truth entering the system.</li>
          <li><strong>Encoded Processes:</strong> Determines how faithfully that information is transformed, integrated, and modeled without introducing algorithmic distortion or cumulative error cascades.</li>
        </ol>
        <p>Therefore, GIS accuracy depends inextricably on <strong>Both (A) and (B)</strong>.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): None of these — Contradicts Foundational GIS Science</div>
        <p>
          Asserting that accuracy depends on neither source data nor processing denies the basic mathematical and scientific principles of spatial analysis.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Error Sources and Mitigation Strategies in GIS Workflows</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Error Source</th>
            <th>Category</th>
            <th>Underlying Mechanism</th>
            <th>Mitigation / Quality Control Strategy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Map Digitization Inaccuracy</strong></td>
            <td>Source Data</td>
            <td>Operator hand tremors, mylar media stretching, paper folding.</td>
            <td>Use high-resolution flatbed scanners, affine GCP rectification, automated vectorization.</td>
          </tr>
          <tr>
            <td><strong>Datum Misalignment</strong></td>
            <td>Encoded Process</td>
            <td>Overlaying WGS 84 GPS points onto Everest 1830 topo sheets without 7-parameter Helmert transformation.</td>
            <td>Standardize all spatial layers to a single common datum and projection before analysis.</td>
          </tr>
          <tr>
            <td><strong>Raster Grid Resampling</strong></td>
            <td>Encoded Process</td>
            <td>Altering pixel cell size from $10\text{ m}$ to $30\text{ m}$ blurs sharp geological contacts.</td>
            <td>Use cubic convolution or bilinear interpolation; retain finest native resolution.</td>
          </tr>
          <tr>
            <td><strong>Sliver Polygons</strong></td>
            <td>Encoded Process</td>
            <td>Overlaying two independently digitized boundaries of the same fault or formation.</td>
            <td>Define strict cluster snapping tolerances and execute automated sliver elimination filters.</td>
          </tr>
          <tr>
            <td><strong>Classification Error</strong></td>
            <td>Source Data</td>
            <td>Misidentifying basalt as dolerite in remote sensing spectral classification.</td>
            <td>Conduct field ground-truthing, calculate confusion matrix and kappa coefficient ($\kappa > 0.85$).</td>
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
        <strong>Problem 1: Gauss Error Propagation in Slope Calculation</strong><br>
        A Digital Elevation Model (DEM) is used to calculate topographic slope: $S = \frac{\Delta Z}{L}$, where horizontal distance is $L = 100.0\text{ m}$ with zero error ($\sigma_L = 0$). The elevation difference is $\Delta Z = 25.0\text{ m}$ with a source DEM vertical standard error $\sigma_Z = \pm 1.5\text{ m}$. Calculate the standard error in the derived slope ($\sigma_S$) and express it as a percentage.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Differentiate slope equation with respect to $\Delta Z$:
          $$\frac{\partial S}{\partial (\Delta Z)} = \frac{1}{L} = \frac{1}{100.0\text{ m}} = 0.010\text{ m}^{-1}$$
          2. Apply Gauss error propagation formula:
          $$\sigma_S = \left|\frac{\partial S}{\partial (\Delta Z)}\right| \sigma_Z = 0.010 \times 1.5\text{ m} = 0.015 = 1.5\%$$
          The calculated slope is $S = 25.0\% \pm 1.5\%$.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Root Mean Square Error (RMSE) Positional Threshold</strong><br>
        The United States National Map Accuracy Standards (NMAS) mandate that for a map scale of $1 : 50,000$, not more than $10\%$ of well-defined test points shall have a horizontal positional error exceeding $0.85\text{ mm}$ on the map sheet. Calculate the corresponding maximum permissible ground positional error in meters.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate ground error:
          $$\text{Ground Error} = \text{Map Error} \times \text{Scale Denominator} = 0.85\text{ mm} \times 50,000 = 42,500\text{ mm} = 42.5\text{ meters}$$
          At $1 : 50,000$, field test points must lie within $42.5\text{ meters}$ of their true ground coordinates.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Confusion Matrix & Overall Accuracy of Lithological Classification</strong><br>
        A supervised satellite image classification maps $500\text{ test pixels}$ into three lithological classes. A field ground-truth confusion matrix is established:
        - Granite: $180\text{ correctly classified}, 15\text{ misclassified as Basalt}, 5\text{ as Sandstone}$.
        - Basalt: $140\text{ correctly classified}, 10\text{ misclassified as Granite}, 10\text{ as Sandstone}$.
        - Sandstone: $120\text{ correctly classified}, 12\text{ misclassified as Granite}, 8\text{ as Basalt}$.
        Calculate the <strong>Overall Accuracy</strong> of the classified geological map.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Sum of correctly classified diagonal pixels:
          $$\sum_{\text{correct}} = 180 + 140 + 120 = 440\text{ pixels}$$
          2. Total evaluated pixels:
          $$N = 500\text{ pixels}$$
          3. Overall Classification Accuracy:
          $$\text{Overall Accuracy} = \left(\frac{440}{500}\right) \times 100\% = 88.0\%$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Cohen's Kappa Coefficient ($\kappa$) Calculation</strong><br>
        From the classification in Problem 3, the observed overall agreement is $P_o = 0.880$. Statistical calculation of chance agreement based on row and column marginal totals gives $P_e = 0.345$. Calculate Cohen's Kappa Coefficient ($\kappa$) and assess the classification reliability.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Cohen's Kappa formula:
          $$\kappa = \frac{P_o - P_e}{1 - P_e} = \frac{0.880 - 0.345}{1 - 0.345} = \frac{0.535}{0.655} \approx 0.8168$$
          2. Assessment: According to Landis & Koch (1977), $\kappa > 0.80$ represents <strong>"Almost Perfect / Strong Agreement"</strong> above chance, confirming high attribute quality.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Datum Transformation Error Cascade</strong><br>
        A GPS point surveyed in WGS 84 datum is directly plotted onto an Indian toposheet referenced to the historical Everest 1830 datum without applying the 7-parameter Helmert transformation. The shift in Easting is $\Delta X = +62\text{ m}$ and in Northing is $\Delta Y = +215\text{ m}$. Calculate the resulting planimetric positional error vector in meters.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate vector magnitude:
          $$\text{Error} = \sqrt{\Delta X^2 + \Delta Y^2} = \sqrt{(62)^2 + (215)^2} = \sqrt{3844 + 46,225} = \sqrt{50,069} \approx 223.76\text{ meters}$$
          Omitting the datum transformation introduces an operational processing error of over $223\text{ meters}$!
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Sliver Polygon Accumulation in Geological Overlay</strong><br>
        A GIS overlay operation (Union) is performed between two independent geological surveys of a $50\text{ km}$ fault zone. Due to a digitizing positional difference of $\sigma = 4.0\text{ m}$, the overlay generates 140 spurious sliver polygons with an average width of $3.5\text{ m}$ and average length of $300\text{ m}$. Calculate the total artificial error area generated by sliver polygons in hectares.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Area of one average sliver polygon:
          $$A_{\text{sliver}} = 3.5\text{ m} \times 300\text{ m} = 1050\text{ m}^2$$
          2. Total area of 140 sliver polygons:
          $$A_{\text{total}} = 140 \times 1050\text{ m}^2 = 147,000\text{ m}^2$$
          Convert to hectares:
          $$A_{\text{total}} = \frac{147,000\text{ m}^2}{10,000\text{ m}^2\text{/ha}} = 14.70\text{ hectares}$$
          Topological snapping filters must be applied to eliminate these $14.7\text{ hectares}$ of fictitious slivers.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Raster Cell Size Selection via Shannon-Nyquist Theorem</strong><br>
        According to the Shannon-Nyquist sampling theorem in spatial data capture, to reliably resolve a geological narrow feature of minimum linear dimension $W_{\text{min}} = 10.0\text{ m}$ (e.g., an ore vein or dyke), the maximum allowable raster grid cell size ($\Delta x$) must be no greater than half the feature dimension:
        $$\Delta x \le \frac{W_{\text{min}}}{2}$$
        Calculate the maximum permissible raster cell size and state the consequence if a $15\text{ m}$ cell size is chosen.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Maximum permissible cell size:
          $$\Delta x \le \frac{10.0\text{ m}}{2} = 5.0\text{ meters}$$
          2. Consequence of $15\text{ m}$ cell size: If a $15\text{ m}$ cell size is used, spatial aliasing occurs; the $10\text{ m}$ vein will be averaged with surrounding wall rock pixels, losing its continuous geometric continuity and causing false breaks in the mapped ore body.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Cumulative Cost-Distance Processing Error</strong><br>
        In a least-cost-path pipeline for an ore haulage road, a cost raster of cell size $20\text{ m} \times 20\text{ m}$ assigns an average impedance cost per cell with an individual uncertainty of $\pm 5\%$. If the optimal route traverses $1600\text{ cells}$, and cell errors are independent and random, calculate the percentage relative error in the accumulated total route cost ($E_{\text{route}} = \sigma / \sqrt{N}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Apply the standard error of the sum for $N$ independent identical random variables:
          $$\sigma_{\text{sum}} = \sqrt{N} \times \sigma_{\text{cell}} = \sqrt{1600} \times 5\% = 40 \times 5\% = 200\%$$
          2. Relative percentage error of the total accumulated sum:
          $$\text{Relative Error } (\%) = \frac{\sigma_{\text{sum}}}{N \times \mu_{\text{cell}}} = \frac{\sigma_{\text{cell}}}{\sqrt{N}} = \frac{5\%}{\sqrt{1600}} = \frac{5\%}{40} = 0.125\%$$
          Due to statistical averaging over long traverses, independent random errors cancel out, resulting in a negligible $0.125\%$ relative error in total path cost.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=136,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q136_GIS_Accuracy_Source_Data_Processing_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q136: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q136()
