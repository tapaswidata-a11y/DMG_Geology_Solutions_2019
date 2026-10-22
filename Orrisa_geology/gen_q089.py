#!/usr/bin/env python3
"""
Q089 Generator: Harzburgite Peridotite Mineralogy & Ultramafic Petrology
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q089():
    title = r"Q089: Ultramafic Petrology: Harzburgite Mineralogy & Peridotite Ternary Classification | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Ultramafic Suites"
    h1_title = "Q089: Harzburgite: Olivine + Orthopyroxene Ultramafic Peridotite"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 89<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks / Ultramafic Rocks, p. 29; Ch. 10: Mantle Peridotites); R.W. Le Maitre, <em>Igneous Rocks: A Classification and Glossary of Terms (IUGS)</em>; K.M. Bangar, <em>Principles of Engineering Geology</em> (p. 165); G.B. Mahapatra, <em>A Text-Book of Geology</em> (p. 118)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND ETYMOLOGY OF HARZBURGITE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, History & Mineralogical Formula of Harzburgite</div>
    <div class="card-body">
      <p>
        The rock name <strong>harzburgite</strong> was introduced into petrological literature in 1880 by K.A. Lossen, named after its type locality near Bad Harzburg in the Harz Mountains of Lower Saxony, Germany.
      </p>
      <p>
        In the standard <strong>IUGS classification of ultramafic rocks</strong> (Le Maitre, 2002; Winter, 2014, p. 29), <strong>harzburgite</strong> is formally defined as an ultramafic plutonic rock ($M' \ge 90\%$) belonging to the <strong>Peridotite group</strong> ($\text{Olivine} \ge 40\%$), composed essentially of:
      </p>
      <div class="formula-box">
        <strong>IUGS Mineralogical Definition of Harzburgite:</strong><br>
        $$\mathbf{\text{Harzburgite}} = \mathbf{\text{Olivine (40--90\%)}} + \mathbf{\text{Orthopyroxene (10--60\%)}} \quad [\mathbf{\text{Clinopyroxene} < 10\%}]$$
      </div>
      <p>
        It is universally recognized as the <strong>two-mineral ultramafic rock composed of olivine and orthopyroxene (enstatite or bronzite)</strong>, commonly accompanied by accessory chromite or spinel.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q89/winter_p29_harzburgite_ultramafic_ternary.png" alt="IUGS Ultramafic Peridotite Ternary Diagram from Winter">
        <div class="figure-caption">
          <strong>Figure 89.1 — IUGS Ultramafic Classification Ternary ($Ol\text{--}Opx\text{--}Cpx$):</strong> Authentic textbook diagram from J.D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, Ch. 2, p. 29). Highlighting the Harzburgite field defined by $\text{Olivine} = 40\text{--}90\%$, $\text{Opx} > 10\%$, and $\text{Cpx} < 10\%$.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: THE IUGS PERIDOTITE TERNARY CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-indigo">2. The IUGS Peridotite-Pyroxenite Ternary System ($Ol\text{--}Opx\text{--}Cpx$)</div>
    <div class="card-body">
      <p>
        Ultramafic rocks ($M' \ge 90\%$) are classified on a triangular ternary diagram whose vertices represent the three dominant ferromagnesian phases normalized to $100\%$: <strong>Olivine ($Ol$)</strong>, <strong>Orthopyroxene ($Opx$)</strong>, and <strong>Clinopyroxene ($Cpx$)</strong>:
      </p>

      <h4>The Peridotite Division ($\text{Olivine} \ge 40\%$)</h4>
      <ul>
        <li><strong>Dunite:</strong> $\text{Olivine} > 90\%$ (essentially pure olivine rock).</li>
        <li><strong>Harzburgite:</strong> $\text{Olivine} = 40\text{--}90\%$, $\mathbf{Opx > 10\%}$, and $\mathbf{Cpx < 10\%}$ ($\mathbf{\text{Olivine} + \text{Orthopyroxene}}$).</li>
        <li><strong>Wehrlite:</strong> $\text{Olivine} = 40\text{--}90\%$, $\mathbf{Cpx > 10\%}$, and $\mathbf{Opx < 10\%}$ ($\mathbf{\text{Olivine} + \text{Clinopyroxene}}$).</li>
        <li><strong>Lherzolite:</strong> $\text{Olivine} = 40\text{--}90\%$, with <strong>both $Opx > 10\%$ and $Cpx > 10\%$</strong> ($\text{Olivine} + \text{Opx} + \text{Cpx}$). Represents fertile, un-depleted mantle.</li>
      </ul>

      <h4>The Pyroxenite Division ($\text{Olivine} < 40\%$)</h4>
      <ul>
        <li><strong>Orthopyroxenite:</strong> $Opx > 90\%$ of total pyroxenes.</li>
        <li><strong>Clinopyroxenite:</strong> $Cpx > 90\%$ of total pyroxenes.</li>
        <li><strong>Websterite:</strong> Two-pyroxene rock with both $Opx > 10\%$ and $Cpx > 10\%$.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: GEODYNAMIC ROLE: DEPLETED MANTLE RESTITE AND OPHIOLITES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Geodynamic Significance: Depleted Mantle Restite & Ophiolite Tectonites</div>
    <div class="card-body">
      <p>
        Harzburgite is of immense geodynamic significance as the primary constituent of the <strong>depleted sub-oceanic and sub-continental lithospheric mantle</strong>:
      </p>
      <ul>
        <li><strong>Mantle Melting Residue (Restite):</strong> When fertile mantle lherzolite undergoes partial melting beneath mid-ocean ridges or island arcs, the low-melting mineral <strong>clinopyroxene (diopside)</strong> melts out first into the basaltic liquid. The solid refractory residue left behind after $15\text{--}25\%$ basalt extraction is <strong>depleted harzburgite</strong>:
          $$\text{Fertile Lherzolite } (Ol + Opx + Cpx + Sp) \xrightarrow{\text{Partial Melting}} \text{Basaltic Melt} + \mathbf{\text{Depleted Harzburgite Restite } (Ol + Opx + Chromite)}$$
        </li>
        <li><strong>Ophiolite Basal Tectonites:</strong> In complete ophiolite sequences (e.g., Semail Ophiolite in Oman; Andaman Ophiolite; Sukinda in Odisha), the lower several kilometers beneath the Moho consist of foliated, sheared <strong>harzburgite tectonite</strong>, recording high-temperature mantle plastic flow.</li>
        <li><strong>Economic Podiform Chromite:</strong> Interactions between ascending melts and harzburgite dissolve orthopyroxene to precipitate replacive dunite envelopes hosting world-class <strong>podiform chromite ore bodies</strong> (e.g., Sukinda valley, Odisha).</li>
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
        <div class="q-num">Question 89</div>
        <div class="q-text">Harzburgite is an ultramafic plutonic rock composed essentially of :</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Olivine + orthopyroxene</div>
          <div class="opt-node">(B) Olivine + clinopyroxene</div>
          <div class="opt-node">(C) Olivine + plagioclase</div>
          <div class="opt-node">(D) Clinopyroxene + plagioclase</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (A)</div>
        <div><strong>Olivine + orthopyroxene:</strong> Harzburgite is canonically defined as a peridotite composed essentially of olivine (40–90%) and orthopyroxene (10–60%), with less than 10% clinopyroxene.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option correct">
        <div class="opt-title">(A) Olivine + orthopyroxene — CORRECT</div>
        <p>
          <em>Harzburgite</em> is strictly defined in the IUGS classification as an ultramafic peridotite composed essentially of <strong>olivine (40–90%) and orthopyroxene (enstatite/bronzite)</strong> with $<10\%$ clinopyroxene (Winter, 2014, p. 29; Le Maitre, 2002; Bangar, p. 165). It forms the dominant refractory mantle rock of the oceanic and cratonic lithosphere.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(B) Olivine + clinopyroxene — INCORRECT</div>
        <p>
          An ultramafic peridotite composed essentially of <strong>olivine + clinopyroxene (diopside/augite)</strong> with $<10\%$ orthopyroxene is named <strong>Wehrlite</strong> (named after Alois Wehrle).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Olivine + plagioclase — INCORRECT</div>
        <p>
          A plutonic rock composed of <strong>olivine + calcic plagioclase</strong> is named <strong>Troctolite</strong> (or "troutstone"). Because plagioclase is a felsic mineral, troctolite is a <strong>basic/mafic gabbroic rock</strong> ($M' < 90\%$), NOT an ultramafic rock.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Clinopyroxene + plagioclase — INCORRECT</div>
        <p>
          A plutonic rock composed essentially of <strong>clinopyroxene + calcic plagioclase</strong> is an ordinary <strong>Gabbro</strong> (or its volcanic equivalent, Basalt). It is a basic/mafic rock, completely excluded from the ultramafic peridotite group.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">IUGS Ultramafic Clan ($M' \ge 90\%$) Classification Matrix</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Ultramafic Rock</th>
            <th>Group</th>
            <th>Olivine Content ($Ol\%$)</th>
            <th>Orthopyroxene ($Opx\%$)</th>
            <th>Clinopyroxene ($Cpx\%$)</th>
            <th>Tectonic Role & Provenance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>HARZBURGITE</strong></td>
            <td><strong>Peridotite</strong></td>
            <td><strong>$40\text{--}90\%$</strong></td>
            <td><strong>$> 10\%$ (Dominant Pyroxene!)</strong></td>
            <td><strong>$< 10\%$ (Trace/Minor)</strong></td>
            <td><strong>Depleted Mantle Restite; Ophiolite Tectonites; Cratonic Keels</strong></td>
          </tr>
          <tr>
            <td><strong>Wehrlite</strong></td>
            <td>Peridotite</td>
            <td>$40\text{--}90\%$</td>
            <td>$< 10\%$ (Trace/Minor)</td>
            <td>$> 10\%$ (Dominant Pyroxene!)</td>
            <td>Mantle metasomatism; cumulate layered intrusions</td>
          </tr>
          <tr>
            <td><strong>Lherzolite</strong></td>
            <td>Peridotite</td>
            <td>$40\text{--}90\%$</td>
            <td>$> 10\%$ (Significant)</td>
            <td>$> 10\%$ (Significant)</td>
            <td>Fertile, pristine sub-lithospheric upper mantle</td>
          </tr>
          <tr>
            <td><strong>Dunite</strong></td>
            <td>Peridotite</td>
            <td><strong>$> 90\%$</strong></td>
            <td>$< 10\%$</td>
            <td>$< 10\%$</td>
            <td>Ultra-refractory restite; basal cumulates in layered intrusions</td>
          </tr>
          <tr>
            <td><strong>Websterite</strong></td>
            <td>Pyroxenite</td>
            <td>$< 40\%$</td>
            <td>$> 10\%$</td>
            <td>$> 10\%$</td>
            <td>Two-pyroxene cumulate layers; mantle pyroxenite veins</td>
          </tr>
          <tr>
            <td><strong>Orthopyroxenite</strong></td>
            <td>Pyroxenite</td>
            <td>$< 40\%$</td>
            <td>$> 90\%$ of pyroxenes</td>
            <td>$< 10\%$ of pyroxenes</td>
            <td>Bronzitite cumulate layers (e.g., Bushveld Critical Zone)</td>
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
        <div class="p-header">Problem 1: Modal Point-Count Plotting on the Ultramafic Ternary</div>
        <p>
          Point-count modal analysis of an ultramafic rock from an ophiolite mantle section yields: $65\%$ Olivine, $28\%$ Orthopyroxene, $4\%$ Clinopyroxene, and $3\%$ Chromite. Normalize the silicate phases to $100\%$ on the $Ol\text{--}Opx\text{--}Cpx$ triangle and determine the precise rock name.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Ternary Normalization:</strong><br>
          1. <strong>Sum of Essential Silicates:</strong>
          $$\sum = 65\% + 28\% + 4\% = 97.0\%$$<br>
          2. <strong>Normalized Percentages:</strong>
          $$Ol' = \frac{65}{97} \times 100\% = \mathbf{67.01\%}$$<br>
          $$Opx' = \frac{28}{97} \times 100\% = \mathbf{28.87\%}$$<br>
          $$Cpx' = \frac{4}{97} \times 100\% = \mathbf{4.12\%}$$<br>
          3. <strong>Classification Criteria:</strong><br>
          - Normalized Olivine ($67.0\%$) falls between $40\%$ and $90\%$ $\implies$ <strong>Peridotite</strong>.<br>
          - Normalized Orthopyroxene ($28.9\%$) exceeds $10\%$.<br>
          - Normalized Clinopyroxene ($4.1\%$) is strictly $< 10\%$.<br>
          <strong>Conclusion:</strong> The rock plots unambiguously in the <strong>Harzburgite</strong> field.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Mantle Partial Melting Stoichiometry</div>
        <p>
          Write a representative mass-balance melting equation demonstrating how partial melting of a primitive mantle lherzolite produces a basaltic melt and leaves behind a refractory harzburgitic residue.
        </p>
        <div class="p-ans">
          <strong>Petrogenetic Mass Balance:</strong><br>
          At $P = 1.5\text{ GPa}$ (depth $\sim 50\text{ km}$), decompression melting of spinel lherzolite follows the approximate reaction (in wt% coefficients):
          $$\mathbf{1.0\ \text{Lherzolite }} (0.55\ Ol + 0.25\ Opx + 0.15\ Cpx + 0.05\ Sp) \longrightarrow \mathbf{0.20\ \text{Basaltic Liquid}} + \mathbf{0.80\ \text{Harzburgite Residue }} (0.62\ Ol + 0.35\ Opx + 0.03\ Cr\text{-}Sp)$$<br>
          Because clinopyroxene contributes disproportionately to the melt ($\sim 70\%$ of the liquid components), $Cpx$ is completely consumed at $F \approx 20\%$, abruptly transforming the residual mantle from lherzolite to <strong>harzburgite</strong>.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Troctolite vs. Harzburgite Petrologic Demarcation</div>
        <p>
          Explain why Troctolite (Option C) is classified under the Gabbroic clan while Harzburgite (Option A) is classified under the Peridotite clan, citing the Color Index boundary ($M' = 90\%$).
        </p>
        <div class="p-ans">
          <strong>Color Index Demarcation:</strong><br>
          - <strong>Harzburgite:</strong> Composed of $>90\%$ mafic minerals ($Ol + Opx$, $M' \ge 90\%$). It contains no plagioclase. Therefore, it belongs strictly to the <strong>Ultramafic Clan (Peridotite group)</strong>.<br>
          - <strong>Troctolite:</strong> Composed of olivine plus calcic plagioclase (typically $35\text{--}65\%$ plagioclase). Because plagioclase is a felsic mineral, the Color Index of troctolite is $M' = 35\text{--}65\%$, which is far below the $90\%$ ultramafic threshold. Therefore, troctolite is an <strong>olivine gabbroid (basic/mafic rock)</strong>, not an ultramafic rock.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Sukinda Ultramafic Belt, Odisha</div>
        <p>
          Describe the geological significance of the Sukinda ultramafic complex in Odisha. What is the spatial relationship between chromitite seams, dunite, and harzburgite?
        </p>
        <div class="p-ans">
          <strong>Odisha Regional Geology:</strong><br>
          - <strong>Economic Significance:</strong> The Sukinda Valley in Jajpur district, Odisha, contains over <strong>$95\%$ of India's total chromite reserves</strong>.<br>
          - <strong>Stratigraphic Architecture:</strong> Sukinda represents a Precambrian dismembered layered intrusion/ophiolitic complex. The stratigraphy consists of basal serpentinized <strong>harzburgite and dunite</strong>, passing upward into pyroxenite and gabbro.<br>
          - <strong>Chromite Hosting:</strong> Thick stratiform/podiform seams of metallurgical-grade chromitite are enclosed within lenses of pure serpentinized <strong>dunite</strong> that form envelopes within the larger <strong>harzburgite</strong> mantle country rock.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Bastitization of Orthopyroxene during Low-Temperature Hydration</div>
        <p>
          When harzburgite undergoes hydrothermal serpentinization at $T < 300^\circ\text{C}$, olivine and orthopyroxene transform into distinct serpentine pseudomorphs. Name the pseudomorph after orthopyroxene and state its optical appearance.
        </p>
        <div class="p-ans">
          <strong>Serpentinization Microstructure:</strong><br>
          - <strong>Olivine:</strong> Hydrates to lizardite/chrysotile forming a classic <strong>mesh texture</strong> with magnetite strings along grain boundaries.<br>
          - <strong>Orthopyroxene:</strong> Hydrates to a fibrous, silvery-bronze pseudomorph called <strong>bastite</strong> (composed of oriented lizardite or antigorite fibers). Bastite preserves the exact rectangular prismatic shape and $\{110\}$ cleavage planes of the original enstatite, extinguishing uniformly under cross-polarized light.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Spinel Harzburgite vs. Garnet Harzburgite Depth Zonation</div>
        <p>
          State the pressure-depth transition separating spinel harzburgite from garnet harzburgite in the upper mantle, and write the mineralogical reaction.
        </p>
        <div class="p-ans">
          <strong>Mantle Facies Transition:</strong><br>
          - At depths shallower than $\sim 70\text{--}80\text{ km}$ ($P < 2.5\text{--}2.8\text{ GPa}$), aluminium in the mantle is accommodated in <strong>chromian spinel</strong> ($\text{Spinel Harzburgite Facies}$).<br>
          - At greater depths ($P > 2.8\text{ GPa}$, depths $> 80\text{--}90\text{ km}$), spinel reacts with orthopyroxene to form <strong>pyrope garnet</strong>:
          $$\text{MgAl}_2\text{O}_4\ (\text{Spinel}) + 4\text{MgSiO}_3\ (\text{Enstatite}) \rightleftharpoons \text{Mg}_3\text{Al}_2\text{Si}_3\text{O}_{12}\ (\text{Pyrope Garnet}) + \text{Mg}_2\text{SiO}_4\ (\text{Forsterite})$$<br>
          - Garnet harzburgites form the deep sub-continental lithospheric keels of ancient Archean cratons (e.g., Dharwar, Kaapvaal, Siberian cratons), serving as the primary source rock for diamond-bearing kimberlitic xenoliths.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Optical Distinction: Enstatite vs. Diopside in Peridotites</div>
        <p>
          How does a petrologist optically differentiate the orthopyroxene (enstatite) of harzburgite from the clinopyroxene (diopside) of wehrlite under cross-polarized light?
        </p>
        <div class="p-ans">
          <strong>Optical Mineralogy Comparison:</strong><br>
          - <strong>Orthopyroxene (Enstatite in Harzburgite):</strong> Orthorhombic. Displays <strong>straight (parallel) extinction ($0^\circ$)</strong> relative to prismatic cleavage lines in all longitudinal sections; low birefringence ($\delta = 0.008\text{--}0.010$, showing first-order grey to yellow interference colors); pale pink to green pleochroism in hypersthene.<br>
          - <strong>Clinopyroxene (Diopside in Wehrlite):</strong> Monoclinic. Displays <strong>inclined (oblique) extinction ($Z \wedge c = 38\text{--}44^\circ$)</strong>; moderate-to-high birefringence ($\delta = 0.024\text{--}0.030$, showing vibrant second-order blue, red, and green interference colors); non-pleochroic or pale green.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Suprasubduction Zone (SSZ) vs. Mid-Ocean Ridge (MOR) Ophiolites</div>
        <p>
          Why do Suprasubduction Zone (SSZ) ophiolites contain highly depleted harzburgite with ultra-refractory Cr-rich chromite ($Cr\# > 0.60$), whereas abyssal mid-ocean ridge peridotites are dominated by fertile lherzolite with Al-rich chromite ($Cr\# < 0.40$)?
        </p>
        <div class="p-ans">
          <strong>Geodynamic Fluid-Fluxed Melting:</strong><br>
          - <strong>Mid-Ocean Ridges (Dry Melting):</strong> Adiabatic decompression melting is limited to moderate melt fractions ($F \approx 10\text{--}18\%$), leaving a relatively fertile, clinopyroxene-bearing residual mantle (lherzolite to transitional harzburgite).<br>
          - <strong>Suprasubduction Zones (Forearcs / Back-arcs):</strong> The mantle wedge undergoes a <em>second stage of melting</em> driven by the influx of water and hydrous fluids from the subducting slab. High water activity depresses the solidus, driving extreme melt fractions ($F > 25\text{--}30\%$). This completely melts out all clinopyroxene and strips aluminium, producing an ultra-depleted <strong>harzburgite</strong> characterized by magnesium-rich olivine ($\text{Fo}_{92\text{--}94}$) and high-chromium chromite ($\text{Cr}\# = \text{Cr}/(\text{Cr}+\text{Al}) > 0.60$).
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 89, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q089_Harzburgite_Peridotite_Mineralogy_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q089: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q089()
