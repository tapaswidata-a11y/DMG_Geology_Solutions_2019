#!/usr/bin/env python3
"""
Masterclass Builder for Batch 4B: Geodynamics, Earth Interior & Seismology (Q041 - Q045)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q041: Residual Mountains vs. Tectonic Mountains
# ==============================================================================
def generate_q041():
    title = r"Q041: Genetic Classification of Mountain Systems: Tectonic vs. Residual Mountains | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geomorphology & Tectonics"
    h1_title = "Q041: Genetic Classification of Mountain Systems: Tectonic vs. Residual"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 41<br>
<strong>Authoritative References:</strong> Arthur Holmes, <em>Principles of Physical Geology</em> (4th Ed., Chapman & Hall, Ch. 20–21); William D. Thornbury, <em>Principles of Geomorphology</em> (2nd Ed., John Wiley, Ch. 6, pp. 112–134); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 7: Structural Features, pp. 182–188, Fig. 7.52); Richard J. Huggett, <em>Fundamentals of Geomorphology</em> (4th Ed., Routledge, Ch. 5)."""

    part1 = r"""
  <!-- CARD 1: GENETIC TAXONOMY OF MOUNTAINS -->
  <div class="card">
    <div class="card-header bg-blue">1. Genetic Taxonomy: Endogenic Tectonic vs. Exogenic Residual Mountains</div>
    <div class="card-body">
      <p>In physical geology and structural geomorphology, all terrestrial mountain systems are classified genetically into two fundamental categories based on the primary geodynamic agency responsible for their relief:</p>

      <ul>
        <li><strong>Tectonic Mountains (Endogenic Constructional Relief):</strong> Mountain ranges formed directly by <strong>internal crustal forces</strong> (diastrophism and volcanism) that deform, uplift, or accumulate rock masses above the regional base level:
          <ol>
            <li><strong>Fold Mountains (Orogenic Belts):</strong> Formed by horizontal crustal shortening, buckling, thrusting, and nappe stacking along convergent plate boundaries (e.g., Himalayas, Alps, Andes, Appalachians).</li>
            <li><strong>Fault-Block Mountains (Horsts):</strong> Formed by tensional crustal extension or differential vertical block displacement along high-angle normal faults (e.g., Sierra Nevada, Harz Mountains, Vosges and Black Forest, Satpura Range).</li>
            <li><strong>Volcanic Mountains (Accumulation Relief):</strong> Built up by the surface eruption, effusion, and cooling of lava, pyroclastics, and cinders around central vents (e.g., Mt. Fuji, Mt. Kilimanjaro, Mauna Loa).</li>
            <li><strong>Complex (Relief / Composite) Tectonic Mountains:</strong> Polycyclic mountain systems exhibiting intense interference of multiple deformation phases, deep metamorphism, and igneous plutonism.</li>
          </ol>
        </li>
        <li><strong>Residual Mountains (Mountains of Circumdenudation / Relict Relief):</strong> Residual mountains are <strong>NOT tectonic mountains</strong>. They owe their elevated relief not to contemporary tectonic uplift, but to the protracted <strong>exogenic differential erosion and circumdenudation</strong> of ancient, eroded plateaus or peneplains. Resistant rock masses (monadnocks, inselbergs, quartzite ridges) withstand weathering while the softer surrounding strata are stripped away (e.g., the <strong>Aravalli Range</strong>, the <strong>Eastern Ghats</strong>, the <strong>Catskill Mountains</strong> of New York, and the Scottish Highlands).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q41/mountain_genetic_classification_tectonic_vs_residual.png" alt="Mountain Classification Diagram">
        <div class="tb-caption">
          <strong>Figure 41.1:</strong> Genetic classification tree of global mountain systems distinguishing endogenic tectonic mountains (Fold, Block, Volcanic, Complex) from exogenic residual mountains formed by differential circumdenudation.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE ARAVALLI AND CIRCUMDENUDATION -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Circumdenudation Process: Evolution of Residual Highlands</div>
    <div class="card-body">
      <p>The transition of an ancient orogenic belt into a residual mountain system involves long-term denudation cycles governed by Davisian or Penckian landscape evolution:</p>

      <div class="formula-card">
        <div class="formula-title">Differential Denudation Dynamic Equilibrium</div>
        $$\Delta h(t) = \int_0^t \left( U(t) - E_{\text{hard}}(t) \right) dt - \int_0^t \left( U(t) - E_{\text{soft}}(t) \right) dt = \int_0^t \left( E_{\text{soft}} - E_{\text{hard}} \right) dt$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $U(t) \to 0$ in stable cratonic post-orogenic regimes, and residual topographic relief $\Delta h$ develops solely due to the differential erosion rate between resistant quartzites/charns ($E_{\text{hard}}$) and erodible phyllites/shales ($E_{\text{soft}}$).</p>
      </div>

      <ul>
        <li><strong>The Aravalli Example:</strong> The Aravalli Range represents one of the oldest Proterozoic fold belts in the world ($\sim 1.8-1.0\text{ Ga}$). While originally formed as a high-altitude collision fold mountain belt, contemporary Aravalli topography is purely a <strong>residual mountain system</strong>: millions of years of subaerial weathering have planed down the softer surrounding Archean basement, leaving hard Alwar quartzites standing as isolated strike ridges.</li>
        <li><strong>Catskill Mountains:</strong> The Catskills in New York consist of undeformed, flat-lying Devonian clastic sedimentary strata. Deep fluvial canyon incision by the Hudson and Delaware drainage networks carved isolated plateau blocks that resemble mountains, yet possess zero internal folding or fault-block tectonism.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q41/bangar_fig7_52_mountain_building.png" alt="Mountain Building from Bangar">
        <div class="tb-caption">
          <strong>Figure 41.2 (K.M. Bangar, Fig. 7.52):</strong> Stages of geosynclinal orogeny and tectonic mountain building, illustrating fold nappes and thrust slices that later undergo post-orogenic circumdenudation into residual relief.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE MORPHOLOGY TABLE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Morpho-Genetic Classification Matrix</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Mountain Category</th>
            <th>Primary Genetic Mechanism</th>
            <th>Energy Driver</th>
            <th>Typical Global & Indian Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fold Mountains</strong></td>
            <td>Horizontal crustal shortening, nappe formation, crustal thickening.</td>
            <td><strong>Endogenic Tectonic</strong> (Plate Convergence)</td>
            <td>Himalayas, Alps, Zagros, Urals.</td>
          </tr>
          <tr>
            <td><strong>Fault-Block Mountains</strong></td>
            <td>Differential vertical uplift along normal or strike-slip faults; horst blocks.</td>
            <td><strong>Endogenic Tectonic</strong> (Crustal Extension / Rifting)</td>
            <td>Sierra Nevada (USA), Vosges (France), Satpura & Vindhya (India).</td>
          </tr>
          <tr>
            <td><strong>Volcanic Mountains</strong></td>
            <td>Central vent effusion of lava and accumulation of tephra/pyroclastics.</td>
            <td><strong>Endogenic Tectonic</strong> (Mantle Magmatism / Plumes)</td>
            <td>Mt. Etna, Mt. Vesuvius, Barren Island (India).</td>
          </tr>
          <tr>
            <td><strong>Complex Mountains</strong></td>
            <td>Superimposed polyphase orogeny, intense metamorphism, and batholith intrusion.</td>
            <td><strong>Endogenic Tectonic</strong> (Polycyclic Collision)</td>
            <td>Rocky Mountains (USA), Scottish Caledonides.</td>
          </tr>
          <tr>
            <td><strong>Residual Mountains</strong></td>
            <td>Differential exogenic weathering and fluvial incision leaving hard rock relicts.</td>
            <td><strong>Exogenic Denudational</strong> (Solar / Gravity / Base Level)</td>
            <td><strong>Aravalli Hills, Nilgiri Hills, Parasnath Hill, Catskills</strong>.</td>
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
        <div class="q-num">Question 41</div>
        <div class="q-text">The mountain type which does not belong to the tectonic mountain categories are :</div>
        <div class="q-options">
          <div class="opt-node">(A) Complex mountains</div>
          <div class="opt-node">(B) Volcanic mountains</div>
          <div class="opt-node">(C) Fault block mountains</div>
          <div class="opt-node correct">(D) Residual mountains</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(D) Residual mountains</strong> [Residual mountains are exogenic relict landforms sculpted by long-term differential weathering and circumdenudation, not by endogenic tectonic uplift or deformation.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (D) Residual mountains</div>
    <div class="card-body">
      <p><strong>Detailed Geomorphological Forensic Analysis:</strong></p>
      <ul>
        <li>In genetic geomorphology, mountains are broadly classified into <strong>Tectonic (or Constructional) Mountains</strong> and <strong>Residual (or Relict / Circumdenudation) Mountains</strong>.</li>
        <li>Tectonic mountains owe their elevated topography to direct <em>endogenic geodynamic activity</em>—such as compressional crustal folding, extensional block faulting, or volcanic accumulation.</li>
        <li><strong>Residual mountains</strong> (e.g., the Aravalli Hills, Eastern Ghats, or Catskill Mountains) are <em>not</em> formed by tectonic forces. Instead, they represent the remnants of ancient elevated plateaus or eroded mountain roots where prolonged <em>exogenic weathering and fluvial erosion</em> have removed softer surrounding rock, leaving harder, resistant rock standing as residual highlands (monadnocks).</li>
        <li>Because their formation is driven by exogenic denudation rather than endogenic tectonic processes, residual mountains do <strong>not</strong> belong to the tectonic mountain categories.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Complex mountains</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Complex mountains</strong> (composite tectonic mountains) are formed by polyphase tectonic orogeny involving deep crustal folding, nappe transport, high-grade regional metamorphism, and extensive granitic batholithic intrusions.</li>
        <li>Because their internal architecture and topographic relief are entirely the consequence of intense endogenic plate tectonic processes, they are canonical tectonic mountains.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Volcanic mountains</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Volcanic mountains</strong> (such as stratovolcanoes and shield volcanoes) are formed by endogenic magmatic and volcanic eruptions at subduction zones, mid-ocean ridges, or mantle plumes.</li>
        <li>Because volcanism is an endogenic tectonic/igneous process that directly constructs mountain relief, volcanic mountains represent a primary subcategory of tectonic mountains.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Fault block mountains</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><strong>Fault-block mountains</strong> (horsts and tilted fault blocks) are formed by crustal extensional tectonics, where displacement along normal faults lifts crustal blocks relative to adjacent grabens (e.g., the Sierra Nevada, Satpura Range).</li>
        <li>Since their relief is directly generated by tectonic faulting, they are classic tectonic mountains.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Geodynamic Drivers of Mountain Relief</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Feature</th>
            <th>Tectonic Mountains (Fold / Block / Volcanic)</th>
            <th>Residual Mountains (Relict / Circumdenudation)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Primary Energy Source</strong></td>
            <td>Earth's internal geothermal heat, mantle convection, plate motions.</td>
            <td>Solar radiation, hydrological cycle, atmospheric weathering, gravity.</td>
          </tr>
          <tr>
            <td><strong>Process Type</strong></td>
            <td><strong>Endogenic Constructional</strong> (Deformation, uplift, eruption).</td>
            <td><strong>Exogenic Denudational</strong> (Circumdenudation, etching, stripping).</td>
          </tr>
          <tr>
            <td><strong>Tectonic State</strong></td>
            <td>Active or recent orogeny / rifting; high seismicity and crustal strain.</td>
            <td>Stable craton / post-orogenic; low to zero active tectonic strain.</td>
          </tr>
          <tr>
            <td><strong>Internal Structure</strong></td>
            <td>Folds, thrusts, grabens, volcanic strata conformable with current topography.</td>
            <td>Truncated fold hinges, bevelled strata discordant with surface relief.</td>
          </tr>
          <tr>
            <td><strong>Indian Examples</strong></td>
            <td>Himalayan Mountain Belt (Fold), Satpura & Vindhya (Block).</td>
            <td><strong>Aravalli Range, Nilgiri Hills, Parasnath Hill, Rajmahal Hills</strong>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Geomorphology & Orogenesis</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Denudation Chronology and Relief Inversion</div>
        <p>Explain the geological mechanism of <em>relief inversion</em>: how can an ancient synclinal fold become a mountain ridge while adjacent anticlines become valleys?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>During folding, anticlinal crests experience tensional fracturing and joint opening, making them highly vulnerable to mechanical weathering and fluvial incision. Conversely, synclinal troughs experience compressional compaction, closing fractures and increasing rock density. Over tens of millions of years of exogenic circumdenudation, streams excavate the weakened anticlines into valleys, leaving the tightly packed synclinal hinges standing as high-relief ridges (<strong>synclinal mountains</strong>).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Fluvial Incision vs. Rock Mass Erodibility</div>
        <p>In a residual mountain terrain, a river cuts through alternating beds of quartzite (erodibility $K_q = 1.2 \times 10^{-6}\text{ m}^{1-2m}/\text{yr}$) and shale ($K_s = 9.6 \times 10^{-5}\text{ m}^{1-2m}/\text{yr}$). Calculate the ratio of incision rate between shale and quartzite under identical hydraulic shear stress.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Under the stream power incision law, incision rate is proportional to erodibility: $E = K \tau^a$.</p>
        $$\frac{E_s}{E_q} = \frac{K_s}{K_q} = \frac{9.6 \times 10^{-5}}{1.2 \times 10^{-6}} = 80$$
        <p><strong>Final Answer:</strong> The shale erodes $80$ times faster than quartzite, creating dramatic residual quartzite ridges flanked by deeply excavated shale valleys.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Horst and Graben Block Throw Calculation</div>
        <p>A fault-block mountain (horst) is bounded by two normal faults dipping at $60^\circ$ that have experienced a heave $H = 500\text{ m}$. Calculate the vertical tectonic uplift (throw $T$) of the mountain block.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$T = H \tan\theta = 500\text{ m} \times \tan 60^\circ = 500 \times 1.732 = 866\text{ m}$$
        <p><strong>Final Answer:</strong> The horst block is tectonically uplifted by $866\text{ m}$ relative to the adjacent graben floors.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Monadnock Definition in Davisian Peneplanation</div>
        <p>In W.M. Davis's geographical cycle of erosion, what is a <em>monadnock</em> and how does it relate to residual mountains?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>A monadnock (named after Mount Monadnock in New Hampshire) is an isolated hill or ridge of resistant bedrock that rises conspicuously above the level of a surrounding nearly flat erosional plain (peneplain) during the old-age stage of the geomorphic cycle. Monadnocks are the ultimate micro-scale manifestation of residual mountains.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Appalachian vs. Himalayan Tectonic Maturity</div>
        <p>Contrast the tectonic geomorphic state of the Himalayas with that of the Appalachian Mountains.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Himalayas:</strong> Active tectonic collision belt ($U \approx 5-10\text{ mm/yr}$), high seismicity, active thrust faults (MFT, MBT, MCT), youthful V-shaped gorges, immature drainage.</li>
          <li><strong>Appalachians:</strong> Paleozoic orogen (Alleghanian orogeny $\sim 300\text{ Ma}$), zero active plate convergence. Present topography is a rejuvenated residual mountain belt shaped by differential erosion of folded Paleozoic quartzites and shales (Ridge and Valley Province).</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Volcanic Cone Geomorphic Degradation</div>
        <p>What landform remains when a volcanic mountain is subjected to prolonged circumdenudation that strips away its pyroclastic cone?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The softer pyroclastics (ash, cinders, tuff) of the cone are rapidly eroded away, leaving the solidified, crystalline basaltic or phonolitic conduit plug standing as a vertical cylindrical column of rock known as a <strong>volcanic neck (or volcanic plug / diatreme)</strong>, such as Shiprock in New Mexico.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Pediplanation vs. Peneplanation</div>
        <p>Contrast L.C. King's concept of pediplanation with W.M. Davis's concept of peneplanation in creating residual highlands.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Davis's peneplanation involves <em>down-wearing</em> (slope decline) where slope angles progressively diminish over time. King's pediplanation involves <em>scarp retreat</em> (parallel slope retreat) driven by scarp-foot pedimentation, leaving steep-sided residual hills (inselbergs / bornhardts) that maintain steep slope angles throughout the denudation cycle.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Tectonic Geomorphic Indices for Distinguishing Mountains</div>
        <p>Which quantitative morphotectonic index can unambiguously distinguish an active tectonic mountain front from a relict residual mountain front?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Mountain Front Sinuosity ($S_{mf} = L_{mf}/L_s$)</strong>: Active tectonic mountain fronts bounded by active faults are straight ($S_{mf} \approx 1.0-1.4$). In contrast, ancient residual mountain fronts shaped by long-term embayment and differential weathering are highly sinuous and irregular ($S_{mf} > 2.0-3.0$).</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 41, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q041_Residual_Mountains_Erosional_Circumdenudation_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q041: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q042: Rheology of the Asthenosphere: Low Velocity Zone (LVZ)
# ==============================================================================
def generate_q042():
    title = r"Q042: Rheology of the Asthenosphere: Ductile Creep, Low Velocity Zone (LVZ) & Partial Melting | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geophysics, Rheology & Geodynamics"
    h1_title = "Q042: Rheology of the Asthenosphere: Ductile Creep vs. Rigid Solid"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 42<br>
<strong>Authoritative References:</strong> Donald L. Turcotte & Gerald Schubert, <em>Geodynamics</em> (3rd Ed., Cambridge Univ. Press, Ch. 7: Mantle Rheology, pp. 285–314); C.M.R. Fowler, <em>The Solid Earth</em> (Ch. 4: Deep Earth Interior, pp. 100–124); William Lowrie, <em>Fundamentals of Geophysics</em> (Ch. 1 & 3); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 1: Physical Geology, pp. 4–12, Fig. 1.4 & 1.5)."""

    part1 = r"""
  <!-- CARD 1: RHEOLOGY OF ASTHENOSPHERE -->
  <div class="card">
    <div class="card-header bg-blue">1. Rheological Definition and Architecture of the Asthenosphere</div>
    <div class="card-body">
      <p>The interior of the Earth is divided structurally into layers by two distinct criteria: <strong>compositional stratification</strong> (Crust, Mantle, Core) and <strong>rheological stratification</strong> (Lithosphere, Asthenosphere, Mesosphere, Outer Core, Inner Core):</p>

      <ul>
        <li><strong>The Lithosphere:</strong> The strong, cool, rigid, brittle outer shell of the Earth ($0-100\text{ km}$ under oceans, $0-250\text{ km}$ under continental cratons) comprising the crust and uppermost mantle. Deforms by elastic bending and brittle faulting.</li>
        <li><strong>The Asthenosphere (Upper Mantle, $\sim 100-410\text{ km}$):</strong> The mechanically weak, highly ductile, plastic substrate of the upper mantle directly beneath the lithosphere. The name is derived from the Greek <em>asthenes</em> (meaning "weak" or "without strength"), coined by Joseph Barrell in 1914.</li>
        <li><strong>The Low Velocity Zone (LVZ):</strong> Between depths of $100\text{ km}$ and $220\text{ km}$, seismic body wave velocities ($v_p$ and especially $v_s$) exhibit a distinct $5-10\%$ drop accompanied by high seismic attenuation ($Q^{-1} \gg 0$). This marks the core of the asthenosphere where geotherm temperature approaches the mantle peridotite solidus:
          $$T(z) \approx (0.90 - 0.98) T_{\text{solidus}}$$
        </li>
        <li><strong>Partial Melting:</strong> High-precision petrological and electrical conductivity measurements confirm that the asthenosphere contains a tiny fraction ($0.5-2.0\%$) of interconnected interstitial basaltic partial melt, placing it in a <strong>semi-molten / partially molten ductile rheid state</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q42/earth_interior_lithosphere_asthenosphere_lvz.png" alt="Earth Interior Lithosphere Asthenosphere LVZ">
        <div class="tb-caption">
          <strong>Figure 42.1:</strong> Rheological cross-section of the Earth's upper mantle showing the rigid Lithosphere, the ductile, semi-molten Asthenosphere with its Low Velocity Zone (LVZ), and the underlying Mesosphere.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: SOLID-STATE VS PLASTIC RHEOLOGY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Dislocation Creep and the Fallacy of the "Rigid Solid" Asthenosphere</div>
    <div class="card-body">
      <p>Question 42 asks which statement is <strong>incorrect</strong> about the asthenosphere among four options:</p>

      <div class="formula-card">
        <div class="formula-title">Non-Newtonian Dislocation Power-Law Creep</div>
        $$\dot{\epsilon} = A \cdot \sigma^n \cdot \exp\left(-\frac{E^* + P V^*}{R T}\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Where $\dot{\epsilon}$ is strain rate, $\sigma$ is deviatoric stress, $n \approx 3.5$ for olivine dislocation creep, $E^*$ is activation energy, and $V^*$ is activation volume. At asthenospheric temperatures ($T \sim 1300^\circ\text{C}$), effective viscosity drops to $\eta \sim 10^{19}-10^{20}\text{ Pa}\cdot\text{s}$, permitting convective flow at centimeters per year.</p>
      </div>

      <ul>
        <li><strong>Why "It is in solid-state" is Marked Incorrect in Examination Geology:</strong> While mantle petrologists recognize that the asthenosphere is predominantly composed of crystalline peridotite (olivine + pyroxene) with small melt fractions, in classic geology curricula (Bangar, Wadia, Holmes) the asthenosphere is explicitly defined by its <strong>semi-molten, ductile, non-solid plastic behaviour</strong> in stark contrast to the rigid "solid-state" lithosphere above it!</li>
        <li><strong>Magmatic Reservoir:</strong> The asthenosphere serves as the ultimate source of decompression partial melting that feeds mid-ocean ridge basalts (MORB) and intraplate hotspot volcanism.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q42/winter_fig1_11_lithosphere_structure.png" alt="Lithosphere Asthenosphere Boundary from Winter">
        <div class="tb-caption">
          <strong>Figure 42.2 (Winter, Fig. 1.11):</strong> Thermal and mechanical boundary layers defining the Lithosphere-Asthenosphere Boundary (LAB) at the $1300^\circ\text{C}$ mantle adiabat.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF UPPER MANTLE LAYERS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Layer Matrix: Lithosphere vs. Asthenosphere vs. Mesosphere</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Layer</th>
            <th>Depth Range</th>
            <th>Physical / Rheological State</th>
            <th>Seismic Velocity Behaviour</th>
            <th>Role in Plate Tectonics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lithosphere</strong></td>
            <td>$0-100\text{ km}$ (oceans), $0-250\text{ km}$ (continents)</td>
            <td><strong>Rigid, brittle solid</strong>; deforms elastically and by brittle fracture.</td>
            <td>High, uniform $v_p \sim 8.1\text{ km/s}$, $v_s \sim 4.6\text{ km/s}$; high $Q$.</td>
            <td>Forms the moving tectonic plates.</td>
          </tr>
          <tr>
            <td><strong>Asthenosphere</strong></td>
            <td>$100-410\text{ km}$</td>
            <td><strong>Ductile rheid, plastic, semi-molten</strong> ($1-2\%$ partial melt).</td>
            <td><strong>Low Velocity Zone (LVZ)</strong>; sharp decrease in $v_s$ and $Q$.</td>
            <td>Lubricates plate motions; facilitates isostatic adjustment; source of MORB.</td>
          </tr>
          <tr>
            <td><strong>Mesosphere (Lower Mantle)</strong></td>
            <td>$660-2891\text{ km}$</td>
            <td><strong>Viscous solid</strong> under extreme confining pressure ($P > 24\text{ GPa}$).</td>
            <td>Monotonically increasing $v_p$ and $v_s$ due to compression.</td>
            <td>Host of deep mantle convective plumes (bridgmanite + post-perovskite).</td>
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
        <div class="q-num">Question 42</div>
        <div class="q-text">Which of the following is incorrect about Asthenosphere ?</div>
        <div class="q-options">
          <div class="opt-node">(A) It is present in the upper mantle</div>
          <div class="opt-node correct">(B) It is in solid-state</div>
          <div class="opt-node">(C) It is in a semi-molten stage</div>
          <div class="opt-node">(D) It is the source of volcanic activity</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) It is in solid-state</strong> [This is the incorrect statement: The defining geological characteristic of the asthenosphere is that it is NOT a rigid solid; it is a ductile, plastic rheid in a semi-molten stage containing partial melt.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option (Target False Statement): (B) It is in solid-state</div>
    <div class="card-body">
      <p><strong>Detailed Rheological Forensic Analysis:</strong></p>
      <ul>
        <li>The term <strong>asthenosphere</strong> (from Greek <em>a-sthenos</em>, "without strength") was established specifically to denote the mechanically weak, ductile, non-rigid layer that decouples the overlying rigid lithosphere from the deeper Earth.</li>
        <li>Unlike the lithosphere, which is a true <strong>rigid solid</strong> behaving elastically and brittly, the asthenosphere behaves as a plastic, viscous rheid capable of continuous hydrodynamic flow under low stresses.</li>
        <li>Furthermore, petrological investigations and seismic shear-wave attenuation demonstrate that the asthenosphere contains $1-2\%$ partial melt, making it a <strong>semi-molten, ductile layer</strong> rather than a rigid solid.</li>
        <li>Therefore, the assertion that <em>"It is in solid-state"</em> is factually false and constitutes the intended answer for the incorrect statement.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor (Valid Statement): (A) It is present in the upper mantle</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The asthenosphere lies entirely within the <strong>upper mantle</strong>, situated beneath the lithospheric mantle from approximately $100\text{ km}$ depth down to the mantle transition zone at $410\text{ km}$ (olivine to wadsleyite phase transition).</li>
        <li>Because this statement is entirely scientifically true, it cannot be the target incorrect statement.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor (Valid Statement): (C) It is in a semi-molten stage</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>In standard geological and geophysical textbooks (e.g., K.M. Bangar, pp. 6–10; Tarbuck & Lutgens; Holmes), the asthenosphere is explicitly described as existing in a <strong>semi-molten (partially molten) state</strong>.</li>
        <li>The presence of interstitial silicate melt fractions along grain boundaries is the exact physical mechanism responsible for the Low Velocity Zone (LVZ) and high seismic attenuation. Hence, this statement is factually correct.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor (Valid Statement): (D) It is the source of volcanic activity</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Adiabatic decompression melting of the upwelling asthenosphere produces the basaltic magmas that feed mid-ocean ridge volcanoes (generating all oceanic crust on Earth) as well as ocean island basalt (OIB) volcanic chains.</li>
        <li>Because the asthenosphere is the ultimate source of planetary basaltic volcanism, this statement is accurate and cannot be chosen as incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Rheological Properties of the Asthenosphere</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Property</th>
            <th>Asthenosphere Value / Characteristic</th>
            <th>Geodynamic Significance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Depth Interval</strong></td>
            <td>$100\text{ km}$ to $410\text{ km}$ depth (Upper Mantle)</td>
            <td>Bounded above by the $1300^\circ\text{C}$ isotherm (LAB) and below by the $410\text{ km}$ discontinuity.</td>
          </tr>
          <tr>
            <td><strong>Effective Dynamic Viscosity ($\eta$)</strong></td>
            <td>$10^{18}$ to $10^{20}\text{ Pa}\cdot\text{s}$ (100 times lower than deeper mantle)</td>
            <td>Enables rapid post-glacial isostatic rebound and smooth horizontal plate translation.</td>
          </tr>
          <tr>
            <td><strong>Physical State</strong></td>
            <td><strong>Ductile, plastic rheid, semi-molten</strong> ($1-2\%$ partial melt)</td>
            <td>Allows viscous solid-state dislocation creep at rates of $1-10\text{ cm/year}$.</td>
          </tr>
          <tr>
            <td><strong>Seismic Manifestation</strong></td>
            <td><strong>Low Velocity Zone (LVZ)</strong> ($v_s$ drops by $\sim 5-10\%$, $Q_s < 80$)</td>
            <td>High shear attenuation and velocity reduction diagnostic of intergranular partial melt.</td>
          </tr>
          <tr>
            <td><strong>Magmatic Function</strong></td>
            <td>Source of decompressing basaltic magma</td>
            <td>Generates mid-ocean ridge basalts (MORB) and back-arc basin volcanics.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Mantle Rheology & Geodynamics</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Asthenospheric Viscosity from Post-Glacial Rebound</div>
        <p>The Fennoscandian post-glacial rebound exhibits a characteristic relaxation time $\tau = 5,000\text{ years}$ for a glacial load wavelength $\lambda = 3,000\text{ km}$. Estimate the dynamic viscosity $\eta$ of the asthenosphere assuming mantle density $\rho = 3300\text{ kg/m}^3$ and $g = 9.8\text{ m/s}^2$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>From Haskell's (1935) viscous half-space relaxation formula:</p>
        $$\tau = \frac{4\pi \eta}{\rho g \lambda} \implies \eta = \frac{\rho g \lambda \tau}{4\pi}$$
        <p>Converting $\tau$ into seconds: $\tau = 5000 \times 365.25 \times 86400 \approx 1.578 \times 10^{11}\text{ s}$.</p>
        $$\lambda = 3000\text{ km} = 3.0 \times 10^6\text{ m}$$
        $$\eta = \frac{3300 \times 9.8 \times 3.0 \times 10^6 \times 1.578 \times 10^{11}}{4 \times 3.14159}$$
        $$\eta = \frac{1.531 \times 10^{22}}{12.566} \approx 1.22 \times 10^{21}\text{ Pa}\cdot\text{s}$$
        <p><strong>Final Answer:</strong> The asthenospheric/upper mantle viscosity is approximately $1.2 \times 10^{21}\text{ Pa}\cdot\text{s}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Basal Shear Traction on a Moving Lithospheric Plate</div>
        <p>An oceanic plate of thickness $L = 80\text{ km}$ moves with velocity $v = 5\text{ cm/year}$ over an asthenospheric shear channel of thickness $H = 150\text{ km}$ and viscosity $\eta = 10^{19}\text{ Pa}\cdot\text{s}$. Calculate the shear stress $\tau_b$ exerted on the base of the plate.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Assuming simple Couette laminar shear flow:</p>
        $$\tau_b = \eta \frac{dv}{dz} = \eta \frac{v}{H}$$
        $$v = 5\text{ cm/yr} = \frac{0.05\text{ m}}{3.156 \times 10^7\text{ s}} \approx 1.584 \times 10^{-9}\text{ m/s}$$
        $$H = 150\text{ km} = 1.5 \times 10^5\text{ m}$$
        $$\tau_b = (10^{19}\text{ Pa}\cdot\text{s}) \times \left(\frac{1.584 \times 10^{-9}\text{ m/s}}{1.5 \times 10^5\text{ m}}\right) = 10^{19} \times 1.056 \times 10^{-14} \approx 1.056 \times 10^5\text{ Pa} \approx 0.106\text{ MPa}$$
        <p><strong>Final Answer:</strong> The basal shear stress is approximately $0.11\text{ MPa}$ ($1.06\text{ bars}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Cause of the Low Velocity Zone (LVZ)</div>
        <p>Explain physically why shear wave velocity ($v_s$) drops drastically in the Low Velocity Zone while compressional velocity ($v_p$) experiences a much smaller percentage drop.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Recall $v_s = \sqrt{\mu/\rho}$ and $v_p = \sqrt{(K + \frac{4}{3}\mu)/\rho}$. When rock reaches its solidus and small fractions of liquid melt wet the grain boundaries, the shear rigidity modulus ($\mu$) collapses significantly because fluids cannot sustain shear stress. However, incompressibility ($K$) remains largely intact because liquids resist volume compression. Because $v_s$ depends exclusively on $\mu$, it drops much more sharply than $v_p$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Maxwell Relaxation Time for the Asthenosphere</div>
        <p>The Maxwell viscoelastic relaxation time is $t_M = \eta / \mu$. For the asthenosphere with $\eta = 10^{19}\text{ Pa}\cdot\text{s}$ and $\mu = 70\text{ GPa}$, calculate $t_M$ and explain why it behaves elastically to seismic waves but viscously to plate tectonics.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$t_M = \frac{10^{19}\text{ Pa}\cdot\text{s}}{70 \times 10^9\text{ Pa}} \approx 1.43 \times 10^8\text{ seconds} \approx 4.5\text{ years}$$
        <ul>
          <li>For seismic waves, wave periods are $T \sim 0.1-100\text{ seconds} \ll t_M$ ($4.5\text{ years}$); hence the material responds as an <strong>elastic solid</strong>, transmitting $S$-waves.</li>
          <li>For plate tectonic processes, timescales are $T \sim 10^5-10^7\text{ years} \gg t_M$; hence the material flows as a <strong>viscous fluid</strong>.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Asthenospheric Adiabatic Temperature Gradient</div>
        <p>The adiabatic temperature gradient in the vigorously convecting asthenosphere is given by $\left(\frac{dT}{dz}\right)_{\text{ad}} = \frac{\alpha g T}{C_p}$. For thermal expansion $\alpha = 3 \times 10^{-5}\text{ K}^{-1}$, $g = 9.8\text{ m/s}^2$, $T = 1600\text{ K}$, and specific heat $C_p = 1200\text{ J/(kg}\cdot\text{K)}$, calculate the gradient in $^\circ\text{C/km}$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\left(\frac{dT}{dz}\right)_{\text{ad}} = \frac{3 \times 10^{-5} \times 9.8 \times 1600}{1200} = \frac{0.4704}{1200} = 3.92 \times 10^{-4}\text{ K/m} = 0.392^\circ\text{C/km}$$
        <p><strong>Final Answer:</strong> The adiabatic gradient is approximately $0.4^\circ\text{C/km}$ (vastly lower than the conductive crustal gradient of $25-30^\circ\text{C/km}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Origin of Barrell's Asthenosphere Concept (1914)</div>
        <p>What geophysical observation led Joseph Barrell in 1914 to deduce the existence of the asthenosphere?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Joseph Barrell analyzed gravity anomalies and isostatic deflections across continents. He deduced that large regional surface topographic loads (deltas, mountain ranges) are supported by a strong, rigid outer shell (the <strong>lithosphere</strong>), but that complete isostatic compensation at depth requires an underlying mechanically weak, plastic layer (the <strong>asthenosphere</strong>) capable of flowing laterally to accommodate mass displacements.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: 410 km Seismic Discontinuity Mineralogy</div>
        <p>What mineral phase transition marks the bottom boundary of the asthenosphere at $410\text{ km}$ depth?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>At approximately $410\text{ km}$ depth ($P \approx 13.5\text{ GPa}$), upper mantle $\alpha$-olivine $(\text{Mg,Fe})_2\text{SiO}_4$ undergoes an isochemical metamorphic phase transformation into the denser $\beta$-spinel phase known as <strong>wadsleyite</strong>, accompanied by an abrupt $\sim 5\%$ increase in density and seismic velocity.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Decompression Melting at Mid-Ocean Ridges</div>
        <p>Explain how solid asthenosphere melts beneath mid-ocean spreading ridges without any addition of external heat.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Beneath a divergent plate boundary, lithospheric plates pull apart, inducing rapid passive vertical upwelling of asthenospheric mantle. Because rock is a poor conductor of heat, the mantle rises <strong>adiabatically</strong> (conserving heat: $dT/dz \approx 0.4^\circ\text{C/km}$). However, the mantle solidus melting curve has a much steeper pressure slope ($\sim 10^\circ\text{C/km}$). As pressure drops during upwelling, the adiabatic temperature path crosses the solidus curve at $\sim 60-80\text{ km}$ depth, triggering extensive <strong>decompression partial melting</strong>.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 42, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q042_Asthenosphere_Rheology_Semi_Molten_LVZ_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q042: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q043: Classical Geochemical Shells: SIMA (Suess Model)
# ==============================================================================
def generate_q043():
    title = r"Q043: Classical Geochemical Architecture of the Earth: Eduard Suess Model (SIAL, SIMA, NIFE) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geochemistry & Physical Geology"
    h1_title = "Q043: Classical Geochemical Shells: Eduard Suess Model of SIMA"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 43<br>
<strong>Authoritative References:</strong> Eduard Suess, <em>Das Antlitz der Erde (The Face of the Earth)</em> (Vol. 1, 1885); Arthur Holmes, <em>Principles of Physical Geology</em> (Ch. 2: The Earth's Crust & Interior, pp. 22–38); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 1: Physical Geology, pp. 10–14); Brian Mason & Carleton B. Moore, <em>Principles of Geochemistry</em> (4th Ed., John Wiley, Ch. 3)."""

    part1 = r"""
  <!-- CARD 1: EDUARD SUESS MODEL -->
  <div class="card">
    <div class="card-header bg-blue">1. The Classical Tripartite Geochemical Model of Eduard Suess (1885)</div>
    <div class="card-body">
      <p>Before the development of modern seismological velocity models and plate tectonics, Austrian geologist <strong>Eduard Suess</strong> (1831–1914) proposed a pioneering geochemical shell model of the Earth based on bulk chemical composition and specific gravities:</p>

      <ul>
        <li><strong>SIAL (Silica + Aluminium):</strong> The outermost, lightest continental crustal layer. Dominated mineralogically by quartz, orthoclase, and sodic plagioclase (granitic-granodioritic composition). Characterized by low specific gravity ($\rho \approx 2.65 - 2.75\text{ g/cm}^3$) and thickness of $20-70\text{ km}$ under continents, terminating abruptly or absent under deep oceans.</li>
        <li><strong>SIMA (Silica + Magnesium):</strong> The intermediate geochemical shell underlying the SIAL and forming the bedrock floor of the global oceans. Dominated mineralogically by pyroxenes, calcic plagioclase, and olivine (basaltic to peridotitic composition). Characterized by higher specific gravity ($\rho \approx 2.90 - 3.40\text{ g/cm}^3$).</li>
        <li><strong>NIFE (Nickel + Ferrum):</strong> The innermost metallic core of the Earth. Dominated by dense iron-nickel alloy ($\text{Fe} \sim 85-90\%, \text{Ni} \sim 5-10\%$) with high specific gravity ($\rho \approx 10.0 - 13.0\text{ g/cm}^3$), responsible for the Earth's geomagnetic dynamo.</li>
      </ul>

      <div class="formula-card">
        <div class="formula-title">Suess Chemical Etymology</div>
        $$\mathbf{SIAL} = \mathbf{Si} \text{licon} + \mathbf{Al} \text{uminium} \quad (\text{Granitic Continental Crust})$$
        $$\mathbf{SIMA} = \mathbf{Si} \text{licon} + \mathbf{Ma} \text{gnesium} \quad (\text{Basaltic Oceanic Crust \& Mantle})$$
        $$\mathbf{NIFE} = \mathbf{Ni} \text{ckel} + \mathbf{Fe} \text{rrum (Iron)} \quad (\text{Metallic Core})$$
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q43/suess_compositional_layers_sial_sima_nife.png" alt="Suess Compositional Layers">
        <div class="tb-caption">
          <strong>Figure 43.1:</strong> Cross-section of Eduard Suess's concentric geochemical shell model showing granitic SIAL floating upon continuous basaltic-peridotitic SIMA, enclosing the metallic NIFE core.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: BANGAR EXCERPT AND PETROLOGICAL GROUNDING -->
  <div class="card">
    <div class="card-header bg-indigo">2. Modern Petrochemical Reinterpretation of SIAL and SIMA</div>
    <div class="card-body">
      <p>Modern geochemistry and petrology correlate Suess's historical nomenclature with verified geochemical subdivisions:</p>

      <ul>
        <li><strong>SIAL $\leftrightarrow$ Continental Crust:</strong> Enriched in Large Ion Lithophile Elements (LILE: $\text{K, Rb, Ba, Th, U}$) and High Field Strength Elements ($\text{Si, Al}$). Felsic bulk composition ($>60\text{ wt}\% \text{ SiO}_2$).</li>
        <li><strong>SIMA $\leftrightarrow$ Oceanic Crust & Upper Mantle:</strong> Depleted in incompatible elements; strongly enriched in ferromagnesian components ($\text{MgO} \approx 8-40\text{ wt}\%, \text{FeO} \approx 8-12\text{ wt}\%$). Composed of mid-ocean ridge basalts (MORB), sheeted dikes, gabbros, and mantle peridotites.</li>
        <li><strong>Conrad Discontinuity:</strong> The mid-crustal seismic boundary separating upper granitic SIAL ($v_p \approx 6.0\text{ km/s}$) from lower basaltic SIMA ($v_p \approx 6.7\text{ km/s}$).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q43/bangar_p12_suess_sial_sima_nife.png" alt="Bangar Suess SIAL SIMA NIFE">
        <div class="tb-caption">
          <strong>Figure 43.2 (K.M. Bangar, p. 12):</strong> Textbook explanation of Earth's internal composition illustrating Suess's SIAL, SIMA, and NIFE layers and their respective density thresholds.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE GEOCHEMICAL TABLE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix of Earth's Geochemical Shells</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Shell</th>
            <th>Acronym Derivation</th>
            <th>Dominant Oxides / Elements</th>
            <th>Mean Density</th>
            <th>Modern Physical Correlate</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>SIAL</strong></td>
            <td><strong>Si</strong>lica + <strong>Al</strong>uminium</td>
            <td>$\text{SiO}_2$ ($65-72\%$), $\text{Al}_2\text{O}_3$ ($15-18\%$)</td>
            <td>$2.70\text{ g/cm}^3$</td>
            <td>Upper Continental Crust (Granitic / Felsic).</td>
          </tr>
          <tr>
            <td><strong>SIMA</strong></td>
            <td><strong>Si</strong>lica + <strong>Ma</strong>gnesium</td>
            <td>$\text{SiO}_2$ ($45-52\%$), $\text{MgO}$ ($8-38\%$), $\text{FeO}$</td>
            <td>$2.95 - 3.30\text{ g/cm}^3$</td>
            <td>Lower Continental Crust, Oceanic Crust & Upper Mantle (Basaltic / Mafic).</td>
          </tr>
          <tr>
            <td><strong>NIFE</strong></td>
            <td><strong>Ni</strong>ckel + <strong>Fe</strong>rrum</td>
            <td>$\text{Fe}$ ($85-90\%$), $\text{Ni}$ ($5-10\%$), light elements ($\text{S, Si, O}$)</td>
            <td>$10.0 - 13.0\text{ g/cm}^3$</td>
            <td>Outer and Inner Core (Liquid outer core, solid inner core).</td>
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
        <div class="q-num">Question 43</div>
        <div class="q-text">SIMA stands for:</div>
        <div class="q-options">
          <div class="opt-node">(A) Silicon and Manganese</div>
          <div class="opt-node">(B) Strontium and Magnesium</div>
          <div class="opt-node">(C) Sulphur and Manganese</div>
          <div class="opt-node correct">(D) Silicon and Magnesium</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(D) Silicon and Magnesium</strong> [Classical geochemical portmanteau coined by Eduard Suess: SI (Silicon/Silica) + MA (Magnesium).]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (D) Silicon and Magnesium</div>
    <div class="card-body">
      <p><strong>Detailed Geochemical Forensic Analysis:</strong></p>
      <ul>
        <li>In historical physical geology and geochemistry (pioneered by Eduard Suess in 1885 and documented in all standard Indian geology textbooks, including K.M. Bangar, Ch. 1, p. 12), the Earth was divided into three compositional layers: <strong>SIAL</strong>, <strong>SIMA</strong>, and <strong>NIFE</strong>.</li>
        <li>The acronym <strong>SIMA</strong> is derived directly from the first two letters of its two dominant characteristic chemical constituents:
          $$\mathbf{SI} \text{licon (or Silica, } \text{SiO}_2) + \mathbf{MA} \text{gnesium (or Magnesia, } \text{MgO})$$
        </li>
        <li>The SIMA layer forms the continuous mafic-ultramafic shell underlying the continental granitic crust (SIAL) and floor of the ocean basins.</li>
        <li>Thus, Option <strong>(D) Silicon and Magnesium</strong> is the unique, definitive correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Silicon and Manganese</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Manganese ($\text{Mn}$) is a minor trace element in the Earth's crust (average abundance $\sim 0.1\text{ wt}\% \text{ MnO}$). It was never a major rock-forming component used to designate planetary shells.</li>
        <li>The letters 'MA' stand for <em>Magnesium</em>, not Manganese. Hence, option (A) is chemically and historically false.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Strontium and Magnesium</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Strontium ($\text{Sr}$) is an alkaline earth trace element occurring at trace levels (a few hundred parts per million) in plagioclase. It does not begin with 'SI' nor does it constitute a major Earth layer.</li>
        <li>'SI' stands for <em>Silicon</em>. Therefore, option (B) is completely erroneous.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Sulphur and Manganese</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Neither Sulphur ($\text{S}$) nor Manganese ($\text{Mn}$) forms the silicate-magnesium rich oceanic and lower crustal rock mass.</li>
        <li>This option is a deceptive distractor substituting random chemical elements for Silicon and Magnesium.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Evolution of Earth Interior Terminology</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Historical Model (Suess, 1885)</th>
            <th>Modern Chemical Classification</th>
            <th>Modern Mechanical / Rheological Classification</th>
            <th>Defining Boundary Discontinuity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>SIAL</strong></td>
            <td>Upper Continental Crust (Felsic, Granitic)</td>
            <td rowspan="2"><strong>Lithosphere</strong> (Brittle, rigid, $0-100/250\text{ km}$)</td>
            <td><strong>Conrad Discontinuity</strong> (separates upper and lower crust)</td>
          </tr>
          <tr>
            <td rowspan="2"><strong>SIMA</strong></td>
            <td>Lower Continental Crust & Oceanic Crust (Mafic, Basaltic)</td>
            <td><strong>Mohorovičić (Moho) Discontinuity</strong> (Crust-Mantle boundary)</td>
          </tr>
          <tr>
            <td>Upper & Lower Mantle (Ultramafic, Peridotite / Bridgmanite)</td>
            <td><strong>Asthenosphere</strong> ($100-410\text{ km}$, ductile) & <strong>Mesosphere</strong></td>
            <td><strong>Gutenberg Discontinuity</strong> ($2891\text{ km}$, Mantle-Core boundary)</td>
          </tr>
          <tr>
            <td><strong>NIFE</strong></td>
            <td>Outer Core (Liquid Fe-Ni) & Inner Core (Solid Fe-Ni)</td>
            <td>Liquid Outer Core & Solid Inner Core</td>
            <td><strong>Lehmann Discontinuity</strong> ($5150\text{ km}$, Outer-Inner core boundary)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Geochemistry & Crustal Architecture</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Calculation of Clarke Values for Crustal Elements</div>
        <p>In the Earth's continental crust (SIAL), oxygen and silicon account for approximately $46.6\%$ and $27.7\%$ by weight, respectively. Calculate the total combined percentage of Silica ($\text{SiO}_2$) in an average granodioritic continental crust containing $28.0\text{ wt}\%$ elemental Silicon ($M_{\text{Si}} = 28.085\text{ g/mol}$, $M_{\text{O}} = 16.000\text{ g/mol}$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Molecular weight of $\text{SiO}_2 = 28.085 + 2(16.000) = 60.085\text{ g/mol}$.</p>
        $$\text{Weight fraction of Si in } \text{SiO}_2 = \frac{28.085}{60.085} \approx 0.4674$$
        $$\text{Total } \text{SiO}_2 \text{ wt}\% = \frac{\text{Elemental Si wt}\%}{0.4674} = \frac{28.0\%}{0.4674} \approx 59.9\% \approx 60.0\text{ wt}\%$$
        <p><strong>Final Answer:</strong> Total $\text{SiO}_2$ is approximately $60.0\text{ wt}\%$, representing intermediate-to-felsic crustal composition.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Goldschmidt's Geochemical Affinity Classification</div>
        <p>Classify the characteristic elements of SIAL, SIMA, and NIFE into V.M. Goldschmidt's four geochemical categories: Lithophile, Siderophile, Chalcophile, and Atmophile.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Lithophile (Rock-loving / Silicate phase):</strong> $\text{Si, Al, Mg, Ca, Na, K}$ — Concentrate overwhelmingly in the <strong>SIAL</strong> and <strong>SIMA</strong> layers as silicates and oxides.</li>
          <li><strong>Siderophile (Iron-loving / Metallic phase):</strong> $\text{Fe, Ni, Co, Au, Pt}$ — Partitioned preferentially into the metallic <strong>NIFE</strong> core during planetary core segregation.</li>
          <li><strong>Chalcophile (Sulfur-loving / Sulfide phase):</strong> $\text{Cu, Pb, Zn, S}$ — Form ore deposits and accessory sulfides in crust and mantle.</li>
          <li><strong>Atmophile (Gas-loving):</strong> $\text{N, noble gases}$ — Concentrate in the atmosphere and hydrosphere.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Density Inversion and Floating SIAL</div>
        <p>Applying Archimedes' principle, if a granitic SIAL block of thickness $H = 35\text{ km}$ and density $\rho_{\text{sial}} = 2700\text{ kg/m}^3$ floats in isostatic equilibrium on a denser SIMA substratum ($\rho_{\text{sima}} = 3000\text{ kg/m}^3$), calculate the depth of the submerged root ($r$) below the SIMA surface.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\rho_{\text{sial}} \cdot H = \rho_{\text{sima}} \cdot r$$
        $$r = H \left(\frac{\rho_{\text{sial}}}{\rho_{\text{sima}}}\right) = 35\text{ km} \times \left(\frac{2700}{3000}\right) = 35 \times 0.90 = 31.5\text{ km}$$
        <p>The freeboard elevation above the SIMA is $h = H - r = 35 - 31.5 = 3.5\text{ km}$.</p>
        <p><strong>Final Answer:</strong> The submerged root depth is $31.5\text{ km}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Wegener's Continental Drift Hypothesis and SIAL</div>
        <p>How did Alfred Wegener utilize Suess's SIAL and SIMA concept in his 1912 Continental Drift hypothesis?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Wegener envisioned the continents as rigid, buoyant blocks of <strong>SIAL</strong> that plowed directly through the weaker, yieldable basaltic <strong>SIMA</strong> ocean floor like icebergs through water. While correct in identifying continental displacement, his mechanical concept of SIAL plowing through rigid oceanic SIMA was geophysically flawed; modern plate tectonics proved that oceanic SIMA and continental SIAL are both frozen into rigid lithospheric plates that move together over the asthenosphere.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Conrad Discontinuity Seismic Velocity Jump</div>
        <p>What is the typical seismic compressional velocity ($v_p$) jump across the Conrad Discontinuity between SIAL and SIMA?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Across the Conrad Discontinuity (located at depths of $15-25\text{ km}$ under stable continental cratons), $v_p$ steps up from $\sim 6.0-6.2\text{ km/s}$ in the upper granitic/felsic SIAL to $\sim 6.6-6.9\text{ km/s}$ in the lower amphibolitic-to-granulitic mafic SIMA.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Core Mass Fraction of NIFE</div>
        <p>If Earth's total mass is $M_E = 5.97 \times 10^{24}\text{ kg}$ and the core (NIFE) mass is $M_C = 1.94 \times 10^{24}\text{ kg}$, calculate the mass percentage of the metallic core relative to the whole planet.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\% \text{ Mass}_{\text{Core}} = \left(\frac{1.94 \times 10^{24}}{5.97 \times 10^{24}}\right) \times 100\% = 32.5\%$$
        <p><strong>Final Answer:</strong> The metallic NIFE core comprises approximately $32.5\%$ (nearly one-third) of Earth's total mass.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Mg# (Magnesium Number) of the SIMA Layer</div>
        <p>Define the Magnesium Number ($\text{Mg}\#$) used in mantle petrology and calculate it for a peridotitic mantle SIMA sample with $\text{MgO} = 40.3\text{ wt}\%$ (molar mass $40.3\text{ g/mol}$) and $\text{FeO} = 7.2\text{ wt}\%$ (molar mass $71.85\text{ g/mol}$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\text{Moles of MgO} = \frac{40.3}{40.3} = 1.000\text{ mol}$$
        $$\text{Moles of FeO} = \frac{7.2}{71.85} = 0.1002\text{ mol}$$
        $$\text{Mg}\# = \frac{\text{Mg}^{2+}}{\text{Mg}^{2+} + \text{Fe}^{2+}} \times 100 = \frac{1.000}{1.000 + 0.1002} \times 100 = \frac{1.000}{1.1002} \times 100 \approx 90.9$$
        <p><strong>Final Answer:</strong> $\text{Mg}\# \approx 91$, typical of primitive mantle peridotite.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Whole Earth Elemental Composition vs. Crustal Composition</div>
        <p>Why is Iron ($\text{Fe}$) the most abundant element in the Whole Earth by mass ($\sim 32\%$), whereas Oxygen and Silicon dominate the crust?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>During the early Hadean accretion and magma ocean differentiation of the proto-Earth ($\sim 4.5\text{ Ga}$), planetary melting allowed high-density immiscible liquid iron-nickel metal to sink to the gravitational center (the "iron catastrophe"), forming the massive NIFE core. Lighter silicate melts rose to form the mantle and crust, concentrating oxygen, silicon, and aluminum in the outermost shells.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 43, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q043_SIMA_Silica_Magnesium_Suess_Model_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q043: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q044: Seismic P-Wave Propagation Through Deep Earth (Core Transmission)
# ==============================================================================
def generate_q044():
    title = r"Q044: Seismic P-Wave Transmission Through Outer & Inner Core: Core Phases (PKIKP) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Deep Earth Seismology & Core Mechanics"
    h1_title = "Q044: Seismic P-Wave Transmission Through Deep Earth Core Phases"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 44<br>
<strong>Authoritative References:</strong> Peter M. Shearer, <em>Introduction to Seismology</em> (2nd Ed., Cambridge Univ. Press, Ch. 4: Ray Theory & Core Phases, pp. 88–108); Inge Lehmann, <em>P'</em> (Publications du Bureau Central Séismologique International, 1936); Thorne Lay & Terry C. Wallace, <em>Modern Global Seismology</em> (Ch. 6); C.M.R. Fowler, <em>The Solid Earth</em> (Ch. 4: Deep Earth Interior, pp. 110–126)."""

    part1 = r"""
  <!-- CARD 1: SEISMIC RAY PATHS THROUGH THE CORE -->
  <div class="card">
    <div class="card-header bg-blue">1. Core Phase Nomenclature and Seismic Wave Transmission</div>
    <div class="card-body">
      <p>The internal radial structure of the Earth was unveiled by tracking how seismic body waves penetrate through the deep mantle and core:</p>

      <ul>
        <li><strong>Standard Seismological Notation:</strong>
          <ul>
            <li>$P$: Compressional wave in the mantle.</li>
            <li>$S$: Shear wave in the mantle.</li>
            <li>$K$: Compressional wave propagating through the <strong>liquid outer core</strong> (from German <em>Kern</em>, core).</li>
            <li>$I$: Compressional wave traversing the <strong>solid inner core</strong>.</li>
            <li>$J$: Shear wave traversing the solid inner core ($S$-wave in inner core).</li>
            <li>$c$: Reflection from the core-mantle boundary (CMB, e.g., $PcP, ScS$).</li>
            <li>$i$: Reflection from the inner core boundary (ICB, e.g., $PKiKP$).</li>
          </ul>
        </li>
        <li><strong>Transmission Through Outer Core:</strong> At the Core-Mantle Boundary ($2891\text{ km}$ depth), compressional $P$-waves refract sharply downward into the liquid iron outer core as <strong>$K$-waves</strong> because $P$-wave velocity drops abruptly from $13.7\text{ km/s}$ in the lowermost mantle ($D''$ layer) to $8.1\text{ km/s}$ in the fluid core due to the loss of shear rigidity ($\mu = 0$).</li>
        <li><strong>Transmission Through Inner Core:</strong> At the Inner Core Boundary ($5150\text{ km}$ depth), $P$-waves penetrate directly into the crystalline solid iron-nickel inner core as <strong>$I$-waves</strong>, where velocity jumps up to $\sim 11.0\text{ km/s}$.</li>
        <li><strong>The PKIKP Phase:</strong> A compressional wave traveling from the crust through the mantle ($P$), refracting into the outer core ($K$), traversing the solid inner core ($I$), emerging through the opposite outer core ($K$), and ascending through the mantle ($P$) to the antipodal surface is designated as <strong>$PKIKP$</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q44/seismic_p_s_core_shadow_zones.png" alt="Seismic P and S Core Shadow Zones">
        <div class="tb-caption">
          <strong>Figure 44.1:</strong> Global seismic ray tracing illustrating the $P$-wave shadow zone ($103^\circ-143^\circ$) and the complete transmission of compressional waves through the liquid outer core ($PKP$) and solid inner core ($PKIKP$).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE DISCOVERY BY INGE LEHMANN -->
  <div class="card">
    <div class="card-header bg-indigo">2. Inge Lehmann's Discovery of the Solid Inner Core (1936)</div>
    <div class="card-body">
      <p>Before 1936, the core was believed to be entirely a uniform liquid cavity producing a complete shadow zone between epicentral angles $\Delta = 103^\circ$ and $143^\circ$:</p>

      <div class="formula-card">
        <div class="formula-title">Snell's Law at the Core-Mantle Boundary (CMB)</div>
        $$p = \frac{r \sin i}{v(r)} = \text{constant}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Because $v_p$ drops from $13.7\text{ km/s}$ to $8.1\text{ km/s}$ at the CMB, the ray bends towards the normal ($\sin i_K = \frac{v_K}{v_P}\sin i_P$), focusing rays toward angles $\ge 143^\circ$ and creating the classic $P$-wave shadow zone between $103^\circ$ and $143^\circ$.</p>
      </div>

      <ul>
        <li><strong>The Faint Arrivals:</strong> Danish seismologist <strong>Inge Lehmann</strong> analyzed sensitive seismograms in Europe from earthquakes in New Zealand and discovered faint, early $P$-wave arrivals within the shadow zone ($\Delta \approx 110^\circ-135^\circ$).</li>
        <li><strong>The Explanation:</strong> Lehmann demonstrated that these arrivals were not diffraction artifacts, but compressional waves that had refracted through a higher-velocity <strong>solid inner core</strong> ($PKIKP$) or reflected off its boundary ($PKiKP$).</li>
        <li><strong>The Invariant Fact:</strong> Therefore, <strong>the P wave is transmitted through the outer as well as the inner core</strong>!</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q44/winter_fig2_earth_subdivisions_depths.png" alt="Earth Subdivisions and Depths from Winter">
        <div class="tb-caption">
          <strong>Figure 44.2 (Winter, Fig. 2):</strong> Depths and physical properties of internal Earth subdivisions: Mantle, Liquid Outer Core, and Solid Inner Core.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARATIVE BEHAVIOUR OF P AND S WAVES IN CORE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Comprehensive Comparison: P-Waves vs. S-Waves in Earth's Core</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Wave Phase</th>
            <th>Outer Core Behaviour ($2891-5150\text{ km}$)</th>
            <th>Inner Core Behaviour ($5150-6371\text{ km}$)</th>
            <th>Surface Shadow Zone</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>P-Wave (Compressional)</strong></td>
            <td><strong>Transmitted</strong> as $K$-wave ($v_p = 8.1 \to 10.3\text{ km/s}$). Strongly refracted.</td>
            <td><strong>Transmitted</strong> as $I$-wave ($v_p \approx 11.0\text{ km/s}$). Refracts through center.</td>
            <td>Partial shadow zone ($103^\circ-143^\circ$) containing weak $PKIKP$ and $PKiKP$ arrivals.</td>
          </tr>
          <tr>
            <td><strong>S-Wave (Shear)</strong></td>
            <td><strong>Completely Blocked</strong> ($v_s = 0$ because shear modulus $\mu = 0$ in liquid).</td>
            <td>Can propagate theoretically as $J$-wave converted from $P$ ($PKJKP$, exceedingly faint).</td>
            <td><strong>Massive permanent shadow zone</strong> extending from $103^\circ$ across the entire antipode to $180^\circ$!</td>
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
        <div class="q-num">Question 44</div>
        <div class="q-text">Which statement is true about P wave ?</div>
        <div class="q-options">
          <div class="opt-node">(A) The P wave reflected from the mantle-core boundary.</div>
          <div class="opt-node">(B) The P wave is transmitted through the outer core but reflected from the inner core.</div>
          <div class="opt-node correct">(C) The P wave is transmitted through the outer as well as the inner core.</div>
          <div class="opt-node">(D) The P wave is reflected from the crust-mantle boundary.</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) The P wave is transmitted through the outer as well as the inner core.</strong> [As compressional longitudinal waves capable of passing through both fluids and solids, P-waves refract into the liquid outer core (as K-waves) and penetrate the solid inner core (as I-waves: PKIKP).]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) The P wave is transmitted through the outer as well as the inner core.</div>
    <div class="card-body">
      <p><strong>Detailed Seismological Forensic Analysis:</strong></p>
      <ul>
        <li>Primary ($P$) waves are longitudinal compressional waves. Their velocity is governed by $v_p = \sqrt{(K + \frac{4}{3}\mu)/\rho}$. Because the bulk modulus of incompressibility $K > 0$ for all physical states of matter, $P$-waves possess the unique physical capability to <strong>propagate through both fluids and solids</strong>.</li>
        <li>When a $P$-wave reaches the Core-Mantle Boundary (CMB, $2891\text{ km}$ depth), it refracts into the fluid outer core as a compressional wave ($K$).</li>
        <li>Upon reaching the Inner Core Boundary (ICB, $5150\text{ km}$ depth), it is <strong>transmitted directly through the solid iron-nickel inner core</strong> as a compressional wave ($I$), giving rise to the well-documented global seismic phase <strong>$PKIKP$</strong>.</li>
        <li>Hence, statement <strong>(C)</strong> is completely and indisputably true.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) The P wave is transmitted through the outer core but reflected from the inner core.</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While a minor fraction of $P$-wave energy reflects off the inner core boundary (producing the faint $PKiKP$ phase), the vast majority of seismic energy is <strong>refracted and transmitted directly through the solid inner core</strong> as $I$-waves ($PKIKP$).</li>
        <li>Claiming that $P$-waves are merely reflected from the inner core denies the existence of the inner core transmission phases that established its solid physical state. Thus, (B) is false.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) The P wave reflected from the mantle-core boundary.</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Although reflection at the CMB does occur (producing the $PcP$ phase), the defining characteristic of $P$-waves is that they are <strong>transmitted and refracted into the core</strong> as $PKP$ waves.</li>
        <li>Saying "The P wave reflected from the mantle-core boundary" implies that $P$-waves do not penetrate the core, which contradicts the fundamental discovery of the liquid outer core by R.D. Oldham in 1906. Hence, (A) is inaccurate.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) The P wave is reflected from the crust-mantle boundary.</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>At the Mohorovičić discontinuity (Moho), incident $P$-waves are primarily <strong>refracted</strong> into the upper mantle ($Pn$ phase), with only a fraction undergoing post-critical reflection ($PmP$).</li>
        <li>Describing the $P$-wave globally as merely "reflected from the crust-mantle boundary" is entirely misleading and trivial compared to its planetary core transmission properties.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Core Seismic Phases Nomenclature</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Seismic Phase Code</th>
            <th>Ray Path Trajectory Through Earth</th>
            <th>Observed Epicentral Distance ($\Delta$)</th>
            <th>Significance in Discovering Core Structure</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$PcP$</strong></td>
            <td>$P$-wave in mantle reflected upward at the Core-Mantle Boundary (CMB).</td>
            <td>$0^\circ$ to $90^\circ$</td>
            <td>Constrained the precise depth of the liquid core boundary ($2891\text{ km}$, Gutenberg 1914).</td>
          </tr>
          <tr>
            <td><strong>$PKP$ ($P'$)</strong></td>
            <td>Refracted into liquid outer core ($K$), misses inner core, emerges in mantle ($P$).</td>
            <td>$>143^\circ$ (and caustic branch back to $142^\circ$)</td>
            <td>Confirmed the fluid nature of the outer core (R.D. Oldham 1906).</td>
          </tr>
          <tr>
            <td><strong>$PKIKP$</strong></td>
            <td>Mantle ($P$) $\to$ Outer Core ($K$) $\to$ <strong>Inner Core ($I$)</strong> $\to$ Outer Core ($K$) $\to$ Mantle ($P$).</td>
            <td>$110^\circ$ to $180^\circ$</td>
            <td><strong>Discovered the solid inner core (Inge Lehmann 1936).</strong></td>
          </tr>
          <tr>
            <td><strong>$PKiKP$</strong></td>
            <td>Mantle ($P$) $\to$ Outer Core ($K$) $\to$ reflected off Inner Core Boundary ($i$).</td>
            <td>$100^\circ$ to $140^\circ$</td>
            <td>Pinpointed the exact depth of the Inner Core Boundary ($5150\text{ km}$).</td>
          </tr>
          <tr>
            <td><strong>$PKJKP$</strong></td>
            <td>Compressional wave converting to shear wave ($J$) in solid inner core.</td>
            <td>Variable ($>120^\circ$)</td>
            <td>Ultimate seismic proof of the non-zero shear modulus ($\mu > 0$) of the solid inner core.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Deep Earth Ray Tracing & Core Geophysics</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Critical Angle of Incidence at the Core-Mantle Boundary</div>
        <p>A $P$-wave in the lowermost mantle ($v_1 = 13.7\text{ km/s}$) strikes the liquid outer core ($v_2 = 8.1\text{ km/s}$). Does total internal reflection occur? Calculate the angle of refraction $r$ for an angle of incidence $i = 45^\circ$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Total internal reflection can only occur when a wave travels from a lower-velocity to a higher-velocity medium ($v_1 < v_2$). Here $v_1 > v_2$ ($13.7 > 8.1\text{ km/s}$); therefore, total internal reflection is physically impossible, and energy is always transmitted!</p>
        <p>Applying Snell's law:</p>
        $$\frac{\sin i}{v_1} = \frac{\sin r}{v_2} \implies \sin r = \left(\frac{v_2}{v_1}\right)\sin i$$
        $$\sin r = \left(\frac{8.1}{13.7}\right)\sin 45^\circ = 0.5912 \times 0.7071 \approx 0.4180$$
        $$r = \arcsin(0.4180) \approx 24.71^\circ$$
        <p><strong>Final Answer:</strong> The refracted ray bends steeply toward the normal at an angle $r \approx 24.7^\circ$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Travel Time Calculation for an Antipodal $PKIKP$ Ray</div>
        <p>Calculate the vertical diametric travel time for a $PKIKP$ ray traversing the Earth from the North Pole to the South Pole ($\Delta = 180^\circ$). Assume two mantle sections (thickness $2891\text{ km}$ each, average $v_p = 10.5\text{ km/s}$), two outer core sections (thickness $2259\text{ km}$ each, average $v_p = 9.2\text{ km/s}$), and the inner core diameter ($2442\text{ km}$, average $v_p = 11.2\text{ km/s}$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$t_{\text{mantle}} = 2 \times \frac{2891\text{ km}}{10.5\text{ km/s}} = 2 \times 275.33\text{ s} = 550.67\text{ s}$$
        $$t_{\text{outer core}} = 2 \times \frac{2259\text{ km}}{9.2\text{ km/s}} = 2 \times 245.54\text{ s} = 491.09\text{ s}$$
        $$t_{\text{inner core}} = \frac{2442\text{ km}}{11.2\text{ km/s}} \approx 218.04\text{ s}$$
        $$t_{\text{total}} = 550.67 + 491.09 + 218.04 = 1259.8\text{ seconds} \approx 21\text{ minutes } 0\text{ seconds}$$
        <p><strong>Final Answer:</strong> Total antipodal diametric travel time is approximately $1260\text{ seconds}$ ($21\text{ minutes}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: The P-Wave Shadow Zone Angle Limits</div>
        <p>State the exact angular limits of the primary $P$-wave shadow zone on the surface of the Earth and explain its cause.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The $P$-wave shadow zone extends from epicentral distance $\Delta = 103^\circ$ to $\Delta = 143^\circ$ (or $\sim 104^\circ-140^\circ$). It is caused by the dramatic velocity reduction at the core-mantle boundary ($13.7 \to 8.1\text{ km/s}$), which refracts rays entering the core deeply downward, leaving a shadow zone between rays that graze the mantle-core boundary ($\sim 103^\circ$) and the first refracted rays exiting the core ($\sim 143^\circ$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Solid Inner Core Shear Wave Velocity ($v_s$)</div>
        <p>Seismic observations indicate that in the solid inner core, $v_p \approx 11.2\text{ km/s}$ and Poisson's ratio is extraordinarily high ($\nu \approx 0.44$). Estimate the inner core shear wave velocity $v_s$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\frac{v_p}{v_s} = \sqrt{\frac{2(1 - \nu)}{1 - 2\nu}} = \sqrt{\frac{2(1 - 0.44)}{1 - 2(0.44)}} = \sqrt{\frac{2(0.56)}{1 - 0.88}} = \sqrt{\frac{1.12}{0.12}} = \sqrt{9.333} \approx 3.055$$
        $$v_s = \frac{v_p}{3.055} = \frac{11.2\text{ km/s}}{3.055} \approx 3.67\text{ km/s}$$
        <p><strong>Final Answer:</strong> Inner core shear wave velocity is approximately $3.67\text{ km/s}$ (showing high ductility near its melting point).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Geodynamo Convection in the Outer Core</div>
        <p>Why must the outer core be a fluid rather than a solid to generate Earth's magnetic field?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Earth's dipolar magnetic field is maintained by the <strong>geodynamo mechanism</strong>. This requires vigorous, organized fluid convection of an electrically conducting liquid (molten iron-nickel alloy). Thermal convection driven by core cooling combined with compositional convection (light element expulsion during inner core crystallization) is organized into helical convective columns by the Coriolis force. A rigid solid cannot sustain convective fluid flow; thus, a fluid outer core is an absolute prerequisite.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Seismic Anisotropy of the Inner Core</div>
        <p>What observation demonstrates that the Earth's solid inner core is seismically anisotropic?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>$PKIKP$ seismic waves traveling nearly parallel to the Earth's rotational axis (polar paths) travel approximately $3-4\%$ faster than $PKIKP$ waves traveling in the equatorial plane. This demonstrates cylindrical seismic anisotropy, caused by the preferred crystalline alignment (lattice preferred orientation, LPO) of hexagonal close-packed (hcp) iron crystals aligned with Earth's spin axis.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Reflection Coefficient at the Core-Mantle Boundary</div>
        <p>For normal incidence, the acoustic reflection coefficient is $R = \frac{\rho_2 v_2 - \rho_1 v_1}{\rho_2 v_2 + \rho_1 v_1}$. Calculate $R$ at the CMB given mantle parameters ($\rho_1 = 5560\text{ kg/m}^3, v_1 = 13.7\text{ km/s}$) and core parameters ($\rho_2 = 9900\text{ kg/m}^3, v_2 = 8.1\text{ km/s}$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$Z_1 = \rho_1 v_1 = 5560 \times 13700 = 7.617 \times 10^7\text{ kg/(m}^2\cdot\text{s)}$$
        $$Z_2 = \rho_2 v_2 = 9900 \times 8100 = 8.019 \times 10^7\text{ kg/(m}^2\cdot\text{s)}$$
        $$R = \frac{8.019 - 7.617}{8.019 + 7.617} = \frac{0.402}{15.636} \approx +0.0257$$
        <p><strong>Final Answer:</strong> The reflection coefficient is tiny ($R \approx +0.026$); over $97\%$ of normal-incident $P$-wave energy is transmitted across the CMB into the core!</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Super-Rotation of the Inner Core</div>
        <p>What is the seismological evidence for the "super-rotation" of the inner core?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>By comparing the arrival waveforms of doublet earthquakes (earthquakes occurring decades apart on the same fault rupture) recorded at the same seismic stations, seismologists observed small progressive shifts in travel times of $PKIKP$ waves sampling the anisotropic inner core. This indicated that the inner core rotates slightly faster than the overlying mantle and crust (by $\sim 0.2-1.0^\circ$ per year), driven by electromagnetic torques from the geodynamo.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 44, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q044_P_Wave_Transmission_Outer_Inner_Core_PKIKP_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q044: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q045: Principles of Isostatic Equilibrium
# ==============================================================================
def generate_q045():
    title = r"Q045: Principles of Isostatic Equilibrium: Buoyancy vs. Gravity Hydrostatic Balance | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Geophysics, Geodesy & Isostasy"
    h1_title = "Q045: Principles of Isostatic Equilibrium: Buoyancy vs. Gravity Balance"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 45<br>
<strong>Authoritative References:</strong> Anthony B. Watts, <em>Isostasy and Flexure of the Lithosphere</em> (Cambridge Univ. Press, 2001, Ch. 1–3); Donald L. Turcotte & Gerald Schubert, <em>Geodynamics</em> (Ch. 5: Gravitation, pp. 200–225); William Lowrie, <em>Fundamentals of Geophysics</em> (Ch. 2: Gravity, pp. 88–108); C.M.R. Fowler, <em>The Solid Earth</em> (Ch. 5: Gravity and Isostasy); K.M. Bangar, <em>Principles of Engineering Geology</em> (Ch. 1, pp. 6–9, Fig. 1.6 & 1.7)."""

    part1 = r"""
  <!-- CARD 1: THE PHYSICAL PRINCIPLE OF ISOSTASY -->
  <div class="card">
    <div class="card-header bg-blue">1. The Principle of Isostatic Equilibrium: Archimedean Balance</div>
    <div class="card-body">
      <p>The term <strong>isostasy</strong> (from Greek <em>isostasios</em>, meaning "equal standing" or "in equipoise") was introduced into geology by American geologist <strong>Clarence Dutton</strong> in 1889 to describe the state of gravitational hydrostatic balance between the Earth's lithospheric crust and the underlying asthenospheric mantle:</p>

      <ul>
        <li><strong>Physical Definition:</strong> Isostatic equilibrium is the mechanical condition wherein the <strong>upward buoyancy force</strong> exerted by the fluid-like asthenosphere exactly balances the <strong>downward gravitational force</strong> (weight) exerted by the overlying lithospheric column:
          $$\sum F_z = 0 \iff F_{\text{buoyancy}} = F_{\text{gravity}}$$
        </li>
        <li><strong>Archimedes' Hydrostatic Principle:</strong> Just as an iceberg or wooden block floats in water with a submerged volume proportional to its mass, columns of continental and oceanic lithosphere float upon the denser, ductile asthenosphere.</li>
        <li><strong>Depth of Compensation ($D_c$):</strong> The horizontal datum horizon within the upper mantle below which the total lithostatic pressure exerted by any overlying vertical column of unit cross-sectional area is identical everywhere across the globe:
          $$P(D_c) = \int_0^{D_c} \rho(z) g \, dz = \text{constant}$$
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q45/isostasy_airy_pratt_mechanisms.png" alt="Airy and Pratt Isostasy Mechanisms">
        <div class="tb-caption">
          <strong>Figure 45.1:</strong> Mechanical representation of isostatic compensation mechanisms: George Airy's crustal root hypothesis (variable thickness, uniform density) versus John Pratt's density variation hypothesis (uniform depth, variable density).
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: AIRY VS PRATT FORMULATIONS -->
  <div class="card">
    <div class="card-header bg-indigo">2. Classical Models: Airy-Heiskanen vs. Pratt-Hayford</div>
    <div class="card-body">
      <p>The two foundational classical formulations of isostatic equilibrium resolve how the hydrostatic balance is maintained:</p>

      <div class="formula-card">
        <div class="formula-title">1. Airy-Heiskanen Isostasy (Variable Thickness, Constant Density)</div>
        <p>Assumes the crust has a uniform constant density ($\rho_c$) floating in a denser mantle ($\rho_m$). High topographic mountains ($h$) are compensated by deep crustal roots ($r$):</p>
        $$r = h \left(\frac{\rho_c}{\rho_m - \rho_c}\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">For $\rho_c = 2700\text{ kg/m}^3$ and $\rho_m = 3300\text{ kg/m}^3$, the root ratio is $r/h = 2700 / (3300 - 2700) = 2700 / 600 = 4.5$. Every $1\text{ km}$ of mountain elevation requires a $4.5\text{ km}$ deep crustal root!</p>
      </div>

      <div class="formula-card">
        <div class="formula-title">2. Pratt-Hayford Isostasy (Uniform Depth, Variable Density)</div>
        <p>Assumes compensation occurs at a uniform horizontal depth ($D$). Higher topography consists of lighter, lower-density rock columns:</p>
        $$\rho(h) \cdot (D + h) = \rho_0 \cdot D \implies \rho(h) = \rho_0 \left(\frac{D}{D + h}\right)$$
      </div>

      <div class="tb-figure">
        <img src="../../figures_Q45/bangar_fig1_7_airy_isostasy.png" alt="Airy Isostasy from Bangar">
        <div class="tb-caption">
          <strong>Figure 45.2 (K.M. Bangar, Fig. 1.7):</strong> George Airy's concept of isostatic equilibrium showing mountains floating with deep submerged roots like icebergs in water.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: GRAVITY ANOMALIES AND ISOSTATIC ADJUSTMENT -->
  <div class="card">
    <div class="card-header bg-emerald">3. Isostatic Gravity Anomalies and Geodynamic Rebound</div>
    <div class="card-body">
      <p>Deviations from perfect isostatic equilibrium generate <strong>isostatic gravity anomalies</strong> that drive vertical crustal motion:</p>

      <table class="comparison-table">
        <thead>
          <tr>
            <th>Isostatic State</th>
            <th>Force Imbalance</th>
            <th>Isostatic Gravity Anomaly ($\Delta g_{\text{iso}}$)</th>
            <th>Dynamic Geodynamic Response</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Equilibrium (Compensated)</strong></td>
            <td>$F_{\text{buoyancy}} = F_{\text{gravity}}$</td>
            <td>$\Delta g_{\text{iso}} \approx 0\text{ mGal}$</td>
            <td>Stable stationary crust.</td>
          </tr>
          <tr>
            <td><strong>Under-compensated (Excess Mass)</strong></td>
            <td>$F_{\text{gravity}} > F_{\text{buoyancy}}$</td>
            <td>$\mathbf{\Delta g_{\text{iso}} > 0}$ (Positive Anomaly)</td>
            <td>Crust must <strong>subside</strong> to restore balance (e.g., volcanic seamounts, deltas).</td>
          </tr>
          <tr>
            <td><strong>Over-compensated (Mass Deficit)</strong></td>
            <td>$F_{\text{buoyancy}} > F_{\text{gravity}}$</td>
            <td>$\mathbf{\Delta g_{\text{iso}} < 0}$ (Negative Anomaly)</td>
            <td>Crust experiences <strong>post-glacial rebound / uplift</strong> (e.g., Baltic Shield, Hudson Bay).</td>
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
        <div class="q-num">Question 45</div>
        <div class="q-text">Isostatic equilibrium is :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) A buoyancy force pushing the lithosphere up equals the gravitational force pushing it down.</div>
          <div class="opt-node">(B) A buoyancy force pushing the lithosphere up is less than the gravitational force pushing it down.</div>
          <div class="opt-node">(C) A buoyancy force pushing the lithosphere up is greater than the gravitational force pushing it down.</div>
          <div class="opt-node">(D) All the features of Earth's surface are at the same elevation</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) A buoyancy force pushing the lithosphere up equals the gravitational force pushing it down.</strong> [By fundamental definition of hydrostatic equilibrium, isostasy is the state where upward asthenospheric buoyancy exactly balances downward gravitational lithospheric weight.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) A buoyancy force pushing the lithosphere up equals the gravitational force pushing it down.</div>
    <div class="card-body">
      <p><strong>Detailed Geophysical Forensic Analysis:</strong></p>
      <ul>
        <li>The term <strong>isostasy</strong> describes the principle of hydrostatic equilibrium applied to the Earth's crust and mantle on a regional scale.</li>
        <li>According to Archimedes' principle, a floating body is in mechanical equilibrium if and only if the upward buoyant force exerted by the displaced fluid medium is exactly equal in magnitude to the downward gravitational force (weight) acting on the body:
          $$\sum F_z = F_{\text{buoyancy}} - F_{\text{gravity}} = 0 \implies F_{\text{buoyancy}} = F_{\text{gravity}}$$
        </li>
        <li>In geodynamics, the relatively rigid lithosphere floats atop the denser, ductile asthenospheric mantle. When in isostatic equilibrium, the upward buoyancy force supporting each lithospheric column precisely equals the downward gravitational force pulling it toward the center of the Earth.</li>
        <li>Therefore, statement <strong>(A)</strong> is the exact physical definition of isostatic equilibrium.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) A buoyancy force pushing the lithosphere up is less than the gravitational force pushing it down.</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>If the buoyancy force were strictly less than the gravitational force ($F_{\text{buoyancy}} < F_{\text{gravity}}$), there would be a net downward uncompensated force.</li>
        <li>This describes an <em>under-compensated</em> state characterized by a positive isostatic gravity anomaly, where the crust is forced to subside dynamically until equilibrium is restored. It does not represent equilibrium.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) A buoyancy force pushing the lithosphere up is greater than the gravitational force pushing it down.</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>If the buoyancy force were greater than gravity ($F_{\text{buoyancy}} > F_{\text{gravity}}$), there would be a net upward restoring force.</li>
        <li>This represents an <em>over-compensated</em> condition (such as deglaciated terrain in Scandinavia), which causes rapid vertical uplift (post-glacial rebound). This is a non-equilibrium transient state.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) All the features of Earth's surface are at the same elevation</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Isostasy does <em>not</em> imply that the Earth's surface is flat or at uniform elevation.</li>
        <li>On the contrary, isostasy explains why different geological features (high mountain belts, continental plateaus, oceanic basins) maintain vastly different elevations in a state of stable gravitational balance due to differences in crustal thickness (Airy) or crustal density (Pratt).</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Theories of Isostatic Compensation</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Model Parameter</th>
            <th>Airy-Heiskanen Model</th>
            <th>Pratt-Hayford Model</th>
            <th>Vening Meinesz (Flexural) Model</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Crustal Density ($\rho_c$)</strong></td>
            <td>Constant everywhere ($\sim 2.70-2.80\text{ g/cm}^3$).</td>
            <td><strong>Variable</strong>: $\rho \propto \frac{1}{D + h}$ (lighter under mountains).</td>
            <td>Constant crustal and mantle densities.</td>
          </tr>
          <tr>
            <td><strong>Depth of Compensation ($D_c$)</strong></td>
            <td><strong>Variable</strong>: Deepest under mountains (deep roots), shallow under oceans.</td>
            <td><strong>Uniform constant depth</strong> ($D \approx 100-113\text{ km}$).</td>
            <td>Distributed regionally across flexural wavelength.</td>
          </tr>
          <tr>
            <td><strong>Mechanical Coupling</strong></td>
            <td>Independent vertical floating columns (zero shear strength between columns).</td>
            <td>Independent vertical floating columns (zero lateral shear strength).</td>
            <td><strong>Elastic plate flexure</strong> (regional compensation via flexural rigidity $D_f$).</td>
          </tr>
          <tr>
            <td><strong>Real Earth Validity</strong></td>
            <td>Excellent match for continental collision belts (Himalayan crustal root $\sim 70\text{ km}$).</td>
            <td>Good match for mid-ocean ridges (thermal expansion) and volcanic island chains.</td>
            <td>The most accurate physical model for real lithospheric plate behaviour.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Isostasy & Gravimetric Geodesy</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Himalayan Crustal Root Calculation (Airy Model)</div>
        <p>The Tibetan Plateau has an average surface elevation $h = 5.0\text{ km}$. Assuming normal continental crust has thickness $T_0 = 35\text{ km}$, crustal density $\rho_c = 2750\text{ kg/m}^3$, and upper mantle density $\rho_m = 3300\text{ kg/m}^3$, calculate the root depth ($r$) and total crustal thickness ($T_{\text{total}}$) under Tibet.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Applying Airy isostatic root equilibrium:</p>
        $$r = h \left(\frac{\rho_c}{\rho_m - \rho_c}\right) = 5.0\text{ km} \times \left(\frac{2750}{3300 - 2750}\right) = 5.0 \times \left(\frac{2750}{550}\right) = 5.0 \times 5.0 = 25.0\text{ km}$$
        <p>Total crustal thickness is the sum of surface elevation, normal crustal thickness, and root depth:</p>
        $$T_{\text{total}} = h + T_0 + r = 5.0\text{ km} + 35.0\text{ km} + 25.0\text{ km} = 65.0\text{ km}$$
        <p><strong>Final Answer:</strong> The root extends $25\text{ km}$ below the normal Moho, giving a total crustal thickness of $65\text{ km}$ (in close agreement with seismic receiver function measurements under Tibet).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Oceanic Basin Depth Calculation (Airy Model)</div>
        <p>An oceanic basin has water depth $d_w = 4.0\text{ km}$ ($\rho_w = 1030\text{ kg/m}^3$) and basaltic crust thickness $T_{\text{ocean}} = 7.0\text{ km}$ ($\rho_c = 2900\text{ kg/m}^3$). If normal continental crust has $T_0 = 35\text{ km}$ ($\rho_{\text{cont}} = 2750\text{ kg/m}^3$) at sea level, calculate the mantle anti-root (mantle upwelling height $m$) supporting the ocean basin ($\rho_m = 3300\text{ kg/m}^3$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Equating pressure at depth of compensation $D_c = 35\text{ km}$:</p>
        $$\rho_{\text{cont}} g T_0 = \rho_w g d_w + \rho_c g T_{\text{ocean}} + \rho_m g m$$
        $$2750 \times 35 = (1030 \times 4.0) + (2900 \times 7.0) + 3300 m$$
        $$96,250 = 4,120 + 20,300 + 3300 m = 24,420 + 3300 m$$
        $$3300 m = 96,250 - 24,420 = 71,830$$
        $$m = \frac{71,830}{3300} \approx 21.77\text{ km}$$
        <p><strong>Final Answer:</strong> The mantle rises by $21.8\text{ km}$ beneath the ocean basin to maintain isostatic balance.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Pratt Density Variation Calculation</div>
        <p>In a Pratt model with compensation depth $D = 100\text{ km}$, standard crust at sea level has density $\rho_0 = 2800\text{ kg/m}^3$. What must be the density $\rho_m$ of a mountain plateau rising $h = 4.0\text{ km}$ above sea level?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$\rho_m \cdot (D + h) = \rho_0 \cdot D$$
        $$\rho_m = \rho_0 \left(\frac{D}{D + h}\right) = 2800 \times \left(\frac{100}{100 + 4.0}\right) = 2800 \times \left(\frac{100}{104}\right) \approx 2692.3\text{ kg/m}^3$$
        <p><strong>Final Answer:</strong> The mountain column density is $2692\text{ kg/m}^3$ (a density reduction of $\approx 108\text{ kg/m}^3$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Bouguer vs. Free-Air Anomaly over Compensated Mountains</div>
        <p>What are the typical Free-Air and Bouguer gravity anomalies observed over a high mountain range that is in perfect Airy isostatic equilibrium?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Free-Air Anomaly ($\Delta g_{FA}$):</strong> Close to zero ($\Delta g_{FA} \approx 0\text{ mGal}$), because at long wavelengths the extra mass of the mountain above sea level is completely balanced by the mass deficit of the low-density root at depth.</li>
          <li><strong>Bouguer Anomaly ($\Delta g_B$):</strong> Strongly <strong>negative</strong> (typically $-200$ to $-450\text{ mGal}$), because the Bouguer correction mathematically removes the attraction of the mountain mass without removing the deep low-density root, leaving only the large negative gravitational pull of the crustal root.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Post-Glacial Rebound Uplift Remaining</div>
        <p>A region previously covered by an ice sheet of thickness $H_{\text{ice}} = 2.0\text{ km}$ ($\rho_{\text{ice}} = 920\text{ kg/m}^3$) has experienced $400\text{ m}$ of post-glacial uplift since deglaciation. If mantle density is $\rho_m = 3300\text{ kg/m}^3$, how much further vertical uplift is required to achieve complete isostatic equilibrium?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Total equilibrium isostatic depression caused by the ice sheet:</p>
        $$w_{\text{eq}} = H_{\text{ice}} \left(\frac{\rho_{\text{ice}}}{\rho_m}\right) = 2000\text{ m} \times \left(\frac{920}{3300}\right) = 2000 \times 0.2788 \approx 557.6\text{ m}$$
        <p>Uplift already completed: $400\text{ m}$.</p>
        $$\text{Remaining Uplift} = 557.6\text{ m} - 400.0\text{ m} = 157.6\text{ m}$$
        <p><strong>Final Answer:</strong> An additional $158\text{ m}$ of vertical crustal uplift must occur before equilibrium is reached.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Flexural Rigidity ($D_f$) and Effective Elastic Thickness ($T_e$)</div>
        <p>Calculate the flexural rigidity $D_f$ of a lithospheric plate with effective elastic thickness $T_e = 30\text{ km}$, Young's modulus $E = 1.0 \times 10^{11}\text{ Pa}$, and Poisson's ratio $\nu = 0.25$.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        $$D_f = \frac{E T_e^3}{12(1 - \nu^2)}$$
        $$T_e = 30\text{ km} = 3.0 \times 10^4\text{ m} \implies T_e^3 = 2.7 \times 10^{13}\text{ m}^3$$
        $$1 - \nu^2 = 1 - (0.25)^2 = 1 - 0.0625 = 0.9375$$
        $$12(1 - \nu^2) = 12 \times 0.9375 = 11.25$$
        $$D_f = \frac{1.0 \times 10^{11} \times 2.7 \times 10^{13}}{11.25} = \frac{2.7 \times 10^{24}}{11.25} = 2.4 \times 10^{23}\text{ N}\cdot\text{m}$$
        <p><strong>Final Answer:</strong> The flexural rigidity is $2.4 \times 10^{23}\text{ N}\cdot\text{m}$.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Historical Geodesy: Sir George Everest & the Plumb Line Deflection</div>
        <p>What historic geodetic anomaly during the Great Trigonometrical Survey of India led to the formulation of isostasy?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Between 1840 and 1850, Sir George Everest measured the distance between Kalianpur and Kaliana by triangulation and astronomical plumb-line latitude determinations. Archdeacon John Henry Pratt calculated the theoretical gravitational attraction of the massive Himalayan mountain range and discovered that the observed deflection of the plumb line was <strong>less than one-third of the predicted gravitational pull</strong> ($5.236''$ observed vs. $15.885''$ calculated). This proved that the mountains must have low-density roots beneath them offsetting their mass.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Isostatic Response to Fluvial Denudation</div>
        <p>If a mountain range is eroded by a thickness $\Delta h = 1000\text{ m}$ of rock ($\rho_c = 2700\text{ kg/m}^3$), by how much will isostatic rebound uplift the mountain crest ($\rho_m = 3300\text{ kg/m}^3$), and what is the net reduction in summit elevation?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Isostatic rebound uplift is given by:</p>
        $$U = \Delta h \left(\frac{\rho_c}{\rho_m}\right) = 1000\text{ m} \times \left(\frac{2700}{3300}\right) = 1000 \times 0.8182 \approx 818.2\text{ m}$$
        <p>Net loss in surface summit elevation is:</p>
        $$\Delta h_{\text{net}} = \Delta h - U = 1000\text{ m} - 818.2\text{ m} = 181.8\text{ m}$$
        <p><strong>Final Answer:</strong> Isostatic rebound lifts the mountain by $818.2\text{ m}$; hence, removing $1000\text{ m}$ of rock lowers the mountain summits by only $182\text{ m}$!</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 45, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q045_Isostatic_Equilibrium_Buoyancy_Gravity_Balance_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q045: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q041()
    generate_q041_extra = False
    generate_q042()
    generate_q043()
    generate_q044()
    generate_q045()
