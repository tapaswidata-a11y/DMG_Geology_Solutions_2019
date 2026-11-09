#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 10 Part C (Q136 - Q143)
GIS Foundations, Spatial Autocorrelation, SDI, Interpolation, Map Scale, DBMS & Buffering.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q136: Geographic Field (Continuous Surface Where Every Point Has a Value)
# -----------------------------------------------------------------------------
def gen_q136():
    q_num = 136
    filename = "Q136_Geographic_Field_Phenomenon_Value_Can_Be_Determined_Complete_Guide.html"
    title = "Q136: GIS Foundations - The Geographic Field Concept"
    badge = "OPSC 2019 Geology Paper-II • Question 136 • GIS Data Models"
    h1_title = "Geographic Information Systems: Conceptual Modeling of Continuous Geographic Fields vs. Discrete Entities"
    meta_text = r"<strong>Topic:</strong> GIS Spatial Data Conceptualization • <strong>Key Concept:</strong> Field-Based View of Space vs. Object-Based View (Goodchild 1992) • <strong>Textbooks:</strong> P.A. Burrough & R.A. McDonnell (<em>Principles of Geographical Information Systems</em>, Ch. 2); Kang-tsung Chang (<em>Introduction to Geographic Information Systems</em>, 9th Ed., Ch. 1); M.F. Goodchild (1992, <em>IJGIS</em>); K.M. Bangar (p. 216)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Continuous Fields vs. Discrete Objects in GIS</div>
      <p>In geographic information science (GIScience), spatial ontology, and computer cartography, real-world geographical phenomena are conceptualized and computationally represented through two complementary ontological views (Burrough & McDonnell; Goodchild 1992; Chang):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Spatial Conceptual Model</th>
              <th>Mathematical Formulation</th>
              <th>Fundamental Definition</th>
              <th>Representative Phenomena & GIS Representation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>GEOGRAPHIC FIELD (Continuous Field Model)</strong> (Option A)</td>
              <td>$$z = f(x, y) \quad \text{or} \quad z = f(x, y, t)$$</td>
              <td>A spatial phenomenon that varies continuously across space such that <strong>for every single coordinate point $(x, y)$ in the study area, a real measurable attribute value can be determined</strong>.</td>
              <td>• Elevation above sea level (DEM)<br>• Atmospheric temperature & barometric pressure<br>• Soil pH & geochemical trace element concentrations<br>• Groundwater piezometric head<br><em>Typically implemented as Raster Grids or TINs.</em></td>
            </tr>
            <tr>
              <td><strong>DISCRETE OBJECT (Entity / Feature Model)</strong></td>
              <td>$$\text{Entity } E = \{ID, \text{Geometry}, \text{Attributes}\}$$</td>
              <td>Space is treated as an empty background container populated by distinct, bounded individual entities with well-defined topological boundaries and empty spaces in between.</td>
              <td>• Land cadastral tax parcels (Polygons)<br>• Geological faults and river centerlines (Lines)<br>• Borehole collars and mining shafts (Points)<br><em>Implemented as Vector Points, Lines, Polygons.</em></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q136/geographic_field_continuous_surface_value_every_point.png" alt="Geographic Field vs Discrete Objects" class="figure-img">
        <div class="figure-caption">Figure 136: Mathematical formalization of a Geographic Field $z = f(x, y)$ where every spatial coordinate possesses an unambiguous measurable value (Option A), contrasted with empty-space discrete objects.</div>
      </div>

      <p>Mathematically, a <strong>geographic field</strong> represents a single-valued mapping from two-dimensional geographic space $\mathbb{R}^2$ to an attribute domain $\mathbb{R}$. There are no "empty gaps" or null locations within the study domain; whether measuring ground surface elevation, surface gravity, or ambient temperature, <strong>a value can always be determined</strong> at any chosen coordinate $(x, y)$ (Option A).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 136</div>
        <div class="raw-q-text">A geographic field is a phenomenon where for every point in the study area:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> A value can be determined</div>
          <div class="raw-opt"><span class="opt-letter">B</span> A value can not be determined</div>
          <div class="raw-opt"><span class="opt-letter">C</span> A value is not relevant</div>
          <div class="raw-opt"><span class="opt-letter">D</span> A value is missing</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (A value can be determined)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">A value can be determined</div>
          <p>By authoritative GIS definition (Burrough & McDonnell, 1998; Goodchild, 1992; Chang, Ch. 1), a continuous geographic field is defined precisely by the property that a single, unambiguous attribute value $z$ can be measured, interpolated, or mathematically determined at every point $(x, y)$ across the entire spatial extent of the study area.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">A value can not be determined</div>
          <p>This contradicts the fundamental definition of a field. If values cannot be determined across points, the phenomenon does not constitute a geographic field.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">A value is not relevant</div>
          <p>Values are the defining essence of a continuous field (e.g. elevation in a Digital Elevation Model). Far from being irrelevant, the values at each coordinate define the physical surface.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">A value is missing</div>
          <p>While unmeasured sample locations exist prior to spatial interpolation, the underlying natural phenomenon itself has no missing values—a surface elevation or temperature exists at every point. A field model asserts total spatial completeness.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Field Classification</th>
              <th>Mathematical Property</th>
              <th>Geological / Environmental Example</th>
              <th>Preferred GIS Data Structure</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Scalar Continuous Field</td><td>Single numerical value per point ($z \in \mathbb{R}$)</td><td>Topographic elevation, terrain slope, groundwater depth</td><td>Raster Grid, TIN (Triangulated Irregular Network)</td></tr>
            <tr><td>Vector Field</td><td>Magnitude and direction at every point ($\vec{V} \in \mathbb{R}^2$ or $\mathbb{R}^3$)</td><td>Groundwater flow velocity vectors, tectonic plate motion vectors, wind velocity</td><td>Vector displacement grid, flow lines</td></tr>
            <tr><td>Categorical (Discrete) Field</td><td>Qualitative class label at every point ($C \in \{C_1, C_2, ...\}$)</td><td>Lithological bedrock geology map, soil classification map</td><td>Classified integer raster grid, polygon coverage</td></tr>
            <tr><td>Tensor Field</td><td>Multi-dimensional matrix at every point ($\mathbf{T}_{ij}$)</td><td>Crustal tectonic stress tensor ($\sigma_{xx}, \sigma_{yy}, \tau_{xy}$)</td><td>Finite element geomechanical mesh</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between a Continuous Field and a Discrete Object in GIS database design?</div>
        <div class="pq-ans">Answer: A continuous field assigns a value to every point in space ($z = f(x, y)$); a discrete object models distinct entities with definite boundaries separated by empty space.</div>
        <div class="pq-exp">Topography is a field; cadastral land parcels are discrete objects.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Which GIS data structure is most naturally suited to represent continuous geographic fields?</div>
        <div class="pq-ans">Answer: The regular Raster Grid (and the Triangulated Irregular Network, TIN).</div>
        <div class="pq-exp">A raster represents space as an exhaustive tessellation of cells where every cell matrix location $(i, j)$ stores an explicit attribute value.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. Can a lithological geological map be conceptualized as a geographic field?</div>
        <div class="pq-ans">Answer: Yes, as a categorical (discrete) field, where every location $(x, y)$ on the map belongs to exactly one geological rock unit.</div>
        <div class="pq-exp">There are no "holes" in a bedrock geological map; every point has a defined stratigraphy.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. In a scalar field representing topographic elevation $z = f(x, y)$, what do the first spatial derivatives represent?</div>
        <div class="pq-ans">Answer: Terrain slope gradient ($S = \sqrt{(\partial z/\partial x)^2 + (\partial z/\partial y)^2}$) and aspect ($\theta = \arctan[(\partial z/\partial y) / (\partial z/\partial x)]$).</div>
        <div class="pq-exp">The gradient vector points in the direction of maximum rate of elevation change.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What mathematical operation is used to construct a continuous geographic field from sparse, discrete borehole data points?</div>
        <div class="pq-ans">Answer: Spatial Interpolation (e.g. Inverse Distance Weighting, Ordinary Kriging, Splines).</div>
        <div class="pq-exp">Interpolation converts discrete point observations $(x_i, y_i, z_i)$ into an exhaustive continuous raster surface $\hat{z}(x, y)$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is a Triangulated Irregular Network (TIN)?</div>
        <div class="pq-ans">Answer: A vector-based continuous field structure that partitions surface space into a contiguous network of non-overlapping triangular facets using Delaunay triangulation.</div>
        <div class="pq-exp">TINs adaptively concentrate high point density in rugged terrain and sparse points in flat plains, optimizing storage compared to fixed-grid rasters.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the "modifiable areal unit problem" (MAUP) when aggregating continuous fields into discrete polygon zones?</div>
        <div class="pq-ans">Answer: Statistical results and spatial correlations change unpredictably depending on the arbitrary size (scale effect) and boundary arrangement (zone effect) of the aggregation units.</div>
        <div class="pq-exp">MAUP demonstrates why continuous field modeling avoids artificial administrative boundary artifacts.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between an isotropic and an anisotropic geographic field?</div>
        <div class="pq-ans">Answer: An isotropic field exhibits identical spatial variation properties in all directions; an anisotropic field exhibits directional dependence (e.g., geological strike or structural fault trend).</div>
        <div class="pq-exp">Anisotropic variograms incorporate directional ellipses to align spatial estimation along structural trends.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q137: Spatial Autocorrelation & Tobler's First Law of Geography
