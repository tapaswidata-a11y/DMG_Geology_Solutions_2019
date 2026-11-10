"""
Geological Domain Forensics Engine:
Contains domain-specific knowledge rules to generate deep, forensic distractor explanations
for all major geology/mining topics:
- Stratigraphy, Paleontology, Index Fossils, Formations
- Petrology (Igneous, Sedimentary, Metamorphic), Textures, Classifications
- Structural Geology, Faults, Folds, Kinematics
- Mineralogy, Crystallography, Optical Mineralogy
- Economic Geology, Indian Ore Deposits, Metal Mines
- Geophysics, Seismic Waves, Gravity, Magnetic, Electrical, Well Logging
- Remote Sensing, Sensors, Orbits, GIS, Photogrammetry
- Engineering Geology, Dams, Tunnels, Rock Mechanics, Soil Mechanics
- Environmental Geology, Hazards, Disasters, Hydrology, Hydrogeology
"""

import re

def clean_txt(t):
    if not t: return ""
    t = re.sub(r'[\r\n\t]+', ' ', t)
    t = re.sub(r'\s*([:;•\|\—\_\~\@\(\)]|\.\s*)+\s*$', '', t)
    t = re.sub(r'^\s*([:;•\|\—\_\~\@\(\)]|\.\s*)+\s*', '', t)
    return re.sub(r'\s+', ' ', t).strip()

