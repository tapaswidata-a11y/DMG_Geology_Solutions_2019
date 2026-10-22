#!/usr/bin/env python3
"""
Q131 Generator: GIS Vector Data Model Geometric Primitives: Points, Lines & Polygons
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q131():
    title = r"Q131: GIS & Remote Sensing: Vector Geometric Primitives | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q131: Vector Data Model: Points, Lines, and Polygons as the Triad of Earth Surface Features"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 131<br>
<strong>Authoritative References:</strong> Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (9th Ed., McGraw-Hill, Ch. 3: Vector Data Model, pp. 45–68); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS and Remote Sensing, p. 216); Paul A. Longley et al., <em>Geographic Information Science and Systems</em> (4th Ed., Wiley, Ch. 3); Peter A. Burrough and Rachael A. McDonnell, <em>Principles of Geographical Information Systems</em> (Ch. 2)."""

    part1 = r"""
  <!-- CARD 1: THE VECTOR DATA MODEL & GEOMETRIC PRIMITIVES -->
  <div class="card">
    <div class="card-header bg-blue">1. The Vector Spatial Data Model & The Universal Geometric Primitives</div>
    <div class="card-body">
      <p>
        In Geographic Information Systems (GIS), digital cartography, and spatial database management, <strong>all discrete geographic features on the Earth's surface are abstracted, modeled, and characterized using three fundamental geometric primitives: Points, Lines (Arcs), and Polygons (Areas)</strong> (Chang, 2019; Longley et al., 2015; Bangar, p. 216).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q131/gis_vector_primitives_point_line_polygon.png" alt="GIS Vector Primitives: Point, Line, Polygon">
        <div class="figure-caption">
          <strong>Figure 131.1 — The Vector Geometric Primitives Hierarchy:</strong> 0-Dimensional Points (single coordinate pairs $[X, Y]$ representing wells, spot heights), 1-Dimensional Lines/Polylines (ordered coordinate chains $[X_1, Y_1] \rightarrow [X_n, Y_n]$ representing rivers, roads, fault traces), and 2-Dimensional Polygons (closed loops with identical start and end vertices enclosing spatial areas like geological formations, lakes, and mining leases).
        </div>
      </div>

      <h4>Mathematical & Topological Formalization of Primitives</h4>
      <p>
        According to the Open Geospatial Consortium (OGC) Simple Feature Access specification and ISO 19107:
      </p>
      <ul>
        <li>
          <strong>Point Features (0-Dimensional, $\text{dim} = 0$):</strong>
          Defined mathematically by a single coordinate pair $(X, Y)$ in a specified projected coordinate system (or latitude/longitude in geographic coordinates). A point has zero length, zero width, and zero surface area. Used to represent entities whose spatial extent is negligible at the map scale:
          <em>Geological examples:</em> exploratory boreholes, water wells, seismic recording stations, mineral sample locations, strike-and-dip measurement points, mine shaft portals.
        </li>
        <li>
          <strong>Line / Polyline Features (1-Dimensional, $\text{dim} = 1$):</strong>
          Defined mathematically by an ordered sequence of connected coordinate vertices $(X_1, Y_1), (X_2, Y_2), \dots, (X_n, Y_n)$ with distinct starting and ending nodes. A line possesses length and direction, but zero surface area.
          <em>Geological examples:</em> geological fault traces, thrust planes, anticlinal fold axes, dykes, river streams, contour lines, railway tracks, seismic survey profile lines.
        </li>
        <li>
          <strong>Polygon Features (2-Dimensional, $\text{dim} = 2$):</strong>
          Defined mathematically by a closed boundary composed of a sequence of lines where the first vertex coincides exactly with the last vertex: $(X_1, Y_1) \equiv (X_n, Y_n)$. A polygon possesses perimeter, perimeter vertices, and enclosed surface area.
          <em>Geological examples:</em> geological lithological formations, granite batholith outcrops, mining concessions, drainage basins / watersheds, national parks, surface lakes, ore bodies.
        </li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q131/bangar_p216_gis_vector_features_points_lines_polygons.png" alt="GIS Geographic Features from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 131.2 — Geographic Feature Representation in GIS:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 216). Confirms: <em>"All geographic features on the Earth's surface can be characterized and defined as point feature, line feature, or polygon feature."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SCALE-DEPENDENT ABSTRACTION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Cartographic Scale-Dependence & Multi-Scale Feature Abstraction</div>
    <div class="card-body">
      <h4>Cartographic Generalization and Dimension Transition</h4>
      <p>
        The assignment of a geographic entity to a point, line, or polygon primitive is not an inherent static property of the real-world object; it is fundamentally governed by the <strong>cartographic map scale</strong> (Burrough & McDonnell, 1998):
      </p>
      <table class="table">
        <thead>
          <tr>
            <th>Real-World Geographic Entity</th>
            <th>Large-Scale Map (e.g. $1 : 1,000$ to $1 : 5,000$)</th>
            <th>Medium-Scale Map (e.g. $1 : 50,000$)</th>
            <th>Small-Scale Regional Map (e.g. $1 : 1,000,000$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>City / Urban Settlement</strong></td>
            <td>Complex mosaic of Polygons (individual building footprints, city blocks).</td>
            <td>Single large boundary Polygon.</td>
            <td>Single dimensionless Point feature with city center coordinates.</td>
          </tr>
          <tr>
            <td><strong>River / Estuary System</strong></td>
            <td>Double-line Polygon representing open water surface and banks.</td>
            <td>Single-line Polyline feature.</td>
            <td>Simplified Polyline or omitted entirely if below threshold.</td>
          </tr>
          <tr>
            <td><strong>Kimberlite Pipe / Mineral Deposit</strong></td>
            <td>Detailed oval Polygon outlining contact metamorphic aureole.</td>
            <td>Small circular Polygon.</td>
            <td>Single Point feature with symbol denoting commodity.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 3: TOPOLOGY AND ATTRIBUTE LINKAGE -->
  <div class="card">
    <div class="card-header bg-indigo">3. Topological Relationships & Relational Attribute Coupling</div>
    <div class="card-body">
      <h4>The Dual Architecture: Spatial Coordinates + Attribute Tables</h4>
      <p>
        The power of the vector data model stems from the seamless relational coupling between the geometric primitives and tabular attribute databases:
      </p>
      <ul>
        <li><strong>Topology:</strong> The mathematical language of geometric spatial relationships (adjacency, connectivity, and containment) that remains invariant under rubber-sheeting, rotation, or projection:
          <ul>
            <li><em>Adjacency / Contiguity:</em> Which rock polygons share a common fault boundary (Polygon Topology).</li>
            <li><em>Connectivity:</em> How stream line segments connect at river junctions (Arc-Node Topology).</li>
            <li><em>Containment:</em> Which groundwater monitoring wells fall inside a specific basalt aquifer polygon (Point-in-Polygon).</li>
          </ul>
        </li>
        <li><strong>Relational Attribute Table:</strong> Every single point, line, or polygon carries a unique Feature Identifier ($\text{FID}$ or $\text{ObjectID}$) linked directly to a row in an attribute table storing geological properties (rock type, age, mineral grade, permeability, owner).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 131</div>
      <div class="question-text">
        All geographic features on the Earth’s surface can be characterized and defined as :
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Point feature</li>
        <li class="option-item"><strong>(B)</strong> Line feature</li>
        <li class="option-item"><strong>(C)</strong> Polygon feature</li>
        <li class="option-item correct"><strong>(D)</strong> All of these</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (D) All of these</strong> — In the GIS vector data model, all real-world geographical entities on Earth are collectively represented by the three universal geometric primitives: Points (0D), Lines (1D), and Polygons (2D).
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Point feature — Incomplete (Only One Primitive)</div>
        <p>
          Point features represent zero-dimensional geographic entities characterized by a single $(X, Y)$ coordinate pair (e.g., wells, mine shafts, spot elevations). While points are fundamental primitives, they cannot represent linear networks (faults, streams) or areal expanses (lithological formations, lakes). Selecting only Option (A) is incomplete and incorrect.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Line feature — Incomplete (Only One Primitive)</div>
        <p>
          Line (or polyline) features represent one-dimensional linear entities characterized by an ordered chain of coordinates with length and direction (e.g., dykes, anticlinal fold hinges, highways). Lines cannot capture point entities or enclosed geographic areas. Selecting only Option (B) is incomplete and incorrect.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Polygon feature — Incomplete (Only One Primitive)</div>
        <p>
          Polygon features represent two-dimensional enclosed regions with measurable perimeters and areas (e.g., sedimentary basins, batholiths, mining concessions). Selecting only Option (C) ignores points and lines and is therefore incomplete.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (D): All of these — Fully Verified & Comprehensive Answer</div>
        <p>
          In Geographic Information Systems and vector spatial modeling (Chang, 2019; Bangar, p. 216), Earth's surface features are exhaustively classified into the triad of <strong>Points, Lines, and Polygons</strong>:
        </p>
        <ol>
          <li>Points represent discrete location-based entities ($0\text{D}$).</li>
          <li>Lines represent linear, directional, and networked entities ($1\text{D}$).</li>
          <li>Polygons represent contiguous, enclosed surface territories ($2\text{D}$).</li>
        </ol>
        <p>Therefore, Option (D) encompasses the complete foundational geometry of GIS vector data modeling.</p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">The Vector Geometric Primitives: Technical Characteristics and Geological Examples</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Geometric Primitive</th>
            <th>Topological Dimension</th>
            <th>Coordinate Structure</th>
            <th>Geometric Attributes</th>
            <th>Representative Geological Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Point Feature</strong></td>
            <td>0-Dimensional ($\text{dim} = 0$)</td>
            <td>Single coordinate pair: $[X, Y]$</td>
            <td>Location coordinates $(X, Y, Z)$; zero length, zero area.</td>
            <td>Exploratory boreholes, water wells, earthquake epicenters, mineral sample sites, mine adits.</td>
          </tr>
          <tr>
            <td><strong>Line / Polyline Feature</strong></td>
            <td>1-Dimensional ($\text{dim} = 1$)</td>
            <td>Ordered sequence of vertices: $[X_1, Y_1] \rightarrow [X_n, Y_n]$</td>
            <td>Length, direction, sinuosity, flow orientation; zero area.</td>
            <td>Geological faults, thrust contacts, fold hinge traces, dolerite dykes, contour lines, seismic reflection profiles.</td>
          </tr>
          <tr>
            <td><strong>Polygon / Area Feature</strong></td>
            <td>2-Dimensional ($\text{dim} = 2$)</td>
            <td>Closed loop where start equals end: $[X_1, Y_1] \equiv [X_n, Y_n]$</td>
            <td>Enclosed surface area, perimeter, centroid coordinates $(X_c, Y_c)$.</td>
            <td>Stratigraphic lithologies, granite plutons, mining leases, alluvial floodplains, groundwater basins.</td>
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
        <strong>Problem 1: Polyline Length Calculation from Vertex Coordinates</strong><br>
        A geological fault trace is digitized as a 2D vector polyline with four consecutive vertices in a projected UTM coordinate system (coordinates in meters):
        $$V_1 = (450000, 2430000), \quad V_2 = (453000, 2434000), \quad V_3 = (456000, 2438000), \quad V_4 = (460000, 2441000)$$
        Calculate the total ground length of the fault trace in kilometers.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Euclidean length for each segment ($\Delta L_i = \sqrt{\Delta X_i^2 + \Delta Y_i^2}$):
          $$\text{Segment 1-2: } \Delta X = 453000 - 450000 = 3000\text{ m}, \quad \Delta Y = 2434000 - 2430000 = 4000\text{ m}$$
          $$L_{12} = \sqrt{3000^2 + 4000^2} = \sqrt{9,000,000 + 16,000,000} = \sqrt{25,000,000} = 5000\text{ m}$$
          $$\text{Segment 2-3: } \Delta X = 456000 - 453000 = 3000\text{ m}, \quad \Delta Y = 2438000 - 2434000 = 4000\text{ m}$$
          $$L_{23} = \sqrt{3000^2 + 4000^2} = 5000\text{ m}$$
          $$\text{Segment 3-4: } \Delta X = 460000 - 456000 = 4000\text{ m}, \quad \Delta Y = 2441000 - 2438000 = 3000\text{ m}$$
          $$L_{34} = \sqrt{4000^2 + 3000^2} = 5000\text{ m}$$
          2. Total polyline length:
          $$L_{\text{total}} = L_{12} + L_{23} + L_{34} = 5000 + 5000 + 5000 = 15,000\text{ m} = 15.0\text{ km}$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Polygon Enclosed Area via Surveyor's / Shoelace Formula</strong><br>
        A mining concession polygon has four corner vertices in UTM coordinates (meters):
        $$A = (1000, 1000), \quad B = (4000, 1000), \quad C = (5000, 4000), \quad D = (1000, 4000)$$
        Calculate the enclosed surface area in hectares ($1\text{ ha} = 10,000\text{ m}^2$) using the Shoelace (Gauss Area) algorithm.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Apply the Shoelace algorithm:
          $$\text{Area} = \frac{1}{2} |(X_A Y_B - Y_A X_B) + (X_B Y_C - Y_B X_C) + (X_C Y_D - Y_C X_D) + (X_D Y_A - Y_D X_A)|$$
          2. Compute cross-products:
          $$X_A Y_B - Y_A X_B = (1000 \times 1000) - (1000 \times 4000) = 1,000,000 - 4,000,000 = -3,000,000$$
          $$X_B Y_C - Y_B X_C = (4000 \times 4000) - (1000 \times 5000) = 16,000,000 - 5,000,000 = +11,000,000$$
          $$X_C Y_D - Y_C X_D = (5000 \times 4000) - (4000 \times 1000) = 20,000,000 - 4,000,000 = +16,000,000$$
          $$X_D Y_A - Y_D X_A = (1000 \times 1000) - (4000 \times 1000) = 1,000,000 - 4,000,000 = -3,000,000$$
          3. Sum terms:
          $$\sum = -3,000,000 + 11,000,000 + 16,000,000 - 3,000,000 = 21,000,000\text{ m}^2$$
          $$\text{Area} = \frac{1}{2} |21,000,000| = 10,500,000\text{ m}^2$$
          4. Convert to hectares:
          $$\text{Area} = \frac{10,500,000\text{ m}^2}{10,000\text{ m}^2\text{/ha}} = 1050\text{ hectares}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Centroid Calculation of a Triangular Geological Outcrop Polygon</strong><br>
        A triangular outcrop of pegmatite has three vertex coordinates:
        $V_1 = (500, 200)$, $V_2 = (1100, 600)$, and $V_3 = (800, 1000)$.
        Calculate the spatial centroid coordinates $(X_c, Y_c)$ where a label symbol should be placed automatically by the GIS.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Centroid of a triangle is the arithmetic mean of its vertices:
          $$X_c = \frac{X_1 + X_2 + X_3}{3} = \frac{500 + 1100 + 800}{3} = \frac{2400}{3} = 800.0\text{ m}$$
          $$Y_c = \frac{Y_1 + Y_2 + Y_3}{3} = \frac{200 + 600 + 1000}{3} = \frac{1800}{3} = 600.0\text{ m}$$
          The centroid coordinates are $(800.0, 600.0)$.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Topological Euler Formula for Planar GIS Networks</strong><br>
        In a topological vector layer of geological quadrangle maps, Euler's planar graph formula relates the number of Vertices ($V$), Edges/Arcs ($E$), and Polygons/Faces ($F$, including the infinite exterior background face):
        $$V - E + F = 2$$
        A mapped district contains $45\text{ boundary nodes (vertices)}$ and $62\text{ geological contact arcs (edges)}$. Calculate the number of distinct geological formations (interior polygons) mapped in the district.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Solve for total faces $F$:
          $$F = 2 - V + E = 2 - 45 + 62 = 19\text{ faces}$$
          2. The total faces $F$ include the single unbounded exterior face (the area outside the map boundary).
          3. Number of interior geological polygons:
          $$F_{\text{interior}} = F - 1 = 19 - 1 = 18\text{ geological formations (polygons)}$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Point-in-Polygon (Ray-Casting Algorithm) Test</strong><br>
        A groundwater monitoring well has coordinates $P = (5, 5)$. A potential contamination contaminant plume is modeled as a polygon with vertices:
        $A = (2, 2)$, $B = (8, 2)$, $C = (8, 8)$, $D = (2, 8)$.
        A horizontal ray is cast from $P(5, 5)$ eastward along the $+X$ direction to infinity. Calculate the number of intersections of the ray with the polygon edges and determine whether the well lies inside the plume polygon.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Equation of the cast ray: $y = 5$ for $x \ge 5$.<br>
          2. Check intersection with each edge:
          <ul>
            <li>Edge $AB$ (from $(2,2)$ to $(8,2)$): horizontal at $y = 2$ &rarr; no intersection with $y = 5$.</li>
            <li>Edge $BC$ (from $(8,2)$ to $(8,8)$): vertical at $x = 8$, spanning $y \in [2, 8]$. The ray $y = 5$ intersects this edge at $(8, 5)$. Since $x = 8 \ge 5$, this is a valid intersection ($1\text{ intersection}$).</li>
            <li>Edge $CD$ (from $(8,8)$ to $(2,8)$): horizontal at $y = 8$ &rarr; no intersection with $y = 5$.</li>
            <li>Edge $DA$ (from $(2,8)$ to $(2,2)$): vertical at $x = 2$, spanning $y \in [2, 8]$. The line intersects at $(2, 5)$, but this is behind the ray origin ($x = 2 < 5$), so not counted.</li>
          </ul>
          3. Jordan Curve / Ray Casting Rule: An <strong>odd number of intersections (1 intersection)</strong> proves that point $P$ lies strictly <strong>INSIDE the polygon</strong>.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Vector Buffer Generation Geometry</strong><br>
        An environmental regulation mandates a protective buffer zone of radius $R = 200\text{ m}$ around a solitary groundwater borehole (represented as a 0D Point feature). (a) What geometric primitive is generated by buffering this point? (b) Calculate the surface area of the resulting buffer in square meters and hectares.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Resulting Primitive: Buffering a 0-dimensional Point feature by distance $R$ generates a <strong>2-Dimensional circular Polygon feature</strong>.
          2. Surface area of the circular polygon:
          $$\text{Area} = \pi R^2 = \pi (200\text{ m})^2 = 40,000 \pi \approx 125,663.7\text{ m}^2$$
          3. Convert to hectares:
          $$\text{Area} = \frac{125,663.7\text{ m}^2}{10,000\text{ m}^2\text{/ha}} \approx 12.57\text{ hectares}$$
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Storage Space Complexity: Vector vs. Raster</strong><br>
        A square mining concession of size $10\text{ km} \times 10\text{ km}$ ($100\text{ km}^2$) is stored in both vector and raster formats:
        (1) In vector format, the concession is stored as a 4-vertex polygon with 8 coordinate floating-point values ($8 \times 8\text{ bytes} = 64\text{ bytes}$) plus $100\text{ bytes}$ header.
        (2) In raster format with a spatial resolution of $1.0\text{ m} \times 1.0\text{ m}$, each grid cell stores 1 byte.
        Calculate the ratio of the uncompressed raster file size to the vector file size.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Vector storage size:
          $$S_{\text{vector}} = 64 + 100 = 164\text{ bytes}$$
          2. Raster grid dimensions and storage:
          $$\text{Grid size} = \left(\frac{10,000\text{ m}}{1\text{ m}}\right) \times \left(\frac{10,000\text{ m}}{1\text{ m}}\right) = 10,000 \times 10,000 = 10^8\text{ cells}$$
          $$S_{\text{raster}} = 10^8\text{ cells} \times 1\text{ byte/cell} = 100,000,000\text{ bytes} = 100\text{ MB}$$
          3. Ratio:
          $$\text{Ratio} = \frac{100,000,000\text{ bytes}}{164\text{ bytes}} \approx 609,756$$
          <em>Insight:</em> The vector polygon representation is over $600,000\times$ more compact for homogeneous boundary data than high-resolution raster grids.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Sinuosity Index of a Geological Stream Line</strong><br>
        A river channel traversing a floodplain is digitized as a polyline with a total curve length of $L_{\text{actual}} = 18.5\text{ km}$. The straight-line distance between the source node and outlet node is $L_{\text{straight}} = 10.0\text{ km}$. Calculate the Sinuosity Index ($SI = L_{\text{actual}} / L_{\text{straight}}$) and classify the stream channel (straight, sinuous, or meandering where meandering requires $SI \ge 1.50$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate Sinuosity Index:
          $$SI = \frac{L_{\text{actual}}}{L_{\text{straight}}} = \frac{18.5\text{ km}}{10.0\text{ km}} = 1.85$$
          2. Geomorphological Classification:
          Since $SI = 1.85 \ge 1.50$, the stream channel is classified as <strong>Meandering</strong>.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=131,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q131_GIS_Vector_Primitives_Points_Lines_Polygons_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q131: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q131()
