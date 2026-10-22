#!/usr/bin/env python3
"""
Q118 Generator: Hydrothermal Metamorphism & Metasomatism
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q118():
    title = r"Q118: Metamorphic Petrology: Hydrothermal Metamorphism & Metasomatism | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Metasomatism"
    h1_title = "Q118: Hydrothermal Metamorphism: Fluid-Rock Interaction, Allochemical Transfer & Metasomatism"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 118<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 29: Metasomatism and Hydrothermal Alteration, pp. 635–645; Fig. 29.1); D.S. Korzhinskii (1970), <em>Theory of Metasomatic Zonation</em> (Clarendon Press); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 81–84, 180); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROLOGICAL STATUS OF METASOMATISM -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Historical Roots & The Hydrothermal-Metasomatic Equivalence</div>
    <div class="card-body">
      <p>
        In metamorphic petrology and ore geology (Winter, 2014, pp. 635–645; Korzhinskii, 1970; Bangar, p. 81), <strong>hydrothermal metamorphism</strong> refers to the profound mineralogical and chemical alteration of rocks driven by the pervasive circulation of hot, chemically reactive aqueous solutions and supercritical fluids ($T \approx 100\text{--}600^\circ\text{C}$).
      </p>
      <p>
        In geological literature, the universally established scientific synonym for hydrothermal metamorphism is <strong>metasomatism</strong> (derived from the Greek $\mu\epsilon\tau\acute{\alpha}$, <em>meta</em>, denoting change, and $\sigma\tilde{\omega}\mu\alpha$, <em>soma</em>, meaning body).
      </p>
      <p>
        The term was introduced in 1826 by the German mineralogist Carl Friedrich Naumann and rigorously formulated thermodynamically by V.M. Goldschmidt (1922) and D.S. Korzhinskii (1970) as an <strong>open-system process of rock replacement</strong> where chemical components are introduced and removed simultaneously by hydrothermal diffusion and advective fluid percolation while the rock remains in the solid state.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q118/winter_p640_hydrothermal_metasomatism_allochemical.png" alt="Metasomatism and Hydrothermal Alteration from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 118.1 — Fluid-Rock Interaction and Metasomatic Zonation:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 640). Illustrates allochemical mass transfer between circulating hydrothermal fluids and host rocks, generating concentric metasomatic alteration zones.
        </div>
      </div>

      <h4>Fundamental Contrast: Isochemical Metamorphism vs. Metasomatism</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Characteristic</th>
            <th>Standard Regional Metamorphism (Autochemical)</th>
            <th>Hydrothermal Metamorphism / Metasomatism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>System Behavior</strong></td>
            <td><strong>Closed System</strong> (except for release of volatile $\text{H}_2\text{O}$ and $\text{CO}_2$)</td>
            <td><strong>Open System</strong> (free exchange of major non-volatile chemical components)</td>
          </tr>
          <tr>
            <td><strong>Bulk Rock Composition</strong></td>
            <td>Conserved; bulk chemistry identical to parental protolith</td>
            <td>Radically transformed; elements ($\text{Si, Fe, Mg, Ca, Na, K, metals}$) added/subtracted</td>
          </tr>
          <tr>
            <td><strong>Driving Mechanism</strong></td>
            <td>Regional geothermal heat ($\Delta T$) and tectonic differential stress</td>
            <td>Chemical potential gradients ($\Delta\mu_i$) and advective hydrothermal fluid flow</td>
          </tr>
          <tr>
            <td><strong>Volume Relationships</strong></td>
            <td>Substantial volume change ($\Delta V \ne 0$) under lithostatic compaction</td>
            <td>Lindgren's <strong>Law of Constant Volume</strong>: equal volume replacement via ionic exchange</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: CANONICAL METASOMATIC PROCESSES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Canonical Hydrothermal Metasomatic Processes in the Geological Record</div>
    <div class="card-body">
      <h4>Major Classes of Metasomatism</h4>
      <ul>
        <li><strong>Serpentinization & Steatitization:</strong> Hydrothermal hydration of ultramafic peridotites by hot seawater ($T \approx 200\text{--}400^\circ\text{C}$):
          $$2\text{Mg}_2\text{SiO}_4\text{ (forsterite)} + 3\text{H}_2\text{O} \rightarrow \text{Mg}_3\text{Si}_2\text{O}_5(\text{OH})_4\text{ (serpentine)} + \text{Mg(OH)}_2$$
          Further $\text{CO}_2$ infiltration transforms serpentine into <strong>talc-carbonate rock (soapstone)</strong>.
        </li>
        <li><strong>Greisenization:</strong> High-temperature ($400\text{--}500^\circ\text{C}$) auto-metasomatic alteration of granitic cupolas by post-magmatic, fluorine- and boron-rich hydrothermal fluids, converting feldspars into an aggregate of <strong>quartz + muscovite (lithium-rich) + topaz + fluorite + cassiterite ($\text{SnO}_2$)</strong>.</li>
        <li><strong>Spilitization (Ocean-Floor Metamorphism):</strong> Interaction of basaltic lavas with circulating ocean floor seawater at mid-ocean ridges, replacing calcic plagioclase with <strong>albite</strong> and pyroxene with <strong>chlorite/actinolite</strong>:
          $$\text{CaAl}_2\text{Si}_2\text{O}_8\text{ (anorthite)} + \text{Na}^+ + \text{Si}^{4+} \rightarrow \text{NaAlSi}_3\text{O}_8\text{ (albite)} + \text{Ca}^{2+} + \text{Al}^{3+}$$
        </li>
        <li><strong>Fenitization:</strong> Alkaline metasomatism around carbonatite and nepheline syenite complexes, where ultra-alkaline fluids enrich host granites in aegirine, sodic amphibole, and nepheline.</li>
        <li><strong>Skarnification:</strong> Contact metasomatism where silica- and iron-rich hydrothermal fluids from a granitic magma react with host carbonate rocks (limestone/dolomite).</li>
      </ul>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 118:</strong> The other name of hydrothermal metamorphism in geological literature is :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Autochemical metamorphism</div>
        <div class="option-item"><strong>(B)</strong> Allochemical metamorphism</div>
        <div class="option-item correct-option"><strong>(C)</strong> Metasomatism</div>
        <div class="option-item"><strong>(D)</strong> All of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(C) Metasomatism</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Autochemical Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> <strong>Autochemical (isochemical) metamorphism</strong> refers to standard regional metamorphism wherein the bulk chemical composition of the rock remains constant (closed system, except for the escape of volatile $\text{H}_2\text{O}$ and $\text{CO}_2$). Hydrothermal metamorphism, by contrast, is characterized by extensive chemical addition and removal of non-volatile elements via fluid circulation. Therefore, autochemical is the exact <em>antithesis</em> of hydrothermal metamorphism.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Evaluated — Allochemical Metamorphism</div>
        <p>
          <strong>Incorrect as a Specific Synonym:</strong> While hydrothermal metamorphism is broad-brush <em>allochemical</em> in nature (meaning "different chemistry"), "allochemical metamorphism" is merely a general descriptive modifier. In geological literature and textbook nomenclature (Winter, 2014, p. 635; Bangar, p. 81; Korzhinskii, 1970), the formal, universally recognized substantive name used interchangeably with hydrothermal metamorphism is <strong>Metasomatism</strong>.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-c">Option (C) Confirmed — Metasomatism</div>
        <p>
          <strong>Correct:</strong> In all authoritative geological curricula and petrological treatises (Winter, 2014, p. 635; Bangar, p. 81; Mahapatra, p. 126; Bucher & Grapes, 2011), <strong>metasomatism</strong> is the universally accepted and widely cited alternative name for <strong>hydrothermal metamorphism</strong>. It rigorously defines the process of substantial chemical composition change and mineral replacement brought about by circulating hydrothermal aqueous solutions.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — All of These</div>
        <p>
          <strong>Incorrect:</strong> Because Option (A) is completely false and diametrically opposed to hydrothermal processes, Option (D) is logically invalid. The official and scientific correct answer is exclusively <strong>(C) Metasomatism</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis of Metasomatic vs. Classical Metamorphic Environments</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Thermal (Contact) Metamorphism</th>
            <th>Regional (Dynamothermal) Metamorphism</th>
            <th>Hydrothermal Metamorphism (Metasomatism)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Dominant Agent</strong></td>
            <td>Conductive Magmatic Heat ($\Delta T$)</td>
            <td>Regional Heat ($\Delta T$) + Directed Stress ($\sigma_1 > \sigma_3$)</td>
            <td><strong>Circulating Aqueous Hydrothermal Fluids</strong></td>
          </tr>
          <tr>
            <td><strong>Chemical Openness</strong></td>
            <td>Largely isochemical (autochemical)</td>
            <td>Largely isochemical (autochemical)</td>
            <td><strong>Open system (Allochemical mass exchange)</strong></td>
          </tr>
          <tr>
            <td><strong>Transport Mechanism</strong></td>
            <td>Solid-state lattice diffusion</td>
            <td>Grain-boundary diffusion + plastic creep</td>
            <td><strong>Advective fluid percolation + chemical diffusion</strong></td>
          </tr>
          <tr>
            <td><strong>Characteristic Products</strong></td>
            <td>Hornfels, Quartzite, Marble</td>
            <td>Slate, Schist, Gneiss</td>
            <td><strong>Skarn, Greisen, Serpentinite, Spilite, Propylite</strong></td>
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
        <p>Define Lindgren's "Law of Constant Volume" in metasomatism and explain how a granite can be converted into a greisen without changing its physical bulk volume.</p>
        <p><strong>Solution:</strong>
          Waldemar Lindgren (1918) established the <strong>Law of Constant Volume</strong>: metasomatic replacement in solid rocks proceeds on an <strong>equal-volume basis ($\Delta V_{bulk} \approx 0$)</strong>. Because the host rock is confined under crustal pressure, replacement occurs by simultaneous, molecule-by-molecule (or ion-by-ion) dissolution of reactant minerals and precipitation of product minerals. As acidic hydrothermal fluids dissolve K-feldspar in granite, fluorine-rich mica (muscovite/lepidolite), quartz, and topaz precipitate directly within the created sub-microscopic void spaces, preserving original rock dimensions, fault markers, and structural textures without expansion or collapse.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Distinguish between "diffusional metasomatism" and "infiltrational (advective) metasomatism" according to D.S. Korzhinskii's theory.</p>
        <p><strong>Solution:</strong>
          - <strong>Diffusional Metasomatism:</strong> Mass transfer occurs via chemical diffusion of dissolved ions through stagnant, stationary pore fluids across a chemical potential gradient ($\Delta\mu_i$). Metasomatic alteration zones are typically <strong>narrow (millimeters to centimeters)</strong>, and zone boundaries exhibit continuous chemical gradients.
          - <strong>Infiltrational (Advective) Metasomatism:</strong> Mass transfer is driven by the physical, hydrodynamic flow (percolation) of hydrothermal solutions through interconnected fractures and pores under a hydraulic pressure gradient ($\nabla P$). Metasomatic zones can extend for <strong>hundreds of meters to kilometers</strong>, and zone boundaries are characterized by sharp, step-like compositional discontinuities.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is "spilitization" and what chemical exchange occurs between ocean-floor basalts and heated seawater?</p>
        <p><strong>Solution:</strong>
          <strong>Spilitization</strong> is low-temperature ($200\text{--}350^\circ\text{C}$) ocean-floor hydrothermal metasomatism of submarine basaltic lavas. Heated seawater circulating through oceanic crust exchanges ions with calcic plagioclase:
          $$\text{CaAl}_2\text{Si}_2\text{O}_8\text{ (anorthite)} + \text{Na}^+ + \text{Si}^{4+} \rightarrow \text{NaAlSi}_3\text{O}_8\text{ (albite)} + \text{Ca}^{2+} + \text{Al}^{3+}$$
          The basalt absorbs $\text{Na}^+$ and $\text{H}_2\text{O}$ from seawater while leaching $\text{Ca}^{2+}, \text{Fe}^{2+}, \text{Mn}^{2+}, \text{Cu}$, and $\text{Zn}$ into the hydrothermal fluid, converting normal basalt into an albite-chlorite rock termed <strong>spilite</strong> and feeding seafloor "black smoker" massive sulfide deposits.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Explain the process of "greisenization" and name the primary economic metal ore associated with greisen deposits.</p>
        <p><strong>Solution:</strong>
          <strong>Greisenization</strong> is high-temperature ($400\text{--}500^\circ\text{C}$) post-magmatic hydrothermal metasomatism affecting the apical cupolas of highly fractionated, peraluminous granitic plutons. Volatile-rich acidic fluids enriched in $F, B, Li, H_2O$ attack granitic feldspars, converting them into a quartz-white mica (muscovite/zinnwaldite)-topaz-fluorite rock called <strong>greisen</strong>. The primary economic metal ore precipitated in greisens is <strong>tin (cassiterite, $\text{SnO}_2$)</strong> and tungsten (wolframite, $\text{(Fe,Mn)WO}_4$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>How does metasomatic fenitization provide an exploration guide for carbonatite-hosted rare earth element (REE) and niobium deposits?</p>
        <p><strong>Solution:</strong>
          <strong>Fenitization</strong> produces broad, halo-like metasomatic aureoles surrounding intrusive carbonatite and alkaline complexes. Highly mobile, mantle-derived alkaline fluids rich in $\text{Na, K, Fe}^{3+}$, and volatiles invade surrounding granitic country rocks, converting quartz and biotite into aegirine, sodic amphibole (riebeckite/arfvedsonite), and alkali feldspar. Because the fenite alteration halo extends up to several kilometers beyond the central intrusion, mapping fenite zones directly vectors exploration geologists toward concealed, high-grade carbonatite plugs hosting rich <strong>REE and niobium (pyrochlore)</strong> mineralization.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is "propylitic alteration" in hydrothermal porphyry copper systems and what mineral assemblage characterizes it?</p>
        <p><strong>Solution:</strong>
          <strong>Propylitic alteration</strong> is a low-temperature ($200\text{--}300^\circ\text{C}$) hydrothermal metasomatic zone forming the outermost, distal halo around porphyry copper-gold deposits. It results from the interaction of cooling igneous host rocks with circulating meteoric hydrothermal fluids. The diagnostic mineral assemblage consists of <strong>epidote + chlorite + calcite + albite $\pm$ pyrite</strong>, imparting a distinctive dull green hue to the altered rocks.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Why does metasomatism typically produce monomineralic or oligomineralic rock zones (e.g., pure dunite, pure quartzite, pure skarn zones), whereas regional metamorphism produces polymineralic assemblages?</p>
        <p><strong>Solution:</strong>
          Governed by Korzhinskii's <strong>Phase Rule for Open Systems</strong>:
          $$F = C_{inert} - P + 2$$
          In an open metasomatic system, perfectly mobile components ($C_{mobile}$, whose chemical potentials are externally fixed by the fluid) do not count toward degrees of freedom ($C_{inert}$). Because many components ($\text{H}_2\text{O}, \text{CO}_2, \text{K, Na, Ca}$) become mobile, the number of inert components ($C_{inert}$) drops drastically. To satisfy the phase rule, the number of stable phases ($P$) must also drop, causing the progressive elimination of mineral phases and generating simplified, <strong>monomineralic or oligomineralic metasomatic reaction zones</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>What is a "reaction skarn" and how does it differ from an "infiltrational ore skarn"?</p>
        <p><strong>Solution:</strong>
          - <strong>Reaction Skarn (Bimetasomatic):</strong> Forms along the contact between two chemically contrasting rocks (e.g., shale and limestone) via <strong>local chemical diffusion across the contact</strong>; fluid serves only as a diffusion medium; alteration zones are thin (centimeters) and typically barren of ore.
          - <strong>Infiltrational Ore Skarn:</strong> Forms by the <strong>large-scale, advective flow of magmatic-hydrothermal fluids</strong> carrying dissolved silica, iron, and base metals into reactive carbonate host rocks; alteration zones extend tens to hundreds of meters and host major economic ore bodies of copper, tungsten, iron, and zinc.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=118,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q118_Hydrothermal_Metamorphism_Metasomatism_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q118: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q118()
