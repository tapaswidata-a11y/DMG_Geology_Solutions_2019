#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Metamorphic Formulations, and Syntheses for Chapter 13: Metamorphic Petrology
Dr. Ausaf Sayeed - Objective Geology (150 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Al2SiO5 Phase Equilibria & Geothermobarometry
    if any(k in t_low for k in ["al2sio5", "kyanite", "andalusite", "sillimanite", "triple point"]):
        return (
            r"\text{Triple Point: } T \approx 500^\circ\text{C}, \quad P \approx 3.76\text{ kbar} \quad (\text{Holdaway, 1971}); \quad \Delta V_{\text{And} \to \text{Ky}} = -5.7\text{ cm}^3/\text{mol}",
            "The aluminosilicate polymorphic system (Kyanite-Andalusite-Sillimanite) represents the universal petrological calibration grid for metapelitic rocks. Because all three polymorphs share the identical anhydrous stoichiometry (Al2SiO5), phase boundaries depend solely on pressure and temperature without fluid composition interference. Kyanite has the smallest molar volume (44.09 cm3/mol) and highest density (3.67 g/cm3), stabilized by high lithostatic pressure; andalusite has the largest molar volume (51.53 cm3/mol), stable at low pressure; and sillimanite is the high-temperature entropy-stabilized polymorph.",
            "Holdaway, M.J. (1971, Stability of andalusite and the aluminum silicate phase diagram. Am. J. Sci. 271: 97-131); Pattison, D.R.M. (1992, J. Geol. 100: 423-446)"
        )

    # 2. Goldschmidt's Mineralogical Phase Rule & ACF/AKF Projections
    if any(k in t_low for k in ["phase rule", "acf", "akf", "afm", "goldschmidt", "p <= c", "thompson"]):
        return (
            r"P \le C \quad (F = C - P + 2 \ge 2 \implies P \le C); \quad A = [\text{Al}_2\text{O}_3 + \text{Fe}_2\text{O}_3] - [\text{Na}_2\text{O} + \text{K}_2\text{O}], \ C = \text{CaO} - 3.3\text{P}_2\text{O}_5, \ F = \text{FeO} + \text{MgO}",
            "V.M. Goldschmidt's (1911) Mineralogical Phase Rule states that because metamorphic mineral assemblages persist over finite geographic zones of temperature and confining pressure (divariant fields, variance F >= 2), the number of coexisting stable equilibrium phases (P) cannot exceed the number of independent chemical components (C): P <= C. Eskola (1915) designed the ACF and AKF triangular projection diagrams by subtracting alkalis bound in feldspars from alumina, allowing graphical representation of metamorphic facies assemblages.",
            "Goldschmidt, V.M. (1911, Die Kontaktmetamorphose im Kristianiagebiet); Eskola, P. (1915, On the Petrology of the Orijärvi Region); Thompson, J.B. (1957, Am. Mineral. 42: 842-858)"
        )

    # 3. Barrow's Progressive Zones & Isograds
    if any(k in t_low for k in ["barrow", "isograd", "barrovian", "dalradian", "chlorite zone", "biotite zone", "staurolite"]):
        return (
            r"\text{Barrovian Sequence: } \text{Chlorite} \xrightarrow{400^\circ\text{C}} \text{Biotite} \xrightarrow{500^\circ\text{C}} \text{Garnet (Alm)} \xrightarrow{550^\circ\text{C}} \text{Staurolite} \xrightarrow{600^\circ\text{C}} \text{Kyanite} \xrightarrow{680^\circ\text{C}} \text{Sillimanite}",
            "George Barrow (1893, 1912) established the foundational concept of progressive metamorphic index zones in the pelitic Dalradian rocks of the Scottish Highlands. Tilley (1924) formalized the boundaries as 'isograds', representing surfaces of equal metamorphic grade where a specific net-transfer reaction occurs. Under medium P/T Barrovian conditions (~4-8 kbar), prograde dewatering progressively reconstructs low-grade chlorite and white mica into increasingly dense anhydrous framework and nesosilicate minerals.",
            "Barrow, G. (1893, On an intrusion of muscovite-biotite gneiss in the SE Highlands of Scotland. Q. J. Geol. Soc. Lond. 49: 330-358); Tilley, C.E. (1924, Geol. Mag. 61: 167-171)"
        )

    # 4. Eclogites & Blueschists (Subduction Metamorphism)
    if any(k in t_low for k in ["eclogite", "blueschist", "glaucophane", "lawsonite", "omphacite", "pyrope"]):
        return (
            r"\text{Eclogite Transition: } \text{Plagioclase} + \text{Pyroxene} \xrightarrow{P > 12\text{--}15\text{ kbar}} \text{Omphacite } (\text{Cpx}_{ss}) + \text{Pyrope-rich Garnet} + \text{Quartz}",
            "Eclogites and blueschists are diagnostic of high-pressure, low-to-moderate-temperature metamorphism developed along active subduction zones (Miyashiro's high P/T facies series). Under pressures >12-15 kbar (>45-50 km depth), low-density plagioclase feldspar breaks down completely into jadeite-diopside solid solution (omphacite) and almandine-pyrope garnet, creating ultra-dense (density > 3.4-3.6 g/cm3) mantle-penetrating oceanic slab residues.",
            "Eskola, P. (1921, The mineral facies of rocks. Norsk Geol. Tidsskr. 6: 143-194); Coleman, R.G. et al. (1965, Eclogites and eclogites. GSA Bull. 76: 483-508)"
        )

    # 5. Granulite Facies & Charnockites
    if any(k in t_low for k in ["granulite", "charnockite", "enderbite", "hypersthene", "khondalite"]):
        return (
            r"\text{Granulite Dehydration: } \text{Hornblende} + \text{Quartz} \xrightarrow{> 750^\circ\text{C}} \text{Orthopyroxene (Hypersthene)} + \text{Clinopyroxene} + \text{Plagioclase} + \text{H}_2\text{O}",
            "The Granulite facies represents the highest temperature regional metamorphic regime in continental crust (>750-950°C, 6-11 kbar). Primary hydrous minerals (micas, amphiboles) break down into anhydrous pyroxenes, garnets, and perthites. Charnockites are orthopyroxene-bearing quartzofeldspathic granulites formed under low water activity (aH2O < 0.3) facilitated by deep crustal CO2-carbonic fluid flushing or fluid-absent anatectic melt extraction.",
            "Holland, T.H. (1900, The charnockite series. Mem. Geol. Surv. India 28: 119-249); Newton, R.C. (1992, Charnockitic graintisation: An overview. J. Geol. Soc. India)"
        )

    # 6. Cataclastic & Dynamic Metamorphism (Fault Rocks)
    if any(k in t_low for k in ["mylonite", "cataclasite", "pseudotachylyte", "mortar", "flaser", "shear zone"]):
        return (
            r"\text{Fault Rock Evolution: } \text{Mortar Texture (Brittle)} \to \text{Cataclasite} \to \text{Mylonite (Ductile Dynamic Recrystallization)} \to \text{Pseudotachylyte (Frictional Melt)}",
            "Dynamic metamorphism concentrates intense non-hydrostatic shear strain along localized fault and plate-boundary shear zones. In the brittle upper crust (<10-15 km), frictional cataclasis produces non-foliated fault breccias and cataclasites via microcracking and grain milling. In the ductile deeper crust (>250-300°C for quartz, >450°C for feldspar), dislocation creep and dynamic recrystallization generate cohesive, foliated mylonites with eye-shaped porphyroclasts and ribbon quartz.",
            "Lapworth, C. (1885, The Highland controversy in British geology. Nature 32: 558-559); Sibson, R.H. (1977, Fault rocks and fault mechanisms. J. Geol. Soc. Lond. 133: 191-213)"
        )

    # 7. Anatexis & Migmatite Petrology
    if any(k in t_low for k in ["migmatite", "anatexis", "leucosome", "melanosome", "palingenesis", "ptygmatic"]):
        return (
            r"\text{Anatexis: } \text{Paleosome (Parent)} \to \text{Neosome} \begin{cases} \text{Leucosome (Granitic partial melt: Qz + Fsp)} \\ \text{Melanosome (Refractory restite: Bt + Grt + Sil)} \end{cases}",
            "Anatexis is the in-situ partial melting of rocks under upper-amphibolite and granulite facies conditions. Water-saturated minimum melting in the haplogranite system (Ab-Or-Qz-H2O) initiates at 650-700°C at 5 kbar. Migmatites preserve the intimate structural segregation of newly crystallized quartzofeldspathic melt ribbons (leucosome), dark refractory residues of biotite-garnet-sillimanite (melanosome), and unmolten paleosome domains deformed into ptygmatic folds.",
            "Mehnert, K.R. (1968, Migmatites and the Origin of Granitic Rocks. Elsevier); Sawyer, E.W. (2008, Atlas of Migmatites. Can. Mineral. Spec. Publ. 9)"
        )

    # 8. Carbonate Metamorphism & Skarns
    if any(k in t_low for k in ["wollastonite", "skarn", "forsterite", "diopside", "decarbonation"]):
        return (
            r"\text{Decarbonation Reactions: } \begin{cases} \text{CaCO}_3 + \text{SiO}_2 \to \text{CaSiO}_3 \text{ (Wollastonite)} + \text{CO}_2 \uparrow \\ \text{CaMg}(\text{CO}_3)_2 + 2\text{SiO}_2 \to \text{CaMgSi}_2\text{O}_6 \text{ (Diopside)} + 2\text{CO}_2 \uparrow \\ 2\text{CaMg}(\text{CO}_3)_2 + \text{SiO}_2 \to \text{Mg}_2\text{SiO}_4 \text{ (Forsterite)} + 2\text{CaCO}_3 + 2\text{CO}_2 \uparrow \end{cases}",
            "Contact metamorphism of siliceous limestones and dolostones is governed by progressive decarbonation reactions driven by temperature elevation and continuous volatile dilution (XCO2 vs XH2O). The initial reaction produces tremolite, followed by diopside, forsterite, and wollastonite. In metasomatic skarns, infiltration of Fe-Si-Al-rich hydrothermal fluids from magmatic plutons converts carbonate beds into grossular-andradite garnet, diopside-hedenbergite, and wollastonite.",
            "Bowen, N.L. (1940, Progressive metamorphism of siliceous limestone and dolomite. J. Geol. 48: 225-274); Einaudi, M.T. et al. (1981, Skarn deposits. Econ. Geol. 75th Anniv. Vol.)"
        )

    # Default Metamorphic Principles
    return (
        r"\text{Metamorphic Transformation: } \text{Protolith} + \Delta T + \Delta P + \Delta \sigma_{ij} + \text{Fluids} \to \text{Equilibrium Mineral Assemblage}",
        "Metamorphic petrology deciphers the thermodynamic transformations, kinetic recrystallization pathways, and structural fabrics that develop when rocks adjust to temperatures and pressures prevailing in Earth's interior. Combining phase equilibria, multi-component geothermobarometry, and isotopic geochronology provides quantitative reconstructions of tectonic burial, orogenic crustal thickening, and unroofing trajectories.",
        "Winter, J.D. (2014, Principles of Igneous and Metamorphic Petrology. Pearson); Spear, F.S. (1993, Metamorphic Phase Equilibria and Pressure-Temperature-Time Paths); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["facies", "eskola", "greenschist", "amphibolite", "granulite", "eclogite", "blueschist"]):
        return {
            "title": "Comprehensive Framework of Eskola's Metamorphic Facies",
            "headers": ["Metamorphic Facies", "P-T Field Range", "Diagnostic Metabasite Assemblage", "Diagnostic Metapelite Assemblage"],
            "rows": [
                ["Zeolite Facies", "100-200°C, 1-3 kbar", "Laumontite + Heulandite + Albite + Chlorite", "Smectite + Illite + Quartz (incipient diagenesis)"],
                ["Greenschist Facies", "300-450°C, 3-8 kbar", "Albite + Actinolite + Epidote + Chlorite", "Muscovite (sericite) + Chlorite + Quartz + Albite"],
                ["Amphibolite Facies", "500-700°C, 4-10 kbar", "Hornblende + Plagioclase (>An20) ± Garnet", "Biotite + Almandine Garnet + Staurolite + Kyanite"],
                ["Granulite Facies", ">750-950°C, 5-11 kbar", "Orthopyroxene (Hypersthene) + Cpx + Plagioclase", "Garnet + Sillimanite + K-feldspar + Quartz (Khondalite)"],
                ["Blueschist Facies", "200-400°C, 6-12 kbar", "Glaucophane + Lawsonite / Epidote + Aragonite", "Phengite + Paragonite + Glaucophane + Quartz"],
                ["Eclogite Facies", "500-900°C, >12-25 kbar", "Omphacite (sodic Cpx) + Pyrope Garnet (no plagioclase)", "Kyanite + Phengitic Muscovite + Quartz/Coesite"]
            ]
        }

    if any(k in t_low for k in ["barrow", "zone", "isograd", "staurolite", "kyanite", "sillimanite"]):
        return {
            "title": "George Barrow's (1893) Classic Metamorphic Zones in Pelitic Rocks",
            "headers": ["Index Zone", "Critical Index Mineral", "Key Prograde Net-Transfer Reaction", "Metamorphic Facies Equivalent"],
            "rows": [
                ["Chlorite Zone", "Chlorite + Sericite", "Smectite/illite recrystallization in pelites", "Lower Greenschist Facies (~300-350°C)"],
                ["Biotite Zone", "Biotite (brown titaniferous)", "Chlorite + Muscovite -> Biotite + Al-Chlorite + Qz", "Upper Greenschist Facies (~400-450°C)"],
                ["Garnet Zone", "Almandine Garnet", "Chlorite + Biotite + Qz -> Almandine + Muscovite + H2O", "Epidote-Amphibolite Facies (~500°C)"],
                ["Staurolite Zone", "Staurolite (idioblastic cruciform)", "Garnet + Chlorite -> Staurolite + Biotite + H2O", "Lower Amphibolite Facies (~550-600°C)"],
                ["Kyanite Zone", "Kyanite (bladed triclinic)", "Staurolite + Chlorite + Qz -> Kyanite + Biotite + H2O", "Middle Amphibolite Facies (~600-650°C)"],
                ["Sillimanite Zone", "Sillimanite (fibrolite)", "Muscovite + Quartz -> K-feldspar + Sillimanite + H2O", "Upper Amphibolite Facies (>680°C)"]
            ]
        }

    if any(k in t_low for k in ["cataclastic", "mylonite", "shear", "fault", "pseudotachylyte"]):
        return {
            "title": "Classification and Microstructural Evolution of Fault Rocks (Sibson, 1977)",
            "headers": ["Fault Rock Type", "Deformation Regime", "Cohesion & Fabric", "Dominant Deformation Mechanism"],
            "rows": [
                ["Fault Breccia / Gouge", "Brittle (upper 1-5 km)", "Incohesive, random unoriented fabric", "Frictional sliding, brittle fracturing, comminution"],
                ["Cataclasite", "Brittle (depth 5-10 km)", "Cohesive, non-foliated, microbrecciated", "Microcracking, grain rotation, mechanical granulation"],
                ["Flaser Rock / Flasergneis", "Brittle-ductile transition", "Cohesive, lenticular relics in sheared bands", "Incipient crystal-plastic strain around rigid augen"],
                ["Mylonite / Ultramylonite", "Ductile shear (>10-15 km, >300°C)", "Cohesive, strongly foliated, fluxion structure", "Dislocation creep, dynamic recrystallization, grain-size reduction"],
                ["Pseudotachylyte", "Coseismic slip surface (all depths)", "Glassy or cryptocrystalline black injection veins", "Thermal frictional melting during rapid seismic rupture"]
            ]
        }

    # Default Metamorphic Petrology Synthesis Table
    return {
        "title": "Comparative Mineralogical Evolution of Major Metamorphic Protoliths",
        "headers": ["Protolith Class", "Low Grade (Greenschist)", "Medium Grade (Amphibolite)", "High Grade (Granulite)"],
        "rows": [
            ["Pelitic (Shales/Mudstones)", "Chlorite + Sericite + Quartz + Albite", "Biotite + Almandine + Staurolite + Kyanite", "Garnet + Sillimanite + K-feldspar + Cordierite"],
            ["Basic / Mafic (Basalts/Gabbros)", "Albite + Actinolite + Epidote + Chlorite", "Hornblende + Plagioclase (Oligoclase-Andesine)", "Orthopyroxene (Hypersthene) + Cpx + Plagioclase"],
            ["Calcareous (Impure Limestone)", "Calcite + Quartz + Talc + Tremolite", "Calcite + Diopside + Grossular Garnet", "Wollastonite + Anorthite + Vesuvianite / Forsterite"],
            ["Quartzo-Feldspathic (Arkose/Granite)", "Quartz + Microcline + Albite + Sericite", "Quartz + Oligoclase + Microcline + Biotite", "Mesoperthite + Quartz + Garnet ± Hypersthene (Charnockite)"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["al2sio5", "kyanite", "andalusite", "sillimanite"]):
        return [
            {
                "question": "In a metapelitic schist, kyanite and sillimanite are found coexisting in mutual contact with quartz and muscovite. Assuming Holdaway's (1971) phase diagram, what can be deduced about the minimum pressure of crystallization?",
                "options": {
                    "a": "< 2.0 kbar",
                    "b": ">= 3.76 kbar",
                    "c": "< 1.5 kbar",
                    "d": "Strictly at atmospheric pressure"
                },
                "answer": "b",
                "explanation": "The Kyanite-Sillimanite phase boundary originates at the triple point (~3.76 kbar, 500°C) and ascends to higher pressures and temperatures; hence, kyanite-sillimanite equilibrium requires P >= 3.76 kbar."
            },
            {
                "question": "Which of the following Al2SiO5 polymorphs has the highest crystal density and is considered the classic diagnostic 'stress mineral' of Barrovian metamorphism?",
                "options": {
                    "a": "Andalusite",
                    "b": "Kyanite",
                    "c": "Sillimanite",
                    "d": "Mullite"
                },
                "answer": "b",
                "explanation": "Kyanite is triclinic with a density of 3.53-3.67 g/cm3 (significantly denser than andalusite at 3.15 and sillimanite at 3.23), stabilized by high pressure and deviatoric shear stress."
            }
        ]

    if any(k in t_low for k in ["facies", "greenschist", "amphibolite", "granulite", "eclogite", "blueschist"]):
        return [
            {
                "question": "A metabasic rock contains omphacitic pyroxene and pyrope-almandine garnet, with zero plagioclase feldspar. To which metamorphic facies does this rock belong?",
                "options": {
                    "a": "Amphibolite facies",
                    "b": "Granulite facies",
                    "c": "Eclogite facies",
                    "d": "Blueschist facies"
                },
                "answer": "c",
                "explanation": "The bimineralic assemblage of omphacite clinopyroxene and pyrope-rich garnet in the absence of plagioclase is the defining diagnostic hallmark of the Eclogite facies."
            },
            {
                "question": "The appearance of which of the following minerals in basic rocks definitively marks the entry from the amphibolite facies into the granulite facies?",
                "options": {
                    "a": "Glaucophane",
                    "b": "Orthopyroxene (Hypersthene)",
                    "c": "Tremolite",
                    "d": "Epidote"
                },
                "answer": "b",
                "explanation": "In metabasites, the prograde dehydration breakdown of hornblende into orthopyroxene (hypersthene) + clinopyroxene + plagioclase marks the fundamental boundary of the Granulite facies."
            }
        ]

    # Default Metamorphic Petrology Practice Problems
    return [
        {
            "question": "According to George Barrow's classic metamorphic zonation of the Scottish Highlands, what is the correct progressive sequence of index minerals in pelitic rocks with increasing grade?",
            "options": {
                "a": "Chlorite -> Biotite -> Garnet -> Staurolite -> Kyanite -> Sillimanite",
                "b": "Biotite -> Chlorite -> Garnet -> Kyanite -> Staurolite -> Sillimanite",
                "c": "Chlorite -> Garnet -> Biotite -> Staurolite -> Kyanite -> Sillimanite",
                "d": "Sillimanite -> Kyanite -> Staurolite -> Garnet -> Biotite -> Chlorite"
            },
            "answer": "a",
            "explanation": "The classic Barrovian progressive sequence in pelites is: Chlorite -> Biotite -> Almandine Garnet -> Staurolite -> Kyanite -> Sillimanite."
        },
        {
            "question": "Which of the following fault rocks is characterized by dark glassy or cryptocrystalline veinlets formed by frictional melting during rapid seismic rupture?",
            "options": {
                "a": "Mylonite",
                "b": "Pseudotachylyte",
                "c": "Cataclasite",
                "d": "Phyllonite"
            },
            "answer": "b",
            "explanation": "Pseudotachylyte represents fossil earthquake slip surfaces formed by localized frictional melt generation along high-velocity fault planes during seismic slip."
        }
    ]