# -----------------------------------------------------------------------------
def gen_q137():
    q_num = 137
    filename = "Q137_Interpolation_Made_Possible_By_Spatial_Autocorrelation_Complete_Guide.html"
    title = "Q137: Spatial Statistics - Spatial Autocorrelation and Tobler's Law"
    badge = "OPSC 2019 Geology Paper-II • Question 137 • Spatial Statistics & Geostatistics"
    h1_title = "Spatial Statistics & Geostatistics: Spatial Autocorrelation as the Theoretical Foundation of Spatial Interpolation"
    meta_text = r"<strong>Topic:</strong> Spatial Statistics & Tobler's First Law • <strong>Key Concept:</strong> Spatial Autocorrelation (Moran's $I$, Geary's $C$) & Geostatistical Semivariance • <strong>Textbooks:</strong> Waldo Tobler (1970, <em>Economic Geography</em>); Kang-tsung Chang (Ch. 15); P.A. Burrough & R.A. McDonnell (Ch. 6); K.M. Bangar (p. 217); A.G. Journel & C.J. Huijbregts (<em>Mining Geostatistics</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Spatial Autocorrelation and Tobler's First Law</div>
      <p>In spatial analysis, geostatistics, and GIS, <strong>spatial interpolation</strong>—the estimation of unknown values at unmeasured locations using sample points of known values—is fundamentally predicated on a foundational geographical axiom formulated by Waldo Tobler in 1970, known as <strong>Tobler's First Law of Geography</strong>:</p>

      <div class="math-block">
        $$\text{“Everything is related to everything else, but near things are more related than distant things.”}$$
      </div>

      <p>This universal phenomenon is formally quantified in mathematical statistics as <strong>Spatial Autocorrelation</strong> (Option A). Spatial autocorrelation measures the correlation of a variable with itself across geographic space. If near locations have similar attribute values, the dataset exhibits <strong>positive spatial autocorrelation</strong>:</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Spatial Autocorrelation State</th>
              <th>Mathematical Metric (Moran's $I$)</th>
              <th>Physical / Geological Manifestation</th>
              <th>Impact on Spatial Interpolation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Positive Spatial Autocorrelation</strong> (Option A)</td>
              <td>$$I > 0 \quad (\text{Approaching } +1.0)$$</td>
              <td>High values cluster near high values; low values cluster near low values. Smooth, continuous gradients (e.g. elevation, ore grade, groundwater head).</td>
              <td><strong>Enables Reliable Interpolation:</strong> Nearby control points provide strong, predictive weighting for estimating intervening unmeasured points.</td>
            </tr>
            <tr>
              <td>Zero Spatial Autocorrelation (Randomness)</td>
              <td>$$I \approx -\frac{1}{N - 1} \approx 0$$</td>
              <td>Spatial randomness (white noise); values at one point provide zero information about neighboring points.</td>
              <td><strong>Interpolation Fails:</strong> Estimating unknown values from neighbors is no better than guessing the global dataset mean.</td>
            </tr>
            <tr>
              <td>Negative Spatial Autocorrelation (Dispersion)</td>
              <td>$$I < 0 \quad (\text{Approaching } -1.0)$$</td>
              <td>Checkerboard pattern; high values systematically surrounded by low values (extreme spatial repulsion).</td>
              <td>Standard distance-weighted interpolation yields severe inverse errors.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q137/spatial_autocorrelation_toblers_law_variogram.png" alt="Spatial Autocorrelation and Semivariogram" class="figure-img">
        <div class="figure-caption">Figure 137: Theoretical semivariogram $\gamma(h)$ demonstrating spatial autocorrelation: semivariance is small at short lag distances $h$ (high correlation) and reaches the sill at range $a$, proving why interpolation works (Option A).</div>
      </div>

      <h4>Mathematical Formulation: Moran's $I$ and Semivariance $\gamma(h)$</h4>
      <p>The global degree of spatial autocorrelation in a spatial dataset is formally quantified by <strong>Moran's $I$ Index</strong>:</p>

      <div class="math-block">
        $$I = \frac{N}{\sum_{i=1}^N \sum_{j=1}^N w_{ij}} \frac{\sum_{i=1}^N \sum_{j=1}^N w_{ij} (z_i - \bar{z})(z_j - \bar{z})}{\sum_{i=1}^N (z_i - \bar{z})^2}$$
      </div>

      <p>where $w_{ij}$ is the spatial weight between points $i$ and $j$, $z_i$ is the attribute value, and $\bar{z}$ is the mean. In geostatistics (Matheron; Journel), this spatial continuity is modeled by the <strong>experimental semivariogram</strong> $\gamma(h)$:</p>

      <div class="math-block">
        $$\gamma(h) = \frac{1}{2 N(h)} \sum_{i=1}^{N(h)} [z(x_i) - z(x_i + h)]^2$$
      </div>

      <p>Because $\gamma(h)$ is small at short separation distances ($h$), nearby points are statistically dependent. This fundamental principle of <strong>Spatial Autocorrelation</strong> is what makes spatial interpolation mathematically possible and valid.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 137</div>
        <div class="raw-q-text">Interpolation is made possible by a principle called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Spatial Autocorrelation</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Spatial auto-correction</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Thematic Autocorrelation</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Thematic auto-correction</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Spatial Autocorrelation)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">Spatial Autocorrelation</div>
          <p>By international GIS and spatial statistical standards (Tobler 1970; Burrough & McDonnell; Chang, Ch. 15; Bangar, p. 217), <strong>Spatial Autocorrelation</strong> is the foundational scientific principle that justifies all spatial interpolation methods. It states that spatial attributes are correlated across distance, allowing unmeasured values to be predicted from nearby sample points.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial auto-correction</div>
          <p>Fabricated distractor mimicking technical phrasing. "Auto-correction" refers to automated software correction of typographical or geometric errors (e.g. snapping dangling nodes in GIS digitizing), not the statistical spatial continuity principle.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Thematic Autocorrelation</div>
          <p>Spurious terminology. Autocorrelation in GIS is inherently <em>spatial</em> (evaluating attribute covariance across geographical distance $h$). "Thematic autocorrelation" is not a recognized scientific term.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Thematic auto-correction</div>
          <p>Fabricated distractor combining unrelated GIS words. It has no mathematical or statistical existence in GIScience.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Spatial Autocorrelation Statistic</th>
              <th>Formula / Mathematical Index</th>
              <th>Value Range</th>
              <th>Interpretation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Global Moran's $I$</td><td>$I = \frac{N}{S_0} \frac{\sum \sum w_{ij} (z_i - \bar{z})(z_j - \bar{z})}{\sum (z_i - \bar{z})^2}$</td><td>$-1.0 \le I \le +1.0$</td><td>$+1$: Perfect clustering (Positive)<br>$0$: Completely random<br>$-1$: Perfect dispersion (Negative)</td></tr>
            <tr><td>Geary's $C$ (Ratio)</td><td>$C = \frac{(N-1)}{2 S_0} \frac{\sum \sum w_{ij} (z_i - z_j)^2}{\sum (z_i - \bar{z})^2}$</td><td>$0 \le C \le 2.0$</td><td>$C < 1$: Positive autocorrelation<br>$C = 1$: Spatial randomness<br>$C > 1$: Negative autocorrelation</td></tr>
            <tr><td>Local Moran's $I_i$ (LISA)</td><td>$I_i = \frac{z_i - \bar{z}}{s^2} \sum_j w_{ij} (z_j - \bar{z})$</td><td>Varies locally</td><td>Identifies local spatial clusters: High-High, Low-Low, and spatial outliers (High-Low)</td></tr>
            <tr><td>Getis-Ord $G_i^*$ (Hotspot)</td><td>$G_i^* = \frac{\sum_j w_{ij} x_j - \bar{X} \sum_j w_{ij}}{S \sqrt{\frac{n \sum w_{ij}^2 - (\sum w_{ij})^2}{n-1}}}$</td><td>Standard normal $Z$-score</td><td>$Z > +1.96$: Statistically significant Hot Spot ($95\%$ conf.)<br>$Z < -1.96$: Statistically significant Cold Spot</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental assumption of all distance-decay spatial interpolation algorithms (like IDW)?</div>
        <div class="pq-ans">Answer: That spatial autocorrelation is positive and decreases monotonically with increasing geographical distance ($w_i \propto 1/d_i^p$).</div>
        <div class="pq-exp">Closer sample points are given exponentially higher weights because their values are more strongly correlated with the target point.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. In a geostatistical semivariogram $\gamma(h)$, what is the "Range" ($a$)?</div>
        <div class="pq-ans">Answer: The separation distance beyond which sample points are no longer spatially autocorrelated and become statistically independent.</div>
        <div class="pq-exp">At the range, the semivariogram reaches an asymptotic plateau known as the "Sill" ($C_0 + C$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What does the "Nugget Effect" ($C_0$) represent in a semivariogram?</div>
        <div class="pq-ans">Answer: Measurement error and micro-scale spatial variability occurring at distances shorter than the smallest sampling interval.</div>
        <div class="pq-exp">A pure nugget semivariogram (flat line) indicates zero spatial autocorrelation at the sampled scale.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. If a spatial dataset has a Moran's $I$ of $+0.85$ with a $p$-value of $0.0001$, what does this indicate?</div>
        <div class="pq-ans">Answer: Strong, statistically significant positive spatial autocorrelation (values are heavily clustered in space).</div>
        <div class="pq-exp">The probability that this clustered spatial pattern arose by random chance is less than $0.01\%$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What does LISA stand for in spatial statistics?</div>
        <div class="pq-ans">Answer: Local Indicators of Spatial Association (developed by Luc Anselin, 1995).</div>
        <div class="pq-exp">LISA decomposes global spatial autocorrelation into local components to map specific spatial clusters and anomalies.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why does classic Ordinary Least Squares (OLS) regression fail when applied to spatially autocorrelated geographic data?</div>
        <div class="pq-ans">Answer: It violates the standard Gauss-Markov assumption of independent and identically distributed (i.i.d.) residual errors ($\text{Cov}(\epsilon_i, \epsilon_j) = 0$).</div>
        <div class="pq-exp">Spatial autocorrelation inflates type-I error rates, requiring Spatial Autoregressive (SAR) or Geographically Weighted Regression (GWR) models.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How does Inverse Distance Weighting (IDW) utilize Tobler's First Law?</div>
        <div class="pq-ans">Answer: By assigning weights inversely proportional to distance raised to a power $p$: $\hat{z}(x_0) = \frac{\sum z_i / d_i^p}{\sum 1 / d_i^p}$.</div>
        <div class="pq-exp">Commonly, $p=2$ (inverse distance squared), reflecting rapid distance-decay of spatial autocorrelation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between Ordinary Kriging and IDW?</div>
        <div class="pq-ans">Answer: IDW uses an arbitrary fixed geometric weighting function ($1/d^p$); Kriging uses an optimized semivariogram model of the data's actual spatial autocorrelation to provide Best Linear Unbiased Estimates (BLUE) and estimation variance.</div>
        <div class="pq-exp">Kriging accounts for spatial clustering and redundancy among neighboring sample points.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q138: Spatial Data Infrastructure (SDI) Architecture
# -----------------------------------------------------------------------------
def gen_q138():
    q_num = 138
    filename = "Q138_In_GIS_Application_SDI_Stands_For_Spatial_Data_Infrastructure_Complete_Guide.html"
    title = "Q138: Geoinformatics - Spatial Data Infrastructure (SDI)"
    badge = "OPSC 2019 Geology Paper-II • Question 138 • Geoinformatics & SDI"
    h1_title = "Geoinformatics & Enterprise GIS: Definition, Architecture, and Pillars of Spatial Data Infrastructure (SDI)"
    meta_text = r"<strong>Topic:</strong> Spatial Data Infrastructure & Standards • <strong>Key Concept:</strong> SDI Definition, Core Components (Data, Metadata, Standards, Network, People) • <strong>Textbooks:</strong> Ian Masser (<em>Building European Spatial Data Infrastructures</em>, Esri Press); G. Rajabifard et al. (<em>Developing Spatial Data Infrastructures: From Concept to Reality</em>); Kang-tsung Chang (Ch. 1); K.M. Bangar (p. 217)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Spatial Data Infrastructure (SDI)</div>
      <p>In modern geoinformatics, spatial database management, and e-governance, <strong>SDI</strong> is the universal acronym for <strong>Spatial Data Infrastructure</strong> (Option B). The concept of an SDI was first formalized in the United States by Presidential Executive Order 12906 in 1994, which established the National Spatial Data Infrastructure (NSDI) under the Federal Geographic Data Committee (FGDC), and has since been adopted globally (e.g. India's NSDI and the European Union's INSPIRE Directive).</p>

      <p>By international consensus (Rajabifard et al.; Masser; FGDC), a <strong>Spatial Data Infrastructure</strong> is formally defined as:</p>

      <div class="math-block">
        $$\text{“A dynamic, multi-tiered framework of technologies, policies, institutional arrangements,}$$
        $$\text{standards, and human resources required to acquire, process, store, distribute, and optimize the use of spatial data.”}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>SDI Core Pillar</th>
              <th>Functional Description</th>
              <th>International Standard / Implementation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>1. Geospatial Data (Core & Thematic)</strong></td>
              <td>Authoritative foundational layers: geodetic control, topographic base, administrative boundaries, hydrology, transport, elevation, geology.</td>
              <td>Survey of India (SOI) Topomaps, Geological Survey of India (GSI) 1:50,000 basemaps.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>2. Metadata (Data Cataloguing)</strong></td>
              <td>Standardized structured documentation describing dataset origin, accuracy, lineage, coordinate reference system, and ownership ("data about data").</td>
              <td><strong>ISO 19115</strong> (Geographic information — Metadata) and FGDC Content Standard.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>3. Technical Standards & Interoperability</strong></td>
              <td>Open specifications enabling diverse GIS software systems to exchange and render geospatial data seamlessly across networks.</td>
              <td><strong>OGC Standards:</strong> WMS (Web Map Service), WFS (Web Feature Service), WCS (Web Coverage Service), GeoTIFF, GeoJSON.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>4. Access Network / Geoportal</strong></td>
              <td>Internet clearinghouses, discovery catalogues, and cloud web services enabling users to search, visualize, and download spatial datasets.</td>
              <td>India NSDI Geoportal, Bhuvan (ISRO), INSPIRE Geoportal, US Data.gov.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>5. People & Policy Framework</strong></td>
              <td>Legal agreements, data sharing mandates, intellectual property rights (IPR), pricing policies, and skilled geospatial workforce.</td>
              <td>National Geospatial Policy of India (2022); Open Data Policy (NDSAP).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q138/spatial_data_infrastructure_sdi_components.png" alt="Spatial Data Infrastructure Architecture" class="figure-img">
        <div class="figure-caption">Figure 138: Structural model of a Spatial Data Infrastructure (SDI, Option B), illustrating the five foundational pillars: Data, Metadata, Standards, Access Networks, and People/Policies.</div>
      </div>

      <p>The primary goal of an SDI is to eliminate duplication of data collection among government agencies, drastically reduce GIS project costs, ensure semantic interoperability, and democratize access to authoritative spatial data for disaster mitigation, natural resources management, and infrastructure engineering.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 138</div>
        <div class="raw-q-text">In Gis application, SDI stands for:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Spatial Data Interface</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Spatial Data Infrastructure</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Spatial Data Intention</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Spatial Data international</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Spatial Data Infrastructure)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Spatial Data Infrastructure</div>
          <p>In all geographic information systems literature, international spatial data policy, and enterprise geoinformatics (Masser; Rajabifard; Chang, Ch. 1; Bangar, p. 217), <strong>SDI</strong> stands universally and unambiguously for <strong>Spatial Data Infrastructure</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Data Interface</div>
          <p>An interface refers to an application programming interface (API) or graphic user interface (GUI) component. While SDIs utilize web interfaces, SDI itself stands for infrastructure.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Data Intention</div>
          <p>Arbitrary fabricated distractor without any technical meaning in GIS or computer science.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Data international</div>
          <p>Grammatically and conceptually incorrect. While international SDIs exist (e.g. GSDI - Global Spatial Data Infrastructure), the letters "SDI" stand specifically for Spatial Data Infrastructure.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>SDI Level / Initiative</th>
              <th>Jurisdiction</th>
              <th>Key Mandate / Platform</th>
              <th>Established Year</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>National SDI (NSDI India)</td><td>Government of India (DST)</td><td>National portal integrating SOI, GSI, FSI, CGWB spatial layers</td><td>2001 / 2006</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>INSPIRE Directive</td><td>European Union (27 nations)</td><td>Legally binding environmental spatial data interoperability (34 data themes)</td><td>2007</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>US NSDI</td><td>United States (FGDC)</td><td>Established by Executive Order 12906; Geospatial Data Act (2018)</td><td>1994</td></tr>
            <tr><td>State SDI (e.g. Odisha SDI)</td><td>State Governments</td><td>State-level spatial databases for land administration, mining, and revenue</td><td>2010s</td></tr>
            <tr><td>Global SDI (GSDI)</td><td>Global Association</td><td>Promotes international cooperation and capacity building for developing nations</td><td>1996</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the Open Geospatial Consortium (OGC) and what role does it play in an SDI?</div>
        <div class="pq-ans">Answer: An international standards organization that develops open, vendor-neutral specifications (WMS, WFS, WCS, KML) to ensure spatial data interoperability across different GIS software.</div>
        <div class="pq-exp">Without OGC standards, an Esri ArcGIS client could not read data served from an open-source QGIS/GeoServer backend.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the fundamental difference between a Web Map Service (WMS) and a Web Feature Service (WFS) in an SDI?</div>
        <div class="pq-ans">Answer: WMS serves pre-rendered raster images of map layers (PNG/JPEG) for visual display; WFS serves raw vector geometries and attribute tables (GML/GeoJSON) allowing direct spatial querying and editing.</div>
        <div class="pq-exp">WMS is for display; WFS allows client-side GIS spatial analysis.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What international standard defines the schema for geographic metadata in an SDI?</div>
        <div class="pq-ans">Answer: ISO 19115 (Geographic information — Metadata) and ISO 19139 (XML implementation).</div>
        <div class="pq-exp">ISO 19115 provides a structured format to document identification, spatial reference, lineage, quality, and distribution constraints.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a "Clearinghouse" or "Geoportal" in an SDI architecture?</div>
        <div class="pq-ans">Answer: A web-based search engine and catalogue service (CSW - Catalogue Service for the Web) that allows users to discover, query metadata for, and access distributed geospatial datasets.</div>
        <div class="pq-exp">India's NSDI Portal and ISRO's Bhuvan act as national clearinghouses.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What major reform was introduced by the Government of India's National Geospatial Policy (2022)?</div>
        <div class="pq-ans">Answer: Complete deregulation and liberalization of geospatial data creation and acquisition, allowing Indian private entities to collect high-resolution data without prior security clearances.</div>
        <div class="pq-exp">It promotes democratization of spatial data and unifies national surveying under modern CORS networks.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the "CORS" network being established by the Survey of India as part of modern national geodetic SDI?</div>
        <div class="pq-ans">Answer: Continuously Operating Reference Stations; a network of permanent geodetic GNSS base stations providing real-time kinematic (RTK) positioning with centimeter-level accuracy nationwide.</div>
        <div class="pq-exp">CORS eliminates the need for individual surveyors to set up local reference base stations.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is "Interoperability" in the context of a Spatial Data Infrastructure?</div>
        <div class="pq-ans">Answer: The capability of disparate, autonomous hardware, software, and database systems to communicate, execute programs, and transfer geospatial data without human intervention or data conversion.</div>
        <div class="pq-exp">Interoperability requires adherence to open OGC web service protocols and ISO data standards.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between a "Data-Centric" and a "Process-Centric" SDI?</div>
        <div class="pq-ans">Answer: A first-generation data-centric SDI focused primarily on assembling and cataloguing static spatial datasets; a second-generation process-centric SDI focuses on dynamic web services, real-time sensor integration, and user-driven analytics.</div>
        <div class="pq-exp">Modern SDIs are service-oriented architectures (SOA) integrated into cloud web GIS.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q139: Spatial Interpolation Using Known Control Points to Estimate Unknown Points
