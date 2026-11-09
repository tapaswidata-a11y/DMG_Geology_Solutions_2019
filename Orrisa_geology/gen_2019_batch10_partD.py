#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 10 Part D (Q144 - Q150)
Burrough Definition, Reclassification, Point-in-Polygon, Raster Model, Map Projections,
Cartographic Modeling & The GIS Data Stream.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q144: Peter Burrough (1986) Classic Toolbox Definition of GIS
# -----------------------------------------------------------------------------
def gen_q144():
    q_num = 144
    filename = "Q144_GIS_Definition_Set_Of_Tools_Peter_Burrough_1986_Complete_Guide.html"
    title = "Q144: GIS Foundations - Peter Burrough's 1986 Definition"
    badge = "OPSC 2019 Geology Paper-II • Question 144 • GIS Foundations & History"
    h1_title = "Geographic Information Systems: Foundational Definition and the Five Core Subsystems by Peter A. Burrough (1986)"
    meta_text = r"<strong>Topic:</strong> GIS Historical Evolution & Core Definitions • <strong>Key Concept:</strong> Peter Burrough's Classic 'Toolbox' Definition (1986) • <strong>Textbooks:</strong> P.A. Burrough (1986, <em>Principles of Geographical Information Systems for Land Resources Assessment</em>, Oxford Univ. Press, p. 6); P.A. Burrough & R.A. McDonnell (1998); Kang-tsung Chang (Ch. 1); K.M. Bangar (p. 216)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Peter Burrough's Classic Definition of GIS</div>
      <p>During the rapid development of computer cartography and environmental modeling in the 1980s, numerous definitions of Geographic Information Systems (GIS) emerged, categorized into toolbox-based, database-oriented, and organizational definitions. Among all academic literature, the classic, universally quoted <strong>toolbox definition</strong> was articulated by Professor <strong>Peter A. Burrough</strong> in his seminal 1986 textbook <em>Principles of Geographical Information Systems for Land Resources Assessment</em> (Oxford University Press, p. 6):</p>

      <div class="math-block">
        $$\text{“A GIS is a powerful set of tools for collecting, storing, retrieving at will,}$$
        $$\text{transforming, and displaying spatial data from the real world for a particular set of purposes.”}$$
      </div>

      <p>Burrough's definition revolutionized GIS by identifying the five indispensable functional subsystems that define any complete GIS software architecture (Burrough, 1986; Burrough & McDonnell, 1998; Chang):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Functional Subsystem (Burrough 1986)</th>
              <th>Core Technical Capabilities</th>
              <th>Practical Geospatial Operations</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td><strong>1. Collecting (Data Input & Acquisition)</strong></td>
              <td>Capturing real-world spatial coordinates and attributes from analog or raw sources.</td>
              <td>Digitization of paper geological maps, GPS surveying, aerial drone photogrammetry, satellite image ingestion.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>2. Storing (Data Storage & Management)</strong></td>
              <td>Organizing spatial geometries and attribute tables in structured digital formats.</td>
              <td>Relational geodatabases (PostGIS, Oracle Spatial), topological vector structures, multi-band raster matrices.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>3. Retrieving (Data Query & Retrieval)</strong></td>
              <td>Selective extraction of features based on spatial or attribute criteria.</td>
              <td>SQL queries (<code>SELECT * WHERE rock_type = 'Granite'</code>), spatial location queries, cursor indexing.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>4. Transforming (Data Transformation & Analysis)</strong></td>
              <td>Modifying coordinates, projecting, overlaying, and analyzing spatial relationships to generate new information.</td>
              <td>Map projections, coordinate transformation, buffering, polygon overlay, spatial interpolation (kriging), terrain slope modeling.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>5. Displaying (Data Output & Visualization)</strong></td>
              <td>Visual rendering and cartographic production of spatial data for human interpretation.</td>
              <td>Thematic map layouts, 3D terrain draping, interactive web maps, automated report generation.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q144/peter_burrough_1986_gis_definition_five_functions.png" alt="Peter Burrough 1986 GIS Definition" class="figure-img">
        <div class="figure-caption">Figure 144: The five foundational functional subsystems of GIS articulated in Peter Burrough's classic 1986 definition: Collecting, Storing, Retrieving, Transforming, and Displaying spatial data (Option B).</div>
      </div>

      <p>Burrough's operational definition distinguishes a true GIS from a simple Computer-Aided Design (CAD) drafting program or computerized mapping tool: while CAD displays graphics, a GIS fundamentally includes the capacity to <strong>transform and spatially analyze</strong> geographic data to solve complex real-world environmental and geological problems.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 144</div>
        <div class="raw-q-text">A GIS is "a set of tools for collecting, storing, retrieving, tranformating and displaying spatial data from the real world fora particular use” as defined by:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> David Rhind (1991)</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Peter Burrough (1986)</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Mike Goodchild (1997)</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Roger Chorley (1987)</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Peter Burrough (1986))
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Peter Burrough (1986)</div>
          <p>This quotation is the verbatim classic definition formulated by Professor <strong>Peter A. Burrough</strong> in his landmark 1986 book <em>Principles of Geographical Information Systems for Land Resources Assessment</em> (Oxford University Press, p. 6). It is universally cited across university GIS textbooks as the definitive "toolbox" definition of a GIS.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">David Rhind (1991)</div>
          <p>Professor David Rhind defined GIS from an individual-organization perspective in 1989/1991 as "a computer system for capturing, storing, checking, integrating, manipulating, analysing and displaying data which are spatially referenced to the Earth", but he is not the author of the 1986 five-tool definition quoted in the question.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Mike Goodchild (1997)</div>
          <p>Professor Michael F. Goodchild is widely recognized as the father of "Geographic Information Science" (GIScience, 1992). His work focused on spatial ontology, spatial analysis, and uncertainty modeling, rather than the 1986 toolbox definition.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Roger Chorley (1987)</div>
          <p>Lord Chorley chaired the UK Committee of Enquiry into the Handling of Geographic Information, which produced the influential <em>Chorley Report</em> (1987), defining GIS as "a system for capturing, storing, checking, integrating, manipulating, analysing and displaying data".</p>
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
              <th>Pioneering GIS Scholar / Institution</th>
              <th>Year</th>
              <th>Focus of Definition</th>
              <th>Historical Significance</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Roger Tomlinson</td><td>1963 / 1968</td><td>Computerized Land Resource Inventory</td><td>Created the <strong>Canada Geographic Information System (CGIS)</strong>; coined the term "GIS".</td></tr>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Peter A. Burrough</strong></td><td><strong>1986</strong></td><td><strong>Five-Tool Operational Subsystems</strong> (Option B)</td><td>Wrote the first comprehensive academic university textbook on GIS (Oxford Press).</td></tr>
            <tr><td>Chorley Committee (UK)</td><td>1987</td><td>Government & Societal Information Handling</td><td>Standardized British government adoption of digital spatial data.</td></tr>
            <tr><td>Michael F. Goodchild</td><td>1992</td><td>Geographic Information Science (GIScience)</td><td>Established GIS as a scientific discipline studying spatial data structures and spatial algorithms.</td></tr>
            <tr><td>David Rhind</td><td>1989 / 1991</td><td>Multidisciplinary Decision Support</td><td>Co-edited the foundational <em>Geographical Information Systems: Principles and Applications</em>.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Who is universally regarded as the "Father of GIS"?</div>
        <div class="pq-ans">Answer: Dr. Roger Tomlinson (1933–2014).</div>
        <div class="pq-exp">He designed and led the development of the Canada Geographic Information System (CGIS) in the 1960s for the Canada Land Inventory.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What was the world's first true operational computer Geographic Information System?</div>
        <div class="pq-ans">Answer: The Canada Geographic Information System (CGIS), operational in the late 1960s.</div>
        <div class="pq-exp">CGIS pioneered topological polygon encoding, raster-to-vector scanning, and national land capability overlays.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What was the seminal textbook authored by Peter A. Burrough in 1986?</div>
        <div class="pq-ans">Answer: <em>Principles of Geographical Information Systems for Land Resources Assessment</em> (Oxford University Press).</div>
        <div class="pq-exp">In 1998, Burrough and Rachael McDonnell expanded it into the widely used university classic <em>Principles of Geographical Information Systems</em>.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What fundamental capability distinguishes a Geographic Information System (GIS) from a Computer-Aided Design (CAD) system?</div>
        <div class="pq-ans">Answer: Spatial analysis, topological relationship modeling, map projections/coordinate systems, and dynamic linkage between geometry and relational attribute databases.</div>
        <div class="pq-exp">CAD primarily models 2D/3D graphical geometry for drafting; GIS performs spatial overlay, proximity, and network routing.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What are the four core components that constitute a complete operational GIS?</div>
        <div class="pq-ans">Answer: Hardware, Software, Spatial & Attribute Data, and People (Skilled personnel and management protocols).</div>
        <div class="pq-exp">Without trained personnel and standardized procedures, hardware and software cannot produce valid geographic decisions.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How did Michael Goodchild define the boundary between "GIS" (the technology) and "GIScience" (the science)?</div>
        <div class="pq-ans">Answer: GIS is the computer software and hardware tool; GIScience is the fundamental scientific discipline that studies the generic theoretical concepts behind spatial data, representations, algorithms, and uncertainty.</div>
        <div class="pq-exp">Goodchild published this foundational distinction in 1992 in the <em>International Journal of Geographical Information Systems</em>.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is "Topology" in GIS vector data structures?</div>
        <div class="pq-ans">Answer: The mathematical study of geometric properties and spatial relationships (adjacency, connectivity, and containment) that remain invariant under continuous transformation.</div>
        <div class="pq-exp">Topology explicitly stores which polygon is to the left/right of an arc and which nodes connect intersecting lines.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What major software package developed at Harvard Laboratory for Computer Graphics in 1965 pioneered computer mapping?</div>
        <div class="pq-ans">Answer: SYMAP (Synagraphic Mapping System), developed under Howard Fisher.</div>
        <div class="pq-exp">SYMAP produced line-printer maps of continuous spatial surfaces, inspiring subsequent vector overlay packages like ODYSSEY and Esri's ARC/INFO.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q145: Reclassification in GIS
