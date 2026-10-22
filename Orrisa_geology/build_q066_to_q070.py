#!/usr/bin/env python3
"""
Masterclass Builder for Batch 5D: Micropaleontology, Anthropoids & Invertebrate Phyla (Q066 - Q070)
Elevates all guides to the full Assam DGMS 2019 masterclass standard.
"""
import os
from build_batch1_masterclass import wrap_html, SOLUTIONS_DIR

# ==============================================================================
# Q066: Foraminifera: Heterotrophic Amoeboid Protists
# ==============================================================================
def generate_q066():
    title = r"Q066: Micropaleontology: Foraminifera as Heterotrophic Rhizopodial Protists | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Micropaleontology & Protistan Biology"
    h1_title = "Q066: Foraminifera: Heterotrophic Amoeboid Protists"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 66<br>
<strong>Authoritative References:</strong> Howard A. Armstrong & Martin D. Brasier, <em>Microfossils</em> (2nd Ed., Blackwell, Ch. 11: Foraminifera, pp. 142–186); Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (Ch. 11, p. 389); Bilal U. Haq & Anne Boersma, <em>Introduction to Marine Micropaleontology</em> (Elsevier, Ch. 2); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: FORAMINIFERAL BIOLOGY AND NUTRITION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Biological Nature of Foraminifera: Heterotrophic Phagotrophy</div>
    <div class="card-body">
      <p>In biological taxonomy and micropaleontology, the <strong>Foraminifera</strong> (Order Foraminiferida, Phylum Granuloreticulosa / Rhizopoda) are a vast, ubiquitous group of single-celled, test-bearing eukaryotic microorganisms that have dominated marine benthic and planktonic ecosystems from the Cambrian to the present day:</p>

      <ul>
        <li><strong>Heterotrophic Mode of Life:</strong> By fundamental physiological definition, Foraminifera are strictly <strong>heterotrophic organisms</strong>. Being protozoans (animal-like single-celled eukaryotes), they cannot synthesize their own organic molecules from inorganic carbon dioxide and water (i.e., they are incapable of independent autotrophy).</li>
        <li><strong>Reticulopodial Feeding Mechanics:</strong> Foraminifera feed by extending an active, dynamic network of branching, anastomosing cytoplasmic threads called <strong>reticulopodia (granuloreticulopodia)</strong> through test apertures and wall pores. These sticky pseudopodia exhibit bidirectional cytoplasmic streaming, capturing live prey (diatoms, dinoflagellates, bacteria, ciliates, and micro-invertebrates like copepods) and digesting them via external and internal phagocytosis.</li>
        <li><strong>The Endosymbiont Phenomenon:</strong> While many shallow-water photic-zone foraminifera (e.g., modern *Amphistegina*, *Peneroplis*, and ancient *Nummulites*) harbor photosynthetic microalgal endosymbionts (zooxanthellae, chlorophytes, diatoms) that contribute metabolic energy via mixotrophy, the host foraminiferal organism itself remains unequivocally <strong>heterotrophic</strong>.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q66/foraminifera_rhizopodial_feeding_heterotrophic.png" alt="Foraminifera Reticulopodial Feeding">
        <div class="tb-caption">
          <strong>Figure 66.1 (Armstrong & Brasier 2005):</strong> Living foraminiferan extending an extensive, sticky mesh of branching granuloreticulopodia capturing prey, illustrating its obligate heterotrophic nutrition.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: TEST WALL MORPHOLOGY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Shell Architecture and Wall Microstructure</div>
    <div class="card-body">
      <p>The protective shell (test) of foraminifera is classified into three fundamental wall microstructures reflecting ecological niches:</p>

      <div class="formula-card">
        <div class="formula-title">Trio of Foraminiferal Wall Microstructures</div>
        $$\mathbf{\text{Organic (Tectinous)}} \quad \longrightarrow \quad \mathbf{\text{Agglutinated (Arenaceous)}} \quad \longrightarrow \quad \mathbf{\text{Calcareous (Hyaline / Porcellaneous / Microgranular)}}$$
      </div>

      <ul>
        <li><strong>Agglutinated (Arenaceous) Tests:</strong> Constructed by gathering ambient mineral grains (quartz silt, sponge spicules, heavy minerals) from the seafloor and cementing them together with organic tectin, ferric oxide, or calcium carbonate cement (e.g., <em>Textularia, Ammobaculites</em>).</li>
        <li><strong>Porcellaneous Tests:</strong> Secreted high-magnesium calcite crystals arranged randomly like a felt-work, appearing opaque, milky-white, and porcelain-like in reflected light (e.g., <em>Miliolina, Quinqueloculina</em>).</li>
        <li><strong>Hyaline (Perforate) Tests:</strong> Secreted low-to-high magnesium calcite with optic c-axes perpendicular to the surface, perforated by thousands of microscopic pores, appearing glassy and translucent (e.g., <em>Globigerina, Nummulites, Rotalia</em>).</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON MATRIX OF PROTISTAN MODES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Major Microfossil Groups and Nutritional Modes</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Microfossil Group</th>
            <th>Primary Nutritional Mode</th>
            <th>Skeletal Mineralogy</th>
            <th>Primary Ecological Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Foraminifera</strong> (Target)</td>
            <td><strong>Heterotrophic</strong> (Phagotrophic / Carnivorous / Detrital)</td>
            <td>Calcite ($\text{CaCO}_3$) or Agglutinated silt.</td>
            <td>Benthic and planktonic consumers; paleoceanographic proxies ($\delta^{18}\text{O}, \delta^{13}\text{C}$).</td>
          </tr>
          <tr>
            <td><strong>Radiolaria</strong></td>
            <td>Heterotrophic (with algal endosymbionts)</td>
            <td>Amorphous Silica ($\text{SiO}_2 \cdot n\text{H}_2\text{O}$, Opal-A).</td>
            <td>Pelagic zooplankton; deep-sea siliceous oozes.</td>
          </tr>
          <tr>
            <td><strong>Diatoms</strong></td>
            <td><strong>Autotrophic</strong> (Oxygenic Photosynthesis)</td>
            <td>Amorphous Silica (Frustules).</td>
            <td>Primary producers; cold-water upwelling blooms.</td>
          </tr>
          <tr>
            <td><strong>Coccolithophores</strong></td>
            <td><strong>Autotrophic</strong> (Photosynthetic Phytoplankton)</td>
            <td>Low-Mg Calcite (Coccoliths).</td>
            <td>Primary producers; pelagic chalk formation.</td>
          </tr>
          <tr>
            <td><strong>Dinoflagellates</strong></td>
            <td>Mixotrophic (both Autotrophic and Heterotrophic)</td>
            <td>Organic dinosporin (Sporopollenin-like).</td>
            <td>Planktonic primary producers and predators; red tides.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 66</div>
        <div class="q-text">Foraminifera are —-__ organisms.</div>
        <div class="q-options">
          <div class="opt-node">(A) Autotrophic</div>
          <div class="opt-node">(B) both Autotrophic and Heterotrophic</div>
          <div class="opt-node correct">(C) Heterotrophic</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) Heterotrophic</strong> [Foraminifera are single-celled protozoan protists that capture and ingest external food via reticulopodia, classifying them biologically as heterotrophic organisms.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) Heterotrophic</div>
    <div class="card-body">
      <p><strong>Detailed Biological & Micropaleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In biological taxonomy (Armstrong & Brasier 2005; Haq & Boersma 1978; Boggs Jr. 2012, p. 389), <strong>Foraminifera</strong> are classified under the Kingdom Protista as amoeboid, rhizopodial single-celled protozoans.</li>
        <li>As animals/protozoans, their primary mode of nutrition is strictly <strong>heterotrophic</strong>: they actively capture and engulf external nutrients (organic detritus, bacteria, algae, and micro-zooplankton) using their anastomosing network of reticulopodia.</li>
        <li>Unlike true autotrophic phytoplankton (such as diatoms and coccolithophores), foraminifera cannot synthesize organic matter from sunlight and carbon dioxide on their own.</li>
        <li>Therefore, Option <strong>(C) Heterotrophic</strong> is the scientifically definitive and correct biological classification.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Autotrophic</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Autotrophic organisms synthesize their own food from inorganic substances using light (photosynthesis) or chemical energy (chemosynthesis).</li>
        <li>Foraminifera are animal-like protists lacking chloroplasts of their own; they cannot produce food autotrophically. Calling foraminifera autotrophs is a fundamental biological error.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) both Autotrophic and Heterotrophic</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>While some specialized larger benthic foraminifera engage in *mixotrophy* by harboring photosynthetic algal endosymbionts (diatoms or dinoflagellates), this is a symbiotic relationship, not innate autotrophy of the foraminifer itself.</li>
        <li>In standard biological and geological textbooks, foraminifera are universally and unequivocally classified as <strong>heterotrophic</strong> organisms.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (C) Heterotrophic is the exact, canonical biological definition, Option (D) is false.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Major Suborders of Foraminifera</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Suborder</th>
            <th>Test Wall Mineralogy & Microstructure</th>
            <th>Stratigraphic Range</th>
            <th>Representative Genera</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Textulariina</strong></td>
            <td><strong>Agglutinated</strong> (Grains cemented by organic/calcite cement).</td>
            <td>Cambrian to Recent.</td>
            <td><em>Textularia, Ammobaculites, Saccammina</em>.</td>
          </tr>
          <tr>
            <td><strong>Fusulinina</strong></td>
            <td>Microgranular calcite (dense, sugary texture; complex internal septa).</td>
            <td>Late Paleozoic (Carboniferous to Permian Extinction).</td>
            <td><em>Fusulina, Schwagerina, Triticites</em> (Major index fossils).</td>
          </tr>
          <tr>
            <td><strong>Miliolina</strong></td>
            <td><strong>Porcellaneous</strong> (Imperforate high-Mg calcite felt-work).</td>
            <td>Carboniferous to Recent.</td>
            <td><em>Quinqueloculina, Triloculina, Alveolina</em>.</td>
          </tr>
          <tr>
            <td><strong>Rotaliina</strong></td>
            <td><strong>Hyaline</strong> (Perforate low-Mg radial/granular calcite).</td>
            <td>Triassic to Recent.</td>
            <td><em>Rotalia, Globigerina, Nummulites, Discocyclina</em>.</td>
          </tr>
          <tr>
            <td><strong>Globigerinina</strong></td>
            <td>Planktonic hyaline calcite; spinose or cancellous chambers.</td>
            <td>Middle Jurassic to Recent.</td>
            <td><em>Globotruncana</em> (Cretaceous), <em>Globigerina, Orbulina</em>.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Micropaleontology & Paleoceanography</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Paleothermometry using Oxygen Isotopes ($\delta^{18}\text{O}$)</div>
        <p>Explain how the calcite tests of benthic and planktonic foraminifera serve as the primary paleothermometer for ancient ocean water temperatures.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>When a foraminifer secretes its calcium carbonate test ($\text{CaCO}_3$), the isotopic fractionation of $^{18}\text{O}$ and $^{16}\text{O}$ is temperature-dependent. At colder temperatures, the heavier isotope $^{18}\text{O}$ is preferentially incorporated into the shell. By measuring the ratio via mass spectrometry: $T(^\circ\text{C}) = 16.9 - 4.38(\delta_c - \delta_w) + 0.10(\delta_c - \delta_w)^2$, paleoceanographers reconstruct past sea-surface and bottom-water temperatures throughout the Cenozoic.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Dimorphism in Foraminifera (Alternation of Generations)</div>
        <p>Explain the morphological difference between microspheric and megalospheric tests in a dimorphic foraminiferan population.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Microspheric Form (B-Form):</strong> Originates from the fusion of flagellated sexual gametes. Has a tiny initial proloculus ($10-20\text{ }\mu\text{m}$), but grows into a massive adult shell with numerous chambers.</li>
          <li><strong>Megalospheric Form (A-Form):</strong> Produced by asexual schizogony (multiple fission). Has a large initial proloculus ($100-300\text{ }\mu\text{m}$), but grows into a smaller adult shell with fewer chambers. Megalospheric forms outnumber microspheric forms by $10:1$ to $30:1$.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Carbonate Compensation Depth (CCD) and Agglutinated Forams</div>
        <p>Why do deep-sea sediments below the Carbonate Compensation Depth (CCD, $\sim 4500\text{ m}$) contain only agglutinated foraminifera, completely lacking calcareous tests?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Below the CCD, seawater is highly undersaturated with respect to $\text{CaCO}_3$ due to high hydrostatic pressure and high dissolved $\text{CO}_2$, causing calcareous tests to dissolve completely. Deep-water agglutinated foraminifera (DWAF) synthesize non-calcareous tests using insoluble silica grains cemented by organic or ferric tectin, surviving down to the abyssal trenches ($>6000\text{ m}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Coiling Direction of *Neogloboquadrina pachyderma*</div>
        <p>How does the coiling direction of the planktonic foraminifer <em>Neogloboquadrina pachyderma</em> indicate Pleistocene glacial vs. interglacial epochs?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Sinistral (Left-coiling):</strong> Dominates ($>90\%$) in cold polar/subpolar waters ($T < 7.2^\circ\text{C}$), signifying glacial periods in mid-latitude marine cores.</li>
          <li><strong>Dextral (Right-coiling):</strong> Dominates in warmer subpolar-to-temperate waters ($T > 7.2^\circ\text{C}$), signifying warm interglacial intervals.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Fusulinid Foraminifera in Carboniferous-Permian Biostratigraphy</div>
        <p>What structural complexity inside the test makes fusulinid foraminifera the premier index fossils of the Late Paleozoic?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Fusulinids (rice-grain shaped, $0.5-5\text{ cm}$ long) possess complexly fluted internal septa (septal folding), chomata, and tunnel structures. Their rapid evolutionary radiation and extinction at the end-Permian provide high-resolution global biozones across Carboniferous and Permian carbonate platforms.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Planktonic vs. Benthic Ratio ($P/B$ Ratio)</div>
        <p>What does a high ratio of planktonic to benthic foraminifera ($P/B > 90\%$) signify about water depth and distance from shore?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In nearshore and shallow inner-shelf waters ($0-50\text{ m}$), benthic foraminifera dominate ($P/B < 20\%$). As water depth increases across the outer continental shelf and continental slope ($>200-2000\text{ m}$), planktonic foraminifera multiplying in the vast overlying water column rain down in enormous numbers, driving the $P/B$ ratio above $80-95\%$, making it an accurate paleobathymetric depth proxy.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: *Globotruncana* as a Cretaceous Index Fossil</div>
        <p>What diagnostic morphological feature identifies the planktonic foraminifer <em>Globotruncana</em> in Cretaceous thin sections?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Globotruncana</em> possesses trochospiral chambers with a prominent <strong>double peripheral keel (double carinae)</strong> of imperforate calcite around the margin, a broad umbilical aperture covered by complex tegilla, and a flattened spiral side, diagnostic of the Late Cretaceous (Turonian-Maastrichtian).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Carbon Isotope Vital Effect</div>
        <p>Why do foraminifera with photosynthetic endosymbionts exhibit heavier carbon isotope values ($\delta^{13}\text{C}$) in their tests?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Algal endosymbionts actively perform photosynthesis inside the foraminiferal cytoplasm, preferentially sequestering the light isotope $^{12}\text{C}$ to build organic sugars. This leaves the localized intracellular inorganic carbon pool enriched in the heavier isotope $^{13}\text{C}$, which is then incorporated into the precipitating $\text{CaCO}_3$ test (positive $\delta^{13}\text{C}$ offset / vital effect).</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 66, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q066_Foraminifera_Heterotrophic_Protists_Rhizopodia_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q066: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q067: Pliopithecus: Miocene Catarrhine Anthropoid Primates
# ==============================================================================
def generate_q067():
    title = r"Q067: Cenozoic Primate Evolution: Pliopithecus as a Miocene Stem-Catarrhine Anthropoid | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Primate Evolution"
    h1_title = "Q067: Pliopithecus: Miocene Stem-Catarrhine Anthropoid"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 67<br>
<strong>Authoritative References:</strong> John G. Fleagle, <em>Primate Adaptation and Evolution</em> (3rd Ed., Academic Press, Ch. 12: Miocene Catarrhines, pp. 320–342); Frederick S. Szalay & Eric Delson, <em>Evolutionary History of the Primates</em> (Academic Press); Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 10); David R. Begun, <em>Fossil Primates of Europe</em> (Cambridge Univ. Press)."""

    part1 = r"""
  <!-- CARD 1: PLIOPITHECUS CLASSIFICATION -->
  <div class="card">
    <div class="card-header bg-blue">1. The Genus Pliopithecus: Evolutionary Position Among the Anthropoidea</div>
    <div class="card-body">
      <p>The fossil primate <strong><em>Pliopithecus</em></strong> (named by French paleontologist Paul Gervais in 1849 from Middle Miocene strata in Sansan, France) represents one of the most famous and historically pivotal genera in tertiary vertebrate paleontology:</p>

      <ul>
        <li><strong>Taxonomic Classification:</strong> <em>Pliopithecus</em> is a quintessential genus of the <strong>Anthropoidea (Anthropoids / Simians)</strong>, belonging to the Superfamily <strong>Pliopithecoidea</strong> within the Parvorder <strong>Catarrhini</strong> (Old World higher primates).</li>
        <li><strong>Geochronological & Geographic Distribution:</strong> It flourished during the <strong>Early to Late Miocene ($\sim 18-10\text{ Ma}$)</strong> and persisted into the basal Pliocene across Europe (France, Spain, Germany, Poland, Slovakia) and eastern Asia (China, e.g., <em>Pliopithecus zhanxiangi</em>).</li>
        <li><strong>The First Eurasian Catarrhine:</strong> Following the closure of the Tethyan seaway and the establishment of the Gomphothere land bridge connecting Afro-Arabia to Eurasia at $\sim 19\text{ Ma}$, <em>Pliopithecus</em> was among the very first anthropoid lineages to migrate out of Africa and successfully colonize the subtropical forested belts of Europe and Asia.</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q67/pliopithecus_anthropoid_skull_dentition.png" alt="Pliopithecus Skull and Dentition">
        <div class="tb-caption">
          <strong>Figure 67.1 (Szalay & Delson 1979 / Fleagle 2013):</strong> Cranial and dental anatomy of <em>Pliopithecus antiquus</em>, illustrating complete postorbital closure, catarrhine dental formula ($2.1.2.3$), and the diagnostic "Pliopithecus triangle" on lower molars.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: ANTHROPOID SYNAPOMORPHIES -->
  <div class="card">
    <div class="card-header bg-indigo">2. Anatomical Hallmarks of the Anthropoidea in Pliopithecus</div>
    <div class="card-body">
      <p><em>Pliopithecus</em> exhibits the full suite of diagnostic morphological characters that define higher primates (Anthropoids):</p>

      <div class="formula-card">
        <div class="formula-title">The Anthropoid Cranio-Dental Formula</div>
        $$\text{Dental Formula: } \frac{2 \cdot 1 \cdot 2 \cdot 3}{2 \cdot 1 \cdot 2 \cdot 3} \times 2 = 32 \text{ Teeth} \quad \left(\mathbf{I}\frac{2}{2}, \mathbf{C}\frac{1}{1}, \mathbf{P}\frac{2}{2}, \mathbf{M}\frac{3}{3}\right)$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">Possesses the definitive catarrhine dental formula with two premolars, identical to modern Old World monkeys, apes, and humans.</p>
      </div>

      <ul>
        <li><strong>Complete Postorbital Closure:</strong> A solid bony wall (postorbital septum) separates the eye orbit from the temporal fossa, a critical anthropoid feature protecting the eyes during mastication.</li>
        <li><strong>Fused Frontal Bones:</strong> The right and left frontal bones fuse into a single solid frontal plate across the metopic suture.</li>
        <li><strong>Fused Mandibular Symphysis:</strong> The two dentary halves fuse completely at the chin midline.</li>
        <li><strong>The "Pliopithecus Triangle":</strong> A distinctive, narrow, triangular crest or cingulum on the buccal side of the lower molar cusps (talonid basin), characteristic of pliopithecoids.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON MATRIX OF FOSSIL PRIMATES -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Evolutionary Radiation of Miocene Primates</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Fossil Primate Genus</th>
            <th>Taxonomic Superfamily</th>
            <th>Locality & Epoch</th>
            <th>Locomotor / Ecological Specialization</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong><em>Pliopithecus</em></strong> (Target)</td>
            <td><strong>Pliopithecoidea (Stem Catarrhine Anthropoid)</strong></td>
            <td>Europe & Asia (Miocene, $\sim 18-10\text{ Ma}$).</td>
            <td>Arboreal quadruped; retains primitive tail; eats soft fruits.</td>
          </tr>
          <tr>
            <td><strong><em>Proconsul</em></strong></td>
            <td>Proconsuloidea (Stem Hominoidea)</td>
            <td>East Africa (Early Miocene, $\sim 20-17\text{ Ma}$).</td>
            <td>Tailless arboreal quadruped; ape-like brain and shoulder.</td>
          </tr>
          <tr>
            <td><strong><em>Dryopithecus</em></strong></td>
            <td>Hominoidea (Crown Hominoid / Ape)</td>
            <td>Europe (Middle-Late Miocene, $\sim 12-9\text{ Ma}$).</td>
            <td>Suspensory brachiator; Y-5 molar pattern; thin enamel.</td>
          </tr>
          <tr>
            <td><strong><em>Sivapithecus</em></strong></td>
            <td>Hominoidea (Ponginae / Ancestor of Orangutan)</td>
            <td>Siwaliks of India & Pakistan ($\sim 12.5-8.5\text{ Ma}$).</td>
            <td>Arboreal quadruped; oval eye orbits, dished face, thick molar enamel.</td>
          </tr>
          <tr>
            <td><strong><em>Australopithecus</em></strong></td>
            <td>Hominini (True Bipedal Hominid)</td>
            <td>East & South Africa (Pliocene, $\sim 4-2\text{ Ma}$).</td>
            <td><strong>Obligate terrestrial bipedalism</strong>; small brain, reduced canines.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 67</div>
        <div class="q-text">Pliopithecus is a genus of —__________ found in the Upper Miocene and Lower Pliocene strata of Europe and possibly Asia.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) Anthropoids</div>
          <div class="opt-node">(B) Bipedal ape-like animals</div>
          <div class="opt-node">(C) Lazarus taxa</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) Anthropoids</strong> [Pliopithecus is a celebrated fossil genus of higher primates belonging to the Anthropoidea (specifically stem-catarrhines), possessing an anthropoid skull and dental formula.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) Anthropoids</div>
    <div class="card-body">
      <p><strong>Detailed Primate Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In primate taxonomy and vertebrate paleontology (Fleagle 2013, Ch. 12; Szalay & Delson 1979; Benton 2014), <strong><em>Pliopithecus</em></strong> is universally classified under the suborder/infraorder <strong>Anthropoidea (Anthropoids / Simians)</strong>.</li>
        <li>It represents an ancient stem-catarrhine (higher primate) characterized by definitive anthropoid synapomorphies: complete postorbital closure of the eye orbits, fused mandibular symphysis, and a catarrhine dental formula of $2.1.2.3$.</li>
        <li>It was the first major anthropoid radiation to spread into the Miocene forests of Europe and Asia.</li>
        <li>Therefore, Option <strong>(A) Anthropoids</strong> is the exact, scientifically verified classification.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Bipedal ape-like animals</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li><em>Pliopithecus</em> was <strong>not bipedal</strong>; postcranial skeletons (such as <em>Epipliopithecus vindobonensis</em> from Slovakia) prove that it was an arboreal <strong>quadrupedal monkey-like climber</strong> possessing a short external tail.</li>
        <li>Bipedalism evolved tens of millions of years later in the hominin lineage (e.g., <em>Sahelanthropus, Ardipithecus, Australopithecus</em>) in Africa.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Lazarus taxa</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>A <strong>Lazarus taxon</strong> is an organism that disappears from the fossil record during a mass extinction only to reappear much later (e.g., the coelacanth).</li>
        <li><em>Pliopithecus</em> is a legitimate, well-documented extinct genus of fossil anthropoid primates, not an evolutionary disappearance-reappearance anomaly.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (A) Anthropoids is the precise taxonomic group to which <em>Pliopithecus</em> belongs, Option (D) is false.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: High-Level Taxonomy of the Primates</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Taxonomic Rank</th>
            <th>Name of Clade</th>
            <th>Diagnostic Defining Characteristics</th>
            <th>Representative Genera</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Suborder</strong></td>
            <td><strong>Strepsirrhini</strong> ("Wet-nosed")</td>
            <td>Grooming claw, tooth comb, unfused symphysis, open postorbital bar.</td>
            <td>Lemurs, Lorises, Galagos.</td>
          </tr>
          <tr>
            <td><strong>Suborder</strong></td>
            <td><strong>Haplorhini</strong> ("Dry-nosed")</td>
            <td>Dry rhinarium, retinal fovea, postorbital closure.</td>
            <td>Tarsiers + Anthropoidea.</td>
          </tr>
          <tr>
            <td><strong>Infraorder</strong> (Target)</td>
            <td><strong>Anthropoidea (Simiiformes)</strong></td>
            <td><strong>Complete postorbital closure, fused frontals, fused mandibular symphysis.</strong></td>
            <td><strong><em>Pliopithecus</em>, New World Monkeys, Old World Monkeys, Apes, Humans.</strong></td>
          </tr>
          <tr>
            <td><strong>Parvorder</strong></td>
            <td><strong>Catarrhini</strong></td>
            <td>Narrow downward-facing nostrils; 2 premolars ($2.1.2.3$ dental formula).</td>
            <td>Pliopithecoids, Cercopithecoids, Hominoids.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Primate Evolution & Anthropoid Paleontology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Dental Formula of Platyrrhines vs. Catarrhines</div>
        <p>Contrast the dental formula of New World monkeys (Platyrrhini) with that of <em>Pliopithecus</em> and Old World higher primates (Catarrhini).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Platyrrhini (New World Monkeys):</strong> Dental formula is $\frac{2.1.3.3}{2.1.3.3} \times 2 = 36 \text{ teeth}$ (retains <strong>three premolars</strong> in each quadrant).</li>
          <li><strong>Catarrhini (<em>Pliopithecus</em>, Old World Monkeys, Apes):</strong> Dental formula is $\frac{2.1.2.3}{2.1.2.3} \times 2 = 32 \text{ teeth}$ (loss of the second premolar leaves <strong>two premolars</strong>, $\text{P}_3$ and $\text{P}_4$).</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: The Ectotympanic Tube in Catarrhine Crania</div>
        <p>What primitive cranial feature in <em>Pliopithecus</em> demonstrates that it branched off before the divergence of modern catarrhines?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Modern catarrhines (cercopithecoids and hominoids) possess an extended, bony tubular <strong>ectotympanic tube</strong> leading to the ear canal. In <em>Pliopithecus</em>, the ectotympanic bone is a simple, primitive annulus (ring-like bone) fused to the bulla without a bony tube, proving it is a stem-catarrhine.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: The Siwalik Primate *Sivapithecus*</div>
        <p>What primate fossil discovered in the Middle Siwalik beds of the Potwar Plateau and Ramnagar (India) is recognized as the direct ancestor of the modern Orangutan (*Pongo*)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Sivapithecus indicus</em></strong> (and <em>Sivapithecus sivalensis</em>). It shares unique cranial synapomorphies with living orangutans: vertically elongated oval eye orbits, narrow interorbital distance, concave "dished" facial profile, and smooth unsegmented subnasal alveolar plane.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: *Gigantopithecus bilaspurensis* in India</div>
        <p>What is the significance of the fossil ape <em>Gigantopithecus</em> discovered in the Siwalik Hills of Himachal Pradesh?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Gigantopithecus bilaspurensis</em> (Late Miocene, $\sim 6-8\text{ Ma}$) and its Pleistocene descendant <em>Gigantopithecus blacki</em> represent the <strong>largest primates that ever lived</strong> (estimated body mass $>250-300\text{ kg}$). They possessed massive jaws with thick, flat-crowned molars adapted for chewing tough fibrous vegetation like bamboo.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Postorbital Bar vs. Postorbital Septum</div>
        <p>How does the orbit of a strepsirrhine prosimian (e.g., lemur) differ from an anthropoid like <em>Pliopithecus</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Strepsirrhines:</strong> Possess only a lateral <strong>postorbital bar</strong>; the orbit remains wide open to the temporal fossa posteriorly.</li>
          <li><strong>Anthropoids (<em>Pliopithecus</em>):</strong> Possess a complete, bony <strong>postorbital septum / closure</strong>, separating the eye orbit into an enclosed cone that insulates the eye from chewing muscle vibrations.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: The Fayum Depression and Anthropoid Radiation</div>
        <p>What famous geological locality in Egypt preserves the ancestral Eocene-Oligocene radiation of early anthropoids?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Fayum Depression (Jebel Qatrani Formation)</strong>, which yielded the iconic stem-anthropoids and early catarrhines <em>Aegyptopithecus zeuxis</em>, <em>Propliopithecus</em>, and <em>Catopithecus</em> ($\sim 34-30\text{ Ma}$).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Brachiation vs. Quadrupedalism in Pliopithecus</div>
        <p>Why did early researchers mistakenly classify <em>Pliopithecus</em> as a fossil gibbon (hylobatid)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Early workers observed that <em>Pliopithecus</em> had relatively slender limbs and short facial proportions similar to modern gibbons. However, complete limb skeletons proved that its intermembral index was $\sim 90-95$ (equal arm and leg lengths typical of <strong>quadrupedal tree-climbers</strong>), completely lacking the extreme arm elongation (index $>130$) and mobile wrist joints required for true ricochetal brachiation.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Miocene Climate and Primate Extinction in Europe</div>
        <p>Why did <em>Pliopithecus</em> and other apes disappear from Europe by the end of the Miocene ($\sim 8-5\text{ Ma}$)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The Messinian salinity crisis and global tectonic cooling caused the warm, subtropical evergreen rainforests of Europe to be replaced by cold, dry, deciduous woodlands and open grasslands. As arboreal fruit-bearing trees disappeared, tropical frugivorous anthropoids like <em>Pliopithecus</em> and <em>Dryopithecus</em> were driven to regional extinction in Europe.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 67, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q067_Pliopithecus_Miocene_Catarrhine_Anthropoid_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q067: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q068: Origin of Mammals: Upper Triassic to Lower Jurassic