# -----------------------------------------------------------------------------
def gen_q139():
    q_num = 139
    filename = "Q139_Process_Using_Known_Data_Points_Spatial_Interpolation_Complete_Guide.html"
    title = "Q139: Spatial Analysis - Spatial Interpolation Foundations"
    badge = "OPSC 2019 Geology Paper-II • Question 139 • Spatial Analysis & Surface Modeling"
    h1_title = "Spatial Surface Modeling: Spatial Interpolation Using Known Sample Points to Estimate Values at Unknown Locations"
    meta_text = r"<strong>Topic:</strong> Spatial Surface Interpolation • <strong>Key Concept:</strong> Spatial Estimation, IDW, Kriging & Radial Basis Functions • <strong>Textbooks:</strong> Kang-tsung Chang (<em>Introduction to Geographic Information Systems</em>, 9th Ed., Ch. 15); P.A. Burrough & R.A. McDonnell (Ch. 6); K.M. Bangar (p. 217); E.H. Isaaks & R.M. Srivastava (<em>Applied Geostatistics</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Spatial Interpolation Process</div>
      <p>In earth science, environmental geology, mining engineering, and GIS, financial and logistical constraints make it impossible to collect physical measurements at every point across a continuous landscape. Instead, scientists collect field data at a discrete set of known sample locations (e.g. exploration boreholes, groundwater monitoring wells, seismic shotpoints, or weather stations).</p>

      <p>By international GIS definition (Chang; Burrough & McDonnell; Isaaks & Srivastava), <strong>the computational and mathematical process of using data points with known values to estimate values at unknown, unmeasured points in any given area is called Spatial Interpolation</strong> (Option B):</p>

      <div class="math-block">
        $$\hat{z}(x_0, y_0) = \sum_{i=1}^n \lambda_i \cdot z(x_i, y_i)$$
      </div>

      <p>where $\hat{z}(x_0, y_0)$ is the estimated attribute value at the unknown target location $(x_0, y_0)$, $z(x_i, y_i)$ are the known sample values, and $\lambda_i$ are mathematical weights assigned to each sample point (typically subject to $\sum \lambda_i = 1$).</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Interpolation Method Class</th>
              <th>Underlying Mathematical Theory</th>
              <th>Specific Algorithms</th>
              <th>Geological & Environmental Application</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td><strong>Deterministic Interpolation (Distance-Based)</strong></td>
              <td>Assigns weights purely based on geometric distance or mathematical smoothness; provides no statistical error estimate.</td>
              <td>• <strong>Inverse Distance Weighting (IDW):</strong> $\lambda_i = \frac{d_i^{-p}}{\sum d_i^{-p}}$<br>• <strong>Splines (Thin Plate / Tension):</strong> Minimizes surface curvature.<br>• <strong>Trend Surface Analysis:</strong> Global polynomial regression.</td>
              <td>Quick rainfall surface mapping, regional gravity anomaly separation, preliminary terrain elevation modeling.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Geostatistical Interpolation (Probabilistic / Spatial Structure)</strong></td>
              <td>Uses spatial autocorrelation modeled via the experimental semivariogram ($\gamma(h)$) to calculate Best Linear Unbiased Estimates (BLUE).</td>
              <td>• <strong>Ordinary Kriging (OK)</strong><br>• <strong>Universal Kriging (UK)</strong> (handles spatial trend)<br>• <strong>Indicator Kriging (IK)</strong> (threshold exceedance)<br>• <strong>Cokriging</strong> (uses secondary covariate).</td>
              <td>Mining ore reserve block estimation, groundwater hydraulic head, soil contaminant plumes; <strong>provides prediction standard error map $\sigma_k(x_0)$</strong>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q139/spatial_interpolation_idw_kriging_unknown_points.png" alt="Spatial Interpolation Process" class="figure-img">
        <div class="figure-caption">Figure 139: Conceptual mechanics of Spatial Interpolation (Option B): estimating the unknown value $\hat{z}(x_0)$ from surrounding known control points $z_1, z_2, z_3, z_4$ using distance-decay weights.</div>
      </div>

      <p>Spatial interpolation transforms sparse point samples into an uninterrupted, continuous raster grid surface or contour map, which is essential for digital elevation modeling, ore grade contouring, and hydrological modeling.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 139</div>
        <div class="raw-q-text">The process of using data points with known values to estimate values at unknown points in any given area is called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Spatial Prediction</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Spatial interpolation</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Spatial Adjustment</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Spatial Reflection</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Spatial interpolation)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Spatial interpolation</div>
          <p>By verbatim textbook and standard GIS definition (Chang, Ch. 15; Burrough & McDonnell; Bangar, p. 217), the exact process of taking known geographic sample data points and estimating values at unmeasured locations within the bounds of the study area is called <strong>Spatial Interpolation</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Prediction</div>
          <p>While geostatistics sometimes uses "spatial prediction" informally as an umbrella term, "spatial interpolation" is the precise, formal technical term universally used in GIS and spatial analysis curricula for estimating unknown points from known sample points.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Adjustment</div>
          <p>Spatial adjustment refers to rubbersheeting, edge-matching, and geometric coordinate transformation of digitized vector linework to align with georeferenced base features. It does not estimate surface attribute values.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Spatial Reflection</div>
          <p>Fabricated distractor mixing wave optics ("reflection") with spatial terminology; has no meaning in spatial analysis.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Interpolation Method</th>
              <th>Exact vs Inexact</th>
              <th>Local vs Global</th>
              <th>Primary Strength / Characteristic</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Inverse Distance Weighting (IDW)</td><td>Exact (passes through known points)</td><td>Local</td><td>Simple, intuitive, computationally fast; creates "bull's-eye" artifacts around isolated extrema.</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td>Ordinary Kriging (OK)</td><td>Exact (if nugget = 0)</td><td>Local</td><td><strong>BLUE:</strong> Best Linear Unbiased Estimator; minimizes estimation variance and outputs error map.</td></tr>
            <tr><td>Regularized Spline</td><td>Exact</td><td>Local</td><td>Produces smooth, continuous, visually pleasing surfaces with continuous first and second derivatives.</td></tr>
            <tr><td>Trend Surface Analysis</td><td>Inexact (does not pass through points)</td><td>Global</td><td>Fits a single global polynomial plane/surface to separate regional trends from local residuals.</td></tr>
            <tr><td>Thiessen (Voronoi) Polygons</td><td>Exact (stepwise)</td><td>Local</td><td>Assigns the exact value of the nearest sample point to every cell; creates abrupt stepped boundaries.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between Spatial Interpolation and Spatial Extrapolation?</div>
        <div class="pq-ans">Answer: Interpolation estimates values *inside* the spatial boundary bounded by the control points; extrapolation estimates values *outside* the convex hull of known points (which carries extreme uncertainty).</div>
        <div class="pq-exp">Interpolation is statistically constrained by surrounding points; extrapolation diverges rapidly.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What distinguishes an "Exact" interpolator from an "Inexact" interpolator?</div>
        <div class="pq-ans">Answer: An exact interpolator predicts values that match the original sample values identically at the sample locations ($\hat{z}(x_i) = z(x_i)$); an inexact interpolator smooths the surface and may predict different values at sample points.</div>
        <div class="pq-exp">IDW and Splines are exact; Trend surface analysis is inexact.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the effect of increasing the power parameter ($p$) in Inverse Distance Weighting (IDW)?</div>
        <div class="pq-ans">Answer: Higher power values (e.g. $p=3$ or $4$) concentrate influence almost entirely on the immediately adjacent nearest neighbor, making the surface steeper around points; lower power ($p=1$) smooths the surface.</div>
        <div class="pq-exp">The standard default value in GIS software is $p=2$ (inverse distance squared).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. Why is Kriging widely regarded as superior to deterministic methods in mining ore evaluation?</div>
        <div class="pq-ans">Answer: Because Kriging models the spatial continuity structure (semivariogram), accounts for clustering of sample boreholes (declustering effect), and outputs an objective Kriging Variance map quantifying estimation uncertainty.</div>
        <div class="pq-exp">Mining companies use the kriging error map to identify drill-hole gaps before sinking expensive shafts.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is "Cokriging"?</div>
        <div class="pq-ans">Answer: A geostatistical technique that interpolates a primary sparsely sampled variable (e.g. soil heavy metal concentration) by utilizing cross-correlation with a densely sampled, cheaper secondary variable (e.g. airborne radiometrics or elevation).</div>
        <div class="pq-exp">Cokriging leverages the cross-semivariogram between two correlated spatial variables.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What causes the "Bull's-Eye" effect in IDW interpolated surfaces?</div>
        <div class="pq-ans">Answer: As the estimation point approaches an isolated extreme high or low sample point, distance $d \to 0$, causing weight $1/d^p \to \infty$ and creating concentric circular contour rings.</div>
        <div class="pq-exp">Bull's-eyes are artificial artifacts of distance weighting without directional derivative constraints.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Cross-Validation technique used to evaluate the accuracy of spatial interpolation?</div>
        <div class="pq-ans">Answer: "Leave-One-Out" cross-validation: temporarily remove one sample point, estimate its value using the remaining $n-1$ points, compute residual error ($z_i - \hat{z}_i$), and repeat for all $n$ points to calculate RMSE.</div>
        <div class="pq-exp">The method yielding the lowest RMSE is selected as the optimal interpolation model.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is Universal Kriging used for in geological terrain modeling?</div>
        <div class="pq-ans">Answer: For spatial datasets that exhibit a non-stationary regional deterministic trend (drift) along with local random spatial correlation.</div>
        <div class="pq-exp">Universal Kriging separates the global trend (e.g. regional fault dip) from local stationary semivariance residuals.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q140: Representation of a Large City Across Map Scales (1:25,000 vs 1:1,000,000)
