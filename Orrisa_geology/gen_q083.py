#!/usr/bin/env python3
"""
Q083 Generator: Main Central Thrust (MCT) in Himalayan Tectonic Architecture
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q083():
    title = r"Q083: Structural Geology & Himalayan Tectonics: Main Central Thrust (MCT) Architecture | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Structural Geology & Himalayan Tectonics"
    h1_title = "Q083: Main Central Thrust (MCT): Tectonic Boundary of the Higher Himalaya"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 83<br>
<strong>Authoritative References:</strong> Ben A. van der Pluijm & Stephen Marshak, <em>Earth Structure: An Introduction to Structural Geology and Tectonics</em> (2nd Ed., W.W. Norton, Ch. 21, Fig. 21.21); K.S. Valdiya, <em>Geology of the Kumaun Lesser Himalaya</em> (Wadia Institute of Himalayan Geology); Arnold Heim & Augusto Gansser (1939, <em>Central Himalaya: Geological Observations of the Swiss Expedition</em>); O.N. Bhargava, <em>The Himalayan Geology</em>."""

    part1 = r"""
  <!-- CARD 1: HIMALAYAN MORPHOTECTONIC BELTS AND ARCHITECTURE -->
  <div class="card">
    <div class="card-header bg-blue">1. The Himalayan Morphotectonic Framework & Longitudinal Fault Architecture</div>
    <div class="card-body">
      <p>
        The <strong>Himalayan Orogen</strong>, produced by the continent-continent collision between the Indian and Eurasian plates (~55 Ma to present), represents the premier active convergent mountain belt on Earth. The orogenic wedge is structured into five distinct, laterally continuous morphotectonic lithotectonic zones separated by crustal-scale, north-dipping boundary fault systems (Heim & Gansser, 1939; Valdiya, 1980; Van der Pluijm & Marshak, 2004):
      </p>

      <div class="figure-box">
        <img src="../../figures_Q83/vdp_fig21_21_himalayan_mct.png" alt="Himalayan Tectonic Architecture and Main Central Thrust from Van der Pluijm and Marshak">
        <div class="figure-caption">
          <strong>Figure 83.1 — Tectonic Architecture of the Himalayan Orogen:</strong> Authentic diagram from Van der Pluijm & Marshak (<em>Earth Structure</em>, Ch. 21, Fig. 21.21). Illustrating the northward-dipping crustal thrust architecture: the Main Central Thrust (MCT) carrying the High-grade Great Himalayan Crystallines (HHC) over the Lesser Himalayan Sequence (LHS), underlain southward by the MBT and MFT.
        </div>
      </div>

      <h4>North-to-South Structural Transect of the Himalaya</h4>
      <ol>
        <li><strong>Indus-Yarlung Tsangpo Suture Zone (ITSN / ISZ):</strong> The collision boundary demarcated by ophiolites and trench mélanges representing the closed Neotethys Ocean.</li>
        <li><strong>Tethyan Sedimentary Series (TSS / THS):</strong> A thick sequence ($>10\text{ km}$) of fossiliferous Cambrian-to-Eocene shallow-marine shelf sediments deposited on the northern passive margin of India.</li>
        <li><strong>South Tibetan Detachment System (STDS):</strong> A major low-angle, top-to-the-north <em>extensional normal fault / ductile shear zone</em> that places unmetamorphosed Tethyan sediments over the underlying crystalline core.</li>
        <li><strong>Higher Himalayan Crystallines (HHC / Great Himalayan Sequence, GHS):</strong> The metamorphic backbone of the mountain chain! Composed of high-grade Proterozoic paragneisses, orthogneisses, kyanite-sillimanite schists, migmatites, and Miocene leucogranites formed at amphibolite-to-granulite facies ($T = 650\text{--}800^\circ\text{C}, P = 8\text{--}12\text{ kbar}$).</li>
        <li><strong>Main Central Thrust (MCT):</strong> <em>The definitive ductile shear zone!</em> A massive, crustal-scale intracontinental thrust fault that accommodated tens to hundreds of kilometers of southward displacement, placing the high-grade HHC over the low-grade Lesser Himalaya.</li>
        <li><strong>Lesser Himalayan Sequence (LHS):</strong> Low-grade to unmetamorphosed Paleoproterozoic to Mesoproterozoic quartzites, slates, phyllites, and stromatolitic carbonates (e.g., Damtha, Deoban, Jaunsar, Krol, and Tal groups).</li>
        <li><strong>Main Boundary Thrust (MBT):</strong> A brittle-to-ductile thrust fault that places the Proterozoic Lesser Himalayan sequence over the Cenozoic Siwalik Molasse.</li>
        <li><strong>Sub-Himalayan Zone (Siwalik Group):</strong> Middle Miocene to Early Pleistocene syn-orogenic foreland molasse sandstones, mudstones, and conglomerates.</li>
        <li><strong>Main Frontal Thrust (MFT / Himalayan Frontal Thrust, HFT):</strong> The active, southernmost blind/emergent thrust fault placing Siwalik strata over the Quaternary alluvium of the Indo-Gangetic Plains.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 2: MCT SHEAR ZONE & INVERTED METAMORPHISM -->
  <div class="card">
    <div class="card-header bg-indigo">2. The MCT Ductile Shear Zone & The "Inverted Metamorphism" Paradox</div>
    <div class="card-body">
      <p>
        The <strong>Main Central Thrust (MCT)</strong> is not a simple razor-thin fault surface; rather, it is a complex, ductile shear zone several kilometers thick characterized by intense penetrative plastic deformation:
      </p>
      <ul>
        <li><strong>Microstructural Mylonitization:</strong> Rocks within the shear zone display spectacular mylonites, ribbon quartz, dynamically recrystallized feldspar porphyroclasts, S-C fabrics, mica fish, and asymmetric pressure shadows indicating pervasive <strong>top-to-the-south/southwest thrust kinematics</strong>.</li>
        <li><strong>The Inverted Metamorphic Gradient:</strong> In ordinary metamorphic terrains, metamorphic grade increases downward with depth. In the Lesser Himalaya directly underlying the MCT, however, <strong>metamorphic grade increases systematically upwards toward the thrust sheet</strong>:
          $$\text{Chlorite Zone (Low)} \longrightarrow \text{Biotite} \longrightarrow \text{Garnet} \longrightarrow \text{Staurolite} \longrightarrow \text{Kyanite} \longrightarrow \mathbf{\text{Sillimanite (Directly beneath MCT!)}}$$
        </li>
      </ul>

      <h4>Thermal-Mechanical Origin of Inverted Metamorphism</h4>
      <p>
        Petrologists and geodynamicists explain this phenomenon through three synergistic processes:
      </p>
      <ol>
        <li><strong>Thermal Inversion by Thrusting (Le Fort, 1975):</strong> Emplacement of the colossal, scorching-hot HHC metamorphic slab ($T > 750^\circ\text{C}$) over the relatively cold footwall Lesser Himalaya conducted heat downward, baking the uppermost footwall into higher-grade zones.</li>
        <li><strong>Shear Heating:</strong> High plastic strain rates and friction within the ductile shear zone generated immense shear strain heating along the fault core.</li>
        <li><strong>Channel Flow Extrusion (Grujic et al., 2002; Beaumont et al., 2001):</strong> During the Early to Middle Miocene (~23–16 Ma), a ductile, partially molten mid-crustal channel of HHC was extruded southward between two coeval bounding shear zones: the basal thrust (MCT) and the roof normal fault (STDS).</li>
      </ol>
    </div>
  </div>

  <!-- CARD 3: VALDIYA'S DUAL MCT NOMENCLATURE & MODERN SEISMOTECTONICS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Regional Nomenclature (MCT-I vs. MCT-II) & The Basal MHT Décollement</div>
    <div class="card-body">
      <h4>Valdiya's Two-Tier Division in the Kumaun-Garhwal Himalaya</h4>
      <p>
        In the Indian Himalaya, Professor K.S. Valdiya (1980) delineated two distinct thrust planes:
      </p>
      <ul>
        <li><strong>MCT-I (Munsiari Thrust):</strong> The lower tectonic boundary, separating the low-grade metasediments of the Lesser Himalaya from the chlorite-biotite-garnet mylonitic gneisses of the Munsiari Formation.</li>
        <li><strong>MCT-II (Vaikrita Thrust):</strong> The true primary MCT (in the strict Swiss sense of Heim & Gansser), which brings the coarse-grained, high-grade kyanite-sillimanite psammitic gneisses and migmatites of the <strong>Vaikrita Group (HHC)</strong> over the Munsiari Formation.</li>
      </ul>

      <h4>The Main Himalayan Thrust (MHT) Basal Décollement</h4>
      <p>
        Geophysical deep seismic reflection profiles (e.g., Project INDEPTH) and earthquake hypocenters prove that at depth, the surface faults—MFT, MBT, and MCT—merge downward into a single, master low-angle basal detachment fault: the <strong>Main Himalayan Thrust (MHT)</strong>. The MHT absorbs the majority of the $\sim 18\text{--}20\text{ mm/year}$ of active convergence between the Indian shield and the Tibetan Plateau, serving as the rupture plane for catastrophic great earthquakes (e.g., 1905 Kangra, 1934 Bihar-Nepal, 2015 Gorkha).
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 83</div>
        <div class="q-text">The ductile shear zone along with the High-grade Great Himalayan Crystalline complex was placed above the Low-grade to unmeta-morphosed Lesser Himalayan Sequence is termed as the :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Main Central Thrust (MCT)</div>
          <div class="opt-node">(B) Main Frontal Thrust (MFT)</div>
          <div class="opt-node">(C) Main Boundary Thrust (MBT)</div>
          <div class="opt-node">(D) Himalayan Frontal Thrust (HFT)</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Main Central Thrust (MCT):</strong> The premier crustal-scale ductile shear zone of the Himalaya that thrusts the high-grade Greater Himalayan Crystalline (HHC) complex southward over the low-grade to unmetamorphosed Lesser Himalayan Sequence (LHS).</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Main Central Thrust (MCT) — CORRECT</div>
        <p>
          The <strong>Main Central Thrust (MCT)</strong> is the universally established, textbook tectonic boundary that places the high-grade, kyanite-sillimanite-bearing Great Himalayan Crystalline (HHC) complex over the low-grade Proterozoic Lesser Himalayan Sequence (LHS). It represents an intracontinental ductile shear zone several kilometers thick, characterized by pervasive mylonitization and the famous inverted metamorphic gradient (Heim & Gansser, 1939; Valdiya, 1980; Van der Pluijm & Marshak, p. 488).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Main Frontal Thrust (MFT) — INCORRECT</div>
        <p>
          The <em>Main Frontal Thrust (MFT)</em> is the southernmost, active tectonic boundary of the Himalaya. It places the deformed Cenozoic Siwalik molasse over the modern, flat Quaternary alluvium of the Indo-Gangetic Plains. It is a brittle, shallow thrust fault that has no contact with the High-grade Great Himalayan Crystallines.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Main Boundary Thrust (MBT) — INCORRECT</div>
        <p>
          The <em>Main Boundary Thrust (MBT)</em> separates the <strong>Lesser Himalayan Sequence in its hanging wall from the Sub-Himalayan Siwalik Group in its footwall</strong>. It is a predominantly brittle to semi-brittle fault formed during the Late Miocene–Pliocene, located far to the south of the Great Himalayan Crystalline complex.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Himalayan Frontal Thrust (HFT) — INCORRECT</div>
        <p>
          <em>Himalayan Frontal Thrust (HFT)</em> is simply an alternative, synonymous geological name for the Main Frontal Thrust (MFT). It marks the outermost structural boundary between the Sub-Himalaya and the Indo-Gangetic Foreland Basin.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Master Tectonic Architecture of the Himalayan Convergent Orogen</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Tectonic Boundary</th>
            <th>Hanging Wall Lithology</th>
            <th>Footwall Lithology</th>
            <th>Kinematic Nature & Deformation Style</th>
            <th>Age of Major Activity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Indus-Yarlung Tsangpo Suture (ITSN)</strong></td>
            <td>Trans-Himalayan (Ladakh/Gangdese Batholith)</td>
            <td>Tethyan Himalayan Sediments (THS)</td>
            <td>Subduction suture, ophiolite obduction, strike-slip</td>
            <td>Late Cretaceous – Eocene (~55 Ma)</td>
          </tr>
          <tr>
            <td><strong>South Tibetan Detachment (STDS)</strong></td>
            <td>Tethyan Sedimentary Series (THS, unmetamorphosed)</td>
            <td><strong>Higher Himalayan Crystallines (HHC)</strong></td>
            <td><strong>Low-angle normal fault detachment (Top-to-North)</strong></td>
            <td>Early to Middle Miocene (~22–16 Ma)</td>
          </tr>
          <tr>
            <td><strong>Main Central Thrust (MCT)</strong></td>
            <td><strong>Higher Himalayan Crystallines (HHC, High-grade)</strong></td>
            <td><strong>Lesser Himalayan Sequence (LHS, Low-grade)</strong></td>
            <td><strong>Ductile shear zone (Top-to-South thrust); Mylonites</strong></td>
            <td><strong>Early to Middle Miocene (~23–16 Ma)</strong></td>
          </tr>
          <tr>
            <td><strong>Main Boundary Thrust (MBT)</strong></td>
            <td>Lesser Himalayan Sequence (Proterozoic metasediments)</td>
            <td>Sub-Himalayan Siwalik Group (Cenozoic Molasse)</td>
            <td>Brittle to semi-ductile reverse thrust fault</td>
            <td>Late Miocene – Pliocene (~10–5 Ma)</td>
          </tr>
          <tr>
            <td><strong>Main Frontal Thrust (MFT / HFT)</strong></td>
            <td>Sub-Himalayan Siwalik Group (Molasse)</td>
            <td>Indo-Gangetic Alluvium (Quaternary sediments)</td>
            <td>Brittle emergent thrust fault, active seismogenic fault</td>
            <td>Pleistocene to Recent (Active today!)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- WORKED PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Analytical & Quantitative Practice Problems</div>
    <div class="card-body">

      <!-- Problem 1 -->
      <div class="p-card">
        <div class="p-header">Problem 1: Critical Coulomb Wedge Taper Calculation for the Himalaya</div>
        <p>
          According to Davis, Suppe & Dahlen's (1983) Critical Coulomb Wedge Theory, a convergent orogenic wedge maintains dynamic stability when its critical taper angle ($\alpha + \beta$) satisfies:
          $$\alpha + \beta = \frac{1 - \lambda_b}{1 - \lambda} \mu_b$$
          In the Central Nepal Himalaya, the basal décollement (MHT) dips northward at $\beta = 6^\circ$, and the average topographic slope is $\alpha = 2.5^\circ$. If the pore fluid pressure ratio throughout the wedge is hydrostatic ($\lambda = 0.40$), and the basal pore fluid pressure ratio is $\lambda_b = 0.75$, calculate the effective basal friction coefficient ($\mu_b$).
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Wedge Calculation:</strong><br>
          1. Calculate total wedge taper angle in radians:
          $$\alpha + \beta = 2.5^\circ + 6.0^\circ = 8.5^\circ$$<br>
          Converting to radians:
          $$\theta = 8.5 \times \frac{\pi}{180} \approx 0.14835\text{ radians}$$<br>
          2. Substitute pore fluid factors:
          $$\frac{1 - \lambda_b}{1 - \lambda} = \frac{1 - 0.75}{1 - 0.40} = \frac{0.25}{0.60} \approx 0.4167$$<br>
          3. Solve for $\mu_b$:
          $$\alpha + \beta = 0.4167 \times \mu_b \implies \mu_b = \frac{0.14835}{0.4167} \approx \mathbf{0.356}$$<br>
          <strong>Interpretation:</strong> The effective basal friction coefficient along the Main Himalayan Thrust is $\mu_b \approx 0.36$, indicating that high fluid pressures ($\lambda_b = 0.75$) substantially weaken the fault zone, permitting crustal overthrusting of the Higher Himalaya.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Thrust Displacement Rate and Crustal Shortening Calculation</div>
        <p>
          Structural reconstructions of the Main Central Thrust across the Kumaun-Garhwal Himalaya indicate a total cumulative southward heave (horizontal displacement) of $L = 140\text{ km}$. Geochronologic dating of syn-kinematic monazites indicates primary ductile thrust shearing operated from $22\text{ Ma}$ to $15\text{ Ma}$. Calculate the average ductile slip rate along the MCT in millimeters per year ($\text{mm/yr}$).
        </p>
        <div class="p-ans">
          <strong>Slip Rate Derivation:</strong><br>
          1. <strong>Time Duration ($\Delta t$):</strong>
          $$\Delta t = 22\text{ Ma} - 15\text{ Ma} = 7.0\text{ million years} = 7.0 \times 10^6\text{ years}$$<br>
          2. <strong>Displacement ($L$):</strong>
          $$L = 140\text{ km} = 140 \times 10^3\text{ m} = 1.4 \times 10^8\text{ mm}$$<br>
          3. <strong>Average Slip Rate ($v$):</strong>
          $$v = \frac{L}{\Delta t} = \frac{1.4 \times 10^8\text{ mm}}{7.0 \times 10^6\text{ years}} = \mathbf{20.0\text{ mm/year}}$$<br>
          <strong>Significance:</strong> During the Early-to-Middle Miocene, the MCT absorbed virtually the entire $\sim 20\text{ mm/yr}$ rate of Indo-Asian convergence prior to the forward propagation of deformation to the MBT and MFT.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Microstructural Shear Sense in MCT Mylonites</div>
        <p>
          A oriented quartzofeldspathic mylonite collected from the MCT zone at Joshimath, Uttarakhand, displays S-surfaces inclined at $40^\circ$ to the North, C-surfaces dipping at $25^\circ$ to the North, and asymmetric $\sigma$-type feldspar porphyroclasts with tails extending parallel to C. Deduce the tectonic sense of shear and the transport direction of the Higher Himalayan slab.
        </p>
        <div class="p-ans">
          <strong>Kinematic Deduction:</strong><br>
          1. <strong>S-C Fabric Relationship:</strong> S-surfaces (schistosity/flattening planes) dip more steeply ($40^\circ\text{ N}$) than C-surfaces (cisaillement/shear bands, $25^\circ\text{ N}$). The acute angle between S and C ($40^\circ - 25^\circ = 15^\circ$) points in the direction of shear displacement on the hanging wall.<br>
          2. <strong>Asymmetric Porphyroclasts:</strong> The staircase geometry of recrystallized tail mantles on $\sigma$-porphyroclasts confirms a synthetic, dextral-equivalent rotational sense when looking west.<br>
          <strong>Conclusion:</strong> The microstructural fabric definitively proves <strong>Top-to-the-South/Southwest thrusting</strong>, representing the southward translation of the Higher Himalayan slab over India.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Channel Flow Hypothesis & Coeval Fault Operation</div>
        <p>
          State the fundamental premise of the "Channel Flow" model for the Higher Himalayan Crystallines (Beaumont et al., 2001) and explain how two faults with opposite senses of shear (MCT and STDS) operated simultaneously in the Miocene.
        </p>
        <div class="p-ans">
          <strong>Channel Flow Synthesis:</strong><br>
          1. <strong>Mid-Crustal Low-Viscosity Channel:</strong> High radiogenic heat production and dehydration melting in the thickened Tibetan/Himalayan crust generated widespread leucogranitic partial melts, drastically lowering the effective viscosity of the middle crust ($10^{18}\text{--}10^{19}\text{ Pa}\cdot\text{s}$) to form a ductile channel.<br>
          2. <strong>Extrusion Between Opposing Faults:</strong> Gravitational potential energy gradients drove the ductile channel southward toward the low-pressure foreland. The extruded slab was bounded by:
             - <strong>MCT at the Base:</strong> Top-to-the-South <em>thrust shear zone</em>.<br>
             - <strong>STDS at the Top:</strong> Top-to-the-North <em>normal detachment fault</em>.<br>
          3. Coeval movement on both faults (~22–16 Ma) allowed the Higher Himalayan crystalline slab to extrude like toothpaste onto the Indian plate.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Inverted Metamorphism: 1D Thermal Diffusion Modeling</div>
        <p>
          Assume a hot metamorphic slab (HHC) at initial temperature $T_1 = 750^\circ\text{C}$ is instantaneously thrust over a cold footwall (LHS) at initial temperature $T_0 = 150^\circ\text{C}$ along the MCT. Using the 1D conduction equation across an infinite step contact, calculate the immediate contact temperature ($T_{\text{contact}}$) and explain why the footwall exhibits an inverted thermal gradient.
        </p>
        <div class="p-ans">
          <strong>Thermal Analytical Solution:</strong><br>
          Assuming equivalent thermal conductivity and diffusivity in both units:
          $$T_{\text{contact}} = \frac{T_1 + T_0}{2} = \frac{750^\circ\text{C} + 150^\circ\text{C}}{2} = \frac{900}{2} = \mathbf{450^\circ\text{C}}$$<br>
          - <strong>Temperature Profile:</strong> Directly beneath the contact, heat diffuses downward into the footwall according to the error function:
          $$T(z, t) = T_{\text{contact}} - (T_{\text{contact}} - T_0) \text{erf}\left(\frac{z}{2\sqrt{\kappa t}}\right)$$<br>
          - <strong>Inverted Gradient:</strong> The uppermost footwall reaches $450^\circ\text{C}$ (amphibolite/garnet grade), while deeper footwall levels ($z > 5\text{ km}$) remain at lower ambient temperatures ($< 250^\circ\text{C}$). This transient inverted thermal profile bakes the footwall rocks in an inverted sequence from sillimanite/kyanite near the fault down to chlorite at deeper stratigraphic levels.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Geochronologic Dating of Thrusting via Syn-Kinematic Monazites</div>
        <p>
          Why is in-situ U-Th-Pb dating of monazite grains enclosed within syn-kinematic garnet and kyanite porphyroblasts superior to Ar-Ar dating of muscovite for determining the exact timing of MCT movement?
        </p>
        <div class="p-ans">
          <strong>Geochronological Principles:</strong><br>
          - <strong>Monazite Closure Temperature:</strong> Monazite has an exceptionally high U-Th-Pb closure temperature ($T_c > 800\text{--}900^\circ\text{C}$), which is higher than peak MCT metamorphism. Chemical zoning and inclusions aligned with the mylonitic foliation directly date metamorphic crystal growth during active ductile thrusting ($23\text{--}16\text{ Ma}$).<br>
          - <strong>Muscovite Ar-Ar Limitation:</strong> Argon in muscovite has a low closure temperature of only $T_c \approx 350\text{--}400^\circ\text{C}$. In high-grade terrains, muscovite continues to lose radiogenic $^{40}\text{Ar}$ by volume diffusion long after thrusting ceases, recording only the timing of late exhumation and cooling below $350^\circ\text{C}$ ($< 12\text{--}8\text{ Ma}$), rather than the onset of thrust motion.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Valdiya's Vaikrita vs. Munsiari Formations</div>
        <p>
          In the Kumaun Himalaya, contrast the lithological and metamorphic characteristics of the Munsiari Formation (MCT-I hanging wall) and the Vaikrita Group (MCT-II hanging wall).
        </p>
        <div class="p-ans">
          <strong>Stratigraphic & Metamorphic Contrast:</strong><br>
          - <strong>Munsiari Formation (Between MCT-I and MCT-II):</strong> Composed of chlorite-sericite schists, biotite phyllites, highly sheared mylonitic augen gneisses, and amphibolites. Represents sheared basement rocks metamorphosed at green-schist to lower amphibolite facies ($T \approx 450\text{--}550^\circ\text{C}$).<br>
          - <strong>Vaikrita Group (True HHC above MCT-II):</strong> Composed of coarse-grained garnet-kyanite-sillimanite psammitic gneisses, calc-silicate marbles, migmatites, and tourmaline leucogranite intrusions. Represents high-grade upper amphibolite to granulite facies ($T \approx 650\text{--}780^\circ\text{C}$, $P \approx 8\text{--}11\text{ kbar}$).
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Seismic Hazards and the Main Himalayan Thrust (MHT) Ramp</div>
        <p>
          Geodetic GPS measurements reveal that the Main Himalayan Thrust is completely locked from the surface down to a depth of $\sim 15\text{--}18\text{ km}$, accumulating an elastic slip deficit of $18\text{ mm/yr}$. If a mid-crustal ramp exists beneath the High Himalayan front, explain how it controls the nucleation and rupture of great Himalayan earthquakes.
        </p>
        <div class="p-ans">
          <strong>Seismotectonic Mechanism:</strong><br>
          1. <strong>The MHT Mid-Crustal Ramp:</strong> Geophysical imaging shows the basal MHT décollement is nearly flat beneath the Ganga Basin and Sub-Himalaya, steepens into a prominent ramp dipping at $\sim 15\text{--}20^\circ$ beneath the front of the Higher Himalaya, and flattens again into a ductile horizontal shear zone beneath Tibet.<br>
          2. <strong>Stress Concentration & Nucleation:</strong> The transition from ductile creep at depth to brittle stick-slip behavior occurs precisely at this mid-crustal ramp (coinciding with the $350^\circ\text{C}$ isotherm). Elastic strain accumulates at the ramp updip boundary, where great ruptures (such as the $M_w 7.8$ Gorkha earthquake in 2015) nucleate and propagate southward toward the MBT and MFT.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 83, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q083_Main_Central_Thrust_MCT_Himalaya_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q083: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q083()
