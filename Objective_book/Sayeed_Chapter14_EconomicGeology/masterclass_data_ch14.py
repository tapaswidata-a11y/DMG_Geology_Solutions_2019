#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Economic Formulations, and Syntheses for Chapter 14: Economic Geology
Dr. Ausaf Sayeed - Objective Geology (243 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Petroleum Geology & Reservoir Mechanics
    if any(k in t_low for k in ["petroleum", "oil", "gas", "reservoir", "darcy", "bombay high", "cambay", "digboi", "ankleshwar", "gandhar"]):
        return (
            r"\text{STOIIP: } N = \frac{7758 \cdot A \cdot h \cdot \phi \cdot (1 - S_w)}{B_{oi}} \quad [\text{STB}]; \quad q = -\frac{k A}{\mu} \frac{dP}{dx} \quad (\text{Darcy's Law})",
            "Petroleum accumulations require the spatial-temporal co-occurrence of five fundamental elements: an organically rich, thermally mature source rock (Type I/II/III kerogen in the oil window, 60-120°C); a porous and permeable reservoir rock (sandstone or vuggy limestone); a regional impermeable cap rock/seal (evaporite or thick shale); a structural, stratigraphic, or combination trapping geometry; and favorable migration pathways connecting source kitchen to trap prior to seal breach. In India, Tertiary basins (Assam Shelf, Cambay Rift, Mumbai Offshore, Krishna-Godavari, Cauvery, Barmer) host the primary commercial plays.",
            "Levorsen, A.I. (1967, Geology of Petroleum. Freeman); Hunt, J.M. (1996, Petroleum Geochemistry and Geology. Freeman); DGH India Annual Hydrocarbon Reports"
        )

    # 2. Lindgren's Hydrothermal P-T Classification
    if any(k in t_low for k in ["hydrothermal", "epithermal", "mesothermal", "hypothermal", "telethermal", "xenothermal", "leptothermal", "lindgren"]):
        return (
            r"\text{Lindgren (1913, 1933): } \begin{cases} \text{Hypothermal: } T = 300\text{--}600^\circ\text{C}, & P = 1\text{--}3\text{ kbar (deep intrusive)} \\ \text{Mesothermal: } T = 200\text{--}300^\circ\text{C}, & P = 0.5\text{--}1.5\text{ kbar (intermediate depth)} \\ \text{Epithermal: } T = 50\text{--}200^\circ\text{C}, & P \le 100\text{ bar (shallow sub-volcanic)} \\ \text{Telethermal: } T < 100^\circ\text{C}, & \text{far-travelled basinal brines} \\ \text{Xenothermal: } T \approx 300\text{--}500^\circ\text{C}, & P \text{ low (telescoped volcanic)} \end{cases}",
            "Waldemar Lindgren's genetic classification establishes a quantitative continuum of hydrothermal ore deposition governed by decreasing temperature and lithostatic/hydrostatic confining pressure away from igneous or metamorphic heat engines. Fluid inclusions and stable isotope thermometry demonstrate that as ascending metalliferous aqueous solutions depressurize and cool, phase separation (boiling), wall-rock sulfidation, and fluid mixing trigger progressive metal precipitation along predictable paragenetic vectors.",
            "Lindgren, W. (1913, 1933, Mineral Deposits. McGraw-Hill); Graton, L.C. (1933, The hydrothermal depth-zones. Ore Deposits of the Western States); Buddington, A.F. (1935, Econ. Geol. 30: 205-222)"
        )

    # 3. Supergene Sulfide Oxidation & Enrichment
    if any(k in t_low for k in ["supergene", "oxidation", "gossan", "chalcocite", "limonite", "boxwork", "covellite"]):
        return (
            r"\text{Pyrite Oxidation: } 2\text{FeS}_2 + 7\text{O}_2 + 2\text{H}_2\text{O} \to 2\text{Fe}^{2+} + 4\text{SO}_4^{2-} + 4\text{H}^+; \quad \text{Enrichment: } 5\text{FeS}_2 + 14\text{Cu}^{2+} + 14\text{SO}_4^{2-} + 12\text{H}_2\text{O} \to 7\text{Cu}_2\text{S} \downarrow + 5\text{Fe}^{2+} + 19\text{SO}_4^{2-} + 24\text{H}^+",
            "Supergene sulfide enrichment represents a natural chemical beneficiation factory operating in the vadose and phreatic weathering zones. Above the water table, atmospheric oxygen and percolating meteoric waters oxidize primary pyrite into sulfuric acid and ferric sulfate. Highly soluble copper is leached as cupric sulfate and carried down to the reducing zone beneath the water table, where it reacts with primary chalcopyrite and pyrite through cation exchange, precipitating supergene blankets of chalcocite (Cu2S, 79.8% Cu) and covellite (CuS, 66.4% Cu) beneath an insoluble porous gossan cap.",
            "Emmons, W.H. (1917, The Enrichment of Ore Deposits. USGS Bull. 625); Titley, S.R. (1982, Advances in Geology of the Porphyry Copper Deposits. Univ. Arizona Press)"
        )

    # 4. Magmatic Segregation & Immiscible Sulfide Melts
    if any(k in t_low for k in ["magmatic", "chromite", "immiscible", "sideronitic", "bushveld", "sukinda", "kudremukh", "titanomagnetite"]):
        return (
            r"\text{Sulfide Partitioning: } D_i^{\text{sulf/sil}} = \frac{C_i^{\text{sulfide melt}}}{C_i^{\text{silicate melt}}}; \quad D_{\text{PGE}} \approx 10^4\text{--}10^5, \ D_{\text{Ni}} \approx 200\text{--}500, \ D_{\text{Cu}} \approx 600\text{--}1000",
            "Magmatic ore deposits crystallize directly from silicate or oxide-sulfide melts during fractional crystallization. Early magmatic gravitational settling concentrates dense, refractory, early-crystallized spinels (chromite, FeCr2O4) into stratiform cumulate reefs in layered intrusions (e.g., Sukinda, Bushveld). In sulfur-saturated mafic-ultramafic magmas, an immiscible dense sulfide liquid separates into immiscible droplets that scavenge chalcophile elements (Ni, Cu, Co, PGE) and collect at the base of the chamber.",
            "Naldrett, A.J. (2004, Magmatic Sulfide Deposits: Geology, Geochemistry and Exploration. Springer); Bateman, A.M. (1950, Economic Mineral Deposits. Wiley)"
        )

    # 5. Banded Iron Formations (BIFs) & Sedimentary Iron
    if any(k in t_low for k in ["bif", "banded iron", "algoma", "superior", "itabirite", "bailadila", "hematite", "magnetite"]):
        return (
            r"\text{Iron Precipitation: } 4\text{Fe}^{2+} + \text{O}_2 + 10\text{H}_2\text{O} \to 4\text{Fe}(\text{OH})_3 \downarrow + 8\text{H}^+; \quad 2\text{Fe}(\text{OH})_3 \xrightarrow{\Delta T, P} \text{Fe}_2\text{O}_3 \text{ (Hematite)} + 3\text{H}_2\text{O}",
            "Banded Iron Formations (BIFs) are rhythmically laminated Precambrian marine chemical sedimentary rocks containing >=15% iron and alternating chert/quartz bands. Algoma-type BIFs developed in Archean volcano-sedimentary greenstone belts via submarine hydrothermal exhalative venting. Superior-type BIFs precipitated on broad Paleoproterozoic continental passive margins between 2.6 and 1.8 Ga following the Great Oxidation Event (GOE) when free oxygen produced by cyanobacterial photosynthesis titrated vast reservoirs of anoxic dissolved oceanic ferrous iron.",
            "James, H.L. (1954, Sedimentary facies of iron-formation. Econ. Geol. 49: 235-293); Gross, G.A. (1980, A classification of iron formations. Can. Mineral. 18: 215-222)"
        )

    # 6. Residual Concentration & Bauxite Lateritization
    if any(k in t_low for k in ["bauxite", "laterite", "gibbsite", "kalahandi", "east coast", "lithomarge", "katni"]):
        return (
            r"\text{Bauxitization: } \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4 \text{ (Kaolinite)} + 5\text{H}_2\text{O} \xrightarrow{\text{leaching of SiO}_2} 2\text{Al}(\text{OH})_3 \text{ (Gibbsite)} \downarrow + 2\text{H}_4\text{SiO}_4 \text{ (aqueous)}",
            "Bauxite is a residual weathering product formed by prolonged tropical lateritization (humic, high-rainfall, well-drained conditions) of aluminous protoliths (khondalites in East Coast Bauxite, Deccan basalts in central India). As tropical groundwaters continuously leach mobile alkalis, alkaline earths, and silica (desilication), insoluble trivalent aluminum and ferric iron are residually enriched, crystallizing as gibbsite [Al(OH)3] and goethite/hematite capping elevated plateaus above a kaolinitic lithomarge clay base.",
            "Valeton, I. (1972, Bauxites. Elsevier); Balasubramaniam, K.S. (1988, Laterites and Bauxites of India. Oxford & IBH); Ausaf Sayeed (Objective Geology)"
        )

    # 7. Coal Petrology & Coalification Rank
    if any(k in t_low for k in ["coal", "lignite", "anthracite", "barakar", "neyveli", "palana", "jharia", "bituminous", "coking"]):
        return (
            r"\text{Coalification Series: } \text{Peat } (C \sim 55\%) \xrightarrow{\Delta T, P} \text{Lignite } (C \sim 65\text{--}72\%) \xrightarrow{} \text{Bituminous } (C \sim 75\text{--}90\%) \xrightarrow{} \text{Anthracite } (C > 92\%)",
            "Coal is a combustible organic sedimentary rock formed by the anaerobic biochemical compaction and thermal maturation of terrestrial plant debris (peat). The coalification continuum progresses under geothermal heating with expulsion of moisture, CO2, and methane, driving the systematic increase of fixed carbon, vitrinite reflectance (Ro), and calorific value while decreasing volatile matter. In India, over 98% of reserves occur in Permian Lower Gondwana formations (Barakar and Raniganj), with vital Tertiary lignite basins at Neyveli and Palana.",
            "Stach, E. et al. (1982, Stach's Textbook of Coal Petrology. Gebrüder Borntraeger); Chandra, D. et al. (2000, Coal and Organic Petrology. GSI Special Publ.)"
        )

    # 8. Industrial, Fertilizer & Strategic Minerals
    if any(k in t_low for k in ["barytes", "mica", "monazite", "asbestos", "thorium", "uranium", "gypsum", "diamond", "jaduguda", "mangampeta"]):
        return (
            r"\text{Reserves/Resource Formula: } \text{Tonnage} = V \cdot \rho \cdot (1 - \text{dilution}); \quad \text{Cut-Off Grade: } x_c = \frac{C_{\text{mining}} + C_{\text{milling}}}{R \cdot (P_{\text{metal}} - C_{\text{refining}})}",
            "Industrial and strategic minerals provide the foundational raw materials for chemical, agricultural, nuclear, and manufacturing industries. India holds globally dominant strategic positions in stratiform bedded barytes (Mangampeta volcanogenic deposit in Cuddapah Basin), book muscovite ruby mica (Bihar-Jharkhand and Nellore pegmatite belts), heavy mineral beach placers rich in thorium-bearing monazite and ilmenite (Chavara and Manavalakurichi), and shear-hosted hydrothermal uranium (Singhbhum Shear Zone).",
            "Kesler, S.E. & Simon, A.C. (2015, Mineral Resources, Economics and the Environment. Cambridge); Indian Bureau of Mines (IBM) Yearbooks"
        )

    # Default Economic Principles
    return (
        r"\text{Concentration Factor: } F_c = \frac{\text{Minimum Economic Tenor (Cut-off)}}{\text{Average Crustal Abundance (Clarke)}}; \quad \text{Ore} = \text{Mineral Aggregate Extractable at a Profit}",
        "Economic geology investigates the geological occurrence, spatial distribution, physical-chemical genesis, and commercial extraction of metallic ores, industrial minerals, fossil fuels, and nuclear raw materials. An ore deposit represents an anomalous geochemical concentration where natural geological processes have enriched specific elements by factors of hundreds to tens of thousands above their background crustal abundance, permitting economically profitable exploitation.",
        "Guilbert, J.M. & Park, C.F. (1986, The Geology of Ore Deposits. Freeman); Evans, A.M. (1993, Ore Geology and Industrial Minerals. Blackwell); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["hydrothermal", "epithermal", "mesothermal", "hypothermal", "telethermal", "xenothermal", "lindgren"]):
        return {
            "title": "Waldemar Lindgren's Hydrothermal Depth-Temperature Classification",
            "headers": ["Hydrothermal Zone", "Formation Temperature", "Estimated Depth Range", "Diagnostic Mineral Assemblage & Examples"],
            "rows": [
                ["Hypothermal", "300°C to 500-600°C", "3,000 to >10,000 m (deep)", "Gold-quartz veins (KGF, Hutti), tourmaline, cassiterite, arsenopyrite, pyrrhotite"],
                ["Mesothermal", "200°C to 300°C", "1,500 to 4,500 m (intermediate)", "Porphyry copper (Malanjkhand), Mother Lode gold, chalcopyrite, galena, sphalerite"],
                ["Epithermal", "50°C to 200°C", "<1,500 m (shallow subvolcanic)", "Bonanza gold-silver tellurides, electrum, stibnite, cinnabar, colloform chalcedony"],
                ["Telethermal", "<100°C", "Shallow to surface (distal)", "Mississippi Valley-type (MVT) stratabound galena-sphalerite, barite, fluorite in carbonates"],
                ["Xenothermal", "300°C to 500°C", "Shallow (<1,500 m, volcanic)", "Telescoped tin-tungsten-silver sulfosalts (Bolivian subvolcanic veins, cassiterite+stibnite)"]
            ]
        }

    if any(k in t_low for k in ["petroleum", "oil", "gas", "bombay high", "cambay", "digboi", "basin", "reservoir"]):
        return {
            "title": "Strategic Framework of Major Hydrocarbon-Producing Basins of India",
            "headers": ["Sedimentary Basin", "DGH Category", "Dominant Reservoir Strata", "Key Discoveries & Geological Traps"],
            "rows": [
                ["Mumbai Offshore (Bombay High)", "Category I (Proven)", "Early Miocene L-III Biomicritic Limestones", "Giant anticlinal limestone dome over basement uplift (1974); Heera, Panna, Neelam"],
                ["Cambay Basin (Gujarat)", "Category I (Proven)", "Eocene Hazad / Ankleshwar Sandstones", "Faulted rollover anticlines, drape folds; Ankleshwar (1960), Gandhar (largest onland)"],
                ["Assam Shelf (Upper Assam)", "Category I (Proven)", "Oligocene Barail / Miocene Tipam Sands", "Digboi (1889, oldest field), Nahorkatiya, Moran, Lakwa; fault-bounded anticlines"],
                ["Krishna-Godavari (KG) Basin", "Category I (Proven)", "Cretaceous-Tertiary Deltaic & Deepwater Sands", "Ravva (shallow offshore), Dhirubhai deepwater gas; channel-fan stratigraphic traps"],
                ["Cauvery Basin", "Category I (Proven)", "Cretaceous-Paleocene Fractured Basement & Sands", "Narimanam, Kovilkalappal; fault-block horst-graben combination traps"],
                ["Barmer-S持achor Basin", "Category I (Proven)", "Paleocene-Eocene Fatehgarh Sandstones", "Mangala, Bhagyam, Aishwarya; rift basin fault-block structural closures"]
            ]
        }

    if any(k in t_low for k in ["bauxite", "laterite", "east coast", "kalahandi", "aluminium"]):
        return {
            "title": "Comparative Petrogenetic Framework of Indian Bauxite Deposits",
            "headers": ["Bauxite Province", "Geologic Protolith Rock", "Primary Hydrate Mineralogy", "Deposit Morphology & Topographic Setting"],
            "rows": [
                ["East Coast Bauxite (Odisha/A.P.)", "Khondalites (garnet-sillimanite metapelites)", "Gibbsite [Al(OH)3] (>90%, trihydrate)", "Colossal continuous blanket capping high plateaus (1000-1400 m; Panchpatmali, Baphlimali)"],
                ["Central India (M.P. & Chhattisgarh)", "Deccan Traps (tholeiitic basalts)", "Mixture of Gibbsite and Boehmite [AlO(OH)]", "High-level lateritic blanket caps on Maikal Hills, Amarkantak, Bailadila, Phutkapahar"],
                ["Jharkhand (Ranchi-Palamau)", "Chota Nagpur granitic gneisses & basalt relicts", "Gibbsite with subordinate boehmite and diaspore", "Lochandas and Bagru hill flat-topped mesas capping Archean basement"],
                ["Gujarat (Kutch & Jamnagar)", "Deccan Trap lavas and Tertiary supratrappean clays", "Boehmite, gibbsite, and detrital nodules", "Low-lying coastal plains, reworked detrital/sedimentary pockets under marine clays"],
                ["Katni Region (M.P.)", "Vindhyan quartzites and clay formations", "Gibbsite and diasporic bauxite", "Low-level valley deposits, sinkhole pocket accumulations, reworked detrital ore beds"]
            ]
        }

    if any(k in t_low for k in ["manganese", "iron", "copper", "lead", "zinc", "chromite", "zawar", "khetri"]):
        return {
            "title": "Premier Metallic Ore Belts of India: Geologic Setting & Paragenesis",
            "headers": ["Mineral Commodity", "World-Class Indian Mining District", "Host Geological Formation", "Diagnostic Primary Ore Mineral Assemblage"],
            "rows": [
                ["Lead-Zinc-Silver", "Zawar & Rampura-Agucha (Rajasthan)", "Aravalli carbonates (Zawar); BGC schists (Agucha)", "Sphalerite (ZnS) + Galena (PbS) + Pyrite + Argentite in dolomites/schists"],
                ["Copper", "Singhbhum (Jharkhand) & Khetri (Rajasthan)", "Singhbhum Shear Zone schists; Delhi Group phyllites", "Chalcopyrite (CuFeS2) + Pyrrhotite + Pyrite + Bornite in quartz veins"],
                ["Iron Ore (Hematite/Magnetite)", "Bailadila (C.G.), Barabil (Odisha), Kudremukh (K.T.)", "Precambrian Banded Iron Formations (BHQ/BHJ/BMQ)", "Hematite (Fe2O3) in enriched supergene zones; Magnetite (Fe3O4) in BMQ"],
                ["Manganese", "Balaghat-Nagpur (M.P./M.S.) & Sukinda (Odisha)", "Sausar Group Gondites; Eastern Ghats Kodurites", "Braunite (3Mn2O3·MnSiO3) + Pyrolusite (MnO2) + Psilomelane + Hausmannite"],
                ["Chromite", "Sukinda Valley (Jajpur district, Odisha)", "Precambrian ultramafics (serpentinized dunite-peridotite)", "Stratiform cumulate Chromite (FeCr2O4) seams with nickeliferous laterites"],
                ["Gold", "Kolar Gold Field & Hutti (Karnataka)", "Neoarchean greenstone amphibolites (Dharwar Craton)", "Native gold in quartz-carbonate veins + Pyrrhotite + Arsenopyrite + Galena"]
            ]
        }

    # Default Economic Synthesis Table
    return {
        "title": "Classification and Physicochemical Criteria of Mineral Deposits",
        "headers": ["Genetic Class", "Primary Physicochemical Mechanism", "P-T Regimes & Environments", "Benchmark Commodity Examples"],
        "rows": [
            ["Magmatic Segregation", "Gravitational crystal settling / liquid immiscibility", "T > 1000°C, deep plutonic chambers", "Bushveld & Sukinda chromite, Sudbury Ni-Cu sulfides, Bushveld Merensky PGE"],
            ["Hydrothermal Veins", "Aqueous fluid transport as chloride/bisulfide complexes", "T = 50-600°C, crustal fracture networks", "KGF gold-quartz lodes, Khetri copper, Zawar lead-zinc, Cornwall tin-tungsten"],
            ["Contact Metasomatic (Skarn)", "Reaction between magmatic fluids and carbonate wall rock", "T = 400-800°C, intrusive contact aureoles", "Tungsten-fluorite skarns (Sirohi), iron-copper skarns, wollastonite"],
            ["Sedimentary Chemical / Exhalative", "Syngenetic subaqueous precipitation / black smokers", "Sedimentary basins, marine water columns", "Lake Superior & Bailadila BIFs, Sausar gondite manganese, Kupferschiefer copper"],
            ["Residual Weathering", "Intense chemical leaching and residual concentration", "Subaerial tropical weathering profiles", "East Coast lateritic bauxite, Sukinda nickeliferous laterite, China clay"],
            ["Mechanical Placer", "Hydrodynamic sorting by moving water, waves, or wind", "Rivers, beaches, alluvial floodplains", "Kerala monazite-ilmenite beach sands, California alluvial gold, Witwatersrand paleoplacers"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["petroleum", "oil", "gas", "reservoir"]):
        return [
            {
                "question": "Which of the following organic matter kerogen types is predominantly oil-prone and formed primarily from lacustrine algal and planktonic precursors?",
                "options": {
                    "a": "Type I Kerogen",
                    "b": "Type II Kerogen",
                    "c": "Type III Kerogen",
                    "d": "Type IV Kerogen"
                },
                "answer": "a",
                "explanation": "Type I kerogen has the highest atomic H/C ratio (>1.5) and lowest O/C ratio, derived from algal lipids and highly oil-prone upon thermal maturation in the oil window."
            },
            {
                "question": "The primary carbonate reservoir horizon that accounts for over 80% of hydrocarbon reserves in the offshore Bombay High field is designated as:",
                "options": {
                    "a": "L-I limestone",
                    "b": "L-II limestone",
                    "c": "L-III limestone",
                    "d": "S-I sandstone"
                },
                "answer": "c",
                "explanation": "The Early Miocene L-III biomicrite carbonate sequence is the principal regional reservoir of Bombay High, characterized by high primary and vuggy solution porosity."
            }
        ]

    if any(k in t_low for k in ["hydrothermal", "epithermal", "mesothermal", "hypothermal"]):
        return [
            {
                "question": "Which of the following hydrothermal depth-zones is characterized by mineralization deposited by far-traveled, spent solutions at low temperatures in rocks displaying minimal wall-rock alteration?",
                "options": {
                    "a": "Hypothermal",
                    "b": "Xenothermal",
                    "c": "Telethermal",
                    "d": "Epithermal"
                },
                "answer": "c",
                "explanation": "L.C. Graton (1933) established the 'telethermal' zone for low-temperature hydrothermal deposits (e.g., MVT lead-zinc) formed far from their igneous heat sources with negligible host-rock alteration."
            },
            {
                "question": "What physical parameter uniquely distinguishes 'Xenothermal' mineral deposits from standard hypothermal deposits?",
                "options": {
                    "a": "Extremely high pressure at low temperature",
                    "b": "High temperature at anomalously shallow crustal depths (low lithostatic pressure)",
                    "c": "Formation strictly under submarine abyssal conditions",
                    "d": "Deposition exclusively by cold meteoric descending waters"
                },
                "answer": "b",
                "explanation": "A.F. Buddington defined xenothermal deposits as high-temperature ore systems emplaced at shallow depths (low pressure), causing rapid fluid boiling and severe telescoping of mineral assemblages."
            }
        ]

    # Default Economic Practice Problems
    return [
        {
            "question": "In the supergene weathering profile of a copper sulfide ore body, which of the following secondary sulfide minerals marks the highest grade of copper enrichment immediately beneath the water table?",
            "options": {
                "a": "Chalcocite (Cu2S)",
                "b": "Malachite",
                "c": "Azurite",
                "d": "Cuprite"
            },
            "answer": "a",
            "explanation": "Chalcocite contains 79.8% metallic copper and forms the primary constituent of the supergene enrichment blanket through replacement of primary chalcopyrite and pyrite under reducing conditions."
        },
        {
            "question": "The world's largest single deposit of stratiform bedded volcanogenic barytes (BaSO4) is located in which geological basin of India?",
            "options": {
                "a": "Vindhyan Basin",
                "b": "Cuddapah Basin (Mangampeta)",
                "c": "Gondwana Basin",
                "d": "Aravalli Basin"
            },
            "answer": "b",
            "explanation": "Mangampeta in the Cuddapah Basin of Andhra Pradesh contains over 70 million tonnes of bedded tuffaceous barytes formed by submarine felsic exhalative volcanism during the Proterozoic."
        }
    ]
