#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Stratigraphic Formulas, and Syntheses for Chapter 10: Indian Geology
Dr. Ausaf Sayeed - Objective Geology (175 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Cuddapah Basin & Stratigraphic Architecture
    if any(k in t_low for k in ["cuddapah", "papaghani", "cheyair", "nallamalai", "kistna", "kurnool", "mangampeta"]):
        return (
            r"\text{Cuddapah Sequence: } \text{Papaghani (Basal)} \xrightarrow{\text{Unconf}} \text{Cheyair} \xrightarrow{\text{Major Unconf}} \text{Nallamalai} \xrightarrow{\text{Unconf}} \text{Kistna} \implies \text{Kurnool Superposition}",
            "The Cuddapah Basin (Paleo- to Neoproterozoic, ~1.9 to 1.0 Ga) forms a crescent-shaped intracratonic basin resting unconformably upon the Dharwar cratonic basement along the Eparchaean Unconformity. The succession records multi-cycle rifting and passive-margin sedimentation comprising quartzites, shales, and carbonates totaling ~6,000 m. The western margin remains virtually undeformed and unmetamorphosed, while the eastern margin is intensely folded and thrusted against the Eastern Ghats Mobile Belt.",
            "King, W. (1872, On the Kadapah and Karnul Formations in the Madras Presidency); Nagaraja Rao et al. (1987, Mem. Geol. Soc. India); Ramakrishnan & Vaidyanadhan (2008)"
        )

    # 2. Vindhyan Supergroup & Basin Architecture
    if any(k in t_low for k in ["vindhyan", "semri", "kaimur", "rewa", "bhander", "fawn limestone", "nagod", "majhgawan"]):
        return (
            r"\text{Vindhyan Architecture: } \text{Semri (Lower, Marine/Carbonate)} \xrightarrow{\text{Pre-Kaimur Unconf}} \text{Kaimur} \to \text{Rewa} \to \text{Bhander (Upper, Fluvio-Deltaic)}",
            "The Vindhyan Supergroup covers >100,000 km² in Central India, spanning Mesoproterozoic to Neoproterozoic time (~1.7 to 0.6 Ga). The Lower Vindhyan (Semri Group) represents shallow-marine carbonate-shale deposition with prolific stromatolites (Conophyton, Colonella) and Chopan porcellanites. The Upper Vindhyan (Kaimur, Rewa, Bhander) is dominated by mature quartz arenites, deltaic shales, and diamondiferous conglomerates (Panna), bounded on the northwest by the Great Boundary Fault.",
            "Auden, J.B. (1933, Vindhyan Sedimentation in the Son Valley); Soni et al. (1987); Chakraborty, C. (2006); Valdiya, K.S. (The Making of India)"
        )

    # 3. Gondwana Supergroup & Paleoclimate Evolution
    if any(k in t_low for k in ["gondwana", "talchir", "barakar", "raniganj", "panchet", "glossopteris", "gangamopteris", "vertebraria"]):
        return (
            r"\text{Gondwana Succession: } \text{Talchir (Glacial, } \text{C}_3\text{)} \to \text{Barakar (Humid Swamps, } \text{P}_1\text{)} \to \text{Raniganj (Acme, } \text{P}_2\text{)} \to \text{Panchet (Semi-Arid Red Beds, } \text{T}_1\text{)}",
            "The Gondwana Supergroup (Upper Carboniferous to Lower Cretaceous, ~300 to 110 Ma) occupies fault-bounded grabens and half-grabens (Damodar, Son-Mahanadi, Pranhita-Godavari, Satpura). Sedimentation initiated under periglacial conditions with the Talchir tillite, transitioned into warm-humid temperate coal-forming fluviatile conditions (Barakar and Raniganj), shifted to semi-arid red-bed deposition in the Triassic (Panchet), and culminated with Upper Gondwana Bennettitalean floras (Ptilophyllum) and Rajmahal volcanism.",
            "Fox, C.S. (1931, The Gondwana System and Related Formations); Krishnan, M.S. (Geology of India and Burma); Veevers & Tewari (1995, Gondwana Master Basin)"
        )

    # 4. Deccan Volcanic Province & Eruption Dynamics
    if any(k in t_low for k in ["deccan", "trap", "basalt", "intertrappean", "lameta", "k-pg"]):
        return (
            r"V_{\text{basalt}} \approx 1.5 \times 10^6 \text{ km}^3, \quad \Delta t_{\text{eruption}} \approx 750\text{ ka across } 66.0 \text{ Ma Boundary}, \quad \text{Rate: } \sim 2 \text{ km}^3/\text{yr}",
            "The Deccan Volcanic Province (DVP) represents one of the largest continental flood basalt provinces on Earth, triggered by the passage of the Indian Plate over the Réunion mantle plume at the Cretaceous-Paleogene boundary. High-precision 40Ar/39Ar and U-Pb geochronology demonstrates that >90% of the basalt stratigraphy (Kalsubai, Lonavala, and Wai subgroups) erupted within <750,000 years, driving massive SO2/CO2 outgassing contemporaneous with the end-Cretaceous mass extinction.",
            "Courtillot et al. (1988); Schoene et al. (2019, Science); Sprain et al. (2019, Science); Subbarao, K.V. (Deccan Flood Basalts)"
        )

    # 5. Himalayan Tectonics, Major Faults & Foreland Basin
    if any(k in t_low for k in ["himalaya", "mct", "mbt", "hft", "suture", "siwalik", "karewa", "indus"]):
        return (
            r"\text{Himalayan Tectonic Architecture (S to N): } \text{HFT (Frontal)} \to \text{Siwaliks (Molasse)} \to \text{MBT} \to \text{Lesser Himalaya} \to \text{MCT} \to \text{HHC} \to \text{Tethyan Zone} \to \text{ITSZ}",
            "The collision of the Indian and Eurasian plates (~55 Ma) created the Himalayan orogen, characterized by major south-verging crustal thrust systems: (1) Indus-Tsangpo Suture Zone (ITSZ) marking the closed ocean basin; (2) Main Central Thrust (MCT) transporting High Himalayan Crystallines over Lesser Himalaya; (3) Main Boundary Thrust (MBT) placing Lesser Himalaya over the Neogene Siwalik molasse; and (4) Himalayan Frontal Thrust (HFT/MFT) actively imbricating the foreland alluvium.",
            "Gansser, A. (1964, Geology of the Himalayas); Valdiya, K.S. (1980, Stratigraphy and Tectonics of the Lesser Himalaya); Yin, A. (2006)"
        )

    # 6. Marine Mesozoic: Kutch, Jaisalmer & Cauvery Basins
    if any(k in t_low for k in ["kutch", "jaisalmer", "cauvery", "ariyalur", "uttatur", "patcham", "chari", "katrol", "umia"]):
        return (
            r"\text{Kutch Jurassic: } \text{Patcham (Bathonian)} \to \text{Chari (Callovian)} \to \text{Katrol (Kimmeridgian)} \to \text{Umia (Tithonian--Neocomian)}",
            "Mesozoic marine transgressions inundated peri-cratonic rift basins along the western and eastern margins of India during the breakup of Gondwanaland. The Kutch and Jaisalmer basins preserve magnificent cephalopod-rich ammonoid successions recording Tethyan marine cycles, while the Cauvery Basin preserves a classic continuous Cenomanian to Danian sequence (Uttatur, Trichinopoly, Ariyalur, Niniyur) rich in ammonites, inoceramids, and sauropod dinosaurs.",
            "Waagen, W. (1873, Jurassic Fauna of Kutch); Blanford, H.F. (1862, Cretaceous Rocks of South Arcot); Biswas, S.K. (1991, Kutch Basin)"
        )

    # 7. Dharwar, Singhbhum & Indian Precambrian Cratons
    if any(k in t_low for k in ["dharwar", "singhbhum", "sargur", "omg", "closepet", "peninsular gneiss", "iron ore", "bif"]):
        return (
            r"\text{Dharwar Evolution: } \text{Sargur Enclaves (>3.1 Ga)} \to \text{PGC TTG Gneisses (3.4--3.0 Ga)} \to \text{Dharwar Supergroup (2.9--2.6 Ga)} \to \text{Closepet Granite (2.51 Ga)}",
            "The Indian Precambrian shield consists of five major cratonic nuclei: Dharwar, Bastar, Singhbhum, Bundelkhand, and Aravalli. The Singhbhum Craton preserves the Older Metamorphic Group (OMG, ~3.5 Ga) and vast Banded Iron Formations (BIF) of the Iron Ore Group (IOG). The Dharwar Craton preserves the transition from Mesoarchean Sargur high-grade greenstones and TTG gneisses to Neoarchean Dharwar volcanic-sedimentary synclinoria intruded by the 2.51 Ga Closepet Granite batholith.",
            "Radhakrishna, B.P. & Vaidyanadhan, R. (Geology of Karnataka); Saha, A.K. (1994, Crustal Evolution of Singhbhum-North Orissa); Ramakrishnan & Vaidyanadhan (2008)"
        )

    # Default Indian Geology Framework
    return (
        r"\text{Indian Chronostratigraphic Division: } \text{Archaean} \to \text{Purana} \to \text{Dravidian} \to \text{Aryan}",
        "Indian Geology integrates Archean cratonic nuclei, Proterozoic intracratonic Purana basins, Gondwana rift sequences, Cretaceous-Cenozoic basaltic flood provinces, and the active collision orogen of the Himalayas. Understanding these stratigraphic successions provides the fundamental scientific foundation for mineral exploration, hydrocarbon discovery, and geotechnical infrastructure development across the Indian subcontinent.",
        "Krishnan, M.S. (Geology of India and Burma); Wadia, D.N. (Geology of India); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["cuddapah", "kurnool", "purana"]):
        return {
            "title": "Lithostratigraphic Architecture of the Proterozoic Cuddapah Basin",
            "headers": ["Group / Formation", "Dominant Lithology", "Depositional Environment", "Diagnostic Structural / Economic Feature"],
            "rows": [
                ["Papaghani Group", r"\text{Gulcheru Quartzite, Vempalle Dolomite}", "Shallow marine to tidal flat", "Chrysotile asbestos and barytes veins at basic sill contacts"],
                ["Cheyair Group", r"\text{Pulivendla Quartzite, Tadpatri Shale}", "Submarine fan and volcanic sills", "Host to Mangampeta bedded barite tuffs (~1.9 Ga)"],
                ["Nallamalai Group", r"\text{Bairenkonda Quartzite, Cumbum Shale}", "Tectonized shelf and flyschoid basin", "Agnigundala lead-zinc-copper mineralization in Nallamalai fold belt"],
                ["Kistna Group", r"\text{Irlakonda Quartzite, Kolamnala Shale, Srisailam Quartzite}", "Fluvial to shallow marine plateau", "Upper Cuddapah capping quartzites forming Srisailam plateau"],
                ["Kurnool Group (Unconformable)", r"\text{Banganapalle, Narji Limestone, Auk Shale, Paniam, Kundair}", "Flat-lying platform carbonate/clastic", "Basal Banganapalle diamondiferous conglomerate"]
            ]
        }

    if any(k in t_low for k in ["vindhyan", "semri", "bhander", "kaimur"]):
        return {
            "title": "Vindhyan Supergroup: Lithostratigraphic Hierarchy & Key Marker Horizons",
            "headers": ["Stratigraphic Group", "Diagnostic Formations", "Dominant Rock Types", "Paleoenvironmental & Economic Highlights"],
            "rows": [
                ["Semri Group (Lower Vindhyan)", r"\text{Arangi, Kajrahat, Chopan Porcellanite, Kheinjua, Rohtas}", "Limestones, shales, porcellanites, glauconitic sandstone", "Prolific columnar stromatolites in Fawn Limestone; Chopan volcanic ash beds"],
                ["Kaimur Group", r"\text{Sasaram Sandstone, Bijaigarh Shale, Dhandraul Quartzite}", "Supermature quartz arenites, black pyritic shales", "Amjhore bedded pyrite; massive scarp-forming orthoquartzites"],
                ["Rewa Group", r"\text{Panna Shale, Asan Sandstone, Jhiri Shale, Govindgarh Sandstone}", "Greenish-red shales, sandstones, diamondiferous conglomerates", "Panna diamondiferous conglomerate bands"],
                ["Bhander Group (Uppermost)", r"\text{Ganurgarh Shale, Nagod Limestone, Sirbu Shale, Bhander Sandstone}", "Argillaceous shales, cement-grade limestones, red sandstones", "Vast cement industry resources (Nagod limestone); red building stones"]
            ]
        }

    if any(k in t_low for k in ["gondwana", "talchir", "barakar", "raniganj"]):
        return {
            "title": "Indian Gondwana Supergroup: Chronostratigraphy, Flora & Paleoclimate",
            "headers": ["Gondwana Division", "Stratigraphic Formations", "Diagnostic Fossil Flora / Fauna", "Paleoclimatic Depositional Regime"],
            "rows": [
                ["Lower Gondwana (Talchir)", r"\text{Talchir Boulder Bed, Needle Shales}", "Gangamopteris cyclopteroides, Noeggerathiopsis", "Permo-Carboniferous continental glaciation (striated pavement)"],
                ["Lower Gondwana (Damuda)", r"\text{Karharbari, Barakar, Ironstone Shale, Raniganj}", "Glossopteris indica, Vertebraria indica, Schizoneura", "Humid temperate coal swamps; 98% of India's bituminous coal"],
                ["Middle Gondwana (Panchet/Mahadeva)", r"\text{Panchet Formation, Pachmarhi, Parsora, Maleri}", "Dicroidium, Lystrosaurus, Gonioglyptus, Hyperodapedon", "Semi-arid tropical red beds, labyrinthodont amphibians, early dinosaurs"],
                ["Upper Gondwana", r"\text{Rajmahal Traps, Kota, Jabalpur, Athgarh, Umia}", "Ptilophyllum acutifolium, Williamsonia, Kotasaurus", "Warm subtropical rainforests; early Jurassic mammals and sauropods"]
            ]
        }

    if any(k in t_low for k in ["siwalik", "himalaya", "foreland"]):
        return {
            "title": "Siwalik Group: Stratigraphic Zonation & Heavy Mineral Provenance",
            "headers": ["Siwalik Subgroup", "Diagnostic Formations", "Characteristic Vertebrate Fauna", "Dominant Heavy Mineral Signature"],
            "rows": [
                ["Lower Siwalik (Middle Miocene)", r"\text{Kamlial and Chinji Formations}", "Sivapithecus, Dinotherium, Giraffokeryx", "Staurolite dominance (initial unroofing of Lesser Himalayan metamorphics)"],
                ["Middle Siwalik (Late Miocene)", r"\text{Nagri and Dhok Pathan Formations}", "Hipparion theobaldi, Stegodon, Bramatherium", "Kyanite dominance (unroofing of High Himalayan Crystalline belt)"],
                ["Upper Siwalik (Plio-Pleistocene)", r"\text{Tatrot, Pinjor, Boulder Conglomerate}", "Equus sivalensis, Elephas hysudricus, Colossochelys", "Hornblende and sillimanite dominance (paroxysmal uplift of Higher Himalaya)"]
            ]
        }

    # Default Indian Geology Synthesis Matrix
    return {
        "title": f"Synthesis Matrix: {topic} - Indian Stratigraphic Architecture",
        "headers": ["Geological Parameter", "Stratigraphic Details", "Key Formations & Marker Beds", "Economic / Tectonic Significance"],
        "rows": [
            ["Regional Tectonic Setting", r"\text{" + topic[:25] + r"}", "Peninsular Craton / Extra-Peninsular Tethys", "Constrains geodynamic evolution of the Indian Plate"],
            ["Lithological Association", r"\text{Sedimentary / Igneous / Metamorphic}", "Conglomerates, sandstones, shales, carbonates", "Defines depositional basin architecture and provenance"],
            ["Chronostratigraphic Datum", r"\text{Isotopic Age / Biostratigraphic Biozone}", "Zircon U-Pb, Ar-Ar, Index Fossil assemblage", "Global chronostratigraphic correlation across deep time"],
            ["Mineral Resources", r"\text{Metallic / Energy / Industrial Minerals}", "Coal, petroleum, iron ore, limestone, diamonds", "Constitutes India's critical strategic mineral foundation"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = topic.lower()

    if any(k in t_low for k in ["cuddapah", "vindhyan", "purana"]):
        return [
            {
                "question": "Which of the following regional structural lineaments defines the northwestern tectonic boundary of the Vindhyan Basin in Rajasthan?",
                "options": {
                    "a": "Narmada-Son Lineament (NSL)",
                    "b": "Great Boundary Fault (GBF)",
                    "c": "Eastern Ghats Frontal Thrust",
                    "d": "Main Central Thrust (MCT)"
                },
                "answer": "b",
                "explanation": "The Great Boundary Fault (GBF) is an 800-km-long regional thrust fault in southeastern Rajasthan bringing older deformed pre-Vindhyan rocks over the flat-lying Upper Vindhyan Bhander Group."
            },
            {
                "question": "What is the primary operational criterion distinguishing the Kurnool Group from the underlying Cuddapah Supergroup in Andhra Pradesh?",
                "options": {
                    "a": "The Kurnool Group is intensely deformed into isoclinal nappes, whereas the Cuddapah is horizontal",
                    "b": "The Kurnool Group rests with a profound regional angular unconformity upon the eroded edges of the Cuddapah Supergroup",
                    "c": "The Kurnool Group contains abundant dinosaur bones",
                    "d": "The Kurnool Group consists exclusively of volcanic basalt flows"
                },
                "answer": "b",
                "explanation": "The Neoproterozoic Kurnool Group rests with a sharp, regional angular unconformity upon both the deformed Cuddapah formations and the basement granites, initiating with basal diamondiferous Banganapalle conglomerates."
            }
        ]

    # Default Indian Geology Practice
    return [
        {
            "question": "Why is the Talchir Formation of the Gondwana Supergroup regarded as an exceptional chronostratigraphic time-marker across the Indian Peninsula?",
            "options": {
                "a": "It preserves continental flood basalt lava flows",
                "b": "It contains a regionally synchronous glacio-marine tillite and boulder bed recording the Late Carboniferous Gondwanan glaciation",
                "c": "It is rich in marine Jurassic ammonites",
                "d": "It contains commercial anthracite coal seams"
            },
            "answer": "b",
            "explanation": "The basal Talchir Boulder Bed represents a continent-wide continental tillite deposited by an extensive Permo-Carboniferous ice sheet, providing an unambiguous isochronous chronostratigraphic datum across all Indian Gondwana basins."
        },
        {
            "question": "Which major tectonic boundary in the Himalaya separates the high-grade metamorphic Higher Himalayan Crystalline Complex (HHC) from the underlying sedimentary Lesser Himalaya?",
            "options": {
                "a": "Himalayan Frontal Thrust (HFT)",
                "b": "Main Boundary Thrust (MBT)",
                "c": "Main Central Thrust (MCT)",
                "d": "Indus-Tsangpo Suture Zone (ITSZ)"
            },
            "answer": "c",
            "explanation": "The Main Central Thrust (MCT) is a north-dipping ductile shear zone along which the high-grade Proterozoic Vaikrita crystalline thrust sheet was emplaced southward over the low-grade metasedimentary rocks of the Lesser Himalaya."
        }
    ]
