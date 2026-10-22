#!/usr/bin/env python3
"""
Q103 Generator: Heavy Minerals & Sedimentary Provenance Analysis
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q103():
    title = r"Q103: Sedimentary Petrology: Heavy Minerals & Provenance Analysis | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Provenance"
    h1_title = "Q103: Heavy Mineral Suites: Petrographic Fingerprinting & Sedimentary Provenance Reconstructions"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 103<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Sandstones / Provenance, pp. 165–172; Fig. 5.15); Maria A. Mange and Heinz F.W. Maurer, <em>Heavy Minerals in Colour</em> (Chapman & Hall); F.J. Pettijohn, P.E. Potter, and R. Siever, <em>Sand and Sandstone</em>; Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PRINCIPLES OF HEAVY MINERAL PROVENANCE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, Separation Techniques & The Provenance Paradigm</div>
    <div class="card-body">
      <p>
        In clastic sedimentology and basin analysis (Boggs, 2014, pp. 165–172; Mange & Maurer, 1992; Pettijohn et al., 1987), <strong>heavy minerals</strong> are defined as accessory detrital mineral grains that possess a specific gravity greater than that of the standard rock-forming framework minerals (quartz $\rho \approx 2.65\text{ g/cm}^3$ and feldspars $\rho \approx 2.55\text{--}2.76\text{ g/cm}^3$).
      </p>
      <p>
        By convention, minerals with <strong>$\text{specific gravity} > 2.85\text{ g/cm}^3$</strong> (the density of bromoform, $\text{CHBr}_3$) or $> 2.90\text{ g/cm}^3$ (sodium polytungstate) are designated as heavy minerals. Although they typically constitute <strong>less than $1.0\%$ (often $< 0.1\%$)</strong> of a sandstone by weight, their extraordinary compositional diversity makes them the single most potent diagnostic tool for reconstructing <strong>sedimentary provenance</strong>.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q103/boggs_p170_heavy_minerals_provenance.png" alt="Heavy Mineral Suites and Provenance Lithologies from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 103.1 — Diagnostic Heavy Mineral Suites and Source Rock Lithologies:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 170). Details specific heavy mineral assemblages corresponding to acid igneous, basic/ultrabasic igneous, dynamic regional metamorphic, contact metamorphic, and recycled sedimentary provenances.
        </div>
      </div>

      <h4>The Concept of Sedimentary Provenance</h4>
      <p>
        The geological term <strong>provenance</strong> (from the French <em>provenir</em>, meaning "to originate or come forth") is an expansive, integrated scientific concept that encompasses:
      </p>
      <ol>
        <li><strong>Source Rock Lithology:</strong> The precise petrographic nature of the parent rocks (granite, basalt, amphibolite, schist, or older sedimentary strata).</li>
        <li><strong>Tectonic Setting of the Source Area:</strong> Craton interior, volcanic island arc, Andean-type continental magmatic arc, or collision orogen.</li>
        <li><strong>Paleoclimate and Weathering:</strong> The climatic regime under which the source rocks were unroofed and decomposed.</li>
        <li><strong>Drainage Basin Geometry & Paleocurrent Pathways:</strong> The geographic dispersal routes, transport distances, and fluvial/marine mixing patterns.</li>
      </ol>
    </div>
  </div>

  <!-- CARD 2: DIAGNOSTIC HEAVY MINERAL SUITES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Diagnostic Heavy Mineral Suites for Specific Source Lithologies</div>
    <div class="card-body">
      <h4>Petrographic Mineral Fingerprints</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Source Rock Lithology</th>
            <th>Diagnostic Heavy Mineral Assemblage</th>
            <th>Diagnostic Petrographic Characteristics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Acidic Igneous (Granites & Pegmatites)</strong></td>
            <td>Apatite, Biotite, Tourmaline (brown/pink schorl), Zircon, Monazite, Muscovite, Sphene (Titanite), Cassiterite</td>
            <td>Euhedral, prismatic, growth-zoned zircons; fluorine/boron-bearing species.</td>
          </tr>
          <tr>
            <td><strong>Basic & Ultrabasic Igneous (Basalts, Gabbros, Peridotites)</strong></td>
            <td>Augite, Hypersthene, Enstatite, Olivine, Chromite, Picotite, Ilmenite, Magnetite</td>
            <td>High-temperature pyroxenes; chrome spinels; opaque Fe-Ti oxides; low ZTR index.</td>
          </tr>
          <tr>
            <td><strong>Low-Grade Metamorphic (Greenschist Facies)</strong></td>
            <td>Chlorite, Chloritoid, Epidote, Zoisite, Actinolite, Green Tourmaline</td>
            <td>Flaky green phyllosilicates; pistachio-green pleochroic epidote.</td>
          </tr>
          <tr>
            <td><strong>High-Grade Regional Metamorphic (Amphibolite & Granulite Facies)</strong></td>
            <td>Garnet (almandine-pyrope), Kyanite, Sillimanite, Staurolite, Andalusite, Epidote, Hornblende</td>
            <td>Diagnostic aluminosilicate polymorphs ($\text{Al}_2\text{SiO}_5$); golden-yellow pleochroic staurolite; bladed kyanite.</td>
          </tr>
          <tr>
            <td><strong>Contact Metamorphic (Thermal Aureoles)</strong></td>
            <td>Andalusite (chiastolite), Cordierite, Vesuvianite, Wollastonite, Grossular garnet</td>
            <td>Cross-shaped carbonaceous inclusions in chiastolite; sector-twinned cordierite.</td>
          </tr>
          <tr>
            <td><strong>Recycled / Polycyclic Sedimentary</strong></td>
            <td>Zircon, Tourmaline, Rutile (ZTR $> 90\%$), Rounded Leucoxene, Rounded Chert</td>
            <td>Exceptionally high roundness and sphericity; abraded overgrowths; absence of labile species.</td>
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
        <strong>Question 103:</strong> The origin of many heavy mineral species is limited to rather specific rock types ; hence, heavies provide information concerning :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> source rock</div>
        <div class="option-item"><strong>(B)</strong> mineral dispersion pattern</div>
        <div class="option-item"><strong>(C)</strong> quaternary sediments</div>
        <div class="option-item correct-option"><strong>(D)</strong> provenance</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(D) provenance</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Source Rock (Incomplete Sub-concept)</div>
        <p>
          <strong>Incorrect:</strong> While heavy minerals certainly reveal the lithological nature of the parent rocks, "source rock" is merely <strong>one individual parameter</strong> within the broader geological discipline. Heavy minerals provide vastly more comprehensive data: they constrain tectonic regime, paleorelief, weathering intensity, transport distance, and drainage basin evolution. In sedimentary geology curricula and exam benchmarks (Boggs, 2014, p. 165; Pettijohn, 1975), the full, overarching scientific objective of heavy mineral study is formally designated as <strong>provenance</strong>.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Mineral Dispersion Pattern</div>
        <p>
          <strong>Incorrect:</strong> "Mineral dispersion pattern" refers specifically to exploration geochemistry (such as secondary geochemical dispersion halos around economic ore bodies during stream-sediment prospecting). While spatial mapping of heavies can delineate dispersion, this is a localized applied technique, not the primary fundamental petrological information revealed by diagnostic heavy mineral assemblages.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Quaternary Sediments</div>
        <p>
          <strong>Incorrect:</strong> Heavy mineral analysis applies equally to sedimentary rocks of <strong>all geological ages</strong>—from Archean quartzites and Proterozoic sandstones to Paleozoic, Mesozoic, and Cenozoic strata worldwide. It is not restricted to Quaternary sediments.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-d">Option (D) Confirmed — Provenance</div>
        <p>
          <strong>Correct:</strong> By fundamental definition in sedimentology (Boggs, 2014; Pettijohn et al., 1987; Mange & Maurer, 1992), because distinct heavy mineral species originate under specific thermomechanical conditions in particular parent rocks, their presence, variety, optical properties, and roundness provide diagnostic fingerprints of the sediment's <strong>provenance</strong> (source rock composition, tectonic setting, relief, climate, and transport history).
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Matrix: Provenance Discrimination Parameters from Heavy Mineral Petrography</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Analytical Dimension</th>
            <th>Heavy Mineral Indicator / Metric</th>
            <th>Geological Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Lithological Fingerprinting</strong></td>
            <td>Staurolite + Kyanite + Sillimanite</td>
            <td>Medium- to high-grade regionally metamorphosed pelitic rocks (Barrovian metamorphic terrane).</td>
          </tr>
          <tr>
            <td><strong>Tectonic Unroofing</strong></td>
            <td>Chrome spinel ($\text{Cr#}$) + Olivine $\rightarrow$ Pyroxenes $\rightarrow$ Zircon + Monazite</td>
            <td>Progressive erosional unroofing from ophiolitic mantle obduction to deeper granitic continental core.</td>
          </tr>
          <tr>
            <td><strong>Transport & Recycling</strong></td>
            <td>Roundness of Zircon and Tourmaline; ZTR Index $> 90\%$</td>
            <td>Polycyclic sedimentary recycling across multiple sedimentary cycles in stable cratonic basins.</td>
          </tr>
          <tr>
            <td><strong>Paleoclimate & Weathering</strong></td>
            <td>Survival vs. destruction of apatite, pyroxene, and amphibole</td>
            <td>Humid tropical climate dissolves apatite and pyroxene; arid or cold-glacial climates preserve them.</td>
          </tr>
          <tr>
            <td><strong>Diagenetic Dissolution (Intrastratal Solution)</strong></td>
            <td>Etched cockscomb terminations on augite and hornblende; skeletal garnets</td>
            <td>Deep burial mesodiagenesis by corrosive basinal pore waters dissolving labile minerals in-situ.</td>
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
        <p>A heavy mineral separation from a deltaic sandstone reveals an abundance of honey-yellow pleochroic staurolite, bladed kyanite, and almandine garnet. What specific provenance lithology and metamorphic grade are indicated?</p>
        <p><strong>Solution:</strong> The heavy mineral assemblage indicates a <strong>medium- to high-grade regionally metamorphosed pelitic source rock (amphibolite facies)</strong>. Staurolite, kyanite, and almandine are classic Barrovian index minerals formed by the regional metamorphism of aluminous shales under temperatures of $500\text{--}650^\circ\text{C}$ and pressures of $4\text{--}8\text{ kbar}$.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain how the chemical composition of detrital chrome spinel (specifically the Chromium Number, $\text{Cr\#} = \frac{\text{Cr}}{\text{Cr} + \text{Al}}$) is used in heavy mineral provenance analysis to distinguish between mid-ocean ridge basalts (MORB) and forearc peridotites.</p>
        <p><strong>Solution:</strong>
          Chrome spinel ($\text{(Mg,Fe)(Cr,Al,Fe)}_2\text{O}_4$) is highly resistant to chemical weathering and alteration. In modern petrogenetic models (Dick & Bullen, 1984):
          - <strong>MORB / Abyssal Peridotites:</strong> Exhibit low to moderate $\text{Cr\#}$ ($< 0.60$, typically $0.20\text{--}0.50$), reflecting lower degrees of mantle partial melting.
          - <strong>Forearc Peridotites / Supra-Subduction Zone Ophiolites:</strong> Undergo extreme fluxed partial melting ($> 25\text{--}35\%$), which selectively strips aluminum into the melt, leaving highly refractory residual spinels with <strong>very high $\text{Cr\#}$ ($> 0.60\text{ to } 0.85$)</strong>. Thus, detrital spinel $\text{Cr\#}$ precisely discriminates the geodynamic tectonic setting of the source ophiolite.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is "intrastratal solution" and how can it bias heavy mineral provenance interpretations in deeply buried sandstones?</p>
        <p><strong>Solution:</strong>
          <strong>Intrastratal solution</strong> (diagenetic dissolution) is the post-depositional leaching and destruction of unstable heavy minerals by hot, circulating basinal pore waters during deep burial diagenesis. Minerals disappear in a predictable order of decreasing stability:
          $$\text{Olivine} \rightarrow \text{Pyroxenes} \rightarrow \text{Amphiboles} \rightarrow \text{Epidote} \rightarrow \text{Garnet} \rightarrow \text{Staurolite} \rightarrow \text{Kyanite} \gg \text{ZTR}$$
          If an ancient sandstone has undergone intense intrastratal solution, an originally diverse heavy mineral assemblage may be stripped of all pyroxenes and amphiboles, falsely mimicking a high-maturity or multi-cycle cratonic provenance. Petrographers check for serrated "cockscomb" or "hacksaw" dissolution textures on remaining grains to detect this bias.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>How does the morphological roundness of detrital zircon crystals differentiate a first-cycle plutonic provenance from a polycyclic sedimentary provenance?</p>
        <p><strong>Solution:</strong>
          - <strong>First-Cycle Plutonic Provenance:</strong> Zircons directly weathered from a granitic pluton retain sharp, euhedral crystal facets, acute bipyramidal terminations, and pristine oscillatory growth zoning with zero roundness ($\rho < 0.15$).
          - <strong>Polycyclic Sedimentary Provenance:</strong> Because zircon is extremely hard (Mohs 7.5) and chemically inert, rounding a zircon crystal requires hundreds to thousands of kilometers of abrasive transport over multiple sedimentary recycling episodes. The presence of well-rounded, egg-shaped or spherical zircons ($\rho > 0.60$) definitively establishes a recycled sedimentary source rock.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Explain the principle of "hydraulic equivalence" in heavy mineral grain-size distribution.</p>
        <p><strong>Solution:</strong>
          According to C. Rubey (1933), when moving water deposits mineral grains, denser heavy minerals settle at the same hydrodynamic velocity as larger, lighter quartz grains. Under Stokes' Law and turbulent drag, two grains are in <strong>hydraulic equivalence</strong> when they possess the same settling velocity:
          $$v_{\text{heavy}} = v_{\text{quartz}} \implies d_{\text{heavy}} \approx d_{\text{quartz}} \sqrt{\frac{\rho_{\text{quartz}} - \rho_f}{\rho_{\text{heavy}} - \rho_f}}$$
          Because heavy minerals have higher densities ($\rho_h = 3.5\text{--}5.2\text{ g/cm}^3$ vs. $\rho_q = 2.65\text{ g/cm}^3$), their depositional grain diameter is systematically <strong>finer ($0.5\text{ to } 1.0\phi$ smaller)</strong> than the co-occurring quartz framework grains.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>What specific source rock is indicated by the presence of detrital glaucophane and lawsonite in a foreland basin sandstone?</p>
        <p><strong>Solution:</strong>
          Glaucophane (sodic amphibole) and lawsonite are the pathognomonic diagnostic minerals of <strong>blueschist facies metamorphism</strong>, formed under conditions of extreme high pressure and low temperature ($P = 6\text{--}12\text{ kbar}$, $T = 200\text{--}400^\circ\text{C}$). Their presence unequivocally diagnoses an <strong>obducted subduction complex or accretionary wedge suture zone</strong> provenance (e.g., Franciscan-type subduction complexes).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>How does U-Pb geochronology of detrital zircon revolutionize sedimentary provenance studies?</p>
        <p><strong>Solution:</strong>
          While optical heavy mineral microscopy identifies broad rock classes, in-situ LA-ICP-MS or SIMS U-Pb isotopic dating of individual detrital zircon cores yields absolute crystallization ages for hundreds of grains in a single sandstone. The resulting age probability density plot (e.g., peaks at $2.5\text{ Ga}$, $1.8\text{ Ga}$, and $500\text{ Ma}$) acts as an isotopic "DNA barcode" that matches the sediment directly to specific geological provinces, terranes, and mountain belts, precisely reconstructing continental drainage systems through geological time.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Contrast the heavy mineral suites expected from an arid desert environment vs. an intensely weathered, humid tropical rainforest basin draining the same granitic batholith.</p>
        <p><strong>Solution:</strong>
          - <strong>Arid Desert Drainage:</strong> Lacks moisture for chemical leaching. Both chemically stable (zircon, tourmaline, sphene) and chemically unstable/labile heavies (apatite, biotite, hornblende, augite) survive unweathered, yielding a diverse, multi-species heavy mineral suite.
          - <strong>Humid Tropical Rainforest Drainage:</strong> Extreme chemical hydrolysis and acidic humic groundwater dissolve all unstable species (apatite, pyroxenes, amphiboles are completely leached away). Only the ultra-resistant ZTR trio (Zircon, Tourmaline, Rutile) survives, yielding an artificially depleted, ultra-mature residual heavy mineral assemblage.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=103,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q103_Heavy_Minerals_Provenance_Analysis_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q103: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q103()