# -----------------------------------------------------------------------------
def gen_q145():
    q_num = 145
    filename = "Q145_What_Is_Reclassification_Combining_Data_Ranges_Complete_Guide.html"
    title = "Q145: GIS Spatial Analysis - Reclassification"
    badge = "OPSC 2019 Geology Paper-II • Question 145 • GIS Spatial Analysis"
    h1_title = "GIS Spatial Analysis & Raster Modeling: The Principles and Operations of Reclassification"
    meta_text = r"<strong>Topic:</strong> Raster Geoprocessing & Spatial Analysis • <strong>Key Concept:</strong> Reclassification, Value Slicing, Attribute Recoding & Suitability Modeling • <strong>Textbooks:</strong> Kang-tsung Chang (<em>Introduction to Geographic Information Systems</em>, 9th Ed., Ch. 12); P.A. Burrough & R.A. McDonnell (Ch. 5); C. Dana Tomlin (<em>GIS and Cartographic Modeling</em>); K.M. Bangar (p. 219)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Reclassification in Raster GIS</div>
      <p>In Geographic Information Systems (GIS), <strong>reclassification</strong> (also termed <em>re-coding</em> or <em>value slicing</em>) is a fundamental cell-by-cell local operation in Map Algebra. It replaces existing input cell values in a raster dataset with new output values based on a user-defined lookup table, mathematical function, or range threshold (Chang; Burrough & McDonnell; Tomlin):</p>

      <p>By international GIS definition, <strong>reclassification is the process of combining one or more data ranges (or discrete values) into a new data range (or new categorical value) to create a new derived data layer</strong> (Option A):</p>

      <div class="math-block">
        $$\text{Output Cell } g(x, y) = T[f(x, y)]$$
      </div>

      <p>where $f(x, y)$ is the input raster value, $g(x, y)$ is the new reclassified value, and $T$ is the reclassification mapping function.</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Reclassification Mechanism</th>
              <th>Operation Description</th>
              <th>Practical Geospatial / Geological Example</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>1. Range Slicing (Class Binning)</strong> (Option A)</td>
              <td>Groups continuous numerical values into discrete ordinal or nominal categories based on specified range intervals.</td>
              <td><strong>Slope Reclassification:</strong><br>• $0^\circ\text{--}5^\circ \implies \text{Class 1 (Flat / Low Landslide Risk)}$<br>• $5^\circ\text{--}20^\circ \implies \text{Class 2 (Moderate)}$<br>• $>20^\circ \implies \text{Class 3 (High Landslide Hazard)}$.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>2. One-to-One Value Remapping</strong></td>
              <td>Replaces each unique categorical or numerical value directly with another specific code.</td>
              <td><strong>Lithological Coding:</strong> Remapping 50 detailed stratigraphical formation codes into 3 broad rock classes: Sedimentary (1), Igneous (2), Metamorphic (3).</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>3. Boolean Thresholding (Binary Masking)</strong></td>
              <td>Evaluates a conditional expression to output a binary mask: $1$ if true, $0$ or NoData if false.</td>
              <td><strong>Aquifer Protection Mask:</strong> Cells where depth to water table $< 5\text{ m}$ become $1$ (Vulnerable); all others become $0$.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>4. Common Scale Normalization (Suitability Modeling)</strong></td>
              <td>Rescales disparate variables (slope, soil depth, distance to faults, rainfall) onto a common evaluation scale (e.g. 1 to 10).</td>
              <td>Multi-Criteria Decision Analysis (MCDA) for mining lease site selection or landfill suitability mapping.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q145/gis_reclassification_data_ranges_new_layer.png" alt="GIS Reclassification Process" class="figure-img">
        <div class="figure-caption">Figure 145: Reclassification workflow in GIS: grouping continuous numerical elevation/slope data ranges into new categorical classes to produce a derived thematic layer (Option A).</div>
      </div>

      <p>Reclassification does not modify the original input dataset; it creates an entirely <strong>new data layer</strong> with generalized or transformed attribute values, acting as the mandatory preparatory step for weighted raster overlay and multi-criteria spatial decision support.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 145</div>
        <div class="raw-q-text">What is reclassification ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> The process of combining one or more data ranges into a new data range to create a new data layer</div>
          <div class="raw-opt"><span class="opt-letter">B</span> An analytical technique based on point data</div>
          <div class="raw-opt"><span class="opt-letter">C</span> The process of simplifying data in a data layer</div>
          <div class="raw-opt"><span class="opt-letter">D</span> The process of combining two or more data layers</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (The process of combining one or more data ranges into a new data range to create a new data layer)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">The process of combining one or more data ranges into a new data range to create a new data layer</div>
          <p>By authoritative GIScience and Map Algebra definitions (Chang, Ch. 12; Burrough & McDonnell; Tomlin; Bangar, p. 219), <strong>reclassification</strong> is precisely the operational process of grouping, re-assigning, or combining one or more existing data values/ranges into new values or ranges to generate an entirely new derived thematic data layer.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">An analytical technique based on point data</div>
          <p>Reclassification is a generic local spatial operation primarily applied to raster grids and tabular polygon attributes. It is not an analytical technique specifically based on point data (which would refer to spatial interpolation or point pattern analysis).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; INCOMPLETE DEFINITION</div>
          <div class="opt-title">The process of simplifying data in a data layer</div>
          <p>While reclassification can simplify continuous data into categories, "simplifying data" is a vague description that also encompasses vector line generalization (e.g. Douglas-Peucker) and feature elimination. Option A provides the rigorous, formal definition of reclassification.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">The process of combining two or more data layers</div>
          <p>Combining two or more different data layers is the definition of <strong>Spatial Overlay</strong> (e.g. Intersect, Union, Weighted Overlay) or Mosaic/Merge, not reclassification. Reclassification operates on a <em>single</em> input layer at a time.</p>
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
              <th>Map Algebra Operation Category</th>
              <th>Spatial Neighborhood Scope</th>
              <th>Representative Tools</th>
              <th>Input Layers Required</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Local Operation</strong> (e.g. Reclassification)</td><td>Single cell location $(x, y)$ independently</td><td><strong>Reclassify</strong>, Raster Calculator ($A + B$), Trigonometric math, Conditional (Con)</td><td>Single raster (or multiple rasters evaluated cell-by-cell)</td></tr>
            <tr><td>Focal (Neighborhood) Operation</td><td>Target cell + surrounding roving window ($3 \times 3$, $5 \times 5$)</td><td>Focal Mean, Focal Variety, Slope, Aspect, Hillshade, High-pass filter</td><td>Single raster</td></tr>
            <tr><td>Zonal Operation</td><td>Groups of cells sharing the same zone ID</td><td>Zonal Statistics (Zonal Mean elevation per geological formation)</td><td>Two rasters (Zone layer + Value layer)</td></tr>
            <tr><td>Global Operation</td><td>Entire raster grid surface simultaneously</td><td>Euclidean Distance, Cost-Distance, Viewshed, Flow Accumulation</td><td>Single raster</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. To which class of Map Algebra operations does Reclassification belong according to C. Dana Tomlin's classification?</div>
        <div class="pq-ans">Answer: Local Operations.</div>
        <div class="pq-exp">The output value at cell $(x, y)$ is computed strictly from the input value at that exact same cell $(x, y)$ without referencing neighboring cells.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. In landfill site suitability modeling, why is Reclassification a mandatory prerequisite before Weighted Overlay?</div>
        <div class="pq-ans">Answer: Because input datasets have completely different physical units (slope in degrees, distance in meters, geology in text names); reclassification converts all layers onto a common standardized suitability scale (e.g. 1 = Unsuitable to 5 = Highly Suitable).</div>
        <div class="pq-exp">Without reclassification, layers with different measurement scales cannot be combined mathematically.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is "Equal Interval" vs. "Quantile" reclassification of continuous data?</div>
        <div class="pq-ans">Answer: Equal Interval divides the range ($Max - Min$) into classes of equal numerical width; Quantile assigns an equal number of grid cells/records to each class.</div>
        <div class="pq-exp">Quantile produces visually balanced maps for skewed datasets; Equal Interval is preferred for naturally continuous gradients (temperatures).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the "Natural Breaks" (Jenks) classification method commonly used in GIS reclassification?</div>
        <div class="pq-ans">Answer: An optimization algorithm that minimizes variance within each class while maximizing the variance between different classes.</div>
        <div class="pq-exp">It identifies natural groupings inherent in the data distribution.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What happens to cells assigned the value "NoData" during a reclassification operation?</div>
        <div class="pq-ans">Answer: They are treated as missing/null; in most operations they remain NoData in the output, or can be explicitly remapped to a valid numeric value if desired.</div>
        <div class="pq-exp">NoData masking prevents invalid calculations outside the study boundary.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does vector reclassification differ from raster reclassification?</div>
        <div class="pq-ans">Answer: Vector reclassification adds a new attribute column to the table and populates it with recoded values using SQL (<code>UPDATE table SET class = 1 WHERE slope < 5</code>), followed optionally by a <code>Dissolve</code> operation.</div>
        <div class="pq-exp">Raster reclassification writes a new grid file containing the replaced cell matrix values.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a "Boolean Sieve" in GIS suitability modeling?</div>
        <div class="pq-ans">Answer: Reclassifying multiple thematic layers into binary $1$ (suitable) and $0$ (unsuitable) masks, and multiplying them together ($L_1 \times L_2 \times L_3$) so that only areas meeting all criteria receive a $1$.</div>
        <div class="pq-exp">If any single criterion fails ($0$), the entire product becomes zero (veto power).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is "Slice" in raster geoprocessing?</div>
        <div class="pq-ans">Answer: An automated reclassification tool that divides the range of cell values into a specified number of equal-interval or equal-area output classes without requiring a manual lookup table.</div>
        <div class="pq-exp">It automates linear or quantile binning into $N$ output integer bins.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q146: Point-in-Polygon Overlay in GIS
