#!/usr/bin/env python3
"""
Q106 Generator: Migmatite High-Grade Metamorphism & Anatexis
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q106():
    title = r"Q106: Metamorphic Petrology: Migmatite & High-Grade Anatexis | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Anatexis"
    h1_title = "Q106: Migmatite Petrology: High-Grade Metamorphism, Partial Melting & Leucosome-Melanosome Fabric"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 106<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 27: Migmatites and Anatexis, pp. 405–420; Fig. 27.2 / p. 411); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer); K.M. Bangar, <em>Principles of Engineering Geology</em> (pp. 85–90, 185); Akiho Miyashiro, <em>Metamorphism and Metamorphic Belts</em> (Allen & Unwin)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROGENESIS OF MIGMATITES -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Petrogenetic Architecture & Terminology of Migmatites</div>
    <div class="card-body">
      <p>
        The term <strong>migmatite</strong> was introduced into petrological literature in 1907 by the Finnish petrologist Jakob Johannes Sederholm, derived from the Greek $\mu\tilde{\iota}\gamma\mu\alpha$ (<em>migma</em>, meaning "mixture").
      </p>
      <p>
        In modern metamorphic petrology (Winter, 2014, pp. 405–420; Bucher & Grapes, 2011), a <strong>migmatite</strong> is formally defined as an ultra-composite, megascopically heterogeneous rock found typically in <strong>high-grade metamorphic terranes</strong>. It consists of two or more repetitively layered or intimately intermingled constituents:
      </p>
      <ol>
        <li><strong>Neosome:</strong> The newly formed, modified portion of the rock created during high-grade metamorphism and partial melting, subdivided into:
          <ul>
            <li><strong>Leucosome:</strong> The light-colored, granitoid or trondhjemitic constituent enriched in quartz, plagioclase, and/or K-feldspar, representing the crystallized <strong>partial melt (in-situ anatectic liquid)</strong> or injected magmatic segregations.</li>
            <li><strong>Melanosome:</strong> The dark-colored, refractory residual layer bordering the leucosome, composed of residual mafic ferromagnesian minerals (biotite, hornblende, garnet, cordierite, sillimanite) left behind after melt extraction (the <em>restitic selvage</em>).</li>
          </ul>
        </li>
        <li><strong>Paleosome (Mesosome):</strong> The preserved, unmolten or least-modified parent metamorphic rock (gneiss, schist, or amphibolite) representing the unaltered protolith.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q106/winter_p411_migmatite_high_grade_metamorphism.png" alt="Migmatite Structure and High-Grade Anatexis from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 106.1 — Petrographic Architecture and Anatexis of Migmatites:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 411). Shows stromatic (layered) migmatite with light-colored granitic leucosome veins, dark restitic melanosome borders, and metamorphic paleosome.
        </div>
      </div>

      <h4>P-T Conditions: The High-Grade Metamorphic Domain</h4>
      <p>
        Migmatites mark the transitional thermal boundary zone between <strong>solid-state metamorphism and igneous magmatism (anatexis)</strong>:
      </p>
      <ul>
        <li><strong>Metamorphic Grade:</strong> Exclusively <strong>High Grade (Upper Amphibolite to Granulite Facies)</strong>.</li>
        <li><strong>Temperatures:</strong> In excess of the wet granite solidus, typically <strong>$T = 650^\circ\text{C}$ to $850^\circ\text{C}$</strong> (under water-saturated conditions, minimum melting occurs at $\sim 650^\circ\text{C}$ at $P \approx 4\text{--}6\text{ kbar}$).</li>
        <li><strong>Pressures:</strong> Mid-to-lower continental crust depths, typically <strong>$P = 4\text{ to } 10\text{ kbar}$</strong> (depths of $15\text{ to } 35\text{ km}$).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: ANATEXIS REACTIONS & MORPHOLOGICAL STRUCTURES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Anatectic Dehydration-Melting Reactions & Morphological Structures</div>
    <div class="card-body">
      <h4>Vapour-Absent Dehydration Melting Reactions</h4>
      <p>
        In continental collision zones, free aqueous fluid is rapidly consumed at lower grades. Consequently, high-grade migmatite anatexis is driven primarily by <strong>vapour-absent dehydration melting</strong> of hydrous phyllosilicates (Winter, 2014, p. 414):
      </p>
      <ol>
        <li><strong>Muscovite Dehydration Melting ($T \approx 680\text{--}720^\circ\text{C}$):</strong>
          $$\text{Muscovite} + \text{Quartz} + \text{Plagioclase} \rightarrow \text{Granitic Melt (Leucosome)} + \text{Sillimanite} + \text{K-feldspar}$$
        </li>
        <li><strong>Biotite Dehydration Melting ($T \approx 750\text{--}850^\circ\text{C}$):</strong>
          $$\text{Biotite} + \text{Sillimanite} + \text{Plagioclase} + \text{Quartz} \rightarrow \text{Granitic Melt} + \text{Garnet (or Cordierite)} \pm \text{K-feldspar}$$
          Here, garnet ($\text{Fe-Mg}$ almandine) or cordierite forms peritectic porphyroblasts trapped within the dark melanosome selvages.
      </ol>

      <h4>Morphological Structural Classes of Migmatites (Mehnert, 1968)</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Migmatite Structure</th>
            <th>Morphology & Geometric Fabric</th>
            <th>Melt Fraction & Deformation Intensity</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stromatic (Layered)</strong></td>
            <td>Regular, planar, alternating parallel sheets of leucosome and melanosome</td>
            <td>Low to moderate melt fraction ($10\text{--}20\%$); shear strain parallel to foliation.</td>
          </tr>
          <tr>
            <td><strong>Dictyonitic</strong></td>
            <td>Reticulate, vein-like network of leucosomes following intersecting shear bands</td>
            <td>Melt localized along brittle-ductile conjugate fracture systems.</td>
          </tr>
          <tr>
            <td><strong>Schollen (Raft)</strong></td>
            <td>Isolated, angular fragments/rafts of paleosome floating within a leucosome matrix</td>
            <td>High melt fraction ($> 30\text{--}40\%$); brecciation of brittle competent layers.</td>
          </tr>
          <tr>
            <td><strong>Phlebitic</strong></td>
            <td>Irregular, wavy, ptygmatically folded leucosome veins branching through host rock</td>
            <td>Moderate melt fraction; ductile ptygmatic bucking during compression.</td>
          </tr>
          <tr>
            <td><strong>Nebulitic</strong></td>
            <td>Fuzzy, ghost-like patches with indistinct, diffuse boundaries</td>
            <td>Very high melt fraction ($> 50\%$); near-complete magmatic homogenization.</td>
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
        <strong>Question 106:</strong> Migmatite consists of two or more constituents often layered repetitively forming a composite rock found in which metamorphic grade ?
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Low to medium grade</div>
        <div class="option-item"><strong>(B)</strong> Low grade</div>
        <div class="option-item"><strong>(C)</strong> Medium and high-grade</div>
        <div class="option-item correct-option"><strong>(D)</strong> High grade</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) High grade</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Low to Medium Grade</div>
        <p>
          <strong>Incorrect:</strong> Low-grade metamorphic rocks (sub-greenschist to greenschist facies, $T \approx 200\text{--}400^\circ\text{C}$) and medium-grade rocks (epidote-amphibolite facies, $T \approx 400\text{--}550^\circ\text{C}$) operate entirely in the solid state. Temperatures in these regimes are far below the minimum wet granite melting solidus ($\sim 650^\circ\text{C}$). Under no circumstances can partial melting (anatexis) or migmatite generation initiate in low- to medium-grade regimes.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Low Grade</div>
        <p>
          <strong>Incorrect:</strong> Low-grade metamorphism produces fine-grained slates and phyllites characterized by hydrous minerals (chlorite, sericite, actinolite). It cannot produce the granitic leucosomes, refractory restites, and high-temperature partial melts that define migmatites.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Medium and High-Grade</div>
        <p>
          <strong>Incorrect:</strong> While migmatites border upper-amphibolite facies, they are universally and unequivocally classified as the benchmark products of <strong>high-grade metamorphism</strong> (Winter, 2014, p. 405; Bucher & Grapes, 2011; Bangar, p. 87). Grouping migmatite formation with "medium grade" is technically inaccurate because the thermal energy required to cross the crustal solidus ($T > 650\text{--}700^\circ\text{C}$) strictly defines high-grade conditions. The official OPSC answer key specifically designates (D).
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — High Grade</div>
        <p>
          <strong>Correct:</strong> By universal petrological consensus (Winter, 2014; Bucher & Grapes, 2011; Miyashiro, 1994; Bangar, p. 87), <strong>migmatites</strong> are found exclusively in <strong>high-grade metamorphic terranes</strong> (upper amphibolite and granulite facies, $T = 650\text{--}850^\circ\text{C}$, $P = 4\text{--}10\text{ kbar}$). At these extreme temperatures, hydrous minerals break down via dehydration melting, generating in-situ granitic partial melts (leucosomes) alongside refractory residual restites (melanosomes).
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis: Metamorphic Grades and Representative Rock Suites</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Grade</th>
            <th>Temperature Range</th>
            <th>Metamorphic Facies</th>
            <th>Diagnostic Pelitic Mineral Assemblage</th>
            <th>Characteristic Rock Types</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Very Low Grade</strong></td>
            <td>$150\text{ to } 300^\circ\text{C}$</td>
            <td>Zeolite, Prehnite-Pumpellyite</td>
            <td>Illite, Smectite, Chlorite, Quartz</td>
            <td>Argillite, Slate</td>
          </tr>
          <tr>
            <td><strong>Low Grade</strong></td>
            <td>$300\text{ to } 450^\circ\text{C}$</td>
            <td>Greenschist</td>
            <td>Chlorite, Muscovite (phengite), Albite, Quartz</td>
            <td>Phyllite, Chlorite-schist, Greenschist</td>
          </tr>
          <tr>
            <td><strong>Medium Grade</strong></td>
            <td>$450\text{ to } 650^\circ\text{C}$</td>
            <td>Epidote-Amphibolite, Amphibolite</td>
            <td>Biotite, Almandine Garnet, Staurolite, Kyanite</td>
            <td>Garnet-mica schist, Kyanite schist, Amphibolite</td>
          </tr>
          <tr>
            <td><strong>High Grade</strong></td>
            <td><strong>$650\text{ to } 850+^\circ\text{C}$</strong></td>
            <td><strong>Upper Amphibolite, Granulite</strong></td>
            <td>Sillimanite, K-feldspar, Cordierite, Peritectic Garnet, Hypersthene</td>
            <td><strong>Migmatite</strong>, Sillimanite gneiss, Granulite, Charnockite</td>
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
        <p>A pelitic gneiss in a continental collision core undergoes partial melting at $T = 720^\circ\text{C}$ and $P = 6\text{ kbar}$. Write the dehydration-melting reaction for muscovite and identify which products partition into the leucosome and which into the melanosome.</p>
        <p><strong>Solution:</strong>
          The muscovite dehydration-melting reaction is:
          $$\text{Muscovite} + \text{Quartz} + \text{Plagioclase} \rightarrow \text{Granitic Liquid (Melt)} + \text{Sillimanite} + \text{K-feldspar}$$
          - <strong>Leucosome Partitioning:</strong> The hydrous granitic liquid (rich in normative quartz, albite, and orthoclase components) cools and crystallizes to form the light-colored, felsic <strong>leucosome</strong> veins.
          - <strong>Melanosome Partitioning:</strong> Insoluble refractory prismatic crystals of <strong>sillimanite</strong>, along with residual unmolten biotite, partition into the dark, aluminous <strong>melanosome</strong> restitic border.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain the physical concept of the Rheological Critical Melt Fraction (RCMF) in a high-grade migmatite terrane.</p>
        <p><strong>Solution:</strong>
          The <strong>Rheological Critical Melt Fraction (RCMF)</strong>, typically between <strong>$25\text{ and } 35\text{ volume}\%\text{ melt}$</strong> (van der Molen and Paterson, 1979), marks the fundamental mechanical threshold where:
          - Below RCMF ($< 25\%$ melt): The rock behaves as a rigid, grain-supported solid framework with isolated melt pockets in grain junctions; bulk viscosity remains high ($\eta \sim 10^{18}\text{ Pa}\cdot\text{s}$).
          - Above RCMF ($> 30\text{--}35\%$ melt): The solid grains become completely suspended in the liquid melt; bulk viscosity plummets by <strong>$10\text{ to } 14\text{ orders of magnitude}$</strong> ($\eta \sim 10^4\text{ to } 10^6\text{ Pa}\cdot\text{s}$), causing the rock to behave as a flowing magma capable of buoyant diapiric ascent and pluton formation.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Distinguish between a "restitic melanosome" and a "cumulate melanosome" in migmatite petrology.</p>
        <p><strong>Solution:</strong>
          - <strong>Restitic Melanosome:</strong> Represents the refractory solid residue left behind when the lowest-melting eutectic components (quartz + feldspar) are selectively extracted as liquid melt (e.g., concentrated restitic biotite, garnet, and sillimanite).
          - <strong>Cumulate Melanosome:</strong> Represents early-crystallizing high-temperature mafic crystals that precipitate from the anatectic melt and accumulate gravitationally or mechanically along the crystallization front.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is "ptygmatic folding" in a migmatite and what does it reveal about the relative viscosity of the leucosome vs. the paleosome host?</p>
        <p><strong>Solution:</strong>
          <strong>Ptygmatic folding</strong> refers to tortuous, highly irregular, meandrine buckle folds developed in isolated granitic leucosome veins cross-cutting a metamorphic host rock. According to Biot's buckle folding theory, ptygmatic folds develop when a relatively <strong>competent, high-viscosity vein</strong> is embedded in an <strong>incompetent, lower-viscosity, ductile host matrix</strong> undergoing strong bulk layer-parallel shortening.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Why do water-saturated melting curves (wet solidus) have negative $dP/dT$ slopes, whereas dehydration-melting curves have positive $dP/dT$ slopes in $P\text{-}T$ space?</p>
        <p><strong>Solution:</strong>
          Governed by the Clapeyron equation: $\frac{dP}{dT} = \frac{\Delta S}{\Delta V}$.
          - <strong>Wet Solidus ($\text{Rock} + \text{H}_2\text{O} \rightarrow \text{Melt}$):</strong> Because free water is consumed and water dissolves readily into granitic melt with a high density, the change in volume is negative ($\Delta V < 0$), while entropy increases ($\Delta S > 0$), producing a <strong>negative slope ($dP/dT < 0$)</strong>.
          - <strong>Dehydration Melting ($\text{Hydrous Mineral} \rightarrow \text{Melt} + \text{Anhydrous Solids}$):</strong> No free fluid phase is consumed; the liquid melt occupies more volume than the dense solid reactants ($\Delta V > 0$), resulting in a <strong>positive slope ($dP/dT > 0$)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Under what specific geodynamic conditions do migmatites form extensive regional belts in the continental crust?</p>
        <p><strong>Solution:</strong>
          Regional migmatite terranes develop in <strong>deep orogenic roots of continent-continent collision zones</strong> (e.g., the Greater Himalayan Crystalline complex, Variscides, and Grenville orogen). Crustal thickening ($> 60\text{--}70\text{ km}$) combined with radioactive radiogenic heat production ($U, Th, K$) in overthrust pelitic sheets drives temperatures above $700^\circ\text{C}$, triggering regional crustal melting, channel flow, and leucogranite plutonism.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is a "diatexite" and how does it differ from a "metatexite" in the Mehnert-Brown migmatite nomenclature?</p>
        <p><strong>Solution:</strong>
          - <strong>Metatexite:</strong> A migmatite exhibiting segregated, incipient melting where primary metamorphic structures (foliation, layering) are <strong>preserved</strong> in the paleosome/mesosome, and melt fractions remain low ($< 25\%$).
          - <strong>Diatexite:</strong> An advanced migmatite that has exceeded the RCMF ($> 35\text{--}50\%$ melt); primary metamorphic layering is <strong>completely obliterated</strong> by pervasive melting and turbulent magmatic flow, producing nebulitic to schollen textures transitioning into true anatectic granite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Why are peritectic garnets in migmatite leucosomes typically unzoned or exhibit flat chemical composition profiles compared to prograde metamorphic garnets?</p>
        <p><strong>Solution:</strong>
          Prograde garnets grown in the solid state below $600^\circ\text{C}$ preserve sharp growth zoning (Mn-rich cores to Fe-rich rims) because intra-crystalline lattice diffusion is sluggish. In contrast, peritectic garnets in migmatites crystallize at extreme temperatures ($T > 750\text{--}800^\circ\text{C}$) in equilibrium with melt; at these high temperatures, <strong>volume diffusion is extremely rapid</strong>, homogenizing any chemical gradients and producing flat, unzoned compositional profiles.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=106,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q106_Migmatite_High_Grade_Metamorphism_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q106: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q106()
