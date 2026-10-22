#!/usr/bin/env python3
"""
Masterclass Builder for Batch 5B: Stratigraphy, Basin Correlation & Unconformities (Q056 - Q060)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q056: Chronostratigraphic Correlation: Establishing Time-Equivalence
# ==============================================================================
def generate_q056():
    title = r"Q056: Principles of Stratigraphic Correlation: Chronostratigraphic vs. Lithostratigraphic Equivalence | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Principles of Stratigraphy & Basin Analysis"
    h1_title = "Q056: Chronostratigraphic Correlation: Establishing Time-Equivalence"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 56<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (4th Ed., Pearson, Ch. 15: Stratigraphic Correlation, pp. 518–534, Fig. 15.2); International Commission on Stratigraphy (ICS), <em>International Stratigraphic Guide</em> (A. Salvador, Ed., 2nd Ed., 1994); North American Commission on Stratigraphic Nomenclature (NACSN), <em>North American Stratigraphic Code</em> (2005); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 13)."""

    part1 = r"""
  <!-- CARD 1: TAXONOMY OF STRATIGRAPHIC CORRELATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Fundamentals of Stratigraphic Correlation</div>
    <div class="card-body">
      <p>In stratigraphy and basin analysis, <strong>correlation</strong> is the demonstrative process of establishing geometric, lithological, paleontological, or temporal correspondence between geographically separated stratigraphic units. The International Stratigraphic Guide rigorously separates correlation into three distinct categories:</p>

      <ul>
        <li><strong>Chronostratigraphic Correlation (Time Correlation):</strong> The specific scientific procedure of demonstrating that separated rock bodies, lithofacies, or physical events were deposited or occurred at the <strong>exact same geological time / identical absolute age</strong>. It establishes true chronocorrelation across diverse depositional realms (e.g., correlating deep pelagic shales with coastal barrier sandstones that formed synchronously).</li>
        <li><strong>Lithostratigraphic Correlation:</strong> The matching of rock strata based strictly on their <strong>lithological similarity, petrographic properties, and geometric position</strong> without regard to their age. Crucially, lithostratigraphic units (formations, members) are frequently <em>diachronous (time-transgressive)</em> due to marine transgressions and regressions (Walther's Law).</li>
        <li><strong>Biostratigraphic Correlation:</strong> The matching of strata based on identical fossil content and biozone boundaries (assemblage zones, taxon-range zones, concurrent-range zones).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q56/boggs_fig15_chronostratigraphic_vs_lithostratigraphic.png" alt="Chronostratigraphic vs Lithostratigraphic Correlation">
        <div class="tb-caption">
          <strong>Figure 56.1 (Sam Boggs Jr., Fig. 15.2):</strong> Fundamental dichotomy in stratigraphy: Lithostratigraphic boundaries (transgressive beach sandstones, dashed red) migrate diachronously across time horizons, whereas Chronostratigraphic isochrons (bentonite ash beds, solid blue) cut across lithologies at true constant time lines.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: TOOLS OF CHRONOSTRATIGRAPHY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Primary Geoscientific Tools for Establishing Chronostratigraphic Age Equivalence</div>
    <div class="card-body">
      <p>Establishing that distant rock bodies share the same age requires identifying <strong>isochronous marker surfaces (time horizons)</strong> that were deposited virtually instantaneously across wide geographic areas:</p>

      <div class="formula-card">
        <div class="formula-title">Mathematical Statement of Chronostratigraphic Equivalence</div>
        $$\text{Unit } A(\mathbf{x}_1) \sim \text{Unit } B(\mathbf{x}_2) \iff t_1 = t_2 \quad \left(\text{Instantaneous Time Horizon: } \frac{dt}{dx} \to 0\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Contrasted with diachronous lithofacies migration: $\frac{dt}{dx} = \frac{1}{v_{\text{transgression}}} \neq 0$.</p>
      </div>

      <ul>
        <li><strong>1. Volcanic Ash Beds (Bentonites / Tonsteins):</strong> Airborne plinian volcanic eruptions disperse pyroclastic ash across entire continents and ocean basins within days. High-precision CA-ID-TIMS U-Pb dating on sanidine/zircon crystals provides absolute chronostratigraphic datum surfaces with sub-permil accuracy ($\pm 20,000\text{ years}$).</li>
        <li><strong>2. Magnetostratigraphic Polarity Reversals:</strong> Earth's geomagnetic field reverses synchronously worldwide. A magnetic chron boundary (e.g., the Matuyama-Brunhes reversal at $0.78\text{ Ma}$) represents an absolute global chronostratigraphic isochron.</li>
        <li><strong>3. Chemostratigraphic Isotopic Excursions:</strong> Rapid, planetary-scale carbon ($\delta^{13}\text{C}$), oxygen ($\delta^{18}\text{O}$), or strontium ($^{87}\text{Sr}/^{86}\text{Sr}$) excursions (e.g., the PETM hyperthermal negative carbon isotope excursion at $56\text{ Ma}$).</li>
        <li><strong>4. Microfossil Datum Planes (FADs and LADs):</strong> First Appearance Datums (FAD) and Last Appearance Datums (LAD) of planktonic organisms (foraminifera, calcareous nannoplankton).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q56/boggs_p524_chronostratigraphic_correlation_principles.png" alt="Boggs Chronostratigraphic Correlation Principles">
        <div class="tb-caption">
          <strong>Figure 56.2 (Sam Boggs Jr., p. 524):</strong> Textbook principles of chronostratigraphic correlation, defining how isochronous surfaces establish time equivalence across distant basins.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON MATRIX OF CORRELATION METHODS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Comparison: Litho- vs. Bio- vs. Chronostratigraphic Correlation</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Correlation Category</th>
            <th>Fundamental Basis</th>
            <th>Units Correlated</th>
            <th>Temporal Validity</th>
            <th>Primary Limitations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chronostratigraphic Correlation</strong></td>
            <td><strong>Age Equivalence (Same Geological Time)</strong></td>
            <td><strong>Erathem, System, Series, Stage, Chronozone.</strong></td>
            <td><strong>Strictly Isochronous (True Time Equivalent).</strong></td>
            <td>Requires radiometric dates, ash beds, or magnetic reversals.</td>
          </tr>
          <tr>
            <td><strong>Lithostratigraphic Correlation</strong></td>
            <td>Lithologic composition, rock type, and stratigraphic position.</td>
            <td>Group, Formation, Member, Bed.</td>
            <td>Frequently <strong>Diachronous</strong> (Time-Transgressive).</td>
            <td>Misleads age interpretation due to lateral facies shifts (Walther's Law).</td>
          </tr>
          <tr>
            <td><strong>Biostratigraphic Correlation</strong></td>
            <td>Similar fossil content and taxon assemblage ranges.</td>
            <td>Biozone (Range Zone, Interval Zone, Assemblage Zone).</td>
            <td>Approximately isochronous within the resolution of the biochron ($0.5-2\text{ Ma}$).</td>
            <td>Fossil preservation bias; provincialism and facies control on living taxa.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 56</div>
        <div class="q-text">_____ is the process of establishing which sedimentary strata are the same age at distant geographical areas by means of their stratigraphic relationship.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Chronostratigraphic correlation</div>
          <div class="opt-node">(B) Lithostratigraphic correlation</div>
          <div class="opt-node">(C) Biostratigraphic correlation</div>
          <div class="opt-node">(D) Stratigraphic correlation</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Chronostratigraphic correlation</strong> [The process of establishing that strata in geographically separated areas were deposited at the exact same geological age is by formal definition chronostratigraphic correlation.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Chronostratigraphic correlation</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In formal stratigraphic nomenclature (Boggs Jr. 2012, Ch. 15; Salvador 1994, International Stratigraphic Guide), correlation that specifically establishes that rock bodies in distant geographic regions share the <strong>exact same age</strong> (temporal equivalence) is designated as <strong>Chronostratigraphic correlation</strong> (or chronocorrelation / time correlation).</li>
        <li>It utilizes isochronous horizons—such as tephra ash falls (bentonites), paleomagnetic reversals, and isotope chemostratigraphy—to tie disparate facies together along lines of equal time.</li>
        <li>Therefore, Option <strong>(A) Chronostratigraphic correlation</strong> is the textbook-verified, precise scientific term.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Lithostratigraphic correlation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Lithostratigraphic correlation</strong> matches strata based solely on physical rock characteristics (lithology, grain size, mineralogy) and geometric position.</li>
        <li>Lithostratigraphic units are famously <em>diachronous</em> (time-transgressive). For example, a basal sandstone in a transgressive sea grows progressively younger in the direction of the shoreline; tracing that sandstone across a basin does <em>not</em> establish strata of the same age. Hence, (B) is false.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Biostratigraphic correlation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Biostratigraphic correlation</strong> establishes similarity in fossil content and biozones.</li>
        <li>While biostratigraphy is a crucial tool used to achieve time correlation, biostratigraphic correlation in itself specifically denotes fossil assemblage matching, which can occasionally be facies-controlled or diachronous (due to migration rates). The overarching process of establishing *same age* is chronostratigraphic correlation.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Stratigraphic correlation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Stratigraphic correlation</strong> is the broad umbrella term encompassing all forms of geological correlation (litho-, bio-, chrono-, chemo-, and seismic).</li>
        <li>Because the question specifically asks for the process of establishing strata of the <em>same age</em>, the specific and exact term required is <strong>Chronostratigraphic correlation</strong>.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Stratigraphic Classification Hierarchies</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Category</th>
            <th>Formal Hierarchy of Units</th>
            <th>Diagnostic Defining Criterion</th>
            <th>Primary Field / Lab Tool</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Chronostratigraphic</strong></td>
            <td>Eonothem $\to$ Erathem $\to$ System $\to$ Series $\to$ <strong>Stage</strong> $\to$ Chronozone</td>
            <td><strong>Time of formation (Isochronous rock body).</strong></td>
            <td>Isotope geochronology, magnetostratigraphy, stable isotopes ($\delta^{13}\text{C}$).</td>
          </tr>
          <tr>
            <td><strong>Geochronologic</strong> (Pure Time)</td>
            <td>Eon $\to$ Era $\to$ Period $\to$ Epoch $\to$ <strong>Age</strong> $\to$ Chron</td>
            <td>Abstract divisions of geological time (years / Ma).</td>
            <td>Astronomical tuning, decay constants ($\lambda$).</td>
          </tr>
          <tr>
            <td><strong>Lithostratigraphic</strong></td>
            <td>Supergroup $\to$ Group $\to$ <strong>Formation</strong> $\to$ Member $\to$ Bed</td>
            <td>Lithological homogeneity and mappability.</td>
            <td>Field mapping, petrography, well-log gamma ray signatures.</td>
          </tr>
          <tr>
            <td><strong>Biostratigraphic</strong></td>
            <td>Biohorizon $\to$ <strong>Biozone</strong> (Range, Interval, Assemblage)</td>
            <td>Specific fossil taxa and evolutionary lineages.</td>
            <td>Micropaleontology, palynology, ammonite / graptolite biozonation.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Correlation Methods & Geochronology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Transgressive Shoreface Velocity Calculation</div>
        <p>A transgressive quartz sandstone unit has a basal age of $505.0\text{ Ma}$ at location A and $501.0\text{ Ma}$ at location B, situated $200\text{ km}$ inland. Calculate the rate of shoreline migration in $\text{mm/year}$ and determine whether this formation is isochronous or diachronous.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\Delta t = 505.0 - 501.0 = 4.0\text{ Ma} = 4.0 \times 10^6\text{ years}$$
        $$\text{Distance } D = 200\text{ km} = 2.0 \times 10^8\text{ mm}$$
        $$v_{\text{migration}} = \frac{D}{\Delta t} = \frac{2.0 \times 10^8\text{ mm}}{4.0 \times 10^6\text{ yr}} = 50\text{ mm/year} = 5.0\text{ cm/year}$$
        <p><strong>Final Answer:</strong> The shoreline migrated at $50\text{ mm/year}$. Because the age of the sandstone differs by $4.0\text{ million years}$ between locations, the formation is <strong>strongly diachronous (time-transgressive)</strong>.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Bentonite Ash Bed Correlation</div>
        <p>Why do altered volcanic ash beds (bentonites / tonsteins) provide the gold standard for chronostratigraphic correlation across differing sedimentary facies?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Volcanic ash plumes from explosive plinian eruptions are carried across the stratosphere and settle out over marine basins, deltas, and lakes within a matter of days or weeks (essentially instantaneous in geological time: $dt \to 0$). The resulting thin clay-rich bentonite layer cuts across all environmental boundaries, providing a literal physical time plane containing radiometrically datable zircons and sanidines.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Walther's Law of Facies Application</div>
        <p>State Walther's Law of Facies and explain how it prevents erroneous chronostratigraphic correlations.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Walther's Law states: <em>"Facies that occur in conformable vertical succession must have been formed in laterally adjacent depositional environments at the same time."</em> This warns stratigraphers that vertical changes in rock type (e.g., sandstone $\to$ shale $\to$ limestone) represent lateral shifts of environmental belts over time, meaning lithostratigraphic contacts cannot be assumed to be horizontal time planes.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Magnetostratigraphic Reversal Resolution</div>
        <p>How does magnetostratigraphic correlation establish time equivalence without requiring body fossils?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>When volcanic rocks cool below their Curie temperature ($T_c$) or magnetic minerals settle in sediments, they align with Earth's magnetic dipole field. Geomagnetic field polarity reversals (Normal vs. Reverse chrons) occur globally at the exact same instant ($<5,000\text{ years}$ transition duration). By matching the unique bar-code pattern of normal and reversed polarity zones to the global geomagnetic polarity timescale (GPTS), strata are chronocorrelated worldwide.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Carbon Isotope Chemostratigraphic Correlation ($\delta^{13}\text{C}$)</div>
        <p>In a Precambrian basin devoid of index fossils, how can a negative carbon isotope excursion establish chronostratigraphic equivalence with another continent?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The oceanic carbon reservoir has a residence time of $\sim 10^5\text{ years}$, which is much longer than the ocean mixing time ($\sim 1,000\text{ years}$). Therefore, catastrophic carbon perturbations (such as the Shuram negative $\delta^{13}\text{C}$ excursion of the Ediacaran) alter the isotopic composition of seawater synchronously worldwide. Carbonate rocks precipitating from seawater preserve this identical isotopic curve, allowing global chronocorrelation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Seismic Reflection Clinoforms as Time Lines</div>
        <p>In seismic stratigraphy, do seismic reflections represent lithological boundaries or chronostratigraphic time horizons?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Seismic reflections are generated at acoustic impedance contrasts ($Z = \rho v$) which coincide with bedding planes, stratal unconformities, and hiatuses. Because stratal surfaces were once continuous depositional surfaces (paleo-seafloors) formed over a single increment of time, <strong>seismic reflections represent chronostratigraphic time-surfaces</strong>, cutting across diachronous lithofacies boundaries.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: GSSP (Golden Spike) Definition</div>
        <p>What is a Global Boundary Stratotype Section and Point (GSSP) in chronostratigraphy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>A GSSP (popularly termed a "Golden Spike") is an internationally agreed-upon, physically designated reference point in a specific geological rock outcrop that defines the lower boundary of a formal chronostratigraphic <strong>Stage</strong> (and hence Series and System). It is anchored to a primary marker event (e.g., FAD of a microfossil or magnetic reversal).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Graphic Correlation Method of Shaw (1964)</div>
        <p>What is Alan Shaw's graphic correlation technique and what does the Slope of the Line of Correlation (LOC) indicate?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In Shaw's graphic correlation, the stratigraphic positions of fossil datums (FADs and LADs) in Section A are plotted along the X-axis against the same datums in Section B on the Y-axis. The data points define a Line of Correlation (LOC). The <strong>slope of the LOC ($dy/dx$)</strong> represents the <strong>ratio of relative sediment accumulation rates</strong> between the two sections.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 56, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q056_Chronostratigraphic_Correlation_Time_Equivalence_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q056: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q057: Stratigraphy of Talcher Coalfield: Raja Rao (GSI 1982) Classification
# ==============================================================================
def generate_q057():
    title = r"Q057: Gondwana Stratigraphy of Talcher Coalfield: Raja Rao (GSI 1982) Early Permian Subdivisions | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Coal Geology of Odisha"
    h1_title = "Q057: Stratigraphy of Talcher Coalfield: Raja Rao (1982) Subdivisions"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 57<br>
<strong>Authoritative References:</strong> C.S. Raja Rao, <em>Coalfields of India: Coal Resources of Tamil Nadu, Andhra Pradesh, Orissa and Maharashtra</em> (Bull. Geol. Surv. India, Series A, No. 45, Vol. II, 1982, pp. 45–68); K.M. Bangar, <em>Principles of Engineering Geology</em> (p. 338, p. 176); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 318–322); N.D. Mitra, <em>Structure and Tectonics of Gondwana Basins of Peninsular India</em> (1993)."""

    part1 = r"""
  <!-- CARD 1: RAJA RAO CLASSIFICATION OF TALCHER COALFIELD -->
  <div class="card">
    <div class="card-header bg-blue">1. The Talcher Coalfield: Stratigraphic Framework of C.S. Raja Rao (GSI 1982)</div>
    <div class="card-body">
      <p>The <strong>Talcher Coalfield</strong>, situated in the Brahmani-Mahanadi valley in the Angul and Sambalpur districts of Odisha, represents the largest single repository of thermal power-grade bituminous coal in India (holding over 50 billion tonnes of geological reserves). In 1982, Geological Survey of India Director <strong>C.S. Raja Rao</strong> synthesized the definitive stratigraphic architecture of the basin:</p>

      <ul>
        <li><strong>Broad Chronostratigraphic Division:</strong> Raja Rao classified the sedimentary sequence of Talcher Coalfield into two overarching chronological divisions:
          <ol>
            <li><strong>Early Permian Succession:</strong> The lower sequence comprising the basal glaciogenic beds and the initial coal-bearing sequence.</li>
            <li><strong>Late Permian to Triassic Succession:</strong> The upper sequence comprising the Middle-to-Late Permian and Triassic units (Barren Measures, Raniganj, and Kamthi/Mahadeva formations).</li>
          </ol>
        </li>
        <li><strong>Subdivisions of the Early Permian:</strong> In Raja Rao's official classification, the Early Permian sequence of Talcher Coalfield is specifically and systematically divided into two constituent basal formations:
          <div class="formula-card">
            <div class="formula-title">Raja Rao (1982) Early Permian Sequence of Talcher</div>
            $$\mathbf{Talchir \text{ Formation}} \quad \longrightarrow \quad \mathbf{Karharbari \text{ Formation}}$$
            <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Followed conformably by the main Barakar Formation (Early Permian Artinskian).</p>
          </div>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q57/mahapatra_p168_talchir_karharbari_succession.png" alt="Talchir and Karharbari Succession">
        <div class="tb-caption">
          <strong>Figure 57.1 (G.B. Mahapatra, p. 168):</strong> Stratigraphic classification of the Lower Gondwana sequence of the Mahanadi-Talcher basin highlighting the basal Talchir glaciogene facies and overlying Karharbari-Barakar coal measures.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: DETAILED FORMATION ATTRIBUTES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Lithological Characteristics of the Talchir and Karharbari Formations in Odisha</div>
    <div class="card-body">
      <p>The two Early Permian formations established in Raja Rao's classification exhibit distinct sedimentological signatures:</p>

      <ul>
        <li><strong>1. Talchir Formation:</strong> Resting with profound nonconformity on Precambrian Eastern Ghats granulites and granites, it consists of:
          <ul>
            <li>The basal <strong>Talchir Boulder Bed</strong>: Unsorted diamictite containing striated and faceted cobbles of quartzite and granite in a green-grey rock flour matrix.</li>
            <li><strong>Needle Shales:</strong> Thinly laminated greenish olive-grey silts and shales displaying pencil-jointing.</li>
            <li><strong>Varved Silts and Turbidite Sandstones:</strong> Lacustrine deposits carrying ice-rafted dropstones. Completely devoid of coal.</li>
          </ul>
        </li>
        <li><strong>2. Karharbari Formation:</strong> Represents the pioneering coal-forming episode in the Talcher basin:
          <ul>
            <li>Composed of poorly sorted, coarse-grained sub-arkosic sandstones, pebbly grits, reworked glacial clasts, and carbonaceous shales.</li>
            <li>Contains the basal <strong>Seam I (Bottom Seam)</strong> of Talcher Coalfield, characterized by dull, inertinite-rich, low-volatile bituminous coal.</li>
            <li>Palynologically and paleobotanically identified by the diagnostic presence of <em>Gondwanidium validum</em>, <em>Buriadia sewardana</em>, and <em>Crucisaccites</em>.</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q57/bangar_p176_talcher_coalfield_stratigraphy.png" alt="Talcher Coalfield Stratigraphy from Bangar">
        <div class="tb-caption">
          <strong>Figure 57.2 (K.M. Bangar, p. 176):</strong> Textbook stratigraphic classification of Indian coalfields documenting the Talchir and Karharbari sequence.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPLETE TALCHER BASIN SUCCESSION -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Stratigraphic Succession of the Talcher Coalfield</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Broad Division (Raja Rao 1982)</th>
            <th>Formation Name</th>
            <th>Approx. Thickness</th>
            <th>Dominant Lithologies & Coal Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td rowspan="2"><strong>Late Permian to Triassic</strong></td>
            <td><strong>Kamthi (Mahadeva) Formation</strong></td>
            <td>$150-250\text{ m}$</td>
            <td>Red ferruginous sandstones, quartz pebble conglomerates. Barren of coal.</td>
          </tr>
          <tr>
            <td><strong>Barren Measures Formation</strong></td>
            <td>$100-200\text{ m}$</td>
            <td>Dark carbonaceous shales, greenish siltstones. Barren of coal.</td>
          </tr>
          <tr>
            <td rowspan="3"><strong>Early Permian</strong> (Target Division)</td>
            <td><strong>Barakar Formation</strong></td>
            <td>$300-500\text{ m}$</td>
            <td>Feldspathic sandstones, grey shales, thick composite coal seams (Seams II to VIII). Prolific coal.</td>
          </tr>
          <tr>
            <td><strong>Karharbari Formation</strong></td>
            <td>$50-100\text{ m}$</td>
            <td><strong>Sub-arkosic grits, dirty sandstones, Seam I. Basal coal-bearing unit.</strong></td>
          </tr>
          <tr>
            <td><strong>Talchir Formation</strong></td>
            <td>$60-150\text{ m}$</td>
            <td><strong>Boulder bed (tillite), olive green needle shales, varvites. Glaciogenic, devoid of coal.</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 57</div>
        <div class="q-text">Raja Rao of GSI in 1982 classified the stratigraphic sequence of Talcher coalfield, Orissa into Early Permian and Late Permian to Triassic. The Early Permian is again classified into which formations ?</div>
        <div class="q-options">
          <div class="opt-node">(A) Lower Kamthi</div>
          <div class="opt-node correct">(B) Talchir and Karharbari</div>
          <div class="opt-node">(C) Damuda Group</div>
          <div class="opt-node">(D) All of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Talchir and Karharbari</strong> [In C.S. Raja Rao's (GSI 1982) authoritative classification of the Talcher Coalfield, the Early Permian succession is specifically subdivided into the Talchir and Karharbari Formations (followed by Barakar).]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Talchir and Karharbari</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In the official Geological Survey of India memoir <em>Coalfields of India</em> (Vol. II, 1982), C.S. Raja Rao systematically classified the stratigraphic sequence of the <strong>Talcher Coalfield, Orissa</strong>.</li>
        <li>The succession was bifurcated into an <em>Early Permian</em> division and a <em>Late Permian to Triassic</em> division.</li>
        <li>The <strong>Early Permian</strong> was explicitly subdivided into two diagnostic basal units: the <strong>Talchir Formation</strong> (representing the glaciogenic tillites and needle shales) and the <strong>Karharbari Formation</strong> (representing the initial gritty sandstone coal measure hosting Seam I).</li>
        <li>Therefore, Option <strong>(B) Talchir and Karharbari</strong> is the exact, authoritative, and scientifically verified answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Lower Kamthi</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Lower Kamthi Formation</strong> belongs to the <strong>Late Permian to Triassic</strong> division of Raja Rao's classification, not the Early Permian.</li>
        <li>It represents upper barren red ferruginous clastics, making it chronostratigraphically incorrect.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Damuda Group</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Damuda Group</strong> is a major hierarchical <em>group</em> rank that includes the Karharbari, Barakar, Barren Measures, and Raniganj formations.</li>
        <li>The question asks for the specific lower <em>formations</em> into which the Early Permian was subdivided, not a group name. Furthermore, the Talchir Formation does not belong to the Damuda Group; it forms its own independent group/formation below the Damuda.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) All of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Lower Kamthi is Late Permian-Triassic and Damuda is a group, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Stratigraphic Evolution of the Talcher Coalfield</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Formation</th>
            <th>Primary Coal Seams</th>
            <th>Coal Quality / Rank</th>
            <th>Maceral Composition</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Barakar Formation</strong> (Main Measures)</td>
            <td>Seam II through Seam VIII (Composite seams up to $40\text{ m}$ thick).</td>
            <td>Non-coking thermal power coal; high moisture ($6-10\%$), high ash ($30-45\%$).</td>
            <td>Rich in vitrinite and inertinite bands.</td>
          </tr>
          <tr>
            <td><strong>Karharbari Formation</strong> (Basal Coal)</td>
            <td><strong>Seam I</strong> (Split into Top, Middle, Bottom sections; $3-8\text{ m}$).</td>
            <td>Semi-coking to medium-coking potential; lower ash ($18-24\%$).</td>
            <td>Dominated by <strong>inertinite macerals (fusinite, semifusinite)</strong>; dull durain coal.</td>
          </tr>
          <tr>
            <td><strong>Talchir Formation</strong> (Basal Glacial)</td>
            <td><strong>Completely Barren</strong> (Zero coal seams).</td>
            <td>N/A (Glacial tillites and lacustrine shales).</td>
            <td>No coal macerals; contains reworked cold-climate monosaccate spores.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Odisha Coal Geology & Basin Mechanics</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Strip Ratio Calculation in Talcher Opencast Mines</div>
        <p>In an opencast coal block of the Talcher Coalfield, a composite Barakar coal seam has thickness $T_{\text{coal}} = 25\text{ m}$. Overlying overburden rock has thickness $T_{\text{ob}} = 75\text{ m}$. Calculate the Stripping Ratio (in $\text{m}^3/\text{tonne}$) assuming coal density $\rho_{\text{coal}} = 1.4\text{ tonnes/m}^3$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>For unit horizontal area ($1\text{ m}^2$):</p>
        $$\text{Volume of Overburden} = 1\text{ m}^2 \times 75\text{ m} = 75\text{ m}^3$$
        $$\text{Mass of Coal} = 1\text{ m}^2 \times 25\text{ m} \times 1.4\text{ tonnes/m}^3 = 35\text{ tonnes}$$
        $$\text{Stripping Ratio} = \frac{75\text{ m}^3}{35\text{ tonnes}} \approx 2.14\text{ m}^3/\text{tonne}$$
        <p><strong>Final Answer:</strong> The stripping ratio is $2.14\text{ m}^3/\text{tonne}$, indicating an exceptionally favorable opencast mining project.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Distinguishing Karharbari Coal from Barakar Coal</div>
        <p>What petrographic and maceral characteristic distinguishes Karharbari coals from Barakar coals in the Talcher basin?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Karharbari coals (Seam I) are dull, hard, compact coals dominated by the <strong>inertinite maceral group</strong> (fusinite, inertodetrinite, semifusinite $>50\%$) formed by oxidative subaerial peat exposure and wildfires. In contrast, Barakar coals (Seams II-VIII) are banded, brighter coals containing higher proportions of the <strong>vitrinite maceral group</strong> ($40-60\%$) formed under permanently waterlogged, reducing anoxic swamp conditions.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Geographic Boundaries of the Talcher Basin</div>
        <p>State the structural tectonic boundaries of the Talcher Coalfield within Odisha.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Talcher Coalfield forms the southeastern terminus of the <strong>Mahanadi-Brahmani Master Graben</strong>. It is bounded on the north by the North Fault scarp against Rengali Province gneisses, on the south and west by Eastern Ghats charnockites and khondalites, and plunges gently towards the west-northwest into the adjacent Ib River Coalfield.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Gross Calorific Value (GCV) Determination</div>
        <p>According to India's Ministry of Coal GCV pricing banding, calculate the GCV of a Talcher coal sample containing Moisture $M = 7.0\%$ and Ash $A = 38.0\%$ using the empirical formula: $\text{GCV (kcal/kg)} = 8550 - 150(M + A)$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$M + A = 7.0 + 38.0 = 45.0\%$$
        $$\text{GCV} = 8550 - 150(45.0) = 8550 - 6750 = 1800\text{ kcal/kg}$$
        <p><strong>Final Answer:</strong> $\text{GCV} = 1800\text{ kcal/kg}$ (corresponding to Grade G16 power utility thermal coal).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Palynological Dating of the Talcher Karharbari</div>
        <p>Which pollen genus is the definitive biostratigraphic marker for the Karharbari Formation in Talcher?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The radial monosaccate genus <strong><em>Crucisaccites monoletus</em></strong> and <strong><em>Parasaccites korbaensis</em></strong>, accompanied by the appearance of striate disaccate pollen (<em>Faunipollenites</em>), marking the Sakmarian stage of the early Cisuralian.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Structural Asymmetry of the Talcher Half-Graben</div>
        <p>How do sedimentary dip angles vary from the southern to the northern boundary of the Talcher Coalfield?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Along the southern boundary, Gondwana strata rest unconformably upon Precambrian basement with gentle northern dips of $5^\circ-10^\circ$. Moving northward toward the master boundary fault, dips increase sharply to $25^\circ-45^\circ$, forming an asymmetric half-graben tilted towards the northern boundary fault.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Groundwater Hazards in Mining Talcher Coal</div>
        <p>What hydrogeological hazard is associated with the multi-aquifer system in the Barakar sandstones of Talcher?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The thick, porous Barakar sandstone layers sandwiching coal seams form prolific confined and semi-confined artesian aquifers. Heavy seasonal monsoons recharge these sandstones, generating high artesian pore pressures capable of bursting pit bottoms or causing sudden flooding of opencast sumps.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Fossil Flora of the Overlying Kamthi Formation</div>
        <p>What characteristic gymnosperm fossil plant assemblage appears in the Kamthi beds overlying the coal measures in Talcher?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Kamthi beds contain late Permian to early Triassic floral elements, notably <em>Schizoneura gondwanensis</em>, <em>Glossopteris conspicua</em>, and <em>Dicroidium</em> fronds, signifying a climatic drying trend with the onset of seasonal arid conditions.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 57, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q057_Talcher_Coalfield_Orissa_Raja_Rao_Stratigraphy_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q057: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q058: Precambrian Stratigraphy of Rajasthan: Aravalli Mountain Belt
# ==============================================================================
def generate_q058():
    title = r"Q058: Precambrian Stratigraphy of Rajasthan: Aravalli Mountain Belt Succession | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Precambrian Geology & Rajasthan Craton"
    h1_title = "Q058: Aravalli Mountain Belt: Precambrian Stratigraphic Succession"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 58<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 310–314, p. 164); P.K. Mukherjee, <em>A Text Book of Geology</em> (pp. 198–202, p. 200); A.M. Heron, <em>The Geology of Central Rajputana</em> (Mem. Geol. Surv. India, Vol. 79, 1953); A.B. Roy, <em>Stratigraphic and Tectonic Framework of the Aravalli Mountain Range</em> (Geol. Soc. India Memoir 7, 1988)."""

    part1 = r"""
  <!-- CARD 1: ARAVALLI STRATIGRAPHIC SUCCESSION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Precambrian Framework of Rajasthan: Basement vs. Supracrustal Belts</div>
    <div class="card-body">
      <p>The <strong>Aravalli Mountain Belt</strong> in Rajasthan and northern Gujarat represents one of the oldest and most spectacular orogenic belts on Earth, extending over $700\text{ km}$ from Delhi south-southwest to Champaner. Its geological history records multiple Precambrian cycles of continental rifting, shelf sedimentation, island arc accretion, and continent-continent collision:</p>

      <ul>
        <li><strong>1. Archean Basement (Oldest):</strong>
          <ul>
            <li><strong>Banded Gneissic Complex (BGC) / Mewar Gneiss (Archean, $>2.5\text{ Ga}$ to $3.3\text{ Ga}$):</strong> Composed of tonalite-trondhjemite-granodiorite (TTG) gneisses, amphibolites, pelitic schists, and intrusive multi-phase granitoids (e.g., Berach Granite $\sim 2.5\text{ Ga}$). This ancient basement forms unit <strong>1(d)</strong>.</li>
          </ul>
        </li>
        <li><strong>2. Aravalli Supergroup (Paleoproterozoic, $\sim 2.5\text{ Ga}$ to $1.8\text{ Ga}$):</strong> Separated from the underlying BGC by a profound angular unconformity marked by basal polymictic conglomerates. The supergroup developed through continental rifting into a passive margin shelf-slope basin, classically subdivided in <strong>ascending chronological order from older to younger</strong> into:
          <ol>
            <li><strong>(a) Delwara Group (Basal):</strong> Represents the initial syn-rift stage; amygdaloidal tholeiitic metabasalts (Delwara volcanics), quartzites, and conglomerates.</li>
            <li><strong>(b) Debari Group (Middle):</strong> Platform carbonate and arenite shelf deposits; arkosic quartzites, dolomites, and carbonaceous phyllites. Hosts the world-renowned <strong>Jhamarkotra stromatolitic phosphorite deposit</strong>.</li>
            <li><strong>(c) Jharol Group (Upper):</strong> Deep-marine turbidites, phyllites, mica schists, and thin-bedded quartzites with serpentinized ultramafic bodies (ophiolitic suture fragments).</li>
          </ol>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q58/mahapatra_p164_aravalli_delhi_succession.png" alt="Mahapatra Aravalli Delhi Succession">
        <div class="tb-caption">
          <strong>Figure 58.1 (G.B. Mahapatra, p. 164):</strong> Stratigraphic succession of Rajasthan Precambrians showing Archean BGC basement overlain unconformably by the Aravalli Supergroup (Delwara $\to$ Debari $\to$ Jharol).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: OLDER TO YOUNGER MATCHING LOGIC -->
  <div class="card">
    <div class="card-header bg-indigo">2. Forensic Stratigraphic Sequencing: Resolving 1(d), 2(a, b, c)</div>
    <div class="card-body">
      <p>Question 58 tests the precise chronological matching of groups and formations from oldest to youngest:</p>

      <div class="formula-card">
        <div class="formula-title">The Ascending Chronological Formula</div>
        $$\mathbf{1(d): \text{ Archean Basement (BGC)}} \quad \longrightarrow \quad \mathbf{2(a, b, c): \text{ Aravalli [Delwara } \to \text{Debari } \to \text{Jharol]}}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Oldest to Youngest: Archean TTG Basement $\to$ Syn-Rift Volcanics $\to$ Platform Phosphatic Carbonates $\to$ Deep-Water Pelagic Turbidites.</p>
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q58/pkm_p200_aravalli_supergroup_sequence.png" alt="PKM Aravalli Supergroup Sequence">
        <div class="tb-caption">
          <strong>Figure 58.2 (P.K. Mukherjee, p. 200):</strong> Textural and lithostratigraphic details of the Aravalli Supergroup sequence resting upon the Banded Gneissic Complex.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON MATRIX OF RAJASTHAN PRECAMBRIANS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Stratigraphic Hierarchy of the Northwestern Indian Shield</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Supergroup / Complex</th>
            <th>Constituent Groups</th>
            <th>Geochronological Age</th>
            <th>Tectonic Setting & Key Mineral Deposits</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Delhi Supergroup</strong></td>
            <td>Ajabgarh Group (Upper)<br>Alwar Group (Middle)<br>Raialo Group (Basal)</td>
            <td>Mesoproterozoic ($\sim 1800-1000\text{ Ma}$)</td>
            <td>Intracontinental to pericontinental rift basin. Copper (Khetri), Lead-Zinc.</td>
          </tr>
          <tr>
            <td><strong>Aravalli Supergroup</strong></td>
            <td><strong>(c) Jharol Group</strong> (Upper)<br><strong>(b) Debari Group</strong> (Middle)<br><strong>(a) Delwara Group</strong> (Basal)</td>
            <td><strong>Paleoproterozoic ($\sim 2500-1800\text{ Ma}$)</strong></td>
            <td><strong>Rift-to-passive margin basin. Jhamarkotra phosphorite, Lead-Zinc (Zawar).</strong></td>
          </tr>
          <tr>
            <td><strong>Archean Basement</strong></td>
            <td><strong>(d) Banded Gneissic Complex (BGC)</strong> & Berach Granite</td>
            <td><strong>Archean ($>2500-3300\text{ Ma}$)</strong></td>
            <td><strong>Crystalline TTG basement and ancient greenstone enclaves.</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 58</div>
        <div class="q-text">General geological formation of the Aravalli Mountains : [Group/Supergroup] Formation. Match the correct sequence from older to younger formations. The sequence is :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) 1(d), 2(a, b, c)</div>
          <div class="opt-node">(B) 1(d), 2(c, b, a)</div>
          <div class="opt-node">(C) 1(a), 2(b, c, d)</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) 1(d), 2(a, b, c)</strong> [Matching Archean Basement (1) with BGC (d), and Paleoproterozoic Aravalli Supergroup (2) in ascending chronological order: Delwara (a) $\to$ Debari (b) $\to$ Jharol (c).]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) 1(d), 2(a, b, c)</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In standard regional stratigraphy of Rajasthan (Heron 1953; Roy 1988; Mahapatra p. 164 & 312; Mukherjee p. 200), the Precambrian formations are ordered from older to younger:
          <ol>
            <li><strong>Unit 1 (Archean Basement):</strong> Matched with <strong>(d) Banded Gneissic Complex (BGC)</strong>, representing the $\sim 3.3-2.5\text{ Ga}$ granite-gneiss floor.</li>
            <li><strong>Unit 2 (Aravalli Supergroup):</strong> Subdivided in strict ascending chronological order (older to younger) into:
              <br>• <strong>(a) Delwara Group:</strong> Basal rift volcanics and quartzites.
              <br>• <strong>(b) Debari Group:</strong> Middle platform carbonates, quartzites, and Jhamarkotra phosphorites.
              <br>• <strong>(c) Jharol Group:</strong> Upper deep-water turbidites and schists.
            </li>
          </ol>
        </li>
        <li>Therefore, the correct chronological sequence is represented by the formula <strong>1(d), 2(a, b, c)</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) 1(d), 2(c, b, a)</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>This option lists the Aravalli Supergroup subdivisions in <em>reverse chronological order</em> (from youngest Jharol down to oldest Delwara).</li>
        <li>Because the examination prompt explicitly demands the sequence from <strong>older to younger</strong> formations, this inverted sequence is incorrect.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) 1(a), 2(b, c, d)</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>This incorrectly pairs Unit 1 (Basement) with (a) Delwara Group, which is an overlying supracrustal unit, and misplaces (d) BGC as the youngest unit of the Aravalli.</li>
        <li>This violates fundamental superposition and basement-cover relationships.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (A) is the exact, canonical sequence matching the established literature, Option (D) is false.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Mineral Wealth of the Aravalli-Delhi Orogen</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Group / Formation</th>
            <th>Primary Lithologies</th>
            <th>Major Mineral Deposits</th>
            <th>Economic Significance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Debari Group</strong> (Aravalli)</td>
            <td>Dolomitic limestone, carbonaceous phyllites, quartzites.</td>
            <td><strong>Jhamarkotra Phosphorite</strong>, <strong>Zawar Lead-Zinc-Silver</strong>.</td>
            <td>India's premier rock phosphate mine; historic ancient zinc-silver smelting.</td>
          </tr>
          <tr>
            <td><strong>Delwara Group</strong> (Aravalli)</td>
            <td>Metabasalts, chlorite schists, quartzites.</td>
            <td>Copper and minor gold occurrences.</td>
            <td>Syn-rift volcanic metal concentration.</td>
          </tr>
          <tr>
            <td><strong>Alwar / Ajabgarh</strong> (Delhi)</td>
            <td>Quartzites, calc-gneisses, amphibolites.</td>
            <td><strong>Khetri Copper Belt</strong>, Makrana Marble, Emeralds.</td>
            <td>Premier copper mining center of Hindustan Copper Limited (HCL).</td>
          </tr>
          <tr>
            <td><strong>BGC / Mewar Gneiss</strong></td>
            <td>TTG gneisses, intrusive granites, pegmatites.</td>
            <td>Mica, Beryl, Feldspar, building granite.</td>
            <td>Rajasthan pegmatite belt mineral production.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Precambrian Geodynamics & Ore Geology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Phosphorite Biomineralization at Jhamarkotra</div>
        <p>What biogenic sedimentary structure is responsible for the concentration of high-grade phosphorite ($\sim 30-35\% \text{ P}_2\text{O}_5$) in the Debari Group at Jhamarkotra?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Jhamarkotra deposit is hosted within <strong>columnar stromatolites</strong> (specifically <em>Collenia columnaris, Baicalia</em>). Ancient cyanobacterial mats trapped and precipitated fine colloidal carbonate-fluorapatite (francolite) from nutrient-rich coastal upwelling waters, alternating with pure dolomite laminae to form thick, economic stratabound phosphorite reefs.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Geochronology of the Berach Granite</div>
        <p>The Berach Granite intrudes the BGC but is unconformably overlain by the basal Aravalli conglomerate. If its U-Pb zircon age is $2550 \pm 10\text{ Ma}$, what does this establish about the Aravalli Supergroup?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>By the Principle of Inclusions and Unconformities, the Aravalli Supergroup must be <strong>strictly younger than $2550\text{ Ma}$</strong>. This places the initiation of Aravalli rifting in the earliest Paleoproterozoic, establishing the Berach Granite as part of the Archean basement stabilization.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Zawar Lead-Zinc Metallogenesis</div>
        <p>What is the ore mineralogy and genetic model of the world-class lead-zinc deposits at Zawar?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Hosted in dolomites of the Mochia, Balaria, and Baroi formations (Aravalli Supergroup), the ore mineralogy consists of <strong>sphalerite ($\text{ZnS}$)</strong> and <strong>galena ($\text{PbS}$)</strong> with associated native silver and pyrite. It represents a <strong>Sedimentary Exhalative (SEDEX)</strong> to Mississippi Valley-Type (MVT) stratabound hydrothermal deposit.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Phulad Ophiolite Suite Significance</div>
        <p>What tectonic feature is represented by the Phulad Ophiolite along the western margin of the Delhi fold belt?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Phulad Ophiolite Suite (comprising pillowed metabasalts, sheeted dikes, gabbros, and serpentinized peridotites) represents obducted remnants of Mesoproterozoic oceanic crust, marking the <strong>paleo-suture zone</strong> of continental collision between the Marwar Craton and the Bundelkhand/BGC Craton.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Great Boundary Fault (GBF) Displacement</div>
        <p>What is the nature of displacement along the Great Boundary Fault of Rajasthan, and which blocks are juxtaposed?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The GBF is a major longitudinal <strong>reverse / thrust fault</strong> dipping northwestward, along which the deformed Precambrian rocks of the Aravalli-Bhilwara belt are thrust southeastward over the undeformed Upper Vindhyan strata (Bhander and Kaimur groups).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Metamorphic Inversion across the Aravalli Belt</div>
        <p>Describe the regional metamorphic grade variation across the Aravalli Mountain Range from east to west.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Metamorphic grade increases systematically from <strong>east to west</strong>: from low-grade sub-greenschist/greenschist facies (slates and phyllites) in the eastern Hindoli and Delwara belts to amphibolite and granulite facies (garnet-sillimanite schists, calc-granulites, and charnockites) in the western Delhi and BGC sectors.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Debari Basal Conglomerate Clast Composition</div>
        <p>What clast lithologies dominate the polymictic Debari Conglomerate at the base of the Aravalli Supergroup?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Debari Conglomerate contains rounded to subangular clasts of <strong>quartzite, granite, vein quartz, and BGC tourmaline-bearing gneisses</strong>, proving that the underlying crystalline Archean crust was uplifted and subaerially eroded prior to Aravalli basin subsidence.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Tectonic Origin of the Aravalli-Delhi Belt</div>
        <p>Explain the Wilson Cycle model for the evolution of the Aravalli and Delhi orogenic belts.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The region underwent two successive Wilson Cycles: (1) <strong>Aravalli Cycle ($\sim 2.5-1.8\text{ Ga}$):</strong> Continental rifting of Archean BGC, ocean basin opening, passive margin deposition, and subsequent compressional closure and collision; followed by (2) <strong>Delhi Cycle ($\sim 1.8-1.0\text{ Ga}$):</strong> Intracratonic rifting, development of the South Delhi oceanic tract, subduction-related arc magmatism, and terminal collision during the assembly of the Rodinia supercontinent.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 58, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q058_Aravalli_Mountains_Precambrian_Succession_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q058: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q059: Lameta Formation: The Infratrappean Beds of Central India
# ==============================================================================
def generate_q059():
    title = r"Q059: Mesozoic-Cenozoic Transition: Lameta Formation (Infratrappean Beds) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Vertebrate Paleontology"
    h1_title = "Q059: Lameta Formation: The Infratrappean Beds of Central India"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 59<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 334–336, p. 175); P.K. Mukherjee, <em>A Text Book of Geology</em> (pp. 218–222); M.S. Krishnan, <em>Geology of India and Burma</em> (Ch. 16: The Deccan Traps); C.A. Matley, <em>Stratigraphy, Fossils and Geological Relationships of the Lameta Beds of Jubbulpore</em> (Rec. GSI, Vol. 53, 1921); Ashok Sahni, <em>Cretaceous Vertebrates of India</em> (Geol. Soc. India, 2001)."""

    part1 = r"""
  <!-- CARD 1: LAMETA FORMATION GEOLOGICAL DEFINITION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Lameta Formation: The Continental Infratrappean Benchmark</div>
    <div class="card-body">
      <p>The <strong>Lameta Formation</strong> (named after the type locality at Lameta Ghat on the Narmada River near Jabalpur, Madhya Pradesh, by J.G. Medlicott in 1860) is an internationally celebrated Late Cretaceous (Maastrichtian, $\sim 70-66\text{ Ma}$) sedimentary formation found extensively across Madhya Pradesh, Gujarat, and Maharashtra:</p>

      <ul>
        <li><strong>The Concept of Infratrappean Beds:</strong> In Indian stratigraphy, the Lameta Formation is classically and universally designated as the <strong>Infratrappean Beds</strong> (from Latin <em>infra</em>, meaning "below" or "beneath").
          <div class="formula-card">
            <div class="formula-title">The Fundamental Trappean Stratigraphic Relationship</div>
            $$\mathbf{Infratrappean \text{ Beds (Lameta)}} \quad \xrightarrow{\text{Subjacent To}} \quad \mathbf{Deccan \text{ Basalt Traps}} \quad \xrightarrow{\text{Intercalated With}} \quad \mathbf{Intertrappean \text{ Beds}}$$
          </div>
        </li>
        <li><strong>Structural & Stratigraphic Position:</strong> The Lameta Beds rest unconformably upon Precambrian crystalline basement (Jabalpur granite/schists) or Gondwana sandstones, and lie <strong>directly beneath the lowermost basaltic lava flows of the Deccan Traps</strong>.</li>
        <li><strong>Contrast with Intertrappeans:</strong>
          <ul>
            <li><strong>Infratrappeans (Lameta):</strong> Sedimentary strata deposited <em>prior</em> to the onset of Deccan volcanism, immediately underlying the first lava flow.</li>
            <li><strong>Intertrappeans:</strong> Thin, localized, highly fossiliferous lacustrine/fluvial sedimentary lenses deposited <em>during quiescent volcanic intervals between two successive basalt flows</em> (e.g., at Rajahmundry, Nagpur, Worli).</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q59/mahapatra_p175_lameta_infratrappean_deccan_traps.png" alt="Lameta Infratrappean from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 59.1 (G.B. Mahapatra, p. 175):</strong> Stratigraphic position of the Lameta Formation as the classic Infratrappean horizon underlying the Deccan volcanic trap pile.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: PALEONTOLOGY AND DINOSAURS OF LAMETA -->
  <div class="card">
    <div class="card-header bg-indigo">2. World-Class Vertebrate Paleontology: Dinosaurs of the Lameta Beds</div>
    <div class="card-body">
      <p>The Lameta Formation is globally renowned as one of the most prolific Cretaceous vertebrate fossil localities in the world, documenting terrestrial life directly preceding the catastrophic K-Pg mass extinction:</p>

      <ul>
        <li><strong>Sauropod & Theropod Dinosaurs:</strong> Yielded holotypes of titanosaurs (<em>Titanosaurus indicus, Isisaurus colberti, Jainosaurus septentrionalis</em>) and abelisaurid predatory theropods (<em>Rajasaurus narmadensis, Indosuchus, Carnotaurus</em> relatives).</li>
        <li><strong>Dinosaur Nesting Grounds & Megaloolithid Eggs:</strong> Extensive nesting sites at Balasinor (Rahioli, Gujarat) and Jabalpur containing clutches of spherical sauropod eggs (<em>Megaloolithus</em>) and embryonic bone remains.</li>
        <li><strong>Depositional Environment:</strong> Represents semi-arid to sub-humid fluvio-lacustrine, palustrine, and caliche-rich paleosol environments bordering the shallow epicontinental marine seaway of the Narmada rift.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q59/mahapatra_p176_infratrappean_vs_intertrappean.png" alt="Infratrappean vs Intertrappean from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 59.2 (G.B. Mahapatra, p. 176):</strong> Textbook cross-section illustrating the clear physical distinction between Infratrappean Lameta beds (under the basal flow) and Intertrappean sedimentary interbeds (between basalt flows).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF INFRATRAPPEAN VS INTERTRAPPEAN -->
  <div class="card">
    <div class="card-header bg-emerald">3. Comparative Matrix: Infratrappean vs. Intertrappean Beds</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Property</th>
            <th>Infratrappean Beds (Lameta Formation)</th>
            <th>Intertrappean Beds</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Position Relative to Basalt</strong></td>
            <td><strong>Directly beneath the lowermost basalt flow.</strong></td>
            <td><strong>Intercalated between successive basalt flows.</strong></td>
          </tr>
          <tr>
            <td><strong>Stratigraphic Thickness</strong></td>
            <td>$20\text{ m}$ to $50\text{ m}$ (Continuous regional formation).</td>
            <td>$1\text{ m}$ to $5\text{ m}$ (Discontinuous local lenses).</td>
          </tr>
          <tr>
            <td><strong>Geological Age</strong></td>
            <td>Late Cretaceous (Maastrichtian, $\sim 70-66\text{ Ma}$).</td>
            <td>Latest Maastrichtian to Early Paleocene (Danian, $\sim 66-64\text{ Ma}$).</td>
          </tr>
          <tr>
            <td><strong>Dominant Lithologies</strong></td>
            <td>Greenish cherty limestones, mottled clays, calcretes.</td>
            <td>Silicified cherts, bituminous shales, pyroclastic ash.</td>
          </tr>
          <tr>
            <td><strong>Characteristic Biota</strong></td>
            <td><strong>Titanosaurid dinosaurs, abelisaurs, dinosaur eggs.</strong></td>
            <td>Freshwater gastropods (<em>Physa prinsepii</em>), pelobatid frogs, charophytes.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 59</div>
        <div class="q-text">The Lameta Formation is also known as the ________, is a sedimentary geological formation found in Madhya Pradesh, Gujarat, and Maharashtra, India, associated with the Deccan Traps.</div>
        <div class="q-options">
          <div class="opt-node">(A) Bagh Beds</div>
          <div class="opt-node">(B) Intertrappean Beds</div>
          <div class="opt-node correct">(C) Infratrappean Beds</div>
          <div class="opt-node">(D) All of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) Infratrappean Beds</strong> [The Lameta Formation directly underlies the Deccan Traps and is universally designated as the Infratrappean Beds in Indian stratigraphy.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) Infratrappean Beds</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>In Indian geology and stratigraphy (Krishnan 1982; Wadia 1975; Mahapatra 2019, p. 175; Mukherjee 2013, p. 220), the <strong>Lameta Formation</strong> is universally synonymized with and formally termed the <strong>Infratrappean Beds</strong>.</li>
        <li>The term *infratrappean* explicitly designates sedimentary strata that were deposited on the pre-volcanic land surface immediately prior to the massive outpourings of the Deccan volcanic eruptions, therefore lying directly *below* (infra) the basal trap flows.</li>
        <li>These beds are famous for their cherty limestones, mottled clays, and world-class dinosaur nesting sites and skeletons (e.g., <em>Rajasaurus, Titanosaurus</em>).</li>
        <li>Hence, Option <strong>(C) Infratrappean Beds</strong> is the precise, unambiguous correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Intertrappean Beds</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Intertrappean Beds</strong> are thin ($1-5\text{ m}$), localized sedimentary lenses that formed in freshwater lakes and rivers during dormant periods *between* two successive Deccan basalt lava flows.</li>
        <li>They contain abundant freshwater gastropods such as <em>Physa prinsepii</em> and <em>Lymnaea</em>. Because the Lameta Formation lies *beneath* the entire volcanic pile rather than between flows, calling it "Intertrappean" is an egregious stratigraphic error.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Bagh Beds</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The <strong>Bagh Beds</strong> represent a marine Cretaceous transgressive succession (Nodular Limestone, Deola-Chirakhan Marl, Coralline Limestone) deposited along the Narmada rift valley.</li>
        <li>While partly coeval with the Lameta Formation, the Bagh Beds represent marine facies, whereas the Lameta Formation represents continental fluvio-lacustrine infratrappean facies. They are two distinct stratigraphic formations.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) All of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because only Option (C) Infratrappean Beds correctly describes the Lameta Formation, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Cretaceous-Tertiary Formations Associated with Deccan Volcanism</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Stratigraphic Entity</th>
            <th>Structural Relation to Deccan Traps</th>
            <th>Depositional Facies</th>
            <th>Diagnostic Fossil Assemblage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lameta Formation</strong></td>
            <td><strong>Infratrappean</strong> (Directly below basal basalt flow)</td>
            <td>Fluvio-lacustrine, palustrine, calcretes.</td>
            <td><strong>Titanosaurids, <em>Rajasaurus</em>, <em>Megaloolithus</em> dinosaur eggs.</strong></td>
          </tr>
          <tr>
            <td><strong>Bagh Beds</strong></td>
            <td>Infratrappean (Marine equivalent along western Narmada)</td>
            <td>Shallow marine carbonate shelf.</td>
            <td>Echinoids (<em>Hemiaster</em>), ammonites (<em>Placenticeras</em>), oysters.</td>
          </tr>
          <tr>
            <td><strong>Intertrappean Beds</strong></td>
            <td><strong>Intercalated</strong> (Between successive lava flows)</td>
            <td>Freshwater lacustrine, ponds, stream channels.</td>
            <td><em>Physa prinsepii</em>, <em>Paludina</em>, fossil frogs (<em>Indobatrachus</em>).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Mesozoic Paleontology & Deccan Volcanism</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Paleosol Calcretes and Pedogenesis in Lameta Beds</div>
        <p>The Mottled Nodular Beds of the Lameta Formation exhibit extensive pedogenic calcrete (caliche) nodules. What paleoclimatic conditions do calcretes signify?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Pedogenic calcretes precipitate in the B-horizon of soils where annual evapotranspiration significantly exceeds annual precipitation. In the modern world, mature calcretes form in <strong>semi-arid climates</strong> with seasonal rainfall between $100\text{ mm}$ and $500\text{ mm/year}$, proving that central India experienced a pronounced seasonal, semi-arid monsoon climate during the terminal Cretaceous.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Titanosaur Sauropod Bone Histology</div>
        <p>What unique histological structure in <em>Isisaurus</em> long bones demonstrates rapid juvenile growth rates in Indian titanosaurs?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Cross-sections of titanosaur limb bones from the Lameta beds reveal <strong>fibrolamellar bone tissue</strong> with dense, reticulate and plexiform vascular canals, punctuated by annual Lines of Arrested Growth (LAGs). Fibrolamellar tissue is characteristic of warm-blooded mammals and birds, proving that sauropods maintained high metabolic rates and explosive growth.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Discovery of Rajasaurus narmadensis</div>
        <p>Where was the famous predatory horned abelisaurid dinosaur <em>Rajasaurus narmadensis</em> discovered, and what is its anatomical hallmark?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Rajasaurus</em> was discovered in the Lameta limestone quarry at Rahioli, Kheda district, Gujarat, by GSI paleontologists Suresh Srivastava and Ashok Sahni. Its anatomical hallmark is a prominent, rounded <strong>median frontal horn</strong> on its skull roof, short robust jaws, and vestigial forelimbs characteristic of Gondwanan Abelisauridae.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: K-Pg Boundary Ash in Intertrappean Beds</div>
        <p>High-precision $^{40}\text{Ar}/^{39}\text{Ar}$ dating of Deccan basalt flows bounding the Jhilmili intertrappean bed in MP yields an age of $66.05 \pm 0.05\text{ Ma}$. What is the significance of this date?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>This date is identical within analytical error to the globally defined <strong>Cretaceous-Paleogene (K-Pg) boundary</strong> ($66.043\text{ Ma}$). The presence of both Danian planktonic foraminifera and iridium spikes within the Jhilmili intertrappeans proves that Deccan flood basalt volcanism erupted across the K-Pg boundary, acting as a major contributor to the global mass extinction.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Thermal Metamorphism of Infratrappean Rocks</div>
        <p>What metamorphic contact feature is commonly observed on the top surface of the Lameta limestone where it contacts the overlying basalt?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The intense thermal heat ($1150-1200^\circ\text{C}$) of the overriding basaltic lava flow thermally bakes the upper $0.5-2\text{ m}$ of the underlying Lameta limestone and shale, creating a hardened, red-burned <strong>baked zone (hornfels / jasperoid porcelainization)</strong>, providing unequivocal proof that the limestone was deposited *prior* to the lava flow.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Megaloolithus Eggshell Microstructure</div>
        <p>What structural type characterizes the dinosaur eggshells found in the Lameta nesting grounds?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>They belong to the oofamily <strong>Megaloolithidae</strong>, characterized by spherulitic radiating calcitic prisms (dinosauroid-spherulitic type) with high-density tubocanaliculate pore systems, designed for gas exchange in moist, buried colonial sand nests.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Physa prinsepii as an Intertrappean Index Fossil</div>
        <p>Why is the sinistral gastropod <em>Physa prinsepii</em> universally found in Intertrappean beds but absent from Infratrappean Lameta beds?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Physa prinsepii</em> is a specialized freshwater pulmonary snail that colonized warm, silica-rich volcanic crater lakes and shallow ponds that formed on the basalt flow surfaces between eruptions. It evolved during the peak volcanic phases and is thus diagnostic of the Intertrappeans.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Volume of Deccan Flood Basalts</div>
        <p>If the Deccan volcanic province originally covered $1.5 \times 10^6\text{ km}^2$ with an average cumulative lava thickness of $1.0\text{ km}$, calculate the total erupted basalt volume in cubic kilometers ($\text{km}^3$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$V = \text{Area} \times \text{Thickness} = (1.5 \times 10^6\text{ km}^2) \times 1.0\text{ km} = 1.5 \times 10^6\text{ km}^3$$
        <p><strong>Final Answer:</strong> Total erupted volume was approximately $1.5\text{ million cubic kilometers}$, representing one of the largest Large Igneous Provinces (LIPs) in Phanerozoic Earth history.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 59, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q059_Lameta_Formation_Infratrappean_Deccan_Traps_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q059: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q060: The Eparchean Unconformity at Tirupati Hills (Cuddapah Basin)
# ==============================================================================
def generate_q060():
    title = r"Q060: Regional Unconformities: The Eparchean Unconformity at Tirupati Hills | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Indian Stratigraphy & Structural Unconformities"
    h1_title = "Q060: The Eparchean Unconformity at Tirupati Hills"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 60<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 302–306, p. 160); P.K. Mukherjee, <em>A Text Book of Geology</em> (p. 200); Ramakrishnan & Vaidyanadhan, <em>Geology of India</em> (Vol. 1, Ch. 11: Cuddapah Basin, pp. 275–314); Geological Survey of India, <em>National Geological Monuments of India</em> (Special Publication No. 61); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 13)."""

    part1 = r"""
  <!-- CARD 1: THE EPARCHEAN UNCONFORMITY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Eparchean Unconformity: The Great Chronological Divide of Peninsular India</div>
    <div class="card-body">
      <p>In Indian stratigraphy and global Precambrian geology, the <strong>Eparchean Unconformity</strong> represents the profound, continent-wide planar erosional unconformity that separates the intensely deformed, metamorphosed, and crystalline <strong>Archean basement</strong> from the overlying undeformed to gently folded <strong>Proterozoic (Purana) sedimentary cover</strong>:</p>

      <ul>
        <li><strong>National Geological Monument at Tirumala (Tirupati Hills):</strong> The most spectacular, classic, and globally renowned outcrop of the Eparchean Unconformity is exposed along the Ghat road near Tirupati in the Chittoor district of Andhra Pradesh (declared a <strong>National Geological Monument</strong> by the Geological Survey of India in 2001).</li>
        <li><strong>Stratigraphic Juxtaposition:</strong>
          <ul>
            <li><strong>Underlying Footwall:</strong> Coarse-grained, pink Archean granitic gneiss and hornblende-biotite gneisses (Peninsular Gneissic Complex, dated at $\sim 2.5\text{ Ga}$ to $2.6\text{ Ga}$) cut by basic dolerite dikes.</li>
            <li><strong>Overlying Hanging Wall:</strong> Gently dipping ($10^\circ-12^\circ$ northeast) basal quartzites and polymictic basal conglomerates of the <strong>Nagari Quartzite Formation</strong> (Nallamalai / Papaghni Groups of the Proterozoic <strong>Cuddapah Supergroup</strong>, initiated at $\sim 1.9-1.8\text{ Ga}$).</li>
          </ul>
        </li>
        <li><strong>The Time Hiatus ($\sim 500-700\text{ Ma}$):</strong> The Eparchean Unconformity records an immense period of non-deposition, cratonic uplift, deep crustal peneplanation, and weathering spanning over <strong>500 to 700 million years</strong> between the Archean stabilization and the initiation of Purana intracratonic sedimentation.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q60/mahapatra_p160_eparchean_unconformity.png" alt="Eparchean Unconformity from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 60.1 (G.B. Mahapatra, p. 160):</strong> The Eparchean Unconformity: Horizontal Proterozoic Cuddapah quartzites resting nonconformably on vertical Archean granite gneisses.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: P.K. MUKHERJEE EXCERPT AND TERMINOLOGY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Scientific Etymology: Eparchean vs. The Great Unconformity</div>
    <div class="card-body">
      <p>Question 60 tests the precise Indian geological terminology for this monument:</p>

      <div class="formula-card">
        <div class="formula-title">The Eparchean Chronological Formulation</div>
        $$\mathbf{\text{Archean Peninsular Gneiss } (\sim 2.5\text{ Ga})} \xrightarrow[\text{Hiatus } \approx 700\text{ Ma}]{\mathbf{Eparchean \text{ Unconformity}}} \mathbf{\text{Cuddapah Supergroup } (\sim 1.8\text{ Ga})}$$
      </div>

      <ul>
        <li><strong>Etymology of "Eparchean":</strong> Coined from Greek <em>epi</em> (meaning "upon" or "after") + <em>Archean</em>, denoting the fundamental transition surface capping the Archean Era across the Indian Peninsular Shield.</li>
        <li><strong>Why "The Great Unconformity" is Geographically Distinct:</strong> In international geology, "The Great Unconformity" classically refers to John Wesley Powell's (1869) discovery in the <strong>Grand Canyon (USA)</strong>, separating the Paleoproterozoic Vishnu Schist from the Cambrian Tapeats Sandstone. In Indian geological literature, the specific Tirupati boundary is universally termed the <strong>Eparchean Unconformity</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q60/pkm_p200_cuddapah_archaean_unconformity.png" alt="PKM Cuddapah Archaean Unconformity">
        <div class="tb-caption">
          <strong>Figure 60.2 (P.K. Mukherjee, p. 200):</strong> Geological cross-section documenting the Eparchean contact between the Cuddapah Supergroup and the Archean crystalline floor.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF UNCONFORMITY TYPES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Classification of Geological Unconformities</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Type of Unconformity</th>
            <th>Structural & Lithological Criterion</th>
            <th>Classic Global & Indian Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Nonconformity</strong> (Eparchean Type)</td>
            <td>Sedimentary strata resting upon eroded plutonic igneous or high-grade metamorphic rocks.</td>
            <td><strong>Eparchean Unconformity at Tirupati Hills (Cuddapah quartzites over Archean granite).</strong></td>
          </tr>
          <tr>
            <td><strong>Angular Unconformity</strong></td>
            <td>Younger horizontal strata resting on tilted or folded older sedimentary strata.</td>
            <td>Siccar Point (Hutton), Grand Canyon (Chuar over Bass), Aravalli-Delhi boundary.</td>
          </tr>
          <tr>
            <td><strong>Disconformity</strong></td>
            <td>Parallel sedimentary beds separated by an irregular, carved erosional surface.</td>
            <td>Talchir tillite on striated Vindhyan pavement; Uttatur-Trichinopoly contact.</td>
          </tr>
          <tr>
            <td><strong>Paraconformity</strong></td>
            <td>Parallel sedimentary beds without obvious physical erosion, but harboring a major paleontological time gap.</td>
            <td>Paleozoic-Mesozoic paraconformities in flat-lying platform carbonates.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 60</div>
        <div class="q-text">The boundary in between sedimentary rocks of the Cudappah Supergroup and Archaean rocks found near Tirupati Hills, creating a period of nondepositions and erosion of about 500 Ma has been defined as__.</div>
        <div class="q-options">
          <div class="opt-node">(A) The Great Unconformity</div>
          <div class="opt-node correct">(B) Eparchean Unconfornity</div>
          <div class="opt-node">(C) Paraconformity</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Eparchean Unconfornity</strong> [The profound unconformity between the Cuddapah Supergroup and underlying Archean granitic gneisses at Tirupati Hills is classically termed the Eparchean Unconformity.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Eparchean Unconfornity</div>
    <div class="card-body">
      <p><strong>Detailed Stratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>The boundary separating the Proterozoic sedimentary rocks of the <strong>Cuddapah Supergroup</strong> (Nagari Quartzite) from the underlying crystalline <strong>Archean basement</strong> (granites and gneisses) at Tirupati Hills (Tirumala Ghat) represents an enormous time hiatus of over 500 to 700 million years.</li>
        <li>In Indian geology (Mahapatra p. 160 & 304; Mukherjee p. 200; Ramakrishnan & Vaidyanadhan Vol. 1, p. 275; GSI National Monuments), this classic contact is universally and formally designated as the <strong>Eparchean Unconformity</strong>.</li>
        <li>It signifies the end of the Archean Era and the prolonged post-Archean peneplanation before the onset of Purana basin sedimentation.</li>
        <li>Therefore, Option <strong>(B) Eparchean Unconfornity</strong> (spelled verbatim as in the official exam paper) is the verified, definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) The Great Unconformity</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While the Eparchean unconformity is physically a "great" unconformity, the formal term <strong>The Great Unconformity</strong> is historically reserved in global literature for the boundary between the Precambrian basement and Cambrian Tapeats Sandstone in the Grand Canyon of Arizona (USA).</li>
        <li>In Indian stratigraphic nomenclature and national monument registers, this feature is strictly named the <strong>Eparchean Unconformity</strong>.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Paraconformity</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>A <strong>paraconformity</strong> is a type of unconformity in which the strata above and below the gap are completely parallel, and the contact resembles a simple bedding plane without any physical erosional relief (recognized only through missing fossil zones).</li>
        <li>At Tirupati Hills, the contact is a prominent <strong>nonconformity</strong> between crystalline igneous granite below and bedded sedimentary quartzite above, with basal conglomerates and clear erosional relief. It is not a paraconformity.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (B) is the universally established name of the monument, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Major Unconformities of Peninsular India</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Unconformity Name</th>
            <th>Underlying Formation (Footwall)</th>
            <th>Overlying Formation (Hanging Wall)</th>
            <th>Approximate Hiatus Duration</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Eparchean Unconformity</strong> (Tirupati)</td>
            <td><strong>Archean Peninsular Gneiss ($\sim 2.5\text{ Ga}$)</strong></td>
            <td><strong>Cuddapah Nagari Quartzite ($\sim 1.8\text{ Ga}$)</strong></td>
            <td><strong>$\sim 700\text{ million years}$</strong></td>
          </tr>
          <tr>
            <td><strong>Eparchean Unconformity</strong> (Vindhyan)</td>
            <td>Archean Bundelkhand Granite ($\sim 2.5\text{ Ga}$)</td>
            <td>Semri Basal Conglomerate ($\sim 1.7\text{ Ga}$)</td>
            <td>$\sim 800\text{ million years}$</td>
          </tr>
          <tr>
            <td><strong>Gondwana Basal Unconformity</strong></td>
            <td>Precambrian Basement / Vindhyan strata</td>
            <td>Talchir Boulder Bed (Tillite, $\sim 300\text{ Ma}$)</td>
            <td>$\sim 200-1500\text{ million years}$</td>
          </tr>
          <tr>
            <td><strong>Deccan Trap Basal Unconformity</strong></td>
            <td>Archean / Gondwana / Lameta Beds</td>
            <td>Deccan Basalt Flow 1 ($\sim 66\text{ Ma}$)</td>
            <td>Variable ($0-2400\text{ million years}$)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Structural Unconformities & Indian Tectonics</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Paleoweathering Crust (Saprolite) at Tirupati</div>
        <p>What petrological feature is observed directly beneath the Eparchean Unconformity on the upper surface of the Archean granite at Tirupati?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Directly beneath the basal Nagari conglomerate, the Archean granite displays a fossil weathering zone or <strong>paleosol / saprolite profile</strong> ($1-3\text{ m}$ thick). Feldspars are chemically degraded into kaolinite clay, and biotite is oxidized into chlorite and hematite, demonstrating prolonged subaerial chemical weathering under an ancient Precambrian atmosphere prior to Cuddapah marine transgression.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Geochronological Calculation of Hiatus Duration</div>
        <p>If the basement granite at Tirupati has a radiometric date of $2520 \pm 15\text{ Ma}$ and the overlying basal Cuddapah tuff has a U-Pb date of $1850 \pm 5\text{ Ma}$, calculate the exact time duration of the Eparchean hiatus.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\text{Hiatus Duration } \Delta t = 2520\text{ Ma} - 1850\text{ Ma} = 670\text{ Ma}$$
        <p><strong>Final Answer:</strong> The hiatus represents a time gap of $670\text{ million years}$ ($\approx 0.67\text{ billion years}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Mangampeta Barite Deposit in the Cuddapah Basin</div>
        <p>What unique volcanogenic bedded barite deposit occurs within the Cuddapah Supergroup above the Eparchean basement?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Mangampeta Barite Deposit</strong> in the Kadapa district of Andhra Pradesh is the largest bedded barite ($\text{BaSO}_4$) deposit in the world. It occurs within the Pullampet Formation of the Cheyair/Nallamalai Group, formed by exhalative submarine barium-rich volcanic tuffs and rosettes settling in an anoxic marine basin.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Cuddapah Crescent Basin Geometry</div>
        <p>What structural tectonic feature bounds the eastern convex margin of the Cuddapah Basin against the Eastern Ghats Mobile Belt?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The eastern margin is truncated by an intense, arcuate, west-verging <strong>thrust front (Eastern Nallamalai Fold-Thrust Belt)</strong> where the high-grade metamorphic rocks of the Eastern Ghats Mobile Belt were thrust westward over the Purana sediments during the Grenvillian-age collision ($\sim 1.0\text{ Ga}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Dolerite Dike Truncation Principle</div>
        <p>Numerous Proterozoic dolerite dikes cut through the Archean granite at Tirupati but terminate abruptly at the Eparchean contact without penetrating the overlying Nagari Quartzite. What does this demonstrate?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>By the <strong>Principle of Cross-Cutting Relationships</strong>, the dolerite dike intrusion occurred *after* the crystallization of the granite, but *before* the deposition of the Nagari Quartzite. The dikes were planed off flat during the Eparchean erosional interval, proving they predate the Cuddapah Supergroup.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: National Geological Monument Designation</div>
        <p>Which governmental agency in India designates and preserves National Geological Monuments such as the Tirupati Eparchean Unconformity?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Geological Survey of India (GSI)</strong>, under the Ministry of Mines, Government of India, is the statutory authority that identifies, declares, and maintains National Geological Monuments for geo-heritage, educational, and scientific conservation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Distinction Between Nonconformity and Disconformity</div>
        <p>How does a nonconformity physically differ from a disconformity in engineering site investigations?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Nonconformity:</strong> Massive, unstratified crystalline plutonic/metamorphic basement below with bedded sedimentary rock above. High shear strength contrast; potential seepage along weathered paleosol.</li>
          <li><strong>Disconformity:</strong> Stratified sedimentary rock both above and below the contact, with parallel bedding planes. Weakness is confined to the paleo-karst or erosional channel infill.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Peneplanation Velocity Calculation</div>
        <p>If $15\text{ km}$ of Archean orogenic crust was stripped away by erosion to expose the deep granites at Tirupati during the $670\text{ Ma}$ Eparchean hiatus, calculate the average denudation rate in $\text{meters per million years}$ ($\text{m/Ma}$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\text{Denudation Rate } E = \frac{15,000\text{ m}}{670\text{ Ma}} \approx 22.39\text{ m/Ma}$$
        <p><strong>Final Answer:</strong> The average cratonic denudation rate was approximately $22.4\text{ m/Ma}$ ($0.022\text{ mm/year}$), characteristic of slow cratonic peneplanation.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 60, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q060_Eparchean_Unconformity_Tirupati_Cuddapah_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q060: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q056()
    generate_q057()
    generate_q058()
    generate_q059()
    generate_q060()