# ==============================================================================
def generate_q068():
    title = r"Q068: Origin of Mammals: Upper Triassic to Lower Jurassic Radiation (Morganucodontids) | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Vertebrate Paleontology & Mammalian Evolution"
    h1_title = "Q068: Origin of Mammals: Upper Triassic to Lower Jurassic"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 68<br>
<strong>Authoritative References:</strong> Michael J. Benton, <em>Vertebrate Palaeontology</em> (4th Ed., Ch. 10: The Origin of Mammals, pp. 288–315); T.S. Kemp, <em>The Origin and Evolution of Mammals</em> (Oxford Univ. Press, 2005); Zhe-Xi Luo, <em>Transformation and Diversification in Early Mammal Evolution</em> (Nature, 2007); G.B. Mahapatra, <em>A Text-Book of Geology</em>."""

    part1 = r"""
  <!-- CARD 1: THE ORIGIN OF TRUE MAMMALS -->
  <div class="card">
    <div class="card-header bg-blue">1. The Dawn of Mammaliaformes in the Fossil Record</div>
    <div class="card-body">
      <p>The evolutionary transition from advanced non-mammalian cynodont therapsids to true crownward mammals (clade <strong>Mammaliaformes</strong>) represents one of the most thoroughly documented anatomical transformations in vertebrate history:</p>

      <ul>
        <li><strong>Chronological Origin:</strong> The earliest definitive mammals are universally recognized in the fossil record in the <strong>Upper Triassic (Carnian-Norian-Rhaetian stages, $\sim 225-205\text{ Ma}$)</strong> and radiated extensively across the <strong>Lower Jurassic ($\sim 201-175\text{ Ma}$)</strong>.</li>
        <li><strong>Iconic Late Triassic - Early Jurassic Taxa:</strong>
          <ul>
            <li><strong><em>Morganucodon watsoni</em> (Late Triassic of Wales and China):</strong> An agile, shrew-sized nocturnal insectivore ($\sim 10\text{ cm}$ long) that established the mammalian body plan.</li>
            <li><strong><em>Kuehneotherium praecursoris</em> (Late Triassic of UK):</strong> Earliest mammal with reverse-triangle molar cusp patterns ancestral to tribosphenic molars.</li>
            <li><strong><em>Adelobasileus cromptoni</em> (Carnian, $\sim 225\text{ Ma}$, Texas):</strong> The earliest known mammaliaform braincase showing lateral expansion of the cerebral hemispheres.</li>
            <li><strong><em>Sinoconodon</em> (Early Jurassic of Yunnan, China):</strong> Primitive mammaliaform with specialized jaw mechanics.</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q68/benton_morganucodon_earliest_mammal_triassic.png" alt="Morganucodon Earliest Mammal">
        <div class="tb-caption">
          <strong>Figure 68.1 (Michael J. Benton, Fig. 10.4):</strong> Skeletal anatomy and skull of <em>Morganucodon</em> from the Late Triassic, illustrating the definitive mammalian dentary-squamosal jaw joint and specialized tricuspid cheek teeth.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: ANATOMICAL DEFINITION OF A MAMMAL -->
  <div class="card">
    <div class="card-header bg-indigo">2. Anatomical Hallmarks of the Earliest Mammals</div>
    <div class="card-body">
      <p>The boundary between cynodont reptiles and mammals is defined osteologically by two revolutionary anatomical transformations:</p>

      <div class="formula-card">
        <div class="formula-title">The Classical Osteological Definition of Mammalia</div>
        $$\mathbf{\text{Reptilian Jaw Joint}} \text{ (Articular - Quadrate)} \quad \longrightarrow \quad \mathbf{\text{Mammalian Jaw Joint}} \text{ (Dentary - Squamosal)}$$
        <p style="margin-top:6px; font-size:12.5px; color:#cbd5e1;">The articular bone evolved into the <strong>Malleus (Hammer)</strong>, the quadrate into the <strong>Incus (Anvil)</strong>, joining the stapes to create the three-ossicle middle ear!</p>
      </div>

      <ul>
        <li><strong>Double Jaw Joint in Morganucodontids:</strong> <em>Morganucodon</em> preserves the extraordinary transitional stage: it had simultaneously evolved the new <strong>dentary-squamosal jaw joint</strong> while still retaining the ancient reduced <strong>articular-quadrate joint</strong> acting as a dual-function hinge and sound transducer.</li>
        <li><strong>Diphyodont Dentition:</strong> Unlike reptiles which continuously replace teeth throughout life (polyphyodonty), early mammals evolved <strong>diphyodonty</strong> (a single set of deciduous milk teeth replaced once by permanent adult teeth), enabling precise occlusal alignment of molar cusps.</li>
        <li><strong>Encephalization & Nocturnal Sensory Expansion:</strong> Expanded cerebral cortex and enlarged olfactory bulbs accommodated night vision, sensitive whiskers (vibrissae), and acute hearing.</li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON TABLE OF CYNODONT TO MAMMAL -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Cynodont Therapsid vs. Earliest Mammal vs. Modern Mammal</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Anatomical Feature</th>
            <th>Advanced Cynodont (e.g., <em>Probainognathus</em>)</th>
            <th>Earliest Mammaliaform (e.g., <em>Morganucodon</em>)</th>
            <th>Living Crown Mammal</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Jaw Joint</strong></td>
            <td>Articular (lower) against Quadrate (upper).</td>
            <td><strong>Double Joint: Dentary-Squamosal AND Articular-Quadrate.</strong></td>
            <td><strong>Exclusively Dentary-Squamosal.</strong></td>
          </tr>
          <tr>
            <td><strong>Middle Ear Ossicles</strong></td>
            <td>Single ossicle (Stapes only); postdentary bones on jaw.</td>
            <td>Postdentary bones reduced, resting in dentary sulcus.</td>
            <td><strong>Three ossicles in cranium: Malleus, Incus, Stapes.</strong></td>
          </tr>
          <tr>
            <td><strong>Tooth Replacement</strong></td>
            <td>Polyphyodont (continuous multiple tooth replacement).</td>
            <td><strong>Diphyodont (Milk teeth replaced once by adult teeth).</strong></td>
            <td>Diphyodont or monophyodont.</td>
          </tr>
          <tr>
            <td><strong>Secondary Palate</strong></td>
            <td>Incomplete or partially ossified.</td>
            <td><strong>Fully ossified bony secondary palate.</strong></td>
            <td>Complete bony and soft secondary palate (suckling enabled).</td>
          </tr>
          <tr>
            <td><strong>Geological Age</strong></td>
            <td>Middle to Late Triassic.</td>
            <td><strong>Upper Triassic to Lower Jurassic (Target).</strong></td>
            <td>Jurassic to Present.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 68</div>
        <div class="q-text">The earliest mammals are recognized in the ___.</div>
        <div class="q-options">
          <div class="opt-node">(A) Permian</div>
          <div class="opt-node correct">(B) Upper Triassic and Lower Jurassic</div>
          <div class="opt-node">(C) Cambrian to Silurian</div>
          <div class="opt-node">(D) Devonian</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(B) Upper Triassic and Lower Jurassic</strong> [The earliest true mammals (Mammaliaformes, such as Morganucodon and Adelobasileus) appear in the fossil record in the Upper Triassic and radiate in the Lower Jurassic.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (B) Upper Triassic and Lower Jurassic</div>
    <div class="card-body">
      <p><strong>Detailed Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In vertebrate paleontology (Benton 2014, Ch. 10, p. 295; Kemp 2005; Carroll 1988), the earliest definitive fossils of mammals (Mammaliaformes) appear in the <strong>Upper Triassic</strong> (specifically in the Carnian, Norian, and Rhaetian stages, $\sim 225-201\text{ Ma}$) and extend continuously into the <strong>Lower Jurassic</strong>.</li>
        <li>Classic representatives include <em>Adelobasileus</em> (Carnian, $\sim 225\text{ Ma}$, Texas), <em>Morganucodon</em> (Rhaetian, $\sim 205\text{ Ma}$, Wales and China), <em>Kuehneotherium</em>, and <em>Sinoconodon</em> (Lower Jurassic).</li>
        <li>These organisms evolved the definitive mammalian dentary-squamosal jaw articulation, diphyodont dentition, and hair/endothermy.</li>
        <li>Therefore, Option <strong>(B) Upper Triassic and Lower Jurassic</strong> is the factually accurate, textbook-verified correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Permian</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The Permian Period was dominated by primitive <strong>synapsids</strong> (pelycosaurs like <em>Dimetrodon</em> and early therapsids like gorgonopsians).</li>
        <li>While they belong to the synapsid stem-lineage leading towards mammals, they were reptiles (with reptilian articular-quadrate jaw joints, polyphyodont teeth, and small brains), not mammals. True mammals did not appear until the end of the Triassic.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) Cambrian to Silurian</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>During the Cambrian to Silurian, life was primarily marine; only early jawless and primitive jawed fishes existed in the vertebrate world.</li>
        <li>Tetrapods did not even walk on land until the Late Devonian, making the appearance of mammals in the early Paleozoic temporally impossible by over 200 million years.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) Devonian</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>The Devonian is famously the "Age of Fishes" and saw the earliest emergence of stem-amphibians (e.g., <em>Ichthyostega</em>).</li>
        <li>Amniotes (reptiles and synapsids) did not evolve until the Carboniferous, and mammals did not appear until the Late Triassic.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Mesozoic Radiation of Mammalian Clades</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Mammalian Clade</th>
            <th>Geological Range</th>
            <th>Diagnostic Evolutionary Specialization</th>
            <th>Representative Genera</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Morganucodonta</strong></td>
            <td><strong>Upper Triassic to Lower Jurassic</strong></td>
            <td>Double jaw joint, diphyodont teeth, tricuspid molars.</td>
            <td><strong><em>Morganucodon</em>, <em>Megazostrodon</em></strong>.</td>
          </tr>
          <tr>
            <td><strong>Docodonta</strong></td>
            <td>Middle Jurassic to Early Cretaceous</td>
            <td>Complex rectangular crushing molars; semi-aquatic swimming (<em>Castorocauda</em>).</td>
            <td><em>Docodon</em>, <em>Castorocauda</em>.</td>
          </tr>
          <tr>
            <td><strong>Multituberculata</strong></td>
            <td>Middle Jurassic to Late Eocene ($120\text{ Ma}$ span!)</td>
            <td>Rodent-like incisors, blade-like shearing premolars, multicusped grinding molars.</td>
            <td><em>Kuehneodon</em>, <em>Taeniolabis</em>.</td>
          </tr>
          <tr>
            <td><strong>Monotremata</strong> (Prototheria)</td>
            <td>Early Cretaceous to Present</td>
            <td>Egg-laying mammals; cloaca; electroreceptive bill.</td>
            <td><em>Steropodon</em> (fossil opalized jaw), Platypus, Echidna.</td>
          </tr>
          <tr>
            <td><strong>Theria</strong> (Marsupials & Placentals)</td>
            <td>Early Cretaceous to Present</td>
            <td>True <strong>tribosphenic molars</strong>; live birth (viviparity).</td>
            <td><em>Eomaia</em> (Placental), <em>Sinodelphys</em> (Marsupial).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Synapsid Evolution & Mammalian Origins</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Reichert-Gaupp Theory of Middle Ear Ossicles</div>
        <p>Explain the Reichert-Gaupp theory for the evolutionary transformation of the reptilian jaw elements into the mammalian middle ear.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>In non-mammalian synapsids, the lower jaw consisted of seven bones, hinged at the <strong>articular bone</strong> against the cranial <strong>quadrate bone</strong>. As the dentary expanded to form the entire lower jaw in mammals, the reduced articular detached from the jaw and migrated into the middle ear cavity to become the <strong>malleus (hammer)</strong>. The cranial quadrate shrank to become the <strong>incus (anvil)</strong>, and the ancient angular bone became the <strong>ectotympanic ring</strong> supporting the eardrum.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Tribosphenic Molar Mechanics</div>
        <p>Describe the function of the two distinct parts of a tribosphenic molar (trigonid and talonid basin) in early therian mammals.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li><strong>Trigonid (Anterior Shearing Triangle):</strong> Composed of three sharp cusps (protoconid, paraconid, metaconid) that shear past the upper molar like scissor blades to slice insect chitin and meat.</li>
          <li><strong>Talonid Basin (Posterior Crushing Heel):</strong> A low basin surrounded by cusps (hypoconid, entoconid, hypoconulid) into which the upper protocone pestle grinds, crushing food in mortar-and-pestle action.</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Indian Jurassic Mammals (Kota Formation)</div>
        <p>What important primitive mammals were discovered in the Lower Jurassic Kota Formation of the Pranhita-Godavari Valley in India?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Kotatherium haldanei</em></strong> and <strong><em>Indotherium pranhitai</em></strong> (Order Morganucodonta / Symmetrodonta). Discovered in Early Jurassic freshwater fluvio-lacustrine limestones alongside sauropod dinosaurs (<em>Barapasaurus tagorei</em>), they confirm that early mammaliaforms had colonized eastern Gondwanaland by the Early Jurassic.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Lactation and Diphyodonty Evolutionary Link</div>
        <p>Why is diphyodont tooth replacement (having milk teeth replaced by adult teeth) directly linked to the origin of lactation (nursing milk)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Reptilian hatchlings have teeth from day one to feed on solid food, requiring continuous tooth replacement as jaws grow. In mammals, mothers nurse newborn young with liquid milk, eliminating the need for functional teeth during early rapid jaw growth. Deciduous teeth erupt only when the jaw nears adult size, followed by a single permanent adult set that occludes with micrometer precision.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Secondary Palate and Breathing During Chewing</div>
        <p>What physiological advantage did the fully ossified secondary palate give to early mammals like <em>Morganucodon</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The bony secondary palate completely separates the nasal respiratory passage from the oral food-processing cavity. This enabled early mammals to chew and process food in the mouth continuously without suffocating, while also allowing newborn infants to suckle milk while breathing simultaneously.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Encephalization Quotient in Early Mammals</div>
        <p>How did the brain-to-body size ratio (encephalization quotient) of <em>Morganucodon</em> compare to contemporary therapsids?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>CT-scan endocasts reveal that <em>Morganucodon</em> had a relative brain size <strong>three to four times larger</strong> than contemporary non-mammalian cynodonts. The expansion was concentrated in the neocortex, olfactory bulbs, and cerebellar hemispheres, reflecting the sensory integration required for nocturnal navigation and acute tactile coordination.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: *Castorocauda* and Ecological Diversification in the Jurassic</div>
        <p>How did the 2006 discovery of *Castorocauda lutrasimilis* shatter the stereotype that Mesozoic mammals were all small, generalized shrew-like insectivores?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Castorocauda</em> (Middle Jurassic of Daohugou, China, $\sim 164\text{ Ma}$) was a large docodont ($\sim 50\text{ cm}$ long, $\sim 1\text{ kg}$) possessing webbed feet, a flattened scaly beaver-like tail for swimming, seal-like fish-catching teeth, and dense modern fur, proving early mammals had diversified into complex aquatic and swimming niches over $100\text{ million years}$ before the extinction of dinosaurs.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Endothermy Evidence from Bone Histology</div>
        <p>What histological feature in the limb bones of Late Triassic mammaliaforms demonstrates endothermy (warm-bloodedness)?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Limb cross-sections exhibit well-vascularized <strong>fibrolamellar bone tissue with secondary osteons</strong>, indicating continuous rapid bone growth powered by high basal metabolic rates, contrasting with the poorly vascularized lamellar-zonal bone of ectothermic reptiles.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 68, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q068_Earliest_Mammals_Upper_Triassic_Lower_Jurassic_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q068: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q069: Major Invertebrate Fossil Phyla: Phylum Mollusca
