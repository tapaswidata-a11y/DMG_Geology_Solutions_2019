#!/usr/bin/env python3
"""
Q135 Generator: Digital Data Creation Methods in GIS: Digitization & Orthoimagery
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q135():
    title = r"Q135: GIS & Remote Sensing: Digital Data Creation Methods | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q135: Digital GIS Data Creation: Vector Digitization and Orthorectified Imagery"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 135<br>
<strong>Authoritative References:</strong> Thomas M. Lillesand, Ralph W. Kiefer, and Jonathan W. Chipman, <em>Remote Sensing and Image Interpretation</em> (7th Ed., Wiley, Ch. 3: Photogrammetry & Orthophotos, pp. 120–175); Kang-tsung Chang, <em>Introduction to Geographic Information Systems</em> (9th Ed., Ch. 5: GIS Data Acquisition, pp. 95–124); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS, p. 220); Paul R. Wolf and Bon A. Dewitt, <em>Elements of Photogrammetry with Applications in GIS</em>."""

    part1 = r"""
  <!-- CARD 1: OVERVIEW OF DIGITAL DATA CREATION IN GIS -->
  <div class="card">
    <div class="card-header bg-blue">1. Architecture of Digital Data Creation: Primary vs. Secondary Spatial Capture</div>
    <div class="card-body">
      <p>
        In Geographic Information Systems (GIS), digital photogrammetry, and geoinformatics, <strong>digital data creation</strong> is the operational process of encoding geographical phenomena into computer-readable digital spatial formats (vector geometries and georeferenced raster datasets) (Chang, 2019; Lillesand et al., 2015; Bangar, p. 220).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q135/gis_digital_data_creation_digitization_orthoimagery.png" alt="Digital Data Creation: Digitization and Orthorectified Imagery">
        <div class="figure-caption">
          <strong>Figure 135.1 — Digital Spatial Data Creation Pathways:</strong> Two premier methods for digital GIS data creation: (A) Heads-up / manual Digitization of spatial vector primitives from existing maps, and (B) Photogrammetrically corrected Orthorectified Aerial/Satellite Imagery providing uniform scale base maps.
        </div>
      </div>

      <h4>The Two Primary Methods in Digital GIS Data Creation</h4>
      <p>
        As codified in standard geoinformatics curricula, the creation of GIS databases relies fundamentally on:
      </p>
      <ul>
        <li>
          <strong>1. Digitization (Vector Data Creation):</strong>
          The process of converting geographic features from analog paper maps, aerial photos, or field survey field-sheets into digital vector formats (Points, Lines, Polygons):
          <ul>
            <li><em>Heads-Up (On-Screen) Digitization:</em> Tracing features directly on a high-resolution computer monitor over georeferenced raster basemaps, DEMs, or satellite scenes using a mouse or graphics stylus.</li>
            <li><em>Tablet Digitization:</em> Mounting historical hardcopy paper maps on an electromagnetic digitizing tablet and tracing features with a high-precision multi-button cursor (puck).</li>
            <li><em>Automated / Semi-Automated Vectorization:</em> Employing pattern recognition and edge-detection algorithms to convert scanned black-and-white contour sheets into vector polylines.</li>
          </ul>
        </li>
        <li>
          <strong>2. Orthorectified Imagery (Raster Data Creation & Base Layer):</strong>
          Raw aerial photographs and high-resolution satellite imagery contain severe geometric distortions caused by camera tilt, optical lens aberrations, and terrain relief displacement:
          <ul>
            <li><em>Orthorectification:</em> A rigorous photogrammetric process that mathematically rectifies every pixel using exterior orientation parameters, camera calibration data, and a high-resolution <strong>Digital Elevation Model (DEM)</strong> to eliminate relief displacement ($d = r \cdot h / H$).</li>
            <li>The resulting <strong>Orthophoto / Orthoimage</strong> possesses a planimetrically uniform scale across its entire extent, functioning as a true map upon which distances, angles, and surface areas can be directly measured.</li>
            <li>It serves both as an independent digital raster data product and the premier visual backdrop for heads-up digitization of geological formations, structures, roads, and land parcels.</li>
          </ul>
        </li>
      </ul>

      <div class="figure-box">
        <img src="../../figures_Q135/bangar_p220_digital_data_creation_digitization.png" alt="Digital Data Creation from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 135.2 — Digital Data Creation in Engineering Geology:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 220). Outlines digital GIS data capture methods, emphasizing digitization and orthorectified imagery while excluding telecommunication demodulation.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE NATURE OF DEMODULATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Why Demodulation is Completely Irrelevant to GIS Data Creation</div>
    <div class="card-body">
      <h4>Electronic Communications vs. Spatial Data Science</h4>
      <p>
        Option (C) introduces the term <strong>Demodulation</strong>, which is an electronic engineering concept with zero function in GIS digital data creation:
      </p>
      <ul>
        <li><strong>Definition of Demodulation:</strong> In telecommunications and electronic signal processing, demodulation is the inverse process of modulation. It extracts the original baseband information-bearing signal (voice, audio, binary data) from a high-frequency analog carrier radio wave (e.g., in AM/FM radio receivers, optical fiber transceivers, or DSL telephone modems).</li>
        <li><strong>Absence in Spatial Modeling:</strong> Demodulation creates no geographical geometries, builds no vector primitives, rectifies no aerial imagery, and populates no GIS attribute tables. It was deliberately inserted into the exam paper as an acoustic/electronic distractor to test candidate vocabulary discernment.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: GEOMETRIC CORRECTION & PHOTOGRAMMETRIC RECTIFICATION -->
  <div class="card">
    <div class="card-header bg-indigo">3. Photogrammetric Rectification: Eliminating Relief Displacement</div>
    <div class="card-body">
      <h4>Mathematical Mechanics of Relief Displacement ($d$)</h4>
      <p>
        In an unrectified aerial photograph, high terrain points are displaced radially outward from the nadir/principal point, while depressions are displaced inward:
      </p>
      <div class="math-block">
        $$d = \frac{r \cdot h}{H}$$
        $$\text{where: } d = \text{Relief displacement (mm)}, \quad r = \text{Radial distance from principal point (mm)},$$
        $$h = \text{Terrain elevation above datum (m)}, \quad H = \text{Flying height of aircraft above datum (m)}$$
      </div>
      <p>
        Because relief displacement alters apparent distances, an unrectified aerial photo cannot be used as an accurate spatial GIS layer. Orthorectification applies the collinearity equations on a pixel-by-pixel basis using a DEM to project every pixel into its true orthogonal map location:
      </p>
      <div class="math-block">
        $$x - x_0 = -f \left[\frac{m_{11}(X - X_L) + m_{12}(Y - Y_L) + m_{13}(Z - Z_L)}{m_{31}(X - X_L) + m_{32}(Y - Y_L) + m_{33}(Z - Z_L)}\right]$$
        $$y - y_0 = -f \left[\frac{m_{21}(X - X_L) + m_{22}(Y - Y_L) + m_{23}(Z - Z_L)}{m_{31}(X - X_L) + m_{32}(Y - Y_L) + m_{33}(Z - Z_L)}\right]$$
      </div>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card question-card">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-number">Question 135</div>
      <div class="question-text">
        Which digital data creation methods are used for GIS data creation ?
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Digitization</li>
        <li class="option-item"><strong>(B)</strong> Orthorectified imagery</li>
        <li class="option-item"><strong>(C)</strong> Demodulation</li>
        <li class="option-item correct"><strong>(D)</strong> Both (A) and (B)</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (D) Both (A) and (B)</strong> — Both Digitization (the primary vector capture method) and Orthorectified Imagery (the premier photogrammetric raster base layer and image capture technique) are standard digital GIS data creation methods.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Digitization — Correct Method, but Incomplete</div>
        <p>
          Digitization is the fundamental technique used to convert analog graphic features (paper geological maps, survey plans) into digital vector geometries (Points, Lines, Polygons) via manual heads-up screen tracing or digitizing tablets. However, selecting Option (A) alone fails to recognize that Orthorectified Imagery is equally an indispensable digital creation method.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Orthorectified imagery — Correct Method, but Incomplete</div>
        <p>
          Orthorectified imagery (orthophotography) is generated by correcting raw aerial or satellite images for camera tilt and terrain relief displacement using photogrammetry and DEMs. It produces true planimetric digital raster layers that serve as direct spatial datasets and primary basemaps. Selecting (B) alone is incomplete.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (C): Demodulation — Complete Technical Fallacy</div>
        <p>
          Demodulation is an electronic hardware process used in radio communication systems and modems to recover an analog or digital information signal from a high-frequency carrier wave. It has no application in spatial GIS data creation.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (D): Both (A) and (B) — Fully Verified & Comprehensive Answer</div>
        <p>
          In Geographic Information Systems literature (Bangar, p. 220; Chang, Ch. 5; Lillesand et al.):
        </p>
        <ol>
          <li><strong>Digitization</strong> provides the primary vector capture pipeline.</li>
          <li><strong>Orthorectified imagery</strong> provides the primary raster capture and photogrammetric basemap pipeline.</li>
        </ol>
        <p>Therefore, Option (D) correctly identifies both established spatial data creation techniques.</p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Matrix: Digital Spatial Data Creation Methods in GIS</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Method</th>
            <th>Primary Output Format</th>
            <th>Source Material</th>
            <th>Key Equipment / Software</th>
            <th>Geological Application</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Heads-Up (On-Screen) Digitization</strong></td>
            <td>Vector (Points, Polylines, Polygons)</td>
            <td>Scanned geological maps, orthoimagery, DEM hillshades</td>
            <td>GIS software (QGIS, ArcGIS), high-resolution monitors, graphics tablet</td>
            <td>Tracing fault systems, lithological boundaries, dyke swarms, mining lease perimeters.</td>
          </tr>
          <tr>
            <td><strong>Orthorectified Imagery (Photogrammetry)</strong></td>
            <td>Raster (GeoTIFF, ECW, IMG with planimetric metric scale)</td>
            <td>Raw aerial photos, satellite imagery (WorldView, Sentinel, Landsat) + DEM</td>
            <td>Digital photogrammetry workstations, bundle block adjustment software</td>
            <td>Planimetrically accurate visual base maps, regional structural mapping, open-pit pit wall monitoring.</td>
          </tr>
          <tr>
            <td><strong>Tablet Manual Digitization</strong></td>
            <td>Vector (Points, Lines, Polygons)</td>
            <td>Original historical paper maps, archival mylar sheets</td>
            <td>Electromagnetic digitizer table ($36'' \times 48''$), 16-button puck cursor</td>
            <td>Legacy map conservation; converting pre-digital paper geological maps.</td>
          </tr>
          <tr>
            <td><strong>Automated Vectorization</strong></td>
            <td>Vector Polylines</td>
            <td>High-contrast binary scanned raster contour sheets</td>
            <td>Raster-to-vector tracing algorithms, center-line thinning filters</td>
            <td>Mass conversion of topographic elevation contours.</td>
          </tr>
          <tr>
            <td><strong>GNSS / GPS Field Surveying</strong></td>
            <td>Vector (3D Points & Tracks)</td>
            <td>Direct in-situ satellite signal acquisition</td>
            <td>Differential GPS / RTK receivers ($< 1\text{ cm}$ precision)</td>
            <td>Drill hole collar surveying, claim boundary pegging, geological outcrop ground-truthing.</td>
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
        <strong>Problem 1: Photogrammetric Relief Displacement Calculation</strong><br>
        A vertical aerial photograph is taken from an aircraft flying at an altitude $H = 3000\text{ m}$ above sea level datum with a camera of focal length $f = 152.4\text{ mm}$. A mountain summit has an elevation of $h = 450\text{ m}$ above datum. On the photograph, the image of the summit is measured at a radial distance $r = 85.0\text{ mm}$ from the principal point. Calculate the relief displacement ($d$) of the summit image in millimeters.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Use the relief displacement formula:
          $$d = \frac{r \cdot h}{H}$$
          2. Substitute given values ($r = 85.0\text{ mm}, h = 450\text{ m}, H = 3000\text{ m}$):
          $$d = \frac{85.0\text{ mm} \times 450\text{ m}}{3000\text{ m}} = \frac{38,250}{3000} = 12.75\text{ mm}$$
          The mountain summit is displaced radially outward from its true planimetric position by $12.75\text{ mm}$. Orthorectification shifts this pixel back by exactly $12.75\text{ mm}$.
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Ground Sampling Distance (GSD) of Digital Orthoimagery</strong><br>
        A digital aerial photogrammetric camera has a focal length $f = 100.0\text{ mm}$ and a CCD sensor pixel size of $p = 5.2\ \mu\text{m}$ ($0.0052\text{ mm}$). If the survey aircraft flies at an altitude $H = 1500\text{ m}$ above average terrain ground level, calculate the Ground Sampling Distance (GSD) of the resulting raw imagery in centimeters per pixel.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate scale of the aerial photograph ($S$):
          $$S = \frac{f}{H} = \frac{0.100\text{ m}}{1500\text{ m}} = \frac{1}{15,000}$$
          2. Calculate Ground Sampling Distance (GSD):
          $$\text{GSD} = \frac{p}{S} = p \times \left(\frac{H}{f}\right) = 0.0052\text{ mm} \times 15,000 = 78.0\text{ mm} = 7.80\text{ cm/pixel}$$
          The spatial resolution of the orthophoto is $7.8\text{ cm}$ per pixel.
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: Minimum Ground Control Points (GCPs) for Polynomial Rectification</strong><br>
        When georeferencing and rectifying an unprojected scanned historical geological map into a 2D projected coordinate system, the general 2D polynomial transformation of order $n$ requires a minimum number of Ground Control Points ($N$) given by:
        $$N_{\text{min}} = \frac{(n + 1)(n + 2)}{2}$$
        Calculate the minimum number of GCPs required for: (a) a 1st-order Affine transformation, (b) a 2nd-order polynomial transformation, and (c) a 3rd-order projective transformation.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. 1st-Order Affine ($n = 1$):
          $$N_{\text{min}} = \frac{(1 + 1)(1 + 2)}{2} = \frac{2 \times 3}{2} = 3\text{ GCPs (minimum 4 recommended for redundancy)}$$
          2. 2nd-Order Polynomial ($n = 2$):
          $$N_{\text{min}} = \frac{(2 + 1)(2 + 2)}{2} = \frac{3 \times 4}{2} = 6\text{ GCPs}$$
          3. 3rd-Order Polynomial ($n = 3$):
          $$N_{\text{min}} = \frac{(3 + 1)(3 + 2)}{2} = \frac{4 \times 5}{2} = 10\text{ GCPs}$$
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Root Mean Square Error (RMSE) of Georeferencing Control Points</strong><br>
        A scanned geological map is georeferenced using four Ground Control Points (GCPs). The measured residual errors in Easting ($\Delta X$) and Northing ($\Delta Y$) in meters are:
        GCP 1: $\Delta X = +1.2\text{ m}, \Delta Y = -0.8\text{ m}$;
        GCP 2: $\Delta X = -1.5\text{ m}, \Delta Y = +1.0\text{ m}$;
        GCP 3: $\Delta X = +0.6\text{ m}, \Delta Y = +1.4\text{ m}$;
        GCP 4: $\Delta X = -0.9\text{ m}, \Delta Y = -1.1\text{ m}$.
        Calculate: (a) $\text{RMSE}_x$, (b) $\text{RMSE}_y$, and (c) Total Planimetric $\text{RMSE}_{\text{total}}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Compute sum of squared residuals:
          $$\sum \Delta X^2 = (1.2)^2 + (-1.5)^2 + (0.6)^2 + (-0.9)^2 = 1.44 + 2.25 + 0.36 + 0.81 = 4.86\text{ m}^2$$
          $$\sum \Delta Y^2 = (-0.8)^2 + (1.0)^2 + (1.4)^2 + (-1.1)^2 = 0.64 + 1.00 + 1.96 + 1.21 = 4.81\text{ m}^2$$
          2. Compute component RMSEs ($N = 4$):
          $$\text{RMSE}_x = \sqrt{\frac{4.86}{4}} = \sqrt{1.215} \approx 1.102\text{ m}$$
          $$\text{RMSE}_y = \sqrt{\frac{4.81}{4}} = \sqrt{1.2025} \approx 1.097\text{ m}$$
          3. Total Planimetric RMSE:
          $$\text{RMSE}_{\text{total}} = \sqrt{\text{RMSE}_x^2 + \text{RMSE}_y^2} = \sqrt{1.215 + 1.2025} = \sqrt{2.4175} \approx 1.555\text{ m}$$
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: Vector Snapping Tolerance Configuration</strong><br>
        During heads-up manual digitization of geological faults, a GIS operator sets a snapping tolerance of $d_{\text{snap}} = 5\text{ screen pixels}$ at a display scale where $1\text{ pixel} = 2.0\text{ meters on ground}$. If an incoming fault polyline endpoint terminates at a ground distance of $8.5\text{ meters}$ from an existing regional shear zone, determine whether the GIS vertex-snapping engine will automatically snap the endpoint to close the node.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate ground snapping distance:
          $$D_{\text{snap}} = 5\text{ pixels} \times 2.0\text{ m/pixel} = 10.0\text{ meters}$$
          2. Compare endpoint distance to tolerance:
          $$\text{Actual distance } d = 8.5\text{ m} < D_{\text{snap}} = 10.0\text{ m}$$
          <em>Conclusion:</em> Because $8.5\text{ m} \le 10.0\text{ m}$, the endpoint lies inside the active snapping radius. The GIS engine <strong>will automatically snap</strong> the vertex to the existing line, successfully avoiding an undershoot topological error.
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Uncompressed File Size of High-Resolution Orthoimagery</strong><br>
        A regional mineral belt covering an area of $20\text{ km} \times 15\text{ km}$ is surveyed to produce an orthorectified digital image mosaic with a Ground Sampling Distance of $\text{GSD} = 0.5\text{ m/pixel}$. The image has 4 spectral bands (Blue, Green, Red, Near-Infrared), each quantized to 8-bit radiometric resolution ($1\text{ byte per pixel per band}$). Calculate the uncompressed file size of the digital orthoimage in Gigabytes ($\text{GB}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Image pixel dimensions:
          $$\text{Columns } X = \frac{20,000\text{ m}}{0.5\text{ m/pix}} = 40,000\text{ pixels}$$
          $$\text{Rows } Y = \frac{15,000\text{ m}}{0.5\text{ m/pix}} = 30,000\text{ pixels}$$
          $$\text{Total pixels per band} = 40,000 \times 30,000 = 1,200,000,000\text{ pixels (1.2 Gigapixels)}$$
          2. Total file size for 4 bands at $1\text{ byte/pix/band}$:
          $$\text{Bytes} = 1.2 \times 10^9 \times 4 \times 1\text{ byte} = 4.8 \times 10^9\text{ bytes}$$
          Convert to Gigabytes ($\text{GB}$, where $1\text{ GB} = 10^9\text{ bytes}$ or $1\text{ GiB} = 2^{30}\text{ bytes}$):
          $$\text{File Size} = \frac{4.8 \times 10^9}{10^9} = 4.80\text{ GB}$$
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Undershoot and Overshoot Topological Clean-Up</strong><br>
        After automated vectorization of a scanned drainage network, automated topological validation detects 42 "dangle nodes" (dead-end lines). Inspection reveals:
        - 28 dangles represent natural stream spring heads (valid first-order tributaries).
        - 10 dangles are undershoots that stopped short of intersecting the main river trunk.
        - 4 dangles are overshoots that crossed past the main river trunk due to tracing inertia.
        Determine: (a) how many errors must be topologically corrected, and (b) what automated geoprocessing tool is executed to fix the undershoots within a $15\text{ m}$ search distance.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Topological errors to correct:
          $$\text{Errors} = 10\text{ undershoots} + 4\text{ overshoots} = 14\text{ topological errors}$$
          (The 28 natural headwater springs are genuine geographic endpoints and must be preserved).
          2. Automated Geoprocessing Tool:
          Execute the <strong>Extend Line</strong> tool (with an extension length of $15.0\text{ m}$) to snap the 10 undershoots to the main channel, followed by the <strong>Trim Line</strong> tool to eliminate the 4 overshoots.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Drone Photogrammetry Flight Line Overlap Calculation</strong><br>
        An unmanned aerial vehicle (UAV / Drone) surveys an open-pit iron ore quarry for orthoimagery generation. The flight lines are planned with $75\%$ forward longitudinal overlap and $60\%$ lateral side overlap. If the camera footprint on the ground at the design flying height covers an area of $240\text{ m} \times 160\text{ m}$ ($240\text{ m}$ across-track $\times 160\text{ m}$ along-track), calculate: (a) the forward air base advance distance between successive photo triggers, and (b) the line spacing between adjacent parallel flight traverses.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Forward advance distance between photos ($75\%$ overlap):
          $$\text{Forward advance } B = (1 - 0.75) \times 160\text{ m} = 0.25 \times 160\text{ m} = 40.0\text{ meters}$$
          2. Lateral line spacing between flight lines ($60\%$ side overlap):
          $$\text{Line spacing } W = (1 - 0.60) \times 240\text{ m} = 0.40 \times 240\text{ m} = 96.0\text{ meters}$$
          The drone triggers an image every $40\text{ m}$ along flight lines spaced $96\text{ m}$ apart to ensure seamless stereoscopic overlap for orthorectification.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=135,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q135_Digital_GIS_Data_Creation_Methods_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q135: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q135()
