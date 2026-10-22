#!/usr/bin/env python3
"""
Q116 Generator: Granulite Facies, Charnockite Suite & Hypersthene Granite
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q116():
    title = r"Q116: Metamorphic Petrology: Granulite Facies & Charnockite Suite | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Metamorphic Petrology & Granulites"
    h1_title = "Q116: The Charnockite Suite: Granulite Facies Quartzo-Feldspathic Rocks & Hypersthene Metamorphism"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 116<br>
<strong>Authoritative References:</strong> John D. Winter, <em>Principles of Igneous and Metamorphic Petrology</em> (2nd Ed., Ch. 25: Granulite Facies / Charnockites, pp. 492–496; Fig. 25.5); Thomas H. Holland (1900), <em>The Charnockite Series: A Group of Archaean Hypersthenic Rocks in Peninsular India</em> (Memoirs of the GSI, Vol. 28); K.M. Bangar, <em>Principles of Engineering Geology</em> (pp. 87–90, 185); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 140–141)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND ETYMOLOGY OF CHARNOCKITE -->
  <div class="card">
    <div class="card-header bg-blue">1. Definition, History & Petrographic Framework of the Charnockite Suite</div>
    <div class="card-body">
      <p>
        The term <strong>charnockite</strong> holds a celebrated position in Indian and global petrology. It was introduced in 1893 and formally established in 1900 by Sir Thomas Henry Holland of the Geological Survey of India, named in honor of <strong>Job Charnock</strong> (the traditional founder of Calcutta), whose tombstone in St. John's Churchyard, Kolkata, was carved from a distinctive dark hypersthenic rock quarried from St. Thomas Mount in Pallavaram, Chennai (Madras).
      </p>
      <p>
        In modern metamorphic and igneous classification (IUGS; Winter, 2014, pp. 492–496), <strong>charnockite</strong> (sensu stricto) is formally defined as a <strong>hypersthene-bearing granite</strong>—a quartzo-feldspathic plutonic or high-grade metamorphic rock formed under dry, anhydrous <strong>Granulite Facies</strong> conditions, characterized by the pathognomonic coexistence of <strong>orthopyroxene (hypersthene / enstatite)</strong> with quartz, alkali feldspar (perthite/microcline), and plagioclase.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q116/winter_p493_granulite_facies_charnockite_hypersthene.png" alt="Granulite Facies and Charnockite Stability from John D. Winter">
        <div class="figure-caption">
          <strong>Figure 116.1 — Granulite Facies Phase Equilibria and the Charnockite Suite:</strong> Authentic textbook diagram from John D. Winter (<em>Principles of Igneous and Metamorphic Petrology</em>, p. 493). Shows the high-temperature anhydrous breakdown of hydrous biotite and hornblende into orthopyroxene (hypersthene) + K-feldspar + quartz, defining the granulite facies charnockitic domain.
        </div>
      </div>

      <h4>Diagnostic Petrographic Features of Charnockite</h4>
      <ul>
        <li><strong>Hypersthene Orthopyroxene:</strong> The defining ferromagnesian mineral, exhibiting unmistakable pleochroism under plane-polarized light (PPL): <strong>$X = \text{pink/pale red}$, $Y = \text{yellowish-brown}$, $Z = \text{pale green}$</strong>, with straight (parallel) extinction and low birefringence.</li>
        <li><strong>Greasy, Dark Appearance ("Charnockite Look"):</strong> Macroscopically, charnockite displays a highly distinctive, dark, resinous, dark greenish-grey to olive-brown greasy luster, often causing hand specimens of felsic granite to be mistaken for mafic gabbros. Microscopically, this color is caused by sub-micron liquid $\text{CO}_2$ fluid inclusions and exsolution lamellae within quartz and feldspar lattices.</li>
        <li><strong>Perthitic Feldspar & Blue Quartz:</strong> Abundant coarse microperthite or antiperthite, alongside quartz that frequently displays a pale bluish, smoky, or opalescent chatoyance due to sub-microscopic rutile needles.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: PETROGENESIS & CO2 FLUSHING -->
  <div class="card">
    <div class="card-header bg-emerald">2. Granulite Petrogenesis: Dehydration Melting vs. Carbonic Metamorphism</div>
    <div class="card-body">
      <h4>The Dehydration Reaction Generating Hypersthene</h4>
      <p>
        In the lower continental crust ($T = 750\text{--}900^\circ\text{C}, P = 6\text{--}10\text{ kbar}$), hydrous biotite mica breaks down in the presence of quartz via the classic granulite dehydration reaction:
      </p>
      $$\text{K(Mg,Fe)}_3\text{AlSi}_3\text{O}_{10}(\text{OH})_2\text{ (Biotite)} + 3\text{SiO}_2\text{ (Quartz)} \xrightarrow{\Delta T} 3\mathbf{\text{(Mg,Fe)SiO}_3\text{ (Hypersthene)}} + \text{KAlSi}_3\text{O}_8\text{ (K-feldspar)} + \text{H}_2\text{O}\uparrow$$
      <p>
        The liberation of orthopyroxene (hypersthene) marks the terminal destruction of amphibolite-facies hydrous assemblages and entry into the granulite facies charnockite suite.
      </p>

      <h4>The "Charnockite in the Making" Phenomenon (Kabbaldurga, Karnataka)</h4>
      <p>
        In southern India (Kabbaldurga quarry), Pichamuthu (1960) and Janardhan et al. (1979) discovered patchy, in-situ conversions of grey amphibolite-facies Peninsular Gneiss into greasy, brown charnockite along fracture networks. This landmark discovery demonstrated that charnockitization can occur via <strong>carbonic metamorphism</strong>: influx of mantle-derived, supercritical carbon dioxide ($\text{CO}_2$) flushes through ductile fractures, driving water activity to very low levels ($a_{\text{H}_2\text{O}} \ll 0.1$), thereby dehydrating biotite and hornblende into hypersthene at subsolidus temperatures.
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
        <strong>Question 116:</strong> Granulite facies quartzo-feldspathic plutonic rocks characterized by the presence of hypersthenes often designated as :
      </div>
      <div class="options-grid">
        <div class="option-item correct-option"><strong>(A)</strong> Charnockite</div>
        <div class="option-item"><strong>(B)</strong> Orthoamphibolite</div>
        <div class="option-item"><strong>(C)</strong> Paramphibolite</div>
        <div class="option-item"><strong>(D)</strong> Greenalite</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(A) Charnockite</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-correct">
        <div class="option-badge opt-a">Option (A) Confirmed — Charnockite</div>
        <p>
          <strong>Correct:</strong> By universal scientific definition in igneous and metamorphic petrology (Holland, 1900; Winter, 2014, p. 493; Bangar, p. 87; Mahapatra, p. 140), <strong>charnockite</strong> is the exact and authoritative name for granulite-facies quartzo-feldspathic plutonic and metamorphic rocks characterized fundamentally by the presence of <strong>orthopyroxene (hypersthene)</strong>.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Orthoamphibolite</div>
        <p>
          <strong>Incorrect:</strong> An <strong>orthoamphibolite</strong> is a metamorphic rock formed by the medium-grade (amphibolite facies) metamorphism of an <strong>igneous mafic protolith</strong> (such as basalt, dolerite, or gabbro). It is composed predominantly of green-to-black <strong>hornblende amphibole and calcic plagioclase</strong>. It is mafic (not quartzo-feldspathic), belongs to the amphibolite facies (not granulite facies), and is characterized by amphibole rather than hypersthene.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Paramphibolite</div>
        <p>
          <strong>Incorrect:</strong> A <strong>paramphibolite</strong> is an amphibolite-facies rock derived from the metamorphism of a <strong>sedimentary protolith</strong> (such as a calcareous shale, marl, or impure dolomitic mudstone). Like orthoamphibolite, it is dominated by hornblende and plagioclase, entirely distinct from hypersthene-bearing charnockite.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Greenalite</div>
        <p>
          <strong>Incorrect:</strong> <strong>Greenalite</strong> is a specific, hydrous iron silicate mineral belonging to the serpentine group ($\text{Fe}^{2+}_3\text{Si}_2\text{O}_5(\text{OH})_4$). It occurs as microscopic green ooids and peloids in unmetamorphosed or low-grade Precambrian banded iron formations (BIFs). It is neither a rock type nor associated with granulite-facies charnockites.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Classification of the Charnockite Series (IUGS)</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Charnockite Series Member</th>
            <th>Plutonic Equivalence</th>
            <th>Essential Mineralogy</th>
            <th>$\text{SiO}_2$ Range</th>
            <th>Color Index ($M'$)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Charnockite (sensu stricto)</strong></td>
            <td>Hypersthene Granite</td>
            <td>Quartz + K-feldspar (perthite) + Plagioclase + Hypersthene</td>
            <td>$> 70\text{ wt}\%$ (Felsic / Acidic)</td>
            <td>$< 10\text{--}15$ (Leucocratic)</td>
          </tr>
          <tr>
            <td><strong>Enderbite</strong></td>
            <td>Hypersthene Tonalite / Granodiorite</td>
            <td>Quartz + Plagioclase (dominant over K-feldspar) + Hypersthene</td>
            <td>$65\text{--}72\text{ wt}\%$ (Felsic)</td>
            <td>$10\text{--}20$</td>
          </tr>
          <tr>
            <td><strong>Opdalite / Mangerite</strong></td>
            <td>Hypersthene Granodiorite / Monzonite</td>
            <td>Plagioclase + K-feldspar (subequal) + Quartz + Hypersthene $\pm$ Diopside</td>
            <td>$60\text{--}66\text{ wt}\%$ (Intermediate)</td>
            <td>$15\text{--}30$ (Mesocratic)</td>
          </tr>
          <tr>
            <td><strong>Norite (Basic Charnockite)</strong></td>
            <td>Hypersthene Gabbro</td>
            <td>Calcic Plagioclase + Hypersthene + Augite / Diopside (Quartz absent)</td>
            <td>$48\text{--}54\text{ wt}\%$ (Basic / Mafic)</td>
            <td>$> 40\text{--}70$ (Melanocratic)</td>
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
        <p>Under a petrographic microscope, how does a geologist definitively identify hypersthene in a charnockite thin section, distinguishing it from clinopyroxene (augite)?</p>
        <p><strong>Solution:</strong>
          - <strong>Hypersthene (Orthopyroxene):</strong> Orthorhombic ($Pbca$); exhibits diagnostic <strong>vivid trichroic pleochroism</strong> ($X = \text{pink/salmon red}$, $Y = \text{yellowish}$, $Z = \text{pale green}$), <strong>parallel (straight) extinction ($0^\circ$)</strong> relative to the $\{110\}$ cleavage in prismatic sections, and low first-order birefringence ($\delta \approx 0.010\text{--}0.015$).
          - <strong>Augite (Clinopyroxene):</strong> Monoclinic ($C2/c$); exhibits pale green color without strong pink pleochroism, <strong>inclined extinction ($Z \wedge c = 38\text{--}48^\circ$)</strong>, and much higher upper second-order birefringence ($\delta \approx 0.025$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>What is an "enderbite" and how does its modal feldspar proportion differ from charnockite sensu stricto?</p>
        <p><strong>Solution:</strong>
          In the charnockite series, an <strong>enderbite</strong> (named after Enderby Land, Antarctica) is the hypersthene-bearing equivalent of a <strong>tonalite</strong>. In charnockite sensu stricto, alkali feldspar (K-feldspar/perthite) is dominant or subequal to plagioclase. In enderbite, <strong>plagioclase feldspar (typically oligoclase/andesine, $\text{An}_{25\text{--}40}$) constitutes $> 65\text{ to } 90\%$</strong> of the total feldspar volume, with K-feldspar reduced to an accessory phase.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Explain the role of carbon dioxide ($\text{CO}_2$) flushing in lowering water activity ($a_{\text{H}_2\text{O}}$) during the genesis of charnockites in southern India.</p>
        <p><strong>Solution:</strong>
          Under normal fluid-present conditions, granitic crust melts at $650^\circ\text{C}$ in the presence of pure $\text{H}_2\text{O}$ ($a_{\text{H}_2\text{O}} = 1.0$). In southern India (Eastern Ghats and Southern Granulite Terrane), juvenile mantle degassing or deep basaltic underplating introduced large volumes of supercritical $\text{CO}_2$. Because $\text{CO}_2$ is immiscible with silicate melt and displaces water, water activity plummeted to <strong>$a_{\text{H}_2\text{O}} \le 0.1\text{ to } 0.3$</strong>. This severe dehydration stabilized orthopyroxene (hypersthene) at high temperatures ($800\text{--}900^\circ\text{C}$) without inducing pervasive large-scale anatectic melting.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Why do charnockites frequently display a dark, greasy olive-brown macroscopic color even when their chemical composition is $75\%\text{ SiO}_2$ (felsic granite)?</p>
        <p><strong>Solution:</strong>
          The dark, greasy appearance is an optical absorption effect. At granulite facies conditions, extreme thermal and fluid pressure generates billions of <strong>sub-micron inclusions of liquid $\text{CO}_2$</strong>, microscopic cryptocrystalline graphite films, and ultra-fine iron oxide/rutile exsolution lamellae dispersed within the crystal lattices of quartz and feldspar. These micro-inclusions scatter and absorb incident light internally, mimicking the dark visual appearance of a mafic rock.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>What is a "khondalite" and what is its regional geological relationship with charnockites in the Eastern Ghats Mobile Belt of Odisha?</p>
        <p><strong>Solution:</strong>
          A <strong>khondalite</strong> (named by T.L. Walker after the Khond tribes of Odisha) is a high-grade <strong>garnet-sillimanite-graphite metapelitic schist/gneiss</strong> ($\pm\text{ quartz, K-feldspar}$). In the Eastern Ghats Mobile Belt of Odisha and Andhra Pradesh, khondalites represent the aluminous sedimentary cover sequence (metapelites) that was co-metamorphosed with intrusive and basement charnockites under ultra-high-temperature (UHT) granulite-facies conditions ($T > 900\text{--}1000^\circ\text{C}$).
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>State the mineralogical difference between an "amphibolite" and a "two-pyroxene granulite" (basic charnockite) derived from the exact same basaltic protolith.</p>
        <p><strong>Solution:</strong>
          - <strong>Amphibolite (Amphibolite Facies, $T \approx 500\text{--}650^\circ\text{C}$):</strong> Dominated by hydrous calcic <strong>hornblende + plagioclase</strong> $\pm$ quartz $\pm$ almandine garnet.
          - <strong>Two-Pyroxene Granulite (Granulite Facies, $T > 750^\circ\text{C}$):</strong> Hornblende has completely dehydrated via the reaction: $\text{Hornblende} + \text{Quartz} \rightarrow \mathbf{\text{Hypersthene (Opx)}} + \mathbf{\text{Diopside/Augite (Cpx)}} + \text{Plagioclase} + \text{H}_2\text{O}$.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Why are charnockites considered premier dimension stones and heavy railway ballast materials in civil engineering?</p>
        <p><strong>Solution:</strong>
          Because charnockites crystallized under extreme granulite pressures ($P > 7\text{--}9\text{ kbar}$), their constituent quartz, feldspar, and pyroxene crystals form an ultra-dense, completely interlocking granoblastic mosaic with <strong>virtually zero porosity ($< 0.2\%$)</strong> and no planar cleavage planes. This imparts exceptional unconfined compressive strength ($\sigma_c > 200\text{--}300\text{ MPa}$), high abrasion resistance, and negligible water absorption, making them superior to standard granites for railway ballast and polished monument facings.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>What is "leptynite" and how is it related to charnockite in Indian geology?</p>
        <p><strong>Solution:</strong>
          A <strong>leptynite</strong> is a light-colored, leucocratic granulite composed of quartz, microperthitic K-feldspar, and pink almandine-pyrope garnet, with <strong>orthopyroxene (hypersthene) being completely absent or retrogressed</strong>. In the Eastern Ghats and Tamil Nadu, leptynites form by the retrograde hydration or garnet-consuming recrystallization of charnockite along shear zones.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=116,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q116_Granulite_Facies_Charnockite_Hypersthene_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q116: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q116()
