#!/usr/bin/env python3
"""
Q111 Generator: The Tripartite Metamorphic Classification & Regional Metamorphism
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q111():
    title = r"Q111: Metamorphic Petrology: The Tripartite Metamorphic Classification | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Classification"
    h1_title = "Q111: Metamorphic Classification: The Classical Triad (Contact, Regional, Dynamic)"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 111<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 21: An Introduction to Metamorphic Petrology, pp. 405–415; Fig. 21.2); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 81–84, 180); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 125–128); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: THE CLASSICAL TRIPARTITE METAMORPHIC CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Classical Tripartite Classification of Metamorphism</div>
    <div class="card-body">
      <p>
        In metamorphic geology (Winter, 2014, pp. 405–415; Bangar, p. 81; Mahapatra, p. 125), metamorphism is defined as the solid-state mineralogical, chemical, and structural adaptation of pre-existing rocks to physical and chemical conditions differing from those under which they originally formed.
      </p>
      <p>
        Historically and canonically, metamorphic processes are grouped into <strong>three grand primary categories</strong> based on the spatial scale of the event, the governing geological agent, and the tectonic environment:
      </p>
      <ol>
        <li><strong>Contact (Thermal) Metamorphism:</strong> Driven by conductive heat radiating outward from an intruding igneous magma body into adjacent cooler host rocks at shallow to intermediate crustal depths ($P_{lithostatic} < 2\text{--}4\text{ kbar}$). The stress field is hydrostatic (non-directed), producing localized concentric alteration halos (contact aureoles) characterized by non-foliated, granoblastic <strong>hornfelses</strong>.</li>
        <li><strong>Regional (Dynamothermal) Metamorphism:</strong> The most vast and dominant form of metamorphism on Earth, affecting thousands of square kilometers across orogenic mountain belts (convergent plate margins). Driven by the coupled action of <strong>elevated geothermal heat ($\Delta T$)</strong> and <strong>directed tectonic differential stress ($\sigma_1 > \sigma_3$)</strong> during continental collisions, producing penetratively foliated rocks (slates, schists, gneisses).</li>
        <li><strong>Dynamic (Cataclastic) Metamorphism:</strong> Driven by intense mechanical differential shear stress ($\tau$) localized along narrow fault planes, graben margins, and brittle-ductile shear zones. At shallow crustal levels ($< 5\text{--}10\text{ km}$, low temperatures), brittle crushing and pulverization dominate, producing fault gouge, fault breccia, and cataclasites; at deeper crustal levels with thermal activation, ductile shearing produces mylonites.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q111/winter_p410_metamorphism_types_contact_regional_dynamic.png" alt="Metamorphic Types and Settings from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 111.1 — The Three Fundamental Types of Metamorphism:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 410). Illustrates the spatial and tectonic domains of Contact metamorphism (pluton aureoles), Regional metamorphism (orogenic mountain roots), and Dynamic metamorphism (fault and shear zones).
        </div>
      </div>

      <h4>Comparison of Governing Agents across the Triad</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Type</th>
            <th>Primary Driving Agent</th>
            <th>Stress Regime</th>
            <th>Geological Spatial Scale</th>
            <th>Representative Rock Suite</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Contact (Thermal)</strong></td>
            <td>Thermal heat ($\Delta T$) from igneous plutons</td>
            <td>Hydrostatic / Isotropic ($\sigma_1 \approx \sigma_2 \approx \sigma_3$)</td>
            <td>Local: meters to $1\text{--}2\text{ km}$ surrounding intrusions</td>
            <td>Hornfels, Spotted slates, Marble, Quartzite, Skarn</td>
          </tr>
          <tr>
            <td><strong>Regional (Dynamothermal)</strong></td>
            <td><strong>Coupled Heat ($\Delta T$) + Directed Stress ($\sigma_1 > \sigma_3$)</strong></td>
            <td><strong>Triaxial differential tectonic compression</strong></td>
            <td><strong>Regional: hundreds to thousands of $\text{km}^2$</strong></td>
            <td><strong>Slate, Phyllite, Mica-schist, Gneiss, Migmatite</strong></td>
          </tr>
          <tr>
            <td><strong>Dynamic (Cataclastic)</strong></td>
            <td>Directed mechanical shear stress ($\tau$)</td>
            <td>High-strain localized shear</td>
            <td>Linear / Local: centimeters to tens of meters along fault zones</td>
            <td>Fault breccia, Cataclasite, Pseudotachylyte, Mylonite</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: EXTENDED MODERN CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Extended Modern Classifications: Hydrothermal, Burial & Impact Metamorphism</div>
    <div class="card-body">
      <h4>Modern Additions to the Classical Triad</h4>
      <p>
        In modern petrogenetic taxonomy (Winter, 2014; IUGS Subcommission on the Systematics of Metamorphic Rocks), the three classical types are complemented by specialized metamorphic environments:
      </p>
      <ul>
        <li><strong>Hydrothermal Metamorphism (Metasomatism):</strong> Chemical alteration driven by the circulation of hot, aqueous, ion-rich fluids through oceanic crust (e.g., black smokers at mid-ocean ridges, converting basalt into spilite, serpentinite, and soapstone).</li>
        <li><strong>Burial Metamorphism (Coombs, 1961):</strong> Low-temperature, low-to-moderate pressure recrystallization in deep subsiding sedimentary basins ($> 5\text{--}10\text{ km}$) without significant tectonic deformation, characterized by the <strong>zeolite and prehnite-pumpellyite facies</strong>.</li>
        <li><strong>Shock (Impact) Metamorphism:</strong> Instantaneous, extreme-energy impact of extraterrestrial bolides (meteorites) generating shock pressures of $10\text{ to }> 100\text{ GPa}$, producing planar deformation features (PDFs) in quartz, coesite, stishovite, and tektites.</li>
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
        <strong>Question 111:</strong> Three types of metamorphism are recognized e.g., Contact, ________ and Dynamic metamorphism.
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Thermal</div>
        <div class="option-item"><strong>(B)</strong> Static</div>
        <div class="option-item"><strong>(C)</strong> Local</div>
        <div class="option-item correct-option"><strong>(D)</strong> Regional</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) Regional</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Thermal Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> "Thermal metamorphism" is essentially a synonym for <strong>contact metamorphism</strong> (heat-driven alteration around an igneous intrusion). Because contact metamorphism is already explicitly named in the prompt ("Contact, ________ and Dynamic"), listing thermal would be a redundant repetition rather than completing the classical triad.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Static Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> "Static metamorphism" (or load metamorphism) refers loosely to recrystallization under vertical lithostatic pressure without horizontal tectonic stress (such as burial metamorphism). It is not one of the three foundational primary types established in standard geological curricula.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Local Metamorphism</div>
        <p>
          <strong>Incorrect:</strong> "Local metamorphism" is a spatial grouping category that encompasses contact, dynamic, and impact metamorphism (events confined to restricted, localized geographic areas). It is not a specific metamorphic mechanism coordinate with Contact and Dynamic.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — Regional Metamorphism</div>
        <p>
          <strong>Correct:</strong> By universal scientific agreement and standard textbook definition (Bangar, p. 81; Mahapatra, p. 125; Winter, 2014, p. 410), the three classical, universally recognized types of metamorphism are <strong>Contact metamorphism</strong>, <strong>Regional metamorphism</strong>, and <strong>Dynamic metamorphism</strong>. Regional metamorphism is the vast, orogenic process that accounts for more than $90\%$ of all metamorphic rocks on Earth.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comparative Analysis of the Classical Metamorphic Triad</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Category</th>
            <th>Primary Heat Source</th>
            <th>Role of Directed Differential Stress</th>
            <th>Dominant Fabric</th>
            <th>Plate Tectonic Environment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Contact</strong></td>
            <td>Magmatic heat from cooling plutons / batholiths</td>
            <td>Absent (Hydrostatic confining pressure)</td>
            <td>Non-foliated (granoblastic, hornfelsic)</td>
            <td>Continental magmatic arcs, shallow plutonic intrusions</td>
          </tr>
          <tr>
            <td><strong>Regional</strong></td>
            <td>Regional geothermal gradient + crustal thickening + radioactive decay</td>
            <td><strong>Dominant (Intense tectonic compression $\sigma_1 \gg \sigma_3$)</strong></td>
            <td><strong>Pervasively foliated (slaty, schistose, gneissic)</strong></td>
            <td><strong>Convergent collision orogens (Himalayas, Alps, Caledonides)</strong></td>
          </tr>
          <tr>
            <td><strong>Dynamic</strong></td>
            <td>Frictional dissipation (secondary)</td>
            <td><strong>Extreme localized shear stress ($\tau$)</strong></td>
            <td>Cataclastic / Mylonitic (foliated ribbons or shattered breccia)</td>
            <td>Major fault zones, transform faults, crustal detachment faults</td>
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
        <p>Distinguish between "Contact Metamorphism" and "Regional Metamorphism" based on spatial extent, typical structural fabric, and dominant geological driving agents.</p>
        <p><strong>Solution:</strong>
          - <strong>Spatial Extent:</strong> Contact metamorphism is local, restricted to narrow aureoles ($10\text{ m to } 2\text{ km}$) surrounding igneous bodies. Regional metamorphism covers vast orogenic provinces over thousands of square kilometers ($100\text{ to } 1000+\text{ km}$).
          - <strong>Structural Fabric:</strong> Contact metamorphism produces <strong>non-foliated</strong>, massive hornfelses. Regional metamorphism produces <strong>pervasively foliated</strong> slates, schists, and gneisses.
          - <strong>Driving Agents:</strong> Contact metamorphism is driven primarily by <strong>magmatic heat ($\Delta T$)</strong> under hydrostatic stress. Regional metamorphism is driven by the coupled combination of <strong>regional geothermal heat ($\Delta T$) and directed tectonic compressive differential stress ($\sigma_1 > \sigma_3$)</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>What is a "pseudotachylyte" and under which of the three metamorphic types does it originate?</p>
        <p><strong>Solution:</strong>
          A <strong>pseudotachylyte</strong> is an ultra-fine-grained, glassy or cryptocrystalline dark rock formed by the <strong>frictional melting of seismic fault surfaces</strong> during coseismic earthquake slip. It originates under extreme, high-strain-rate <strong>Dynamic Metamorphism</strong> along brittle-ductile faults where seismic shear strain generates localized flash frictional heating exceeding $1000^\circ\text{C}$ in seconds, melting thin glass veins.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>How does the width of a contact metamorphic aureole scale with the size and composition of an igneous intrusion?</p>
        <p><strong>Solution:</strong>
          The width of a contact aureole is governed by Fourier's law of conductive heat transfer and thermal diffusion ($x \sim 2\sqrt{\kappa t}$). It scales directly with:
          1. <strong>Intrusion Size (Thermal Mass):</strong> A narrow dyke ($1\text{ m}$ wide) produces an aureole only centimeters wide, whereas a gigantic granitic batholith ($10\text{--}20\text{ km}$ across) maintains sustained hydrothermal/conductive heat output for millions of years, generating an aureole $1\text{ to } 3\text{ km}$ wide.
          2. <strong>Magma Composition (Initial Temperature):</strong> Mafic/ultramafic magmas intrude at $1100\text{--}1200^\circ\text{C}$, producing much higher thermal grades and wider pyrometamorphic aureoles than cool felsic granitic magmas ($700\text{--}800^\circ\text{C}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is a "mylonite" and at what crustal depths does dynamic metamorphism transition from cataclasites to mylonites?</p>
        <p><strong>Solution:</strong>
          A <strong>mylonite</strong> is a cohesive, foliated dynamic metamorphic rock characterized by intense, ductile grain-size reduction (dynamic recrystallization and crystal-plastic dislocation creep) forming fine-grained groundmass ribbons enclosing eye-shaped porphyroclasts. The transition from brittle cataclasites to ductile mylonites occurs at the <strong>Brittle-Ductile Transition Zone (BDT)</strong>, typically at depths of <strong>$10\text{ to } 15\text{ km}$</strong> where crustal temperatures reach <strong>$300\text{--}350^\circ\text{C}$</strong> (the threshold for plastic dislocation glide in quartz).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Explain why burial metamorphism is characterized by the absence of penetrative foliation, even though confining lithostatic pressure may exceed $3\text{ kbar}$.</p>
        <p><strong>Solution:</strong>
          In a stable, subsiding sedimentary basin, confining pressure is purely lithostatic (vertical overburden weight, $\sigma_v = \rho g z$). In the absence of horizontal tectonic shortening or plate convergence, lateral stresses are approximately equal ($\sigma_h \approx \sigma_H$) and differential stress is minimal. Because there is <strong>no directed deviatoric differential stress ($\sigma_1 \gg \sigma_3$)</strong>, growing low-temperature minerals (zeolites, prehnite, pumpellyite) lack a preferred kinematic orientation, preserving original sedimentary bedding fabrics without developing metamorphic foliation.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Which of the three classical metamorphic types is responsible for the formation of the Barrovian metamorphic sequence in the Scottish Dalradian?</p>
        <p><strong>Solution:</strong>
          The Barrovian sequence was produced by <strong>Regional (Dynamothermal) Metamorphism</strong> during the Ordovician Grampian Orogeny ($\sim 470\text{ Ma}$, Caledonian cycle). Crustal thickening caused by the collision of an oceanic island arc with the Laurentian continental margin subjected Dalradian pelites to progressive regional heat and directed tectonic compressive stress, generating the classic Chlorite $\rightarrow$ Biotite $\rightarrow$ Garnet $\rightarrow$ Staurolite $\rightarrow$ Kyanite $\rightarrow$ Sillimanite regional belts.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "pyrometamorphism" and how does it relate to contact metamorphism?</p>
        <p><strong>Solution:</strong>
          <strong>Pyrometamorphism</strong> is an extreme, ultra-high-temperature subtype of contact metamorphism produced when rocks come into direct contact with very hot, dry basaltic magma ($T > 1000\text{--}1200^\circ\text{C}$) at very shallow crustal levels or within volcanic pipes. It is characterized by incipient melting (buchites) and high-temperature anhydrous phases such as tridymite, mullite, and sanidine.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>How does the presence of volatile aqueous fluids ($\text{H}_2\text{O}$) catalyze regional metamorphic reactions compared to dry contact metamorphism?</p>
        <p><strong>Solution:</strong>
          Aqueous fluids act as a powerful thermodynamic catalyst by:
          1. <strong>Accelerating Reaction Kinetics:</strong> Dissolving solid reactants and facilitating rapid advective and diffusive ion transport across grain boundaries ($10^6\text{ to } 10^8\text{ times}$ faster than solid-state lattice diffusion).
          2. <strong>Lowering Melting Temperatures:</strong> Depressing the solidus by several hundred degrees ($T_{wet} \sim 650^\circ\text{C}$ vs. $T_{dry} > 950^\circ\text{C}$).
          3. <strong>Hydrolytic Weakening:</strong> Diffusing into mineral lattices (quartz), weakening $\text{Si-O}$ bonds and accelerating crystal-plastic dislocation creep and ductile foliation development.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=111,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q111_Metamorphism_Types_Contact_Regional_Dynamic_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q111: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q111()
