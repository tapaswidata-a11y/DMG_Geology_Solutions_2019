#!/usr/bin/env python3
"""
Q137 Generator: Spatio-Temporal GIS & Time as the Fourth Dimension
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q137():
    title = r"Q137: GIS & Geoinformatics: Time as the Fourth Dimension | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • GIS, Cartography & Geoinformatics"
    h1_title = "Q137: Spatio-Temporal Modeling: Conceptualizing Time (T) as the Fourth Dimension in GIS"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 137<br>
<strong>Authoritative References:</strong> Michael F. Worboys and Matt Duckham, <em>GIS: A Computing Perspective</em> (2nd Ed., CRC Press, Ch. 6: Spatio-Temporal Models, pp. 240–285); Gail Langran, <em>Time in Geographic Information Systems</em> (Taylor & Francis); Donna J. Peuquet, <em>Representing Space and Time in GIS</em>; K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 11: GIS, p. 222)."""

    part1 = r"""
  <!-- CARD 1: TIME AS THE FOURTH DIMENSION -->
  <div class="card">
    <div class="card-header bg-blue">1. Conceptual Foundations: Introducing the Fourth Dimension (Time) into GIS</div>
    <div class="card-body">
      <p>
        In Geographic Information Science (GIScience), digital geoinformatics, and dynamic earth system modeling, <strong>Time ($T$) is universally recognized and designated as the Fourth Dimension in GIS</strong> (Worboys & Duckham, 2004; Langran, 1992; Bangar, p. 222).
      </p>

      <div class="figure-box">
        <img src="../../figures_Q137/spatio_temporal_gis_4th_dimension_time.png" alt="Spatio-Temporal GIS: Time as the Fourth Dimension">
        <div class="figure-caption">
          <strong>Figure 137.1 — Spatio-Temporal Data Architecture (4D GIS):</strong> Synthesis of 3-dimensional spatial coordinate geometry $(X, Y, Z)$ with the continuous chronological axis $(T)$, forming the 4D hypercube $(X, Y, Z, T)$ necessary to model dynamic geological processes such as seismic rupture, groundwater plume advection, and open-pit mine excavation progression.
        </div>
      </div>

      <h4>The Evolution from Static 2D/3D Maps to Dynamic 4D Systems</h4>
      <p>
        Traditional GIS architectures were fundamentally static:
      </p>
      <ul>
        <li><strong>2D Spatial GIS:</strong> Modeled geographic space using horizontal planar Cartesian coordinates $(X, Y)$ (Easting, Northing).</li>
        <li><strong>3D Spatial GIS:</strong> Integrated topographic elevation or subterranean depth $(Z)$, yielding $(X, Y, Z)$ spatial coordinates.</li>
        <li><strong>4D Spatio-Temporal GIS:</strong> Integrates chronological <strong>Time ($T$)</strong>, formulating every real-world phenomenon as a multi-dimensional function:
          <div class="math-block">
            $$\text{Geographic State } S = f(X, Y, Z, T)$$
          </div>
        </li>
      </ul>
      <p>
        Because Earth is a dynamic, continuously evolving planet, static snapshots fail to capture rates of change, causality, or cyclical periodicity. Integrating Time empowers GIS to analyze not only <em>"where"</em> something is, but <em>"when"</em> it occurred, <em>"how fast"</em> it changes, and <em>"where"</em> it will migrate in the future.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q137/bangar_p222_gis_fourth_dimension_time.png" alt="Fourth Dimension in GIS from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 137.2 — The Fourth Dimension in GIS:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 222). Confirms: <em>"Time is considered the fourth dimension in GIS, transforming static spatial models into spatio-temporal systems $(X, Y, Z, T)$."</em>
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: DYNAMIC GEOLOGICAL PROCESSES REQUIRING 4D GIS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Dynamic Geoscience Applications Requiring 4-Dimensional Spatio-Temporal GIS</div>
    <div class="card-body">
      <p>
        In geology, hydrogeology, and geophysics, incorporating the temporal dimension ($T$) is mandatory for modeling non-stationary processes:
      </p>
      <ul>
        <li><strong>Earthquake Seismology & Fault Rupture:</strong> Propagating seismic shear and compressional wavefronts away from a hypocenter $(X_0, Y_0, Z_0)$ at origin time $T_0$, tracking stress redistribution along fault segments over milliseconds to centuries.</li>
        <li><strong>Hydrogeology & Contaminant Transport:</strong> Advective-dispersive migration of toxic industrial leachate or heavy metals through an unconfined sandy aquifer over decades:
          <div class="math-block">
            $$\frac{\partial C}{\partial T} = D_x \frac{\partial^2 C}{\partial X^2} - v_x \frac{\partial C}{\partial X}$$
          </div>
        </li>
        <li><strong>Open-Pit Mine Excavation Progression:</strong> Tracking the monthly and annual removal of overburden benches, bench volume displacement, and progressive tailings dam sedimentation.</li>
        <li><strong>Geomorphological Evolution:</strong> Quantifying coastal cliff retreat rates, deltaic progradation, and landslide creep displacement via multi-temporal satellite interferometry (InSAR).</li>
        <li><strong>Volcanology:</strong> Real-time mapping of lava flow fronts, volcanic ash cloud dispersion trajectories in the atmosphere, and ground inflation/deflation recorded by continuous GNSS networks.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: SPATIO-TEMPORAL DATA STRUCTURES -->
  <div class="card">
    <div class="card-header bg-indigo">3. Spatio-Temporal Data Models: Snapshot vs. Space-Time Composite</div>
    <div class="card-body">
      <h4>Architectures for Encoding Time in GIS Databases</h4>
      <table class="table">
        <thead>
          <tr>
            <th>Spatio-Temporal Model</th>
            <th>Structural Architecture</th>
            <th>How Time is Represented</th>
            <th>Advantages & Limitations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Snapshot Model</strong></td>
            <td>Series of independent discrete map layers for each timestamp ($T_1, T_2, T_3$).</td>
            <td>External layer timestamp; complete state recorded at each time slice.</td>
            <td>Simple to implement; massive data redundancy because unchanging features are repeatedly duplicated.</td>
          </tr>
          <tr>
            <td><strong>Space-Time Composite</strong></td>
            <td>A single decomposed polygonal mesh where overlapping historical boundaries create new polygon fragments.</td>
            <td>Each fragmented polygon carries an attribute history matrix ($T_{\text{start}}, T_{\text{end}}$).</td>
            <td>Zero data redundancy; tracks exact boundary changes; polygon count explodes over long time horizons.</td>
          </tr>
          <tr>
            <td><strong>Event-Based Model (ESTDM)</strong></td>
            <td>Base map at $T_0$ plus a sequential transaction ledger recording only spatial change events.</td>
            <td>Time attached directly to discrete change events ($\Delta E_i$).</td>
            <td>Highly compact storage; requires chronological forward/backward playback to reconstruct state at any arbitrary time.</td>
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
      <div class="question-number">Question 137</div>
      <div class="question-text">
        Which of the following might be considered the fourth dimension in GIS ?
      </div>
      <ul class="option-list">
        <li class="option-item"><strong>(A)</strong> Space</li>
        <li class="option-item"><strong>(B)</strong> Scale</li>
        <li class="option-item correct"><strong>(C)</strong> Time</li>
        <li class="option-item"><strong>(D)</strong> Location</li>
      </ul>
      <div class="answer-banner">
        <strong>Correct Answer: (C) Time</strong> — In GIScience and spatio-temporal modeling, <strong>Time ($T$)</strong> is universally recognized as the fourth dimension, complementing the three spatial dimensions $(X, Y, Z)$ to form 4D spatio-temporal systems $(X, Y, Z, T)$.
      </div>
    </div>
  </div>

  <!-- FORENSIC OPTION ANALYSIS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Options</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="option-title">Option (A): Space — Already Accounts for Dimensions 1, 2, and 3</div>
        <p>
          "Space" refers to physical geometric extent. In GIS, space is fully described by the three primary spatial dimensions: $X$ (Easting / Longitude), $Y$ (Northing / Latitude), and $Z$ (Elevation / Depth). Space cannot be the "fourth" dimension because it already constitutes the first three dimensions.
        </p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (B): Scale — A Dimensionless Ratio, Not a Coordinate Dimension</div>
        <p>
          Scale is a dimensionless mathematical ratio ($d_m / D_g$) or representative fraction expressing the proportion between map distance and ground distance. It is an operational parameter of display and cartographic generalization, not an independent physical coordinate axis.
        </p>
      </div>

      <div class="option correct">
        <div class="option-title">Option (C): Time — Fully Verified & Universal GIScience Standard</div>
        <p>
          In Geographic Information Systems literature (Bangar, p. 222; Worboys & Duckham, Ch. 6; Langran):
        </p>
        <ol>
          <li>The first two dimensions are horizontal planar coordinates $(X, Y)$.</li>
          <li>The third dimension is vertical height or subterranean depth $(Z)$.</li>
          <li>The <strong>fourth dimension is chronological Time ($T$)</strong>, enabling multi-temporal change detection, kinematics, and predictive time-series simulation.</li>
        </ol>
        <p>Therefore, Time is universally designated as the fourth dimension in GIS.</p>
      </div>

      <div class="option wrong">
        <div class="option-title">Option (D): Location — Synonymous with Spatial Coordinates</div>
        <p>
          "Location" is the geographical position of an entity, defined specifically by its spatial coordinates $(X, Y)$ or $(X, Y, Z)$. It is a synonym for spatial position, not an additional fourth dimension.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD: SYNTHESIS COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">The Dimensional Continuum in Geographic Information Systems</div>
    <div class="card-body">
      <table class="table">
        <thead>
          <tr>
            <th>Dimension Model</th>
            <th>Coordinate Axes</th>
            <th>Core Geometric Concept</th>
            <th>Representative Earth Science Use Cases</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>0-Dimensional (0D)</strong></td>
            <td>Single point</td>
            <td>Dimensionless discrete point</td>
            <td>Borehole collar, epicenter point, spot elevation, stream gauging station.</td>
          </tr>
          <tr>
            <td><strong>1-Dimensional (1D)</strong></td>
            <td>Ordered line string</td>
            <td>Length and direction; zero area</td>
            <td>Fault rupture line, river channel, dyke trace, seismic survey profile.</td>
          </tr>
          <tr>
            <td><strong>2-Dimensional (2D)</strong></td>
            <td>$(X, Y)$</td>
            <td>Planar surface area and perimeter</td>
            <td>Geological formation outcrop, watershed boundary, mining concession lease.</td>
          </tr>
          <tr>
            <td><strong>3-Dimensional (3D)</strong></td>
            <td>$(X, Y, Z)$</td>
            <td>True volumetric space / depth</td>
            <td>Underground stopes, folded overturned nappes, 3D ore deposit block models.</td>
          </tr>
          <tr>
            <td><strong>4-Dimensional (4D)</strong></td>
            <td>$(X, Y, Z, T)$</td>
            <td>Spatio-temporal evolution over Time</td>
            <td>Active seismic wave propagation, contaminant plume advection, pit excavation over time.</td>
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
        <strong>Problem 1: 4D Contaminant Plume Advection Distance Over Time</strong><br>
        A toxic chemical leak from a tailings pond enters a sandy unconfined aquifer at time $T_0 = 0$ at coordinates $(X_0 = 1000\text{ m}, Y_0 = 2000\text{ m})$. The regional groundwater seepage velocity is $v_x = 0.40\text{ m/day}$ along the $+X$ axis and $v_y = 0.10\text{ m/day}$ along the $+Y$ axis. Calculate: (a) the 4D spatio-temporal position $(X, Y, T)$ of the plume center after $T = 365\text{ days}$, and (b) the total linear advection distance.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate displacement along $X$ and $Y$ at $T = 365\text{ days}$:
          $$\Delta X = v_x \times T = 0.40\text{ m/day} \times 365\text{ days} = 146.0\text{ meters}$$
          $$\Delta Y = v_y \times T = 0.10\text{ m/day} \times 365\text{ days} = 36.5\text{ meters}$$
          2. Compute coordinates at $T = 365\text{ days}$:
          $$X(365) = X_0 + \Delta X = 1000 + 146.0 = 1146.0\text{ m}$$
          $$Y(365) = Y_0 + \Delta Y = 2000 + 36.5 = 2036.5\text{ m}$$
          $$\text{4D State: } (X = 1146.0\text{ m}, Y = 2036.5\text{ m}, Z = -15.0\text{ m}, T = 365\text{ days})$$
          3. Total linear advection distance:
          $$D = \sqrt{\Delta X^2 + \Delta Y^2} = \sqrt{(146.0)^2 + (36.5)^2} = \sqrt{21,316 + 1332.25} = \sqrt{22,648.25} \approx 150.49\text{ meters}$$
        </div>
      </div>

      <!-- PROBLEM 2 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 2: Geomorphological Shoreline Erosion Rate in Spatio-Temporal GIS</strong><br>
        In a coastal GIS study of the Odisha coastline (Chandipur-Puri sector), a high-water shoreline polyline was digitized from satellite imagery at two distinct epochs:
        $T_1 = \text{January 2000}$, and $T_2 = \text{January 2020}$ ($\Delta T = 20.0\text{ years}$).
        At a monitoring transect, the shoreline retreated inland by $\Delta s = 140.0\text{ meters}$. Calculate: (a) the annual coastal retreat rate ($v_{\text{erosion}}$), and (b) predict the total landward retreat by the year $2050$ assuming linear steady-state erosion.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Annual coastal retreat rate:
          $$v_{\text{erosion}} = \frac{\Delta s}{\Delta T} = \frac{140.0\text{ m}}{20.0\text{ years}} = 7.0\text{ meters/year}$$
          2. Projected retreat from 2020 to 2050 ($\Delta T = 30.0\text{ years}$):
          $$\Delta s_{\text{future}} = v_{\text{erosion}} \times 30.0\text{ years} = 7.0\text{ m/year} \times 30.0\text{ years} = 210.0\text{ meters}$$
        </div>
      </div>

      <!-- PROBLEM 3 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 3: InSAR Subsidence Velocity along Vertical Coordinate ($Z$) Over Time ($T$)</strong><br>
        Persistent Scatterer InSAR (PS-InSAR) measures ground deformation over an abandoned coal mining field. A scatterer point at planar location $(X = 520100, Y = 2640200)$ records cumulative vertical displacements relative to datum:
        At $T_0 = \text{Day } 0: \Delta Z = 0.0\text{ mm}$;
        At $T_1 = \text{Day } 730\text{ (2.0 years)}: \Delta Z = -96.0\text{ mm}$.
        Calculate the average vertical subsidence rate in millimeters per year ($\text{mm/yr}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate time difference in years: $\Delta T = 2.0\text{ years}$.
          2. Vertical velocity $v_z$:
          $$v_z = \frac{\Delta Z}{\Delta T} = \frac{-96.0\text{ mm}}{2.0\text{ years}} = -48.0\text{ mm/year}$$
          The ground surface is subsiding at an active rate of $48.0\text{ mm/year}$.
        </div>
      </div>

      <!-- PROBLEM 4 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 4: Geological Fault Slip Rate from Paleoseismic Trenching</strong><br>
        In a paleoseismic GIS investigation of an active strike-slip fault, radiocarbon dating ($^{14}\text{C}$) of an offset alluvial channel determines that the channel was deposited at $T = 12,000\text{ years BP}$. GIS measurement of the horizontal piercing point offset across the fault trace reveals an offset of $\Delta X = 48.0\text{ meters}$. Calculate the long-term fault slip rate in millimeters per year ($\text{mm/yr}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Long-term slip rate:
          $$v_{\text{slip}} = \frac{\Delta X}{\Delta T} = \frac{48.0\text{ m}}{12,000\text{ years}} = 0.0040\text{ m/year}$$
          2. Convert to millimeters per year:
          $$v_{\text{slip}} = 0.0040 \times 1000\text{ mm/yr} = 4.0\text{ mm/year}$$
          The active strike-slip fault operates at a rate of $4.0\text{ mm/year}$.
        </div>
      </div>

      <!-- PROBLEM 5 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 5: 4D Open-Pit Mine Excavation Volume Rate Calculation</strong><br>
        Sequential drone photogrammetric DEMs are captured over an open-cast iron ore mine at two survey epochs:
        Survey 1: March 31, 2021; Survey 2: September 30, 2021 ($\Delta T = 6\text{ months} = 183\text{ days}$).
        Volumetric DEM surface subtraction ($\text{DEM}_1 - \text{DEM}_2$) calculates a net excavated pit volume of $\Delta V = 1,464,000\text{ m}^3$. Calculate the average daily extraction rate in cubic meters per day ($\text{m}^3\text{/day}$).
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Daily extraction rate:
          $$\text{Rate} = \frac{\Delta V}{\Delta T} = \frac{1,464,000\text{ m}^3}{183\text{ days}} = 8000.0\text{ m}^3/\text{day}$$
        </div>
      </div>

      <!-- PROBLEM 6 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 6: Space-Time Cube Voxel Resolution</strong><br>
        A 4D Spatio-Temporal Voxel Cube is generated to model atmospheric sulfur dioxide ($\text{SO}_2$) gas plumes emanating from a volcanic caldera. The spatial domain is $20\text{ km} \times 20\text{ km} \times 5\text{ km}$ ($X \times Y \times Z$) with spatial voxel size $100\text{ m} \times 100\text{ m} \times 50\text{ m}$. The model runs for a time span of $24\text{ hours}$ with a temporal step of $\Delta T = 15\text{ minutes}$. Calculate the total number of 4D space-time voxels in the simulation.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Spatial voxel count:
          $$N_x = \frac{20,000\text{ m}}{100\text{ m}} = 200, \quad N_y = \frac{20,000\text{ m}}{100\text{ m}} = 200, \quad N_z = \frac{5,000\text{ m}}{50\text{ m}} = 100$$
          $$N_{\text{spatial}} = 200 \times 200 \times 100 = 4,000,000\text{ voxels}$$
          2. Temporal steps ($24\text{ hours} = 1440\text{ minutes}$):
          $$N_t = \frac{1440\text{ min}}{15\text{ min}} = 96\text{ time slices}$$
          3. Total 4D space-time voxels:
          $$N_{\text{4D}} = N_{\text{spatial}} \times N_t = 4,000,000 \times 96 = 384,000,000\text{ voxels (384 Million)}$$
        </div>
      </div>

      <!-- PROBLEM 7 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 7: Space-Time Composite Polygon Fragmentation</strong><br>
        A forest parcel is initially a single unified polygon at $T_0$. At $T_1$, a new highway bisects the polygon into 2 pieces. At $T_2$, a powerline easement crosses the parcel perpendicular to the highway, dividing each piece into 2 again. At $T_3$, a commercial quarry is excised from one quadrant. How many space-time composite child polygons exist at $T_3$?
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. At $T_0$: $1\text{ polygon}$.
          2. At $T_1$: Bisection yields $2\text{ polygons}$.
          3. At $T_2$: Perpendicular cross yields $2 \times 2 = 4\text{ polygons}$.
          4. At $T_3$: Excising an interior quarry polygon divides one quadrant into two (quarry boundary + remaining doughnut/parcel) &rarr; $3 + 2 = 5\text{ composite polygons}$.
          Each child polygon carries the complete chronological history of changes from $T_0$ to $T_3$.
        </div>
      </div>

      <!-- PROBLEM 8 -->
      <div class="p-3 mb-3 border rounded bg-light">
        <strong>Problem 8: Seismic Rupture Wavefront Velocity</strong><br>
        An earthquake epicenter is located at $(X_0, Y_0)$ with origin time $T_0 = 10:14:00.0\text{ UTC}$. A seismological GIS network detects the first P-wave arrival at three automated stations:
        Station 1 ($D_1 = 30.0\text{ km}$): $T_1 = 10:14:05.0\text{ UTC}$ ($\Delta t_1 = 5.0\text{ s}$);
        Station 2 ($D_2 = 72.0\text{ km}$): $T_2 = 10:14:12.0\text{ UTC}$ ($\Delta t_2 = 12.0\text{ s}$);
        Station 3 ($D_3 = 120.0\text{ km}$): $T_3 = 10:14:20.0\text{ UTC}$ ($\Delta t_3 = 20.0\text{ s}$).
        Calculate the apparent crustal P-wave velocity ($V_p$) in $\text{km/s}$.
        <div class="mt-2 text-success">
          <strong>Solution:</strong><br>
          1. Calculate velocity for each station:
          $$V_{p1} = \frac{30.0\text{ km}}{5.0\text{ s}} = 6.0\text{ km/s}$$
          $$V_{p2} = \frac{72.0\text{ km}}{12.0\text{ s}} = 6.0\text{ km/s}$$
          $$V_{p3} = \frac{120.0\text{ km}}{20.0\text{ s}} = 6.0\text{ km/s}$$
          The crustal P-wave velocity is uniform at $V_p = 6.0\text{ km/s}$.
        </div>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=137,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q137_Time_Fourth_Dimension_GIS_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q137: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q137()