# -----------------------------------------------------------------------------
def gen_q146():
    q_num = 146
    filename = "Q146_Point_In_Polygon_Overlay_Points_Within_Boundary_Complete_Guide.html"
    title = "Q146: Vector GIS - Point-in-Polygon Overlay"
    badge = "OPSC 2019 Geology Paper-II • Question 146 • Vector Spatial Analysis"
    h1_title = "Vector Spatial Analysis & Computational Geometry: Topological Mechanics of the Point-in-Polygon Overlay"
    meta_text = r"<strong>Topic:</strong> Vector Spatial Overlay & Topological Containment • <strong>Key Concept:</strong> Point-in-Polygon Overlay, Ray-Casting Algorithm & Spatial Joins • <strong>Textbooks:</strong> Kang-tsung Chang (Ch. 11); P.A. Burrough & R.A. McDonnell (Ch. 5); Joseph O'Rourke (<em>Computational Geometry in C</em>); K.M. Bangar (p. 219)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Point-in-Polygon Spatial Overlay</div>
      <p>In vector GIS and computational geometry, <strong>spatial overlay</strong> superimposes two or more geographic layers sharing a common coordinate reference system to evaluate topological relationships between intersecting geometries. When an overlay combines a <strong>point layer</strong> with a <strong>polygon layer</strong>, the operation is formally termed a <strong>Point-in-Polygon Overlay</strong> (Chang; Burrough & McDonnell; O'Rourke):</p>

      <p>By international GIS definition, <strong>a point-in-polygon overlay is an overlay method used to determine as to which points lie within the boundary of a polygon</strong> (Option D):</p>

      <div class="math-block">
        $$\text{Overlay}(P, Q) = \{ p_i \in P \mid p_i \text{ is topologically contained inside polygon } q_j \in Q \}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Vector Overlay Type</th>
              <th>Input Layer 1</th>
              <th>Input Layer 2 (Overlay Layer)</th>
              <th>Output Feature Geometry & Function</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>POINT-IN-POLYGON OVERLAY</strong> (Option D)</td>
              <td>Point Layer (e.g. Water Wells, Boreholes)</td>
              <td>Polygon Layer (e.g. Geological Formations, Districts)</td>
              <td><strong>Points:</strong> Retains point geometry but appends all polygon attribute fields to each point record (Spatial Join: which well lies in which rock unit).</td>
            </tr>
            <tr>
              <td>Line-in-Polygon Overlay</td>
              <td>Line Layer (e.g. Rivers, Faults)</td>
              <td>Polygon Layer (e.g. Mining Concessions)</td>
              <td><strong>Lines:</strong> Splits lines at polygon boundaries; attributes of polygons transferred to intersecting line segments.</td>
            </tr>
            <tr>
              <td>Polygon-on-Polygon Overlay</td>
              <td>Polygon Layer 1 (e.g. Soil Map)</td>
              <td>Polygon Layer 2 (e.g. Land Use)</td>
              <td><strong>Polygons:</strong> Creates new intersecting polygon slivers possessing combined attributes from both parent layers (Intersect/Union).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q146/point_in_polygon_overlay_gis_operation.png" alt="Point in Polygon Overlay" class="figure-img">
        <div class="figure-caption">Figure 146: Point-in-Polygon overlay (Option D) and the Ray-Casting algorithm: a horizontal ray cast from an interior point intersects polygon edges an odd number of times (1 or 3), verifying containment.</div>
      </div>

      <h4>Computational Geometry: The Ray-Casting (Even-Odd) Algorithm</h4>
      <p>How does a computer mathematically decide whether a point $(x_0, y_0)$ lies inside an irregular polygon? The standard algorithm used in GIS software is the <strong>Ray-Casting Algorithm</strong> (Jordan Curve Theorem):</p>
      <ul>
        <li>A semi-infinite horizontal test ray is cast from test point $(x_0, y_0)$ extending to $+\infty$ along the $+X$ axis.</li>
        <li>The algorithm counts the total number of intersections ($N$) between the ray and the polygon's bounding line segments.</li>
        <li><strong>Containment Rule:</strong>
          <ul>
            <li>If $N$ is <strong>ODD</strong> ($N = 1, 3, 5, \dots$), the point lies <strong>INSIDE</strong> the polygon.</li>
            <li>If $N$ is <strong>EVEN</strong> ($N = 0, 2, 4, \dots$), the point lies <strong>OUTSIDE</strong> the polygon.</li>
          </ul>
        </li>
      </ul>

      <p>In practical geological GIS, point-in-polygon overlay enables queries such as: <em>Which mineral exploration drill-holes fall inside the newly leased quarry polygon?</em> or <em>Which earthquake epicenters fall inside active seismotectonic graben zones?</em></p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 146</div>
        <div class="raw-q-text">What is ‘point-in-polygon’ overlay ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> A method interpolating point data</div>
          <div class="raw-opt"><span class="opt-letter">B</span> An overlay method used to determine the distance between a point and its nearest neighbouring polygon</div>
          <div class="raw-opt"><span class="opt-letter">C</span> An overlay method used to reclassify polygon data</div>
          <div class="raw-opt"><span class="opt-letter">D</span> An overlay method used to determine as to which points lie within the boundary of a polygon</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (An overlay method used to determine as to which points lie within the boundary of a polygon)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">An overlay method used to determine as to which points lie within the boundary of a polygon</div>
          <p>By universal vector GIS definition (Chang, Ch. 11; Burrough & McDonnell; Bangar, p. 219), a <strong>point-in-polygon overlay</strong> evaluates the topological containment relationship between a point layer and a polygon layer to determine exactly which point features fall within the spatial perimeter boundary of each polygon, transferring the polygon attributes into the point records.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">A method interpolating point data</div>
          <p>Interpolation (IDW, Kriging) creates continuous raster surfaces from discrete points. It has nothing to do with polygon topological overlays.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">An overlay method used to determine the distance between a point and its nearest neighbouring polygon</div>
          <p>Determining distances to nearest features is a <strong>proximity analysis</strong> tool (e.g. Near tool, Generate Near Table, or Cost Distance), not an overlay operation.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">An overlay method used to reclassify polygon data</div>
          <p>Reclassification changes attribute values of a single layer based on lookup rules. It does not perform geometric topological overlays between points and polygons.</p>
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
              <th>Topological Relationship</th>
              <th>Mathematical Operator</th>
              <th>DE-9IM Matrix Predicate</th>
              <th>Practical Geospatial Query</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Containment (Within)</strong></td><td><code>ST_Contains(Poly, Point)</code> / <code>ST_Within(Point, Poly)</code></td><td><code>T*****FF*</code></td><td>Find all groundwater wells located inside the coastal saline aquifer polygon.</td></tr>
            <tr><td>Intersection</td><td><code>ST_Intersects(GeomA, GeomB)</code></td><td><code>T********</code></td><td>Find which road segments cross over an active fault scarp.</td></tr>
            <tr><td>Adjacency (Touches)</td><td><code>ST_Touches(PolyA, PolyB)</code></td><td><code>FT*******</code></td><td>Identify mining leases that share a common boundary fence.</td></tr>
            <tr><td>Disjoint</td><td><code>ST_Disjoint(GeomA, GeomB)</code></td><td><code>FF*FF****</code></td><td>Find exploration targets situated completely outside protected forest reserves.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. In a point-in-polygon overlay between an exploration borehole point layer and a regional lithology polygon layer, what attributes will appear in the output attribute table?</div>
        <div class="pq-ans">Answer: The output attribute table contains all original borehole attributes (collar ID, depth, assay grade) PLUS all attributes from the intersecting lithology polygon (formation name, age, lithological rock group).</div>
        <div class="pq-exp">Point-in-polygon overlay performs a spatial join that enriches point data with host polygon attributes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the Winding Number algorithm in computational geometry for point-in-polygon testing?</div>
        <div class="pq-ans">Answer: An algorithm that computes the total number of times the polygon boundary winds or wraps around the test point (winding number $W \ne 0 \implies \text{Inside}$).</div>
        <div class="pq-exp">The winding number handles self-intersecting complex polygons more robustly than the basic even-odd ray test.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a "Spatial Join" in GIS software?</div>
        <div class="pq-ans">Answer: Joining attribute tables of two layers based on their relative geographic location or topological relationship (e.g. containment, nearest, or intersection) rather than a shared common alphanumeric key field.</div>
        <div class="pq-exp">Point-in-polygon overlay is the classic implementation of a spatial join based on containment.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a "Sliver Polygon" in vector GIS overlay?</div>
        <div class="pq-ans">Answer: A tiny, spurious, elongated polygon artifact generated along boundaries when overlaying two layers that share the same real-world boundary digitized slightly differently.</div>
        <div class="pq-exp">Slivers are removed using topological snapping tolerances or cluster tolerance rules.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. If a test ray cast from a point intersects a polygon's bounding edges exactly twice, is the point inside or outside the polygon?</div>
        <div class="pq-ans">Answer: Outside the polygon.</div>
        <div class="pq-exp">By the even-odd rule: 2 is an even number, meaning the ray enters and exits an exterior lobe without containing the origin point.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What happens if a point falls exactly on the boundary line segment of a polygon during a point-in-polygon query?</div>
        <div class="pq-ans">Answer: It depends on the software's boundary convention; standard OGC specifications treat the boundary as part of the polygon interior (<code>ST_Covers</code>) or evaluate it under specific vertex-touching edge rules.</div>
        <div class="pq-exp">Software typically defines inclusion if the point lies on the left/top boundary edges to prevent double-counting between adjacent polygons.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Dimensionally Extended 9-Intersection Model (DE-9IM)?</div>
        <div class="pq-ans">Answer: A topological framework that formally defines the spatial relationship between two geometries ($A$ and $B$) by evaluating the intersection dimensions ($0, 1, 2$, or empty) of their Interior, Boundary, and Exterior.</div>
        <div class="pq-exp">DE-9IM forms the mathematical foundation of spatial SQL predicates (<code>ST_Within</code>, <code>ST_Contains</code>, <code>ST_Crosses</code>).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the first computational screening step a spatial DBMS executes before running the ray-casting point-in-polygon test?</div>
        <div class="pq-ans">Answer: The Minimum Bounding Box (MBR / BBOX) test.</div>
        <div class="pq-exp">If the point's coordinates $(x, y)$ fall outside the polygon's simple bounding box ($X_{\text{min}}, Y_{\text{min}}, X_{\text{max}}, Y_{\text{max}}$), the point is instantly rejected without evaluating hundreds of complex boundary vertices.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q147: Raster Data Model (Matrix of Cells Organized into Rows and Columns)
# -----------------------------------------------------------------------------
def gen_q147():
    q_num = 147
    filename = "Q147_Matrix_Of_Cells_Organized_Into_Rows_And_Columns_Raster_Complete_Guide.html"
    title = "Q147: GIS Data Structures - The Raster Data Model"
    badge = "OPSC 2019 Geology Paper-II • Question 147 • GIS Data Structures"
    h1_title = "Geographic Data Structures: Architecture and Principles of the Raster Data Model"
    meta_text = r"<strong>Topic:</strong> GIS Data Models & Grid Architecture • <strong>Key Concept:</strong> Raster Grid Matrix, Rows/Columns, Pixel Resolution & Tessellation • <strong>Textbooks:</strong> Kang-tsung Chang (<em>Introduction to Geographic Information Systems</em>, 9th Ed., Ch. 4); P.A. Burrough & R.A. McDonnell (Ch. 2); K.M. Bangar (p. 216); David J. Buckley (<em>The GIS Primer</em>)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Raster Spatial Data Model</div>
      <p>In Geographic Information Systems (GIS), digital cartography, and digital image processing, spatial reality is encoded in computers using two primary data models: the <strong>Vector Data Model</strong> (which represents features as explicit discrete points, lines, and polygons using coordinate lists) and the <strong>Raster Data Model</strong>.</p>

      <p>By formal GIS definition (Chang; Burrough & McDonnell; Bangar), <strong>a matrix of cells organized into regular rows and columns containing a value representing some information is called a Raster</strong> (Option B):</p>

      <div class="math-block">
        $$\text{Raster Matrix } \mathbf{R} = [Z_{i,j}]_{M \times N} \quad (i = 1, \dots, M \text{ rows}; \quad j = 1, \dots, N \text{ columns})$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Raster Architecture Component</th>
              <th>Mathematical / Structural Property</th>
              <th>Function in GIS Spatial Modeling</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Matrix of Cells (Grid / Pixels)</strong></td>
              <td>Regular orthogonal tessellation of identical rectangular or square cells.</td>
              <td>Exhaustively tiles the entire geographic bounding extent without any gaps or overlaps.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Row and Column Coordinates ($i, j$)</strong></td>
              <td>Integer matrix indices starting at $(0, 0)$ from the Upper-Left corner.</td>
              <td>Implicit spatial position; physical ground coordinates are computed via affine georeferencing: $X = X_0 + j \cdot \Delta x$, $Y = Y_0 - i \cdot \Delta y$.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>Cell Dimension (Spatial Resolution)</strong></td>
              <td>Length of a cell side on the ground ($\Delta x = \Delta y$, e.g. $30\text{ m}$).</td>
              <td>Determines the minimum spatial resolving power; cell area $= (\Delta x)^2$.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>Cell Attribute Value ($Z$)</strong></td>
              <td>Integer (nominal/discrete) or Floating-Point (continuous scalar).</td>
              <td>Stores the physical parameter: elevation (m), spectral radiance, NDVI, soil category, or rock unit code.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q147/raster_matrix_rows_columns_cell_values.png" alt="Raster Data Model Matrix" class="figure-img">
        <div class="figure-caption">Figure 147: Architecture of the Raster Data Model (Option B): an orthogonal matrix of cells structured in rows and columns where every cell stores an attribute value.</div>
      </div>

      <h4>Comparison: Raster Model vs. Other Terminology</h4>
      <ul>
        <li><strong>Raster (Option B):</strong> The universal standard term for space partitioned into regular rows and columns of equal cells.</li>
        <li><strong>Crystal (Option A):</strong> A solid material whose constituent atoms are arranged in a periodic microscopic lattice structure; an optical/mineralogical term having zero meaning as a GIS data model.</li>
        <li><strong>Segment (Option C):</strong> A 1D line element connecting two vertices in vector data models; not a matrix of cells.</li>
        <li><strong>Polygon (Option D):</strong> A 2D closed planar area bounded by coordinate vertex rings in vector models.</li>
      </ul>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 147</div>
        <div class="raw-q-text">A matrix of cells organized into rows and columns containing a value representing some information is called:</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Crystal</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Raster</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Segment</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Polygon</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Raster)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Raster</div>
          <p>By international GIScience and computer graphics definitions (Chang, Ch. 4; Burrough & McDonnell; Bangar, p. 216), a <strong>Raster</strong> (or raster grid) is defined precisely as a cellular matrix organized into a regular grid of rows and columns, where each individual grid cell contains an explicit numerical or categorical value representing geographic phenomena.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Crystal</div>
          <p>A crystal is an ordered solid-state mineral structure with periodic atomic repetition (crystallography). It is not a GIS data model.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Segment</div>
          <p>In vector data structures, a segment is a straight line segment connecting two sequential coordinate vertices along an arc. It is a linear 1D vector entity, not a 2D matrix of cells.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Polygon</div>
          <p>A polygon is a vector geometry defined by a closed sequence of coordinate pairs $(x_1, y_1), \dots, (x_n, y_n)$ enclosing an area. It does not consist of a matrix of rows and columns.</p>
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
              <th>Evaluation Parameter</th>
              <th>Raster Data Model (Option B)</th>
              <th>Vector Data Model (Points, Lines, Polygons)</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Spatial Representation</td><td>Regular matrix of square cells (Pixels)</td><td>Explicit $(X, Y)$ coordinate pairs and nodes</td></tr>
            <tr><td>Best Suited Phenomena</td><td>Continuous fields (DEM, temperature, satellite imagery)</td><td>Discrete entities with sharp boundaries (parcels, roads)</td></tr>
            <tr><td>Data Storage Requirements</td><td>Large file sizes; scales with spatial resolution ($\propto 1/\Delta x^2$)</td><td>Compact file sizes; scales with feature complexity</td></tr>
            <tr><td>Spatial Analysis Strengths</td><td>Rapid cell-by-cell Map Algebra, overlay, surface modeling</td><td>Network routing, topological connectivity, precise boundary cadastral calculation</td></tr>
            <tr><td>Geometric Accuracy & Scale Change</td><td>Subject to pixelation and staircase boundary effects if enlarged</td><td>Resolution-independent; scales smoothly without jagged steps</td></tr>
            <tr><td>Standard File Formats</td><td>GeoTIFF, Esri Grid, IMG, NetCDF, HDF, DEM</td><td>Shapefile, GeoJSON, File Geodatabase, KML, DXF</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. If the spatial resolution (cell size) of a raster grid is halved (e.g. from $30\text{ m}$ to $15\text{ m}$), what happens to the total number of cells and file storage size?</div>
        <div class="pq-ans">Answer: The total number of cells and file size quadruple (increase by a factor of $4$).</div>
        <div class="pq-exp">$$\text{Number of Cells} \propto \frac{1}{(\Delta x)^2} = \left(\frac{30}{15}\right)^2 = 4$$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is a "World File" in raster georeferencing (e.g. <code>.tfw</code>, <code>.jgw</code>)?</div>
        <div class="pq-ans">Answer: A 6-line plain text ASCII sidecar file containing affine transformation parameters: cell size in X and Y, rotation parameters, and ground coordinates of the upper-left pixel center.</div>
        <div class="pq-exp">It enables GIS software to project row/column pixel indices into real-world geographic coordinates.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is Run-Length Encoding (RLE) in raster data compression?</div>
        <div class="pq-ans">Answer: A lossless compression method that records contiguous sequences of identical cell values as a pair: (Count, Value), rather than storing every cell individually.</div>
        <div class="pq-exp">Example: <code>5, 5, 5, 5, 5, 2, 2</code> compresses into <code>(5, 5), (2, 2)</code>, drastically reducing storage for categorical maps.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the difference between an Integer Raster and a Floating-Point Raster?</div>
        <div class="pq-ans">Answer: An integer raster stores whole numbers (discrete categorical data like land use) and can maintain a Value Attribute Table (VAT); a floating-point raster stores decimal numbers (continuous surfaces like DEMs) and cannot have a VAT.</div>
        <div class="pq-exp">Continuous surfaces have infinite unique decimal values, precluding simple attribute frequency tables.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is "Vectorization" vs. "Rasterization"?</div>
        <div class="pq-ans">Answer: Vectorization converts raster grids into vector points, lines, or polygons; rasterization converts vector geometries into a cellular matrix of grid cells.</div>
        <div class="pq-exp">Both are standard data format conversion tools in GIS.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In a Digital Elevation Model (DEM) raster, what algorithm is commonly used to determine flow direction from each cell?</div>
        <div class="pq-ans">Answer: The D8 (Eight-Direction) flow model.</div>
        <div class="pq-exp">It routes surface water from the center cell to the steepest down-slope neighbor among its 8 surrounding cells.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Quadtree data structure in raster GIS?</div>
        <div class="pq-ans">Answer: A hierarchical 2D spatial indexing structure that recursively subdivides space into four quadrants (NW, NE, SW, SE) until all cells within a quadrant have identical values.</div>
        <div class="pq-exp">Quadtrees compress large homogeneous areas while preserving high detail in complex zones.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a "Multi-Band Raster"?</div>
        <div class="pq-ans">Answer: A single raster file comprising multiple geographically co-registered matrix layers (bands), where each band records a distinct spectral wavelength or temporal observation (e.g. Landsat 7-band GeoTIFF).</div>
        <div class="pq-exp">Each individual pixel coordinate $(i, j)$ contains a vector of brightness values across all bands.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q148: Map Projection Families (Cylindrical, Conic, Azimuthal) vs Geographic Coordinate System
