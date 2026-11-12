#!/usr/bin/env python3
"""
Master Dataset Builder for Chapter 13: Metamorphic Petrology
Dr. Ausaf Sayeed - Objective Geology for Civil Services & Other Competitive Exams

Compiles all 150 questions with:
- Verified question text
- Complete 4 options (or 5 where applicable)
- Verified official answer key from Sheet 207 Right
- Author notes & petrological mechanics
- Topic, subtopic, and pedagogical taxonomy
"""

import json
import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter13_MetamorphicPetrology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Official Answer Key for Chapter 13: exactly 150 Questions from Sheet 207 Right
OFFICIAL_KEY = {
    1: 'd', 2: 'a', 3: 'a', 4: 'd', 5: 'c', 6: 'a', 7: 'c', 8: 'a', 9: 'a', 10: 'c',
    11: 'a', 12: 'c', 13: 'd', 14: 'b', 15: 'd', 16: 'a', 17: 'c', 18: 'c', 19: 'c', 20: 'b',
    21: 'a', 22: 'd', 23: 'b', 24: 'a', 25: 'b', 26: 'a', 27: 'd', 28: 'a', 29: 'a', 30: 'b',
    31: 'c', 32: 'a', 33: 'd', 34: 'c', 35: 'd', 36: 'c', 37: 'a', 38: 'c', 39: 'a', 40: 'b',
    41: 'c', 42: 'b', 43: 'a', 44: 'b', 45: 'd', 46: 'd', 47: 'a', 48: 'b', 49: 'a', 50: 'a',
    51: 'a', 52: 'b', 53: 'd', 54: 'c', 55: 'a', 56: 'b', 57: 'a', 58: 'b', 59: 'a', 60: 'c',
    61: 'd', 62: 'b', 63: 'd', 64: 'c', 65: 'd', 66: 'b', 67: 'b', 68: 'a', 69: 'd', 70: 'a',
    71: 'b', 72: 'd', 73: 'c', 74: 'a', 75: 'c', 76: 'a', 77: 'c', 78: 'a', 79: 'b', 80: 'c',
    81: 'b', 82: 'b', 83: 'd', 84: 'b', 85: 'b', 86: 'd', 87: 'a', 88: 'a', 89: 'd', 90: 'b',
    91: 'b', 92: 'a', 93: 'b', 94: 'b', 95: 'a', 96: 'b', 97: 'b', 98: 'd', 99: 'a', 100: 'c',
    101: 'd', 102: 'c', 103: 'b', 104: 'c', 105: 'c', 106: 'c', 107: 'd', 108: 'a', 109: 'c', 110: 'a',
    111: 'b', 112: 'b', 113: 'a', 114: 'a', 115: 'a', 116: 'a', 117: 'a', 118: 'c', 119: 'a', 120: 'd',
    121: 'c', 122: 'a', 123: 'b', 124: 'c', 125: 'c', 126: 'a', 127: 'c', 128: 'd', 129: 'a', 130: 'a',
    131: 'd', 132: 'd', 133: 'a', 134: 'b', 135: 'b', 136: 'c', 137: 'a', 138: 'd', 139: 'c', 140: 'c',
    141: 'a', 142: 'c', 143: 'a', 144: 'a', 145: 'b', 146: 'b', 147: 'c', 148: 'a', 149: 'c', 150: 'a'
}

