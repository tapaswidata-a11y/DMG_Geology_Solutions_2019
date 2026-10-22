#!/usr/bin/env python3
"""
Q104 Generator: Conglomerates & Rudaceous Sedimentary Rocks Petrography
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q104():
    title = r"Q104: Sedimentary Petrology: Conglomerates & Rudaceous Rocks | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Classification"
    h1_title = "Q104: Conglomerate Petrography: Rudaceous Grain-Size Classification, Fabric & Provenance"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 104<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Conglomerates and Breccias, pp. 132–136; Fig. 5.3); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 67–70, 169); G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 142–146); F.J. Pettijohn, <em>Sedimentary Rocks</em> (3rd Ed., Harper & Row)."""

    part1 = r"""
  <!-- CARD 1: DEFINITION AND GRAIN-SIZE ARCHITECTURE OF RUDACEOUS ROCKS -->
  <div class="card">
    <div class="card-header bg-blue">1. Wentworth Grain-Size Scale & The Rudaceous (Psephitic) Classification</div>
    <div class="card-body">
      <p>
        In clastic sedimentary petrology (Boggs, 2014, pp. 132–136; Bangar, p. 67; Mahapatra, p. 142), sedimentary rocks are systematically divided into three broad textural categories according to the physical diameter of their predominant framework particles:
      </p>
      <ol>
        <li><strong>Rudaceous (Psephitic) Rocks:</strong> Coarse-grained clastic sedimentary rocks composed predominantly of gravel-sized clasts possessing diameters <strong>greater than $2.0\text{ mm}$ ($-1\phi$)</strong>, extending across granules ($2\text{--}4\text{ mm}$), pebbles ($4\text{--}64\text{ mm}$), cobbles ($64\text{--}256\text{ mm}$), and boulders ($> 256\text{ mm}$).</li>
        <li><strong>Arenaceous (Psammitic) Rocks:</strong> Medium-grained clastic rocks composed of sand-sized particles ranging from <strong>$0.0625\text{ mm}$ ($1/16\text{ mm}$, $+4\phi$) to $2.0\text{ mm}$ ($-1\phi$)</strong>, exemplified by sandstones.</li>
        <li><strong>Argillaceous (Pelitic) Rocks:</strong> Fine-grained clastic rocks composed of silt and clay particles smaller than <strong>$0.0625\text{ mm}$ ($+4\phi$)</strong>, exemplified by shales, mudstones, and claystones.</li>
      </ol>
      <p>
        Within the rudaceous division, a <strong>conglomerate</strong> is formally defined as an indurated rudaceous rock wherein the gravel-sized framework clasts are predominantly <strong>rounded to sub-rounded</strong>, distinguished from a <strong>breccia</strong> wherein the clasts are sharply angular.
      </p>

      <div class="figure-box">
        <img src="../../figures_Q104/boggs_p134_conglomerates_rudaceous_rocks.png" alt="Classification and Fabric of Conglomerates from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 104.1 — Textural Classification and Petrography of Conglomerates:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 134). Illustrates the structural fabrics of rudaceous rocks: Clast-supported (orthoconglomerate) vs. Matrix-supported (paraconglomerate / diamictite), alongside oligomictic and polymictic compositional variations.
        </div>
      </div>

      <h4>Etymological Origins of Clastic Terminology</h4>
      <p>
        Geological terminology preserves parallel pairs derived from Latin and Classical Greek:
      </p>
      <ul>
        <li><strong>Rudaceous:</strong> Derived from the Latin <em>rudus</em>, meaning "rubble, crushed stone, or broken stones." Its Greek equivalent is <strong>psephitic</strong> (from $\psi\tilde{\eta}\phi\omicron\varsigma$, <em>psephos</em>, meaning pebble).</li>
        <li><strong>Arenaceous:</strong> Derived from the Latin <em>arena</em>, meaning "sand." Greek equivalent: <strong>psammitic</strong> (from $\psi\acute{\alpha}\mu\mu\omicron\varsigma$, <em>psammos</em>).</li>
        <li><strong>Argillaceous:</strong> Derived from the Latin <em>argilla</em>, meaning "clay." Greek equivalent: <strong>pelitic</strong> (from $\pi\eta\lambda\acute{o}\varsigma$, <em>pelos</em>).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: PETROGRAPHIC CLASSIFICATION OF CONGLOMERATES -->
  <div class="card">
    <div class="card-header bg-emerald">2. Petrographic Classification: Fabric, Composition & Depositional Mechanics</div>
    <div class="card-body">
      <h4>Classification Based on Clast-Matrix Fabric</h4>
      <ul>
        <li><strong>Orthoconglomerate (Clast-Supported):</strong> The gravel clasts touch one another in a three-dimensional framework, with interstitial voids filled by sand/silt matrix and authigenic cement. Matrix content is <strong>$< 15\%$</strong>. Formed by high-energy, fluid-traction currents (torrential braided river bars, wave-dominated marine beaches) where turbulent water winnows out fine sediment during gravel rolling.</li>
        <li><strong>Paraconglomerate (Matrix-Supported / Diamictite):</strong> The gravel clasts are completely dispersed and "float" within an abundant, fine-grained muddy or sandy matrix without touching. Formed by cohesive, non-turbulent mass flows (subaerial debris flows, subaqueous lahars, or glacial ice transport yielding <em>tillites</em>).</li>
      </ul>

      <h4>Classification Based on Clast Compositional Variety</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Category</th>
            <th>Clast Composition</th>
            <th>Hydrodynamic / Climatic Significance</th>
            <th>Typical Geological Setting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Oligomictic (Monomictic) Conglomerate</strong></td>
            <td>Single ultra-resistant rock type ($> 90\%$; e.g., vein quartz, quartzite, or chert)</td>
            <td>Supermature; prolonged intense chemical weathering and long-distance fluvial/beach abrasion.</td>
            <td>Transgressive basal conglomerates resting on regional unconformities (e.g., Eparchean unconformity).</td>
          </tr>
          <tr>
            <td><strong>Polymictic (Petromictic) Conglomerate</strong></td>
            <td>Diverse mixture of unstable rock types (basalt, granite, limestone, schist, shale)</td>
            <td>Immature; rapid erosion, violent tectonic uplift, short transport distances.</td>
            <td>Syn-orogenic alluvial fans, fault scarps, molasse wedges (e.g., Siwalik Boulder Conglomerate).</td>
          </tr>
          <tr>
            <td><strong>Intraformational Conglomerate</strong></td>
            <td>Clasts eroded from within the same sedimentary basin (e.g., desiccation-cracked mud chips, "edgewise" flat-pebble conglomerates)</td>
            <td>Brief subaerial exposure or storm rip-up of semi-consolidated seafloor mud.</td>
            <td>Intertidal mudflats, shallow carbonate shelf tempestites.</td>
          </tr>
          <tr>
            <td><strong>Extraformational Conglomerate</strong></td>
            <td>Clasts derived from outside the basin of deposition (eroded from older highlands)</td>
            <td>Regional geological provenance and tectonic unroofing.</td>
            <td>Fluvial valleys, alluvial fans, marine delta systems.</td>
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
        <strong>Question 104:</strong> Conglomerate belongs to which type of sedimentary rocks ?
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Argillaceous</div>
        <div class="option-item"><strong>(B)</strong> Arenaceous</div>
        <div class="option-item correct-option"><strong>(C)</strong> Rudaceous</div>
        <div class="option-item"><strong>(D)</strong> Both (B) and (C) are correct</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(C) Rudaceous</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Argillaceous</div>
        <p>
          <strong>Incorrect:</strong> <strong>Argillaceous</strong> (pelitic) sedimentary rocks are defined strictly by a fine grain size of <strong>$< 0.0625\text{ mm}$ ($< 1/16\text{ mm}$)</strong>, consisting of micro-particles of silt and clay minerals. Prominent examples include shale, mudstone, and claystone. Because conglomerates are composed predominantly of coarse pebbles, cobbles, and boulders ($> 2.0\text{ mm}$), classifying a conglomerate as argillaceous is diametrically opposed to physical sedimentary definitions.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-b">Option (B) Refuted — Arenaceous</div>
        <p>
          <strong>Incorrect:</strong> <strong>Arenaceous</strong> (psammitic) sedimentary rocks are medium-grained clastic rocks whose framework grains fall strictly in the sand-size range: <strong>$0.0625\text{ mm to } 2.0\text{ mm}$</strong> (such as quartz arenites, arkoses, and greywackes). While a conglomerate may contain minor interstitial sand matrix filling the voids between large pebbles, the defining framework clasts that give the rock its name and lithological identity are gravel clasts ($> 2\text{ mm}$). Therefore, conglomerate is not an arenaceous rock.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-c">Option (C) Confirmed — Rudaceous</div>
        <p>
          <strong>Correct:</strong> By universal scientific definition in sedimentary geology (Boggs, 2014, p. 132; Bangar, p. 67; Mahapatra, p. 142), <strong>conglomerate</strong> is the archetype of <strong>rudaceous (psephitic) sedimentary rocks</strong>—coarse-grained clastic rocks consisting predominantly of rounded or sub-rounded gravel-sized clasts larger than <strong>$2.0\text{ mm}$</strong> (up to boulders $> 256\text{ mm}$) cemented by a finer matrix and chemical cement.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Both (B) and (C) are Correct</div>
        <p>
          <strong>Incorrect:</strong> Because arenaceous rocks and rudaceous rocks are mutually exclusive grain-size divisions separated by the canonical $2.0\text{ mm}$ Wentworth boundary, a conglomerate cannot simultaneously belong to both classes. Option (D) is a distractor; the sole correct classification is <strong>(C) Rudaceous</strong>.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Textural & Engineering Comparison of Clastic Sedimentary Rock Groups</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Clastic Division</th>
            <th>Wentworth Grain-Size Range</th>
            <th>Defining Rock Types</th>
            <th>Hydrodynamic Energy of Deposition</th>
            <th>Engineering Characteristics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Rudaceous (Psephitic)</strong></td>
            <td><strong>$> 2.0\text{ mm}$ ($-1\phi$ to $< -8\phi$)</strong></td>
            <td><strong>Conglomerate</strong> (rounded clasts)<br><strong>Breccia</strong> (angular clasts)</td>
            <td>Extremely high energy: Torrential flash floods, wave surf, glacial debris flows</td>
            <td>High unconfined compressive strength when cemented by silica/calcite; excellent aggregate if unweathered.</td>
          </tr>
          <tr>
            <td><strong>Arenaceous (Psammitic)</strong></td>
            <td>$0.0625\text{ to } 2.0\text{ mm}$ ($+4\phi\text{ to } -1\phi$)</td>
            <td>Sandstone (Quartz arenite, Arkose, Lithic sandstone, Greywacke)</td>
            <td>Moderate to high energy: Fluvial river bars, desert dunes, beach foreshores</td>
            <td>Primary petroleum/groundwater reservoir rocks; variable strength ($15\text{--}200\text{ MPa}$).</td>
          </tr>
          <tr>
            <td><strong>Argillaceous (Pelitic)</strong></td>
            <td>$< 0.0625\text{ mm}$ ($> +4\phi\text{ to } > +8\phi$)</td>
            <td>Shale, Siltstone, Mudstone, Claystone</td>
            <td>Low to zero energy: Quiet water suspension settling in deep marine/lakes</td>
            <td>Low compressive strength; high slaking susceptibility; impermeable cap rocks and aquitards.</td>
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
        <p>A civil engineer evaluates an outcrop containing $60\%$ rounded quartzite cobbles ($64\text{ to } 128\text{ mm}$ diameter) in point contact, with the interstitial spaces filled by coarse quartz sand cemented by syntaxial silica. Classify this rock texturally, state its fabric, and evaluate its suitability as aggregate for high-strength concrete.</p>
        <p><strong>Solution:</strong>
          - <strong>Classification:</strong> <strong>Rudaceous clastic rock</strong>, specifically an <strong>oligomictic orthoconglomerate</strong> (quartz-pebble conglomerate).
          - <strong>Fabric:</strong> <strong>Clast-supported (framework supported)</strong>.
          - <strong>Suitability:</strong> Because the clasts and cement consist entirely of chemically inert, mechanically hard quartz ($\text{SiO}_2$), this rock possesses exceptional unconfined compressive strength ($> 150\text{ MPa}$), high abrasion resistance, and negligible Los Angeles Abrasion loss ($< 15\%$), making it an <strong>outstanding aggregate for high-strength concrete</strong>.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Explain why basal conglomerates are almost universally oligomictic (composed almost exclusively of vein quartz and quartzite pebbles) rather than polymictic.</p>
        <p><strong>Solution:</strong>
          Basal conglomerates mark a major transgressive marine unconformity where rising sea levels slowly transgress across an ancient peneplained continental landmass. The shoreline surf zone spends hundreds of thousands of years relentlessly rolling and abrading the weathered regolith. Under such sustained mechanical pounding and wave reworking, all mechanically weak and chemically unstable rocks (granite, basalt, schist, limestone) are ground down and disintegrated into sand and mud, leaving only the ultra-durable, indestructible clasts—<strong>vein quartz and quartzite</strong>—to form an oligomictic quartz-pebble conglomerate.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>What is a "tillite" in sedimentology, and why is it classified as a paraconglomerate rather than an orthoconglomerate?</p>
        <p><strong>Solution:</strong>
          A <strong>tillite</strong> is a lithified glacial till deposited directly by glacial ice without subsequent fluvial sorting (e.g., the Talcher boulder bed of the Gondwana Supergroup). Glacial ice is an ultra-viscous, non-turbulent transport medium that carries all grain sizes simultaneously without sorting. Consequently, the resulting rock exhibits a <strong>matrix-supported (paraconglomerate) fabric</strong>, where unsorted, striate-faceted boulders and cobbles "float" isolated inside an abundant, fine-grained rock-flour mudstone matrix.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>Define "imbrication" in rudaceous conglomerates and explain how it is used to determine ancient river paleoflow directions.</p>
        <p><strong>Solution:</strong>
          <strong>Imbrication</strong> is a preferred primary depositional orientation of discoid or blade-shaped gravel clasts in a fluvial riverbed. Strong hydrodynamic currents tilt the pebbles such that their long ($a$-) and intermediate ($b$-) planes <strong>dip systematically upstream into the oncoming current</strong> (shingled arrangement) to minimize fluid drag. Therefore, the direction of maximum downward dip of the imbricated pebbles points directly toward the upstream provenance, allowing geologists to deduce the ancient paleocurrent vector.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Contrast an "intraformational conglomerate" with an "extraformational conglomerate" in terms of transport distance and energy source.</p>
        <p><strong>Solution:</strong>
          - <strong>Intraformational Conglomerate:</strong> Clasts originate from within the depositional basin itself (e.g., ripped-up, semi-lithified mudflats or carbonate hardgrounds during storm surges). Transport distance is <strong>extremely short (meters to tens of meters)</strong>.
          - <strong>Extraformational Conglomerate:</strong> Clasts originate from external bedrock highlands outside the basin boundaries and are transported tens to hundreds of kilometers by high-energy fluvial rivers or glacial systems into the basin.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Calculate the Wentworth phi ($\phi$) value of a pebble with a diameter of exactly $8.0\text{ mm}$.</p>
        <p><strong>Solution:</strong>
          The Wentworth phi conversion formula is:
          $$\phi = -\log_2(d_{\text{mm}})$$
          For $d = 8.0\text{ mm} = 2^3\text{ mm}$:
          $$\phi = -\log_2(2^3) = -3.0\phi$$
          Therefore, an $8.0\text{ mm}$ gravel clast corresponds to exactly <strong>$-3.0\phi$</strong> on the logarithmic Wentworth scale.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>Why do geologists refer to the Siwalik Upper Boulder Conglomerate as a "syn-orogenic" polymictic rudite?</p>
        <p><strong>Solution:</strong>
          The Upper Siwalik Boulder Conglomerate was deposited during the Pleistocene epoch contemporaneously with the intense, active tectonic collision and rapid uplift of the Higher and Lesser Himalayas (syn-orogenic). The towering topographic relief and steep river gradients drove violent torrential outwash that shed enormous, unsorted gravels containing diverse rock types—granites, quartzites, phyllites, schists, and basic volcanic rocks (polymictic petromictic suite)—into the subsiding Himalayan foreland basin.
        </p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>In geotechnical tunneling, why does an uncemented or poorly cemented gravel bed (loose rudaceous deposit) represent a hazardous "running ground" condition?</p>
        <p><strong>Solution:</strong>
          Because gravel clasts ($> 2\text{ mm}$) possess zero cohesion ($c' = 0$) and rely entirely on intergranular frictional interlocking ($\phi'$), excavating a tunnel face removes lateral confining support. When unconfined or subjected to water seepage pressure, the loose gravel and sand matrix spontaneously fluidize and collapse, pouring into the tunnel heading as a catastrophic <strong>"running ground" or chimney cave-in</strong>, which can propagate all the way to the ground surface.
        </p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=104,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q104_Conglomerate_Rudaceous_Sedimentary_Rock_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q104: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q104()