# -----------------------------------------------------------------------------
def gen_q148():
    q_num = 148
    filename = "Q148_Not_A_Type_Of_Map_Projection_Geographic_Complete_Guide.html"
    title = "Q148: Cartography - Map Projections vs Coordinate Systems"
    badge = "OPSC 2019 Geology Paper-II • Question 148 • Cartography & Map Projections"
    h1_title = "Mathematical Cartography: The Three Developable Surface Projection Families vs. Geographic Coordinate Systems"
    meta_text = r"<strong>Topic:</strong> Map Projections & Coordinate Systems • <strong>Key Concept:</strong> Developable Surfaces (Cylindrical, Conic, Azimuthal) vs. Geographic Coordinates (GCS) • <strong>Textbooks:</strong> J.P. Snyder (1987, <em>Map Projections: A Working Manual</em>, USGS Paper 1395); Kang-tsung Chang (Ch. 2); P.A. Burrough & R.A. McDonnell (Ch. 2); K.M. Bangar (p. 216)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Developable Surfaces and Map Projections</div>
      <p>Because the Earth is a three-dimensional oblate ellipsoid (or geoid), it cannot be flattened onto a two-dimensional planar sheet without introducing geometric distortion in at least one of four fundamental spatial properties: <strong>Shape (Conformality)</strong>, <strong>Area (Equivalence)</strong>, <strong>Distance (Equidistance)</strong>, or <strong>Direction (Azimuthality)</strong> (Carl Friedrich Gauss's <em>Theorema Egregium</em>).</p>

      <p>A <strong>Map Projection</strong> is a systematic mathematical transformation that maps angular coordinates on the curved ellipsoid $(\phi, \lambda)$ onto planar Cartesian coordinates $(x, y)$ on a flat map sheet. In classical cartography, projections are constructed by projecting the Earth's graticule onto a <strong>developable surface</strong>—a 3D geometric surface that can be cut and unrolled into a flat 2D plane without stretching or tearing (Snyder 1987; Chang; Bangar):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Developable Surface Projection Family</th>
              <th>Geometric Surface Geometry</th>
              <th>Standard Line / Contact</th>
              <th>Optimal Global Application</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td><strong>1. CYLINDRICAL PROJECTION</strong> (Option A)</td>
              <td>A cylinder wrapped around the globe (tangent at Equator or secant at standard parallels).</td>
              <td>Straight horizontal parallels and straight vertical meridians intersecting at $90^\circ$.</td>
              <td>Equatorial and tropical regions, global maritime navigation (<strong>Mercator</strong>, <strong>Transverse Mercator / UTM</strong>).</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>2. CONIC PROJECTION</strong> (Option B)</td>
              <td>A cone placed apex-up over the pole, resting tangent or secant along standard parallels.</td>
              <td>Concentric circular arcs for parallels, radiating straight lines for meridians.</td>
              <td>Mid-latitude east-west continental belts (<strong>Lambert Conformal Conic - LCC</strong>, <strong>Albers Equal Area</strong>).</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>3. AZIMUTHAL (PLANAR) PROJECTION</strong> (Option C)</td>
              <td>A flat tangent or secant plane touching the globe at a single contact point.</td>
              <td>True directions preserved from the center point; concentric circles for parallels.</td>
              <td>Polar regions, global hemispherical views, seismic epicenter mapping (<strong>Stereographic</strong>, <strong>Gnomonic</strong>, <strong>Orthographic</strong>).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>GEOGRAPHIC (GCS)</strong> (Option D &bull; NOT A PROJECTION)</td>
              <td>Unprojected spherical/ellipsoidal 3D datum framework. Coordinates expressed in <strong>angular degrees</strong> ($\text{Latitude } \phi, \text{Longitude } \lambda$).</td>
              <td>No developable surface; does not project onto a flat Cartesian plane.</td>
              <td>Global reference framework (<strong>WGS 84</strong>, Indian Everest 1956). <strong>NOT a map projection!</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q148/map_projection_types_vs_geographic_coordinate_system.png" alt="Map Projection Types vs Geographic Coordinates" class="figure-img">
        <div class="figure-caption">Figure 148: The three fundamental developable surfaces of map projections—Cylindrical (Option A), Conic (Option B), and Azimuthal (Option C)—contrasted with the unprojected 3D Geographic Coordinate System (Option D).</div>
      </div>

      <p>Therefore, while Cylindrical, Conic, and Azimuthal constitute the three classic, universal geometric families of map projections, <strong>Geographic</strong> refers to an unprojected spherical coordinate system, and is <strong>NOT a type of map projection</strong> (Option D).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 148</div>
        <div class="raw-q-text">Which of the following is not a type of map projection ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Cylindrical</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Conic</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Azimuthal</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Geographic</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Geographic)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; NOT A PROJECTION</div>
          <div class="opt-title">Geographic</div>
          <p>A <strong>Geographic Coordinate System (GCS)</strong> (e.g. WGS 84, NAD 83, Everest 1956) is a 3D reference framework that defines locations on the curved Earth ellipsoid using angular units of degrees, minutes, and seconds ($\text{Latitude } \phi, \text{Longitude } \lambda$). It does not use a developable surface and is <strong>not a map projection</strong>. Flat paper maps require projected coordinate systems (PCS).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; VALID PROJECTION TYPE</div>
          <div class="opt-title">Cylindrical</div>
          <p>Cylindrical is one of the three primary developable surface projection families (e.g. Mercator, Transverse Mercator, Plate Carrée). It projects the sphere onto an enveloping cylinder.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; VALID PROJECTION TYPE</div>
          <div class="opt-title">Conic</div>
          <p>Conic is one of the three classic projection families (e.g. Lambert Conformal Conic, Albers Equal Area, Polyconic). It projects the sphere onto a tangent or secant cone.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; VALID PROJECTION TYPE</div>
          <div class="opt-title">Azimuthal</div>
          <p>Azimuthal (also called Planar) is the third primary projection family (e.g. Orthographic, Stereographic, Lambert Azimuthal Equal Area). It projects the sphere onto a flat tangent plane.</p>
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
              <th>Projection Family</th>
              <th>Preserved Metric Property</th>
              <th>Prominent Mathematical Projections</th>
              <th>Primary Practical Use</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;"><td>Cylindrical Conformal</td><td>True local angles and shapes (Conformal)</td><td><strong>Mercator</strong> ($\tan\theta$ expansion), <strong>Universal Transverse Mercator (UTM)</strong></td><td>Marine navigation (Rhumb lines are straight lines); global topographic grid (UTM 6° zones)</td></tr>
            <tr style="background:#eff6ff;"><td>Cylindrical Equal-Area</td><td>True surface areas (Equivalent)</td><td>Gall-Peters, Lambert Cylindrical Equal-Area</td><td>Thematic global population distribution maps</td></tr>
            <tr style="background:#eff6ff;"><td>Conic Conformal</td><td>True local shapes across mid-latitudes</td><td><strong>Lambert Conformal Conic (LCC)</strong></td><td>Survey of India topographic base sheets; aeronautical flight navigation charts</td></tr>
            <tr style="background:#eff6ff;"><td>Conic Equal-Area</td><td>True surface areas across east-west zones</td><td><strong>Albers Equal Area Conic</strong></td><td>National census mapping, agricultural resource distribution</td></tr>
            <tr style="background:#eff6ff;"><td>Azimuthal (Planar)</td><td>True great circle directions from center; Stereographic preserves shape</td><td>Polar Stereographic, Gnomonic (all great circles are straight lines)</td><td>Polar navigation, seismic wave propagation rays</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td>Geographic (GCS)</td><td>None (distorts shape, area, and distance on flat screen)</td><td>Unprojected Latitude/Longitude (Plate Carrée display)</td><td><strong>Global GPS data collection and storage</strong> (WGS 84: EPSG 4326)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. What is the fundamental difference between a Geographic Coordinate System (GCS) and a Projected Coordinate System (PCS)?</div>
        <div class="pq-ans">Answer: A GCS defines locations on a 3D curved ellipsoid using angular degrees (latitude/longitude); a PCS transforms those angular coordinates onto a 2D flat planar surface using linear metric units (meters, feet).</div>
        <div class="pq-exp">GCS uses $(\phi, \lambda)$ in degrees; PCS uses $(X, Y)$ (Easting/Northing) in meters.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the Universal Transverse Mercator (UTM) projection system?</div>
        <div class="pq-ans">Answer: A conformal cylindrical projection where a cylinder is placed transverse (perpendicular) to the Earth's equator, dividing the globe between $80^\circ\text{S}$ and $84^\circ\text{N}$ into 60 longitudinal zones, each $6^\circ$ wide.</div>
        <div class="pq-exp">UTM limits scale distortion to less than $1$ part in $1,000$ by using a central meridian scale factor of $0.9996$.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What projection was traditionally used for the 1:50,000 topographic maps of India by the Survey of India?</div>
        <div class="pq-ans">Answer: The Polyconic projection (on the Everest 1830/1956 ellipsoid), later transitioning to Universal Transverse Mercator (UTM) and Lambert Conformal Conic (LCC) on WGS 84.</div>
        <div class="pq-exp">Polyconic uses a separate cone for every parallel of latitude, making adjacent quadrangle sheets fit together perfectly along north-south borders.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a "Conformal" map projection?</div>
        <div class="pq-ans">Answer: A projection that preserves true local angles, scale factor is independent of direction at any point ($a = b$), and parallels and meridians intersect at $90^\circ$, preserving local shapes.</div>
        <div class="pq-exp">Mercator and Lambert Conformal Conic are conformal; they preserve shapes but distort areas at broad scales.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is an "Equivalent" (Equal-Area) map projection?</div>
        <div class="pq-ans">Answer: A projection that preserves the true relative areal proportions of all geographic features everywhere on the map ($a \cdot b = 1$).</div>
        <div class="pq-exp">No map projection can be simultaneously conformal and equal-area (Tissot's Indicatrix theorem).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. In a Gnomonic azimuthal projection, what unique geometric property do all straight lines possess?</div>
        <div class="pq-ans">Answer: Every straight line drawn on a Gnomonic projection represents a true Great Circle route (the shortest flight distance between two points on the globe).</div>
        <div class="pq-exp">Gnomonic projections are created by projecting rays from the exact center of the Earth.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a "False Easting" and "False Northing" in projected coordinate systems?</div>
        <div class="pq-ans">Answer: Large arbitrary positive numbers added to the origin coordinates (e.g. $500,000\text{ meters}$ False Easting in UTM) to ensure all coordinates within the zone remain positive numbers.</div>
        <div class="pq-exp">This prevents negative coordinate values in computational GIS databases.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is "Tissot's Indicatrix"?</div>
        <div class="pq-ans">Answer: A mathematical graphic tool consisting of small infinitesimal circles on the globe that distort into ellipses on a map projection, revealing the exact magnitude and orientation of angular and areal distortion.</div>
        <div class="pq-exp">On a conformal map, Tissot's indicatrices remain circles of varying sizes; on an equal-area map, they deform into ellipses of constant area.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q149: Cartographic Modeling (Tomlin's Map Algebra & Spatial Operation Flowchart)
