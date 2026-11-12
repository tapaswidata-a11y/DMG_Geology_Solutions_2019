#!/usr/bin/env python3
"""
Verified Questions Q1 to Q30 for Chapter 2: Physical Geology & Geomorphology
Dr. Ausaf Sayeed - Objective Geology
"""

BATCH1_QS = {
    1: {
        "q": 1,
        "topic": "Chemical Weathering: Oceanic Geochemistry & Na-K Partitioning",
        "question": "Although sodium and potassium have approximately equal concentrations in nature, the waters of the seas and oceans are relatively strongly enriched in sodium because :",
        "options": {
            "A": "the potash feldspars have low stability relative to plagioclase feldspar",
            "B": "sodium is chemically more reactive than potassium",
            "C": "potassium enters readily into newly formed clay minerals while sodium tends to remain in solution",
            "D": "sodium is NOT particularly stable in the weathering environment and therefore passes into solution"
        },
        "ans": "C",
        "ref": "Arthur Holmes (Principles of Physical Geology, pp. 380–395); Krauskopf & Bird (Introduction to Geochemistry, Ch. 13); Faure (Principles of Geochemistry)"
    },
    2: {
        "q": 2,
        "topic": "Sedimentary Geochemistry: Aluminum Insolubility and Residual Clay Concentration",
        "question": "The aluminium content of sedimentary rocks is usually very high because :\nI. Aluminium is one of the most insoluble elements and does not readily go into solution\nII. Much of the aluminium is taken up by the clay minerals to form clay-rich rocks\nIII. Formation of residual deposits leads to the concentration of aluminium in sedimentary rocks",
        "options": {
            "A": "I and II are correct",
            "B": "I and III are correct",
            "C": "II and III are correct",
            "D": "All of the above are correct"
        },
        "ans": "D",
        "ref": "Mason & Moore (Principles of Geochemistry, Ch. 6); Sam Boggs Jr. (Principles of Sedimentology and Stratigraphy, Ch. 7)"
    },
    3: {
        "q": 3,
        "topic": "Weathering Regimes: Ubiquity of Mechanical Weathering across Extreme Climates",
        "question": "Physical weathering is NOT characteristic of :",
        "options": {
            "A": "Polar regions",
            "B": "Hot deserts",
            "C": "Cold deserts",
            "D": "None of the above"
        },
        "ans": "D",
        "ref": "Arthur Holmes (pp. 370–385); W.D. Thornbury (Principles of Geomorphology, Ch. 4); Bloom (Geomorphology, Ch. 6)"
    },
    4: {
        "q": 4,
        "topic": "Mechanical Weathering: Exfoliation and Onion-Skin Sheeting",
        "question": "Exfoliation is a form of :",
        "options": {
            "A": "Physical weathering",
            "B": "Chemical weathering",
            "C": "Biochemical weathering",
            "D": "Mass wasting"
        },
        "ans": "A",
        "ref": "W.D. Thornbury (Principles of Geomorphology, pp. 68–75); K.M. Bangar (Principles of Engineering Geology, p. 58)"
    },
    5: {
        "q": 5,
        "topic": "Rock Fabric & Mechanical Weathering: Exfoliation Domes in Massive Plutonic Rocks",
        "question": "Exfoliation is most characteristically found in :",
        "options": {
            "A": "Granites",
            "B": "Spilites",
            "C": "Arkoses",
            "D": "Orthoquartzites"
        },
        "ans": "A",
        "ref": "Arthur Holmes (Principles of Physical Geology, pp. 385–390); W.D. Thornbury (p. 72); Billings (Structural Geology)"
    },
    6: {
        "q": 6,
        "topic": "Weathering Coupling: Role of Chemical Hydration in Assisting Physical Exfoliation",
        "question": "Exfoliation, a dominant physical process, is also assisted by some chemical processes. The most important part is played by :",
        "options": {
            "A": "Hydration",
            "B": "Oxidation",
            "C": "Hydrolysis",
            "D": "Carbonation"
        },
        "ans": "A",
        "ref": "Arthur Holmes (Principles of Physical Geology, p. 388); Ollier (Weathering, Ch. 3); Thornbury (p. 73)"
    },
    7: {
        "q": 7,
        "topic": "Chemical Weathering Mechanics: Volumetric Expansion and Density Loss via Hydration",
        "question": "Hydration of a salt is accompanied by one or more of the following :\n(1) increase in volume\n(2) increase in porosity\n(3) decrease in density\n(4) decrease in volume",
        "options": {
            "A": "1 and 3 only",
            "B": "1, 2 and 3 only",
            "C": "2 and 4 only",
            "D": "2, 3 and 4 only"
        },
        "ans": "B",
        "ref": "Dr. Ausaf Sayeed (Explanatory Note *7, p. 143); Arthur Holmes (p. 382); Winkler (Stone: Properties, Durability in Man's Environment)"
    },
    8: {
        "q": 8,
        "topic": "Goldich Weathering Stability Series: Silicate Polymerization Controls on Mineral Durability",
        "question": "According to the Mineral Stability series of Goldich :",
        "options": {
            "A": "olivine weathers to pyroxene and pyroxene weathers to hornblende",
            "B": "olivine, pyroxene and hornblende have equal susceptibility to weathering",
            "C": "minerals rich in Si-O are least resistant to chemical weathering",
            "D": "olivine is less stable than pyroxene and pyroxene is less stable than hornblende"
        },
        "ans": "D",
        "ref": "S.S. Goldich (1938, J. Geol. 46, pp. 17–58); Sam Boggs Jr. (pp. 14–18); Faure (Principles of Geochemistry)"
    },
    9: {
        "q": 9,
        "topic": "Climatic Geomorphology: Tropical Humid Regimes and Accelerated Chemical Weathering",
        "question": "Which one of the following places is more likely to be affected by chemical weathering ?",
        "options": {
            "A": "Thar Desert",
            "B": "Tibetan plateau",
            "C": "Leh",
            "D": "Siwalik"
        },
        "ans": "D",
        "ref": "Arthur Holmes (Principles of Physical Geology, Ch. 12); D.N. Wadia (Geology of India); Thornbury (pp. 58–65)"
    },
    10: {
        "q": 10,
        "topic": "Mass Wasting Dynamics: Gravitational Transfer of Regolith and Bedrock",
        "question": "Mass Wasting may be described as :",
        "options": {
            "A": "Excessive loss of material by landslides",
            "B": "Downslope movement of rock and soil under the direct influence of gravity",
            "C": "Excessive loss of organically-rich top soil due to soil erosion",
            "D": "Flowage of saturated debris in periglacial regions"
        },
        "ans": "B",
        "ref": "Sharpe (Landslides and Related Phenomena, Columbia Univ. Press); Varnes (1978, Landslides Analysis and Control); Thornbury (Ch. 4)"
    },
    11: {
        "q": 11,
        "topic": "Kinematics of Mass Wasting: Absence of Spiral Trajectories in Slope Failures",
        "question": "Mass wasting or 'gravitative transfer' is NOT a result of :",
        "options": {
            "A": "vertical movements",
            "B": "lateral movements",
            "C": "diagonal movements",
            "D": "spiral movements"
        },
        "ans": "D",
        "ref": "Sharpe (1938); W.D. Thornbury (Principles of Geomorphology, pp. 88–95); Bloom (Geomorphology, Ch. 7)"
    },
    12: {
        "q": 12,
        "topic": "Mass Movement Classification: Lateral Spreading in Cohesive and Liquefiable Strata",
        "question": "Lateral movement of a series of blocks away from a centre is described as :",
        "options": {
            "A": "Sliding",
            "B": "Gliding",
            "C": "Spreading",
            "D": "Cambering"
        },
        "ans": "C",
        "ref": "Varnes (1978); Cruden & Varnes (1996, TRB Special Report 247); Thornbury (pp. 90–94)"
    },
    13: {
        "q": 13,
        "topic": "Slope Processes: Unconfined Downslope Flow of Saturated Regolith",
        "question": "The slow downslope movement of saturated rock debris which is NOT confined to definite channels is described as :",
        "options": {
            "A": "Debris slide",
            "B": "Mud flow",
            "C": "Solifluction",
            "D": "Soil creep"
        },
        "ans": "B",
        "ref": "Sayeed (Key p. 142); Sharpe (Landslides and Related Phenomena); Thornbury (pp. 89–93)"
    },
    14: {
        "q": 14,
        "topic": "Mass Wasting Mechanics: Distinction Between Downslope Flowage and Lateral Spreading",
        "question": "Which of the following does not result from the lateral movements of rock debris ?",
        "options": {
            "A": "Spreading",
            "B": "Solifluction",
            "C": "Cambering",
            "D": "Sackung"
        },
        "ans": "B",
        "ref": "Varnes (1978); Hutchinson (1988); Thornbury (Principles of Geomorphology, Ch. 4)"
    },
    15: {
        "q": 15,
        "topic": "Quaternary Paleogeomorphology: Periglacial Mass Wasting Epochs",
        "question": "Solifluction and Gelifluction were the important processes of mass wasting during :",
        "options": {
            "A": "Archaean",
            "B": "Proterozoic",
            "C": "Miocene",
            "D": "Pliocene"
        },
        "ans": "C",
        "ref": "Sayeed (Key p. 142); Flint (Glacial and Quaternary Geology); Thornbury (Ch. 14)"
    },
    16: {
        "q": 16,
        "topic": "Aeolian Abrasion: Genesis of Pedestal Rocks (Mushroom Rocks / Gours)",
        "question": "Mushroom-shaped structures having slender columns and wide tops resulting from the abrasive action of wind are described as :",
        "options": {
            "A": "Ventifacts",
            "B": "Brazil nuts",
            "C": "Pedestal rocks",
            "D": "Draas"
        },
        "ans": "C",
        "ref": "Arthur Holmes (Principles of Physical Geology, pp. 490–505); W.D. Thornbury (pp. 290–298); K.M. Bangar (p. 82)"
    },
    17: {
        "q": 17,
        "topic": "Aeolian Deflation: Genesis of Linear Deflation Furrows (Hohlwegs)",
        "question": "Which of the following features denote furrow deflation ?",
        "options": {
            "A": "Hohlwegs",
            "B": "Desert pavements",
            "C": "Blow outs",
            "D": "Playas"
        },
        "ans": "A",
        "ref": "Bagnold (The Physics of Blown Sand and Desert Dunes, Ch. 12); Thornbury (Principles of Geomorphology, p. 293)"
    },
    18: {
        "q": 18,
        "topic": "Desert Morphology: Serir / Reg (Stony Desert Lag Deposits vs. Erosional Forms)",
        "question": "Which of the following is NOT an erosional feature of wind ?",
        "options": {
            "A": "Zeugen",
            "B": "Yardang",
            "C": "Serir",
            "D": "Hohlweg"
        },
        "ans": "C",
        "ref": "Dr. Ausaf Sayeed (Explanatory Note *18, p. 143); Arthur Holmes (p. 492); Thornbury (p. 294)"
    },
    19: {
        "q": 19,
        "topic": "Comparative Planetary Geomorphology: Giant Martian Yardangs in Aeolian Regimes",
        "question": "The aeolian features that have been noticed in the planet Mars are :",
        "options": {
            "A": "Zeugens",
            "B": "Yardangs",
            "C": "Inselbergs",
            "D": "Barchans"
        },
        "ans": "B",
        "ref": "McCauley et al. (1977, J. Geophys. Res. 82, pp. 4031–4054); Greeley & Iversen (Wind as a Geological Process on Earth, Mars, Venus and Titan)"
    },
    20: {
        "q": 20,
        "topic": "Global Desert Typology: Classification of Sandy, Stony, Rocky, and Loess Terranes",
        "question": "Match the following desert types with their international regional terminology :\n(A) Sandy desert —— (1) Reg\n(B) Stony desert —— (2) Koum\n(C) Rocky desert —— (3) Adyry\n(D) Loess desert —— (4) Hamada",
        "options": {
            "A": "A-2, B-2, C-4, D-5",
            "B": "A-2, B-1, C-3, D-4",
            "C": "A-1, B-4, C-3, D-5",
            "D": "A-2, B-1, C-4, D-3"
        },
        "ans": "D",
        "ref": "W.D. Thornbury (Principles of Geomorphology, pp. 288–295); Arthur Holmes (pp. 488–496)"
    },
    21: {
        "q": 21,
        "topic": "Aeolian Sand Dunes: Seif Dunes and Sinuous Longitudinal Sand Ridges",
        "question": "Special types of longitudinal dunes which resemble railway embankments are described as :",
        "options": {
            "A": "Barchans",
            "B": "Parabolic dunes",
            "C": "Seifs",
            "D": "Dome dunes"
        },
        "ans": "C",
        "ref": "Bagnold (1941, The Physics of Blown Sand); Cooke, Warren & Goudie (Desert Geomorphology); Thornbury (p. 302)"
    },
    22: {
        "q": 22,
        "topic": "Dune Kinematics: Saltation Dynamics and Downwind Leeward Migration",
        "question": "The sand dunes migrate in the :",
        "options": {
            "A": "leeward direction",
            "B": "windward direction",
            "C": "both leeward and windward directions",
            "D": "none of the above"
        },
        "ans": "A",
        "ref": "Bagnold (Physics of Blown Sand, Ch. 13); Sam Boggs Jr. (p. 256); K.M. Bangar (p. 85)"
    },
    23: {
        "q": 23,
        "topic": "Sedimentology of Aeolian Dust: Granulometric Sorting of Loess",
        "question": "Loess is a non-stratified, well-sorted aeolian deposit composed of ——— grade fragments :",
        "options": {
            "A": "sand",
            "B": "silt",
            "C": "clay",
            "D": "pebble"
        },
        "ans": "B",
        "ref": "Pye (1987, Aeolian Dust and Dust Deposits); Sam Boggs Jr. (pp. 260–265); Thornbury (p. 306)"
    },
    24: {
        "q": 24,
        "topic": "Arid Landform Genesis: Inselbergs (Bornhardts) as Residual Steep-Sided Monoliths",
        "question": "Inselbergs characteristically consist of :",
        "options": {
            "A": "isolated pillar-like masses in desert regions",
            "B": "U-shaped troughs formed by winds",
            "C": "cup-shaped depressions formed by glacial erosion",
            "D": "sink-hole ponds formed by solution action in karst regions"
        },
        "ans": "A",
        "ref": "Dr. Ausaf Sayeed (Explanatory Note *119, p. 144); Arthur Holmes (p. 493); Thornbury (pp. 295–298)"
    },
    25: {
        "q": 25,
        "topic": "Arid & Semi-Arid Basin Morphology: Bolsons, Bajadas, Dreikanters, and Adobe",
        "question": "Match the following arid geomorphic features with their defining characteristics :\n(A) Bolson ———— (1) A series of coalescing alluvial fans on a piedmont slope\n(B) Bajada ———— (2) A basin more or less rimmed by mountains\n(C) Dreikanter — (4) Angular rocks with polished surfaces (ventifacts)\n(D) Adobe/Limon — (3) Non-stratified silt-grade deposit",
        "options": {
            "A": "A-1, B-2, C-3, D-4",
            "B": "A-2, B-1, C-4, D-3",
            "C": "A-1, B-2, C-4, D-3",
            "D": "A-2, B-1, C-3, D-4"
        },
        "ans": "B",
        "ref": "W.D. Thornbury (Principles of Geomorphology, pp. 296–308); Arthur Holmes (pp. 495–502)"
    },
    26: {
        "q": 26,
        "topic": "Fluvial Dissection of Horizontal Strata: Morphometry of Mesas and Buttes",
        "question": "Flat-topped hills or small mountains formed by stream action and capped by resistant strata are called :",
        "options": {
            "A": "Mesas",
            "B": "Buttes",
            "C": "Cuestas",
            "D": "Stream terraces"
        },
        "ans": "A",
        "ref": "Arthur Holmes (Principles of Physical Geology, pp. 450–462); Thornbury (p. 132); K.M. Bangar (p. 74)"
    },
    27: {
        "q": 27,
        "topic": "Structural Geomorphology of Homoclinal Strata: Cuestas vs. Hogbacks",
        "question": "An erosional ridge having a long, gentle slope on one side (dip slope) and an abrupt slope on the other (scarp) is known as :",
        "options": {
            "A": "Gloup",
            "B": "Groyne",
            "C": "Cuesta",
            "D": "Hogback"
        },
        "ans": "C",
        "ref": "W.D. Thornbury (Principles of Geomorphology, pp. 130–136); Marland P. Billings (Structural Geology); Bangar (p. 75)"
    },
    28: {
        "q": 28,
        "topic": "Genetic Drainage Classification: Obsequent Streams Flowing Counter to Initial Dip",
        "question": "Streams which flow in the opposite direction to the original consequent streams are described as :",
        "options": {
            "A": "Obsequent",
            "B": "Subsequent",
            "C": "Insequent",
            "D": "Resequent"
        },
        "ans": "A",
        "ref": "W.M. Davis (1899); W.D. Thornbury (pp. 115–122); Arthur Holmes (pp. 465–472)"
    },
    29: {
        "q": 29,
        "topic": "Sedimentology & Stratification: Deltaic Clinoform Architecture Reflected in Cross-Bedding",
        "question": "The deltaic structure (topset, foreset, bottomset architecture) is seen on a small-scale in :",
        "options": {
            "A": "Cross-bedding",
            "B": "Graded bedding",
            "C": "Convolute bedding",
            "D": "Ripple lamination"
        },
        "ans": "A",
        "ref": "Sam Boggs Jr. (Principles of Sedimentology and Stratigraphy, Ch. 4, pp. 88–95); Pettijohn (Sedimentary Rocks)"
    },
    30: {
        "q": 30,
        "topic": "Gilbert-Type Delta Architecture: Granulometry and Facies Distribution of Topset Beds",
        "question": "In a deltaic structure, the topset beds consist of :",
        "options": {
            "A": "fine material",
            "B": "coarse material",
            "C": "coarse and fine material",
            "D": "none of the above"
        },
        "ans": "C",
        "ref": "G.K. Gilbert (1885, The Topographic Features of Lake Shores, USGS 5th Ann. Rep.); Sam Boggs Jr. (pp. 295–305); Thornbury (p. 172)"
    }
}

print(f"Batch 1 compiled with {len(BATCH1_QS)} verified questions.")
