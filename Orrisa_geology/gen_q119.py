#!/usr/bin/env python3
"""
Q119 Generator: Contact Metamorphic Temperatures & Hornfels Facies
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q119():
    title = r"Q119: Metamorphic Petrology: Hornfels Contact Metamorphic Temperatures | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Thermal Aureoles"
    h1_title = "Q119: Contact Metamorphic Temperatures: Hornfels Facies, Thermal Aureoles & $700^\circ\text{C}\text{--}800^\circ\text{C}$ Regime"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 119<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 25: Metamorphic Facies / Contact Metamorphic Facies, pp. 484–487; Fig. 25.1); Francis J. Turner, <em>Metamorphic Petrology: Mineralogical, Field, and Tectonic Aspects</em> (McGraw-Hill); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 81–84, 180); Kurt Bucher and Rodney Grapes, <em>Petrogenesis of Metamorphic Rocks</em> (8th Ed., Springer)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND THERMAL REGIMES OF HORNFELS -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Thermal Framework & The Hornfels Facies Series</div>
    <div class="card-body">
      <p>
        The term <strong>hornfels</strong> (German for "horn-stone", derived from its exceptional mechanical toughness and smooth, flint-like fracture resembling animal horn) designates a dense, fine-grained, non-foliated contact metamorphic rock produced by thermal recrystallization in the contact aureole surrounding an igneous intrusion.
      </p>
      <p>
        In metamorphic petrology (Winter, 2014, pp. 484–487; Turner, 1981; Bangar, p. 81), contact metamorphism is characterized by low confining lithostatic pressures ($P < 2\text{--}3\text{ kbar}$, depths $< 10\text{ km}$) and steep thermal gradients. In the inner, highest-temperature zones of contact aureoles—specifically the <strong>Pyroxene Hornfels Facies</strong>—equilibrium crystallization temperatures commonly range from <strong>$700^\circ\text{C}$ to $800^\circ\text{C}$</strong>:
      </p>

      <div class="figure-box">
        <img src="../../figures_Q119/winter_p485_hornfels_facies_temperature_regimes.png" alt="Contact Metamorphic Facies and Hornfels Temperatures from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 119.1 — Contact Metamorphic Facies Series and Temperature Regimes:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 485). Details the contact facies sequence from Albite-Epidote Hornfels ($300\text{--}500^\circ\text{C}$) $\rightarrow$ Hornblende Hornfels ($500\text{--}700^\circ\text{C}$) $\rightarrow$ <strong>Pyroxene Hornfels ($700\text{--}800^\circ\text{C}$)</strong>, terminating at Sanidinite facies ($> 850^\circ\text{C}$).
        </div>
      </div>

      <h4>The Tripartite Hornfels Facies Zonation across Contact Aureoles</h4>
      <p>
        Moving inward toward an intrusive magma body, contact aureoles display a predictable sequence of hornfels facies reflecting increasing thermal intensity:
      </p>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Contact Metamorphic Facies</th>
            <th>Aureole Zone Position</th>
            <th>Equilibrium Temperature Range</th>
            <th>Diagnostic Pelitic / Mafic Mineralogy</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Albite-Epidote Hornfels</strong></td>
            <td>Outer Aureole (Distal)</td>
            <td>$300^\circ\text{C}$ to $500^\circ\text{C}$</td>
            <td>Albite + Epidote + Chlorite + Actinolite + Quartz; Spotted slates</td>
          </tr>
          <tr>
            <td><strong>Hornblende Hornfels</strong></td>
            <td>Middle Aureole (Intermediate)</td>
            <td>$500^\circ\text{C}$ to $700^\circ\text{C}$</td>
            <td>Hornblende + Plagioclase (oligoclase/andesine) + Biotite + Cordierite + Andalusite</td>
          </tr>
          <tr>
            <td><strong>Pyroxene Hornfels</strong></td>
            <td><strong>Inner Aureole (Proximal Contact)</strong></td>
            <td><strong>$700^\circ\text{C}$ to $800^\circ\text{C}$</strong></td>
            <td><strong>Diopside + Hypersthene + Plagioclase (labradorite) + Cordierite + Sillimanite + K-feldspar</strong></td>
          </tr>
          <tr>
            <td><strong>Sanidinite Facies</strong></td>
            <td>Extreme Xenoliths / Wall Contact</td>
            <td>$> 850^\circ\text{C}$ to $1050^\circ\text{C}$</td>
            <td>Sanidine, Tridymite, Mullite, Pigeonite, Spurrite (Pyrometamorphism)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- CARD 2: HEAT TRANSFER & PYROXENE HORNFELS DEHYDRATION -->
  <div class="card">
    <div class="card-header bg-emerald">2. Heat Conduction Physics & Anhydrous Dehydration in the $700\text{--}800^\circ\text{C}$ Window</div>
    <div class="card-body">
      <h4>Magma Intrusion Temperatures and Contact Equilibrium</h4>
      <p>
        The maximum temperature attained at the contact interface between an intruding magma and cold country rock is governed by Jaeger's (1957) conductive heat transfer model:
      </p>
      $$T_{contact} = \frac{T_{magma} + T_{country}}{2}$$
      <ul>
        <li>For a granitic magma intruding at $T_{magma} \approx 800\text{--}900^\circ\text{C}$ into country rock at $200^\circ\text{C}$, the immediate contact temperature is $\sim 500\text{--}600^\circ\text{C}$ (Hornblende hornfels).</li>
        <li>For intermediate and mafic magmas (diorites, gabbros, basalts) intruding at $T_{magma} \approx 1100\text{--}1200^\circ\text{C}$, the proximal contact interface and inner aureole easily reach sustained temperatures of <strong>$700^\circ\text{C}$ to $800^\circ\text{C}$</strong>, generating classic pyroxene hornfelses.</li>
      </ul>

      <h4>Anhydrous Breakdown Reactions at $700\text{--}800^\circ\text{C}$</h4>
      <p>
        In the $700\text{--}800^\circ\text{C}$ window, all hydrous amphiboles and micas become completely unstable and dehydrate:
      </p>
      $$\text{Hornblende} + \text{Quartz} \xrightarrow{700\text{--}800^\circ\text{C}} \text{Diopside (Cpx)} + \text{Hypersthene (Opx)} + \text{Plagioclase} + \text{H}_2\text{O}\uparrow$$
      $$\text{Biotite} + \text{Muscovite} + \text{Quartz} \xrightarrow{700\text{--}800^\circ\text{C}} \text{Cordierite} + \text{K-feldspar} + \text{Sillimanite} + \text{H}_2\text{O}\uparrow$$
      <p>
        This total loss of bound hydroxyl groups results in the completely anhydrous, dense, crystalline hornfelsic texture.
      </p>
    </div>
  </div>
"""

    part2 = r"""
  <!-- OFFICIAL QUESTION CARD -->
  <div class="card bg-amber">
    <div class="card-header">Official Examination Question — OPSC Assistant Geologist 2021</div>
    <div class="card-body">
      <div class="question-text">
        <strong>Question 119:</strong> Common temperatures for the formation of hornfels range from about :
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> 700° to 800°C</div>
        <div class="option-item"><strong>(B)</strong> > 1000°C</div>
        <div class="option-item"><strong>(C)</strong> 1000-1200°C</div>
        <div class="option-item"><strong>(D)</strong> None of these</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) 700° to 800°C</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — The High-Temperature Hornfels Range</div>
        <p>
          <strong>Correct:</strong> In metamorphic petrology curricula and standard examination benchmarks (Winter, 2014, p. 485; Turner, 1981; Bangar, p. 81), the classic high-temperature contact metamorphic hornfels facies—specifically the <strong>Pyroxene Hornfels Facies</strong> developed in the inner contact aureoles of igneous intrusions—is universally defined across the temperature window of <strong>$700^\circ\text{C}$ to $800^\circ\text{C}$</strong>. At these temperatures, hydrous phyllosilicates and amphiboles completely dehydrate into pyroxenes, cordierite, and sillimanite.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Temperatures $> 1000^\circ\text{C}$</div>
        <p>
          <strong>Incorrect:</strong> Temperatures greater than $1000^\circ\text{C}$ exceed the dry melting solidus of crustal rocks, where rocks undergo extensive partial melting and anatexis, entering the magmatic or ultra-rare <strong>sanidinite facies (pyrometamorphism)</strong>. Sanidinite facies conditions are restricted to microscopic xenoliths immersed directly in flowing lava flows or volcanic necks. Normal hornfelses in contact aureoles do not form at $> 1000^\circ\text{C}$.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Temperatures $1000\text{--}1200^\circ\text{C}$</div>
        <p>
          <strong>Incorrect:</strong> The range $1000\text{--}1200^\circ\text{C}$ represents the liquidus eruption temperature of primary basaltic magmas in the mantle and oceanic spreading ridges, not the metamorphic temperature of hornfels country rock. Subjecting country rock to $1200^\circ\text{C}$ results in total complete fusion (buchite glass / magma), not solid-state metamorphic hornfels recrystallization.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — None of These</div>
        <p>
          <strong>Incorrect:</strong> Because Option (A) is the canonically verified and petrologically accurate temperature range, Option (D) is false.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison: Thermal Regimes of Metamorphic Facies</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Metamorphic Facies</th>
            <th>Characteristic Temperature Range</th>
            <th>Typical Pressure Range</th>
            <th>Hydrous vs. Anhydrous Mineralogy</th>
            <th>Primary Geodynamic Regime</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Pyroxene Hornfels</strong></td>
            <td><strong>$700^\circ\text{ to } 800^\circ\text{C}$</strong></td>
            <td>$< 2\text{--}3\text{ kbar}$ (Low $P$)</td>
            <td><strong>Strictly Anhydrous (Pyroxenes, Cordierite, Sillimanite)</strong></td>
            <td><strong>Inner contact aureoles of mafic/granitic plutons</strong></td>
          </tr>
          <tr>
            <td><strong>Hornblende Hornfels</strong></td>
            <td>$500^\circ\text{ to } 700^\circ\text{C}$</td>
            <td>$< 2\text{--}3\text{ kbar}$ (Low $P$)</td>
            <td>Hydrous + Anhydrous (Hornblende, Biotite, Andalusite)</td>
            <td>Middle contact aureoles</td>
          </tr>
          <tr>
            <td><strong>Granulite Facies</strong></td>
            <td>$750^\circ\text{ to } 900^\circ\text{C}$</td>
            <td>$6\text{ to } 11\text{ kbar}$ (High $P$)</td>
            <td>Strictly Anhydrous (Hypersthene, Peritectic Garnet, K-feldspar)</td>
            <td>Deep anhydrous lower continental crust</td>
          </tr>
          <tr>
            <td><strong>Sanidinite Facies</strong></td>
            <td>$> 850^\circ\text{ to } 1050^\circ\text{C}$</td>
            <td>$< 0.5\text{--}1\text{ kbar}$ (Near surface)</td>
            <td>High-T pyrometamorphic phases (Sanidine, Tridymite, Mullite)</td>
            <td>Direct wall-rock xenoliths trapped in volcanic conduits</td>
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
        <p>A quartz-mica shale is thermally metamorphosed in the inner contact aureole of a gabbro lopolith at $T = 750^\circ\text{C}$ and $P = 1.5\text{ kbar}$. What aluminum silicate polymorph ($\text{Al}_2\text{SiO}_5$) will crystallize, and why is kyanite absent?</p>
        <p><strong>Solution:</strong>
          At $T = 750^\circ\text{C}$ and $P = 1.5\text{ kbar}$, conditions fall squarely within the stability field of <strong>Sillimanite</strong> (or high-temperature andalusite near the boundary). <strong>Kyanite is completely absent</strong> because kyanite is the dense, high-pressure polymorph requiring confining pressures exceeding $P > 4\text{--}6\text{ kbar}$ ($z > 15\text{--}20\text{ km}$). Contact metamorphic aureoles develop at shallow crustal depths ($< 5\text{--}10\text{ km}$), where lithostatic pressures are far too low to stabilize kyanite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain the microscopic texture called "hornfelsic texture" (or decussate texture) and why it develops under contact metamorphism.</p>
        <p><strong>Solution:</strong>
          <strong>Hornfelsic (granoblastic / decussate) texture</strong> is an equigranular mosaic of interlocking, unoriented, polygonal mineral crystals meeting at triple junctions of approximately $120^\circ$. It develops because contact metamorphism operates under <strong>hydrostatic (non-directed) stress</strong>. In the absence of directed tectonic differential stress ($\sigma_1 = \sigma_2 = \sigma_3$), crystals minimize their interfacial surface energy by growing with completely random, interlocking orientations without developing planar foliation.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Calculate the width of the contact aureole where temperature exceeded $700^\circ\text{C}$ around a basaltic dyke of thickness $2a = 10\text{ m}$ intruded at $T_m = 1150^\circ\text{C}$ into country rock at $T_0 = 50^\circ\text{C}$, assuming instantaneous intrusion without latent heat.</p>
        <p><strong>Solution:</strong>
          According to Carslaw and Jaeger's 1D conductive cooling model for a dyke:
          The maximum temperature at the dyke wall ($x = a = 5\text{ m}$) immediately after intrusion is:
          $$T_{contact} = \frac{T_m + T_0}{2} = \frac{1150 + 50}{2} = \mathbf{600^\circ\text{C}}$$
          Notice that for a thin dyke, conduction into cold wall rock keeps the contact temperature at $600^\circ\text{C}$, which is <em>below</em> $700^\circ\text{C}$. This demonstrates mathematically that <strong>narrow dykes cannot produce the $700\text{--}800^\circ\text{C}$ pyroxene hornfels facies</strong>; high-temperature hornfelses ($700\text{--}800^\circ\text{C}$) require <strong>massive plutons or batholiths</strong> where sustained magma convection and latent heat of crystallization maintain aureole wall temperatures at $> 700^\circ\text{C}$ for thousands of years.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>What is a "buchite" and under what exceptional thermal conditions does it form?</p>
        <p><strong>Solution:</strong>
          A <strong>buchite</strong> is a pyrometamorphic rock produced when pelitic or psammitic rocks are subjected to extreme temperatures ($> 850\text{--}1050^\circ\text{C}$) in direct contact with dry, superheated basaltic lava flows or volcanic chimneys. Under these extreme conditions, the rock undergoes <strong>incipient melting (pyrometamorphism)</strong>, producing a distinctive rock composed of relic quartz and cordierite crystals embedded in a brown, vesicular glass matrix (pseudotachylyte-like glass).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>How do the mineral assemblages of the Hornblende Hornfels facies and the Pyroxene Hornfels facies differ in metamorphosed basaltic host rocks?</p>
        <p><strong>Solution:</strong>
          - <strong>Hornblende Hornfels Facies ($500\text{--}700^\circ\text{C}$):</strong> Dominated by hydrous minerals: <strong>Hornblende + Plagioclase (andesine/labradorite) $\pm$ Biotite $\pm$ Quartz</strong>.
          - <strong>Pyroxene Hornfels Facies ($700\text{--}800^\circ\text{C}$):</strong> Hornblende has completely dehydrated, replaced by an anhydrous assemblage: <strong>Diopside (Clinopyroxene) + Hypersthene (Orthopyroxene) + Calcic Plagioclase $\pm$ Olivine</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What is "chiastolite" and in which metamorphic zone of a contact aureole is it characteristically found?</p>
        <p><strong>Solution:</strong>
          <strong>Chiastolite</strong> is a distinctive variety of <strong>andalusite</strong> containing cross-shaped, geometric carbonaceous and graphite inclusions oriented along its crystallographic prism diagonals. It forms in the <strong>outer to middle contact aureole (spotted slate to hornblende hornfels zone, $450\text{--}550^\circ\text{C}$)</strong> during the thermal metamorphism of carbonaceous/organic-rich shales. Rapid dendritic growth of andalusite prism corners pushes carbonaceous dust into diagonal re-entrant planes, creating the Maltese cross pattern.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Why is high unconfined compressive strength ($\sigma_c > 200\text{--}250\text{ MPa}$) a defining mechanical property of hornfels in engineering geology?</p>
        <p><strong>Solution:</strong>
          In parent shales or slates, pervasive fissility and clay cleavage planes represent planes of extreme mechanical weakness. During high-temperature contact metamorphism ($700\text{--}800^\circ\text{C}$), thermal sintering, loss of hydroxyl fluids, and complete granoblastic recrystallization weld the minerals into a <strong>tightly interlocked, non-cleavable, isotropic crystalline mosaic</strong>. This obliterates all planes of weakness, transforming soft shale into one of the toughest, most abrasive, and shatter-resistant rocks known in rock mechanics.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>State the fundamental difference between the "Pyroxene Hornfels Facies" and the "Granulite Facies", given that both equilibrate at similar temperatures ($700\text{--}800^\circ\text{C}$) and contain orthopyroxene.</p>
        <p><strong>Solution:</strong>
          The defining distinction is <strong>confining pressure and tectonic stress</strong>:
          - <strong>Pyroxene Hornfels Facies:</strong> Forms at <strong>low lithostatic pressure ($P < 2\text{--}3\text{ kbar}$, $z < 8\text{ km}$)</strong> under hydrostatic stress; rocks are massive, non-foliated, fine-grained hornfelses. High-pressure minerals like almandine-pyrope garnet and kyanite are prohibited.
          - <strong>Granulite Facies:</strong> Forms at <strong>high lithostatic pressure ($P = 6\text{--}11\text{ kbar}$, $z = 20\text{--}35\text{ km}$)</strong> under regional orogenic stress in the deep continental crust; rocks are coarse-grained, pervasively banded or foliated (charnockites, granulites), and frequently contain high-pressure almandine garnet.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=119,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q119_Hornfels_Contact_Metamorphic_Temperatures_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q119: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q119()