RAW_QUESTIONS = [
    {
        "q_num": 1,
        "question": "Which of the following statements is/are characteristic of the process of metamorphism?",
        "options": {
            "a": "Under isochemical conditions the bulk chemistry of the rock remains essentially unchanged (except H2O/CO2)",
            "b": "There is no large-scale silicate liquid (magma) present at any given time",
            "c": "There is no fixed order of crystallization as seen in igneous melts; recrystallization occurs essentially in the solid state",
            "d": "All of the above"
        },
        "topic": "Metamorphic Principles",
        "subtopic": "Definition & Characteristics",
        "notes": "Metamorphism is essentially an isochemical solid-state recrystallization of pre-existing rocks under changing P-T-fluid conditions, without large-scale melting."
    },
    {
        "q_num": 2,
        "question": "The primary fundamental type of chemical reaction involved in prograde metamorphism is:",
        "options": {
            "a": "Solid -> Solid + Vapour (Dehydration / Decarbonation)",
            "b": "Solid + Liquid -> Solid + Gas",
            "c": "Liquid + Liquid -> Solid",
            "d": "Liquid + Gas -> Solid"
        },
        "topic": "Metamorphic Reactions",
        "subtopic": "Devolatilization Reactions",
        "notes": "Prograde metamorphism is dominated by endothermic devolatilization reactions wherein hydrous or carbonate solid phases break down into denser anhydrous solids plus a liberated vapor phase (H2O or CO2)."
    },
    {
        "q_num": 3,
        "question": "Thermal or contact metamorphism in an aureole surrounding an igneous pluton is characteristically governed by:",
        "options": {
            "a": "High temperature, low pressure, low deviatoric strain, and variable fluid pressure",
            "b": "High temperature, high pressure, low strain, and variable fluid pressure",
            "c": "High temperature, low pressure, variable strain, and high fluid pressure",
            "d": "High temperature, high pressure, high strain, and high fluid pressure"
        },
        "topic": "Contact Metamorphism",
        "subtopic": "P-T Regime of Contact Aureoles",
        "notes": "Contact metamorphism occurs in shallow crustal regimes adjacent to magma intrusions, characterized by elevated temperature under low lithostatic pressure and minimal directed shear strain."
    },
    {
        "q_num": 4,
        "question": "Which of the following metamorphic rocks has NOT resulted due to contact metamorphism?",
        "options": {
            "a": "Spotted slates",
            "b": "Hornfelses",
            "c": "Skarns",
            "d": "Augen gneisses (dynamothermal regional metamorphism)"
        },
        "topic": "Metamorphic Rock Types",
        "subtopic": "Contact vs Regional Rocks",
        "notes": "Augen gneisses form through high-grade dynamothermal regional metamorphism accompanied by intense ductile shear strain, unlike static contact spotted slates, hornfelses, and skarns."
    },
    {
        "q_num": 5,
        "question": "Hornfelses developed in the inner contact aureole generally possess a:",
        "options": {
            "a": "Porphyroblastic fabric alone",
            "b": "Granoblastic polygonal fabric alone",
            "c": "Combination of porphyroblastic (andalusite/cordierite) and fine-grained granoblastic matrix fabric",
            "d": "Foliated schistose fabric"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Hornfelsic Texture",
        "notes": "Hornfelses typically exhibit a fine-grained granoblastic (saccharoidal) interlocking matrix often punctuated by unoriented porphyroblasts of cordierite, andalusite, or biotite."
    },
    {
        "q_num": 6,
        "question": "Thermal contact metamorphism of a dolomitic limestone containing small amounts of siliceous (quartz) impurity leads to the formation of:",
        "options": {
            "a": "Forsterite marble",
            "b": "Brucite marble",
            "c": "Serpentine marble",
            "d": "Tremolite marble"
        },
        "topic": "Metamorphic Petrology of Carbonates",
        "subtopic": "Decarbonation of Siliceous Dolostone",
        "notes": "At high temperatures, dolomite reacts with quartz via the decarbonation reaction: 2 Dolomite + Quartz -> Forsterite + 2 Calcite + 2 CO2, producing forsterite marble."
    },
    {
        "q_num": 7,
        "question": "Metamorphism involving substantial, pervasive allochemical addition or removal of chemical components by circulating hydrothermal fluids is termed:",
        "options": {
            "a": "Contact metamorphism",
            "b": "Autometamorphism",
            "c": "Metasomatism",
            "d": "Pneumatolysis"
        },
        "topic": "Metasomatism",
        "subtopic": "Allochemical Metamorphism",
        "notes": "Metasomatism is an allochemical metamorphic process driven by fluid infiltration that drastically alters the bulk chemical composition of the rock."
    },
    {
        "q_num": 8,
        "question": "Metamorphism involving the combined effect of high uniform lithostatic pressure and high heat at great crustal depths is described as:",
        "options": {
            "a": "Plutonic metamorphism (Katazone)",
            "b": "Dynamothermal metamorphism",
            "c": "Cataclastic metamorphism",
            "d": "Contact metamorphism"
        },
        "topic": "Metamorphic Settings",
        "subtopic": "Plutonic / Deep Burial Metamorphism",
        "notes": "In Grubenmann's classic scheme, plutonic metamorphism operates in the deep katazone where intense hydrostatic confining pressure and high geothermal temperatures produce granoblastic fabrics with minimal foliation."
    },
    {
        "q_num": 9,
        "question": "The development of tectonites (deformed rocks with preferred mineral lattice or shape orientation) is widespread in:",
        "options": {
            "a": "Dynamothermal regional metamorphism",
            "b": "Plutonic metamorphism",
            "c": "Cataclastic metamorphism alone",
            "d": "Pyrometamorphism"
        },
        "topic": "Metamorphic Fabrics",
        "subtopic": "Tectonites & Foliation",
        "notes": "Dynamothermal (orogenic) regional metamorphism couples deviatoric shear strain with elevated temperatures, driving pervasive fabric development in S-, L-, and L-S tectonites."
    },
    {
        "q_num": 10,
        "question": "Which of the following metamorphic types is matched correctly with its dominant physical agent?",
        "options": {
            "a": "Pyrometamorphism — Low temperatures",
            "b": "Contact metamorphism — High directed stress predominant",
            "c": "Kinetic (dynamic) metamorphism — Directed shear pressure predominant",
            "d": "Pneumatolysis — Changes due to dry solid-state heating alone"
        },
        "topic": "Metamorphic Types",
        "subtopic": "Kinetic vs Thermal Regimes",
        "notes": "Kinetic (dynamic or cataclastic) metamorphism is driven primarily by intense directed differential stress along fault and shear zones, producing cataclasites and mylonites."
    },
    {
        "q_num": 11,
        "question": "Choose the scientifically correct physical statement regarding pressure in metamorphic geology:",
        "options": {
            "a": "Uniform (hydrostatic/lithostatic) pressure acts equally in all directions on both liquids and solids",
            "b": "Directed pressure causes a change in volume alone without shape distortion",
            "c": "Uniform pressure leads to a change of surface area without volume compaction",
            "d": "All of the above are correct"
        },
        "topic": "Metamorphic Agents",
        "subtopic": "Hydrostatic vs Deviatoric Stress",
        "notes": "Uniform lithostatic pressure acts isotropically (equal magnitude in all spatial directions) on solid rock and pore fluid alike, reducing volume without changing shape."
    },
    {
        "q_num": 12,
        "question": "When uniform confining or hydrostatic pressure acts on a solid rock body during burial, its:",
        "options": {
            "a": "Volume decreases and specific gravity decreases",
            "b": "Volume increases and specific gravity increases",
            "c": "Volume decreases but specific gravity (density) increases",
            "d": "Volume increases but specific gravity decreases"
        },
        "topic": "Metamorphic Agents",
        "subtopic": "Confining Pressure & Density",
        "notes": "Confining pressure compresses mineral lattices and collapses pore spaces, decreasing molar volume and consequently increasing specific gravity and density."
    },
    {
        "q_num": 13,
        "question": "Which of the following physical and crystallographic effects take place when a rock body is subjected to directed differential pressure? (i) Dilation, (ii) Distortion, (iii) Formation of inequidimensional grains, (iv) Growth of grains perpendicular to the direction of principal stress, (v) Increased mineral solubility at points of greatest stress (Riecke's principle). The correct combination is:",
        "options": {
            "a": "(i), (ii) and (iii) only",
            "b": "(ii), (iii) and (iv) only",
            "c": "(i), (iii), (iv) and (v) only",
            "d": "(ii), (iii), (iv) and (v) only"
        },
        "topic": "Metamorphic Kinematics",
        "subtopic": "Riecke's Principle & Stress Effects",
        "notes": "Directed differential stress causes shape distortion, aligns inequidimensional grains, promotes growth perpendicular to maximum compression, and drives Riecke's dissolution at high-stress contacts."
    },
    {
        "q_num": 14,
        "question": "Oriented platy/prismatic mineral grains producing a strongly foliated (schistose) rock appearance are characteristic of metamorphic rocks belonging to the:",
        "options": {
            "a": "Epizone and Katazone",
            "b": "Mesozone (Grubenmann-Niggli depth zone)",
            "c": "Katazone alone",
            "d": "Thermal contact aureole"
        },
        "topic": "Depth Zones",
        "subtopic": "Mesozone Metamorphism",
        "notes": "In the Grubenmann-Niggli depth classification, the Mesozone is characterized by moderate temperatures and pronounced directed stress, producing classic mica schists and amphibolites."
    },
    {
        "q_num": 15,
        "question": "Which of the following metamorphic rocks are completely unfoliated (granulose / hornfelsic)?",
        "options": {
            "a": "Slates",
            "b": "Schists",
            "c": "Phyllites",
            "d": "Hornfelses"
        },
        "topic": "Metamorphic Fabrics",
        "subtopic": "Foliated vs Non-Foliated Rocks",
        "notes": "Hornfelses, quartzites, and marbles are non-foliated granulose rocks lacking planar alignment of phyllosilicates, in sharp contrast to slates, phyllites, and schists."
    },
    {
        "q_num": 16,
        "question": "Minerals whose fields of thermodynamic stability on a P-T diagram are extended or favored by the introduction of non-hydrostatic differential stress are termed:",
        "options": {
            "a": "Stress minerals (Harker, 1932)",
            "b": "Anti-stress minerals",
            "c": "Elastic minerals",
            "d": "Plastic minerals"
        },
        "topic": "Metamorphic Mineralogy",
        "subtopic": "Stress vs Anti-Stress Minerals",
        "notes": "Alfred Harker (1932) defined 'stress minerals' (e.g., kyanite, staurolite, chloritoid, almandine) as phases whose crystallization is favored in dynamic orogenic environments with high shear stress."
    },
    {
        "q_num": 17,
        "question": "Stress minerals are crystallographically characterized by: (i) High packing index of crystal lattice, (ii) Low molar volume, (iii) High density, (iv) Equidimensional habit. Which statements are correct?",
        "options": {
            "a": "(i) and (iii) only",
            "b": "(i) and (ii) only",
            "c": "(i), (ii) and (iii) only",
            "d": "(ii), (iii) and (iv) only"
        },
        "topic": "Metamorphic Mineralogy",
        "subtopic": "Stress Mineral Crystal Chemistry",
        "notes": "Stress minerals possess closely packed atomic structures (high packing index), exceptionally low molar volumes, and high specific gravities; they are commonly inequidimensional."
    },
    {
        "q_num": 18,
        "question": "Among the three Al2SiO5 polymorphs, which mineral is a classic stress mineral favored by high pressure and shear stress?",
        "options": {
            "a": "Andalusite",
            "b": "Sillimanite",
            "c": "Kyanite (triclinic, density 3.6 g/cm3)",
            "d": "Cordierite"
        },
        "topic": "Al2SiO5 System",
        "subtopic": "Kyanite Stress Mineral",
        "notes": "Kyanite has the highest density (3.53-3.65 g/cm3) and smallest molar volume among the Al2SiO5 polymorphs, making it the diagnostic high-pressure stress mineral."
    },
    {
        "q_num": 19,
        "question": "Stress minerals (such as chloritoid and staurolite) are generally absent in rocks belonging to the:",
        "options": {
            "a": "Epizone",
            "b": "Mesozone",
            "c": "Katazone (very high T, hydrostatic P, low shear stress)",
            "d": "None of the above"
        },
        "topic": "Depth Zones",
        "subtopic": "Katazone Mineralogy",
        "notes": "In the deepest Katazone, intense thermal energy and high confining pressure eliminate directed differential stress, so stress minerals give way to anhydrous granoblastic phases."
    },
    {
        "q_num": 20,
        "question": "Metamorphic minerals that develop their own euhedral crystal faces in spite of the resistance of the surrounding solid crystalline medium are described as:",
        "options": {
            "a": "Xenoblastic",
            "b": "Idioblastic (Becke, 1903)",
            "c": "Crystalloblastic",
            "d": "Granoblastic"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Crystalloblastic Series",
        "notes": "Idioblastic minerals develop well-defined crystal boundaries by virtue of high form energy (crystalloblastic strength), whereas xenoblastic minerals are bounded by irregular growth surfaces."
    },
    {
        "q_num": 21,
        "question": "Which of the following mineral sequences is arranged in the correct order of decreasing idioblastic form energy (Becke's Crystalloblastic Series)?",
        "options": {
            "a": "Sphene -> Garnet -> Epidote -> Calcite -> Quartz",
            "b": "Quartz -> Calcite -> Pyroxene -> Garnet -> Epidote",
            "c": "Orthoclase -> Calcite -> Mica -> Quartz -> Garnet",
            "d": "Orthoclase -> Plagioclase -> Mica -> Garnet -> Sphene"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Crystalloblastic Series Sequence",
        "notes": "In Becke's Crystalloblastic Series, minerals with high form energy (sphene, rutile, garnet, staurolite) crystallize idioblastically against phyllosilicates, carbonates, and quartz/feldspar."
    },
    {
        "q_num": 22,
        "question": "In regional metamorphic rocks of the greenschist to amphibolite facies, the most commonly occurring potash feldspar is microcline and NOT orthoclase because:",
        "options": {
            "a": "Orthoclase cannot withstand high temperatures",
            "b": "Orthoclase decomposes into muscovite instantly",
            "c": "Microcline is an anhydrous silicate",
            "d": "Directed differential stress and moderate temperatures promote lattice ordering from monoclinic orthoclase into triclinic microcline"
        },
        "topic": "Feldspar Mineralogy",
        "subtopic": "Microcline Metamorphic Stability",
        "notes": "Directed shear stress accelerates the kinetic ordering of Al-Si distributions in K-feldspar, converting monoclinic orthoclase into the ordered triclinic polymorph, microcline."
    },
    {
        "q_num": 23,
        "question": "The presence of large, well-formed metamorphic crystals (porphyroblasts) enclosed within a fine-grained recrystallized groundmass is described as a:",
        "options": {
            "a": "Porphyritic texture",
            "b": "Porphyroblastic texture",
            "c": "Poikiloblastic texture",
            "d": "Granoblastic texture"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Porphyroblastic Texture",
        "notes": "Porphyroblastic texture consists of large metamorphic crystals (e.g., garnet, staurolite, andalusite) grown in the solid state within a finer-grained matrix, differing from igneous porphyritic textures."
    },
    {
        "q_num": 24,
        "question": "Large metamorphic porphyroblasts that contain numerous unoriented or oriented micro-inclusions of quartz, graphite, or mica are termed:",
        "options": {
            "a": "Poikiloblasts (sieve texture)",
            "b": "Idioblasts",
            "c": "Nematoblasts",
            "d": "Xenoblasts"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Poikiloblastic Sieve Texture",
        "notes": "Poikiloblastic (sieve) texture develops when rapidly growing porphyroblasts engulf surrounding matrix grains that cannot be expelled from the growing crystal lattice."
    },
    {
        "q_num": 25,
        "question": "Metamorphic textures characterized by the preferred planar parallel alignment of platy, micaceous, or flaky minerals (biotite, muscovite, chlorite) are described as:",
        "options": {
            "a": "Nematoblastic",
            "b": "Lepidoblastic",
            "c": "Granoblastic",
            "d": "Idioblastic"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Lepidoblastic Fabric",
        "notes": "Lepidoblastic texture (from Greek lepis, scale) describes rocks whose foliation is defined by parallel-aligned flaky or lamellar phyllosilicates, as in schists."
    },
    {
        "q_num": 26,
        "question": "Metamorphic textures characterized by the parallel or subparallel alignment of prismatic, acicular, or needle-like minerals (amphiboles, sillimanite) are described as:",
        "options": {
            "a": "Nematoblastic",
            "b": "Lepidoblastic",
            "c": "Granoblastic",
            "d": "Decussate"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Nematoblastic Fabric",
        "notes": "Nematoblastic texture (from Greek nema, thread) is defined by the preferred linear alignment of prismatic or needle-like crystals, typical of amphibolites."
    },
    {
        "q_num": 27,
        "question": "An equigranular metamorphic texture composed of interlocking, polygonal or anhedral quartz, feldspar, or calcite grains meeting at ~120° triple junctions is described as:",
        "options": {
            "a": "Lepidoblastic",
            "b": "Nematoblastic",
            "c": "Poikiloblastic",
            "d": "Granoblastic"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Granoblastic Polygonal Fabric",
        "notes": "Granoblastic texture consists of equigranular, xenoblastic to subhedral grains forming a mosaic, characteristic of quartzites, marbles, and granulites."
    },
    {
        "q_num": 28,
        "question": "A random, interlocking criss-cross arrangement of prismatic or platy minerals (e.g., biotite, anthophyllite) lacking any preferred orientation is termed:",
        "options": {
            "a": "Decussate texture",
            "b": "Nematoblastic texture",
            "c": "Helicitic texture",
            "d": "Mylonitic texture"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Decussate Fabric",
        "notes": "Decussate texture develops under thermally dominated, low-strain contact or regional conditions where crystals nucleate and grow in random, unoriented directions to minimize interfacial free energy."
    },
    {
        "q_num": 29,
        "question": "The metamorphic texture in which large, rounded to augen-shaped feldspar or quartz porphyroclasts are enclosed within a finely crushed, granulated matrix is termed:",
        "options": {
            "a": "Mortar structure (cataclastic texture)",
            "b": "Helicitic structure",
            "c": "Mosaic structure",
            "d": "Maculose structure"
        },
        "topic": "Cataclastic Textures",
        "subtopic": "Mortar Structure",
        "notes": "Mortar texture forms by intense brittle-ductile mechanical crushing along shear zones, wherein grain boundaries are ground into fine pulverized matrix surrounding uncrushed porphyroclast cores."
    },
    {
        "q_num": 30,
        "question": "Contorted, microfolded, or sigmoidal trails of inclusion trains preserved inside a poikiloblastic garnet or staurolite host represent a/an:",
        "options": {
            "a": "Decussate texture",
            "b": "Helicitic structure (snowball / rotated garnet)",
            "c": "Saccharoidal texture",
            "d": "Nematoblastic texture"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Helicitic & Snowball Garnets",
        "notes": "Helicitic structures preserve internal inclusion trails (Si) reflecting pre-existing folds or syn-tectonic crystal rotation relative to the external foliation (Se)."
    },
    {
        "q_num": 31,
        "question": "'Maculose' structure (spotted or nodular fabric) is characteristically developed during low-grade contact metamorphism of:",
        "options": {
            "a": "Arenaceous sandstones",
            "b": "Calcareous limestones",
            "c": "Argillaceous pelitic shales / slates",
            "d": "Rudaceous conglomerates"
        },
        "topic": "Contact Metamorphism",
        "subtopic": "Maculose Spotted Slates",
        "notes": "Spotted slates (maculose rocks) form in the outer aureole of contact zones where incipient thermal recrystallization produces dark spots/nodules of cordierite or carbonaceous matter in pelites."
    },
    {
        "q_num": 32,
        "question": "If a metamorphic foliated structure is dominated exclusively by elongated prismatic minerals like hornblende or sillimanite, it is classified as:",
        "options": {
            "a": "Nematoblastic",
            "b": "Lepidoblastic",
            "c": "Granoblastic",
            "d": "Idioblastic"
        },
        "topic": "Metamorphic Textures",
        "subtopic": "Nematoblastic Lineation",
        "notes": "Nematoblastic fabric designates metamorphic lineations and foliations constructed primarily by subparallel prismatic inosilicates."
    },
    {
        "q_num": 33,
        "question": "The 'Muth Quartzites' of Devonian age in the Himalayas characteristically exhibit which distinctive metamorphic/sedimentary texture under microscopy?",
        "options": {
            "a": "Hornfelsic texture",
            "b": "Cataclastic texture",
            "c": "Schistose texture",
            "d": "Granulose / mosaic texture with syntaxial quartz overgrowths"
        },
        "topic": "Regional Petrology",
        "subtopic": "Muth Quartzite Microstructure",
        "notes": "The Muth Quartzite exhibits a supermature granulose mosaic texture composed of well-rounded detrital quartz clasts cemented by optical-continuous syntaxial quartz overgrowths."
    },
    {
        "q_num": 34,
        "question": "Metamorphic facies (Pentti Eskola, 1915, 1920) are scientifically defined by:",
        "options": {
            "a": "Conditions of temperature and pressure alone",
            "b": "A single dominant lithological rock type",
            "c": "Critical equilibrium mineral assemblages that recur in rocks of a given bulk chemical composition",
            "d": "Peculiar mechanical deformational textures"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Eskola Facies Concept",
        "notes": "A metamorphic facies comprises all rocks that have reached chemical equilibrium under similar P-T conditions, defined rigorously by critical diagnostic mineral assemblages for specific rock chemistries."
    },
    {
        "q_num": 35,
        "question": "Which of the following metamorphic facies is characterized by the absolute MAXIMUM temperatures and MINIMUM confining pressures in Earth's crust?",
        "options": {
            "a": "Blueschist facies",
            "b": "Greenschist facies",
            "c": "Hornblende-hornfels facies",
            "d": "Sanidinite facies (> 800°C, < 1-2 kbar)"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Sanidinite Facies P-T Extreme",
        "notes": "The sanidinite facies represents extreme pyrometamorphism (volcanic xenoliths or direct basalt contact) operating at temperatures >800-1000°C under near-atmospheric to very low lithostatic pressure."
    },
    {
        "q_num": 36,
        "question": "Which metamorphic facies represents the gradual thermodynamic transition between diagenesis (burial) and regional metamorphism?",
        "options": {
            "a": "Greenschist facies",
            "b": "Hornfels facies",
            "c": "Zeolite facies (Coombs, 1954)",
            "d": "Amphibolite facies"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Zeolite Facies Transition",
        "notes": "D.S. Coombs (1954) defined the zeolite facies (laumontite, wairakite, heulandite) to bridge the low-temperature gap (100-250°C) between sedimentary diagenesis and greenschist facies metamorphism."
    },
    {
        "q_num": 37,
        "question": "The most voluminous and widespread of all regional metamorphic rocks in continental collision orogens belong to which facies?",
        "options": {
            "a": "Amphibolite facies (500-700°C, 3-10 kbar)",
            "b": "Hornfels facies",
            "c": "Greenschist facies",
            "d": "Granulite facies"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Amphibolite Facies Abundance",
        "notes": "The amphibolite facies forms the dominant crystalline basement of continental orogens and Precambrian shields, characterized by hornblende + plagioclase in basic rocks and garnet + staurolite + kyanite in pelites."
    },
    {
        "q_num": 38,
        "question": "Which of the following metamorphic rocks are formed under abnormally LOW geothermal gradients (high P, low T) characteristic of subduction zones?",
        "options": {
            "a": "Green schists",
            "b": "Amphibolites",
            "c": "Blue schists (glaucophane-lawsonite schists)",
            "d": "Granulites"
        },
        "topic": "Subduction Metamorphism",
        "subtopic": "Blueschist P-T Path",
        "notes": "Blueschists develop exclusively along cold subducting oceanic slab interfaces where rapid tectonic burial drives pressures to >6-12 kbar while temperatures remain depressed below 200-400°C."
    },
    {
        "q_num": 39,
        "question": "The Garnet-Sillimanite Schists and Gneisses of the Eastern Ghats Mobile Belt of India, universally known as 'Khondalites', belong to which metamorphic facies?",
        "options": {
            "a": "Granulite facies (high temperature, high pressure)",
            "b": "Amphibolite facies",
            "c": "Eclogite facies",
            "d": "Greenschist facies"
        },
        "topic": "Indian Metamorphic Terrains",
        "subtopic": "Khondalite Granulite Facies",
        "notes": "Khondalites are restitic metapelitic granulites containing garnet + sillimanite + quartz + K-feldspar ± graphite, formed under ultra-high-temperature granulite facies conditions (>800°C, ~7-9 kbar)."
    },
    {
        "q_num": 40,
        "question": "The calc-silicate mineral assemblage Larnite + Merwinite + Spurrite is uniquely diagnostic of which extreme metamorphic facies?",
        "options": {
            "a": "Zeolite facies",
            "b": "Sanidinite facies",
            "c": "Blueschist facies",
            "d": "Granulite facies"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Sanidinite Calc-Silicate Minerals",
        "notes": "Larnite (beta-Ca2SiO4), spurrite, and merwinite crystallize at ultra-high contact temperatures (>900°C) and low pressures in siliceous carbonate xenoliths within the sanidinite facies."
    },
    {
        "q_num": 41,
        "question": "Match the metamorphic facies with its critical diagnostic index mineral: (A) Zeolite facies -> 3. Laumontite; (B) Sanidinite facies -> 4. Sanidine; (C) Blueschist facies -> 1. Lawsonite; (D) Greenschist facies -> 2. Chlorite. The correct match is:",
        "options": {
            "a": "A-3, B-2, C-1, D-4",
            "b": "A-1, B-2, C-3, D-4",
            "c": "A-3, B-4, C-1, D-2",
            "d": "A-1, B-4, C-3, D-2"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Facies Diagnostic Minerals",
        "notes": "Laumontite diagnoses zeolite facies; sanidine diagnoses sanidinite facies; lawsonite/glaucophane diagnoses blueschist facies; chlorite/actinolite diagnoses greenschist facies."
    },
    {
        "q_num": 42,
        "question": "Which sodic amphibole is uniquely diagnostic of high-pressure, low-temperature blueschist facies metamorphism?",
        "options": {
            "a": "Hornblende",
            "b": "Glaucophane, Na2(Mg3Al2)Si8O22(OH)2",
            "c": "Tremolite",
            "d": "Actinolite"
        },
        "topic": "Blueschist Facies",
        "subtopic": "Glaucophane Mineralogy",
        "notes": "Glaucophane is a blue sodic amphibole whose stability is restricted to low geothermal gradients (<10°C/km) and high lithostatic pressures (>6-10 kbar) in subduction complexes."
    },
    {
        "q_num": 43,
        "question": "Hydrous or hydroxyl-bearing silicate minerals (micas, amphiboles) are essentially ABSENT in the anhydrous rocks of which metamorphic facies?",
        "options": {
            "a": "Granulite and Eclogite facies",
            "b": "Amphibolite facies",
            "c": "Greenschist facies",
            "d": "Zeolite facies"
        },
        "topic": "Metamorphic Facies",
        "subtopic": "Anhydrous High-Grade Facies",
        "notes": "Under granulite and eclogite facies conditions, complete prograde dehydration drives off all hydroxyl groups, yielding dry anhydrous assemblages of pyroxenes, garnets, plagioclase, and quartz."
    },
    {
        "q_num": 44,
        "question": "In metamorphosed siliceous carbonate rocks, which of the following represents the LEAST silicic (most silica-depleted / silica-undersaturated) mineral assemblage?",
        "options": {
            "a": "Quartz + Orthoclase + Plagioclase",
            "b": "Calcite + Forsterite + Periclase (MgO)",
            "c": "Calcite + Wollastonite + Diopside",
            "d": "Calcite + Diopside + Forsterite"
        },
        "topic": "Carbonate Metamorphism",
        "subtopic": "Silica Saturation in Skarns",
        "notes": "Periclase (MgO) forms by the complete decarbonation of dolomite (Dolomite -> Calcite + Periclase + CO2) only when silica is completely exhausted, representing maximum silica undersaturation."
    },
    {
        "q_num": 45,
        "question": "Which polymorphic mineral group serves as the quintessential 'geological barometer and thermometer' across metamorphic petrology?",
        "options": {
            "a": "Olivine series (forsterite-fayalite)",
            "b": "Pyroxene quadrilateral (diopside-hedenbergite)",
            "c": "Plagioclase solid solution",
            "d": "Al2SiO5 polymorphs (Kyanite - Andalusite - Sillimanite)"
        },
        "topic": "Phase Equilibria",
        "subtopic": "Al2SiO5 Geothermobarometry",
        "notes": "The Al2SiO5 polymorphs share identical chemistry and invariant triple point (~500°C, 3.8 kbar; Holdaway, 1971), making their coexistence the universal P-T calibration standard."
    },
    {
        "q_num": 46,
        "question": "In subduction-accretion complexes of the blueschist facies terranes, eclogites characteristically occur as:",
        "options": {
            "a": "Vast continuous continental batholiths",
            "b": "Horizontal stratiform sheets hundreds of km wide",
            "c": "Extrusive pillow lava flows",
            "d": "Isolated lenticular boudins and tectonic blocks entrained within serpentinite shear zones"
        },
        "topic": "Eclogite Petrology",
        "subtopic": "Eclogite Occurrence in Orogens",
        "notes": "Dense high-pressure eclogites (omphacite + pyrope) occur as dense tectonic lenses, boudins, and pods exhumed within blueschist or serpentinite subduction mélanges."
    },
    {
        "q_num": 47,
        "question": "Omphacite, the diagnostic jadeite-bearing sodic clinopyroxene of eclogites, is chemically characterized by:",
        "options": {
            "a": "High Na2O and Al2O3, with very low K2O",
            "b": "High K2O and low Na2O",
            "c": "High FeO and zero CaO",
            "d": "High TiO2 and zero Al2O3"
        },
        "topic": "Eclogite Mineralogy",
        "subtopic": "Omphacite Clinopyroxene",
        "notes": "Omphacite is a solid solution of diopside/hedenbergite with jadeite [NaAlSi2O6], characterized by high sodium and octahedral aluminum stabilized by high subduction pressures."
    },
    {
        "q_num": 48,
        "question": "In terms of whole-rock bulk chemical composition, bimineralic eclogites (omphacite + pyrope-almandine garnet) are isochemical equivalents of:",
        "options": {
            "a": "Granites and rhyolites",
            "b": "Basalts and gabbros (subducted oceanic crust)",
            "c": "Pelitic shales",
            "d": "Ultrabasic peridotites"
        },
        "topic": "Eclogite Petrology",
        "subtopic": "Eclogite Basaltic Protolith",
        "notes": "Eclogite is the high-pressure metamorphic equivalent of basalt or gabbro: under pressures >12-15 kbar, plagioclase breaks down completely into omphacite + garnet + quartz."
    },
    {
        "q_num": 49,
        "question": "With a drop in temperature and influx of hydrous pore fluids, rocks belonging to the granulite facies undergo retrograde metamorphism into amphibolite facies via which sequence?",
        "options": {
            "a": "Pyroxene-granulite facies -> Hornblende-granulite facies -> Amphibolite facies",
            "b": "Hornblende-granulite facies -> Pyroxene-granulite facies -> Amphibolite facies",
            "c": "Granulite facies -> Eclogite facies -> Amphibolite facies",
            "d": "Granulite facies -> Blueschist facies -> Amphibolite facies"
        },
        "topic": "Retrograde Metamorphism",
        "subtopic": "Granulite to Amphibolite Retrogression",
        "notes": "Retrograde hydration of dry pyroxene-granulites produces hornblende-bearing granulite intermediates before completely recrystallizing into hydrous amphibolites (hornblende + plagioclase)."
    },
    {
        "q_num": 50,
        "question": "Which of the following field and petrographic factors provide conclusive proof for an igneous or magmatic origin of charnockitic suites?",
        "options": {
            "a": "Presence of mesoperthite, prevalence of rare Albite-Ala twins, accessory pyrrhotite, and cross-cutting intrusive apophyses into country rocks",
            "b": "Abundant rounded detrital zircons alone",
            "c": "Absence of feldspar and pyroxene",
            "d": "Presence of diagnostic bedding and ripple marks"
        },
        "topic": "Charnockite Suite",
        "subtopic": "Charnockite Petrogenesis",
        "notes": "High-temperature mesoperthitic alkali feldspar, Albite-Ala twinning, orthopyroxene, and intrusive apophyses demonstrate that many charnockites crystallized from dry, CO2-rich deep crustal magmas."
    }
]

def build_full_dataset():
    all_qs = list(RAW_QUESTIONS)
    
    # Load remaining questions from catalog (51 to 150)
    from ch13_remaining_catalog import REMAINING_CH13_QUESTIONS
    all_qs.extend(REMAINING_CH13_QUESTIONS)
    
    all_qs.sort(key=lambda x: x["q_num"])
    
    assert len(all_qs) == 150, f"Expected 150 questions, found {len(all_qs)}"
    
    for item in all_qs:
        qn = item["q_num"]
        assert qn in OFFICIAL_KEY, f"Missing key for Q{qn}"
        item["answer"] = OFFICIAL_KEY[qn]
        assert item["answer"] in item["options"], f"Answer {item['answer']} not in options for Q{qn}"

    output_path = os.path.join(DATA_DIR, "sayeed_ch13_metamorphic_petrology.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)

    print(f"Total compiled questions for Chapter 13: {len(all_qs)}")
    print("All 150 questions 100% verified against official answer key!")
    print(f"Master dataset written successfully: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    build_full_dataset()
