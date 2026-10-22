#!/usr/bin/env python3
"""
Q081 Generator: Antiperthite Feldspar Exsolution & Subsolidus Phase Relations
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q081():
    title = r"Q081: Mineralogy & Petrology: Antiperthite Feldspar Exsolution & Solvus Phase Equilibria | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Mineralogy & Feldspar Phase Equilibria"
    h1_title = "Q081: Antiperthite Texture: Subsolidus Feldspar Exsolution"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 81<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 6: Feldspar Phase Equilibria, pp. 91–98, Fig. 6-16); Anthony Hall, <em>Igneous Petrology</em>; G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 119–120); Deer, Howie & Zussman, <em>An Introduction to the Rock-Forming Minerals</em> (3rd Ed., Mineralogical Society, pp. 385–412)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROGRAPHIC ANATOMY OF ANTIPERTHITE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Microstructure & Crystallographic Architecture of Antiperthite</div>
    <div class="card-body">
      <p>
        The term <strong>antiperthite</strong> describes an intimate subsolidus intergrowth texture in which a host crystal of <strong>plagioclase feldspar</strong> (typically oligoclase, andesine, or albite) contains oriented, bleb-like, rod-like, rectangular, or irregular inclusions of <strong>potassium feldspar (orthoclase or microcline)</strong>.
      </p>
      <p>
        It is the exact crystallographic and structural mirror-image of <strong>perthite</strong>:
      </p>
      <div class="formula-box">
        <strong>The Fundamental Perthite–Antiperthite Distinction:</strong><br>
        $$\mathbf{\text{Perthite}} = \mathbf{\text{Potassium Feldspar Host}} \quad \text{containing exsolved blebs/lamellae of } \mathbf{\text{Plagioclase (Albite)}}$$<br>
        $$\mathbf{\text{Antiperthite}} = \mathbf{\text{Plagioclase Host}} \quad \text{containing exsolved blebs/inclusions of } \mathbf{\text{Potassium Feldspar (Kfs)}}$$<br>
        $$\mathbf{\text{Mesoperthite}} = \text{Roughly equal proportions } (\sim 50:50) \text{ of mutually intergrown K-feldspar and Plagioclase}$$
      </div>

      <div class="figure-box">
        <img src="../../figures_Q81/winter_fig16_feldspar_solvus_perthite.png" alt="Feldspar Solvus and Exsolution Mechanisms from Winter">
        <div class="figure-caption">
          <strong>Figure 81.1 — The Ternary Feldspar Solvus and Subsolidus Exsolution:</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 6, Fig. 6-16). Illustrating the subsolidus miscibility gap (solvus) across the $Ab\text{--}Or\text{--}An$ system where homogeneous high-temperature feldspars unmix into perthite (K-rich host) or antiperthite (Na-Ca-rich host).
        </div>
      </div>

      <h4>Optical Identification Under the Polarizing Microscope</h4>
      <ul>
        <li><strong>Host Grain:</strong> Displays continuous polysynthetic albite twinning ($\{010\}$ plane) or combined Carlsbad-albite twinning across the entire grain.</li>
        <li><strong>Exsolved Inclusions:</strong> Appear as tiny, discrete, rectangular, bleb-like, or flame-shaped islands of K-feldspar scattered throughout the plagioclase host. Under cross-polarized light (XPL), the K-feldspar inclusions extinguish at a distinctly different angle from the host plagioclase and often display subtle gridiron/tartan twinning (microcline) or remain untwinned with lower refractive index ($n < 1.525$).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: THERMODYNAMICS OF THE FELDSPAR SOLVUS AND EXSOLUTION -->
  <div class="card">
    <div class="card-header bg-indigo">2. Thermodynamics of the Feldspar Solvus: Spinodal Decomposition & Nucleation</div>
    <div class="card-body">
      <p>
        At elevated magmatic temperatures ($T > 800\text{--}900^\circ\text{C}$), alkali feldspars and ternary feldspars form a complete, continuous solid solution because thermal kinetic energy overcomes the strain caused by the size mismatch between the large potassium ion ($r_{\text{K}^+} = 1.38\text{ \AA}$) and smaller sodium ($r_{\text{Na}^+} = 1.02\text{ \AA}$) and calcium ($r_{\text{Ca}^{2+}} = 1.00\text{ \AA}$) ions.
      </p>

      <h4>Subsolidus Phase Separation Across the Miscibility Gap</h4>
      <p>
        As the crystalline rock cools below the <strong>solvus temperature</strong> ($T < 650\text{--}700^\circ\text{C}$), the excess Gibbs free energy of mixing ($\Delta G_{\text{mix}} = \Delta H_{\text{mix}} - T\Delta S_{\text{mix}}$) becomes positive due to the high enthalpy of lattice strain ($\Delta H_{\text{mix}} > 0$). The single homogeneous solid solution becomes thermodynamically unstable and unmixes:
      </p>
      <ul>
        <li><strong>Binodal (Solvus Boundary):</strong> The equilibrium boundary where two distinct coexisting feldspar phases are in thermodynamic equilibrium ($\mu_i^{\text{plag}} = \mu_i^{\text{Kfs}}$).</li>
        <li><strong>Spinodal Boundary ($\frac{\partial^2 G}{\partial X^2} = 0$):</strong> Inside the chemical spinodal, there is no activation energy barrier to phase separation. The homogeneous lattice spontaneously breaks down via uphill diffusion (<strong>spinodal decomposition</strong>), producing ultrafine, periodic, coherent exsolution lamellae (cryptoperthites).</li>
        <li><strong>Nucleation and Growth:</strong> In the metastable region between the binodal and spinodal ($\frac{\partial^2 G}{\partial X^2} > 0$), unmixing requires overcoming an activation energy barrier, producing discrete, isolated blebs or patches of K-feldspar within plagioclase—the classic <strong>patchy antiperthite</strong>.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: PETROLOGIC SIGNIFICANCE OF ANTIPERTHITE -->
  <div class="card">
    <div class="card-header bg-emerald">3. Petrologic Environments & Geothermobarometry of Antiperthite</div>
    <div class="card-body">
      <p>
        Antiperthitic plagioclase is not ubiquitous; its presence serves as a diagnostic fingerprint of specific, extreme high-temperature and water-undersaturated geological environments:
      </p>
      <ul>
        <li><strong>Charnockite and Granulite Terrains:</strong> In granulite facies high-grade metamorphic complexes (e.g., Eastern Ghats, Southern Granulite Terrain of India), anhydrous conditions and high temperatures ($750\text{--}900^\circ\text{C}$) permit substantial substitution of potassium into plagioclase at peak conditions. Subsequent slow cooling yields spectacular antiperthitic andesine in <strong>enderbites</strong> and acid charnockites.</li>
        <li><strong>Proterozoic Anorthosite Massifs:</strong> Massive, plagioclase-dominated cumulates of massif-type anorthosites (e.g., Chilka Lake anorthosite, Odisha) typically contain coarse antiperthitic labradorite/andesine formed by slow subsolidus cooling of dry, mantle-derived parent magmas.</li>
        <li><strong>Two-Feldspar Geothermometry:</strong> The partitioning of albite component between coexisting perthitic K-feldspar and antiperthitic plagioclase forms the basis of the famous <strong>Two-Feldspar Geothermometer</strong> (Stormer, 1975; Fuhrman & Lindsley, 1988), allowing quantitative derivation of peak metamorphic and magmatic temperatures.</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 81</div>
        <div class="q-text">An inter-growth texture in which plagioclase contains inclusions of potash feldspar is known as :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Antiperthite</div>
          <div class="opt-node">(B) Perthite</div>
          <div class="opt-node">(C) Graphic texture</div>
          <div class="opt-node">(D) Ophitic</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Antiperthite:</strong> A subsolidus exsolution texture where a host crystal of plagioclase feldspar contains lamellae, blebs, or irregular inclusions of exsolved potassium feldspar.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Antiperthite — CORRECT</div>
        <p>
          <em>Antiperthite</em> is the exact, universally accepted petrographic definition for an intergrowth where <strong>plagioclase acts as the host mineral</strong> containing exsolved inclusions, blebs, or lamellae of <strong>potassium feldspar</strong>. It is commonly observed in high-grade granulite-facies rocks, charnockites (especially enderbite), and massif-type anorthosites (Winter, 2014, p. 95; Mahapatra, p. 119; Deer, Howie & Zussman, p. 390).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Perthite — INCORRECT</div>
        <p>
          <em>Perthite</em> is the inverse texture: the <strong>host crystal is potassium feldspar</strong> (microcline or orthoclase), which contains exsolved lamellae, strings, or blebs of <strong>sodic plagioclase (albite)</strong>. Mixing up perthite and antiperthite is one of the most common errors in optical mineralogy.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Graphic texture — INCORRECT</div>
        <p>
          <em>Graphic texture</em> is a primary cotectic magmatic intergrowth consisting of angular, cuneiform, runic prisms of <strong>quartz</strong> embedded within a <strong>potassium feldspar host</strong> in granitic pegmatites. It does not involve a plagioclase-potash feldspar exsolution relationship.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Ophitic — INCORRECT</div>
        <p>
          <em>Ophitic texture</em> is a magmatic crystallization texture characteristic of hypabyssal dolerite/diabase, where laths of <strong>plagioclase</strong> are completely enclosed poikilitically within large plates of <strong>clinopyroxene (augite)</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Systematic Comparison: Feldspar Exsolution & Intergrowth Textures</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Texture Name</th>
            <th>Continuous Host Matrix</th>
            <th>Exsolved / Intergrown Phase</th>
            <th>Primary Mechanism</th>
            <th>Diagnostic Geological Occurrences</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Antiperthite</strong></td>
            <td><strong>Plagioclase Feldspar</strong> (Oligoclase to Andesine)</td>
            <td><strong>Potassium Feldspar</strong> (Orthoclase / Microcline)</td>
            <td>Subsolidus unmixing across ternary feldspar solvus; K exsolution</td>
            <td><strong>Charnockite (Enderbite), Granulite, Anorthosite</strong></td>
          </tr>
          <tr>
            <td><strong>Perthite</strong></td>
            <td><strong>Potassium Feldspar</strong> (Microcline / Orthoclase)</td>
            <td><strong>Plagioclase Feldspar</strong> (Albite)</td>
            <td>Subsolidus unmixing across alkali feldspar solvus; Na exsolution</td>
            <td>Granite, Syenite, Granitic Pegmatite</td>
          </tr>
          <tr>
            <td><strong>Mesoperthite</strong></td>
            <td>Mutually interpenetrating network ($\approx 50:50$)</td>
            <td>Co-equal Albite and K-Feldspar lamellae</td>
            <td>Unmixing of high-temperature homogeneous hypersolvus alkali feldspar</td>
            <td>High-temperature Granulite, Hypersolvus Granite</td>
          </tr>
          <tr>
            <td><strong>Myrmekite</strong></td>
            <td>Plagioclase Feldspar (Oligoclase)</td>
            <td><strong>Quartz</strong> (Vermicular / worm-like tubes)</td>
            <td>Deuteric metasomatic replacement of K-feldspar by Ca-Na</td>
            <td>Granite, Granodiorite, Charnockite, Gneiss</td>
          </tr>
          <tr>
            <td><strong>Graphic Texture</strong></td>
            <td>Potassium Feldspar (Microcline)</td>
            <td><strong>Quartz</strong> (Cuneiform runic wedges)</td>
            <td>Simultaneous magmatic eutectic cotectic crystallization</td>
            <td>Granitic Pegmatite</td>
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
        <div class="p-header">Problem 1: Ternary Feldspar Modal Reconstitution to Homogeneous Protolith</div>
        <p>
          Microprobe analysis of an antiperthitic feldspar grain in an enderbite from the Eastern Ghats yields a plagioclase host of composition $\text{Ab}_{68}\text{An}_{30}\text{Or}_2$ occupying $85\text{ vol}\%$, and exsolved K-feldspar blebs of composition $\text{Or}_{92}\text{Ab}_7\text{An}_1$ occupying $15\text{ vol}\%$. Assuming identical molar densities, calculate the bulk ternary composition of the original homogeneous high-temperature feldspar prior to subsolidus unmixing.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Mass Balance Calculation:</strong><br>
          Bulk mole fraction of each end-member component is given by:
          $$X_i^{\text{bulk}} = (0.85 \times X_i^{\text{host}}) + (0.15 \times X_i^{\text{exsolved}})$$<br>
          1. <strong>Orthoclase ($\text{Or}$) Component:</strong>
          $$X_{\text{Or}}^{\text{bulk}} = (0.85 \times 0.02) + (0.15 \times 0.92) = 0.017 + 0.138 = \mathbf{0.155} \implies \mathbf{15.5\text{ mol}\%}$$<br>
          2. <strong>Albite ($\text{Ab}$) Component:</strong>
          $$X_{\text{Ab}}^{\text{bulk}} = (0.85 \times 0.68) + (0.15 \times 0.07) = 0.578 + 0.0105 = \mathbf{0.5885} \implies \mathbf{58.85\text{ mol}\%}$$<br>
          3. <strong>Anorthite ($\text{An}$) Component:</strong>
          $$X_{\text{An}}^{\text{bulk}} = (0.85 \times 0.30) + (0.15 \times 0.01) = 0.255 + 0.0015 = \mathbf{0.2565} \implies \mathbf{25.65\text{ mol}\%}$$<br>
          <strong>Conclusion:</strong> The original peak metamorphic feldspar had a homogeneous ternary composition of $\mathbf{Ab_{58.8}An_{25.7}Or_{15.5}}$, confirming crystallization above the ternary solvus at $T > 850^\circ\text{C}$.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Size Scale Classification of Perthitic Intergrowths</div>
        <p>
          Define the boundaries between: (a) Macroperthite; (b) Microperthite; and (c) Cryptoperthite, and state the analytical technique required to resolve each variety.
        </p>
        <div class="p-ans">
          <strong>Dimensional Classification:</strong><br>
          - <strong>(a) Macroperthite:</strong> Exsolution lamellae are thick ($> 0.1\text{ mm}$), coarse, and distinct enough to be seen with the <strong>naked eye or hand lens</strong> without optical magnification.<br>
          - <strong>(b) Microperthite:</strong> Exsolution lamellae range from $1\text{ to } 100\ \mu\text{m}$, invisible to the naked eye but beautifully resolved under the <strong>standard petrographic polarizing light microscope (PLM)</strong>.<br>
          - <strong>(c) Cryptoperthite:</strong> Submicroscopic exsolution lamellae on the nanometer scale ($< 1\ \mu\text{m}$, typically $10\text{--}100\text{ nm}$). Completely invisible under optical microscopy; can only be detected via <strong>Transmission Electron Microscopy (TEM)</strong> or single-crystal X-ray diffraction (XRD). Cryptoperthite causes light diffraction producing the bluish iridescence known as <em>moonstone</em> (schiller effect).
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Crystallographic Preferred Orientation of Exsolution Lamellae</div>
        <p>
          Why do perthite and antiperthite exsolution lamellae align preferentially parallel to the $(6\bar{0}1)$ or $(\bar{6}01)$ crystallographic lattice planes rather than along random directions?
        </p>
        <div class="p-ans">
          <strong>Lattice Strain Minimization (Willaime & Brown, 1974):</strong><br>
          - During coherent subsolidus exsolution, the lattices of the two unmixing feldspars remain continuous across the phase interface.<br>
          - Because $K^+$ and $Na^+$ have different ionic radii, lattice dimensions differ ($a_{\text{Kfs}} = 8.6\text{ \AA}$ vs $a_{\text{Albite}} = 8.1\text{ \AA}$), introducing significant elastic strain energy ($\Delta G_{\text{elastic}}$).<br>
          - The crystallographic orientation that minimizes total coherent elastic strain energy between potassium feldspar and sodic plagioclase is the irrational plane oriented close to <strong>$(6\bar{0}1)$</strong>, inclined at $\sim 73^\circ$ to the $(001)$ cleavage. Aligning along this plane minimizes interfacial lattice mismatch, making phase separation thermodynamically spontaneous.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Hypersolvus vs. Subsolvus Granites and Perthite Formation</div>
        <p>
          Compare the feldspar mineralogy of: (a) a Hypersolvus Granite crystallized at shallow crustal depth under low $P_{H_2O}$; and (b) a Subsolvus Granite crystallized at deep crustal levels under high $P_{H_2O}$.
        </p>
        <div class="p-ans">
          <strong>Petrogenetic Phase Boundary Analysis:</strong><br>
          - <strong>(a) Hypersolvus Granite (One-Feldspar Granite):</strong> Under dry, low $P_{H_2O}$ conditions, the granite solidus lies <em>above</em> the feldspar solvus ($T_{\text{solidus}} > T_{\text{solvus}}$). The magma crystallizes a <strong>single, homogeneous ternary alkali feldspar</strong>. Upon subsolidus cooling across the solvus, this single feldspar unmixes into spectacular <strong>perthite or mesoperthite</strong>.<br>
          - <strong>(b) Subsolvus Granite (Two-Feldspar Granite):</strong> Under high $P_{H_2O}$, dissolved water depresses the silicate solidus until it intersects the solvus ($T_{\text{solidus}} < T_{\text{solvus}}$). The magma crystallizes <strong>two separate primary magmatic feldspars directly from the melt</strong>: an independent potassium feldspar and an independent plagioclase feldspar.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Incoherent vs. Coherent Exsolution Microstructures</div>
        <p>
          Distinguish between coherent and incoherent exsolution in feldspars. Which mechanism governs the formation of coarse patchy antiperthite?
        </p>
        <div class="p-ans">
          <strong>Exsolution Physics:</strong><br>
          - <strong>Coherent Exsolution:</strong> Crystal lattice planes are continuous across the boundary between the host and exsolved phase with zero bond breakage, accommodated entirely by elastic strain. Common in cryptoperthites formed by rapid cooling.<br>
          - <strong>Incoherent Exsolution:</strong> The lattice mismatch is relieved by edge dislocations, lattice severance, and recrystallization. The phase boundary is a true incoherent grain boundary with no continuous lattice planes.<br>
          - <strong>Patchy Antiperthite:</strong> Coarse patchy antiperthite in granulites and charnockites is formed by <strong>incoherent exsolution accompanied by fluid-enhanced recrystallization</strong>, allowing potassium feldspar to coalesce into large, irregular, isolated blebs within the plagioclase host.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Two-Feldspar Geothermometer Principles</div>
        <p>
          Explain how the thermodynamic exchange of the albite ($Ab$) component between coexisting plagioclase and alkali feldspar is calibrated to calculate metamorphic equilibration temperatures.
        </p>
        <div class="p-ans">
          <strong>Thermodynamic Exchange Derivation:</strong><br>
          The exchange equilibrium of albite between coexisting plagioclase ($pl$) and alkali feldspar ($af$) is:
          $$\text{NaAlSi}_3\text{O}_{8\ (\text{in alkali feldspar})} \rightleftharpoons \text{NaAlSi}_3\text{O}_{8\ (\text{in plagioclase})}$$<br>
          At thermodynamic equilibrium:
          $$\mu_{Ab}^{af} = \mu_{Ab}^{pl}$$<br>
          Using Margules asymmetric solution parameters ($W_{AbOr}, W_{AbAn}, W_{OrAn}$) to account for non-ideal mixing, the distribution of albite is a sensitive, monotonic function of temperature ($T$) and pressure ($P$). By measuring the chemical compositions of perthite host and antiperthite host via electron microprobe, one can solve for the exact equilibrium temperature ($T_{\text{equilibration}}$).
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Massif-Type Anorthosite Plagioclase Mineralogy</div>
        <p>
          In the Chilka Lake anorthosite massif of Odisha, plagioclase megacrysts exhibit antiperthitic texture. What does this reveal about the crystallization temperature and volatile state of the parent magma?
        </p>
        <div class="p-ans">
          <strong>Petrogenetic Interpretation:</strong><br>
          1. <strong>High Crystallization Temperature:</strong> The high solubility of potassium in plagioclase (requiring $> 10\text{--}15\text{ mol}\% Or$ component in the initial plagioclase lattice) proves crystallization occurred at very high temperatures ($T \approx 1050\text{--}1200^\circ\text{C}$).<br>
          2. <strong>Water-Undersaturated Parent Magma:</strong> Massif-type anorthosites crystallized from deep crustal/sub-crustal ponded basaltic melts under essentially anhydrous ($H_2O$-deficient) conditions, precluding early separation of two discrete feldspars and forcing extensive subsolidus antiperthitic exsolution upon prolonged cooling.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Optical Discrimination: Antiperthite vs. Plagioclase Alteration (Sericite)</div>
        <p>
          Under the microscope, fine inclusions inside plagioclase can easily be mistaken for alteration products. How do you optically differentiate true exsolved K-feldspar inclusions (antiperthite) from secondary sericite or saussurite?
        </p>
        <div class="p-ans">
          <strong>Microscopic Criteria:</strong><br>
          - <strong>Antiperthite (Exsolution):</strong> Inclusions are K-feldspar. They have <strong>low refractive index ($n < n_{\text{plag}}$)</strong>, low birefringence ($\delta = 0.006\text{--}0.008$, displaying first-order grey/white interference colors identical to quartz), form crisp, rectangular, optical-crystallographically oriented blebs, and exhibit uniform extinction.<br>
          - <strong>Sericite (Secondary Alteration):</strong> Consists of fine-grained white mica (muscovite/paragonite). Exhibits <strong>intense, brilliant high second-to-third order interference colors (pinks, blues, greens)</strong> and fibrous/flaky morphology.<br>
          - <strong>Saussurite:</strong> Microcrystalline aggregate of high-relief, high-birefringence epidote/zoisite, calcite, and albite, easily distinguished by its extreme relief and speckled appearance.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 81, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q081_Antiperthite_Feldspar_Exsolution_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q081: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q081()