# ==============================================================================
def generate_q069():
    title = r"Q069: Invertebrate Paleontology: Major Marine Fossil Phyla & Phylum Mollusca | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Invertebrate Paleontology & Fossil Classification"
    h1_title = "Q069: Invertebrate Paleontology: Major Fossil Phyla & Mollusca"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 69<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (Ch. 18: Invertebrate Paleontology, pp. 344–360, p. 180); E.N.K. Clarkson, <em>Invertebrate Palaeontology and Evolution</em> (4th Ed., Blackwell, Ch. 8: Mollusca, pp. 200–245); R.S. Boardman et al., <em>Fossil Invertebrates</em> (Blackwell Scientific); P.K. Mukherjee, <em>A Text Book of Geology</em> (Ch. 16)."""

    part1 = r"""
  <!-- CARD 1: THE BIG FIVE INVERTEBRATE FOSSIL PHYLA -->
  <div class="card">
    <div class="card-header bg-blue">1. The "Big Five" Invertebrate Phyla in the Geological Record</div>
    <div class="card-body">
      <p>In invertebrate paleontology and historical geology, over 99% of all macro-invertebrate fossils discovered in sedimentary rocks across the Phanerozoic belong to five dominant, heavily biomineralized animal phyla:</p>

      <ul>
        <li><strong>1. Phylum Mollusca (Molluscs) [Target Clue: "__m_."]:</strong> The most diverse and abundant invertebrate phylum in post-Paleozoic marine and terrestrial strata. Encompasses Bivalvia (clams, oysters), Gastropoda (snails), Cephalopoda (ammonites, belemnites, nautiloids), and Scaphopoda. Possesses durable aragonitic and calcitic shells.</li>
        <li><strong>2. Phylum Brachiopoda (Brachiopods):</strong> Lophophorate bivalved filter feeders that completely dominated Paleozoic benthic marine communities, characterized by bilateral symmetry across the valve midline.</li>
        <li><strong>3. Phylum Echinodermata (Echinoderms):</strong> Exclusively marine deuterostomes with secondary pentameral symmetry and stereom high-magnesium calcite endoskeletons (Crinoids, Blastoids, Echinoids, Asteroids).</li>
        <li><strong>4. Phylum Arthropoda (Arthropods):</strong> Segmented bodies with jointed appendages and chitinous/calcified exoskeletons (Trilobites, Eurypterids, Ostracods, Crustaceans).</li>
        <li><strong>5. Phylum Cnidaria (Cnidarians):</strong> Radially symmetrical diploblastic coelenterates; premier geological reef builders possessing massive calcium carbonate corallites (Rugosa, Tabulata, Scleractinia).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q69/mahapatra_p180_invertebrate_fossil_groups.png" alt="Invertebrate Fossil Groups from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 69.1 (G.B. Mahapatra, p. 180):</strong> Systematic classification of major invertebrate fossil phyla: Mollusca, Brachiopoda, Echinodermata, Arthropoda, and Cnidaria.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: TAXONOMIC HIERARCHY -->
  <div class="card">
    <div class="card-header bg-indigo">2. Taxonomic Hierarchy: Phylum Mollusca vs. Class Cephalopoda</div>
    <div class="card-body">
      <p>Question 69 tests fundamental biological taxonomic hierarchy in invertebrate classification:</p>

      <div class="formula-card">
        <div class="formula-title">The Invertebrate Phylum-Level Coordinate Series</div>
        $$\mathbf{Phylum \text{ Mollusca (molluscs)}} \quad \longleftrightarrow \quad \mathbf{Brachiopoda} \quad \longleftrightarrow \quad \mathbf{Echinodermata} \quad \longleftrightarrow \quad \mathbf{Arthropoda} \quad \longleftrightarrow \quad \mathbf{Cnidaria}$$
      </div>

      <ul>
        <li><strong>Coordinate Taxonomic Rank:</strong> The examination prompt lists four taxa at the <strong>Phylum rank</strong>: <em>Brachiopoda</em> (Phylum), <em>Echinodermata</em> (Phylum), <em>Arthropoda</em> (Phylum), and <em>Cnidaria</em> (Phylum).</li>
        <li><strong>Why "Molluscs" is the Only Valid Answer:</strong>
          <ul>
            <li><strong>Molluscs (Phylum Mollusca):</strong> Represents the coordinate phylum-level peer to Brachiopoda, Echinodermata, Arthropoda, and Cnidaria, perfectly matching the typographical clue <strong>"__m_."</strong>.</li>
            <li><strong>Cephalopoda:</strong> A <em>class</em> within the Phylum Mollusca.</li>
            <li><strong>Nautiloids:</strong> A <em>subclass</em> within the Class Cephalopoda.</li>
          </ul>
        </li>
      </ul>
    </div>
  </div>

  <!-- CARD 3: COMPARISON TABLE OF INVERTEBRATE PHYLA -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Diagnostic Morphologies of the Big Five Phyla</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Invertebrate Phylum</th>
            <th>Symmetry Plan</th>
            <th>Skeletal Composition</th>
            <th>Geological Peak Range</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mollusca</strong> (Target)</td>
            <td>Bilateral (unsegmented); mantle secreting external shell.</td>
            <td>Aragonite and Calcite ($\text{CaCO}_3$).</td>
            <td>Mesozoic to <strong>Present (Apex diversity)</strong>.</td>
          </tr>
          <tr>
            <td><strong>Brachiopoda</strong></td>
            <td>Bilateral plane passes <em>through</em> each valve (equilateral, inequivalve).</td>
            <td>Low-Mg Calcite or Calcium Phosphate (Lingulids).</td>
            <td><strong>Paleozoic</strong> (Ordovician to Permian).</td>
          </tr>
          <tr>
            <td><strong>Echinodermata</strong></td>
            <td>Pentameral (5-fold) radial symmetry; water vascular system.</td>
            <td>Single-crystal High-Mg Calcite with porous stereom.</td>
            <td>Paleozoic (Crinoids) to Recent (Echinoids).</td>
          </tr>
          <tr>
            <td><strong>Arthropoda</strong></td>
            <td>Bilateral; metameric segmentation; jointed appendages.</td>
            <td>Chitin mineralized with Calcite/Apatite.</td>
            <td>Cambrian (Trilobites) to Present (Insects/Crustaceans).</td>
          </tr>
          <tr>
            <td><strong>Cnidaria</strong></td>
            <td>Radial or biradial; stinging cnidocytes; solitary or colonial.</td>
            <td>Calcite (Rugosa/Tabulata) or Aragonite (Scleractinia).</td>
            <td>Ordovician to Present (Major reef builders).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 69</div>
        <div class="q-text">Common kinds of invertebrate fossils include __m_., brachiopods, echinoderms, arthropods, and cnidarians.</div>
        <div class="q-options">
          <div class="opt-node correct">(A) molluscs</div>
          <div class="opt-node">(B) nautiloids</div>
          <div class="opt-node">(C) cephalopoda</div>
          <div class="opt-node">(D) All of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(A) molluscs</strong> [The coordinate phylum-level taxon completing the five major invertebrate fossil phyla and matching the prompt clue '__m_.' is molluscs (Phylum Mollusca).]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (A) molluscs</div>
    <div class="card-body">
      <p><strong>Detailed Invertebrate Paleontological Forensic Analysis:</strong></p>
      <ul>
        <li>In standard textbook paleontology (Clarkson 1998, Ch. 1; Mahapatra 2019, Ch. 18, p. 344; Boardman 1987), the marine invertebrate fossil record is dominated by five primary coordinate animal <strong>Phyla</strong>:
          <ol>
            <li><strong>Phylum Mollusca (molluscs)</strong></li>
            <li>Phylum Brachiopoda (brachiopods)</li>
            <li>Phylum Echinodermata (echinoderms)</li>
            <li>Phylum Arthropoda (arthropods)</li>
            <li>Phylum Cnidaria (cnidarians)</li>
          </ol>
        </li>
        <li>The examination prompt explicitly provides the orthographic clue <strong>"__m_."</strong>, which matches the phylum name <strong>molluscs</strong>.</li>
        <li>Furthermore, because brachiopods, echinoderms, arthropods, and cnidarians are all named at the <em>phylum level</em>, the missing coordinate peer must be the phylum <strong>molluscs</strong>.</li>
        <li>Therefore, Option <strong>(A) molluscs</strong> is the singular correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) nautiloids</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>"Nautiloids" (Subclass Nautiloidea) represents a lower-ranking subordinate taxonomic division within the Class Cephalopoda of the Phylum Mollusca.</li>
        <li>It is not coordinate in taxonomic rank with the phyla Brachiopoda or Echinodermata, nor does it begin with 'm'.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (C) cephalopoda</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>"Cephalopoda" is a taxonomic <strong>class</strong> within the Phylum Mollusca, excluding other major fossil molluscs like Bivalvia (pelecypods) and Gastropoda (snails).</li>
        <li>Listing Cephalopoda would omit the vast majority of fossil molluscs and violates coordinate phylum-level parallelism.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) All of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because only Option (A) molluscs represents the coordinate phylum matching the prompt syntax and clue, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Major Classes of the Phylum Mollusca</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Class of Mollusca</th>
            <th>Shell Morphology</th>
            <th>Symmetry Plan</th>
            <th>Primary Geologic Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Bivalvia (Pelecypoda)</strong></td>
            <td>Two lateral valves (right and left); hinged dorsally by teeth/ligament.</td>
            <td>Symmetry plane between valves (equivalve, inequilateral).</td>
            <td>Dominant Mesozoic-Cenozoic benthic filter feeders (oysters, clams, rudists).</td>
          </tr>
          <tr>
            <td><strong>Gastropoda</strong></td>
            <td>Single unchambered univalve shell; usually coiled helically (dextral/sinistral).</td>
            <td>Asymmetrical due to developmental torsion.</td>
            <td>Herbivores, carnivores, and drillers (<em>Natica, Murex</em>) from Cambrian to Present.</td>
          </tr>
          <tr>
            <td><strong>Cephalopoda</strong></td>
            <td>External or internal chambered phragmocone with siphuncle; septa.</td>
            <td>Planispiral bilateral symmetry.</td>
            <td>Apex pelagic predators and <strong>premier Mesozoic index fossils (Ammonites)</strong>.</td>
          </tr>
          <tr>
            <td><strong>Scaphopoda</strong></td>
            <td>Tusk-shaped tubular shell open at both ends.</td>
            <td>Bilateral cylindrical symmetry.</td>
            <td>Infaunal benthic deposit feeders (<em>Dentalium</em>).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Invertebrate Morphology & Shell Geometries</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Bivalve vs. Brachiopod Symmetry Plane</div>
        <p>State the fundamental geometric law that distinguishes a bivalve mollusc shell from a brachiopod shell in field hand specimens.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Bivalve Mollusc (Pelecypoda):</strong> The plane of bilateral symmetry passes <strong>between the two valves</strong> (along the commissure). The right valve is a mirror image of the left valve (<strong>equivalve</strong>), but each individual valve is asymmetrical about its midline (<strong>inequilateral</strong>).</li>
          <li><strong>Brachiopod:</strong> The plane of bilateral symmetry passes <strong>vertically through the center of each valve</strong> (from beak to anterior margin). Each individual valve is symmetrical (<strong>equilateral</strong>), but the pedicle valve is larger and differently shaped than the brachial valve (<strong>inequivalve</strong>).</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Raup's Geometric Coiling Parameters</div>
        <p>David Raup (1966) quantified all coiled mollusc shell geometries using four mathematical parameters. Name them.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
          <li><strong>Shape of Generating Curve ($S$):</strong> Ratio of whorl height to whorl width.</li>
          <li><strong>Whorl Expansion Rate ($W$):</strong> Rate at which the cross-sectional area increases per revolution ($W = [r_2/r_1]^2$).</li>
          <li><strong>Distance of Generating Curve from Coiling Axis ($D$):</strong> Governs whether the shell is tight and overlapping ($D \le 0$) or open and umbilicate ($D > 0$).</li>
          <li><strong>Translation Rate ($T$):</strong> Rate of movement of whorls down the vertical axis of coiling ($T = 0$ for planispiral ammonites; $T > 0$ for helical gastropods).</li>
        </ol>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: Rudist Bivalves as Cretaceous Reef Builders</div>
        <p>What bizarre morphological adaptation allowed rudist bivalves to outcompete scleractinian corals during the Cretaceous?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Rudists (e.g., <em>Hippurites, Radiolites</em>) modified their right valve into a conical, cylindrical horn up to a meter tall cemented to the seafloor, while the left valve shrank into a small, flat lid (operculum). Harboring photosynthetic endosymbionts in their fleshy mantle, they constructed giant biostromal carbonate reefs across the warm Tethyan shelf until their extinction at the K-Pg boundary.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Gastropod Torsion vs. Helical Coiling</div>
        <p>Explain the developmental difference between gastropod <em>torsion</em> and <em>coiling</em>.</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Torsion:</strong> A unique $180^\circ$ counterclockwise rotation of the visceral mass, mantle, and nervous system relative to the head and foot during larval veliger ontogeny, bringing the mantle cavity, gills, and anus directly over the head.</li>
          <li><strong>Coiling:</strong> The geometric spiral growth of the calcium carbonate shell along a helical axis, which evolved independently for hydrodynamic balance and compact housing.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Aragonite vs. Calcite Preservation in Molluscs</div>
        <p>Why do fossil oysters and scallops preserve exquisite fine shell detail in Paleozoic-Mesozoic rocks, while aragonitic clams occur only as hollow molds?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Oysters and scallops secrete shells of <strong>stable low-magnesium calcite</strong>, which resists groundwater dissolution. Most other bivalves and gastropods secrete shells of <strong>metastable aragonite</strong>. During diagenesis, meteoric pore fluids readily dissolve aragonite, leaving empty void molds that are subsequently cast by silica or calcite spar.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: The Radula as a Molluscan Synapomorphy</div>
        <p>What unique anatomical feeding organ unites all classes of Mollusca except Bivalvia?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>radula</strong>—a chitinous, ribbon-like tongue covered in rows of microscopic, replaceable siliceous or chitinous teeth used to scrape algae, bore holes through prey shells, or tear meat. Bivalves lost the radula secondarily when they evolved specialized ciliated filter-feeding gills (ctenidia).</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Echinoderm Stereom Microstructure</div>
        <p>How does a petrologist recognize an echinoderm fossil fragment in a carbonate thin section?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Each skeletal plate or spine of an echinoderm (crinoid ossicle, echinoid spine) behaves under cross-polarized light as a <strong>single optically continuous crystal of high-magnesium calcite</strong> that goes to unit extinction simultaneously. The micro-sponge internal porosity is termed <strong>stereom</strong>, which is diagenetically filled by syntaxial rim calcite overgrowths in optical continuity.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Paleozoic Domination of Brachiopods vs. Post-Paleozoic Molluscs</div>
        <p>What global event caused the dramatic macroevolutionary transition wherein bivalve molluscs replaced brachiopods as the dominant shallow-marine filter feeders?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The <strong>Permian-Triassic Mass Extinction ($\sim 252\text{ Ma}$)</strong> wiped out $>95\%$ of all marine species, including over $90\%$ of brachiopod genera. In the surviving Triassic seas, infaunal siphonate bivalves (capable of burrowing deeply to escape predators) outcompeted stationary epifaunal brachiopods, achieving complete ecological dominance in the Mesozoic Marine Revolution.</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 69, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q069_Invertebrate_Fossil_Phyla_Mollusca_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q069: {out_path} ({len(html)} bytes)")


