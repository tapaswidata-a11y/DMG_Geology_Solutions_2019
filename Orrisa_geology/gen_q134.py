#!/usr/bin/env python3
"""
Q134 Generator: Geoprocessing Architecture & Alphanumeric Input Data in GIS
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q134():
    title = r"Q134: GIS & Spatial Analysis: Geoprocessing Alphanumeric Inputs | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q134: Geoprocessing Architecture: Why Alphanumeric Data Forms the Input of Spatial Workflows"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 134<br>
<strong>Authoritative References:</strong> Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (9th Ed., Ch. 11: Geoprocessing, pp. 245–270); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS and Remote Sensing, p. 219); Paul A. Longley et al., <em>Geographic Information Science and Systems</em> (4th Ed., Wiley, Ch. 13); Peter A. Burrough and Rachael A. McDonnell, <em>Principles of Geographical Information Systems</em> (Ch. 6)."""

    part1 = r"""
  <!-- CARD 1: GEOPROCESSING AND ALPHANUMERIC ARCHITECTURE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Architecture & The Alphanumeric Nature of Geoprocessing Inputs</div>
    <div class="card-body">
      <p>
        In Geographic Information Systems (GIS), spatial analysis, and geoinformatics, <strong>geoprocessing</strong> is the foundational framework for executing automated spatial operations. It accepts one or more input spatial datasets, applies rigorous analytical, topological, or mathematical transformations, and generates derived output datasets (Chang, 2019; Longley et al., 2015; Bangar, p. 219).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q134/geoprocessing_workflow_alphanumeric_inputs.png" alt="Geoprocessing Workflow and Alphanumeric Inputs">
        <div class="figure-caption">
          <strong>Figure 134.1 — Geoprocessing Engine and Dual Alphanumeric Inputs:</strong> Conceptual model illustrating how geoprocessing operations (Buffer, Clip, Intersect, Dissolve, Spatial Join) process composite inputs consisting of numeric spatial coordinates $(X, Y)$ coupled with alphanumeric attribute tables (text strings, categorical codes, and quantitative numeric floats/integers).
        </div>
      </div>

      <h4>Why Geoprocessing Inputs are Fundamentally Alphanumeric</h4>
      <p>
        A geographic feature in a GIS is never merely a collection of geometric points or lines; it is an intelligent digital entity characterized by two intimately linked data components:
      </p>
      <ol>
        <li>
          <strong>Numeric Spatial Component:</strong>
          The geometric primitives (points, vertices of polylines, boundary rings of polygons) are defined by quantitative numerical values:
          <ul>
            <li>Cartesian coordinates: Easting ($X$) and Northing ($Y$) in meters.</li>
            <li>Elevation / Depth values: $Z$ in meters above mean sea level.</li>
            <li>Quantitative attributes: Ore grade percentages ($\text{Fe}\%, \text{Al}_2\text{O}_3\%$), layer thicknesses, permeability coefficients ($k$), porosity ($n$).</li>
          </ul>
        </li>
        <li>
          <strong>Alphabetic / Textual Component:</strong>
          The qualitative descriptors stored in relational database management systems (RDBMS) attribute tables:
          <ul>
            <li>Lithological rock classifications: <em>"Banded Iron Formation"</em>, <em>"Charnockite"</em>, <em>"Dolerite"</em>.</li>
            <li>Chronostratigraphic ages: <em>"Archaean"</em>, <em>"Proterozoic"</em>, <em>"Gondwana"</em>.</li>
            <li>Geological structural identifiers: <em>"Normal Fault"</em>, <em>"Synclinal Hinge"</em>, <em>"Shear Zone"</em>.</li>
            <li>Administrative names: District, mining concession block, operator name.</li>
          </ul>
        </li>
      </ol>
      <p>
        Because GIS data models fuse spatial geometry with relational database attributes, <strong>the input to any geoprocessing operation is fundamentally Alphanumeric</strong> (combining numbers and letters) (Bangar, p. 219).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q134/bangar_p219_geoprocessing_alphanumeric_inputs.png" alt="Geoprocessing Input from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 134.2 — Geoprocessing in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 219). Explicitly confirms: <em>"The input to geoprocessing is alphanumeric (consisting of both numerical coordinate data and alphabetical attribute information)."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: CANONICAL GEOPROCESSING OPERATORS -->
  <div class="card">
    <div class="card-header bg-emerald">2. The Suite of Classical Vector Geoprocessing Operations</div>
    <div class="card-body">
      <p>
        Geoprocessing encompasses standard spatial operators that query, transform, or synthesize alphanumeric layers:
      </p>
      <table class="table">
        <thead>
          <tr>
            <th>Geoprocessing Tool</th>
            <th>Input Geometric Type</th>
            <th>Transformation Logic</th>
            <th>Attribute Handling</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Buffer</strong></td>
            <td>Point, Line, or Polygon</td>
            <td>Generates an equidistant perimeter zone of specified distance ($r$) around features.</td>
            <td>Inherits all alphanumeric attributes from input features.</td>
          </tr>
          <tr>
            <td><strong>Clip</strong></td>
            <td>Point, Line, or Polygon (Input) + Polygon (Clip Boundary)</td>
            <td>Cuts out an input layer using the geographic boundary of another layer (cookie-cutter).</td>
            <td>Preserves alphanumeric attributes of input layer; clip layer attributes discarded.</td>
          </tr>
          <tr>
            <td><strong>Intersect</strong></td>
            <td>Two or more overlapping layers</td>
            <td>Computes the geometric intersection; outputs only areas common to all inputs.</td>
            <td><strong>Fuses alphanumeric attributes:</strong> Output table contains fields from all participating layers.</td>
          </tr>
          <tr>
            <td><strong>Union</strong></td>
            <td>Two polygon layers</td>
            <td>Computes geometric union; retains all areas from both layers.</td>
            <td>Combines all alphanumeric attribute tables, filling non-overlapping cells with $\text{Null}$.</td>
          </tr>
          <tr>
            <td><strong>Dissolve</strong></td>
            <td>Polygon or Line</td>
            <td>Aggregates adjacent features that share an identical alphanumeric attribute value.</td>
            <td>Merges geometric boundaries; aggregates numeric fields via $\text{SUM, MEAN, MAX}$.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 3: ATTRIBUTE QUERIES AND SQL INTEGRATION -->
  <div class="card">
    <div class="card-header bg-indigo">3. Structured Query Language (SQL) & Alphanumeric Data Filtering</div>
    <div class="card-body">
      <h4>Dual-Mode Geoprocessing: Combining Spatial and Attribute Queries</h4>
      <p>
        The power of geoprocessing lies in combining Boolean alphanumeric attribute queries with spatial operators:
      </p>
      <div class="math-block">
        $$\text{SQL Expression: } \text{SELECT * FROM Mining\_Leases WHERE (Status = 'Active') AND (Fe\_Grade } \ge 62.5)$$
      </div>
      <p>
        Here, <code>Status = 'Active'</code> executes an alphabetic string match, while <code>Fe_Grade >= 62.5</code> performs a quantitative numeric inequality. The resulting subset of features is immediately fed into spatial geoprocessing tools (e.g., buffering a $500\text{ m}$ environmental safety zone around active high-grade mines).
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 134</div>
      <div class="question-text">
        The input to geoprocessing is :
      </div>
      <ul class="option-list">
        <li class="option-item correct"><strong>(A)</strong> Alphanumeric</li>
        <li class="option-item"><strong>(B)</strong> Numeric</li>
        <li class="option-item"><strong>(C)</strong> Alphabet</li>
        <li class="option-item"><strong>(D)</strong> Datasheet</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (A) Alphanumeric</strong> — In GIS systems, geoprocessing takes composite spatial layers as input, combining numeric spatial coordinates ($(X,Y)$ vertices, elevations, areas) with alphabetic and textual attribute data (names, rock types, ages), making the input fundamentally alphanumeric.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option correct">
        <div class="option-title">Option (A): Alphanumeric — Fully Verified & Codified Textbook Answer</div>
        <p>
          In engineering geology and GIS (Bangar, p. 219; Chang, Ch. 11), spatial datasets represent real-world entities through a synthesis of <strong>quantitative coordinates (numeric)</strong> and <strong>descriptive classifications (alphabetic)</strong>:
        </p>
        <ol>
          <li>Geographic coordinates, cell values, lengths, and assay values are strictly numerical.</li>
          <li>Geological formation names, stratigraphy, structural classes, and administrative labels are alphabetical text strings.</li>
        </ol>
        <p>Because geoprocessing algorithms process both geometric coordinates and corresponding attribute tables simultaneously, the input format is comprehensively defined as <strong>Alphanumeric</strong>.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Numeric — Incomplete (Ignores Descriptive Attributes)</div>
        <p>
          Selecting "Numeric" accounts only for spatial coordinates, elevation models, or numeric measurements, while completely disregarding text attributes such as rock type ("Granite"), fault sense ("Thrust"), or stratigraphy ("Gondwana"). Pure numeric data cannot represent categorical GIS layers without text descriptors.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Alphabet — Incomplete (Ignores Spatial Coordinates)</div>
        <p>
          Selecting "Alphabet" accounts only for descriptive labels and ignores metric $(X, Y)$ coordinate locations, lengths, elevations, and quantitative measurements. A GIS cannot perform spatial geoprocessing without numeric coordinates.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Datasheet — Confuses Container Format with Data Nature</div>
        <p>
          A "datasheet" (or spreadsheet) is a tabular storage layout or software interface (such as a CSV or Excel file), not the inherent nature of the data itself. The question asks for the fundamental linguistic/numeric type of the input data, which is alphanumeric.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Data Types in GIS Geoprocessing Databases</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Field Data Type</th>
            <th>Category</th>
            <th>Storage Range / Format</th>
            <th>Representative Geological Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Text / String</strong></td>
            <td>Alphabetic / Alphanumeric</td>
            <td>Variable length alphanumeric characters</td>
            <td>Rock name (<em>"Khondalite"</em>), Chronostratigraphy (<em>"Palaeoproterozoic"</em>), Borehole ID (<em>"BH-OD-21"</em>).</td>
          </tr>
          <tr>
            <td><strong>Double / Float</strong></td>
            <td>Numeric</td>
            <td>64-bit IEEE floating point decimal</td>
            <td>Iron ore grade ($64.25\%$), specific gravity ($2.68$), UTM Easting ($452100.5\text{ m}$).</td>
          </tr>
          <tr>
            <td><strong>Long Integer</strong></td>
            <td>Numeric</td>
            <td>32-bit signed integer ($-2 \times 10^9 \text{ to } +2 \times 10^9$)</td>
            <td>Feature ID ($\text{FID}$), Population count, Topographic elevation in millimeters.</td>
          </tr>
          <tr>
            <td><strong>Date / Time</strong></td>
            <td>Alphanumeric (Formatted)</td>
            <td>Standard timestamp (YYYY-MM-DD hh:mm:ss)</td>
            <td>Date of drill hole completion, seismic event origin time.</td>
          </tr>
          <tr>
            <td><strong>Geometry (SHAPE)</strong></td>
            <td>Numeric (Coordinate arrays)</td>
            <td>Ordered sequence of binary coordinate vertices</td>
            <td>Polyline coordinate chains for fault traces, polygon boundary rings for mineral concessions.</td>
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
        <strong>Problem 1: Boolean SQL Attribute Query on Geological Concessions</strong><br>
        A state mining department's GIS attribute table contains $1200\text{ mining concession polygons}$. A spatial query is executed using the SQL expression:
        $$\text{SELECT * FROM Leases WHERE (Mineral = 'Bauxite') AND (Reserve\_MT } \ge 10.0\text{) AND (Status = 'Operating')}$$
        If $150\text{ polygons}$ have <code>Mineral = 'Bauxite'</code>, of which $60$ have reserves $\ge 10.0\text{ MT}$, and among these, $45$ have <code>Status = 'Operating'</code>, calculate: (a) the number of selected polygons, and (b) identify the alphanumeric data types of the three query fields.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Number of selected polygons: Applying the intersection of the three conditions sequentially:
          $$N_{\text{selected}} = 45\text{ polygons}$$
          2. Alphanumeric Data Types:
          <ul>
            <li><code>Mineral</code>: Text / String (Alphabetic descriptor).</li>
            <li><code>Reserve_MT</code>: Float / Double (Numeric quantitative value).</li>
            <li><code>Status</code>: Text / String (Alphabetic categorical state).</li>
          </ul>
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Geoprocessing Dissolve Tool & Areal Aggregation</strong><br>
        A regional geological map contains 85 individual polygon patches of granite batholiths divided into three alphanumeric lithological classes:
        Class A ("Porphyritic Granite"): $30\text{ polygons}$, total area = $140.0\text{ km}^2$;
        Class B ("Microgranite"): $25\text{ polygons}$, total area = $65.0\text{ km}^2$;
        Class C ("Granodiorite"): $30\text{ polygons}$, total area = $115.0\text{ km}^2$.
        A geoprocessing <strong>Dissolve</strong> operation is executed with <code>Dissolve_Field = 'Lithology'</code>. Calculate: (a) the number of polygons in the output feature class, and (b) the area of the dissolved Porphyritic Granite feature.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. The Dissolve geoprocessing tool aggregates all contiguous and non-contiguous features sharing the identical alphanumeric attribute value into a single multi-part polygon feature:
          $$\text{Number of output features} = \text{Number of unique attribute categories} = 3\text{ polygons}$$
          2. The total area of the dissolved "Porphyritic Granite" feature is the sum of its constituents:
          $$A_{\text{Class A}} = 140.0\text{ km}^2$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Environmental Buffer Geoprocessing Calculation</strong><br>
        A mining safety regulation mandates that no open-cast blasting can occur within $500\text{ meters}$ of any river centerline. In a GIS geoprocessing model, a $12.0\text{ km}$ long straight river segment (1D polyline) is buffered with <code>Distance = 500 m</code> (both sides, rounded ends). Calculate the total surface area of the buffer polygon in square kilometers.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Rectangular body of the buffer (length $L = 12.0\text{ km} = 12,000\text{ m}$, width $W = 2 \times 500\text{ m} = 1000\text{ m}$):
          $$A_{\text{rect}} = L \times 2R = 12,000\text{ m} \times 1000\text{ m} = 12,000,000\text{ m}^2 = 12.0\text{ km}^2$$
          2. Two semi-circular rounded ends form one complete circle of radius $R = 500\text{ m}$:
          $$A_{\text{ends}} = \pi R^2 = \pi \times (500\text{ m})^2 = 250,000 \pi \approx 785,398\text{ m}^2 \approx 0.7854\text{ km}^2$$
          3. Total geoprocessing buffer area:
          $$A_{\text{total}} = 12.0 + 0.7854 = 12.7854\text{ km}^2$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Spatial Intersect Attribute Table Fusion</strong><br>
        An exploratory borehole layer (Layer A, Point features) with 5 attribute columns is geoprocessed using the <strong>Intersect</strong> tool with a geological formation layer (Layer B, Polygon features) containing 8 attribute columns. The common unique identifier is preserved, and standard coordinate columns ($\text{Shape\_Length, Shape\_Area}$) are recalculated. Determine the total number of attribute columns in the output attribute table.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. The Intersect geoprocessing tool performs an outer relational join of the attribute schemas:
          $$\text{Columns}_{\text{output}} = \text{Columns}_A + \text{Columns}_B + 1 (\text{FID\_B})$$
          $$5 + 8 + 1 = 14\text{ attribute columns}$$
          Every point feature now carries its original borehole assay data plus the lithology, stratigraphy, and age of the intersecting polygon.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Raster Map Algebra Conditional Expression (Con)</strong><br>
        A digital raster elevation model ($\text{DEM}$) of cell size $30\text{ m} \times 30\text{ m}$ is evaluated for potential landslide hazard using the Map Algebra conditional statement:
        $$\text{Output\_Grid} = \text{Con}(\text{Slope\_Deg} > 35, 1, 0)$$
        If an upland catchment consists of $50,000\text{ total cells}$, of which $6,500\text{ cells}$ have slope angles $> 35^\circ$, calculate: (a) the total area identified as high hazard in hectares, and (b) the percentage of the catchment classified as hazardous.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Area of one raster cell:
          $$A_{\text{cell}} = 30\text{ m} \times 30\text{ m} = 900\text{ m}^2$$
          2. Total hazardous area ($6,500\text{ cells}$ assigned value 1):
          $$A_{\text{hazard}} = 6500 \times 900\text{ m}^2 = 5,850,000\text{ m}^2$$
          Convert to hectares:
          $$A_{\text{hazard}} = \frac{5,850,000\text{ m}^2}{10,000\text{ m}^2\text{/ha}} = 585.0\text{ hectares}$$
          3. Catchment percentage:
          $$\% \text{ Hazard} = \left(\frac{6500}{50,000}\right) \times 100\% = 13.0\%$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Spatial Join Aggregation: Summarizing Borehole Assays per Concession</strong><br>
        A mining block polygon contains 12 exploratory boreholes. The alphanumeric attribute table contains a numeric field <code>Fe_Pct</code>. The values for the 12 boreholes are:
        $$58.2, 60.1, 61.5, 62.0, 62.4, 63.0, 63.5, 64.0, 64.2, 64.8, 65.1, 65.6$$
        A <strong>Spatial Join</strong> geoprocessing tool is executed with the merge rule set to <code>MEAN</code>. Calculate the composite average iron grade assigned to the concession polygon.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Sum of iron grades:
          $$\sum = 58.2 + 60.1 + 61.5 + 62.0 + 62.4 + 63.0 + 63.5 + 64.0 + 64.2 + 64.8 + 65.1 + 65.6 = 754.4\%$$
          2. Arithmetic mean:
          $$\text{Mean Fe Grade} = \frac{754.4}{12} \approx 62.87\%$$
          The concession polygon's attribute table is updated with <code>Mean_Fe = 62.87%</code>.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Clip Tool Geometric Boundary Truncation</strong><br>
        An extensive quartz reef (1D polyline of total length $L = 15.0\text{ km}$) trends across three administrative taluks. A geologist clips the reef layer using the polygon boundary of Taluk "A". The length of the clipped reef polyline within Taluk "A" is measured by the GIS as $6.4\text{ km}$. Calculate the percentage of the reef that falls outside Taluk "A".
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Length outside Taluk "A":
          $$L_{\text{outside}} = 15.0\text{ km} - 6.4\text{ km} = 8.6\text{ km}$$
          2. Percentage outside:
          $$\% \text{ Outside} = \left(\frac{8.6}{15.0}\right) \times 100\% = 57.33\%$$
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Automated Geoprocessing Model Execution Complexity</strong><br>
        An automated Python/ArcPy geoprocessing model iterates through 24 district geological shapefiles. For each district, the model performs: (1) Buffer ($t_1 = 4.0\text{ s}$), (2) Clip ($t_2 = 6.0\text{ s}$), and (3) Dissolve ($t_3 = 5.0\text{ s}$). Calculate the total execution runtime of the script in minutes.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Processing time per district:
          $$t_{\text{district}} = t_1 + t_2 + t_3 = 4.0 + 6.0 + 5.0 = 15.0\text{ seconds}$$
          2. Total time for 24 districts:
          $$T_{\text{total}} = 24 \times 15.0\text{ s} = 360\text{ seconds}$$
          Convert to minutes:
          $$T_{\text{total}} = \frac{360\text{ s}}{60\text{ s/min}} = 6.0\text{ minutes}$$
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=134,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q134_Geoprocessing_Alphanumeric_Inputs_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q134: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q134()
