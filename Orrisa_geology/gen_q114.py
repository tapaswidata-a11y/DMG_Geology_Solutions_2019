#!/usr/bin/env python3
"""
Q114 Generator: The Fundamental Controlling Factors of Metamorphic Processes
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q114():
    title = r"Q114: Metamorphic Petrology: Factors Controlling Metamorphic Processes | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Thermodynamics"
    h1_title = "Q114: Controlling Factors of Metamorphic Processes: Protolith, P-T, Fluids & Geological Time"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 114<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: Factors Controlling Metamorphic Processes, pp. 405–410; Fig. 21.1); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 81–84); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 125–128); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: THE FOUR CONTROLLING FACTORS OF METAMORPHISM -->
  <div class="card">
    <div class="card-header bg-blue">1. The Four Foundational Controlling Factors of Metamorphic Systems</div>
    <div class="card-body">
      <p>
        In metamorphic geology (Winter, 2014, pp. 405–410; Bangar, p. 81; Bucher & Grapes, 2011), the mineralogical assemblage, micro-texture, and structural fabric of a metamorphic rock are governed by <strong>four fundamental thermodynamic, kinetic, and chemical variables</strong>:
      </p>
      <ol>
        <li><strong>(i) Chemical & Mineralogical Composition of the Parent Rock (Protolith):</strong> Because regional metamorphism is essentially an <em>isochemical process</em> (except for the release of volatile $\text{H}_2\text{O}$ and $\text{CO}_2$), the bulk chemical composition of the protolith sets the absolute limits on which mineral phases can possibly nucleate and grow. A pure quartz sandstone can only form quartzite; a pure limestone can only form marble; and an aluminous shale forms pelitic schists.</li>
        <li><strong>(ii) Temperature ($T$) and Pressure ($P$):</strong>
          <ul>
            <li><em>Temperature:</em> The most dominant factor; provides the thermal activation energy ($\Delta G^\ddagger$) required to break atomic bonds and drive solid-state ionic diffusion. It dictates the equilibrium positions of dehydration and decarbonation reactions.</li>
            <li><em>Pressure:</em> Confining (lithostatic) pressure ($\rho g z$) forces crystal lattices to compress into denser, lower-volume polymorphs ($\Delta V < 0$), while <em>directed differential stress</em> ($\sigma_1 > \sigma_3$) drives mechanical deformation and aligns minerals into pervasive foliation.</li>
          </ul>
        </li>
        <li><strong>(iii) The Nature and Presence of a Fluid Phase ($\text{H}_2\text{O}, \text{CO}_2$):</strong> Interstitial volatile fluids act as powerful catalysts. They accelerate solid-state reaction rates by orders of magnitude via grain-boundary diffusion, lower melting solidus curves, and govern decarbonation/dehydration equilibria through fluid activities ($a_{\text{H}_2\text{O}}, a_{\text{CO}_2}$).</li>
        <li><strong>(iv) Duration and Reaction Kinetics (Geological Time):</strong> Metamorphic events operate over timescales of $1\text{ to } 50+\text{ million years}$. Ample geological time allows sluggish, solid-state diffusion and mineral nucleation to overcome kinetic overstepping and achieve true thermodynamic chemical equilibrium.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q114/winter_p408_factors_controlling_metamorphism.png" alt="Factors Controlling Metamorphism from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 114.1 — The Interdependent Factors Controlling Metamorphic Evolution:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 408). Shows the dynamic feedback loops between Protolith Bulk Chemistry, Pressure-Temperature Trajectories, Interstitial Fluid Regimes, and Reaction Time.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: DETAILED THERMODYNAMIC ANALYSIS OF CONTROLLING VARIABLES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Quantitative & Thermodynamic Analysis of the Four Controlling Variables</div>
    <div class="card-body">
      <h4>Thermodynamic Breakdown of Metamorphic Agents</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Factor</th>
            <th>Thermodynamic / Physical Role</th>
            <th>Governing Equation / Law</th>
            <th>Diagnostic Manifestation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>(i) Protolith Composition</strong></td>
            <td>Defines the chemical system ($C$) in Gibbs Phase Rule ($F = C - P + 2$)</td>
            <td>Conservation of mass; isochemical transformation</td>
            <td>Pelitic $\rightarrow$ Garnet/Staurolite; Mafic $\rightarrow$ Hornblende/Epidote; Calcareous $\rightarrow$ Calcite/Wollastonite.</td>
          </tr>
          <tr>
            <td><strong>(ii) Pressure & Temperature</strong></td>
            <td>Defines equilibrium state and mineral stability field in $P\text{-}T$ space</td>
            <td>Gibbs Free Energy: $\Delta G = \Delta H - T\Delta S + P\Delta V$</td>
            <td>High-pressure blueschists; high-temperature granulites; oriented foliation under $\sigma_1 > \sigma_3$.</td>
          </tr>
          <tr>
            <td><strong>(iii) Fluid Composition</strong></td>
            <td>Catalyzes ionic diffusion; controls devolatilization phase equilibria</td>
            <td>Chemical potential of volatile components: $\mu_i = \mu_i^\circ + RT\ln a_i$</td>
            <td>Hydration reactions (serpentinization); decarbonation reactions (skarns); metasomatic ore halos.</td>
          </tr>
          <tr>
            <td><strong>(iv) Geological Time</strong></td>
            <td>Governs reaction kinetics, crystal coarsening, and nucleation rates</td>
            <td>Arrhenius Rate Law: $k = A e^{-E_a / RT}$; Diffusion: $x \approx \sqrt{2Dt}$</td>
            <td>Large porphyroblast growth; coarse granoblastic equilibration; preservation of zoned cores.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 114:</strong> The main factors that control metamorphic processes are : (i) The mineral composition of the parent rock, (ii) The pressure and temperature at which metamorphism takes place, (iii) The types of prevailing fluids (mostly water) during metamorphism, (iv) The amount of time available for metamorphism. Find out the odd one from the listed factors :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> (i) and (ii) are correct</div>
        <div class="option-item"><strong>(B)</strong> (i), (ii) and (iii) are correct</div>
        <div class="option-item"><strong>(C)</strong> (ii), (iii) and (iv) are correct</div>
        <div class="option-item correct-option"><strong>(D)</strong> All of the above are true explanations</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) All of the above are true explanations</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Evaluated — Incomplete Subset</div>
        <p>
          <strong>Incorrect:</strong> While protolith composition (i) and $P\text{-}T$ conditions (ii) are undeniably fundamental controls, selecting (A) falsely excludes fluids (iii) and time (iv), both of which are universally documented as indispensable primary factors controlling metamorphic systems.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Evaluated — Incomplete Subset</div>
        <p>
          <strong>Incorrect:</strong> Option (B) captures factors (i), (ii), and (iii), but arbitrarily excludes time (iv). Without sufficient geological time ($10^5\text{ to } 10^7\text{ years}$), solid-state reactions are kinetically inhibited from reaching equilibrium. Time is a well-established foundational control.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Evaluated — Incomplete Subset</div>
        <p>
          <strong>Incorrect:</strong> Option (C) omits factor (i)—the chemical and mineral composition of the parent rock. Protolith composition is arguably the most fundamental constraint of all, as no rock can crystallize minerals whose elements were not present in the precursor rock.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — All of the Above are True Explanations</div>
        <p>
          <strong>Correct:</strong> Every authoritative textbook in metamorphic petrology (Winter, 2014, p. 405; Bangar, p. 81; Bucher & Grapes, 2011; Miyashiro, 1994) confirms that <strong>all four listed factors—(i) Protolith composition, (ii) Pressure and Temperature, (iii) Fluid presence and composition, and (iv) Geological time—are canonical controlling factors of metamorphism</strong>. None of them is an "odd one" or invalid factor. Therefore, the comprehensive option <strong>(D) All of the above are true explanations</strong> is the verified and logically sound answer.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Systematic Evaluation of Metamorphic Controlling Factors</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Listed Factor</th>
            <th>Scientific Significance</th>
            <th>Primary Impact on Metamorphism</th>
            <th>Consequence of Absence / Variation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>(i) Protolith Composition</strong></td>
            <td>Supplies the chemical elemental components ($\text{Si, Al, Fe, Mg, Ca, Na, K}$)</td>
            <td>Controls phase mineralogy and mineral proportions via the Gibbs Phase Rule</td>
            <td>Determines whether the resulting rock is a marble, quartzite, amphibolite, or metapelite.</td>
          </tr>
          <tr>
            <td><strong>(ii) Pressure & Temperature</strong></td>
            <td>Sets the energetic thermodynamic state and directed deviatoric stress</td>
            <td>Determines metamorphic facies, mineral stability fields, and structural foliation</td>
            <td>Low $T \rightarrow$ Greenschist; High $T \rightarrow$ Granulite; High $P \rightarrow$ Blueschist/Eclogite; Directed stress $\rightarrow$ Schistosity.</td>
          </tr>
          <tr>
            <td><strong>(iii) Prevailing Fluids ($\text{H}_2\text{O}, \text{CO}_2$)</strong></td>
            <td>Provides interstitial transport medium and catalytic activation</td>
            <td>Accelerates reaction kinetics by orders of magnitude; enables hydration/dehydration</td>
            <td>"Dry" rocks (e.g., anhydrous gabbros) resist metamorphism and persist metastably even at high $P\text{-}T$.</td>
          </tr>
          <tr>
            <td><strong>(iv) Available Geological Time</strong></td>
            <td>Enables sluggish solid-state diffusion and crystal growth to proceed</td>
            <td>Permits nucleation, chemical homogenization, and attainment of true chemical equilibrium</td>
            <td>Rapid thermal events (e.g., flash meteorite impact or shallow dykes) yield metastable glasses or cryptocrystalline rinds.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">Exam-Standard Practice Problems & Analytical Derivations</div>
    <div class="card-body">
      <div class="problem-box">
        <h4>Practice Problem 1</h4>
        <p>A completely dry, anhydrous gabbro and a water-saturated basalt are both subjected to identical high-pressure conditions ($P = 15\text{ kbar}, T = 500^\circ\text{C}$). The wet basalt transforms into an eclogite, while the dry gabbro retains its igneous augite and plagioclase with only minor coronas. Which controlling factor explains this discrepancy?</p>
        <p><strong>Solution:</strong>
          This discrepancy is governed by <strong>Factor (iii): The presence of a fluid phase ($\text{H}_2\text{O}$)</strong>. Even when an assemblage is thermodynamically unstable, solid-state reconstructive transformation requires breaking chemical bonds and diffusing ions across grain boundaries. In dry systems, solid-state volume diffusion is extraordinarily slow ($D \sim 10^{-20}\text{ m}^2\text{/s}$), creating a massive <strong>kinetic barrier (overstepping)</strong> that prevents recrystallization. In the wet rock, aqueous fluid creates interconnected grain-boundary pathways where diffusion is $10^6\text{ to } 10^8\text{ times}$ faster, instantly catalyzing equilibrium recrystallization into eclogite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain how the duration of metamorphism (Factor iv: Time) affects the grain size of porphyroblasts according to Ostwald ripening theory.</p>
        <p><strong>Solution:</strong>
          <strong>Ostwald ripening</strong> dictates that small crystals possess a higher surface-area-to-volume ratio and higher interfacial free energy than large crystals. Over extended geological time ($10^6\text{ to } 10^7\text{ years}$), thermodynamics drives the slow dissolution of numerous tiny matrix crystals and the diffusive transfer of their mass onto fewer, larger crystals (porphyroblasts) to minimize total interfacial surface energy ($\sum \gamma_i A_i \rightarrow \text{minimum}$), resulting in coarse-grained, porphyroblastic schists.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Why is regional metamorphism described as an "isochemical" process, and what are the specific chemical exceptions to this rule?</p>
        <p><strong>Solution:</strong>
          Regional metamorphism is considered <strong>isochemical</strong> because the bulk non-volatile elemental composition ($\text{SiO}_2, \text{Al}_2\text{O}_3, \text{FeO}, \text{MgO}, \text{CaO}, \text{Na}_2\text{O}, \text{K}_2\text{O}$) remains essentially constant between protolith and metamorphic product. The sole universal exceptions are <strong>volatile chemical species—principally $\text{H}_2\text{O}$ and $\text{CO}_2$</strong>—which are systematically expelled as pore fluids during prograde dehydration and decarbonation reactions (an open system with respect to volatiles).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>How does the partial pressure ratio $X_{\text{CO}_2} = \frac{P_{\text{CO}_2}}{P_{\text{CO}_2} + P_{\text{H}_2\text{O}}}$ control the decarbonation temperature of calcite + quartz to wollastonite: $\text{CaCO}_3 + \text{SiO}_2 \rightleftharpoons \text{CaSiO}_3 + \text{CO}_2\uparrow$?</p>
        <p><strong>Solution:</strong>
          The chemical equilibrium is governed by the activity of carbon dioxide: $\Delta G = \Delta G^\circ + RT\ln f_{\text{CO}_2}$.
          - When the fluid is pure $\text{CO}_2$ ($X_{\text{CO}_2} = 1.0$), high $\text{CO}_2$ partial pressure suppresses the reaction, requiring high temperatures ($T \approx 750^\circ\text{C}$ at $2\text{ kbar}$) to drive decarbonation.
          - If the system is infiltrated by abundant $\text{H}_2\text{O}$ from an igneous source ($X_{\text{CO}_2} \rightarrow 0.1$), the $\text{CO}_2$ product is continually diluted and flushed away, lowering the equilibrium decarbonation temperature by more than <strong>$150\text{--}200^\circ\text{C}$</strong> (down to $\sim 550^\circ\text{C}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Calculate the lithostatic confining pressure exerted on a rock at $25\text{ km}$ depth in an orogenic root assuming average continental crustal density $\rho = 2800\text{ kg/m}^3$.</p>
        <p><strong>Solution:</strong>
          The lithostatic pressure formula is:
          $$P = \rho g z$$
          Given:
          - $\rho = 2800\text{ kg/m}^3$
          - $g = 9.81\text{ m/s}^2$
          - $z = 25,000\text{ m}$
          $$P = 2800 \times 9.81 \times 25,000 = 686,700,000\text{ Pa} \approx \mathbf{6.87\text{ kbar}} = \mathbf{0.687\text{ GPa}}$$
          The rock experiences approximately $6.87\text{ kbar}$ of lithostatic confining pressure, typical of the amphibolite facies.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>How does thermal activation energy ($E_a$) govern the rate of metamorphic reactions as formulated by the Arrhenius equation?</p>
        <p><strong>Solution:</strong>
          The reaction rate constant $k$ is given by the Arrhenius equation:
          $$k = A \exp\left(-\frac{E_a}{RT}\right)$$
          Because temperature $T$ appears in the denominator of the negative exponential, an increase in metamorphic temperature from $200^\circ\text{C}$ ($473\text{ K}$) to $600^\circ\text{C}$ ($873\text{ K}$) causes an exponential increase in the reaction rate constant $k$ by a factor of <strong>millions</strong>. This explains why low-temperature reactions are frequently kinetically inhibited, whereas high-temperature reactions equilibrate rapidly.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "metasomatism" and how does it represent an exception to the isochemical nature of metamorphism?</p>
        <p><strong>Solution:</strong>
          <strong>Metasomatism</strong> is allochemical metamorphism wherein circulating hydrothermal fluids introduce or remove substantial quantities of non-volatile chemical components ($\text{SiO}_2, \text{Fe, Mg, Ca, Na, K, metals}$) via advective mass transfer across the rock boundaries (e.g., formation of skarns, greisens, or serpentinized peridotites). It represents an <strong>open-system chemical transformation</strong>, violating the strict isochemical assumption.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why do coarse-grained plutonic rocks (like granites) require higher metamorphic temperatures to develop foliation than fine-grained sediments (like shales) under the same directed stress?</p>
        <p><strong>Solution:</strong>
          Fine-grained shales contain sub-microscopic clay minerals with enormous specific surface area, abundant adsorbed pore water, and weak crystal lattices, which deform and dynamically recrystallize readily at $200\text{--}300^\circ\text{C}$. Coarse-grained granites consist of large ($2\text{--}5\text{ mm}$), tightly interlocked anhydrous crystals of quartz and feldspar with zero interstitial fluid and low grain-boundary area. Plastic dislocation creep in feldspar requires temperatures <strong>$> 450\text{--}500^\circ\text{C}$</strong>; below this threshold, granite deforms only via localized brittle cataclasis.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=114,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q114_Factors_Controlling_Metamorphic_Processes_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q114: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q114()
