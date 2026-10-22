#!/usr/bin/env python3
"""
Q139 Generator: Spatial Databases & Geodatabase Architecture
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q139():
    title = r"Q139: GIS & Spatial Databases: The Geodatabase Architecture | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q139: Spatial Database Architecture: The Geodatabase as the Engine of Modern GIS"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 139<br>
<strong>Authoritative References:</strong> Philippe Rigaux, Michel Scholl, and Agnes Voisard, <em>Spatial Databases: With Application to GIS</em> (Morgan Kaufmann); Shashi Shekhar and Sanjay Chawla, <em>Spatial Databases: A Tour</em> (Prentice Hall); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS, p. 224); ESRI Press, <em>Understanding the Geodatabase Architecture</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITIONS AND GEODATABASE ARCHITECTURE -->
  <div class="card">
    <div class="card-header bg-blue">1. Architecture of Spatial Data Management: The Geodatabase</div>
    <div class="card-body">
      <p>
        In Geographic Information Science (GIScience), enterprise data modeling, and spatial database management, <strong>spatial databases that store, manage, and query geographic datasets within a unified relational or object-relational framework are universally known as Geodatabases</strong> (Rigaux et al., 2002; Shekhar & Chawla, 2003; Bangar, p. 224).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q139/geodatabase_spatial_database_architecture.png" alt="Geodatabase Spatial Database Architecture">
        <div class="figure-caption">
          <strong>Figure 139.1 — Object-Relational Geodatabase Architecture:</strong> Integration of spatial geometries (points, lines, polygons, rasters, and 3D TINs) directly inside relational tables alongside alphanumeric attributes, managed by standard Spatial SQL extensions (PostGIS, Oracle Spatial) and accelerated by R-tree spatial indexing.
        </div>
      </div>

      <h4>What is a Geodatabase?</h4>
      <p>
        The term <strong>geodatabase</strong> (short for <em>geographical database</em>) represents the premier native data model of modern GIS:
      </p>
      <ul>
        <li><strong>Unified Storage:</strong> In legacy GIS (such as shapefiles or CAD files), spatial coordinate geometry was stored in separate binary graphics files while non-spatial attributes were stored in external dBase tables (.dbf). A geodatabase unites geometry and attributes inside a single object-relational database management system (ORDBMS).</li>
        <li><strong>Spatial Data Types:</strong> Geometry is stored directly in dedicated spatial columns as binary BLOBs compliant with the Open Geospatial Consortium (OGC) Simple Feature Access standard (e.g., <code>ST_Geometry</code>, <code>GEOMETRY</code>, or Well-Known Binary, WKB).</li>
        <li><strong>Spatial Indexing:</strong> Incorporates specialized multi-dimensional spatial indexes (such as <strong>R-trees, Quadtrees, or Hilbert space-filling curves</strong>) that allow the database to query millions of spatial records in milliseconds using spatial predicates (e.g., <code>ST_Intersects</code>, <code>ST_Contains</code>, <code>ST_Within</code>).</li>
        <li><strong>Intelligent Integrity Rules:</strong> Enforces business rules, attribute validation domains (e.g., permissible iron grades $45.0 - 68.5\%$), subtypes, topological connectivity rules, and network tracing models.</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q139/bangar_p224_spatial_databases_geodatabase.png" alt="Spatial Databases and Geodatabase from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 139.2 — Spatial Databases in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 224). Explicitly confirms: <em>"Spatial databases are also known as geodatabases."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: TYPES OF GEODATABASES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Structural Classification: Personal, File, and Enterprise Geodatabases</div>
    <div class="card-body">
      <p>
        In professional geological survey organizations (such as the Geological Survey of India, GSI, and state mining directorates), three architectural tiers of geodatabases are deployed:
      </p>
      <table class="table">
        <thead>
          <tr>
            <th>Geodatabase Type</th>
            <th>Underlying Database Engine</th>
            <th>Storage Capacity</th>
            <th>Multi-User / Concurrency Support</th>
            <th>Primary Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>File Geodatabase (FGDB)</strong></td>
            <td>Proprietary high-performance folder of binary files</td>
            <td><strong>$1\text{ TB}$ per table</strong> (expandable to $256\text{ TB}$)</td>
            <td>Single-editor; multiple simultaneous readers.</td>
            <td>Standard desktop GIS project storage, high-speed regional geological mapping.</td>
          </tr>
          <tr>
            <td><strong>Enterprise Geodatabase (Multi-user)</strong></td>
            <td>RDBMS engines (PostgreSQL/PostGIS, Oracle Spatial, Microsoft SQL Server)</td>
            <td><strong>Unlimited</strong> (governed by server disk array)</td>
            <td><strong>Full multi-user concurrent editing</strong> with versioning, long transactions, and replication.</td>
            <td>National mineral inventories, statewide mining cadastre, real-time disaster management portals.</td>
          </tr>
          <tr>
            <td><strong>Personal Geodatabase (Legacy)</strong></td>
            <td>Microsoft Access Jet Engine (.mdb)</td>
            <td>$2.0\text{ GB}$ total limit</td>
            <td>Single-user only.</td>
            <td>Historical legacy projects (deprecated in modern 64-bit GIS).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 3: SPATIAL SQL AND GEODATABASE QUERIES -->
  <div class="card">
    <div class="card-header bg-indigo">3. Spatial SQL Operators in Geodatabase Management</div>
    <div class="card-body">
      <h4>Spatial Predicates and Topological Operators</h4>
      <p>
        Modern geodatabases leverage Spatial SQL (ISO/IEC 13249-3) to perform computational geometry directly inside SQL queries:
      </p>
      <div class="math-block">
        $$\text{SQL: } \text{SELECT L.Lease\_ID, L.Mineral, ST\_Area(L.geom) / 10000 AS Area\_Hectares}$$
        $$\text{FROM Mining\_Leases L, Protected\_Forest P}$$
        $$\text{WHERE ST\_Intersects(L.geom, P.geom) = TRUE;}$$
      </div>
      <p>
        This query executes an instantaneous spatial intersection check between thousands of mining polygon boundaries and protected forest reserves without requiring manual graphic overlays.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 139</div>
      <div class="question-text">
        Spatial databases are also known as :
      </div>
      <ul class="option-list">
        <li class="option-item correct"><strong>(A)</strong> Geodatabase</li>
        <li class="option-item"><strong>(B)</strong> Mono database</li>
        <li class="option-item"><strong>(C)</strong> Concurrent database</li>
        <li class="option-item"><strong>(D)</strong> None of these</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (A) Geodatabase</strong> — By universal terminology in GIS and spatial computing (Bangar, p. 224; Rigaux et al.; ESRI), spatial databases designed for storing geographic information are known as <strong>Geodatabases</strong>.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option correct">
        <div class="option-title">Option (A): Geodatabase — Fully Verified & Universal Industry Standard</div>
        <p>
          A <strong>Geodatabase</strong> is the definitive textbook and industry term for a spatial database (Bangar, p. 224; Shekhar & Chawla; Rigaux et al.). It is a relational database management system (RDBMS) extended with spatial data types, spatial indexing, topological relationships, and spatial querying capabilities to store geographic geometries alongside alphanumeric attributes.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Mono database — Fabricated Distractor</div>
        <p>
          "Mono database" is a completely fictitious term fabricated as an examination distractor. It has no meaning in spatial data management or computer science.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Concurrent database — General Computer Science Concept</div>
        <p>
          "Concurrent database" refers to any multi-threaded database system that allows multiple users or transactions to read and write records simultaneously using ACID locking protocols (concurrency control). It describes an operational transaction mechanism, not a spatial database designed for geographic data.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): None of these — Incorrect Choice</div>
        <p>
          Because Option (A) is the exact, authoritative definition, Option (D) is incorrect.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Architecture: Traditional Databases vs. Spatial Geodatabases</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>System Feature</th>
            <th>Standard Relational Database (RDBMS)</th>
            <th>Spatial Database / Geodatabase</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Supported Data Types</strong></td>
            <td>Numbers, text strings, dates, booleans, blobs.</td>
            <td>All standard types + <strong>Spatial geometries: Points, Lines, Polygons, Multipoints, GeometryCollections, Rasters.</strong></td>
          </tr>
          <tr>
            <td><strong>Indexing Mechanisms</strong></td>
            <td>1D B-tree, Hash index.</td>
            <td><strong>2D/3D Multi-dimensional Spatial Indexes: R-Tree, R*-Tree, Quadtree, Hilbert curves.</strong></td>
          </tr>
          <tr>
            <td><strong>Standard Query Language</strong></td>
            <td>Standard SQL (e.g. <code>WHERE Salary > 50000</code>).</td>
            <td><strong>Spatial SQL (OGC / ISO SQL/MM):</strong> <code>ST_Buffer, ST_Distance, ST_Intersects, ST_Contains</code>.</td>
          </tr>
          <tr>
            <td><strong>Topological Integrity</strong></td>
            <td>Relational foreign keys and unique constraints.</td>
            <td>Enforces spatial rules: "Must not overlap", "Must be inside", "Must not have dangles".</td>
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
        <strong>Problem 1: PostGIS Spatial SQL Query for Mineral Exploration</strong><br>
        A mining exploration geodatabase contains two tables: <code>boreholes</code> (Point geometry, field <code>fe_grade</code>) and <code>lithology</code> (Polygon geometry, field <code>rock_type</code>). Write the standard PostGIS Spatial SQL query to select all boreholes with an iron grade $> 60.0\%$ that fall geographically inside polygons classified as <em>"Banded Iron Formation"</em>.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          ```sql
          SELECT B.borehole_id, B.fe_grade, L.rock_type, B.geom
          FROM boreholes B
          JOIN lithology L
            ON ST_Within(B.geom, L.geom)
          WHERE B.fe_grade > 60.0
            AND L.rock_type = 'Banded Iron Formation';
          ```
          <em>Technical Explanation:</em> The spatial predicate function <code>ST_Within(B.geom, L.geom)</code> utilizes the spatial R-tree index on the geodatabase tables to evaluate point-in-polygon containment instantaneously.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: R-Tree Spatial Index Bounding Box Filtering</strong><br>
        An R-Tree spatial index organizes spatial objects by their Minimum Bounding Boxes (MBR: $[X_{\text{min}}, Y_{\text{min}}, X_{\text{max}}, Y_{\text{max}}]$). A query box $Q = [100, 100, 200, 200]$ is executed against four feature MBRs:
        MBR 1: $[50, 50, 90, 90]$;
        MBR 2: $[150, 150, 180, 180]$;
        MBR 3: $[190, 190, 250, 250]$;
        MBR 4: $[300, 300, 400, 400]$.
        Identify which features pass the primary filter stage of the spatial index.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Condition for two 2D bounding boxes to intersect:
          $$\text{Intersect} \iff (X_{\text{min1}} \le X_{\text{max2}}) \land (X_{\text{max1}} \ge X_{\text{min2}}) \land (Y_{\text{min1}} \le Y_{\text{max2}}) \land (Y_{\text{max1}} \ge Y_{\text{min2}})$$
          2. Check each candidate against $Q[100, 100, 200, 200]$:
          - MBR 1: $X_{\text{max}} = 90 < 100$ &rarr; <strong>No overlap</strong> (Completely outside to West).
          - MBR 2: $[150, 150, 180, 180]$ &rarr; Lies entirely within $[100, 100, 200, 200]$ &rarr; <strong>Passes primary filter!</strong>
          - MBR 3: Overlaps from $[190, 190]$ to $[200, 200]$ &rarr; <strong>Passes primary filter!</strong>
          - MBR 4: $X_{\text{min}} = 300 > 200$ &rarr; <strong>No overlap</strong> (Completely outside to East).
          Features 2 and 3 pass the primary filter and proceed to the exact geometric test stage.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Storage Capacity Scaling: Shapefile vs. File Geodatabase</strong><br>
        A statewide high-resolution LiDAR elevation dataset contains $18\text{ GB}$ of vector point records. (a) Can this dataset be stored in a single conventional ESRI Shapefile? (b) Can it be stored in a standard File Geodatabase (FGDB)?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Shapefile Assessment: Conventional shapefiles use a 32-bit offset index file (.shx) which imposes a strict physical file size limit of <strong>$2.0\text{ GB}$</strong> per component file (.shp, .dbf). Attempting to load $18\text{ GB}$ results in immediate overflow error. <strong>Cannot be stored in a Shapefile.</strong>
          2. File Geodatabase Assessment: Standard File Geodatabase tables have a default maximum capacity of <strong>$1.0\text{ TB}$ ($1024\text{ GB}$)</strong> per table (and can be configured to hold up to $256\text{ TB}$). <strong>Easily accommodated in a File Geodatabase with $98\%$ headroom remaining.</strong>
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Dimensionally Extended 9-Intersection Model (DE-9IM)</strong><br>
        The DE-9IM model classifies topological relationships between geometries $A$ and $B$ by evaluating the intersection dimension ($0\text{ for point}, 1\text{ for line}, 2\text{ for area}, F\text{ for empty}$) between their Interiors ($I$), Boundaries ($B$), and Exteriors ($E$):
        $$\text{Matrix: } \begin{bmatrix} \dim(I(A) \cap I(B)) & \dim(I(A) \cap B(B)) & \dim(I(A) \cap E(B)) \\ \dim(B(A) \cap I(B)) & \dim(B(A) \cap B(B)) & \dim(B(A) \cap E(B)) \\ \dim(E(A) \cap I(B)) & \dim(E(A) \cap B(B)) & \dim(E(A) \cap E(B)) \end{bmatrix}$$
        If two mining concession polygons share only a common 1D boundary line and their interiors do not overlap, what is the value of $\dim(I(A) \cap I(B))$ and $\dim(B(A) \cap B(B))$?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. $\dim(I(A) \cap I(B)) = F$ (False / Empty set, because polygon interiors do not overlap).
          2. $\dim(B(A) \cap B(B)) = 1$ (1-Dimensional line, because they share a linear boundary).
          This matches the standard OGC topological predicate <code>ST_Touches(A, B) = TRUE</code>.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Geodatabase Attribute Domain Validation</strong><br>
        In a geodatabase schema for coal prospecting, a Range Attribute Domain named <code>Volatile_Matter_Domain</code> is defined with minimum value $12.0\%$ and maximum value $45.0\%$. A junior field geologist enters an assay value of $52.4\%$. How does the geodatabase engine respond?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          The geodatabase schema validation engine enforces domain integrity constraints. Entering $52.4\%$ violates the defined range ($12.0 - 45.0\%$). The geodatabase immediately flags a <strong>Domain Validation Error</strong> and prevents the record from being committed until a valid value within the specified range is provided.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Enterprise Geodatabase Multi-User Versioning & Reconciliation</strong><br>
        In a statewide mining administration enterprise geodatabase, two geologists concurrently edit the boundary of Lease Block "X" off the Parent <code>DEFAULT</code> version:
        - Geologist A edits Version A and posts changes at $11:00\text{ AM}$.
        - Geologist B edits Version B and attempts to post changes at $11:30\text{ AM}$.
        Describe the automated geodatabase version reconciliation process that resolves the edit collision.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. When Geologist B attempts to post, the geodatabase versioning engine detects that the <code>DEFAULT</code> version has been modified since Version B was created.
          2. The engine executes automated <strong>Reconciliation</strong>, comparing the Delta tables (Adds and Deletes tables) of Version B against the updated <code>DEFAULT</code>.
          3. Because both editors modified the exact same feature (Lease Block "X"), a <strong>Feature-Level Conflict</strong> is flagged.
          4. The system presents the conflict to the administrator to choose between: (a) Keep Version A edits, (b) Keep Version B edits, or (c) Merge geometry interactively before completing the Post operation.
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Precision and Coordinate Storage in Modern Geodatabases</strong><br>
        A modern geodatabase stores spatial coordinates in high-precision 64-bit IEEE double floating-point numbers ($53\text{ bits of mantissa}$, providing $\approx 15 - 17\text{ significant decimal digits}$). In a UTM projection where Easting coordinates are on the order of $10^6\text{ meters}$, calculate the theoretical spatial resolution (smallest distinguishable displacement) supported by high precision.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Significant digits: 16 digits.
          2. With $1,000,000\text{ m}$ (7 digits before the decimal), there remain $16 - 7 = 9\text{ decimal places}$:
          $$\Delta s \approx 10^{-9}\text{ meters} = 1.0\text{ nanometer}$$
          Modern high-precision geodatabases can resolve spatial positions down to sub-millimeter / nanometer precision, eliminating historical snapping drift.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Geometric Network Trace for Mine Ventilation Circuit</strong><br>
        An underground manganese mine ventilation circuit is modeled as a Geometric Network inside an enterprise geodatabase consisting of 60 edge features (mine drifts, shafts) and 45 junction features (intersections, ventilation doors, exhaust fans). A trace solver is executed from the main intake portal to locate all connected downstream drifts. If one ventilation door feature has its attribute set to <code>Status = 'Closed'</code>, explain how the network solver utilizes the geodatabase connectivity table.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. The geodatabase maintains an internal binary Topological Index Table linking edge and junction identifiers.
          2. The geometric network trace algorithm traverses adjacent edges via common junction IDs.
          3. When it reaches the junction with <code>Status = 'Closed'</code>, the solver treats the junction as an active <strong>Network Barrier</strong>, halting traversal along that branch and redirecting flow exclusively through alternate connected open drifts.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=139,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q139_Spatial_Databases_Geodatabase_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q139: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q139()