# -----------------------------------------------------------------------------
def gen_q140():
    q_num = 140
    filename = "Q140_Large_City_Appears_On_1_25000_Scale_Map_As_A_Polygon_Complete_Guide.html"
    title = "Q140: Cartography - Map Scale and Feature Generalization"
    badge = "OPSC 2019 Geology Paper-II • Question 140 • Cartography & Map Design"
    h1_title = "Digital Cartography & GIS Modeling: Scale-Dependent Representation and Generalization of Urban Features"
    meta_text = r"<strong>Topic:</strong> Cartographic Generalization & Map Scale • <strong>Key Concept:</strong> Scale-Dependent Feature Abstraction: Polygon (Large Scale 1:25,000) vs. Point (Small Scale 1:1,000,000) • <strong>Textbooks:</strong> Kang-tsung Chang (Ch. 1 & 3); P.A. Burrough & R.A. McDonnell (Ch. 2); A.H. Robinson et al. (<em>Elements of Cartography</em>, 6th Ed.); K.M. Bangar (p. 216)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Scale-Dependent Cartographic Generalization</div>
      <p>In Geographic Information Systems and cartography, real-world geographical features cannot be represented at their actual physical size. They must be depicted at a defined <strong>map scale</strong>. A fundamental tenet of spatial modeling is that <strong>the geometric primitive (point, line, or polygon) used to represent a real-world entity is strictly dependent upon map scale</strong> (Robinson et al.; Chang; Burrough & McDonnell):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Map Scale Category</th>
              <th>Representative Fraction (RF)</th>
              <th>Ground Coverage vs Detail</th>
              <th>Geometric Representation of a Large City</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Large-Scale Topographic Map</strong> (The Exam Question)</td>
              <td><strong>1:25,000 (or larger, e.g. 1:10,000)</strong></td>
              <td>Covers a small geographic area with high spatial detail ($1\text{ cm} = 250\text{ m}$).</td>
              <td><strong>AS A POLYGON (or Complex Area Feature):</strong> The city is portrayed as a sprawling 2D areal boundary (polygon) encompassing internal street networks, built-up urban blocks, parks, and administrative municipal borders (Option C).</td>
            </tr>
            <tr>
              <td>Medium-Scale Map</td>
              <td>1:250,000</td>
              <td>Covers an entire district ($1\text{ cm} = 2.5\text{ km}$).</td>
              <td>Generalized irregular polygon or simplified urban boundary showing major transport arteries.</td>
            </tr>
            <tr>
              <td>Small-Scale Continental / World Map</td>
              <td>1:1,000,000 to 1:50,000,000</td>
              <td>Covers vast national or continental extents with heavy generalization ($1\text{ cm} = 10\text{ to } 500\text{ km}$).</td>
              <td><strong>AS A SINGLE POINT:</strong> The entire multi-million population metropolis collapses via cartographic symbolization into a 0-dimensional point circle or dot symbol.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q140/city_representation_1_25000_scale_map_generalization.png" alt="City Representation Across Map Scales" class="figure-img">
        <div class="figure-caption">Figure 140: Scale-dependent cartographic generalization: at large scale 1:25,000 a city appears as an areal <strong>Polygon</strong> (Option C), whereas at small scale 1:1,000,000 it is abstracted into a single point.</div>
      </div>

      <h4>The Process of Cartographic Generalization</h4>
      <p>When transitioning from large to small map scales, the cartographer or automated GIS generalizer applies specific generalization operators:</p>
      <ul>
        <li><strong>Collapse (Dimension Reduction):</strong> Reducing 2D polygon features (like an urban city area) into a 0D point symbol, or a dual-carriageway river into a 1D single center-line.</li>
        <li><strong>Simplification:</strong> Removing high-frequency vertices along jagged polygon boundaries (e.g. Douglas-Peucker algorithm).</li>
        <li><strong>Aggregation:</strong> Merging hundreds of individual building polygons into a unified built-up urban cluster polygon.</li>
      </ul>

      <p>On a <strong>1:25,000 scale map</strong> (the classic high-resolution Survey of India and USGS quadrangle topomap), a large city spanning $20\text{ km} \times 20\text{ km}$ occupies a massive $80\text{ cm} \times 80\text{ cm}$ area on the physical map sheet. It is physically impossible to represent it as a single point; it is rendered as an extensive <strong>polygon</strong> (Option C) containing detailed streets, buildings, and zoning divisions.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 140</div>
        <div class="raw-q-text">How a large city generally appears on a 1: 25,000 scale map:?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> As a single point</div>
          <div class="raw-opt"><span class="opt-letter">B</span> As a cluster of points. lines and polygons</div>
          <div class="raw-opt"><span class="opt-letter">C</span> As a polygon</div>
          <div class="raw-opt"><span class="opt-letter">D</span> As a cluster of points</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (As a polygon)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">As a polygon</div>
          <p>On a large-scale map such as 1:25,000 ($1\text{ cm} = 250\text{ m}$), a city represents a major geographical area with distinct municipal boundaries, built-up extents, and territorial zoning. In vector spatial database design and cartographic standards (Chang, Ch. 1; Burrough & McDonnell; Bangar, p. 216), areal features that have measurable spatial length and width at the given scale are modeled and classified fundamentally as <strong>Polygons</strong> (areal geometric primitives).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">As a single point</div>
          <p>A city appears as a single point only on <strong>small-scale maps</strong> (such as 1:1,000,000 or global atlas maps), where the entire urban area has collapsed to zero area due to cartographic scale limits. On a 1:25,000 map, a city covers dozens of square centimeters and cannot be a single point.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; INFORMAL DESCRIPTION</div>
          <div class="opt-title">As a cluster of points. lines and polygons</div>
          <p>While an urban area internally contains trees (points), roads (lines), and buildings (polygons), the geographic entity "the city as a whole" is categorized in GIS spatial modeling by its bounding areal footprint, which is a <strong>polygon</strong>. Option C is the canonical GIS primitive answer.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">As a cluster of points</div>
          <p>Incorrect. A city is not depicted as an isolated scatter of dots on a large-scale topographic map; it is demarcated as a continuous urban built-up polygon wash (typically tinted yellow or pink on Survey of India topomaps).</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Real-World Geographic Feature</th>
              <th>Small-Scale Map (&le; 1:1,000,000)</th>
              <th>Medium-Scale Map (~ 1:100,000)</th>
              <th>Large-Scale Map (&ge; 1:25,000)</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td>Large City (e.g. Bhubaneswar)</td><td><strong>Point</strong> (Circle dot symbol)</td><td>Generalized Polygon / Area tint</td><td><strong>Detailed Polygon</strong> (blocks, streets, boundaries)</td></tr>
            <tr><td>Major River (e.g. Mahanadi)</td><td>Single thin <strong>Line</strong></td><td>Single line with varying line weight</td><td><strong>Polygon</strong> (two distinct shorelines enclosing water area)</td></tr>
            <tr><td>Highway / Expressway</td><td>Simplified <strong>Line</strong></td><td>Single categorized line</td><td>Detailed line or casing polygon showing right-of-way width</td></tr>
            <tr><td>Building / House</td><td>Omitted completely</td><td>Omitted or tiny generalized dot</td><td>Individual footprint <strong>Polygon</strong></td></tr>
            <tr><td>Quarry / Open-Cast Mine</td><td>Pickaxe point symbol</td><td>Small outlined polygon</td><td>Detailed contour <strong>Polygon</strong> with haul roads and benches</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental definition of a "Large Scale" map vs. a "Small Scale" map?</div>
        <div class="pq-ans">Answer: Large-scale maps have a large Representative Fraction (RF, e.g. $1/25,000 = 0.00004$) showing high detail over small areas; small-scale maps have a tiny RF (e.g. $1/1,000,000 = 0.000001$) showing little detail over vast areas.</div>
        <div class="pq-exp">Remember: $\frac{1}{25,000} > \frac{1}{1,000,000}$; hence 1:25,000 is a larger fraction and larger scale.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What popular automated algorithm is used in GIS vector simplification to reduce vertices while preserving polygon shape?</div>
        <div class="pq-ans">Answer: The Douglas-Peucker (Ramer-Douglas-Peucker) line simplification algorithm.</div>
        <div class="pq-exp">It uses a perpendicular tolerance band ($\epsilon$) to recursively prune redundant vertices along linework.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. On standard Survey of India (SOI) 1:50,000 and 1:25,000 topomaps, what color tint is standardly used to portray the built-up polygon area of a town or city?</div>
        <div class="pq-ans">Answer: Yellow tint (for cultivated land) and Pink / Red tint (for built-up urban / inhabited areas).</div>
        <div class="pq-exp">Pink wash represents dense human settlements, historical ruins, and town polygons.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the cartographic operator "Displacement"?</div>
        <div class="pq-ans">Answer: The intentional shifting of two adjacent features (e.g., a railway line and a road running side-by-side along a narrow river gorge) to prevent their symbol lines from overlapping at reduced scales.</div>
        <div class="pq-exp">Displacement resolves visual graphical conflict when symbol line widths exceed ground clearance.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. If a city boundary measures $8\text{ cm} \times 6\text{ cm}$ on a 1:25,000 map, what is its actual ground footprint in square kilometers?</div>
        <div class="pq-ans">Answer: Exactly $3.0\text{ square kilometers}$.</div>
        <div class="pq-exp">At 1:25,000, $1\text{ cm} = 250\text{ m} = 0.25\text{ km}$. Ground length $= 8 \times 0.25 = 2.0\text{ km}$; width $= 6 \times 0.25 = 1.5\text{ km}$. Area $= 2.0 \times 1.5 = 3.0\text{ km}^2$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is a "Multi-Scale Geodatabase" in enterprise GIS?</div>
        <div class="pq-ans">Answer: A spatial database architecture that maintains multiple representation layers of the same real-world features pre-generalized for specific scale thresholds (e.g. LOD 0 to LOD 4 in CityGML).</div>
        <div class="pq-exp">It enables rapid web map rendering by switching from polygon to point representations as the user zooms out.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the minimum legible delineation (MLD) size on a physical paper map?</div>
        <div class="pq-ans">Answer: Approximately $0.5\text{ mm}$ line width and $2\text{ mm} \times 2\text{ mm}$ minimum polygon area ($4\text{ mm}^2$).</div>
        <div class="pq-exp">Features smaller than the MLD must either be exaggerated in size, collapsed to a point, or omitted.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the difference between geometric generalization and semantic generalization in GIS?</div>
        <div class="pq-ans">Answer: Geometric generalization simplifies graphic shapes (smoothing, collapsing); semantic generalization groups attribute classes into broader thematic categories (e.g. merging "granite", "dolerite", and "gabbro" into "Igneous Rocks").</div>
        <div class="pq-exp">Both are necessary when reducing map scale.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q141: Map Scale Conversion 1:50,000 (1 mm = 50 metres)