# -----------------------------------------------------------------------------
def gen_q149():
    q_num = 149
    filename = "Q149_Cartographic_Modeling_Expressing_Organizing_Methods_Complete_Guide.html"
    title = "Q149: GIS Modeling - Cartographic Modeling and Map Algebra"
    badge = "OPSC 2019 Geology Paper-II • Question 149 • GIS Spatial Modeling"
    h1_title = "Spatial Modeling & Geoprocessing: C. Dana Tomlin's Cartographic Modeling Methodology and Map Algebra"
    meta_text = r"<strong>Topic:</strong> Cartographic Modeling & Map Algebra • <strong>Key Concept:</strong> C. Dana Tomlin's Cartographic Modeling Framework (1990) & Data-Flow Methodology • <strong>Textbooks:</strong> C. Dana Tomlin (1990, <em>Geographic Information Systems and Cartographic Modeling</em>, Prentice Hall); Kang-tsung Chang (Ch. 12); P.A. Burrough & R.A. McDonnell (Ch. 5); K.M. Bangar (p. 219)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: C. Dana Tomlin's Cartographic Modeling</div>
      <p>In Geographic Information Systems (GIS), complex environmental, geological, and regional planning challenges—such as identifying optimal mineral exploration prospects, modeling regional groundwater vulnerability, or locating a new mining tailings dam—cannot be solved by a single isolated tool. They require a chained sequence of interconnected spatial operations.</p>

      <p>The foundational methodological framework for structuring these multi-step spatial workflows was formulated in 1983 and published in 1990 by Professor <strong>C. Dana Tomlin</strong> in his classic text <em>Geographic Information Systems and Cartographic Modeling</em> (Prentice Hall). Tomlin defined <strong>Cartographic Modeling</strong> as (Option B):</p>

      <div class="math-block">
        $$\text{“A general methodology for expressing and organizing methods by which}$$
        $$\text{spatial operations are selected and used to develop a GIS model.”}$$
      </div>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Cartographic Modeling Component</th>
              <th>Role in Spatial Workflow Design</th>
              <th>Concrete Geological Example</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>1. Conceptual Problem Definition</strong></td>
              <td>Translates a real-world physical or environmental question into specific geographic criteria and decision rules.</td>
              <td>Delineating high-probability gold mineralization zones: requires granitic intrusive contacts, fault proximity, and hydrothermal clay alteration.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>2. Data Layer Identification</strong></td>
              <td>Specifies necessary spatial data layers (base inputs).</td>
              <td>Bedrock geology polygon map, structural lineament/fault layer, Landsat SWIR band-ratio alteration raster.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>3. Process Flowchart (Data-Flow Model)</strong></td>
              <td>Draws a visual sequence where data layers flow through analytical spatial operators to generate intermediate derived layers.</td>
              <td>Visual geoprocessing flowchart (e.g. ModelBuilder): Fault lines $\to$ Buffer $\to$ Proximity raster $\to$ Reclassify $\to$ Weighted Overlay.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>4. Map Algebra Execution</strong></td>
              <td>Executes mathematical expressions using Tomlin's four universal classes: Local, Focal, Zonal, and Global operations.</td>
              <td>$$\text{Prospectivity} = 0.4 \times \text{Lithology} + 0.35 \times \text{FaultBuffer} + 0.25 \times \text{Alteration}$$</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q149/cartographic_modeling_spatial_operations_flowchart.png" alt="Cartographic Modeling Process" class="figure-img">
        <div class="figure-caption">Figure 149: Cartographic Modeling architecture (Option B): structuring spatial operations into an organized workflow of input layers, geoprocessing tools, and output decision surfaces.</div>
      </div>

      <p>Cartographic modeling provides a high-level conceptual language independent of specific software syntax, serving as the direct intellectual basis for modern graphical visual workflow tools such as <strong>ArcGIS ModelBuilder</strong>, <strong>QGIS Graphical Modeler</strong>, and automated Python spatial scripts.</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 149</div>
        <div class="raw-q-text">Cartographic modeling is :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> The sequence of modeling of real world entities in a GIS database</div>
          <div class="raw-opt"><span class="opt-letter">B</span> A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model</div>
          <div class="raw-opt"><span class="opt-letter">C</span> A generic method of creating a GIS map data structure</div>
          <div class="raw-opt"><span class="opt-letter">D</span> The modeling of map inputs to a GIS, using programming language</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">A way of expressing and organizing methods by which spatial operations are selected and used to develop a GIS model</div>
          <p>This is the verbatim textbook definition established by Professor C. Dana Tomlin (1990; Chang, Ch. 12; Burrough & McDonnell; Bangar, p. 219). Cartographic modeling is the systematic methodology of organizing and chaining spatial operations (Map Algebra) into a cohesive analytical model to address geographic decision problems.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">The sequence of modeling of real world entities in a GIS database</div>
          <p>Modeling real-world entities into digital computer representation refers to <strong>Spatial Data Modeling</strong> (the conceptual, logical, and physical database design phases, e.g. entity-relationship modeling). It is not cartographic modeling.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">A generic method of creating a GIS map data structure</div>
          <p>Creating data structures refers to defining vector topologies, raster matrices, or TIN triangulations. Cartographic modeling operates *on* existing data structures to solve analytical questions.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">The modeling of map inputs to a GIS, using programming language</div>
          <p>While models can be automated via Python scripts, cartographic modeling is a conceptual, software-neutral methodology for organizing spatial operations, not merely the programming of map inputs.</p>
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
              <th>Spatial Modeling Approach</th>
              <th>Methodological Strategy</th>
              <th>Primary Tool / Framework</th>
              <th>Geological / Environmental Role</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>Cartographic Modeling (Map Algebra)</strong> (Option B)</td><td>Data-flow chaining of Local, Focal, Zonal, and Global operations</td><td>Flowcharts, ModelBuilder, Tomlin's Map Algebra</td><td>Mineral potential prospectivity mapping, landslide hazard zonation</td></tr>
            <tr><td>Index Overlay Model (Weighted Linear Combination)</td><td>Standardizes criteria to common scale, applies percentage weights</td><td>$$\text{Index} = \sum w_i S_i$$</td><td>DRASTIC model for groundwater vulnerability assessment</td></tr>
            <tr><td>Fuzzy Logic Spatial Model</td><td>Assigns continuous membership values ($0 \le \mu \le 1$) using fuzzy operators</td><td>Fuzzy AND, Fuzzy OR, Fuzzy Gamma ($\gamma$)</td><td>Mineral prospectivity mapping with uncertain, incomplete exploration data</td></tr>
            <tr><td>Process-Driven (Dynamic Simulation)</td><td>Solves partial differential physical equations over time ($\Delta t$)</td><td>Hydraulic finite-difference models (MODFLOW)</td><td>Transient contaminant transport, aquifer depletion forecasting</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Who authored the 1990 book "Geographic Information Systems and Cartographic Modeling" that pioneered Map Algebra?</div>
        <div class="pq-ans">Answer: C. Dana Tomlin.</div>
        <div class="pq-exp">Tomlin's doctoral dissertation at Yale and Harvard laid the theoretical foundation for raster GIS spatial analysis.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What are the four fundamental categories of Map Algebra operations defined by C. Dana Tomlin?</div>
        <div class="pq-ans">Answer: Local Operations (individual cell), Focal Operations (neighborhood window), Zonal Operations (irregular zones), and Global Operations (entire raster surface).</div>
        <div class="pq-exp">All complex GIS spatial analyses can be decomposed into combinations of these four operations.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the popular graphical visual workflow tool in modern GIS software that directly implements cartographic modeling flowcharts?</div>
        <div class="pq-ans">Answer: ModelBuilder (in Esri ArcGIS) and the Graphical Modeler (in QGIS).</div>
        <div class="pq-exp">Users drag-and-drop data elements and tools onto a canvas, connecting them with visual arrows to automate multi-step geoprocessing workflows.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the classic DRASTIC cartographic model used for in hydrogeology?</div>
        <div class="pq-ans">Answer: An empirical weighted index model used to evaluate groundwater aquifer pollution vulnerability from surface contaminants.</div>
        <div class="pq-exp">DRASTIC stands for: Depth to water, Recharge, Aquifer media, Soil media, Topography, Impact of vadose zone, and Conductivity.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the difference between a static cartographic model and a dynamic cartographic model?</div>
        <div class="pq-ans">Answer: A static model evaluates spatial conditions at a single instant in time (e.g. slope stability today); a dynamic model incorporates feedback loops and time iterations ($\Delta t$) to simulate evolving phenomena (e.g. oil spill spreading or flood wave propagation).</div>
        <div class="pq-exp">Dynamic modeling uses temporal iteration loops.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is "Sensitivity Analysis" in cartographic modeling?</div>
        <div class="pq-ans">Answer: Systematically varying input layer weights or threshold parameters to evaluate how sensitive the final suitability map is to uncertainties in individual criteria.</div>
        <div class="pq-exp">It identifies which criteria have the greatest influence on model outcomes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the Analytical Hierarchy Process (AHP) used for in GIS multi-criteria evaluation?</div>
        <div class="pq-ans">Answer: A structured mathematical technique (developed by Thomas Saaty) using pairwise comparison matrices to derive objective numerical weights for competing decision criteria.</div>
        <div class="pq-exp">AHP computes a Consistency Ratio (CR) to verify that human expert weighting judgments are logically consistent ($\text{CR} < 0.10$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the "Fuzzy Gamma" ($\gamma$) operator in mineral prospectivity cartographic modeling?</div>
        <div class="pq-ans">Answer: An operator combining the conservative Fuzzy Algebraic Product with the optimistic Fuzzy Algebraic Sum: $\mu_{\text{comb}} = (\mu_{\text{sum}})^\gamma \times (\mu_{\text{product}})^{1-\gamma}$ ($0 \le \gamma \le 1$).</div>
        <div class="pq-exp">Fuzzy Gamma provides flexible compromise between extreme "AND" and "OR" operators, making it ideal for combining geological exploration indicators.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q150: The GIS Data Stream (Raw Spatial Data -> Integrated GIS Database)
# -----------------------------------------------------------------------------
def gen_q150():
    q_num = 150
    filename = "Q150_Data_Stream_Raw_Spatial_Data_Processed_Integrated_GIS_Complete_Guide.html"
    title = "Q150: GIS Data Engineering - The GIS Data Stream"
    badge = "OPSC 2019 Geology Paper-II • Question 150 • GIS Data Engineering"
    h1_title = "GIS Data Engineering: The Architecture, Lifecycle, and Mechanics of the GIS Data Stream"
    meta_text = r"<strong>Topic:</strong> GIS Data Acquisition & Processing Workflows • <strong>Key Concept:</strong> The GIS Data Stream: Ingestion, Verification, Georeferencing & Database Integration • <strong>Textbooks:</strong> P.A. Burrough & R.A. McDonnell (Ch. 1 & 4); Jeffrey Star & John Estes (<em>Geographic Information Systems: An Introduction</em>, Prentice Hall); Kang-tsung Chang (Ch. 1 & 3); K.M. Bangar (p. 216)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The GIS Data Stream Concept</div>
      <p>In spatial data engineering, enterprise geodatabase administration, and GIS implementation, raw field and sensory observations cannot be utilized for spatial analysis immediately upon collection. They must pass through an orderly, multi-stage processing pipeline.</p>

      <p>By authoritative GIS definition (Star & Estes; Burrough & McDonnell; Bangar), <strong>the Data Stream is the sequential operational chain or process by which raw, disparate spatial data is captured, converted, verified, and processed into an integrated, topologically coherent GIS database</strong> (Option A):</p>

      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Data Stream Phase</th>
              <th>Operational Inputs</th>
              <th>Technical Processing & Transformation</th>
              <th>Deliverable to Integrated Database</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff;">
              <td><strong>1. Data Ingestion & Capture</strong></td>
              <td>Field GNSS logs, total station coordinates, satellite telemetry streams, paper geological maps, borehole lithologs.</td>
              <td>Sensor deserialization, optical scanning, vector tablet / on-screen heads-up digitizing.</td>
              <td>Raw coordinate strings and uncalibrated digital raster arrays.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>2. Geometric Preprocessing & Georeferencing</strong></td>
              <td>Unprojected pixel grids $(i, j)$ and raw arbitrary CAD drawings.</td>
              <td>Ground Control Point (GCP) matching, affine coordinate transformation, datum conversion (Everest $\to$ WGS 84), map projection.</td>
              <td>Planimetrically accurate, georeferenced spatial layers with metric coordinates.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>3. Topological Cleaning & Error Correction</strong></td>
              <td>Digitized vector lines with overshoots, undershoots, dangling nodes, and unclosed polygon boundaries.</td>
              <td>Fuzzy node snapping, dangling node pruning, planar enforcement, duplicate vertex elimination.</td>
              <td>Topologically valid point, arc, and polygon features satisfying topological integrity rules.</td>
            </tr>
            <tr style="background:#eff6ff;">
              <td><strong>4. Attribute Standardization & Verification</strong></td>
              <td>Field notebooks, laboratory geochemical assay spreadsheets, mineral lease records.</td>
              <td>Data type validation, normalization, domain enforcement, Primary-Key linkage to spatial geometry.</td>
              <td>Structured attribute tables seamlessly joined to spatial vector features.</td>
            </tr>
            <tr style="background:#eff6ff; font-weight:700;">
              <td><strong>5. Enterprise Database Integration</strong> (The Goal)</td>
              <td>Cleaned spatial geometries + validated attribute tables + metadata.</td>
              <td>Spatial indexing (R-Tree/GiST), versioning setup, user access control, ISO 19115 metadata cataloguing.</td>
              <td><strong>Integrated GIS Database</strong> ready for multi-user spatial query, Map Algebra, and cartographic publishing.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q150/gis_data_stream_raw_spatial_data_to_integrated_database.png" alt="The GIS Data Stream" class="figure-img">
        <div class="figure-caption">Figure 150: The complete GIS Data Stream pipeline (Option A): from raw spatial data acquisition through georeferencing, topological validation, and attribute standardization into an Integrated Enterprise GIS Database.</div>
      </div>

      <p>Data engineering studies consistently demonstrate that the <strong>data stream</strong> accounts for <strong>$60\%\text{ to } 80\%$ of the total time, labor, and budget</strong> of any major enterprise GIS implementation project (Burrough; Star & Estes). Without a rigorous data stream, analytical queries suffer from "Garbage In, Garbage Out" (GIGO).</p>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 150</div>
        <div class="raw-q-text">Data stream means :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> The process by which raw spatial data is processed into an integrated GIS database</div>
          <div class="raw-opt"><span class="opt-letter">B</span> The flow of data from one user to another</div>
          <div class="raw-opt"><span class="opt-letter">C</span> The process by which maps are transferred between GIS platforms</div>
          <div class="raw-opt"><span class="opt-letter">D</span> The flow of data from user to GIS platform</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (The process by which raw spatial data is processed into an integrated GIS database)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; CORRECT</div>
          <div class="opt-title">The process by which raw spatial data is processed into an integrated GIS database</div>
          <p>In GIS data engineering and spatial system design (Star & Estes, 1990; Burrough & McDonnell; Bangar, p. 216), the <strong>data stream</strong> refers explicitly to the sequential end-to-end processing pipeline through which raw, heterogeneous spatial data (digitized coordinates, field notes, satellite feeds) is converted, structured, verified, and integrated into a standardized GIS spatial database.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">The flow of data from one user to another</div>
          <p>Data flow between human users represents interpersonal communication, email sharing, or collaboration workflows, not the foundational GIS data stream processing architecture.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">The process by which maps are transferred between GIS platforms</div>
          <p>Transferring maps between platforms is <strong>Data Interoperability</strong>, spatial ETL (Extract-Transform-Load), or file format conversion (e.g. Shapefile to GeoPackage), not the data stream.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">The flow of data from user to GIS platform</div>
          <p>This describes user data entry or GUI user interaction, which is merely a tiny sub-step of data ingestion rather than the complete data processing stream.</p>
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
              <th>Data Pipeline Concept</th>
              <th>Scope & Function</th>
              <th>Key Standard / Protocol</th>
              <th>Practical Objective</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#eff6ff; font-weight:700;"><td><strong>GIS Data Stream</strong> (Option A)</td><td>Sequential pipeline: Acquisition $\to$ Rectification $\to$ Topology $\to$ Integration</td><td>Enterprise GIS Data Ingestion SOPs</td><td>Transforms raw, unstructured field measurements into clean, integrated database layers</td></tr>
            <tr><td>Spatial ETL (Extract-Transform-Load)</td><td>Automated data translation between disparate enterprise database formats</td><td>FME (Feature Manipulation Engine), GDAL/OGR</td><td>Migrates legacy CAD and CSV datasets into an enterprise geodatabase</td></tr>
            <tr><td>Real-Time Data Streaming</td><td>Continuous ingestion of live telemetry data from active sensors</td><td>OGC Sensor Observation Service (SOS), MQTT, Kafka</td><td>Live monitoring of earthquake ground shaking, flood gauges, tracking mining vehicles</td></tr>
            <tr><td>Data Harmonization</td><td>Standardizing heterogeneous schemas and naming conventions across agencies</td><td>INSPIRE Data Specifications, NSDI standards</td><td>Enables national seamless compilation of state geological maps</td></tr>
          </tbody>
        </table>
      </div>

      <div class="pq-item">
        <div class="pq-q">1. Why is the GIS Data Stream typically estimated to consume $60\%\text{ to } 80\%$ of total project resources in any major GIS implementation?</div>
        <div class="pq-ans">Answer: Because spatial data acquisition, manual digitization, georeferencing, topological error correction, and tabular attribute standardization are labor-intensive and require meticulous quality control.</div>
        <div class="pq-exp">Software and hardware purchases are minor compared to the cost of creating clean, authoritative spatial datasets.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What are the common topological errors that must be eliminated during the vector data stream before database integration?</div>
        <div class="pq-ans">Answer: Undershoots (lines failing to connect to an intersection), Overshoots (lines extending past the intersection as dangles), unclosed polygons, self-intersecting loops, and duplicate coincident lines.</div>
        <div class="pq-exp">Topological cleaning ensures lines form valid network nodes and closed polygon boundaries.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What does "Planar Enforcement" mean in vector data stream processing?</div>
        <div class="pq-ans">Answer: The topological rule stating that all intersecting lines must create a node at their intersection, and no two polygons in the same layer can overlap.</div>
        <div class="pq-exp">Planar enforcement ensures space is completely partitioned without overlapping spatial ambiguities.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is GDAL/OGR in modern geospatial data engineering?</div>
        <div class="pq-ans">Answer: Geospatial Data Abstraction Library (GDAL for raster, OGR for vector); the industry-standard open-source C++ translator library used to read, convert, and stream over 200 geospatial data formats.</div>
        <div class="pq-exp">GDAL powers the data input/output engines of QGIS, ArcGIS, Google Earth, and Python GeoPandas.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the role of Data Quality Assurance / Quality Control (QA/QC) in the GIS data stream?</div>
        <div class="pq-ans">Answer: Verifying Positional Accuracy (against high-precision ground GNSS control), Attribute Accuracy (checking assay grades against lab certificates), Completeness, and Logical Consistency.</div>
        <div class="pq-exp">QA/QC ensures the integrated database meets national mapping accuracy standards.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How does "Heads-Up Digitizing" differ from "Heads-Down Digitizing" in data stream workflows?</div>
        <div class="pq-ans">Answer: Heads-up digitizing traces features directly on a computer monitor over a georeferenced raster backdrop using a mouse; heads-down digitizing manually traces paper maps taped to an electromagnetic digitizing tablet using a handheld puck.</div>
        <div class="pq-exp">Heads-up digitizing has completely replaced cumbersome manual digitizer tablets.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is "Rubber Sheeting" in spatial data preprocessing?</div>
        <div class="pq-ans">Answer: A non-linear geometric adjustment technique that stretches, warps, and fits historical distorted maps to modern georeferenced control points like a sheet of flexible rubber.</div>
        <div class="pq-exp">It eliminates non-uniform paper shrinkage and distortion in historical colonial mine plans.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is the final step in the GIS data stream before deploying the database to end users?</div>
        <div class="pq-ans">Answer: Metadata authoring and catalog registration (documenting coordinate reference system, lineage, accuracy, and creator contact details).</div>
        <div class="pq-exp">Without metadata, future users cannot evaluate the suitability or legal reliability of the spatial dataset.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Solutions Batch 10 Part D (Q144 - Q150)...")
    gen_q144()
    gen_q145()
    gen_q146()
    gen_q147()
    gen_q148()
    gen_q149()
    gen_q150()
    print("Batch 10 Part D successfully generated!")
