#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Evolutionary Formulas, and Syntheses for Chapter 8: Palaeontology
Dr. Ausaf Sayeed - Objective Geology (250 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Taphonomy, Fossilization, Carbonization & Diagenesis
    if any(k in t_low for k in ["taphonom", "fossilization", "permineral", "carboniz", "mold", "cast", "lagerst"]):
        return (
            r"\text{Taphonomic Equation: } N_{\text{fossil}} = N_{\text{living}} \times P_{\text{biomin}} \times P_{\text{burial}} \times P_{\text{diagenesis}} \times P_{\text{discovery}}",
            "Taphonomy (coined by I.A. Efremov, 1940) formalizes the transition of organisms from the biosphere into the lithosphere. The process encompasses necrolysis (decay and post-mortem disarticulation), biostratinomy (sedimentological transport, reorientation, and hydraulic sorting), and diagenetic fossildiagenesis (permineralization, recrystallization, mold/cast formation, or carbonization into an inert carbon film). Exceptional preservation occurs in Conservation Lagerstätten under anoxia, hypersalinity, or rapid obrution (catastrophic burial).",
            "I.A. Efremov (1940, Taphonomy: New Branch of Paleontology); Clarkson, E.N.K. (Invertebrate Palaeontology and Evolution, 4th Ed.); Benton & Harper (2020)"
        )

    # 2. Trilobites: Suture Lines, Cephalic Morphology & Eye Mechanics
    if any(k in t_low for k in ["trilobit", "facial suture", "glabella", "pygidium", "cephalon", "proparian", "opisthoparian", "gonatoparian", "holochroal", "schizochroal"]):
        return (
            r"\text{Trilobite Sutural Classification:} \quad \begin{cases} \text{Proparian: } \text{Suture cuts lateral margin anterior to genal angle} \\ \text{Gonatoparian: } \text{Suture intersects apex of genal angle} \\ \text{Opisthoparian: } \text{Suture cuts posterior margin behind genal angle} \end{cases}",
            "Trilobites (Subphylum Trilobitomorpha) possess an uncalcified/calcitic exoskeleton divided longitudinally into an axial lobe and two pleural lobes, and transversely into cephalon, thorax, and pygidium. Facial sutures (lines of ecdysial weakness facilitating moulting) separate the cranidium from free cheeks (librigenae). Visual systems feature calcite crystal optics in two configurations: holochroal eyes (closely packed polygonal lenses under a single continuous corneal membrane) and schizochroal eyes (separated round lenses each with individual cornea, seen in Phacopida).",
            "Treatise on Invertebrate Paleontology (Part O, Arthropoda 1, Trilobita); E.N.K. Clarkson (1973, 1998); Fortey & Owens"
        )

    # 3. Brachiopoda: Symmetry, Valve Anatomy, Dentition & Lophophore
    if any(k in t_low for k in ["brachiopod", "pedicle", "brachial", "delthyrium", "chilidium", "lophophore", "articulata", "inarticulata", "crura", "spiralia"]):
        return (
            r"\text{Brachiopod Symmetry: } \text{Bilateral Plane } \perp \text{ Hinge Line } \implies \text{Valves Unequal, Valve Itself Equilateral}",
            "Phylum Brachiopoda comprises lophophorate coelomates enclosed in two bivalved shells where the plane of bilateral symmetry passes vertically through the beak, perpendicular to the hinge line. The pedicle (ventral) valve is generally larger and contains the delthyrium for the pedicle stalk, while the brachial (dorsal) valve houses the skeletal calcified lophophore supports (crura, loops, or spiralia). Articulate brachiopods (Rhynchonelliformea) possess teeth and sockets with calcitic shells, whereas inarticulate brachiopods (Linguliformea) rely solely on complex musculature with organo-phosphatic shells.",
            "Treatise on Invertebrate Paleontology (Part H, Brachiopoda); Williams et al. (1997); Rudwick, M.J.S. (Living and Fossil Brachiopods)"
        )

    # 4. Bivalvia (Lamellibranchia / Pelecypoda): Dentition, Musculature & Symmetry
    if any(k in t_low for k in ["bivalv", "lamellibranch", "pelecypod", "taxodont", "heterodont", "schizodont", "desmodont", "pachydont", "pallial", "sinupalliate", "integripalliate"]):
        return (
            r"\text{Bivalve Symmetry: } \text{Bilateral Plane Lies Between Left and Right Valves} \implies \text{Valves Inequilateral, Mutually Equal}",
            "Class Bivalvia displays a plane of bilateral symmetry that passes directly along the commissure between the two valves, making each valve inequilateral while the pair are equivalve (except oysters and rudists). Dentition patterns classify major clades: Taxodont (comb-like row of identical small teeth; e.g., Arca, Nucula), Schizodont (large bifurcating divergent teeth; e.g., Trigonia), Heterodont (distinct cardinal teeth beneath beak and lateral teeth; e.g., Venus), Desmodont (teeth reduced, chondrophore spoon; e.g., Mya), and Pachydont (heavy, amorphous peg-like teeth; e.g., Rudists). Siphon presence creates an embayment in the pallial line termed the pallial sinus (sinupalliate).",
            "Moore, R.C. (Treatise Part N, Mollusca 6: Bivalvia); Cox, L.R. (1969); Stanley, S.M. (Relation of Shell Form to Life Habits of the Bivalvia)"
        )

    # 5. Cephalopoda: Suture Ontogeny, Septa & Siphuncle Mechanics
    if any(k in t_low for k in ["cephalopod", "ammon", "nautil", "suture", "septum", "siphuncle", "goniatit", "ceratit", "ammonit", "belemnit", "phragmocone"]):
        return (
            r"\text{Suture Evolution: } \text{Orthoceratitic} \to \text{Goniatitic} \to \text{Ceratitic} \to \text{Ammonitic (Complexly Frilled)}",
            "Cephalopods possess a chambered shell (phragmocone) connected by a hydrostatic siphuncle. The junction of internal septa with the outer shell wall forms the suture line, where saddles arch toward the aperture (anteriorly) and lobes point toward the apex (posteriorly). Siphuncle positioning differentiates major groups: central/subcentral in Nautiloidea, marginal/ventral in Ammonoidea (dorsal in Clymeniida). Increasing suture complexity (from Paleozoic goniatites through Triassic ceratites to Jurassic-Cretaceous ammonites) reinforced thin hydrostatic shells against crushing oceanic hydrostatic pressures.",
            "Westermann, G.E.G. (1996, Ammonoid Life and Function); Arkell et al. (Treatise Part L, Ammonoidea); Lehmann, U. (The Ammonites)"
        )

    # 6. Graptolithina: Stipe Reduction, Thecal Morphology & Evolution
    if any(k in t_low for k in ["graptolit", "theca", "rhabdosome", "sicula", "nema", "virgula", "dichograptid", "monograptid", "didymograptid"]):
        return (
            r"\text{Graptolite Astogeny: } 64 \text{ Stipes} \to 32 \to 16 \to 8 \to 4 \text{ (Tetragraptus)} \to 2 \text{ (Didymograptus)} \to 1 \text{ (Monograptus)}",
            "Class Graptolithina (Hemichordata) were colonial, marine, organic-walled hemichordates displaying extraordinarily rapid evolutionary turnover from Middle Cambrian to Early Carboniferous. Astogeny initiates from an embryonic conical sicula producing thecae along a central rod (virgula/nema). Evolutionary trends exhibit progressive stipe reduction (from many-branched multiramous Dichograptids to 4-branched Tetragraptus, 2-branched Didymograptus, and ultimately uniserial 1-branched Monograptids), alongside stipe orientation shifts from pendent through horizontal to scandent (upright biserial and uniserial).",
            "Bulman, O.M.B. (Treatise Part V, Graptolithina); Cooper & Fortey (1982); Rickards, R.B. (Graptolite Astogeny and Evolution)"
        )

    # 7. Gastropoda: Coiling Geometry, Torsion & Whorl Anatomy
    if any(k in t_low for k in ["gastropod", "dextral", "sinistral", "holostomatous", "siphonostomatous", "columella", "protoconch", "torsion", "umbilicus"]):
        return (
            r"\text{Raup's Parameters: } W = \left(\frac{r_n}{r_{n-1}}\right)^2, \quad D = \frac{d}{r_n}, \quad T = \frac{t}{r_n}",
            "Class Gastropoda undergoes ontogenetic 180° anatomical torsion during the veliger larval stage, rotating the visceral mass, mantle cavity, and anus to face anteriorly over the head. Shell geometry is governed by David Raup's parameters: Whorl expansion rate (W), Distance of whorl from coiling axis (D), and Translation rate along axis (T). Dextral (right-handed) shells display the aperture to the right when viewed with apex upward; holostomatous apertures have continuous unbroken margins (herbivores), whereas siphonostomatous apertures exhibit an anterior notch or canal for a fleshy respiratory siphon (carnivores/scavengers).",
            "Raup, D.M. (1966, Geometric Analysis of Shell Coiling); Cox, L.R. (Treatise Part I, Gastropoda); Morton, J.E. (Molluscs)"
        )

    # 8. Microfossils, Foraminifera & Ostracoda: Wall Structure & Paleobathymetry
    if any(k in t_low for k in ["foraminifer", "microfossil", "ostracod", "conodont", "radiolaria", "diatom", "megalospheric", "microspheric", "planktic", "benthic"]):
        return (
            r"\text{Paleobathymetric Index: } P/B = \frac{N_{\text{planktic}}}{N_{\text{planktic}} + N_{\text{benthic}}} \times 100\% \propto \text{Water Depth}",
            "Foraminifera (Granuloreticulosa) construct single- or multi-chambered tests classified by wall composition: agglutinated (arenaceous), microgranular, porcellaneous (imperforate milioline calcite), and hyaline (perforate radial or granular calcite). Dimorphic life cycles alternate between sexual microspheric generations (small proloculus, large adult test) and asexual megalospheric generations (large proloculus, smaller adult test). Planktic-to-benthic (P/B) ratios serve as quantitative sea-level and bathymetric indicators across continental shelves and abyssal basins.",
            "Cushman, J.A. (Foraminifera: Their Classification and Economic Use); Loeblich & Tappan (1988); Armstrong & Brasier (Microfossils, 2nd Ed.)"
        )

    # 9. Equidae, Proboscidea & Vertebrate Lineages
    if any(k in t_low for k in ["equid", "horse", "hyracotherium", "merychippus", "pliohippus", "proboscid", "elephant", "moeritherium", "mastodon", "mammoth"]):
        return (
            r"\text{Equid Trend: } \text{Hyracotherium (4/3 toes, Brachydont)} \to \text{Merychippus (3 toes, Sub-hypsodont)} \to \text{Equus (1 toe, Hypsodont)}",
            "Vertebrate macroevolution in the Cenozoic exemplifies morphological adaptation to changing biomes. The Equid lineage records transition from forest browser (Eocene *Hyracotherium* with tetradactyl forefeet, tridactyl hindfeet, and low-crowned brachydont teeth without cement) to savanna grazer (*Merychippus*, *Pliohippus*, and *Equus* with monodactyl limbs, spring-ligament foot mechanics, and high-crowned hypsodont cement-covered teeth with complex enamel lophs). Proboscidean evolution tracks horizontal molar shearing, bilophodont to lamellar plate progression, and tusks derived from second upper incisors.",
            "Simpson, G.G. (1951, Horses); Romer, A.S. (Vertebrate Paleontology, 3rd Ed.); Prothero & Schoch (Evolution of Artiodactyls and Perissodactyls)"
        )

    # 10. Indian Gondwana Palaeobotany: Glossopteris, Gangamopteris & Ptilophyllum
    if any(k in t_low for k in ["gondwana", "glossopteris", "gangamopteris", "ptilophyllum", "palaeobotany", "vertebraria", "sahni", "rajmahal"]):
        return (
            r"\text{Indian Floral Zonation: } \begin{cases} \text{Lower Gondwana (Permo-Carboniferous): } \text{Glossopteris / Gangamopteris} \\ \text{Upper Gondwana (Jurassic-Cretaceous): } \text{Ptilophyllum / Williamsonia} \end{cases}",
            "Indian stratigraphy and paleoclimatology are demarcated by distinctive floral successions. The Lower Gondwana flora (Talchir to Panchet) is dominated by the tongue-shaped reticulate-veined leaves of *Glossopteris* (possessing a prominent median midrib) and *Gangamopteris* (characterized by anastomosing venation lacking a median midrib), rooted in *Vertebraria* axes adapted to Permian periglacial swamp environments. The Upper Gondwana flora (Rajmahal, Kota, Jabalpur) is dominated by the cycadophytic Bennettitalean frond *Ptilophyllum*, indicating warm, subtropical-to-tropical Mesozoic regimes.",
            "Prof. Birbal Sahni (1932, 1948); Krishnan, M.S. (Geology of India and Burma); Surange, K.R. (Indian Fossil Pteridophytes)"
        )

    # 11. Evolutionary Principles, Extinction Events & Biostratigraphy
    if any(k in t_low for k in ["punctuated", "phyletic", "dollo", "cope", "heterochrony", "paedomorph", "peramorph", "mass extinction", "iridium", "zone"]):
        return (
            r"\text{Heterochronic Trajectories: } \begin{cases} \text{Paedomorphosis: } \text{Progenesis, Neoteny, Post-displacement} \\ \text{Peramorphosis: } \text{Hypermorphosis, Acceleration, Pre-displacement} \end{cases}",
            "Evolutionary paleobiology synthesizes tempos and modes of speciation. Eldredge and Gould (1972) formulated Punctuated Equilibrium, demonstrating that species remain in long stasis interrupted by rapid cladogenesis in peripherally isolated populations, challenging strict Darwinian phyletic gradualism. Dollo's Law of Irreversibility dictates that complex anatomical structures once lost are never regained in identical form. Cope's Rule notes the macroevolutionary tendency toward body size increase within clades over geological time.",
            "Eldredge & Gould (1972, Models in Paleobiology); Gould, S.J. (1977, Ontogeny and Phylogeny); Raup & Sepkoski (1982, Mass Extinctions)"
        )

    # 12. Echinodermata: Crinoids, Blastoids & Echinoidea
    if any(k in t_low for k in ["echinoderm", "crinoid", "blastoid", "echinoid", "hydrospire", "ambulacr", "madreporite", "aristotle"]):
        return (
            r"\text{Echinoderm Organization: } \text{Secondary Pentameral Symmetry} + \text{Stereom High-Mg Calcite Skeleton}",
            "Phylum Echinodermata possesses an endoskeleton composed of high-magnesium stereom calcite ossicles with sponge-like microporous microstructure, exhibiting secondary pentameral (five-fold) radial symmetry and a unique hydraulic water vascular system. Pelmatozoans (sessile, stalked forms) include Crinoidea (calyx, arms, columnals) and Blastoidea (bud-shaped theca with 5 lancet-shaped ambulacral fields and internal respiratory hydrospires). Echinozoans (mobile forms) include regular sea urchins (radial, epifaunal, possessing Aristotle's lantern) and irregular sea urchins (bilateral, infaunal, heart-shaped with petaloid ambulacra).",
            "Treatise on Invertebrate Paleontology (Parts S, T, U: Echinodermata); Clarkson, E.N.K.; Nichols, D. (Echinoderms)"
        )

    # Default Palaeontological Framework
    return (
        r"\text{Biostratigraphic Range: } \text{FAD (First Appearance Datum)} \to \text{LAD (Last Appearance Datum)} \implies \text{Index Biozone}",
        "Palaeontology links biological morphological change across deep time with chronostratigraphic calibration. The utility of an index (guide) fossil is maximized when a taxon possesses rapid evolutionary morphological turnover, wide geographic distribution across multiple sedimentary facies, pelagic/planktic dispersal, and high preservation potential with readily identifiable hard parts.",
        "Hedberg, H.D. (1976, International Stratigraphic Guide); Clarkson, E.N.K. (Invertebrate Palaeontology and Evolution); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["trilobit", "suture", "cephalon"]):
        return {
            "title": "Diagnostic Classification of Trilobite Facial Sutures & Morphology",
            "headers": ["Suture / Feature", "Suture Trajectory / Definition", "Key Genera / Clades", "Evolutionary / Functional Significance"],
            "rows": [
                ["Proparian", r"\text{Cuts lateral margin anterior to genal angle}", "Phacops, Dalmanites, Cheirurus", "Common in Post-Cambrian Phacopida; genal spines absent or on fixed cheeks"],
                ["Gonatoparian", r"\text{Passes directly through apex of genal angle}", "Calymene, Triarthrus", "Transitional suture geometry; preserves stable cranidial hinge"],
                ["Opisthoparian", r"\text{Cuts posterior cephalic margin inside genal angle}", "Paradoxides, Olenus, Asaphus", "Predominant in Cambrian-Ordovician; genal spines borne on free cheeks (librigenae)"],
                ["Hypoparian", r"\text{Marginal or submarginal along cephalic edge}", "Agnostus, Trinucleus", "Secondary loss of dorsal suture; frequently associated with blindness/benthic adaptation"]
            ]
        }

    if any(k in t_low for k in ["brachiopod", "bivalv", "lamellibranch", "valve"]):
        return {
            "title": "Comparative Synthesis: Phylum Brachiopoda vs Class Bivalvia",
            "headers": ["Anatomical Parameter", "Phylum Brachiopoda (Lamp Shells)", "Class Bivalvia (Clams, Mussels, Oysters)", "Distinguishing Diagnostic Utility"],
            "rows": [
                ["Plane of Symmetry", r"\text{Bilateral Plane } \perp \text{ Hinge Line}", r"\text{Bilateral Plane Between Left \& Right Valves}", "Brachiopod valve is equilateral; Bivalve is inequilateral"],
                ["Valve Relationship", r"\text{Inequivalve (Pedicle } > \text{ Brachial)}", r"\text{Equivalve (Left } = \text{ Right in normal forms)}", "Prevents cross-phylum fossil misidentification"],
                ["Internal Feeding Organ", r"\text{Lophophore supported by calcified brachidia}", r"\text{Ctenidia (paired filamentous / lamellar gills)}", "Brachidia frequently fossilize inside calcitic shell"],
                ["Opening / Closing Mechanism", r"\text{Diductor muscles open; Adductors close}", r"\text{Elastic ligament opens; Adductors close}", "Brachiopods fossilize closed; dead bivalves spring open"]
            ]
        }

    if any(k in t_low for k in ["cephalopod", "ammon", "nautil", "suture"]):
        return {
            "title": "Evolutionary Trajectory of Cephalopod Suture Patterns Across Deep Time",
            "headers": ["Suture Type", "Saddle Geometry (Anterior)", "Lobe Geometry (Posterior)", "Dominant Stratigraphic Range"],
            "rows": [
                ["Nautilitic / Orthoceratitic", r"\text{Broad, gentle, straight to slightly undulating}", r"\text{Simple, smooth, undeformed arcs}", "Cambrian to Present Day (Nautilus)"],
                ["Goniatitic", r"\text{Smooth, entire, undivided, rounded saddles}", r"\text{Smooth, pointed, angular, undivided lobes}", "Devonian to Permian Periods (Goniatites)"],
                ["Ceratitic", r"\text{Smooth, rounded, entire saddles}", r"\text{Denticulate, serrated, finely divided lobes}", "Triassic Period (Ceratites)"],
                ["Ammonitic", r"\text{Complexly frilled, fluted, and foliated}", r"\text{Complexly frilled, branched, and digitate}", "Jurassic to Cretaceous Periods (Ammonites)"]
            ]
        }

    if any(k in t_low for k in ["graptolit", "theca", "rhabdosome", "sicula"]):
        return {
            "title": "Major Macroevolutionary Trends in the Class Graptolithina",
            "headers": ["Macroevolutionary Vector", "Primitive Condition (Lower Ordovician)", "Advanced Condition (Silurian - Devonian)", "Paleoecological Adaptation"],
            "rows": [
                ["Stipe Number", r"64 \to 32 \to 16 \to 8 \text{ Stipes (Dichograptidae)}", r"1 \text{ Stipe (Monograptus)}", "Hydrodynamic efficiency in pelagic water columns"],
                ["Stipe Orientation", r"\text{Pendent (hanging) to Horizontal}", r"\text{Scandent (growing upward alongside nema)}", "Optimized feeding orientation and passive flotation"],
                ["Thecal Arrangement", r"\text{Uniserial or biserial branches}", r"\text{Biserial scandent (Diplograptus) to uniserial}", "Compact structural strength and material economy"],
                ["Thecal Shape", r"\text{Simple cylindrical tubes (Dichograptid type)}", r"\text{Hooked, lobed, coiled, or spinose apertures}", "Specialized micro-suspension feeding niches"]
            ]
        }

    if any(k in t_low for k in ["equid", "horse", "proboscid", "mammoth"]):
        return {
            "title": "Cenozoic Mammalian Macroevolution: Diagnostic Phylogenies",
            "headers": ["Geological Epoch", "Equid Taxon & Dental/Foot Adaptations", "Proboscidean Taxon & Cranio-Dental Trend", "Global Biome Shift"],
            "rows": [
                ["Eocene", r"\text{Hyracotherium (4 front/3 hind toes, brachydont)}", r"\text{Moeritherium (Tapir-like, simple bunodont)}", "Dense subtropical rainforests"],
                ["Oligocene", r"\text{Mesohippus (3 toes touch ground, incipient lophs)}", r"\text{Palaeomastodon (Incipient tusks in both jaws)}", "Cooling climate, woodland savanna opening"],
                ["Miocene", r"\text{Merychippus (3 toes, side toes reduced, sub-hypsodont)}", r"\text{Gomphotherium (Four tusks, bunolophodont molars)}", "Expansive C3 grassland steppes"],
                ["Pliocene-Pleistocene", r"\text{Equus (Single digit III, spring ligament, hypsodont)}", r"\text{Mammuthus / Elephas (Compressed lamellar plates)}", "Arid, abrasive C4 prairie & tundra steppe"]
            ]
        }

    if any(k in t_low for k in ["gondwana", "glossopteris", "ptilophyllum", "gangamopteris"]):
        return {
            "title": "Indian Gondwana Floral Successions: Taxonomic & Stratigraphic Zonation",
            "headers": ["Stratigraphic Division", "Geological Age", "Diagnostic Floral Assemblage", "Lithological Formations & Paleoclimate"],
            "rows": [
                ["Lower Gondwana", r"\text{Early Permian (Asselian-Artinskian)}", "Gangamopteris, Glossopteris, Noeggerathiopsis", "Talchir Boulder Bed to Karharbari Fm; Periglacial"],
                ["Lower Gondwana", r"\text{Late Permian (Raniganj-Barakar)}", "Glossopteris, Vertebraria, Schizoneura, Sphenophyllum", "Barakar & Raniganj Fms; Humid temperate coal swamps"],
                ["Middle Gondwana", r"\text{Early to Middle Triassic}", "Dicroidium, Lepidopteris, Glossopteris (declining)", "Panchet & Kamthi Fms; Semi-arid to seasonal drought"],
                ["Upper Gondwana", r"\text{Jurassic to Early Cretaceous}", "Ptilophyllum, Williamsonia, Elatocladus", "Rajmahal, Kota, & Jabalpur Fms; Subtropical warm humid"]
            ]
        }

    # Default Palaeontology Matrix
    return {
        "title": f"Synthesis Analysis: {topic} - Stratigraphic & Morphologic Framework",
        "headers": ["Diagnostic Metric", "Paleontological Definition", "Systematic Criteria", "Chronostratigraphic / Paleoenvironmental Application"],
        "rows": [
            ["Taxonomic Affinity", r"\text{" + topic[:25] + r"}", "Diagnostic fossil morphology", "Enables species-level phylogenetic resolution"],
            ["Stratigraphic Biozone", r"\text{FAD } \to \text{ LAD Interval}", "First / Last Appearance Datums", "High-resolution chronostratigraphic correlation"],
            ["Preservation Mode", r"\text{Biomineralized Shell / Mold / Film}", "Calcite, aragonite, phosphate, silica, carbon", "Indicates redox, pH, burial rate, and fossildiagenesis"],
            ["Paleoecological Facies", r"\text{Benthic / Planktic / Nektonic Life Habit}", "Substrate, depth, salinity, and temperature proxies", "Reconstructs ancient marine and terrestrial paleoenvironments"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = topic.lower()

    if any(k in t_low for k in ["brachiopod", "bivalv"]):
        return [
            {
                "question": "Which of the following serves as the primary diagnostic distinction separating articulate brachiopods (Rhynchonelliformea) from inarticulate brachiopods (Linguliformea)?",
                "options": {
                    "a": "Articulates possess calcium carbonate shells with tooth-and-socket hinge dentition, whereas inarticulates possess organo-phosphatic shells held solely by muscles",
                    "b": "Articulates lack a lophophore while inarticulates possess a prominent lophophore",
                    "c": "Articulates display bilateral symmetry between valves, while inarticulates display symmetry across each valve",
                    "d": "Articulates are exclusively planktic while inarticulates are exclusively infaunal"
                },
                "answer": "a",
                "explanation": "Articulate brachiopods construct low-magnesium calcite shells featuring interlocking teeth and sockets along the hinge, whereas inarticulate brachiopods (e.g., Lingula) lack hinge dentition and construct apatite (chitinophosphate) shells held exclusively by complex musculature."
            },
            {
                "question": "In Class Bivalvia, what functional morphological adaptation is directly indicated by the presence of a deep pallial sinus on the interior surface of the valve?",
                "options": {
                    "a": "A sessile, cemented epifaunal mode of life (e.g., Ostrea)",
                    "b": "An infaunal burrowing life habit requiring retractable fleshy siphons",
                    "c": "A free-swimming nektonic life habit (e.g., Pecten)",
                    "d": "A carnivorous grazing habit on hard substrates"
                },
                "answer": "b",
                "explanation": "The pallial sinus is an inward embayment in the posterior pallial line formed by the attachment of siphon retractor muscles. Deeply sinupalliate bivalves are active infaunal burrowers requiring long retractable siphons to reach the sediment-water interface."
            }
        ]

    if any(k in t_low for k in ["cephalopod", "ammon"]):
        return [
            {
                "question": "In the evolutionary transition of ammonoid cephalopod suture lines, what defines a 'ceratitic' suture?",
                "options": {
                    "a": "Both lobes and saddles are entirely smooth and unfrilled",
                    "b": "Both lobes and saddles are complexly frilled and foliated",
                    "c": "Saddles are smooth and rounded, while lobes are denticulate and serrated",
                    "d": "Lobes are smooth and rounded, while saddles are denticulate and serrated"
                },
                "answer": "c",
                "explanation": "Ceratitic sutures (diagnostic of the Triassic Period, e.g., Ceratites) are uniquely characterized by anteriorly directed smooth, rounded, entire saddles and posteriorly directed denticulate, serrated, or multidentate lobes."
            },
            {
                "question": "How does the anatomical position of the siphuncle differ between Nautiloidea and Ammonoidea?",
                "options": {
                    "a": "Nautiloids have a marginal ventral siphuncle; ammonoids have a central siphuncle",
                    "b": "Nautiloids have a central or subcentral siphuncle; most ammonoids have an external marginal (ventral) siphuncle",
                    "c": "Both clades have strictly dorsal siphuncles throughout ontogeny",
                    "d": "Nautiloids lack a siphuncle; ammonoids possess paired siphuncles"
                },
                "answer": "b",
                "explanation": "In Nautiloidea, the siphuncle pierces the septa centrally or subcentrally. In contrast, in true Ammonoidea the siphuncle runs along the extreme external ventral margin (with the rare exception of the order Clymeniida where it runs dorsally)."
            }
        ]

    # Default Paleontology Practice
    return [
        {
            "question": f"In paleontological biostratigraphy, what represents the primary criterion for a high-utility index (guide) fossil?",
            "options": {
                "a": "Restricted to a single endemic basin, slow evolutionary change, thick shell",
                "b": "Wide geographic distribution, rapid evolutionary turnover, high preservation potential, and ease of identification",
                "c": "Exclusively benthic, long geological lifespan across multiple eras",
                "d": "Soft-bodied anatomy preserved only in exceptional Konservat-Lagerstätten"
            },
            "answer": "b",
            "explanation": "Ideal index fossils (e.g., graptolites, conodonts, ammonites, planktic foraminifera) possess rapid morphological evolution, cosmopolitan geographic distribution, pelagic/planktic dispersal, and sturdy mineralized skeletons."
        },
        {
            "question": f"Which evolutionary principle dictates that complex anatomical structures or organ complexes once lost during evolutionary divergence cannot be regained in their identical ancestral configuration?",
            "options": {
                "a": "Cope's Rule",
                "b": "Dollo's Law of Irreversibility",
                "c": "Gloger's Rule",
                "d": "Bergmann's Rule"
            },
            "answer": "b",
            "explanation": "Formulated by Louis Dollo in 1893, Dollo's Law of Irreversibility states that an organism cannot return, even partially, to a previous stage already realized in the ranks of its ancestors."
        }
    ]
