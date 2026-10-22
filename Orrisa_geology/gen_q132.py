#!/usr/bin/env python3
"""
Q132 Generator: Map Scale, Representative Fraction & Feature Linear Dimensions
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q132():
    title = r"Q132: GIS & Cartography: Map Scale & Feature Dimensional Enlargement | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q132: Map Scale Dynamics: How Increasing Representative Fraction Enlarges Feature Dimensions"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 132<br>
<strong>Authoritative References:</strong> Peter A. Burrough and Rachael A. McDonnell, <em>Principles of Geographical Information Systems</em> (Ch. 2: Spatial Data and Models); Arthur H. Robinson et al., <em>Elements of Cartography</em> (6th Ed., Wiley, Ch. 6: Map Scale); Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (Ch. 2); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11, p. 217)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND ARITHMETIC OF MAP SCALE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Mathematical Mechanics & The Arithmetic of Map Scale</div>
    <div class="card-body">
      <p>
        In cartography, geological mapping, and GIS, <strong>Map Scale</strong> is defined as the mathematical ratio of a distance measured on the map sheet ($d_m$) to the corresponding actual horizontal distance measured on the ground ($D_g$) (Robinson et al., 1995; Burrough & McDonnell, 1998; Bangar, p. 217):
      </p>

      <div class="math-block">
        $$\text{Map Scale} = \frac{\text{Map Distance } (d_m)}{\text{Ground Distance } (D_g)} = \frac{1}{M} = \text{Representative Fraction (RF)}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q132/map_scale_feature_dimensions_enlargement.png" alt="Map Scale Enlargement and Feature Dimensions">
        <div class="figure-caption">
          <strong>Figure 132.1 — Geometric Effect of Increasing Map Scale:</strong> Comparison of identical real-world ground features mapped at $1 : 100,000$ versus $1 : 50,000$. Increasing the scale by a factor of 2 doubles linear dimensions on the map ($2\times$) and quadruples the printed surface area ($4\times$), allowing fine geological details, fault splays, and bedding traces to appear significantly larger.
        </div>
      </div>

      <h4>The Arithmetic of the Representative Fraction (RF)</h4>
      <p>
        The classical examination stumbling block arises because scale is expressed as a fraction:
      </p>
      <ul>
        <li>At scale $1 : 100,000$, the Representative Fraction is:
          $$\text{RF}_1 = \frac{1}{100,000} = 0.000010$$
        </li>
        <li>At scale $1 : 50,000$, the Representative Fraction is:
          $$\text{RF}_2 = \frac{1}{50,000} = 0.000020$$
        </li>
      </ul>
      <p>
        Because $0.000020 > 0.000010$ ($\frac{1}{50,000} > \frac{1}{100,000}$), transitioning from $1 : 100,000$ to $1 : 50,000$ represents an <strong>INCREASE in map scale</strong> (a larger scale map).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q132/bangar_p217_map_scale_feature_dimensions.png" alt="Map Scale from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 132.2 — Map Scale and Feature Dimensions:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 217). Confirms: <em>"As the scale of a map increases, e.g., 1 : 100000 to 1 : 50000, the relative size of the features on the map will increase."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: LINEAR AND AREAL SCALING RELATIONSHIPS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Linear and Areal Dimensional Scaling Laws</div>
    <div class="card-body">
      <h4>Linear Dimension Scaling Law</h4>
      <p>
        Rearranging the scale definition gives the rendered length of any real-world ground feature on the map sheet:
      </p>
      <div class="math-block">
        $$d_m = \text{RF} \times D_g = \frac{D_g}{M}$$
      </div>
      <p>
        For a fixed ground feature of length $D_g = 1000\text{ meters}$ ($1\text{ km}$):
      </p>
      <ul>
        <li>On a $1 : 100,000$ map:
          $$d_{m(100k)} = \frac{1000\text{ m}}{100,000} = 0.010\text{ m} = 1.0\text{ cm} = 10\text{ mm}$$
        </li>
        <li>On a $1 : 50,000$ map:
          $$d_{m(50k)} = \frac{1000\text{ m}}{50,000} = 0.020\text{ m} = 2.0\text{ cm} = 20\text{ mm}$$
        </li>
      </ul>
      <p>
        Thus, the relative linear size of the feature on the map paper <strong>doubles (increases by $100\%$)</strong>.
      </p>

      <h4>Areal Dimension Scaling Law (The Square Law)</h4>
      <p>
        Because surface area is the product of two orthogonal linear dimensions ($L \times W$), the area occupied by a feature on the map sheet scales as the <strong>square of the linear scale factor</strong>:
      </p>
      <div class="math-block">
        $$A_{\text{map}} = (\text{RF})^2 \times A_{\text{ground}} = \left(\frac{1}{M}\right)^2 A_{\text{ground}}$$
        $$\frac{A_{\text{map}(50k)}}{A_{\text{map}(100k)}} = \left(\frac{100,000}{50,000}\right)^2 = (2)^2 = 4$$
      </div>
      <p>
        A geological formation, granite pluton, or lake occupying $1\text{ km}^2$ on the ground covers $1.0\text{ cm}^2$ on a $1 : 100,000$ map, but expands to cover <strong>$4.0\text{ cm}^2$ (a four-fold areal increase)</strong> on a $1 : 50,000$ map!
      </p>
    </div>
  </div>

  <!-- CARD 3: LARGE SCALE VS SMALL SCALE CARTOGRAPHY -->
  <div class="card">
    <div class="card-header bg-indigo">3. Cartographic Classification: Large-Scale vs. Small-Scale Maps</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Scale Category</th>
            <th>Representative Fraction Range</th>
            <th>Ground Area Covered</th>
            <th>Feature Depiction & Size</th>
            <th>Standard Geological Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Large Scale</strong></td>
            <td>$> 1 : 25,000$<br>(e.g., $1 : 1,000, 1 : 5,000, 1 : 10,000$)</td>
            <td>Small localized area (a single mine pit, dam site, tunnel portal)</td>
            <td>Features appear <strong>large and highly detailed</strong>; buildings, individual joint traces, and borehole collars shown to scale.</td>
            <td>Detailed engineering geology, open-pit mine bench design, tunnel portal mapping.</td>
          </tr>
          <tr>
            <td><strong>Medium Scale</strong></td>
            <td>$1 : 25,000 \text{ to } 1 : 250,000$<br>(e.g., $1 : 50,000, 1 : 100,000$)</td>
            <td>Moderate district or regional quadrangle</td>
            <td>Features appear <strong>moderate in size</strong>; Survey of India Toposheets.</td>
            <td>Standard quadrangle geological mapping, mineral belt reconnaissance, district hydrogeology.</td>
          </tr>
          <tr>
            <td><strong>Small Scale</strong></td>
            <td>$< 1 : 250,000$<br>(e.g., $1 : 1,000,000, 1 : 5,000,000$)</td>
            <td>Enormous regional territory (entire state, country, or continent)</td>
            <td>Features appear <strong>greatly reduced / tiny</strong>; heavy cartographic generalization, symbolization, and omission.</td>
            <td>National geological maps of India (GSI $1 : 2,000,000$), tectonic framework maps, global seismicity.</td>
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
      <div class="question-number">Question 132</div>
      <div class="question-text">
        As the scale of a map increases, e.g., 1 : 100000 to 1 : 50000, the relative size of the features will :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Decrease</li>
        <li class="option-item correct"><strong>(B)</strong> Increase</li>
        <li class="option-item"><strong>(C)</strong> Remain similar</li>
        <li class="option-item"><strong>(D)</strong> No change in size</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (B) Increase</strong> — As map scale increases (e.g., from $1 : 100,000$ to $1 : 50,000$, where $\text{RF}$ increases from $1/100,000$ to $1/50,000$), a unit ground distance is represented by a larger map distance, causing all features to appear larger on the map sheet.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Decrease — Inverted Scale Fallacy</div>
        <p>
          This is a classical arithmetic pitfall where candidates confuse the denominator value ($M$) with the actual fraction value ($1/M$). Because $50,000 < 100,000$, a superficial glance might lead one to think the scale is "smaller". In reality, $1/50,000 = 0.000020$ is <strong>twice as large</strong> as $1/100,000 = 0.000010$. Features decrease in size only when the scale <em>decreases</em> (e.g., zooming out from $1:50,000$ to $1:250,000$).
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (B): Increase — Mathematically and Cartographically Verified</div>
        <p>
          By formal definition of map scale (Bangar, p. 217; Robinson et al.):
          $$\text{Map Distance } = \text{Scale} \times \text{Ground Distance}$$
          When the scale increases from $1:100,000$ to $1:50,000$, the Representative Fraction increases by a factor of 2. Consequently:
        </p>
        <ol>
          <li>The linear dimensions of all features on the map sheet (lengths of rivers, width of dykes, diameters of craters) <strong>double in size</strong> ($2\times$).</li>
          <li>The surface areas of all polygon features (lakes, geological units) <strong>quadruple in size</strong> ($2^2 = 4\times$).</li>
        </ol>
        <p>Thus, the relative size of features rendered on the map increases.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C) & (D): Remain similar / No change in size — Physically Impossible</div>
        <p>
          Map scale is the fundamental transformation factor between real-world space and cartographic representation. A change in map scale directly and proportionately alters the physical dimensions of every geographic entity rendered on the medium. Asserting that feature sizes "remain similar" or experience "no change" contradicts the foundational definition of cartography.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Quantitative Scaling Comparison: 1 km Ground Feature Across Standard Map Scales</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Representative Fraction (RF)</th>
            <th>Verbal Scale Equivalent</th>
            <th>Map Length of $1.0\text{ km}$ Road</th>
            <th>Map Area of $1.0\text{ km}^2$ Forest</th>
            <th>Relative Linear Size vs. $1:100,000$</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$1 : 1,000,000$</strong></td>
            <td>$1\text{ cm} = 10\text{ km}$</td>
            <td>$0.10\text{ cm} = 1.0\text{ mm}$</td>
            <td>$0.01\text{ cm}^2 = 1.0\text{ mm}^2$</td>
            <td>$0.10\times$ (10 times smaller)</td>
          </tr>
          <tr>
            <td><strong>$1 : 250,000$</strong></td>
            <td>$1\text{ cm} = 2.5\text{ km}$</td>
            <td>$0.40\text{ cm} = 4.0\text{ mm}$</td>
            <td>$0.16\text{ cm}^2 = 16.0\text{ mm}^2$</td>
            <td>$0.40\times$ (2.5 times smaller)</td>
          </tr>
          <tr>
            <td><strong>$1 : 100,000$</strong></td>
            <td>$1\text{ cm} = 1.0\text{ km}$</td>
            <td>$1.00\text{ cm} = 10.0\text{ mm}$</td>
            <td>$1.00\text{ cm}^2 = 100.0\text{ mm}^2$</td>
            <td><strong>$1.00\times$ (Baseline)</strong></td>
          </tr>
          <tr>
            <td><strong>$1 : 50,000$</strong></td>
            <td>$1\text{ cm} = 500\text{ m}$</td>
            <td>$2.00\text{ cm} = 20.0\text{ mm}$</td>
            <td>$4.00\text{ cm}^2 = 400.0\text{ mm}^2$</td>
            <td><strong>$2.00\times$ (Twice as large!)</strong></td>
          </tr>
          <tr>
            <td><strong>$1 : 25,000$</strong></td>
            <td>$1\text{ cm} = 250\text{ m}$</td>
            <td>$4.00\text{ cm} = 40.0\text{ mm}$</td>
            <td>$16.00\text{ cm}^2 = 1600.0\text{ mm}^2$</td>
            <td>$4.00\times$ (4 times as large!)</td>
          </tr>
          <tr>
            <td><strong>$1 : 10,000$</strong></td>
            <td>$1\text{ cm} = 100\text{ m}$</td>
            <td>$10.00\text{ cm} = 100.0\text{ mm}$</td>
            <td>$100.00\text{ cm}^2 = 10,000.0\text{ mm}^2$</td>
            <td>$10.00\times$ (10 times as large!)</td>
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
        <strong>Problem 1: Linear Scale Enlargement Ratio</strong><br>
        A geological dyke has a true field length of $D_g = 2500\text{ m}$. Calculate: (a) its length in millimeters on a $1 : 100,000$ map, (b) its length in millimeters on a $1 : 50,000$ map, and (c) the exact magnification factor between the two maps.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Length on $1 : 100,000$ map:
          $$d_{m(100k)} = \frac{2500\text{ m}}{100,000} = 0.025\text{ m} = 25.0\text{ mm}$$
          2. Length on $1 : 50,000$ map:
          $$d_{m(50k)} = \frac{2500\text{ m}}{50,000} = 0.050\text{ m} = 50.0\text{ mm}$$
          3. Magnification factor:
          $$\text{Factor} = \frac{d_{m(50k)}}{d_{m(100k)}} = \frac{50.0\text{ mm}}{25.0\text{ mm}} = 2.0$$
          The linear length of the dyke increases by a factor of $2.0$ (doubles).
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Areal Map Representation (The Square Law)</strong><br>
        A granite pluton covers a real-world ground area of $A_{\text{ground}} = 25.0\text{ km}^2$. Calculate its rendered area in square centimeters ($\text{cm}^2$) on: (a) a $1 : 100,000$ map, and (b) a $1 : 50,000$ map.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Express ground area in square centimeters:
          $$1\text{ km} = 100,000\text{ cm} \implies 1\text{ km}^2 = (10^5\text{ cm})^2 = 10^{10}\text{ cm}^2$$
          $$A_{\text{ground}} = 25.0 \times 10^{10}\text{ cm}^2$$
          2. Area on $1 : 100,000$ map:
          $$A_{m(100k)} = \frac{A_{\text{ground}}}{(100,000)^2} = \frac{25.0 \times 10^{10}}{10^{10}} = 25.0\text{ cm}^2$$
          3. Area on $1 : 50,000$ map:
          $$A_{m(50k)} = \frac{A_{\text{ground}}}{(50,000)^2} = \frac{25.0 \times 10^{10}}{2.5 \times 10^9} = 100.0\text{ cm}^2$$
          <em>Verification:</em> $\frac{100.0}{25.0} = 4.0 = (2)^2$. The rendered map area increases four-fold!
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Minimum Mapping Unit (MMU) on Map Paper</strong><br>
        In national geological mapping standards, the minimum polygon area that can be legibly drawn, color-coded, and labeled on a printed paper map is $4.0\text{ mm}^2$ ($2.0\text{ mm} \times 2.0\text{ mm}$). Calculate the minimum actual ground area (in hectares) that can be depicted on: (a) a $1 : 50,000$ map, and (b) a $1 : 250,000$ map.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Ground area for $1 : 50,000$ map:
          $$1\text{ mm on map} = 50,000\text{ mm on ground} = 50\text{ m}$$
          $$1\text{ mm}^2 \text{ on map} = (50\text{ m})^2 = 2500\text{ m}^2$$
          $$\text{MMU}_{(50k)} = 4.0\text{ mm}^2 \times 2500\text{ m}^2\text{/mm}^2 = 10,000\text{ m}^2 = 1.0\text{ hectare}$$
          2. Ground area for $1 : 250,000$ map:
          $$1\text{ mm on map} = 250,000\text{ mm on ground} = 250\text{ m}$$
          $$1\text{ mm}^2 \text{ on map} = (250\text{ m})^2 = 62,500\text{ m}^2$$
          $$\text{MMU}_{(250k)} = 4.0\text{ mm}^2 \times 62,500\text{ m}^2\text{/mm}^2 = 250,000\text{ m}^2 = 25.0\text{ hectares}$$
          <em>Cartographic Insight:</em> Small ore outcrops between $1\text{ and } 25\text{ hectares}$ can be shown on a $1:50,000$ sheet but must be omitted on a $1:250,000$ sheet.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Determining Unknown Scale from Known Ground Feature</strong><br>
        An aerial photograph displays an airstrip runway with a measured image length of $d_m = 7.2\text{ cm}$ ($0.072\text{ m}$). An engineering survey plan confirms the true horizontal length of the runway is $D_g = 1800\text{ m}$. Determine the Representative Fraction (RF) of the aerial photograph.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate scale ratio:
          $$\text{RF} = \frac{d_m}{D_g} = \frac{0.072\text{ m}}{1800\text{ m}} = \frac{1}{\frac{1800}{0.072}} = \frac{1}{25,000}$$
          The scale of the aerial photograph is $1 : 25,000$.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Ground Distance from Map Measurement on 1 : 50,000 Toposheet</strong><br>
        On a Survey of India $1 : 50,000$ toposheet, the distance between two triangulation stations is measured with a steel ruler to be $14.6\text{ cm}$. Calculate the actual ground distance in kilometers.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. On a $1 : 50,000$ map, $1\text{ cm} = 50,000\text{ cm} = 500\text{ m} = 0.5\text{ km}$.
          2. Compute ground distance:
          $$D_g = 14.6\text{ cm} \times 0.5\text{ km/cm} = 7.30\text{ km}$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Cartographic Generalization & Line Sinuosity Threshold</strong><br>
        Cartographic drafting standards require that the minimum visible separation between two printed parallel lines on a paper map is $0.25\text{ mm}$ (the resolving limit of the human eye at normal reading distance). What is the minimum ground distance that can be distinguished as two separate parallel roads on: (a) a $1 : 50,000$ map, and (b) a $1 : 1,000,000$ map?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. For $1 : 50,000$:
          $$D_g = 0.25\text{ mm} \times 50,000 = 12,500\text{ mm} = 12.5\text{ meters}$$
          2. For $1 : 1,000,000$:
          $$D_g = 0.25\text{ mm} \times 1,000,000 = 250,000\text{ mm} = 250.0\text{ meters}$$
          Parallel features closer than $250\text{ m}$ on the ground merge into a single line on a $1:1,000,000$ map.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Web Mercator Zoom Level vs. Equivalent Map Scale</strong><br>
        In digital web mapping (Google Maps, OpenStreetMap), each increment in Zoom Level ($Z \rightarrow Z + 1$) exactly doubles the linear screen resolution (pixels per ground meter). If Zoom Level 12 corresponds approximately to an RF of $1 : 136,000$, what is the equivalent map scale at Zoom Level 14?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Increase in zoom level: $\Delta Z = 14 - 12 = 2$.
          2. Linear magnification factor: $2^{\Delta Z} = 2^2 = 4$.
          3. New Representative Fraction:
          $$\text{Scale}_{14} = \text{Scale}_{12} \times 4 = \frac{1}{136,000} \times 4 = \frac{4}{136,000} = \frac{1}{34,000}$$
          Zoom Level 14 corresponds to a scale of approximately $1 : 34,000$.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Digital Raster Resampling on Scale Change</strong><br>
        A digital geological map was scanned and digitized at a scale of $1 : 100,000$ with an effective pixel ground resolution of $10\text{ m} \times 10\text{ m}$. To display the map at $1 : 50,000$ on a standard $96\text{ DPI}$ monitor without pixilation, the required ground pixel resolution is $5\text{ m} \times 5\text{ m}$. Calculate the increase in total pixel count required to cover a $20\text{ km} \times 20\text{ km}$ quadrangle.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Quadrangle dimensions: $20,000\text{ m} \times 20,000\text{ m} = 400,000,000\text{ m}^2$.
          2. Pixel count at $10\text{ m}$ resolution ($1:100,000$):
          $$N_1 = \left(\frac{20,000}{10}\right) \times \left(\frac{20,000}{10}\right) = 2000 \times 2000 = 4,000,000\text{ pixels (4 Megapixels)}$$
          3. Pixel count at $5\text{ m}$ resolution ($1:50,000$):
          $$N_2 = \left(\frac{20,000}{5}\right) \times \left(\frac{20,000}{5}\right) = 4000 \times 4000 = 16,000,000\text{ pixels (16 Megapixels)}$$
          $$\text{Increase Factor} = \frac{16,000,000}{4,000,000} = 4.0$$
          The pixel count quadruples ($4\times$), perfectly matching the square law of scale enlargement.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=132,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q132_Map_Scale_Representative_Fraction_Increase_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q132: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q132()