# -----------------------------------------------------------------------------
def gen_q141():
    q_num = 141
    filename = "Q141_Map_Scale_1_50000_1_mm_Represents_50_Metres_Complete_Guide.html"
    title = "Q141: Cartography - Map Scale Metric Conversion"
    badge = "OPSC 2019 Geology Paper-II • Question 141 • Cartographic Mathematics"
    h1_title = "Cartographic Mathematics: Representative Fraction (RF) 1:50,000 and Metric Scale Conversion"
    meta_text = r"<strong>Topic:</strong> Map Scale Calculations & Metric Conversion • <strong>Key Concept:</strong> Representative Fraction (RF), Ground Distance Equivalence ($1\text{ mm} = 50\text{ m}$) • <strong>Textbooks:</strong> Kang-tsung Chang (Ch. 1); A.H. Robinson et al. (<em>Elements of Cartography</em>); K.M. Bangar (p. 216); Survey of India Topographical Mapping Guidelines"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Representative Fraction (RF) and Scale Conversion</div>
      <p>In surveying, geological mapping, and cartography, the <strong>map scale</strong> expresses the mathematical ratio of a distance measured on the map sheet to the corresponding true horizontal distance on the ground surface:</p>

      <div class="math-block">
        $$\text{Map Scale} = \frac{\text{Distance on Map}}{\text{Equivalent Horizontal Distance on Ground}}$$
      </div>

      <p>When expressed as a unitless ratio or fraction, it is formally termed the <strong>Representative Fraction (RF)</strong>:</p>

      <div class="math-block">
        $$\text{RF} = 1 : M = \frac{1}{M}$$
      </div>

      <p>where $1$ unit of distance measured in <em>any</em> unit on the map represents exactly $M$ of those <em>same</em> identical units on the ground.</p>

      <h4>Rigorous Step-by-Step Metric Derivation for RF = 1:50,000:</h4>
      <p>We are asked: <em>What does $1\text{ mm}$ on a map drawn at a scale of $1:50,000$ represent on the ground?</em></p>
      
      <p>1. By definition of RF, $1\text{ unit on map} = 50,000\text{ identical units on the ground}$:</p>
      <div class="math-block">
        $$1\text{ mm on map} = 50,000\text{ mm on the ground}$$
      </div>

      <p>2. Converting ground millimeters to centimeters ($1\text{ cm} = 10\text{ mm}$):</p>
      <div class="math-block">
        $$\text{Ground Distance} = \frac{50,000\text{ mm}}{10\text{ mm/cm}} = 5,000\text{ centimetres}$$
      </div>

      <p>3. Converting ground centimeters to meters ($1\text{ m} = 100\text{ cm}$):</p>
      <div class="math-block">
        $$\text{Ground Distance} = \frac{5,000\text{ cm}}{100\text{ cm/m}} = \mathbf{50\text{ metres}} \quad (\mathbf{Option\ C})$$
      </div>

      <p>4. Converting to kilometers ($1\text{ km} = 1,000\text{ m}$):</p>
      <div class="math-block">
        $$\text{Ground Distance} = \frac{50\text{ m}}{1,000\text{ m/km}} = 0.05\text{ km}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Map Measurement (1:50,000 Scale)</th>
              <th>Ground Millimeters</th>
              <th>Ground Centimeters</th>
              <th>Ground Metres</th>
              <th>Ground Kilometers</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>$1\text{ mm}$ on map</strong></td>
              <td>$50,000\text{ mm}$</td>
              <td>$5,000\text{ cm}$</td>
              <td><strong>$50\text{ metres}$ (Option C)</strong></td>
              <td>$0.05\text{ km}$</td>
            </tr>
            <tr>
              <td>$2\text{ mm}$ on map</td>
              <td>$100,000\text{ mm}$</td>
              <td>$10,000\text{ cm}$</td>
              <td>$100\text{ metres}$</td>
              <td>$0.10\text{ km}$</td>
            </tr>
            <tr>
              <td>$1\text{ cm}$ ($10\text{ mm}$) on map</td>
              <td>$500,000\text{ mm}$</td>
              <td>$50,000\text{ cm}$</td>
              <td>$500\text{ metres}$</td>
              <td>$0.50\text{ km}$</td>
            </tr>
            <tr>
              <td>$2\text{ cm}$ ($20\text{ mm}$) on map</td>
              <td>$1,000,000\text{ mm}$</td>
              <td>$100,000\text{ cm}$</td>
              <td>$1,000\text{ metres}$</td>
              <td><strong>$1.0\text{ kilometer}$</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q141/map_scale_1_50000_1mm_equals_50_metres.png" alt="Map Scale Conversion 1:50,000" class="figure-img">
        <div class="figure-caption">Figure 141: Step-by-step metric conversion proving that $1\text{ mm}$ on a 1:50,000 scale map corresponds to $50,000\text{ mm} = 50\text{ metres}$ on the ground (Option C).</div>
      </div>

      <p>The 1:50,000 topographic scale is the foundational standard for Geological Survey of India (GSI) quadrangle mapping, Survey of India (SOI) open series maps (OSM), and regional structural field exploration across India.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 141</div>
        <div class="raw-q-text">What does 1 mm on a map drawn at a scale of 1: 50,000 represent on the ground ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> 50 centimetres</div>
          <div class="raw-opt"><span class="opt-letter">B</span> 5 metres</div>
          <div class="raw-opt"><span class="opt-letter">C</span> 50 metres</div>
          <div class="raw-opt"><span class="opt-letter">D</span> 500 centimetres</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (50 metres)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">50 metres</div>
          <p>By exact mathematical unit conversion:<br>
          $1\text{ mm on map} = 50,000\text{ mm on ground}$.<br>
          Dividing by $1,000\text{ mm/m}$ gives:
          $$\text{Ground Distance} = \frac{50,000}{1,000} = \mathbf{50\text{ metres}}$$.
          Hence, Option C is strictly correct.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; ARITHMETIC ERROR</div>
          <div class="opt-title">50 centimetres</div>
          <p>$50\text{ cm} = 500\text{ mm}$. If $1\text{ mm} = 50\text{ cm}$, the scale would be $1:500$, which is a micro-architectural site plan, not a 1:50,000 regional topomap.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; ARITHMETIC ERROR</div>
          <div class="opt-title">5 metres</div>
          <p>$5\text{ m} = 5,000\text{ mm}$. If $1\text{ mm} = 5\text{ m}$, the scale would be $1:5,000$ (off by a factor of 10).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; ARITHMETIC ERROR</div>
          <div class="opt-title">500 centimetres</div>
          <p>$500\text{ cm} = 5\text{ metres}$ ($5,000\text{ mm}$). This is identical to Option B and also represents an RF of $1:5,000$, which is a factor of 10 too small.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Standard Map Scale (RF)</th>
              <th>$1\text{ mm}$ on Map Represents</th>
              <th>$1\text{ cm}$ on Map Represents</th>
              <th>$1\text{ inch}$ on Map Represents</th>
              <th>Survey / Geological Role</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>1:1,000</td><td>$1\text{ meter}$</td><td>$10\text{ meters}$</td><td>$83.3\text{ feet}$</td><td>Detailed mine bench & plant layout</td></tr>
            <tr><td>1:5,000</td><td>$5\text{ meters}$</td><td>$50\text{ meters}$</td><td>$416.7\text{ feet}$</td><td>Mine lease boundary & cadastral maps</td></tr>
            <tr><td>1:10,000</td><td>$10\text{ meters}$</td><td>$100\text{ meters}$</td><td>$833.3\text{ feet}$</td><td>Detailed mineral deposit block mapping</td></tr>
            <tr><td>1:25,000</td><td>$25\text{ meters}$</td><td>$250\text{ meters}$</td><td>$\approx 0.39\text{ miles}$</td><td>SOI Open Series high-detail topomap</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>1:50,000</strong> (Exam Standard)</td><td><strong>$50\text{ metres}$</strong></td><td><strong>$500\text{ metres}$</strong></td><td><strong>$\approx 0.79\text{ miles}$</strong></td><td><strong>National Topomap & GSI Base Quadrangle</strong></td></tr>
            <tr><td>1:100,000</td><td>$100\text{ meters}$</td><td>$1\text{ kilometer}$</td><td>$\approx 1.58\text{ miles}$</td><td>Regional district planning maps</td></tr>
            <tr><td>1:250,000</td><td>$250\text{ meters}$</td><td>$2.5\text{ kilometers}$</td><td>$\approx 3.95\text{ miles}$ (1 inch = 4 miles)</td><td>Old degree sheet (1° × 1° quadrangle)</td></tr>
            <tr><td>1:1,000,000</td><td>$1,000\text{ m}$ ($1\text{ km}$)</td><td>$10\text{ kilometers}$</td><td>$\approx 15.8\text{ miles}$</td><td>State geological map / Million Sheet</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. On a 1:50,000 scale geological map, a quartz reef is mapped with a length of $4.6\text{ cm}$. What is the true ground strike length of the reef?</div>
        <div class="pq-ans">Answer: Exactly $2.3\text{ kilometers}$ ($2,300\text{ meters}$).</div>
        <div class="pq-exp">At 1:50,000, $1\text{ cm} = 500\text{ m} = 0.5\text{ km}$. Ground length $= 4.6 \times 0.5 = 2.3\text{ km}$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. If an open-cast limestone quarry covers an area of $4\text{ cm}^2$ on a 1:50,000 topomap, what is its actual area on the ground in hectares?</div>
        <div class="pq-ans">Answer: Exactly $100\text{ hectares}$ ($1.0\text{ square kilometer}$).</div>
        <div class="pq-exp">Area scale $= (\text{Linear Scale})^2 = (1/50,000)^2 = 1 / (2.5 \times 10^9)$. Ground area $= 4\text{ cm}^2 \times 2.5 \times 10^9 = 10^{10}\text{ cm}^2 = 1,000,000\text{ m}^2 = 1.0\text{ km}^2 = 100\text{ hectares}$ ($1\text{ ha} = 10,000\text{ m}^2$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the Representative Fraction of an old British imperial map drawn at a scale of "1 inch = 1 mile"?</div>
        <div class="pq-ans">Answer: Exactly $1:63,360$.</div>
        <div class="pq-exp">$$1\text{ mile} = 5,280\text{ feet} = 5,280 \times 12\text{ inches} = 63,360\text{ inches}$$. Hence $\text{RF} = 1:63,360$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the spatial resolution limit of the human naked eye on a printed paper map (often termed the plotting accuracy limit)?</div>
        <div class="pq-ans">Answer: Approximately $0.2\text{ mm}$ (or $0.25\text{ mm}$).</div>
        <div class="pq-exp">On a 1:50,000 map, $0.2\text{ mm}$ represents $0.2 \times 50\text{ m} = 10\text{ meters}$ on the ground. Any ground feature smaller than $10\text{ m}$ cannot be accurately plotted to true scale.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. If a map has a scale of $1\text{ cm} = 2.5\text{ km}$, what is its Representative Fraction (RF)?</div>
        <div class="pq-ans">Answer: $1:250,000$.</div>
        <div class="pq-exp">$$2.5\text{ km} = 2,500\text{ m} = 250,000\text{ cm}$$. Therefore, $1\text{ cm} / 250,000\text{ cm} = 1:250,000$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does map scale affect the contour interval on standard Survey of India topographic sheets?</div>
        <div class="pq-ans">Answer: 1:50,000 sheets typically have a $20\text{ meter}$ contour interval; 1:25,000 sheets have a $10\text{ meter}$ contour interval.</div>
        <div class="pq-exp">Larger scales permit finer vertical contour intervals without crowding contour lines.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a "Verbal Scale" vs. a "Graphic (Bar) Scale"?</div>
        <div class="pq-ans">Answer: A verbal scale expresses scale in words ("1 cm represents 500 m"); a graphic bar scale draws a calibrated line marked in kilometers or miles.</div>
        <div class="pq-exp">A graphic bar scale remains mathematically accurate even if the map is photographically enlarged or reduced.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the dimension of a standard 1:50,000 Survey of India Open Series Map (OSM) quadrangle in latitude and longitude?</div>
        <div class="pq-ans">Answer: Exactly $15'\text{ by } 15'$ ($15\text{ minutes of latitude} \times 15\text{ minutes of longitude}$).</div>
        <div class="pq-exp">Each $1^\circ \times 1^\circ$ degree sheet is subdivided into 16 individual 1:50,000 sheets numbered 1 to 16.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q142: DBMS (Database Management System) in GIS
# -----------------------------------------------------------------------------
def gen_q142():
    q_num = 142
    filename = "Q142_Abbreviation_DBMS_Stands_For_Database_Management_System_Complete_Guide.html"
    title = "Q142: GIS Technology - Database Management Systems (DBMS)"
    badge = "OPSC 2019 Geology Paper-II • Question 142 • GIS Database Management"
    h1_title = "Geographic Information Systems: Architecture, Role, and Capabilities of Database Management Systems (DBMS)"
    meta_text = r"<strong>Topic:</strong> Spatial Databases & DBMS Architecture • <strong>Key Concept:</strong> RDBMS, Spatial Database Extensions (PostGIS, Oracle Spatial) & ACID Properties • <strong>Textbooks:</strong> Kang-tsung Chang (Ch. 3); P.A. Burrough & R.A. McDonnell (Ch. 3); Abraham Silberschatz et al. (<em>Database System Concepts</em>); K.M. Bangar (p. 217)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Role of DBMS in GIS</div>
      <p>In computer science, information technology, and geographic information systems, the universal abbreviation <strong>DBMS</strong> stands for <strong>Database Management System</strong> (Option C). A DBMS is a specialized software suite designed to define, create, query, update, administer, and retrieve structured data from digital computer storage efficiently and securely.</p>

      <p>A complete GIS comprises two fundamental interconnected subsystems:</p>
      <ul>
        <li>A <strong>Spatial Engine / Geometry Processor:</strong> Handles geographic coordinate strings, topological relationships, spatial projections, and vector/raster rendering.</li>
        <li>An <strong>Attribute Database (DBMS):</strong> Stores tabular descriptive data (e.g. well depth, mineral grade, owner name, chemical assay) linked directly to the spatial geometries via unique Primary Keys.</li>
      </ul>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>DBMS Architecture in GIS</th>
              <th>Data Storage Mechanism</th>
              <th>Query Language & Capabilities</th>
              <th>Prominent Commercial & Open-Source Examples</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Dual-Architecture (Hybrid GIS)</strong></td>
              <td>Geometries stored in proprietary binary files (e.g. shapefile <code>.shp</code>); attributes stored in external tabular DBMS (e.g. <code>.dbf</code>).</td>
              <td>Relational joins on Feature ID (FID). Slow spatial indexing; lacks multi-user concurrent write locks.</td>
              <td>Legacy Esri ArcView 3.x, Shapefiles, MapInfo TAB.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Integrated Spatial DBMS (Object-Relational / Geodatabase)</strong> (Modern Standard)</td>
              <td>Both spatial geometries (as <code>GEOMETRY</code> or <code>GEOGRAPHY</code> data types) and tabular attributes reside natively inside the same relational database tables.</td>
              <td><strong>Spatial SQL (OGC Simple Features for SQL):</strong> Spatial indexing via R-Trees, Quad-trees, and GiST indexes.<br><code>SELECT * FROM faults WHERE ST_Intersects(geom, :area);</code></td>
              <td><strong>PostgreSQL + PostGIS</strong>, <strong>Oracle Spatial & Graph</strong>, <strong>Microsoft SQL Server Spatial</strong>, <strong>Esri Enterprise Geodatabase</strong>, <strong>SpatiaLite</strong>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q142/dbms_database_management_system_gis_architecture.png" alt="DBMS Architecture in GIS" class="figure-img">
        <div class="figure-caption">Figure 142: Relational Database Management System (DBMS, Option C) architecture inside GIS, linking spatial vector geometries with structured attribute tables via SQL.</div>
      </div>

      <h4>Core Advantages Provided by an Enterprise DBMS to GIS:</h4>
      <ul>
        <li><strong>ACID Transaction Compliance:</strong> Ensures <em>Atomicity, Consistency, Isolation, and Durability</em> during multi-user spatial editing.</li>
        <li><strong>Multi-User Versioning & Concurrency:</strong> Hundreds of geologists can edit mine lease boundaries and borehole tables simultaneously without data corruption.</li>
        <li><strong>Rapid Spatial Indexing:</strong> R-tree and GiST bounding-box indexes allow sub-second retrieval of millions of spatial polygons.</li>
        <li><strong>Data Integrity & Security:</strong> Enforces foreign-key constraints, domain rules (e.g. dip angle strictly $0^\circ\text{--}90^\circ$), and granular user role security.</li>
      </ul>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 142</div>
        <div class="raw-q-text">What does the abbreviation DBMS stand for ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Digital Base Mapping System</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Data Borrowing and Movement Software</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Database Management System</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Database Manipulation Software</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Database Management System)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Database Management System</div>
          <p>Across computer science, information technology, and GIScience (Silberschatz et al.; Chang, Ch. 3; Burrough & McDonnell; Bangar, p. 217), the acronym <strong>DBMS</strong> stands universally for <strong>Database Management System</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Digital Base Mapping System</div>
          <p>Plausible-sounding GIS distractor, but completely incorrect. Digital base mapping is a cartographic application, not the acronym DBMS.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Data Borrowing and Movement Software</div>
          <p>Fabricated distractor with no scientific or computational standing.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Database Manipulation Software</div>
          <p>While a DBMS includes a Data Manipulation Language (DML, such as SQL), the formal acronym stands for Database Management System.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Database Model Type</th>
              <th>Data Organization Structure</th>
              <th>Relationships Handling</th>
              <th>Usage in Historical & Modern GIS</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Hierarchical Model</td><td>Tree-like parent-child hierarchy (1:N only)</td><td>Rigid top-down pointers; no many-to-many</td><td>Early 1970s mainframe CAD systems</td></tr>
            <tr><td>Network Model</td><td>Graph structure allowing record to have multiple parents (M:N)</td><td>Complex pointer chains</td><td>1970s experimental spatial databases</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Relational Model (RDBMS)</strong> (Option C)</td><td>Two-dimensional tables (relations) of rows (tuples) and columns (attributes)</td><td>Dynamic Primary Key – Foreign Key joins</td><td><strong>Universal standard:</strong> Basis of all commercial and open-source GIS attributes</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Object-Relational DBMS (ORDBMS)</strong></td><td>Relational tables extended with user-defined spatial data types (ST_Geometry) and methods</td><td>SQL with spatial predicates (ST_Contains, ST_Distance)</td><td><strong>Modern Enterprise GIS:</strong> PostgreSQL/PostGIS, Oracle Spatial, SpatiaLite</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What are the four fundamental "ACID" properties guaranteed by an enterprise DBMS?</div>
        <div class="pq-ans">Answer: Atomicity (all changes succeed or all roll back), Consistency (database rules are preserved), Isolation (concurrent transactions do not conflict), and Durability (committed data survives system crashes).</div>
        <div class="pq-exp">ACID guarantees database reliability during multi-user enterprise edits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What standard spatial extension transforms the open-source PostgreSQL relational database into a high-performance spatial DBMS?</div>
        <div class="pq-ans">Answer: PostGIS.</div>
        <div class="pq-exp">PostGIS adds support for geographic objects, spatial operators, GiST R-Tree indexing, and OGC-compliant spatial SQL functions.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a "Spatial Query" in a spatial DBMS?</div>
        <div class="pq-ans">Answer: A database query that evaluates spatial relationships (e.g. containment, intersection, adjacency, proximity) using geometric SQL functions.</div>
        <div class="pq-exp">Example: <code>ST_DWithin(geom1, geom2, 500)</code> finds all boreholes within $500\text{ m}$ of a fault.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the role of a "Primary Key" in a relational database table?</div>
        <div class="pq-ans">Answer: A unique attribute column (or set of columns) that uniquely identifies each individual record (row) in a table without duplicates.</div>
        <div class="pq-exp">In GIS, the Primary Key links attribute records to the corresponding spatial geometries.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is an R-Tree spatial index and why is it faster than conventional B-Tree database indexing?</div>
        <div class="pq-ans">Answer: An R-Tree indexes multidimensional spatial data by grouping nearby objects into Minimum Bounding Boxes (MBRs) in a hierarchical tree.</div>
        <div class="pq-exp">B-Trees only order 1D linear numbers; R-Trees allow rapid 2D/3D spatial bounding box filtering without scanning every table row.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is the difference between DDL and DML in SQL?</div>
        <div class="pq-ans">Answer: DDL (Data Definition Language) creates and alters database structure (<code>CREATE TABLE</code>, <code>DROP</code>); DML (Data Manipulation Language) queries and updates records (<code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>).</div>
        <div class="pq-exp">DDL sets up schemas; DML populates and retrieves data.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is Database Normalization (e.g. 1NF, 2NF, 3NF)?</div>
        <div class="pq-ans">Answer: The formal mathematical process of organizing database tables to eliminate redundant duplicate data, prevent update anomalies, and ensure data dependencies make logical sense.</div>
        <div class="pq-exp">Third Normal Form (3NF) eliminates transitive attribute dependencies.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is an "Enterprise Geodatabase"?</div>
        <div class="pq-ans">Answer: A spatial database structure built on top of an enterprise RDBMS (Oracle, PostgreSQL, SQL Server) that supports versioning, long transactions, network topology, and multi-user editing.</div>
        <div class="pq-exp">It scales to millions of features accessed simultaneously by hundreds of enterprise clients.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q143: Buffer Operation in GIS (Point, Line, Polygon Proximity Zones)