# ==============================================================================
# Q070: Ammonite Biostratigraphy & Cretaceous Index Fossils
# ==============================================================================
def generate_q070():
    title = r"Q070: Cephalopod Biostratigraphy: Ammonites as Master Mesozoic & Cretaceous Index Fossils | OPSC Geology 2021 Masterclass"
    badge = "GEO - 2/21 • Cephalopod Biostratigraphy & Index Fossils"
    h1_title = "Q070: Ammonites: Master Mesozoic & Cretaceous Index Fossils"
    meta_text = """<strong>Official Exam:</strong> OPSC Assistant Geologist Paper-II (2021), Question 70<br>
<strong>Authoritative References:</strong> G.B. Mahapatra, <em>A Text-Book of Geology</em> (pp. 354–358, Fig. 91.4); P.K. Mukherjee, <em>A Text Book of Geology</em> (p. 215); W.J. Kennedy & C.W. Wright, <em>Evolution and Biostratigraphy of Cretaceous Ammonites</em> (Paleontology Special Paper, 1985); E.N.K. Clarkson, <em>Invertebrate Palaeontology and Evolution</em> (Ch. 8)."""

    part1 = r"""
  <!-- CARD 1: AMMONITES IN THE CRETACEOUS -->
  <div class="card">
    <div class="card-header bg-blue">1. The Ammonite Climax: Cretaceous Marine Biozonation</div>
    <div class="card-body">
      <p>Ammonoids (Subclass <strong>Ammonoidea</strong>, Order Ammonitida) represent the ultimate index fossils of the <strong>Mesozoic Era</strong>, exhibiting spectacular diversity, morphological plasticity, and rapid evolutionary turnover throughout the Triassic, Jurassic, and <strong>Cretaceous Periods</strong>:</p>

      <ul>
        <li><strong>Why Ammonites are Supreme Index Fossils:</strong>
          <ol>
            <li><strong>Rapid Morphological Evolution:</strong> Suture lines, ribbing patterns, keel developments, and whorl dimensions evolved so rapidly that individual species durations (biochrons) averaged less than <strong>$500,000$ to $1\text{ million years}$</strong>.</li>
            <li><strong>Global Cosmopolitan Distribution:</strong> As free-swimming nektonic pelagic organisms with gas-filled chambered phragmocones, ammonites dispersed freely across ocean basins, untethered to local seafloor sediment facies.</li>
            <li><strong>High Fossilization Potential:</strong> Abundant, mineralized aragonitic shells with durable internal septa preserved in clays, limestones, and concretions worldwide.</li>
          </ol>
        </li>
        <li><strong>The Cretaceous Climax & Heteromorph Bloom:</strong> During the <strong>Cretaceous Period</strong>, ammonites underwent an extraordinary final evolutionary radiation characterized by:
          <ul>
            <li>Classic planispiral forms: <em>Acanthoceras, Mortoniceras, Pachydiscus, Placenticeras</em>.</li>
            <li>Specialized <strong>heteromorph ammonites</strong> (uncoiled or bizarrely shaped shells): straight shafts (<em>Baculites</em>), hooked forms (<em>Scaphites, Hamites</em>), and helically coiled forms (<em>Turrilites</em>).</li>
          </ul>
        </li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q70/pkm_p215_jurassic_cretaceous_ammonite_zones.png" alt="Jurassic Cretaceous Ammonite Zones">
        <div class="tb-caption">
          <strong>Figure 70.1 (P.K. Mukherjee, p. 215):</strong> Global biostratigraphic ammonite biozonation scheme of the Jurassic and Cretaceous Systems, documenting species-level index fossils defining stages worldwide.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 2: AMMONITIC SUTURE LINE EVOLUTION -->
  <div class="card">
    <div class="card-header bg-indigo">2. The Evolution of Ammonitic Suture Complexity</div>
    <div class="card-body">
      <p>The intersection of internal chambered septa with the outer shell wall produces the <strong>suture line</strong>, the master diagnostic key in ammonoid taxonomy:</p>

      <div class="formula-card">
        <div class="formula-title">The Four Evolutionary Stages of Cephalopod Sutures</div>
        $$\mathbf{\text{Nautilitic}} \text{ (Smooth)} \longrightarrow \mathbf{\text{Goniatitic}} \text{ (Angular)} \longrightarrow \mathbf{\text{Ceratitic}} \text{ (Denticulate Lobes)} \longrightarrow \mathbf{\text{Ammonitic}} \text{ (Frilled Lobes \& Saddles)}$$
      </div>

      <ul>
        <li><strong>Nautilitic (Cambrian - Present):</strong> Simple, gently undulating or straight line (e.g., modern <em>Nautilus</em>).</li>
        <li><strong>Goniatitic (Devonian - Permian):</strong> Both lobes and saddles are completely smooth and undivided; lobes are angular V-shaped pointing backward.</li>
        <li><strong>Ceratitic (Triassic):</strong> Saddles are smooth and rounded, while lobes are denticulated, saw-toothed, or serrated (e.g., <em>Ceratites</em>).</li>
        <li><strong>Ammonitic (Jurassic - Cretaceous):</strong> Maximum complexity; both lobes and saddles are deeply, intricately subdivided into frilled, dendritic, leaf-like foliations (e.g., <em>Acanthoceras, Pachydiscus</em>).</li>
      </ul>

      <div class="tb-figure">
        <img src="../../figures_Q70/mahapatra_fig91_4_ammonitic_suture_lines.png" alt="Ammonitic Suture Lines from Mahapatra">
        <div class="tb-caption">
          <strong>Figure 70.2 (G.B. Mahapatra, Fig. 91.4):</strong> Stepwise morphological evolution of cephalopod suture lines: Nautilitic $\to$ Goniatitic $\to$ Ceratitic $\to$ Ammonitic.
        </div>
      </div>
    </div>
  </div>

  <!-- CARD 3: COMPARISON OF MESOZOIC CEPHALOPODS -->
  <div class="card">
    <div class="card-header bg-emerald">3. Detailed Matrix: Diagnostic Cretaceous Ammonite Biozones</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Cretaceous Stage</th>
            <th>Primary Global Index Ammonite Genera</th>
            <th>Shell Form / Suture Type</th>
            <th>Indian Outcrop Horizon</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Maastrichtian</strong> (Terminal)</td>
            <td><strong><em>Pachydiscus, Sphenodiscus, Baculites</em></strong></td>
            <td>Planispiral ribbed / straight-shaft heteromorph; complex ammonitic.</td>
            <td>Ariyalur Group (Cauvery Basin, Tamil Nadu).</td>
          </tr>
          <tr>
            <td><strong>Campanian</strong></td>
            <td><strong><em>Placenticeras, Scaphites, Hoplitoplacenticeras</em></strong></td>
            <td>Involute compressed / hooked heteromorph; dendritic sutures.</td>
            <td>Upper Trichinopoly & Sillakkudi Formations.</td>
          </tr>
          <tr>
            <td><strong>Turonian - Coniacian</strong></td>
            <td><strong><em>Collignoniceras, Romaniceras, Lewesiceras</em></strong></td>
            <td>Evolute, prominently tuberculate and keeled shells.</td>
            <td>Trichinopoly Group (Garudamangalam).</td>
          </tr>
          <tr>
            <td><strong>Cenomanian</strong></td>
            <td><strong><em>Acanthoceras, Mantelliceras, Calycoceras</em></strong></td>
            <td>Robust, square whorls with heavy spines and tubercles.</td>
            <td>Upper Uttatur Group (Karai, Tamil Nadu).</td>
          </tr>
          <tr>
            <td><strong>Albian</strong></td>
            <td><strong><em>Mortoniceras, Schloenbachia, Hysteroceras</em></strong></td>
            <td>Compressed, strongly keeled, bifurcating ribs.</td>
            <td>Lower Uttatur Group & Bagh Beds (MP).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

    part2 = r"""
  <!-- QUESTION CARD -->
  <div class="card">
    <div class="card-header bg-slate">Official Examination Question</div>
    <div class="card-body">
      <div class="question-box">
        <div class="q-num">Question 70</div>
        <div class="q-text">Ammonite is a characteristic marine fossil of ___ age around the world and considered an index fossil because of its diverse nature.</div>
        <div class="q-options">
          <div class="opt-node">(A) Palaeozoic</div>
          <div class="opt-node">(B) Cambrian to Silurian</div>
          <div class="opt-node correct">(C) Cretaceous-age</div>
          <div class="opt-node">(D) None of these</div>
        </div>
      </div>

      <div class="ans-banner">
        Verified Correct Answer: <strong>(C) Cretaceous-age</strong> [Ammonites are globally characteristic index fossils of the Mesozoic Era, reaching immense diversity and biostratigraphic utility in the Cretaceous Period before their end-Cretaceous extinction.]
      </div>
    </div>
  </div>

  <!-- CRITICAL DISSECTION CARDS -->
  <div class="card option correct">
    <div class="card-header bg-green">Correct Option: (C) Cretaceous-age</div>
    <div class="card-body">
      <p><strong>Detailed Biostratigraphic Forensic Analysis:</strong></p>
      <ul>
        <li>Ammonites (Order Ammonitida, possessing true ammonitic sutures) are the definitive marine index fossils of the Mesozoic Era (Triassic, Jurassic, and <strong>Cretaceous</strong>).</li>
        <li>Among the given options, the <strong>Cretaceous-age</strong> represents the premier epoch where ammonites diversified into dozens of global index zones (e.g., <em>Acanthoceras, Mortoniceras, Pachydiscus, Scaphites, Baculites</em>) before suffering sudden and complete mass extinction at the Cretaceous-Paleogene (K-Pg) boundary ($66\text{ Ma}$).</li>
        <li>In Indian stratigraphy, the Cretaceous marine beds of the Cauvery Basin (Uttatur and Ariyalur groups) and the Narmada Bagh beds are dated worldwide using these Cretaceous ammonite index zones.</li>
        <li>Therefore, Option <strong>(C) Cretaceous-age</strong> is the verified and correct answer.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (A) Palaeozoic</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>In the Paleozoic Era (Devonian to Permian), ammonoids were represented by primitive <em>goniatites</em> (Order Goniatitida) possessing simple, smooth V-shaped sutures.</li>
        <li>True <strong>ammonites</strong> with complex ammonitic sutures had not yet evolved in the Paleozoic; they are strictly Mesozoic organisms.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (B) Cambrian to Silurian</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>During the Cambrian, Ordovician, and Silurian, the only cephalopods in existence were primitive <strong>nautiloids</strong> (straight orthoceratids and endoceratids with simple smooth sutures).</li>
        <li>Ammonoids had not even originated yet; the first primitive ammonoids appeared in the Early Devonian. Thus, this option is chronologically impossible.</li>
      </ul>
    </div>
  </div>

  <div class="card option wrong">
    <div class="card-header bg-red">Incorrect Distractor: (D) None of these</div>
    <div class="card-body">
      <p><strong>Detailed Refutation:</strong></p>
      <ul>
        <li>Because Option (C) Cretaceous-age correctly designates the Mesozoic age of ammonite index fossils, Option (D) is incorrect.</li>
      </ul>
    </div>
  </div>