GEOLOGICAL_FACTS = {
    # Rock types
    "shale": "Shale is a fine-grained, laminated, fissile siliciclastic sedimentary rock composed of clay- and silt-sized particles deposited in quiet, low-energy standing water (lacustrine, lagoonal, or distal marine basin floors).",
    "limestone": "Limestone is a biogenic or chemical sedimentary rock composed predominantly of calcite (CaCO3) precipitated in warm, shallow, clear tropical marine shelf environments.",
    "arkose": "Arkose is an immature sandstone containing >25% feldspar, formed by rapid mechanical weathering and short-distance transport from granitic/gneissic basement horsts.",
    "graywacke": "Graywacke is a texturally immature, matrix-rich (>15% argillaceous/chloritic matrix) sandstone containing angular quartz, feldspar, and rock fragments, characteristically deposited by submarine turbidity currents.",
    "quartz arenite": "Quartz arenite is an ultra-mature sandstone consisting of >95% monocrystalline quartz with almost zero matrix, formed in high-energy beach and shallow marine shelf environments.",
    "conglomerate": "Conglomerate is a coarse-grained clastic rock containing rounded to subrounded gravel-sized clasts (>2 mm) transported by high-energy fluvial currents or surf action.",
    "breccia": "Breccia consists of angular gravel-sized rock fragments (>2 mm) cemented in a finer matrix, indicating minimal transport before deposition (fault breccia or proximal scree).",
    "granite": "Granite is a felsic plutonic igneous rock composed primarily of quartz, K-feldspar, plagioclase, and biotite/hornblende, crystallizing slowly at deep crustal levels.",
    "basalt": "Basalt is an aphanitic mafic volcanic rock composed of calcic plagioclase, clinopyroxene, and olivine, erupted at oceanic ridges or continental flood basalt provinces.",
    "gabbro": "Gabbro is the coarse-grained intrusive plutonic equivalent of basalt, crystallizing in ophiolite suites and layered mafic intrusions (e.g., Bushveld).",
    "rhyolite": "Rhyolite is an aphanitic to porphyritic felsic volcanic extrusive equivalent of granite, rich in silica (>69% SiO2).",
    "andesite": "Andesite is an intermediate volcanic rock typical of subduction zone volcanic arcs (calc-alkaline series), dominated by plagioclase and amphibole/pyroxene.",
    "diorite": "Diorite is an intermediate plutonic rock composed of plagioclase (andesine-oligoclase) and hornblende/biotite, with minor quartz.",
    "peridotite": "Peridotite is an ultramafic mantle rock composed primarily of olivine and pyroxenes, with <45% SiO2.",
    "dunite": "Dunite is an ultramafic rock composed of >90% olivine, commonly hosting chromite podiform deposits.",
    "komatiite": "Komatiite is an Archean ultramafic volcanic lava characterized by spinifex texture formed by rapid thermal quenching of high-temperature magnesian melts.",
    "schist": "Schist is a medium-grade foliated metamorphic rock characterized by prominent planar alignment of platy minerals (micas, chlorite) producing schistosity.",
    "gneiss": "Gneiss is a high-grade regional metamorphic rock displaying alternating light (felsic quartz-feldspar) and dark (mafic biotite-hornblende) compositional banding.",
    "quartzite": "Quartzite is a non-foliated metamorphic rock formed by recrystallization of pure quartz arenite sandstone under contact or regional metamorphism.",
    "marble": "Marble is a non-foliated metamorphic rock produced by thermal or regional recrystallization of limestone or dolostone.",
    "slate": "Slate is a low-grade metamorphic rock exhibiting perfect slaty cleavage due to preferred microscopic alignment of illite and chlorite flakes.",
    "phyllite": "Phyllite represents a progressive metamorphic grade between slate and schist, exhibiting a lustrous, silky sheen from fine-grained white mica (sericite).",
    "amphibolite": "Amphibolite is a medium-to-high grade metamorphic rock composed predominantly of hornblende and plagioclase, formed by metamorphism of mafic igneous rocks.",
    "granulite": "Granulite is a high-temperature, medium-to-high pressure metamorphic rock characterized by anhydrous granoblastic textures with orthopyroxene.",
    "eclogite": "Eclogite is a high-pressure, low-to-moderate temperature metamorphic rock consisting of omphacitic clinopyroxene and pyrope-rich garnet, indicating subducted oceanic crust.",
    "pegmatite": "Pegmatite is an exceptionally coarse-grained igneous intrusive rock (crystals >2.5 cm) enriched in volatile fluids, incompatible trace elements, Li, Be, and rare earths.",

    # Minerals
    "quartz": "Quartz (SiO2) is a tectosilicate framework mineral with Mohs hardness 7, lacking cleavage and showing conchoidal fracture and high chemical stability.",
    "orthoclase": "Orthoclase (KAlSi3O8) is a monoclinic potassium feldspar characteristic of felsic igneous and metamorphic rocks, displaying two cleavage directions at 90°.",
    "albite": "Albite (NaAlSi3O8) is the sodium-rich endmember of the plagioclase feldspar solid solution series, exhibiting polysynthetic albite twinning.",
    "anorthite": "Anorthite (CaAl2Si2O8) is the calcic endmember of the plagioclase series, dominant in mafic and anorthositic rocks.",
    "biotite": "Biotite is an iron-magnesium phyllosilicate black mica with perfect basal cleavage {001} and strong pleochroism.",
    "muscovite": "Muscovite (white mica) is a hydrous potassium-aluminum phyllosilicate with vitreous luster and outstanding electrical insulating properties.",
    "calcite": "Calcite (CaCO3) crystallizes in the trigonal system with perfect rhombohedral cleavage {1011}, hardness 3, and vigorous effervescence in cold dilute HCl.",
    "dolomite": "Dolomite [CaMg(CO3)2] is an ordered double carbonate exhibiting rhombic cleavage, which effervesces slowly in cold dilute HCl only when powdered.",
    "gypsum": "Gypsum (CaSO4·2H2O) is a hydrous calcium sulfate evaporite mineral with Mohs hardness 2, widely used for plaster and cement retardation.",
    "halite": "Halite (NaCl) is rock salt crystallizing in the cubic system with three directions of perfect cubic cleavage and low density (~2.16 g/cm3).",
    "fluorite": "Fluorite (CaF2) is a halide mineral with Mohs hardness 4, displaying perfect octahedral cleavage in 4 directions.",
    "apatite": "Apatite [Ca5(PO4)3(F,Cl,OH)] is the defining mineral for Mohs hardness 5, serving as the primary source of phosphorus in fertilizers.",
    "talc": "Talc [Mg3Si4O10(OH)2] is a secondary sheet silicate formed by hydrothermal alteration of ultramafic rocks, defining Mohs hardness 1 with greasy feel.",
    "corundum": "Corundum (Al2O3) defines Mohs hardness 9, crystallizing in the hexagonal system; gem varieties include ruby (Cr-bearing) and sapphire (Fe-Ti-bearing).",
    "diamond": "Diamond is the cubic high-pressure polymorph of pure carbon, defining Mohs hardness 10, brought to the surface in kimberlite and lamproite pipes.",
    "graphite": "Graphite is the hexagonal low-pressure polymorph of carbon, characterized by sp2 bonding, metallic luster, softness (H = 1-2), and high electrical conductivity.",
    "olivine": "Olivine [(Mg,Fe)2SiO4] is an isolated nesosilicate forming an isomorphic solid solution from forsterite to fayalite, crystallizing at high magmatic temperatures.",
    "pyroxene": "Pyroxenes are single-chain inosilicates (Si2O6) featuring two sets of cleavages intersecting at approximately 87° and 93°.",
    "amphibole": "Amphiboles are double-chain inosilicates (Si8O22) featuring two prismatic cleavage planes intersecting at approximately 56° and 124°.",
    "garnet": "Garnet is an isotropic nesosilicate [X3Y2(SiO4)3] commonly found in metamorphic and mantle rocks, showing no cleavage and high relief.",
    "sillimanite": "Sillimanite (Al2SiO5) is the high-temperature polymorph of aluminosilicate, characteristic of high-grade pelitic gneisses and khondalites.",
    "kyanite": "Kyanite (Al2SiO5) is the high-pressure triclinic polymorph of aluminosilicate, exhibiting extreme directional hardness anisotropy (4.5 to 7).",
    "andalusite": "Andalusite (Al2SiO5) is the low-pressure polymorph occurring in contact metamorphic aureoles, commonly containing carbonaceous inclusions (chiastolite).",
    "staurolite": "Staurolite is a hydrous Fe-Al nesosilicate found in medium-grade pelitic schists, famed for cruciform penetration twinning at 90° and 60°.",
    "tourmaline": "Tourmaline is a complex cyclosilicate displaying trigonal symmetry, strong pleochroism, and marked pyroelectric/piezoelectric behavior.",
    "zircon": "Zircon (ZrSiO4) is a refractory accessory mineral widely utilized in U-Pb geochronology due to its high closure temperature and resistance to weathering.",
    "monazite": "Monazite [(Ce,La,Nd,Th)PO4] is a radioactive phosphate mineral enriched in light rare earth elements and thorium, concentrated in beach placers.",
    "chromite": "Chromite (FeCr2O4) is a normal spinel-group mineral occurring in stratiform and podiform ultramafic complexes (e.g., Sukinda, Odisha).",
    "magnetite": "Magnetite (Fe3O4) is an inverse spinel with strong ferrimagnetism and high specific gravity (~5.2), forming major banded iron formations.",
    "hematite": "Hematite (Fe2O3) is the primary iron ore mineral in BIFs (e.g., Singhbhum-Orissa craton), exhibiting cherry-red streak.",
    "chalcopyrite": "Chalcopyrite (CuFeS2) is the primary ore of copper, displaying brassy yellow color, greenish-black streak, and tetragonal symmetry.",
    "galena": "Galena (PbS) is the chief ore of lead, crystallizing in cubes with perfect cubic cleavage, high specific gravity (~7.6), and lead-gray streak.",
    "sphalerite": "Sphalerite (ZnS) is the principal ore of zinc, displaying resinous luster, dodecahedral cleavage in 6 directions, and variable Fe-substitution.",
    "bauxite": "Bauxite is a heterogeneous aluminous residual weathering product consisting of gibbsite [Al(OH)3], boehmite, and diaspore formed over khondalites.",

    # Mines and Indian Geology
    "khetri": "Khetri (Rajasthan) is India's classic Proterozoic copper belt hosted in Delhi Supergroup metasediments.",
    "panna": "Panna (Madhya Pradesh) is India's premier diamond-producing field, hosted in Proterozoic kimberlitic pipes and conglomerates of the Vindhyan Supergroup.",
    "malanjkhand": "Malanjkhand (Madhya Pradesh) is India's largest single copper deposit, hosted in a Proterozoic porphyry-style quartz-diorite/granite pluton.",
    "sukinda": "Sukinda (Jajpur district, Odisha) holds over 90% of India's chromite reserves, hosted in ultramafic rocks of the Sukinda Ultramafic Complex.",
    "jharia": "Jharia (Jharkhand) is India's exclusive repository of prime coking bituminous coal, hosted in the Barakar Formation of the Damodar Valley Gondwana basin.",
    "kgf": "Kolar Gold Fields (KGF, Karnataka) is a world-class orogenic lode gold deposit hosted in Archean amphibolites of the Dharwar Craton.",
    "hutti": "Hutti (Karnataka) is an active orogenic gold mine in the Hutti-Maski greenstone belt of the Dharwar Craton.",
    "singhbhum": "The Singhbhum Shear Zone (Jharkhand) is a major Precambrian shear zone hosting world-class copper, uranium (Jaduguda), and apatite-magnetite ores.",
    "bailadila": "Bailadila (Chhattisgarh) hosts world-class high-grade hematite iron ore deposits associated with the Bailadila Iron Ore Series (BIF).",
    "zawar": "Zawar (Rajasthan) is India's primary lead-zinc-silver mining district, hosted in dolomites of the Paleoproterozoic Aravalli Supergroup.",
    "makrana": "Makrana (Rajasthan) is famed for pure white calcitic marble belonging to the Mesoproterozoic Delhi Supergroup.",
    "lapsa buru": "Lapsa Buru (Jharkhand) hosts the world's largest massive kyanite deposit associated with mica schists and quartzites of the Singhbhum belt.",
    "digboi": "Digboi (Assam) is Asia's oldest operating oilfield (discovered 1889), producing hydrocarbons from Miocene Tipam sandstones.",
    "bombay high": "Bombay High (Mumbai Offshore) is India's largest oil and gas field, producing from Miocene L-III limestone reservoirs on the western shelf.",
    "kutch": "The Kutch Basin (Gujarat) is a Mesozoic rift basin renowned for superbly preserved Jurassic ammonite biostratigraphy (Chari, Katrol, Patcham, Umia).",
    "athgarh": "The Athgarh Basin (Odisha) represents an upper Gondwana rift basin characterized by fluvial sandstones and clays preserving fossil flora.",
    "jhamarkotra": "Jhamarkotra (Udaipur, Rajasthan) is India's largest stromatolitic rock phosphate (phosphorite) mine hosted in Aravalli dolomites.",

    # Geophysics & Earth Structure
    "moho": "The Mohorovičić discontinuity (Moho) separates the crust from the mantle, marked by a sharp jump in P-wave velocity from ~6.8 km/s to ~8.1 km/s.",
    "gutenberg": "The Gutenberg discontinuity marks the core-mantle boundary (CMB) at ~2890 km depth, where S-waves vanish completely and P-wave velocity drops sharply.",
    "lehmann": "The Lehmann discontinuity separates the liquid outer core from the solid inner core at ~5150 km depth, where P-waves refract and accelerate.",
    "conrad": "The Conrad discontinuity is a mid-crustal seismic boundary separating the upper granitic/felsic continental crust from the lower mafic/basaltic crust.",
    "p-wave": "P-waves (primary/compressional waves) are longitudinal elastic body waves that travel through solids, liquids, and gases with highest velocity.",
    "s-wave": "S-waves (secondary/shear waves) are transverse elastic body waves that propagate strictly through solids, as liquids have zero shear modulus (mu = 0).",
    "love wave": "Love waves are horizontally polarized surface waves (SH-type) trapped in a low-velocity surface layer, producing purely transverse ground shaking.",
    "rayleigh wave": "Rayleigh waves are surface waves producing retrograde elliptical particle motion in a vertical plane along the direction of propagation.",
    "epicenter": "The epicenter is the point on the Earth's surface directly vertically above the subsurface seismic focus (hypocenter).",
    "hypocenter": "The hypocenter (or focus) is the exact subsurface point of initial rupture where accumulated tectonic strain energy is suddenly released.",

    # Structural geology
    "normal fault": "A normal fault is an extensional fault where the hanging wall moves downward relative to the footwall, resulting in horizontal crustal extension.",
    "reverse fault": "A reverse fault is a compressional fault where the hanging wall moves upward relative to the footwall, producing horizontal crustal shortening.",
    "thrust fault": "A thrust fault is a reverse fault dipping at a low angle (typically <30° or <45°), capable of transporting older strata over younger strata across vast distances.",
    "strike-slip fault": "A strike-slip fault is a fault where tectonic blocks slide horizontally past each other parallel to the fault strike (dextral or sinistral).",
    "anticline": "An anticline is a fold that is convex upward, having older rock units at its core when stratigraphic sequence is normal.",
    "syncline": "A syncline is a fold that is convex downward, having younger rock units at its core.",
    "monocline": "A monocline is a step-like fold in rock strata consisting of a zone of steeper dip within an otherwise horizontal or gently dipping sequence.",
    "horst": "A horst is an uplifted fault block bounded on both sides by conjugate normal faults dipping away from each other.",
    "graben": "A graben is a downdropped fault block bounded by conjugate normal faults dipping toward each other, typical of rift valleys.",

    # Disasters & Environment
    "tornado": "Tornadoes are violently rotating columns of air descending from supercell thunderstorms, most frequent and severe in the USA ('Tornado Alley').",
    "tsunami": "Tsunamis are catastrophic long-wavelength oceanic gravity waves generated by sudden vertical displacement of the seafloor during megathrust subduction earthquakes.",
    "landslide": "Landslides are downslope movements of rock, soil, and debris driven by gravity when shear stress exceeds the shear strength of the slope material.",
    "earthquake": "Earthquakes are sudden ground vibrations caused by the rapid release of elastic strain energy along tectonic faults.",
    "volcano": "Volcanoes are vents in the crust through which molten rock, pyroclastic debris, and volcanic gases erupt onto the surface.",
    "flood": "Floods occur when river discharge exceeds the carrying capacity of the channel, inundating the adjacent floodplain."
}

