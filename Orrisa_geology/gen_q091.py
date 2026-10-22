#!/usr/bin/env python3
"""
Q091 Generator: Sandstone Cements & Argillaceous Sandstone Petrography
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

def generate_q091():
    title = r"Q091: Sedimentary Petrology: Sandstone Cements & Argillaceous Sandstone | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Sedimentary Petrology & Diagenesis"
    h1_title = "Q091: Sandstone Cementing Materials & Argillaceous Sandstone"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 91<br>
<strong>Authoritative References:</strong> Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th/6th Ed., Ch. 5: Sandstones, pp. 135–148; Fig. 5.10); K.M. Bangar, <em>Principles of Engineering Geology</em> (Standard Publishers, pp. 70–73, 172); F.J. Pettijohn, P.E. Potter, and R. Siever, <em>Sand and Sandstone</em> (Springer-Verlag); Maurice E. Tucker, <em>Sedimentary Petrology: An Introduction to the Origin of Sedimentary Rocks</em>."""

    part1 = r"""
  <!-- CARD 1: FUNDAMENTAL PETROGRAPHY OF SANDSTONE CEMENTS -->
  <div class="card">
    <div class="card-header bg-blue">1. Petrographic Architecture of Sandstones: Framework, Matrix, and Cement</div>
    <div class="card-body">
      <p>
        A sandstone is a clastic sedimentary rock composed of sand-sized grains ranging from <strong>$0.0625\text{ mm}$ ($1/16\text{ mm}$ or $4\phi$) to $2.0\text{ mm}$ ($-1\phi$)</strong> according to the Wentworth size scale. Microscopically and petrologically, a sandstone consists of three distinct textural components:
      </p>
      <ol>
        <li><strong>Framework Grains ($> 0.0625\text{ mm}$):</strong> Detrital mineral grains and rock fragments (primarily monocrystalline quartz, polycrystalline quartz, feldspars [K-feldspar and plagioclase], and lithic rock fragments).</li>
        <li><strong>Matrix ($< 0.03\text{ mm}$ or $< 0.0625\text{ mm}$):</strong> Fine-grained detrital interstitial material consisting of silt, clay minerals, and organic debris deposited contemporaneously with the framework grains.</li>
        <li><strong>Cement (Authigenic precipitate):</strong> Mineral material deposited chemically from pore waters within the intergranular void spaces <em>after</em> sediment deposition, during diagenesis. Cement binds the loose framework grains into a rigid, lithified rock.</li>
      </ol>

      <div class="figure-box">
        <img src="../../figures_Q91/boggs_p145_sandstone_cements_argillaceous.png" alt="Sandstone Petrography and Cements from Sam Boggs Jr.">
        <div class="figure-caption">
          <strong>Figure 91.1 — Petrographic Classification of Sandstones and Cements:</strong> Authentic textbook diagram from Sam Boggs Jr. (<em>Principles of Sedimentology and Stratigraphy</em>, p. 145). Diagram illustrating sandstone framework grains (Q-F-L ternary) and diagenetic cements (silica, carbonate, clay minerals, and iron oxides) occupying intergranular pore spaces.
        </div>
      </div>

      <h4>Classification of Sandstones Based on Cementing Material</h4>
      <p>
        Depending on the chemical composition of the pore fluids and the diagenetic environment, different minerals precipitate as cements. Sandstones are conventionally named and classified based on the nature of their primary cementing agent:
      </p>
      <ul>
        <li><strong>Argillaceous Sandstone:</strong> Sandstone in which the interstitial binding material is composed predominantly of <strong>clay minerals</strong> (kaolinite, illite, smectite, montmorillonite, or chlorite). The clay may occur as authigenic pore linings/pore fillings or as compacted detrital matrix ("pseudomatrix"). Because clay minerals have weak cohesive bonding, argillaceous sandstones are typically soft, friable, prone to rapid slaking upon water immersion, and possess poor compressive strength.</li>
        <li><strong>Siliceous Sandstone:</strong> Sandstone bound by <strong>silica ($SiO_2$)</strong>, precipitated as syntaxial quartz overgrowths in optical continuity with detrital quartz grains, or as cryptocrystalline chalcedony and microcrystalline opal. Complete silica cementation produces a tightly interlocked, non-porous rock termed <em>orthoquartzite</em> or <em>sedimentary quartzite</em>, which fractures across grains rather than around them and possesses exceptional hardness (Mohs 7) and chemical durability.</li>
        <li><strong>Calcareous Sandstone:</strong> Sandstone bound by <strong>calcium carbonate ($CaCO_3$, typically calcite or dolomite)</strong>. Calcite cement may occur as sparitic grain coatings, microcrystalline micrite, or large optically continuous crystals enveloping multiple quartz grains (termed <em>poikilotopic</em> or "lustre-mottled" cement). It readily effervesces with dilute ($10\%$) hydrochloric acid ($HCl$).</li>
        <li><strong>Ferruginous Sandstone:</strong> Sandstone bound by <strong>iron oxides or iron hydroxides</strong> (hematite $\text{Fe}_2\text{O}_3$, goethite $\alpha\text{-FeO(OH)}$, or amorphous limonite). These cements impart characteristic red, reddish-brown, yellow, or rusty brown hues to the rock.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 2: DIAGENETIC PROCESSES & CLAY CEMENTATION MECHANISMS -->
  <div class="card">
    <div class="card-header bg-emerald">2. Diagenetic Clay Mineral Genesis & Reservoir Quality Implications</div>
    <div class="card-body">
      <h4>Authigenic Clay Minerals vs. Detrital Matrix</h4>
      <p>
        In sedimentary petrology, distinguishing between detrital matrix and authigenic clay cement is critical for paleogeographic and petroleum reservoir analysis:
      </p>
      <ul>
        <li><strong>Authigenic Clay Cements:</strong> Crystallized directly from circulating pore waters during eodiagenesis and mesodiagenesis. Under the scanning electron microscope (SEM):
          <ul>
            <li><strong>Kaolinite:</strong> Forms delicate vermicular "booklets" or accordion-like stacks in open pore spaces, typically precipitating in acidic, fresh meteoric flushing conditions ($2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \rightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 + 4\text{H}_4\text{SiO}_4 + 2\text{K}^+$).</li>
            <li><strong>Illite:</strong> Forms fibrous, hairy, or ribbon-like projections bridging pore throats, causing catastrophic reductions in permeability while leaving total porosity largely unaffected.</li>
            <li><strong>Smectite / Chlorite:</strong> Precipitates as grain-coating or grain-lining honeycomb platelets that inhibit subsequent quartz overgrowth nucleation, sometimes preserving anomalously high deep-reservoir porosity.</li>
          </ul>
        </li>
        <li><strong>Detrital Clay Matrix (Wackes):</strong> Introduced during sedimentation via flocculation or muddy suspension deposition. According to Pettijohn's (1975) classification, rocks with $> 15\%$ clay matrix are designated as <strong>wackes</strong> (e.g., quartz wacke, arkosic wacke, lithic wacke / greywacke), whereas those with $< 15\%$ matrix are <strong>arenites</strong>.</li>
      </ul>

      <h4>Engineering Geology and Hydrogeological Behavior</h4>
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sandstone Type</th>
            <th>Primary Cement</th>
            <th>Unconfined Compressive Strength ($\sigma_c$)</th>
            <th>Porosity & Permeability</th>
            <th>Engineering Suitability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Argillaceous Sandstone</strong></td>
            <td>Clay minerals (illite, kaolinite, smectite)</td>
            <td>Low to Moderate ($15\text{--}50\text{ MPa}$); slakes in water</td>
            <td>Moderate porosity ($10\text{--}25\%$), very low permeability</td>
            <td>Poor foundation rock; unstable in slopes, swelling risks, slakes rapidly</td>
          </tr>
          <tr>
            <td><strong>Siliceous Sandstone</strong></td>
            <td>Quartz overgrowths, chalcedony, opal</td>
            <td>Very High ($120\text{--}250\text{ MPa}$); brittle, abrasiveness high</td>
            <td>Low porosity ($2\text{--}8\%$), low permeability</td>
            <td>Excellent concrete aggregate, railway ballast, durable dam foundation</td>
          </tr>
          <tr>
            <td><strong>Calcareous Sandstone</strong></td>
            <td>Calcite, dolomite, ankerite</td>
            <td>Moderate to High ($60\text{--}140\text{ MPa}$); acid-soluble</td>
            <td>Variable ($5\text{--}20\%$), secondary vuggy porosity possible</td>
            <td>Good building stone, but susceptible to chemical weathering and acid rain dissolution</td>
          </tr>
          <tr>
            <td><strong>Ferruginous Sandstone</strong></td>
            <td>Hematite, goethite, limonite</td>
            <td>Moderate ($40\text{--}100\text{ MPa}$)</td>
            <td>Moderate ($8\text{--}18\%$)</td>
            <td>Widely used as historical building stone and decorative dimension stone</td>
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
        <strong>Question 91:</strong> Cementing material differs in different sandstones, the sandstone where cementing material is clay is named :
      </div>
      <div class="options-grid">
        <div class="option-item"><strong>(A)</strong> Ferruginous sandstone</div>
        <div class="option-item correct-option"><strong>(B)</strong> Argillaceous sandstone</div>
        <div class="option-item"><strong>(C)</strong> Calcareous sandstone</div>
        <div class="option-item"><strong>(D)</strong> Siliceous sandstone</div>
      </div>
      <div class="verified-banner">
        Verified Correct Answer: <strong>(B) Argillaceous sandstone</strong>
      </div>
    </div>
  </div>

  <!-- FORENSIC REFUTATION OF OPTIONS -->
  <div class="card">
    <div class="card-header bg-slate">Forensic Analysis & Refutation of Options</div>
    <div class="card-body">
      <div class="option-card option-wrong">
        <div class="option-badge opt-a">Option (A) Refuted — Ferruginous Sandstone</div>
        <p>
          <strong>Incorrect:</strong> A <em>ferruginous sandstone</em> is defined specifically by an interstitial cement consisting of <strong>iron oxides or hydroxides</strong>—primarily hematite ($\text{Fe}_2\text{O}_3$), goethite ($\alpha\text{-FeO(OH)}$), or hydrated limonite. This cement imparts vivid red, brown, or ochre-yellow colors to the rock (such as in continental red beds or the Old Red Sandstone of the UK). It does not have clay as its defining cementing agent.
        </p>
      </div>

      <div class="option-card option-correct">
        <div class="option-badge opt-b">Option (B) Confirmed — Argillaceous Sandstone</div>
        <p>
          <strong>Correct:</strong> The term <em>argillaceous</em> is derived from the Latin <em>argilla</em> (meaning white clay). In sedimentary petrology and engineering geology, an <strong>argillaceous sandstone</strong> is explicitly defined as a sandstone in which the binding or interstitial cementing material consists predominantly of <strong>clay minerals</strong> (kaolinite, illite, smectite, or chlorite). Such rocks are characterized by relatively low mechanical competence, susceptibility to slaking, and poor permeability due to clay-choked pore networks.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-c">Option (C) Refuted — Calcareous Sandstone</div>
        <p>
          <strong>Incorrect:</strong> A <em>calcareous sandstone</em> is bound by <strong>calcium carbonate</strong>, predominantly calcite ($\text{CaCO}_3$) or less commonly dolomite ($\text{CaMg(CO}_3)_2$). Its diagnostic petrographic signature is effervescence when treated with cold dilute ($10\%$) hydrochloric acid ($HCl$). When calcite forms large, optically continuous poikilotopic crystals cementing hundreds of quartz grains, it exhibits "lustre-mottling." It does not contain clay as its primary cementing agent.
        </p>
      </div>

      <div class="option-card option-wrong">
        <div class="option-badge opt-d">Option (D) Refuted — Siliceous Sandstone</div>
        <p>
          <strong>Incorrect:</strong> A <em>siliceous sandstone</em> is characterized by <strong>silica ($SiO_2$)</strong> cementation. The silica precipitates from groundwater as secondary syntaxial quartz overgrowths, microcrystalline quartz, chalcedony, or amorphous opal. In advanced stages of cementation, this produces an extremely hard, dense rock (orthoquartzite) where individual sand grains fuse into an impermeable mosaic. It is distinct from clay-cemented argillaceous sandstone.
        </p>
      </div>
    </div>
  </div>
"""

    part3 = r"""
  <!-- CARD 1: COMPARISON MATRIX -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Comparison of Sandstone Cementing Types</div>
    <div class="card-body">
      <table class="table-custom">
        <thead>
          <tr>
            <th>Sandstone Category</th>
            <th>Dominant Cementing Material</th>
            <th>Chemical Formula / Mineralogy</th>
            <th>Diagnostic Field / Lab Test</th>
            <th>Distinctive Physical Properties</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Argillaceous Sandstone</strong></td>
            <td>Clay minerals / matrix</td>
            <td>Hydrous aluminosilicates (kaolinite, illite, smectite)</td>
            <td>Earthy smell when breathed on; slakes in standing water; soft under pick</td>
            <td>Friable, soft, dull appearance, prone to rapid weathering and slope failure</td>
          </tr>
          <tr>
            <td><strong>Siliceous Sandstone</strong></td>
            <td>Silica</td>
            <td>$\text{SiO}_2$ (quartz overgrowths, chalcedony, chert)</td>
            <td>Scratches glass easily (Mohs 7); no effervescence with acid; conchoidal break</td>
            <td>Extremely tough, resistant to abrasion, fractures across framework grains</td>
          </tr>
          <tr>
            <td><strong>Calcareous Sandstone</strong></td>
            <td>Carbonate</td>
            <td>$\text{CaCO}_3$ (calcite) or $\text{CaMg(CO}_3)_2$ (dolomite)</td>
            <td>Vigorous effervescence with cold $10\%\text{ HCl}$ ($2\text{HCl} + \text{CaCO}_3 \rightarrow \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2\uparrow$)</td>
            <td>Moderately durable; susceptible to acid-rain dissolution; lustre-mottling</td>
          </tr>
          <tr>
            <td><strong>Ferruginous Sandstone</strong></td>
            <td>Iron oxide / hydroxide</td>
            <td>$\text{Fe}_2\text{O}_3$ (hematite), $\text{FeO(OH)}$ (goethite, limonite)</td>
            <td>Red, brown, or yellow streak; reddish-brown coloration; heavy specific gravity</td>
            <td>Variable strength depending on cement density; excellent building stone</td>
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
        <p>A civil engineer tests a sandstone sample intended for a railway cutting slope. When submerged in a beaker of water for 24 hours, the rock disintegrates completely into loose sand grains and muddy suspension. Microscopic inspection shows the binding agent consists of hydrous aluminum silicates. Identify the sandstone type and explain the failure mechanism.</p>
        <p><strong>Solution:</strong> The rock is an <strong>argillaceous sandstone</strong>. The failure mechanism is <strong>slaking</strong>, caused by the swelling and hydration of smectite/illite clay cements. Water molecules infiltrate the expandable interlaminar layers of the clay minerals, weakening van der Waals forces and capillary meniscus suction, causing total loss of effective cohesion ($c' \rightarrow 0$) and rapid disintegration.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 2</h4>
        <p>Under a polarizing petrographic microscope, a sandstone exhibits detrital quartz grains completely surrounded by syntaxial quartz overgrowths in optical continuity. The rock fractures through the quartz grains rather than along grain boundaries. What is the precise name of this rock and its cement type?</p>
        <p><strong>Solution:</strong> The rock is a <strong>siliceous sandstone (orthoquartzite or sedimentary quartzite)</strong>. The cement is <strong>silica ($\text{SiO}_2$)</strong>, precipitated as syntaxial quartz overgrowths in crystallographic continuity with the host grains. Because the bond strength between quartz overgrowths and quartz grains equals the intrinsic tensile strength of quartz, fracture occurs intragranularly across grains.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 3</h4>
        <p>Calculate the matrix percentage of a rock with $68\%$ detrital quartz, $12\%$ K-feldspar, $5\%$ rock fragments, and $15\%$ fine silt-clay matrix. According to Pettijohn's sandstone classification, does this rock qualify as an arenite or a wacke?</p>
        <p><strong>Solution:</strong> In Pettijohn's sandstone classification, the boundary between an <strong>arenite</strong> and a <strong>wacke</strong> is defined precisely at $15\%$ matrix ($< 0.03\text{ mm}$ or $< 0.0625\text{ mm}$). Rocks with $\le 15\%$ matrix are classified as <em>arenites</em>, while rocks with $> 15\%$ (up to $75\%$) are classified as <em>wackes</em>. At exactly $15\%$, it lies on the boundary, but rocks containing $> 15\%$ are formally designated as <strong>arkosic wacke</strong> (since feldspar exceeds rock fragments, $F > L$).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 4</h4>
        <p>A petrographer applies a $10\%$ solution of cold hydrochloric acid to an unknown grey sandstone and observes instantaneous, vigorous effervescence. Thin-section staining with Alizarin Red S yields a pink/red stain across the intergranular cement. Identify the cement and the exact sandstone class.</p>
        <p><strong>Solution:</strong> The cement is <strong>calcite ($\text{CaCO}_3$)</strong>, and the rock is a <strong>calcareous sandstone</strong>. The reaction is: $\text{CaCO}_3 + 2\text{HCl} \rightarrow \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2\uparrow$. Alizarin Red S selectively stains non-ferroan calcite pink to red, confirming calcite rather than dolomite (which stains only when boiled in acid or does not stain without iron).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 5</h4>
        <p>Scanning electron microscopy (SEM) of an oil-bearing sandstone reservoir reveals dense mats of pore-bridging fibrous illite hairs. While total porosity measured by helium pycnometry remains high at $22\%$, air permeability drops drastically from $350\text{ mD}$ to $< 0.5\text{ mD}$. Explain this petrophysical paradox.</p>
        <p><strong>Solution:</strong> Fibrous illite occupies very little physical solid volume, thereby preserving the bulk storage volume of the pore bodies (high porosity $\phi = 22\%$). However, its delicate, interlocking fibrous network spans directly across the narrow <strong>pore throats</strong>, multiplying surface area, maximizing tortuosity, and creating intense frictional drag on fluid flow, causing a catastrophic collapse in permeability ($k < 0.5\text{ mD}$).</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 6</h4>
        <p>Explain how iron oxide cements originate in continental red-bed sandstones during early diagenesis (eodiagenesis) according to Walker's (1967) intrastratal alteration model.</p>
        <p><strong>Solution:</strong> According to T.R. Walker's classic model, the red pigment (hematite, $\text{Fe}_2\text{O}_3$) in continental red beds is predominantly diagenetic (authigenic) rather than detrital. In oxidizing, alkaline desert groundwaters, detrital iron-bearing ferromagnesian silicates (biotite, hornblende, augite) undergo in-situ intrastratal chemical dissolution. Dissolved ferrous iron ($Fe^{2+}$) is oxidized to ferric iron ($Fe^{3+}$) and precipitates initially as amorphous ferric hydroxide ($\text{Fe(OH)}_3$ or ferrihydrite), which subsequently ages and dehydrates over geological time into microcrystalline hematite pigment coating sand grains.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 7</h4>
        <p>What is "lustre-mottling" in sedimentary petrography, and in which specific cemented sandstone is it observed?</p>
        <p><strong>Solution:</strong> "Lustre-mottling" is a optical reflection phenomenon observed in <strong>calcareous sandstones</strong> featuring <strong>poikilotopic calcite cement</strong>. Individual optically continuous calcite crystals grow to macroscopic size ($0.5\text{ to } 2\text{ cm}$), completely engulfing hundreds of small detrital quartz grains. When the rock is turned in sunlight, the cleavage faces of the single calcite crystal reflect light simultaneously, creating glittering patches or mottled flashes of lustre.</p>
      </div>

      <div class="problem-box">
        <h4>Practice Problem 8</h4>
        <p>Contrast the unconfined compressive strength ($\sigma_c$) and durability of a siliceous sandstone vs. an argillaceous sandstone in tunnel portal construction.</p>
        <p><strong>Solution:</strong> A <strong>siliceous sandstone</strong> typically possesses an unconfined compressive strength ($\sigma_c$) between $120\text{ and } 250\text{ MPa}$, negligible slaking durability index loss ($I_{d2} > 98\%$), and exceptional shear strength, making it an outstanding, self-supporting rock mass for tunnel portals. In contrast, an <strong>argillaceous sandstone</strong> exhibits low $\sigma_c$ ($15\text{ to } 50\text{ MPa}$), high slake durability degradation ($I_{d2} < 60\%$), and develops high swelling pressures and ravelling when exposed to atmospheric humidity and water seepage, requiring immediate shotcreting, rock bolting, and steel ribs.</p>
      </div>
    </div>
  </div>
"""

    html = wrap_html(
        q_num=91,
        title=title,
        badge=badge,
        h1_title=h1_title,
        meta_text=meta_text,
        part1_content=part1,
        part2_content=part2,
        part3_content=part3
    )

    out_file = os.path.join(SOLUTIONS_DIR, "Q091_Argillaceous_Sandstone_Clay_Cement_Complete_Guide.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q091: {out_file} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_q091()
