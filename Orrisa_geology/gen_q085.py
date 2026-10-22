#!/usr/bin/env python3
"""
Q085 Generator: Lamprophyre Petrography & Panidiomorphic Texture
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q085():
    title = r"Q085: Igneous Petrology: Lamprophyre Petrography & Panidiomorphic Texture | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Igneous Petrology & Lamprophyre Dike Suites"
    h1_title = "Q085: Lamprophyre Petrography: Panidiomorphic (Lamprophyric) Texture"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 85<br>
<strong>Authoritative References:</strong> K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, Ch. 5: Petrology / Igneous Rocks, pp. 82, 165, 178); John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 2: Classification of Igneous Rocks / Lamprophyres); N.M.S. Rock, <em>Lamprophyres</em> (Blackie & Son / Springer); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 120–122)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND PETROGRAPHIC RULES OF LAMPROPHYRES -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition & Fundamental Petrographic Rules of the Lamprophyre Clan</div>
    <div class="card-body">
      <p>
        The term <strong>lamprophyre</strong> was introduced in 1874 by C.W. von Gümbel (derived from the Greek <em>lampros</em> = bright or glistening, and <em>phyro</em> = to mingle or mix), describing the glistening, sparkling reflection of abundant, freshly cleaved mica (biotite/phlogopite) phenocrysts in hand specimens.
      </p>
      <p>
        Lamprophyres are a clan of melanocratic, volatile-rich hypabyssal porphyritic dike rocks characterized by <strong>two iron-clad petrographic rules</strong> (Rock, 1991):
      </p>

      <div class="figure-box">
        <img src="../../figures_Q85/bangar_p178_lamprophyre_panidiomorphic.png" alt="Lamprophyre Petrography and Panidiomorphic Texture from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 85.1 — Petrographic Thin Section of Panidiomorphic Texture in Lamprophyre:</strong> Authentic textbook diagram from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 178). Depicting beautifully formed, sharp euhedral phenocrysts of biotite and hornblende set in a fine-grained, euhedral groundmass of feldspars and mafic minerals.
        </div>
      </div>

      <h4>The Two Cardinal Rules of Lamprophyre Petrography</h4>
      <ol>
        <li><strong>Phenocrysts are Exclusively Mafic:</strong> Phenocrysts consist solely of dark ferromagnesian minerals—<strong>biotite/phlogopite, amphibole (hornblende, kaersutite), clinopyroxene (diopside, titanaugite), and/or olivine</strong>. <em>Feldspars NEVER occur as phenocrysts!</em> Feldspars (orthoclase, sanidine, or plagioclase) and feldspathoids are strictly confined to the fine-grained groundmass.</li>
        <li><strong>Panidiomorphic (Lamprophyric) Texture:</strong> An extraordinary, hallmark texture where an overwhelming percentage of <strong>both the phenocrysts AND the groundmass mineral grains exhibit sharp, perfect, euhedral crystal faces</strong> (idiomorphic forms).</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q85/bangar_p82_lamprophyre_panidiomorphic.png" alt="Panidiomorphic Texture Definition from K.M. Bangar">
        <div class="figure-caption">
          <strong>Figure 85.2 — Classification of Crystallinity and Crystal Form:</strong> Authentic textbook scan from K.M. Bangar (<em>Principles of Engineering Geology</em>, p. 82). Showing the distinction between panidiomorphic, hypidiomorphic, and allotriomorphic textures.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: KINETICS OF PANIDIOMORPHIC TEXTURE -->
  <div class="card">
    <div class="card-header bg-indigo">2. Crystallization Kinetics: Why Lamprophyres are Panidiomorphic</div>
    <div class="card-body">
      <p>
        In typical igneous rocks (e.g., granite or basalt), groundmass crystals interfere with one another during rapid late crystallization, producing irregular, subhedral or anhedral grain boundaries (hypidiomorphic or intersertal textures). Why, then, do lamprophyre groundmass crystals develop <strong>perfect euhedral faces</strong>?
      </p>

      <h4>The Volatile-Fluxing Depolymerization Mechanism</h4>
      <ul>
        <li><strong>Ultra-High Volatile Fugacity ($H_2O, CO_2, F, P$):</strong> Lamprophyric magmas are water- and carbon-dioxide-saturated melts containing up to $3\text{--}8\text{ wt}\% H_2O$ and high dissolved carbonate, fluorine, and phosphorus.</li>
        <li><strong>Viscosity Collapse:</strong> Dissolved water and halogens violently depolymerize the silicate melt network, severing bridging oxygens ($Si\text{--}O\text{--}Si \to 2 Si\text{--}OH$). This reduces magma viscosity by orders of magnitude ($\eta \approx 0.1\text{--}1.0\text{ Pa}\cdot\text{s}$), transforming the melt into a fluid, watery medium.</li>
        <li><strong>High Ionic Diffusivity:</strong> In this ultra-fluid medium, ionic diffusion rates are astronomical. Crystals nucleate and grow rapidly in unhindered suspension, allowing crystal faces to achieve their low-energy, rational crystallographic planes (euhedral / idiomorphic geometry) before the remaining liquid freezes.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: CLASSIFICATION OF THE LAMPROPHYRE CLAN -->
  <div class="card">
    <div class="card-header bg-emerald">3. Systematic Classification of Lamprophyres (IUGS / Rock, 1991)</div>
    <div class="card-body">
      <p>
        Lamprophyres are divided into three primary branches based on their essential mafic minerals and groundmass felsic constituents:
      </p>

      <h4>1. Calc-Alkaline Lamprophyres (Shoshonitic Association)</h4>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Dominant Mafic Phenocryst</th>
            <th>Groundmass Dominant Feldspar: K-Feldspar</th>
            <th>Groundmass Dominant Feldspar: Plagioclase</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Biotite / Phlogopite</strong></td>
            <td><strong>MINETTE</strong> ($\text{Biotite} + \text{Orthoclase}$)</td>
            <td><strong>KERSANTITE</strong> ($\text{Biotite} + \text{Plagioclase}$)</td>
          </tr>
          <tr>
            <td><strong>Amphibole (Hornblende)</strong></td>
            <td><strong>VOGESITE</strong> ($\text{Hornblende} + \text{Orthoclase}$)</td>
            <td><strong>SPESSARTITE</strong> ($\text{Hornblende} + \text{Plagioclase}$)</td>
          </tr>
        </tbody>
      </table>

      <h4>2. Alkaline Lamprophyres</h4>
      <ul>
        <li><strong>Camptonite:</strong> Phenocrysts of brown titaniferous hornblende (kaersutite) and titanaugite set in a plagioclase-dominant groundmass.</li>
        <li><strong>Monchiquite:</strong> Feldspar-free alkaline lamprophyre! Phenocrysts of titanaugite, kaersutite, and olivine set in an isotropic groundmass of <strong>analcime</strong> or volcanic glass.</li>
        <li><strong>Sannaite:</strong> Phenocrysts of titanaugite and biotite in an alkali feldspar-dominant groundmass.</li>
      </ul>

      <h4>3. Ultramafic Lamprophyres</h4>
      <p>
        Melilite-bearing rocks such as <strong>Alnöite</strong> and <strong>Polzenite</strong>, forming transitional links to kimberlites and carbonatites.
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
        <div class="q-num">Question 85</div>
        <div class="q-text">The characteristic texture of lamprophyres is :</div>
        <div class="q-options">
          <div class="opt-node">(A) Allotriomorphic</div>
          <div class="opt-node correct">(B) Panidiomorphic</div>
          <div class="opt-node">(C) Xenomorphic</div>
          <div class="opt-node">(D) Hypidiomorphic</div>
        </div>
      </div>

      <div class="ans-banner">
        <div class="ans-badge">CORRECT ANSWER: (B)</div>
        <div><strong>Panidiomorphic:</strong> The diagnostic texture of lamprophyres (also termed lamprophyric texture), wherein a very high percentage of both the mafic phenocrysts and the groundmass minerals exhibit complete, sharp, euhedral (idiomorphic) crystal outlines.</div>
      </div>
    </div>
  </div>

  <!-- FORENSIC CARD -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis of Answer Choices</div>
    <div class="card-body">
      <div class="option wrong">
        <div class="opt-title">(A) Allotriomorphic — INCORRECT</div>
        <p>
          <em>Allotriomorphic</em> (or aplitic/sugary texture) describes a texture where almost all mineral grains are completely anhedral (lacking rational crystal faces), typically formed in granitic aplites, quartzites, and marbles.
        </p>
      </div>

      <div class="option correct">
        <div class="opt-title">(B) Panidiomorphic — CORRECT</div>
        <p>
          <em>Panidiomorphic texture</em> (from Greek <em>pan</em> = all, <em>idios</em> = own/distinct, <em>morphe</em> = form) is the universal, defining petrographic hallmark of the lamprophyre clan. Driven by high volatile fugacity ($H_2O, CO_2, F$) and low melt viscosity, virtually all constituent minerals—both the dark mafic phenocrysts and the fine groundmass laths—crystallize with perfect, sharp euhedral boundaries (Bangar, p. 82, 178; Winter, 2014, p. 43; Rock, 1991).
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(C) Xenomorphic — INCORRECT</div>
        <p>
          <em>Xenomorphic</em> is an exact synonym for allotriomorphic or anhedral. Minerals have irregular, mutual boundaries dictated by crowding against neighboring grains.
        </p>
      </div>

      <div class="option wrong">
        <div class="opt-title">(D) Hypidiomorphic — INCORRECT</div>
        <p>
          <em>Hypidiomorphic (or granitic) texture</em> is the common texture of standard plutonic rocks (like granite and diorite), where some minerals (like zircon, apatite, biotite) are euhedral to subhedral, but the later-crystallizing minerals (quartz and alkali feldspar) are anhedral, filling interstitial spaces.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Systematic Comparison: Grain Boundary Morphology Terms in Petrology</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Textural Term</th>
            <th>Synonym</th>
            <th>Crystal Face Development</th>
            <th>Physical Mechanism</th>
            <th>Canonical Rock Types</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Panidiomorphic</strong></td>
            <td><strong>Lamprophyric / Automorphic</strong></td>
            <td><strong>$> 80\text{--}90\%$ of crystals are fully Euhedral (Idiomorphic)</strong></td>
            <td>Low viscosity, volatile-rich ($H_2O, CO_2$) melt allowing unconstrained growth</td>
            <td><strong>Lamprophyres (Minette, Kersantite, Spessartite, Camptonite)</strong></td>
          </tr>
          <tr>
            <td><strong>Hypidiomorphic</strong></td>
            <td>Subhedral / Granitic texture</td>
            <td>Mixture of euhedral, subhedral, and anhedral grains</td>
            <td>Sequential cotectic crystallization in moderate-viscosity plutonic melts</td>
            <td>Granite, Granodiorite, Diorite, Syenite</td>
          </tr>
          <tr>
            <td><strong>Allotriomorphic</strong></td>
            <td>Xenomorphic / Anhedral / Aplitic</td>
            <td>Nearly all crystals are irregular and Anhedral (zero crystal faces)</td>
            <td>Simultaneous rapid crystallization of late, highly viscous eutectic melts</td>
            <td>Aplite, Granulite, Marble, Quartzite</td>
          </tr>
          <tr>
            <td><strong>Porphyritic</strong></td>
            <td>Phyric</td>
            <td>Bimodal grain size: Large phenocrysts in fine-grained groundmass</td>
            <td>Two-stage cooling history (slow deep incubation followed by rapid ascent)</td>
            <td>Porphyritic Andesite, Rhyolite, Basalt</td>
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
        <div class="p-header">Problem 1: Calc-Alkaline Lamprophyre Identification Matrix</div>
        <p>
          A hypabyssal dike rock in the Damodar Valley coalfields of India displays a panidiomorphic texture with abundant euhedral phenocrysts of glistening phlogopitic biotite. In thin section, the fine-grained groundmass consists predominantly of euhedral orthoclase feldspar and minor carbonate, with zero plagioclase. Classify this lamprophyre into its specific variety.
        </p>
        <div class="p-ans">
          <strong>Step-by-Step Petrographic Deduction:</strong><br>
          1. <strong>Mafic Phenocryst Phase:</strong> Biotite / Phlogopite.<br>
          2. <strong>Felsic Groundmass Mineralogy:</strong> Potassium feldspar (Orthoclase) dominant; plagioclase absent.<br>
          3. <strong>Classification Scheme (IUGS / Rock, 1991):</strong><br>
             - $\text{Biotite} + \text{Orthoclase} \implies \mathbf{MINETTE}$<br>
             - $\text{Biotite} + \text{Plagioclase} \implies \text{Kersantite}$<br>
             - $\text{Hornblende} + \text{Orthoclase} \implies \text{Vogesite}$<br>
             - $\text{Hornblende} + \text{Plagioclase} \implies \text{Spessartite}$<br>
          <strong>Conclusion:</strong> The rock is definitively a <strong>Minette</strong>, the most widespread mica-lamprophyre in continental rift and Gondwana coalfield dike swarms.
        </div>
      </div>

      <!-- Problem 2 -->
      <div class="p-card">
        <div class="p-header">Problem 2: Ocelli Structures and Liquid Immiscibility in Lamprophyres</div>
        <p>
          Lamprophyres frequently contain rounded, spherical or globular patches (1 to 10 mm in diameter) termed <em>ocelli</em>, consisting of light-colored analcime, calcite, and alkali feldspar surrounded by tangential biotite plates. Contrast the two primary genetic hypotheses for the origin of ocelli.
        </p>
        <div class="p-ans">
          <strong>Genetic Hypotheses:</strong><br>
          1. <strong>Liquid Immiscibility (Silicate-Carbonate/Foid Unmixing):</strong> The volatile-rich, water- and $CO_2$-saturated lamprophyric magma unmixes into two immiscible liquid droplets during late cooling: a host ultrabasic mafic liquid and conjugate globular droplets of alkaline-carbonate or felsic melt (ocelli).<br>
          2. <strong>Amygdaloidal Vapor Segregation:</strong> Ocelli represent late-stage magmatic gas bubbles (vesicles) into which residual, hydrous, highly fractionated pegmatitic/deuteric interstitial silicate-carbonate liquids were squeezed under gas overpressure.
        </div>
      </div>

      <!-- Problem 3 -->
      <div class="p-card">
        <div class="p-header">Problem 3: Chemical Paradox of Lamprophyres (High Mg# with High LREE/LILE)</div>
        <p>
          Explain the famous "geochemical paradox" of lamprophyres: Why do they simultaneously possess primitive mantle characteristics ($Mg\# > 70$, $Ni > 300\text{ ppm}$, $Cr > 600\text{ ppm}$) AND ultra-enriched crustal characteristics ($K_2O > 4\%$, $Ba > 2000\text{ ppm}$, $Sr > 1500\text{ ppm}$, $(\text{La/Yb})_N > 30$)?
        </p>
        <div class="p-ans">
          <strong>Petrogenetic Explanation:</strong><br>
          - <strong>Primitive Signature:</strong> The high $Mg\#$, $Ni$, and $Cr$ confirm that lamprophyre magmas are primary mantle melts derived directly from peridotite that did not undergo extensive crustal fractional crystallization.<br>
          - <strong>Enriched Signature:</strong> The extraordinary enrichment in Large Ion Lithophile Elements (LILE: $K, Ba, Sr$) and Light Rare Earth Elements (LREE) is caused by <strong>extreme low-degree partial melting ($F < 1\text{--}3\%$) of an ancient, metasomatized mantle lithosphere</strong>. Subduction-derived hydrous fluids or carbonatitic melts previously metasomatized the mantle wedge, precipitating veins of phlogopite, apatite, and titanaugite (glimmerite). Melting of these metasomatic veins generated the enriched primary lamprophyre liquid.
        </div>
      </div>

      <!-- Problem 4 -->
      <div class="p-card">
        <div class="p-header">Problem 4: Monchiquite vs. Camptonite Differentiation</div>
        <p>
          Under petrographic inspection, an alkaline lamprophyre displays titanaugite and kaersutite phenocrysts set in an isotropic, low-relief groundmass devoid of crystalline feldspar laths. Distinguish whether this is a camptonite or a monchiquite.
        </p>
        <div class="p-ans">
          <strong>Diagnostic Petrography:</strong><br>
          - <strong>Camptonite:</strong> The groundmass is dominated by crystalline laths of <strong>plagioclase feldspar</strong> (andesine/labradorite).<br>
          - <strong>Monchiquite:</strong> The groundmass is <strong>completely free of feldspar</strong>, composed instead of isotropic <strong>analcime ($\text{NaAlSi}_2\text{O}_6\cdot\text{H}_2\text{O}$)</strong>, nepheline, or devitrified hydrous volcanic glass.<br>
          <strong>Conclusion:</strong> The isotropic, feldspar-free groundmass confirms the rock is a <strong>Monchiquite</strong>.
        </div>
      </div>

      <!-- Problem 5 -->
      <div class="p-card">
        <div class="p-header">Problem 5: Tectonic Setting of Gondwana Coalfield Lamprophyre Dike Swarms</div>
        <p>
          In the Damodar Valley Gondwana coalfields (Jharia, Raniganj, Bokaro), mica-lamprophyre dikes and sills (minettes) intrude and "bake" Permian coal seams into natural coke (jhama). State the geological age of this lamprophyre magmatism and its geodynamic trigger.
        </p>
        <div class="p-ans">
          <strong>Regional Indian Geology:</strong><br>
          - <strong>Geological Age:</strong> Early Cretaceous ($\sim 115\text{--}120\text{ Ma}$, K-Ar and $^{40}\text{Ar}/^{39}\text{Ar}$ dating).<br>
          - <strong>Geodynamic Trigger:</strong> The Rajmahal-Kerguelen mantle plume event and associated rifting along the Damodar graben during the breakup of Eastern Gondwana. The lamprophyres represent deep, volatile-rich alkaline melts channelized along pre-existing basement faults.
        </div>
      </div>

      <!-- Problem 6 -->
      <div class="p-card">
        <div class="p-header">Problem 6: Viscosity and Diffusion Scaling in Panidiomorphic Growth</div>
        <p>
          Using the Stokes-Einstein equation ($D = \frac{k_B T}{6\pi \eta r}$), compare the ionic diffusivity ($D$) of silica in a dry rhyolitic melt ($\eta = 10^7\text{ Pa}\cdot\text{s}$) with that in a water-saturated lamprophyric melt ($\eta = 0.5\text{ Pa}\cdot\text{s}$) at $T = 1000^\circ\text{C}$ (1273 K).
        </p>
        <div class="p-ans">
          <strong>Diffusivity Comparison:</strong><br>
          Since $D \propto \frac{1}{\eta}$ at constant temperature and ionic radius:<br>
          $$\frac{D_{\text{lamprophyre}}}{D_{\text{rhyolite}}} = \frac{\eta_{\text{rhyolite}}}{\eta_{\text{lamprophyre}}} = \frac{10^7\text{ Pa}\cdot\text{s}}{0.5\text{ Pa}\cdot\text{s}} = \mathbf{2.0 \times 10^7}$$<br>
          <strong>Significance:</strong> Ions diffuse <strong>twenty million times faster</strong> in the low-viscosity, volatile-rich lamprophyric melt, completely explaining why crystal faces can grow unconstrained into perfect euhedral (panidiomorphic) forms.
        </div>
      </div>

      <!-- Problem 7 -->
      <div class="p-card">
        <div class="p-header">Problem 7: Optical Mineralogy: Zoned Phlogopite in Minettes</div>
        <p>
          In minette thin sections, phlogopite phenocrysts frequently exhibit spectacular reverse pleochroic rims (tetraferriphlogopite rims). Describe the optical change and explain its crystal-chemical cause.
        </p>
        <div class="p-ans">
          <strong>Crystal-Chemical Description:</strong><br>
          - <strong>Normal Phlogopite Core:</strong> Standard pleochroic scheme: absorption is greatest parallel to cleavage ($\gamma \approx \beta > \alpha$; dark brown/red-brown parallel to horizontal crosshair).<br>
          - <strong>Tetraferriphlogopite Rim:</strong> Shows <strong>abnormal / reverse pleochroism</strong>: absorption is greatest <em>perpendicular</em> to cleavage ($\alpha > \beta \approx \gamma$; dark orange-red perpendicular to cleavage, pale yellow parallel to cleavage).<br>
          - <strong>Cause:</strong> In highly oxidized, peralkaline, silica-undersaturated residual melts, aluminium is deficient, forcing ferric iron ($\text{Fe}^{3+}$) to enter the <strong>tetrahedral $Z$-sites</strong> normally reserved for $Al^{3+}$ and $Si^{4+}$.
        </div>
      </div>

      <!-- Problem 8 -->
      <div class="p-card">
        <div class="p-header">Problem 8: Lamprophyre vs. Lamproite vs. Kimberlite</div>
        <p>
          Clarify the taxonomic distinction between Lamprophyres, Lamproites, and Kimberlites, especially regarding diamond-bearing potential.
        </p>
        <div class="p-ans">
          <strong>Taxonomic Distinction (IUGS / Mitchell, 1995):</strong><br>
          - <strong>Lamprophyre (Broad Clan):</strong> Typically calc-alkaline to alkaline; contains essential plagioclase or orthoclase in groundmass; rarely diamondiferous (except ultramafic varieties like aillikites).<br>
          - <strong>Lamproite:</strong> Ultra-potassic, peralkaline volcanic/hypabyssal rock containing titanium-rich phlogopite, richterite, jeppeite, and wadeite. Can be economically diamondiferous (e.g., Argyle diamond pipe, Australia; Majhgawan pipe, Panna, India).<br>
          - <strong>Kimberlite:</strong> Inequigranular ultramafic rock containing megacrysts of picroilmenite, pyrope garnet, and olivine in a carbonate-serpentine groundmass. Primary terrestrial host of diamonds worldwide.
        </div>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 85, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q085_Lamprophyre_Panidiomorphic_Texture_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q085: {out_path} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q085()
