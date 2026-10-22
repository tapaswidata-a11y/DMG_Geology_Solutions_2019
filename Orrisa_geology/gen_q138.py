#!/usr/bin/env python3
"""
Q138 Generator: Spatial Data Structures: Spaghetti Vector Model vs. Raster Encodings
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q138():
    title = r"Q138: GIS & Spatial Data Structures: Spaghetti Vector Model vs. Raster | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q138: Spatial Data Structures: The Spaghetti Vector Model vs. Raster Compression Systems"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 138<br>
<strong>Authoritative References:</strong> Peter A. Burrough and Rachael A. McDonnell, <em>Principles of Geographical Information Systems</em> (Ch. 3: Spatial Data Structures, pp. 48–74); Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (9th Ed., Ch. 3 & 4); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS, p. 223); David J. Maguire et al., <em>Geographical Information Systems: Principles and Applications</em>."""

    part1 = r"""
  <!-- CARD 1: VECTOR SPAGHETTI VS RASTER COMPRESSION -->
  <div class="card">
    <div class="card-header bg-blue">1. Spatial Data Structures: The Spaghetti Vector Model vs. Raster Encodings</div>
    <div class="card-body">
      <p>
        In Geographic Information Science, digital cartography, and spatial database design, <strong>spatial data structures</strong> define the specific data storage formats and compression algorithms used to encode geometric features into digital computer memory (Burrough & McDonnell, 1998; Chang, 2019; Bangar, p. 223).
      </p>
      <p>
        Spatial structures are broadly partitioned into two competing paradigms: <strong>Vector Data Models</strong> (coordinate-based geometry) and <strong>Raster Data Structures</strong> (grid-cell pixel matrices and compression algorithms).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q138/spatial_data_structures_spaghetti_vs_raster.png" alt="Spatial Data Structures: Spaghetti Vector vs Raster Quadtree and RLE">
        <div class="figure-caption">
          <strong>Figure 138.1 — Comparative Taxonomy of Spatial Data Structures:</strong> The Spaghetti model is an unstructured, non-topological vector format where independent lines cross like cooked noodles. In contrast, Quadtrees, Run-Length Encoding (RLE), and Block Encoding are standard mathematical structures designed specifically for compressing and organizing 2D raster grids.
        </div>
      </div>

      <h4>The Spaghetti Vector Model</h4>
      <p>
        The <strong>Spaghetti Model</strong> is the simplest and earliest <strong>Vector Data Model</strong> in computerized cartography (Bangar, p. 223; Burrough & McDonnell):
      </p>
      <ul>
        <li><strong>Structural Definition:</strong> A collection of independent, unlinked coordinate pairs representing points, polylines, and polygons. Features are stored as raw strings of $[X, Y]$ coordinates with zero topological relationships.</li>
        <li><strong>Why Termed "Spaghetti":</strong> The name stems from the physical analogy of dropping a bowl of cooked spaghetti noodles on a floor. Graphic lines cross, overlap, and terminate randomly in Cartesian coordinate space without any software awareness of intersection nodes, shared boundaries, or spatial contiguity.</li>
        <li><strong>Severe Data Redundancy:</strong> If two adjacent geological formations (e.g., a limestone unit and a shale unit) share a common contact boundary, that shared boundary is digitized and recorded <em>twice independently</em>—once for the limestone polygon and once for the shale polygon. Slivers and gaps inevitably occur.</li>
        <li><strong>Definitive Conclusion:</strong> The Spaghetti model is unequivocally a <strong>VECTOR data model</strong>; it has no relation to raster cell matrices.</li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q138/bangar_p223_raster_vs_vector_spaghetti_model.png" alt="Raster vs Vector Spaghetti Model from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 138.2 — Spatial Data Structures in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 223). Delineates raster data compression techniques (Quadtree, Run-Length, Block Encoding) and identifies the Spaghetti model as a non-topological vector structure.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE AUTHENTIC RASTER DATA STRUCTURES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Comprehensive Operational Review of Authentic Raster Data Structures</div>
    <div class="card-body">
      <h4>1. Quadtree (Hierarchical Raster Subdivision)</h4>
      <p>
        A sophisticated 2D hierarchical spatial data structure based on the recursive decomposition of a raster grid into quadrants:
      </p>
      <ul>
        <li>An entire square raster image ($2^N \times 2^N$ cells) is treated as the root node.</li>
        <li>If all pixels in the grid have the identical attribute value, the node is homogeneous (leaf node).</li>
        <li>If the grid contains heterogeneous pixel values, it is split into four equal quadrants: <strong>North-West (NW), North-East (NE), South-West (SW), and South-East (SE)</strong>.</li>
        <li>The process repeats recursively down to individual pixels until every terminal node is homogeneous. This provides immense data compression for large, uniform geological terrain blocks.</li>
      </ul>

      <h4>2. Run-Length Encoding (RLE — 1D Raster Compression)</h4>
      <p>
        A classical, lossless scanline compression algorithm applied row-by-row across raster matrices:
      </p>
      <ul>
        <li>Instead of storing every pixel individually (e.g., $A, A, A, A, A, B, B, B$), the algorithm stores ordered pairs consisting of the <strong>run count and the pixel value</strong>: $(5, A), (3, B)$.</li>
        <li>Extremely efficient for thematic geological maps where large areas contain contiguous expanses of identical lithological rock types.</li>
      </ul>

      <h4>3. Block Encoding (2D Rectangular Compression)</h4>
      <p>
        A two-dimensional extension of run-length encoding where homogeneous raster areas are aggregated into variable-sized square or rectangular blocks:
      </p>
      <ul>
        <li>Each block is stored as four parameters: the origin coordinates $(X, Y)$, block width/size ($S$), and cell attribute value ($V$).</li>
        <li>Eliminates row-by-row scanline overhead, yielding compact 2D storage.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-indigo">3. Structural Comparison: Vector Spaghetti vs. Topological vs. Raster Models</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Data Model / Structure</th>
            <th>Fundamental Domain</th>
            <th>Internal Storage Format</th>
            <th>Topology Present?</th>
            <th>Primary Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Spaghetti Model</strong></td>
            <td><strong>Vector</strong></td>
            <td>Independent, unordered coordinate strings: $[(X_1, Y_1), \dots, (X_n, Y_n)]$</td>
            <td><strong>No</strong> (Non-topological; lines cross freely)</td>
            <td>Computer-Aided Drafting (CAD), basic graphic rendering, legacy digitizer input.</td>
          </tr>
          <tr>
            <td><strong>Topological Vector (Coverage)</strong></td>
            <td><strong>Vector</strong></td>
            <td>Node tables, Arc-Node lists, Left-Right polygon topology tables</td>
            <td><strong>Yes</strong> (Explicit adjacency, connectivity, containment)</td>
            <td>Advanced spatial analysis, network tracing, contiguous geological polygon mapping.</td>
          </tr>
          <tr>
            <td><strong>Quadtree</strong></td>
            <td><strong>Raster</strong></td>
            <td>Hierarchical quaternary tree graph ($4^k$ child nodes)</td>
            <td>Implicit spatial index</td>
            <td>Lossless raster compression, fast spatial indexing, multi-resolution pyramids.</td>
          </tr>
          <tr>
            <td><strong>Run-Length Encoding (RLE)</strong></td>
            <td><strong>Raster</strong></td>
            <td>Sequential scanline tuples: $[(\text{Count}, \text{Value})]$</td>
            <td>No (Grid-based)</td>
            <td>Standard TIFF/GeoTIFF raster compression, thematic categorical raster maps.</td>
          </tr>
          <tr>
            <td><strong>Block Encoding</strong></td>
            <td><strong>Raster</strong></td>
            <td>2D square block tuples: $[(X, Y, \text{Width}, \text{Value})]$</td>
            <td>No (Grid-based)</td>
            <td>Two-dimensional contiguous zone raster compression.</td>
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
      <div class="question-number">Question 138</div>
      <div class="question-text">
        Which of the following is not a raster data structure ?
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Quadtree</li>
        <li class="option-item correct"><strong>(B)</strong> Spaghetti</li>
        <li class="option-item"><strong>(C)</strong> Run-length encoding</li>
        <li class="option-item"><strong>(D)</strong> Block encoding</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (B) Spaghetti</strong> — The Spaghetti model is an unstructured, non-topological <strong>Vector data model</strong> (where coordinates are stored as simple strings of lines without topology); it is NOT a raster data structure.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Quadtree — Valid Raster Structure (Hence Incorrect Choice)</div>
        <p>
          A quadtree is a premier hierarchical 2D raster data structure that recursively subdivides heterogeneous raster image blocks into four quadrants (NW, NE, SW, SE) until all leaf nodes are homogeneous. Because it is a bona fide raster data structure, it is not the correct answer to this negative prompt.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (B): Spaghetti — Fully Verified & Correct Option (Vector Model)</div>
        <p>
          The <strong>Spaghetti Model</strong> is unequivocally a <strong>Vector data structure</strong>, originally introduced in early computer-aided design (CAD) and rudimentary GIS software (Bangar, p. 223; Burrough & McDonnell, Ch. 3). It stores points, lines, and polygons as independent coordinate lists $[(X_1, Y_1), \dots, (X_n, Y_n)]$ without maintaining shared nodes, polygon adjacency, or line connectivity. Because it operates entirely on Cartesian vector coordinates rather than grid-cell pixel arrays, it is <strong>NOT a raster data structure</strong>.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Run-length encoding — Valid Raster Structure (Hence Incorrect Choice)</div>
        <p>
          Run-length encoding (RLE) is one of the most widely implemented raster compression data structures in GIS (used in GeoTIFF, ESRI Grid, and MrSID). It compresses adjacent cells along raster scanlines into run-length pairs $[(\text{Count}, \text{Value})]$. Being an authentic raster structure, it cannot be chosen.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Block encoding — Valid Raster Structure (Hence Incorrect Choice)</div>
        <p>
          Block encoding is a two-dimensional raster data compression method that aggregates square or rectangular clusters of identical grid cells into discrete blocks $[(X, Y, \text{Size}, \text{Value})]$. It is a legitimate raster data structure and is therefore incorrect.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Technical Trade-Offs: Vector Spaghetti vs. Raster Compression Structures</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Spaghetti Vector Model</th>
            <th>Run-Length Encoding (Raster)</th>
            <th>Quadtree (Raster)</th>
            <th>Block Encoding (Raster)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Spatial Domain</strong></td>
            <td>Vector (Point, Line, Poly)</td>
            <td>1D Scanline Raster</td>
            <td>2D Hierarchical Raster</td>
            <td>2D Block Raster</td>
          </tr>
          <tr>
            <td><strong>Compression Type</strong></td>
            <td>None (Raw coordinate lists)</td>
            <td>Lossless 1D run compression</td>
            <td>Lossless hierarchical tree</td>
            <td>Lossless 2D cluster compression</td>
          </tr>
          <tr>
            <td><strong>Data Redundancy</strong></td>
            <td><strong>Extreme:</strong> Shared borders stored twice</td>
            <td>Low for contiguous zones</td>
            <td>Very low for large homogenous regions</td>
            <td>Low for regular geometric blocks</td>
          </tr>
          <tr>
            <td><strong>Topological Capability</strong></td>
            <td><strong>Zero:</strong> No adjacency or network flow</td>
            <td>Implicit neighborhood via grid indices</td>
            <td>Fast spatial hierarchy indexing</td>
            <td>Implicit via Cartesian block coordinates</td>
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
        <strong>Problem 1: Run-Length Encoding (RLE) Compression Ratio Calculation</strong><br>
        A thematic geological raster grid row of 16 pixels contains the following lithological classifications:
        $$\text{Row: } [G, G, G, G, G, G, S, S, S, S, B, B, B, B, B, B]$$
        (where $G = \text{Granite}, S = \text{Shale}, B = \text{Basalt}$).
        (a) Write the compressed Run-Length Encoded string in $[(\text{Count}, \text{Value})]$ format. (b) Calculate the compression ratio if uncompressed pixels require 1 byte each, and each RLE tuple requires 2 bytes ($1\text{ byte for count} + 1\text{ byte for value}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. RLE compressed string:
          $$[(6, G), (4, S), (6, B)]$$
          2. Uncompressed storage size:
          $$S_{\text{uncompressed}} = 16\text{ pixels} \times 1\text{ byte} = 16\text{ bytes}$$
          3. RLE compressed storage size (3 tuples):
          $$S_{\text{compressed}} = 3\text{ tuples} \times 2\text{ bytes/tuple} = 6\text{ bytes}$$
          4. Compression Ratio ($CR$):
          $$CR = \frac{S_{\text{uncompressed}}}{S_{\text{compressed}}} = \frac{16\text{ bytes}}{6\text{ bytes}} \approx 2.67 : 1 \quad (\approx 62.5\% \text{ storage reduction})$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Quadtree Decomposition of an $8 \times 8$ Geological Raster</strong><br>
        An $8 \times 8$ binary raster grid ($64\text{ total cells}$) contains an ore body located entirely within the top-left quadrant (cells $(0,0)$ to $(3,3)$ are all value $1$), while all other 48 cells in the remaining three quadrants are homogeneous barren host rock (value $0$). Determine: (a) the number of quadrants at Level 1, (b) how many quadrants require further subdivision, and (c) the total number of leaf nodes in the resulting Quadtree.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Level 1 subdivision: The $8 \times 8$ grid is partitioned into four $4 \times 4$ quadrants:
          - NW quadrant: completely filled with value $1$ &rarr; <strong>Homogeneous Leaf Node (Level 1)</strong>.
          - NE quadrant: completely filled with value $0$ &rarr; <strong>Homogeneous Leaf Node (Level 1)</strong>.
          - SW quadrant: completely filled with value $0$ &rarr; <strong>Homogeneous Leaf Node (Level 1)</strong>.
          - SE quadrant: completely filled with value $0$ &rarr; <strong>Homogeneous Leaf Node (Level 1)</strong>.
          2. Further subdivision: <strong>Zero</strong> quadrants require further subdivision because every quadrant is completely homogeneous!
          3. Total leaf nodes:
          $$\text{Total Leaf Nodes} = 4\text{ nodes}$$
          <em>Efficiency:</em> An entire 64-pixel raster is represented losslessly by just 4 tree nodes (a 16:1 compression ratio).
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Spaghetti Model Coordinate Redundancy</strong><br>
        Two adjacent geological mining leases, Lease Alpha and Lease Beta, are digitized using the vector Spaghetti model. Lease Alpha is a 6-sided polygon ($6\text{ vertices}$), and Lease Beta is an 8-sided polygon ($8\text{ vertices}$). They share a common boundary consisting of a 4-vertex polyline. In the Spaghetti model where each vertex coordinate pair $(X, Y)$ requires 16 bytes: (a) calculate total bytes stored, and (b) calculate how many bytes are wasted due to redundant duplicate storage of the shared boundary.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. In the Spaghetti model, polygons are closed by repeating the first vertex:
          - Lease Alpha: 6 vertices + 1 closing vertex = 7 coordinate pairs ($7 \times 16\text{ bytes} = 112\text{ bytes}$).
          - Lease Beta: 8 vertices + 1 closing vertex = 9 coordinate pairs ($9 \times 16\text{ bytes} = 144\text{ bytes}$).
          $$\text{Total stored} = 112 + 144 = 256\text{ bytes}$$
          2. Redundant duplicate storage:
          The shared boundary consists of 4 vertices that are digitized and stored in both polygons:
          $$\text{Redundant storage} = 4\text{ vertices} \times 16\text{ bytes} = 64\text{ bytes}$$
          $$\% \text{ Wasted Space} = \left(\frac{64}{256}\right) \times 100\% = 25.0\%$$
          (A topological Arc-Node model stores the shared boundary arc once, saving $25\%$ storage).
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Block Encoding Storage Reduction</strong><br>
        A thematic raster map of size $100\text{ cells} \times 100\text{ cells}$ ($10,000\text{ cells}$) depicts a massive limestone plateau covering a continuous square area of $60\text{ cells} \times 60\text{ cells}$ ($3,600\text{ cells}$) of uniform value $1$. In uncompressed raster format, this zone requires $3,600\text{ bytes}$. In Block Encoding, this zone is encoded as a single tuple $[X_0, Y_0, \text{Width}, \text{Value}]$ taking 8 bytes. Calculate the local compression ratio achieved for this geological feature.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Uncompressed size = $3,600\text{ bytes}$.
          2. Block-encoded size = $8\text{ bytes}$.
          3. Local Compression Ratio:
          $$CR = \frac{3600\text{ bytes}}{8\text{ bytes}} = 450 : 1$$
          Storage is reduced by $99.78\%$ for the uniform plateau.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Maximum Node Capacity of a Quadtree at Depth Level $D$</strong><br>
        A Quadtree structure has a maximum tree depth $D = 4$ (where root is Level 0). Using the formula for the maximum possible number of nodes in a full quaternary tree:
        $$N_{\text{total}} = \sum_{k=0}^D 4^k = \frac{4^{D+1} - 1}{4 - 1}$$
        Calculate the maximum number of nodes in the quadtree.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Apply the summation formula for $D = 4$:
          $$N_{\text{total}} = \frac{4^{4+1} - 1}{3} = \frac{4^5 - 1}{3} = \frac{1024 - 1}{3} = \frac{1023}{3} = 341\text{ nodes}$$
          (Level 0: $1$, Level 1: $4$, Level 2: $16$, Level 3: $64$, Level 4: $256$; sum = $341$).
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Freeman Chain Coding of a Geological Contact Boundary</strong><br>
        Freeman Chain Coding (using the standard 8-directional compass codes: $0 = \text{East}, 1 = \text{NE}, 2 = \text{North}, 3 = \text{NW}, 4 = \text{West}, 5 = \text{SW}, 6 = \text{South}, 7 = \text{SE}$) encodes a boundary path starting at $(10, 10)$ with the following directional sequence:
        $$\text{Chain Code: } [0, 0, 2, 2, 4, 4, 6, 6]$$
        (a) Trace the path and determine the coordinates of each vertex. (b) Determine whether the path forms a closed polygon loop.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Trace steps:
          - Start: $(10, 10)$
          - Code 0 (East): $(11, 10)$
          - Code 0 (East): $(12, 10)$
          - Code 2 (North): $(12, 11)$
          - Code 2 (North): $(12, 12)$
          - Code 4 (West): $(11, 12)$
          - Code 4 (West): $(10, 12)$
          - Code 6 (South): $(10, 11)$
          - Code 6 (South): $(10, 10)$
          2. Check closure:
          The final vertex $(10, 10)$ is identical to the start vertex $(10, 10)$. <strong>The chain code forms a closed square polygon of size $2 \times 2$ cells.</strong>
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Worst-Case Failure of Run-Length Encoding (Checkerboard Grid)</strong><br>
        A $10 \times 10$ raster grid ($100\text{ pixels}$) contains alternating black and white pixels in a perfect checkerboard pattern ($0, 1, 0, 1, \dots$).
        (a) What is the length of every run? (b) Calculate the compressed RLE size assuming each tuple takes 2 bytes. (c) Determine whether RLE compressed or expanded the file size.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. In a checkerboard pattern, no two adjacent cells share the same value; therefore, every run length is exactly $1$ pixel ($\text{Count} = 1$).
          2. In every 10-pixel row, there are 10 separate tuples: $[(1, 0), (1, 1), (1, 0), \dots]$.
          Across all 10 rows, there are $10 \times 10 = 100\text{ tuples}$.
          $$S_{\text{RLE}} = 100\text{ tuples} \times 2\text{ bytes/tuple} = 200\text{ bytes}$$
          3. Comparison: Uncompressed size was $100\text{ bytes}$. RLE storage is $200\text{ bytes}$.
          <strong>RLE has expanded the file size by $100\%$ ($2\times$ larger)!</strong>
          <em>Data Structure Lesson:</em> Run-length encoding is severely counter-productive for high-frequency, noisy, or checkerboard raster datasets.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Topological Validation: Detecting Spaghetti Errors</strong><br>
        In an automated GIS quality audit of a digitized Spaghetti vector layer containing 500 fault lines, an operator runs an automated topology builder. The algorithm detects:
        - 18 intersecting lines that lack an intersection node (crossed spaghetti lines).
        - 24 lines whose endpoints fall within $1.0\text{ m}$ of each other but do not connect (undershoots).
        - 12 self-intersecting polylines.
        Calculate the total number of topological errors that must be resolved to convert this Spaghetti layer into an authentic topological vector coverage.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Sum all detected topological violations:
          $$\text{Total Errors} = 18\text{ crossed lines} + 24\text{ undershoots} + 12\text{ self-intersections} = 54\text{ topological errors}$$
          All 54 geometric flaws must be cleaned by planarization, node insertion, and snapping before network or spatial overlay analysis can occur.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=138,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q138_Spaghetti_Model_Vector_vs_Raster_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q138: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q138()