"""

    part3 = r"""
  <!-- SYNTHESIS TABLE -->
  <div class="card">
    <div class="card-header bg-slate">Comprehensive Synthesis: Cephalopod Evolutionary Chronology</div>
    <div class="card-body">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>Geological Era / Period</th>
            <th>Dominant Cephalopod Group</th>
            <th>Characteristic Suture Style</th>
            <th>Extinction / Survival Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Cambrian to Silurian</strong></td>
            <td>Nautiloidea (Orthoconic & coiled)</td>
            <td><strong>Nautilitic</strong> (Simple, straight, smooth lines).</td>
            <td>Survived all mass extinctions; living today as <em>Nautilus</em>.</td>
          </tr>
          <tr>
            <td><strong>Devonian to Permian</strong></td>
            <td>Goniatitida (Primitive Ammonoids)</td>
            <td><strong>Goniatitic</strong> (Smooth angular lobes and rounded saddles).</td>
            <td>Decimated at end-Permian extinction ($252\text{ Ma}$).</td>
          </tr>
          <tr>
            <td><strong>Triassic</strong></td>
            <td>Ceratitida (Intermediate Ammonoids)</td>
            <td><strong>Ceratitic</strong> (Rounded saddles, denticulate saw-toothed lobes).</td>
            <td>Decimated at end-Triassic extinction ($201\text{ Ma}$).</td>
          </tr>
          <tr>
            <td><strong>Jurassic to Cretaceous</strong> (Target)</td>
            <td><strong>Ammonitida (True Ammonites & Heteromorphs)</strong></td>
            <td><strong>Ammonitic</strong> (Deeply frilled, complex dendritic lobes and saddles).</td>
            <td><strong>Completely Extinct at the K-Pg Boundary ($66\text{ Ma}$).</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8 WORKED PRACTICE PROBLEMS -->
  <div class="card">
    <div class="card-header bg-purple">High-Yield Practice Problems: Cephalopod Mechanics & Biochronology</div>
    <div class="card-body">

      <div class="practice-box">
        <div class="practice-title">Problem 1: Siphuncular Buoyancy Regulation</div>
        <p>How did the vascularized siphuncle tube regulate buoyancy in living ammonites?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>The siphuncle is a living vascular cord running through the chambered phragmocone. Using active ion-transport enzymes, it pumps sodium and chloride ions out of the chamber liquid into the blood, creating an osmotic gradient. Water follows osmotically into the blood, leaving the closed chamber partially empty at vacuum pressure. Gas ($\text{N}_2, \text{O}_2, \text{CO}_2$) diffuses into the cavity, allowing the ammonite to maintain <strong>neutral buoyancy</strong> at variable depths.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 2: Baculites as a Straight-Shelled Cretaceous Index Fossil</div>
        <p>Why did the Cretaceous ammonite genus <em>Baculites</em> evolve a straight, uncoiled shell, and how is it distinguished from a Paleozoic orthocone nautiloid?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Adaptation:</strong> <em>Baculites</em> evolved a vertical, needle-like shell to feed on vertical migrations of zooplankton in the water column with minimal hydrodynamic drag.</li>
          <li><strong>Distinction from Nautiloids:</strong> An orthoconic nautiloid has simple, straight, smooth nautilitic sutures and a central siphuncle. <em>Baculites</em> exhibits extraordinarily complex, deeply frilled <strong>ammonitic sutures</strong> and a strictly marginal ventral siphuncle.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 3: The Aptychus and Anaptychus</div>
        <p>What were <em>aptychi</em> (singular: aptychus) in ammonite paleontology, and what was their function?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Aptychi are paired, calcified, bivalved-like plates found in the body chamber of ammonites. Originally mistaken for bivalve shells, modern soft-tissue fossils prove they functioned primarily as a rigid <strong>operculum (protective door)</strong> to seal the aperture when the head retracted, and secondarily as the lower jaw element of the biting beak.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 4: Heteromorph Turrilites Coiling Geometry</div>
        <p>What unusual coiling geometry characterizes the Cretaceous index genus <em>Turrilites</em>?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><em>Turrilites</em> exhibits <strong>trochospiral (helicoid) coiling</strong>, resembling a high-spired gastropod (snail) shell. However, it is an authentic ammonite possessing chambered septa, an external marginal siphuncle, and intricate ammonitic sutures ornamented with multiple rows of sharp tubercles.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 5: Involute vs. Evolute Ammonite Hydrodynamics</div>
        <p>Compare the swimming efficiency of an <em>involute oxyconic</em> ammonite (e.g., <em>Placenticeras</em>) with an <em>evolute serpenticonic</em> ammonite (e.g., <em>Dactylioceras</em>).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <ul>
          <li><strong>Involute Oxycone:</strong> Inner whorls completely covered by the outer whorl, narrow knife-like cross-section with sharp venter. Very low drag coefficient ($C_d \approx 0.2$), designed for <strong>rapid nektonic pursuit swimming</strong> in open waters.</li>
          <li><strong>Evolute Serpenticone:</strong> All whorls exposed in a flat coil like a coiled snake, wide contact with water. High drag coefficient ($C_d > 0.8$), designed for slow, stable maneuverability in demersal benthic habitats.</li>
        </ul>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 6: Cause of Ammonite K-Pg Extinction vs. Nautiloid Survival</div>
        <p>Why did ammonites go completely extinct at the K-Pg boundary while nautiloids survived into the modern era?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Ammonites laid tiny eggs ($<1-2\text{ mm}$) that hatched into microscopic, planktotrophic larvae feeding in the uppermost sunlit ocean surface waters. When the Chicxulub asteroid impact and Deccan volcanism shut down ocean photosynthesis, the surface plankton collapsed, starving all ammonite hatchlings. In contrast, nautiloids laid large, yolk-rich eggs ($>25-30\text{ mm}$) directly on the deep sea floor that hatched as miniature scavenging adults feeding on deep-sea carrion, insulating them from surface food chain collapse.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 7: Sphenodiscus in the Fox Hills Sandstone</div>
        <p>What ammonite genus marks the terminal Maastrichtian biozone directly below the K-Pg boundary in North America and India?</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p><strong><em>Sphenodiscus lenticularis</em></strong> (Family Sphenodiscidae). It possesses a strongly compressed, lens-shaped shell with pseudoceratitic/ammonitic sutures, marking the final ammonite biozone of the Mesozoic Era.</p>
      </div>

      <div class="practice-box">
        <div class="practice-title">Problem 8: Ammonite Shell Implosion Depth Calculation</div>
        <p>If the aragonitic outer shell of an ammonite has tensile strength $\sigma_{\text{tensile}} = 100\text{ MPa}$, radius $R = 10\text{ cm}$, and wall thickness $t = 1.0\text{ mm}$, calculate the maximum theoretical implosion depth in meters ($g = 9.8\text{ m/s}^2, \rho_{\text{water}} = 1025\text{ kg/m}^3$).</p>
        <p><strong>Step-by-Step Solution:</strong></p>
        <p>Using thin-walled spherical shell stress formula: $\sigma = \frac{P R}{2t} \implies P_{\text{implosion}} = \frac{2 t \sigma}{R}$.</p>
        $$P = \frac{2 \times (1.0 \times 10^{-3}\text{ m}) \times (100 \times 10^6\text{ Pa})}{0.10\text{ m}} = \frac{2.0 \times 10^5}{0.10} = 2.0 \times 10^6\text{ Pa} = 2.0\text{ MPa}$$
        $$P = \rho g h \implies h = \frac{P}{\rho g} = \frac{2.0 \times 10^6\text{ Pa}}{1025\text{ kg/m}^3 \times 9.8\text{ m/s}^2} = \frac{2.0 \times 10^6}{10,045} \approx 199.1\text{ m}$$
        <p><strong>Final Answer:</strong> The shell would implode at a water depth of approximately $200\text{ meters}$, confirming that ammonites were continental shelf inhabitants!</p>
      </div>

    </div>
  </div>
"""

    html = wrap_html(title, badge, h1_title, meta_text, 70, part1, part2, part3)
    out_path = os.path.join(SOLUTIONS_DIR, "Q070_Ammonite_Index_Fossils_Cretaceous_Mesozoic_Complete_Guide.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated Q070: {out_path} ({len(html)} bytes)")


if __name__ == "__main__":
    generate_q066()
    generate_q067()
    generate_q068()
    generate_q069()
    generate_q070()