# -----------------------------------------------------------------------------
def gen_q143():
    q_num = 143
    filename = "Q143_Buffer_Operation_Used_In_GIS_Area_Within_Set_Distance_Complete_Guide.html"
    title = "Q143: GIS Spatial Analysis - Proximity Buffering"
    badge = "OPSC 2019 Geology Paper-II • Question 143 • GIS Proximity Analysis"
    h1_title = "GIS Spatial Analysis: Geometric Mechanics and Applications of the Buffer Operation"
    meta_text = r"<strong>Topic:</strong> Vector Spatial Operations & Proximity Analysis • <strong>Key Concept:</strong> Fixed-Distance & Variable Buffering of Points, Lines & Polygons • <strong>Textbooks:</strong> Kang-tsung Chang (<em>Introduction to Geographic Information Systems</em>, 9th Ed., Ch. 11); P.A. Burrough & R.A. McDonnell (Ch. 5); K.M. Bangar (p. 219)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Proximity Analysis and the Buffer Operation</div>
      <p>In Geographic Information Systems (GIS), <strong>proximity analysis</strong> is one of the foundational geometric operations used to evaluate spatial relationships based on distance. Among proximity operators, the <strong>Buffer Operation</strong> is the most widely utilized vector geoprocessing tool (Chang; Burrough & McDonnell; Bangar):</p>

      <p>By international GIS definition, <strong>a buffer operation generates a polygon area enclosing all locations situated within a specified, set distance (the buffer distance, $r$) from an input target feature (point, line, or polygon)</strong>:</p>

      <div class="math-block">
        $$\text{Buffer}(S, r) = \{ p \in \mathbb{R}^2 \mid \min_{q \in S} \text{dist}(p, q) \le r \}$$
      </div>

      <p>where $S$ is the input geometry feature, $r$ is the user-defined buffer distance, and $\text{dist}(p, q)$ is the Euclidean (or geodesic) distance between point $p$ and any point $q$ on feature $S$.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Input Feature Geometry</th>
              <th>Generated Buffer Polygon Geometry</th>
              <th>Mathematical Boundary Shape</th>
              <th>Geological & Environmental Application</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Point Feature</strong> (e.g. Borehole, Blast Site)</td>
              <td>A solid circular polygon centered on the point with radius equal to buffer distance $r$.</td>
              <td>$$\text{Area} = \pi r^2$$</td>
              <td>Blast hazard safety exclusion zone around a quarry; radius of influence around an abstraction well.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Line Feature</strong> (e.g. Fault, River, Road)</td>
              <td>A continuous corridor band polygon extending distance $r$ on both sides of the line, terminating in rounded or flat end caps.</td>
              <td>$$\text{Width} = 2r + \text{Length of line}$$</td>
              <td>Riparian protection corridor along a river; seismic ground-rupture hazard setback zone along a fault scarp.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Polygon Feature</strong> (e.g. Mine Lease, National Park)</td>
              <td>An expanded external boundary zone (external buffer) or an interior setback zone (negative/internal buffer).</td>
              <td>Exterior or interior offset polygon</td>
              <td>Statutory $1\text{ km}$ eco-sensitive buffer zone around wildlife sanctuaries; setback zone inside mining lease.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q143/gis_buffer_operation_point_line_polygon.png" alt="GIS Buffer Operation" class="figure-img">
        <div class="figure-caption">Figure 143: Spatial geometry of the GIS Buffer Operation (Option C) applied to Points (circular zone), Lines (corridor ribbon), and Polygons (expanded boundary).</div>
      </div>

      <h4>Buffer Variations in Advanced Geoprocessing:</h4>
      <ul>
        <li><strong>Fixed-Distance Buffering:</strong> All features in the layer receive the identical buffer radius (e.g. $100\text{ m}$ around all streams).</li>
        <li><strong>Variable-Distance (Attribute) Buffering:</strong> Buffer distance is read dynamically from an attribute column (e.g. streams buffered according to stream order: 1st order $= 20\text{ m}$, 4th order $= 100\text{ m}$).</li>
        <li><strong>Multi-Ring (Concentric) Buffering:</strong> Generates a series of concentric concentric distance bands (e.g. $100\text{ m}, 200\text{ m}, 500\text{ m}, 1000\text{ m}$) for distance-decay risk modeling.</li>
        <li><strong>Dissolved vs. Undissolved:</strong> Overlapping buffer circles can either be merged into a single continuous multipart polygon (Dissolved) or preserved as individual intersecting polygons (Undissolved).</li>
      </ul>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 143</div>
        <div class="raw-q-text">For which of the following applications, the buffer operation can be used in GIS ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Calculating the distance from one point to another</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Calculating the area of overlap between two polygon data layers</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Determining the area within a set distance from a point, line or area feature</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Calculating the number of observations within a set distance of a point line or area feature</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Determining the area within a set distance from a point, line or area feature)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Determining the area within a set distance from a point, line or area feature</div>
          <p>By international GIS definition (Chang, Ch. 11; Burrough & McDonnell; Bangar, p. 219), the fundamental purpose of the <strong>buffer operation</strong> in GIS is to delineate and output a polygon defining the continuous geographic area lying within a specified (set) distance from an input point, line, or area (polygon) feature.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Calculating the distance from one point to another</div>
          <p>Calculating straight-line distance between two coordinates is performed using the Euclidean distance formula ($d = \sqrt{\Delta x^2 + \Delta y^2}$) or network distance tools, not the polygon buffer tool.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Calculating the area of overlap between two polygon data layers</div>
          <p>Computing polygon overlap area is the domain of <strong>topological overlay</strong> operations (specifically <code>Intersect</code> or <code>Clip</code>), not buffering.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Calculating the number of observations within a set distance of a point line or area feature</div>
          <p>Counting observations is a secondary spatial query or point-in-polygon aggregation operation. While a buffer polygon can subsequently be used to clip points, the buffer operation itself <em>determines the spatial area within the set distance</em>.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & High-Yield Practice Questions</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Vector Geoprocessing Tool</th>
              <th>Input Layers</th>
              <th>Operation Mechanism</th>
              <th>Output Geometry</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>BUFFER</strong> (Option C)</td><td>Single layer (Point, Line, or Polygon)</td><td>Creates an offset zone at set distance $r$</td><td><strong>Always outputs a Polygon layer</strong></td></tr>
            <tr><td>INTERSECT</td><td>Two or more layers</td><td>Computes geometric intersection; preserves only overlapping areas and combines attributes</td><td>Polygon, Line, or Point (lowest dimension of inputs)</td></tr>
            <tr><td>UNION</td><td>Two polygon layers</td><td>Computes geometric union; preserves all areas from both layers whether overlapping or not</td><td>Polygon layer with combined schemas</td></tr>
            <tr><td>CLIP</td><td>Input layer + Polygon Clip feature</td><td>Acts as a "cookie cutter"; truncates input features outside clip boundary</td><td>Same geometry as input layer (attributes of clip layer omitted)</td></tr>
            <tr><td>DISSOLVE</td><td>Single layer</td><td>Merges adjacent polygons having identical attribute values into a unified polygon</td><td>Simplified polygon layer</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What geometry type is always produced as the output of a GIS buffer operation, regardless of whether the input is a point, a line, or a polygon?</div>
        <div class="pq-ans">Answer: A Polygon (areal) layer.</div>
        <div class="pq-exp">A buffer transforms 0D points and 1D lines into 2D areal zones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is a "Negative Buffer" and to which geometry type can it be applied?</div>
        <div class="pq-ans">Answer: A buffer created with a negative distance ($-r$) that shrinks the feature inward from its boundary; it can only be applied to Polygon features.</div>
        <div class="pq-exp">Negative buffering defines statutory setback boundaries inside mining leases or building lots.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between a Euclidean Buffer and a Geodesic Buffer in GIS software?</div>
        <div class="pq-ans">Answer: A Euclidean buffer calculates distance on a 2D flat planar projected plane; a Geodesic buffer calculates true great-circle distance across the curved Earth ellipsoid.</div>
        <div class="pq-exp">Over continental or global extents, planar Euclidean buffers suffer massive distortion, requiring geodesic buffering.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. In statutory Indian environmental mining regulations, what is the mandatory eco-sensitive buffer zone typically mandated around the boundary of a National Park or Wildlife Sanctuary?</div>
        <div class="pq-ans">Answer: A $10\text{ kilometer}$ default Eco-Sensitive Zone (ESZ) or site-specific $1\text{ km}$ buffer where commercial mining is strictly prohibited by Supreme Court mandates.</div>
        <div class="pq-exp">GIS polygon buffering is the primary tool used by State Pollution Control Boards and MoEFCC to verify mining compliance.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What happens when the "Dissolve" option is selected during a buffer operation on multiple closely spaced points?</div>
        <div class="pq-ans">Answer: Overlapping buffer circles are fused into a single seamless, continuous multipart polygon, eliminating internal intersecting boundaries.</div>
        <div class="pq-exp">If undissolved, overlapping buffer circles overlap as separate independent polygon entities.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does a raster buffer differ from a vector buffer?</div>
        <div class="pq-ans">Answer: A raster buffer calculates Euclidean distance for every raster grid cell from target source cells (using Euclidean Distance / cost-distance) and reclassifies cells where $\text{dist} \le r$ to a value of $1$.</div>
        <div class="pq-exp">Vector buffering uses trigonometric coordinate offset algorithms; raster buffering uses grid cell distance transforms.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a "Variable-Distance Buffer"?</div>
        <div class="pq-ans">Answer: A buffer whose width varies for each individual feature based on numeric values stored in a specified attribute table column.</div>
        <div class="pq-exp">Example: Buffering roads by road hierarchy width (National Highway $= 60\text{ m}$, State Highway $= 30\text{ m}$, Village Road $= 10\text{ m}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the GIS workflow to identify all schools located within $500\text{ meters}$ of an active mining haul road?</div>
        <div class="pq-ans">Answer: (1) Run Buffer on the haul road line layer with distance $= 500\text{ m}$; (2) Perform Spatial Overlay (Point-in-Polygon / Select by Location) of the school point layer intersecting the haul road buffer polygon.</div>
        <div class="pq-exp">Buffering followed by spatial selection is the classic GIS proximity screening workflow.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Solutions Batch 10 Part C (Q136 - Q143)...")
    gen_q136()
    gen_q137()
    gen_q138()
    gen_q139()
    gen_q140()
    gen_q141()
    gen_q142()
    gen_q143()
    print("Batch 10 Part C successfully generated!")