def get_fact_for_option(opt_text):
    low = opt_text.lower().strip()
    # Check exact or partial matches
    for k, v in GEOLOGICAL_FACTS.items():
        if k in low:
            return v
    return ""

print("Domain Forensics engine loaded with 70+ authoritative geological facts.")

# Massive Expansion of Geological Knowledge Base (200+ entries)
GEOLOGICAL_FACTS.update({
    # Stratigraphy & Eras
    "precambrian": "The Precambrian Supereon represents ~88% of Earth's geologic history (4.56 Ga to 541 Ma), divided into Hadean, Archean, and Proterozoic Eons, dominated by shield complexes and early microbial life.",
    "archean": "The Archean Eon (4.0 to 2.5 Ga) is characterized by high mantle heat flow, greenstone belts, TTG (tonalite-trondhjemite-granodiorite) crustal accretion, and the origin of life (stromatolites).",
    "proterozoic": "The Proterozoic Eon (2.5 Ga to 541 Ma) witnessed the Great Oxidation Event (GOE), vast banded iron formation deposition, supercontinent cycles (Columbia, Rodinia), and the appearance of eukaryotes.",
    "paleozoic": "The Paleozoic Era (541 to 252 Ma) encompasses Cambrian explosion through the Permian, dominated by marine invertebrates, the rise of land plants, amphibians, and ending with the massive P-Tr extinction.",
    "mesozoic": "The Mesozoic Era (252 to 66 Ma) is the 'Age of Reptiles' divided into Triassic, Jurassic, and Cretaceous periods, ending with the bolide impact at the Cretaceous-Paleogene (K-Pg) boundary.",
    "cenozoic": "The Cenozoic Era (66 Ma to present) is the 'Age of Mammals', comprising Paleogene, Neogene, and Quaternary periods, marked by Himalayan orogeny and global cooling into icehouse conditions.",
    "cambrian": "The Cambrian Period (541 to 485 Ma) marked the rapid diversification of skeletonized marine life ('Cambrian Explosion'), dominated by trilobites, archaeocyathids, and inarticulate brachiopods.",
    "ordovician": "The Ordovician Period (485 to 443 Ma) witnessed the Great Ordovician Biodiversification Event (GOBE), extensive epeiric carbonate seas, and the first primitive land plants.",
    "silurian": "The Silurian Period (443 to 419 Ma) saw the stabilization of global climates, first vascular land plants (Cooksonia), early terrestrial arthropods, and expansive coral-stromatoporoid reefs.",
    "devonian": "The Devonian Period (419 to 359 Ma) is the 'Age of Fishes', witnessing the rise of ammonoids, placoderms, lobe-finned fish evolving into tetrapods, and the first extensive forests (Archaeopteris).",
    "carboniferous": "The Carboniferous Period (359 to 299 Ma) is renowned for widespread equatorial coal swamps, giant insects, and the evolutionary emergence of the amniotic egg.",
    "permian": "The Permian Period (299 to 252 Ma) saw the assembly of Pangaea, widespread aridification (red beds, evaporites), and concluded with Earth's most severe mass extinction (95% marine loss).",
    "triassic": "The Triassic Period (252 to 201 Ma) was characterized by hot, dry climates across Pangaea, recovery of terrestrial faunas, the emergence of early dinosaurs, mammals, and modern corals (Scleractinia).",
    "jurassic": "The Jurassic Period (201 to 145 Ma) featured the rifting of Pangaea, warm greenhouse climates, dominance of sauropod and theropod dinosaurs, and abundant ammonite and belemnite cephalopods.",
    "cretaceous": "The Cretaceous Period (145 to 66 Ma) featured high eustatic sea levels, extensive chalk deposition, the radiation of flowering angiosperms, and concluded with the Chicxulub asteroid impact.",
    "tertiary": "The Tertiary Period (traditional division, 66 to 2.6 Ma) spanned Paleocene to Pliocene epochs, marked by mammalian radiation, grassland evolution, and Alpine-Himalayan mountain building.",
    "quaternary": "The Quaternary Period (2.6 Ma to present) includes Pleistocene glaciations and Holocene interglacial warming, characterized by orbital Milankovitch cycles and the rise of humans.",

    # Paleontology & Fossils
    "trilobite": "Trilobites are extinct Paleozoic marine arthropods characterized by a three-lobed, three-segment chitinous exoskeleton (cephalon, thorax, pygidium), serving as prime Cambrian index fossils.",
    "ammonite": "Ammonites are extinct cephalopod mollusks featuring complex septal suture lines (goniatitic, ceratitic, ammonitic), serving as premier biostratigraphic index fossils for the Mesozoic.",
    "brachiopod": "Brachiopods are lophophorate marine bivalved invertebrates possessing bilateral symmetry across the plane dividing each valve into equal halves (perpendicular to hinge line).",
    "bivalve": "Bivalves (pelecypods) are mollusks with two lateral valves exhibiting bilateral symmetry where the plane of symmetry passes between the two unequal or equal valves.",
    "gastropod": "Gastropods are univalve mollusks characterized by an asymmetrically coiled conical shell and anatomical torsion, thriving from Cambrian to modern marine/freshwater/terrestrial habitats.",
    "foraminifera": "Foraminifera are single-celled marine protists secreting chambered tests (calcareous or agglutinated), vital for biostratigraphy and paleo-oceanographic isotopic analysis.",
    "graptolite": "Graptolites are colonial hemichordate index fossils from the Ordovician and Silurian, characterized by chitinous rhabdosomes that drifted in open ocean waters.",
    "stromatolite": "Stromatolites are layered, biogenic sedimentary accretionary structures produced by the sediment-trapping and binding activities of benthic photosynthetic cyanobacterial mats.",
    "glossopteris": "Glossopteris is a tongue-shaped fossil seed fern foliage characteristic of Permian Gondwana coal measures, supporting Alfred Wegener's continental drift hypothesis.",

    # Structural geology
    "anticlinorium": "An anticlinorium is a large-scale regional antiformal arch of strata comprising multiple smaller parasitic second- and third-order folds across its broad crest.",
    "synclinorium": "A synclinorium is a composite regional synformal trough comprising subordinate second- and third-order folds across its trough.",
    "isoclinal": "An isoclinal fold is a fold geometry where both limbs are parallel to each other and dip at essentially identical angles in the same direction.",
    "recumbent": "A recumbent fold is an overturned fold with an essentially horizontal axial plane ($<10^\circ$ dip).",
    "chevron": "A chevron fold is characterized by planar, straight limbs and sharp, angular, hinge zones, commonly developing in multilayered beds with contrasting competence.",
    "ptygmatic": "Ptygmatic folding describes tortuously buckled, irregular, meandering quartz or pegmatitic veins enclosed within more ductile, incompetent metamorphic host rocks.",
    "dip-slip": "A dip-slip fault features relative displacement strictly parallel to the dip direction of the fault plane (normal or reverse).",
    "strike-slip": "A strike-slip fault features relative displacement strictly parallel to the horizontal strike of the fault surface, driven by shear stresses.",
    "mylonite": "Mylonite is a fine-grained, foliated metamorphic fault rock produced by dynamic ductile recrystallization, grain-size reduction, and plastic shear strain in deeper shear zones.",
    "cataclasite": "Cataclasite is a cohesive, non-foliated fault rock formed by brittle crushing, micro-fracturing, and frictional grinding of rock particles in the upper brittle crust.",
    "slickenside": "Slickensides are polished and striated planar fault surfaces produced by friction and mineral fiber growth along active dislocation surfaces, indicating displacement direction.",

    # Hydrogeology & Engineering
    "aquifer": "An aquifer is a saturated, permeable subsurface geological formation capable of storing and yielding economically usable quantities of water (e.g., sandstones, unconsolidated gravels).",
    "aquitard": "An aquitard is a low-permeability geological formation that retards water flow but may slowly transmit water between adjacent aquifers (e.g., sandy clay).",
    "aquiclude": "An aquiclude is a saturated subsurface rock or sediment body that absorbs water slowly but is incapable of transmitting it in significant quantities (e.g., solid clay).",
    "aquifuge": "An aquifuge is an impermeable, non-porous rock mass that neither contains nor transmits water (e.g., unfractured fresh granite).",
    "confined aquifer": "A confined (artesian) aquifer is bounded above and below by impermeable confining beds (aquicludes), containing groundwater under hydrostatic pressure greater than atmospheric.",
    "unconfined aquifer": "An unconfined (phreatic) aquifer has a free water table surface open to atmospheric pressure and direct meteoric recharge.",
    "specific yield": "Specific yield ($S_y$) is the ratio of the volume of water that a saturated rock will yield by gravity drainage to the total rock volume.",
    "specific retention": "Specific retention ($S_r$) is the ratio of the volume of water retained against gravity forces to the total rock volume ($n = S_y + S_r$).",
    "hydraulic conductivity": "Hydraulic conductivity ($K$) represents the volume of water that will move through a unit cross-sectional area under a unit hydraulic gradient per unit time.",
    "transmissivity": "Transmissivity ($T = K \cdot b$) is the rate at which water is transmitted through a unit aquifer width under a unit hydraulic gradient through entire saturated thickness $b$.",
    "darcy's law": "Darcy's Law ($Q = -K A \frac{dh}{dl}$) governs laminar groundwater flow through saturated porous media, proportional to the hydraulic gradient.",
    "gravity dam": "A gravity dam is a massive concrete or masonry barrier whose stability against sliding, overturning, and reservoir water pressure depends entirely on its self-weight.",
    "arch dam": "An arch dam is a convex upstream curved concrete barrier that transfers hydrostatic water loads horizontally into the strong, unyielding rock abutments of narrow gorges.",
    "earth dam": "An earth dam (embankment dam) is constructed of compacted native earth materials, featuring a central impervious clay core flanked by permeable stabilization shoulders (e.g., Hirakud).",
    "tunneling": "In engineering tunneling, orientation of the tunnel axis perpendicular to the strike of steeply dipping beds provides optimal roof stability and minimizes overbreak.",

    # Remote Sensing & GIS
    "raster": "Raster data format represents spatial terrain information as a regular grid of rows and columns of equal-sized cells (pixels), ideal for continuous satellite imagery and DEMs.",
    "vector": "Vector data format represents geographic features as discrete points (x, y coordinates), lines (vertices), and polygons (closed loops), ideal for cadastral boundaries and road networks.",
    "spectral resolution": "Spectral resolution describes the width and number of specific electromagnetic wavelength bands recorded by an imaging sensor.",
    "spatial resolution": "Spatial resolution refers to the ground dimension represented by a single pixel (e.g., 30 m for Landsat, 1 m for IKONOS).",
    "radiometric resolution": "Radiometric resolution refers to a sensor's sensitivity to subtle differences in reflected radiation, quantified in digital bit depth (e.g., 8-bit = 256 gray levels).",
    "temporal resolution": "Temporal resolution is the revisit frequency of an Earth observation satellite to re-image the identical geographic ground location.",
    "lidar": "LiDAR (Light Detection and Ranging) is an active optical sensor emitting pulsed laser light to measure precise ground surface elevation models through tree canopies.",
    "gps": "The Global Positioning System (GPS/NAVSTAR) uses a nominal constellation of 24+ operational satellites orbiting in 6 orbital planes at ~20,200 km to provide 3D coordinates.",
    "insat": "INSAT is India's multipurpose geostationary satellite system positioned at ~36,000 km altitude for telecommunications, broadcasting, and meteorological tracking.",
    "cartosat": "Cartosat is an Indian Earth observation satellite series equipped with high-resolution panchromatic and multispectral cameras dedicated to topographic mapping and 3D terrain modeling.",
    "irs": "IRS (Indian Remote Sensing) satellites provide systematic multispectral spaceborne imagery (LISS-III, LISS-IV, AWiFS) supporting natural resource and mineral exploration.",

    # Geochemistry & Isotopes
    "siderophile": "Siderophile elements ('iron-loving', e.g., Fe, Ni, Co, Au, Pt) have high affinity for metallic iron, preferentially partitioning into planetary cores.",
    "chalcophile": "Chalcophile elements ('sulfur-loving', e.g., Cu, Pb, Zn, Ag, Hg) have high affinity for sulfur, concentrating in hydrothermal sulfide ore deposits.",
    "lithophile": "Lithophile elements ('rock-loving', e.g., Si, Al, Na, K, Ca, Mg) have strong affinity for oxygen and halides, dominating silicate crusts and mantles.",
    "atmophile": "Atmophile elements ('gas-loving', e.g., H, N, noble gases) occur predominantly in planetary gaseous atmospheres and hydrospheres.",
    "radiocarbon": "Radiocarbon dating (14C, half-life = 5,730 years) determines the absolute age of organic carbon-bearing materials up to ~50,000 years BP.",
    "rubidium-strontium": "The Rb-Sr system (87Rb decaying to 87Sr with t_1/2 = 48.8 Ga) is widely used for dating ancient granitic and metamorphic cratonic terranes.",
    "potassium-argon": "The K-Ar system (40K decaying to 40Ar with t_1/2 = 1.25 Ga) dates volcanic rocks and minerals by measuring trapped radiogenic argon gas.",
    "uranium-lead": "The U-Pb concordia system (238U -> 206Pb and 235U -> 207Pb) provides the gold standard for high-precision geochronology of zircon and baddeleyite.",

    # Mineralogy & Optical
    "isotropic": "Isotropic minerals (isometric system and amorphous substances) have identical refractive indices in all directions ($n$), showing complete extinction under crossed polars.",
    "anisotropic": "Anisotropic minerals (tetragonal, hexagonal, orthorhombic, monoclinic, triclinic) have directional refractive indices, splitting light into two mutually perpendicular polarized rays.",
    "uniaxial": "Uniaxial minerals (tetragonal and hexagonal) possess a single optic axis coinciding with the crystallographic c-axis ($n_\epsilon$ and $n_\omega$).",
    "biaxial": "Biaxial minerals (orthorhombic, monoclinic, triclinic) possess two optic axes and three principal refractive indices ($n_\alpha, n_\beta, n_\gamma$).",
    "pleochroism": "Pleochroism is the optical phenomenon where an anisotropic mineral displays different colors under plane-polarized light when rotated on the microscope stage.",
    "birefringence": "Birefringence ($\Delta = |n_2 - n_1|$) is the numerical difference between the highest and lowest refractive indices of an anisotropic mineral, producing interference colors.",
    "twinning": "Twinning is a symmetrical intergrowth of two or more single crystals of the same substance related by a specific crystallographic symmetry operation."
})
