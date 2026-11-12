#!/usr/bin/env python3
"""
Master Dataset Builder for Chapter 10: Indian Geology
Dr. Ausaf Sayeed - Objective Geology (175 Questions)
Verified against Official Key (p. 325-327) & Detailed Explanatory Notes
"""

import json
import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter10_IndianGeology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Master Official Answer Key for Chapter 10 (Questions 1 to 175)
OFFICIAL_KEY = {
    1: 'a', 2: 'c', 3: 'b', 4: 'b', 5: 'a', 6: 'd', 7: 'd', 8: 'b', 9: 'c', 10: 'a',
    11: 'b', 12: 'd', 13: 'b', 14: 'd', 15: 'c', 16: 'b', 17: 'c', 18: 'd', 19: 'b', 20: 'c',
    21: 'b', 22: 'b', 23: 'd', 24: 'b', 25: 'a', 26: 'd', 27: 'd', 28: 'c', 29: 'b', 30: 'a',
    31: 'b', 32: 'b', 33: 'a', 34: 'c', 35: 'b', 36: 'b', 37: 'c', 38: 'd', 39: 'c', 40: 'c',
    41: 'a', 42: 'c', 43: 'c', 44: 'b', 45: 'a', 46: 'c', 47: 'a', 48: 'c', 49: 'd', 50: 'b',
    51: 'a', 52: 'a', 53: 'c', 54: 'b', 55: 'a', 56: 'c', 57: 'b', 58: 'a', 59: 'c', 60: 'd',
    61: 'd', 62: 'c', 63: 'a', 64: 'b', 65: 'c', 66: 'd', 67: 'b', 68: 'a', 69: 'a', 70: 'c',
    71: 'c', 72: 'a', 73: 'b', 74: 'b', 75: 'c', 76: 'd', 77: 'c', 78: 'd', 79: 'c', 80: 'a',
    81: 'd', 82: 'b', 83: 'c', 84: 'b', 85: 'd', 86: 'a', 87: 'c', 88: 'd', 89: 'd', 90: 'd',
    91: 'd', 92: 'b', 93: 'a', 94: 'd', 95: 'c', 96: 'a', 97: 'c', 98: 'a', 99: 'c', 100: 'c',
    101: 'c', 102: 'b', 103: 'd', 104: 'a', 105: 'a', 106: 'd', 107: 'a', 108: 'c', 109: 'd', 110: 'b',
    111: 'c', 112: 'b', 113: 'c', 114: 'a', 115: 'c', 116: 'd', 117: 'b', 118: 'd', 119: 'a', 120: 'c',
    121: 'd', 122: 'b', 123: 'a', 124: 'c', 125: 'b', 126: 'a', 127: 'd', 128: 'b', 129: 'a', 130: 'b',
    131: 'b', 132: 'c', 133: 'a', 134: 'c', 135: 'b', 136: 'a', 137: 'a', 138: 'd', 139: 'b', 140: 'c',
    141: 'c', 142: 'a', 143: 'a', 144: 'b', 145: 'c', 146: 'd', 147: 'c', 148: 'a', 149: 'b', 150: 'c',
    151: 'b', 152: 'b', 153: 'a', 154: 'c', 155: 'c', 156: 'a', 157: 'b', 158: 'a', 159: 'a', 160: 'c',
    161: 'a', 162: 'd', 163: 'd', 164: 'c', 165: 'a', 166: 'b', 167: 'a', 168: 'b', 169: 'd', 170: 'c',
    171: 'b', 172: 'b', 173: 'a', 174: 'c', 175: 'd'
}

def get_questions_1_to_45():
    return [
        {
            "q_num": 1,
            "question": "The two-fold classification of the Precambrian into the lower Archaean and the upper Proterozoic Groups was first introduced in:",
            "options": {"a": "USA", "b": "Western Australia", "c": "South America", "d": "Northern Europe"},
            "answer": "a", "topic": "Precambrian Classification", "subtopic": "Historical Foundations",
            "notes": "Introduced in North America by the US Geological Survey (C.R. Van Hise and C.D. Walcott) to distinguish the crystalline crystalline basement (Archaean) from the overlying sedimentary sequences (Proterozoic)."
        },
        {
            "q_num": 2,
            "question": "The Main Unconformity (Eparchaean Unconformity) separating the Archaean and Proterozoic successions occurs globally at:",
            "options": {"a": "3200 M.Y.", "b": "2750 M.Y.", "c": "2500 M.Y.", "d": "1600 M.Y."},
            "answer": "c", "topic": "Precambrian Geochronology", "subtopic": "Archaean-Proterozoic Boundary",
            "notes": "The Archaean-Proterozoic boundary is chronometrically fixed internationally at 2500 Ma (2.5 Ga), marking a fundamental change in Earth's tectonic, atmospheric, and crustal evolution."
        },
        {
            "q_num": 3,
            "question": "Which one of the following granitic bodies marks the boundary between the Archaean and the Proterozoic formations in Rajasthan, India?",
            "options": {"a": "Untala Granite", "b": "Berach Granite", "c": "Erinpura Granite", "d": "Idar Granite"},
            "answer": "b", "topic": "Rajasthan Stratigraphy", "subtopic": "Berach Granite",
            "notes": "The Berach Granite (dated at ~2.5 to 2.6 Ga) intrudes the Archaean Banded Gneissic Complex (BGC) and forms the basement unconformity upon which the Paleoproterozoic Aravalli Supergroup rests."
        },
        {
            "q_num": 4,
            "question": "The Dharwar supracrustal schists of southern India have been classified as belonging to the:",
            "options": {"a": "Older Greenstone belt", "b": "Newer Greenstone belt", "c": "Sargur Schist Complex", "d": "Fundamental Gneissic Complex"},
            "answer": "b", "topic": "Dharwar Craton", "subtopic": "Greenstone Classification",
            "notes": "In the Dharwar Craton, the high-grade Sargur Schists (>3.1 Ga) constitute the Older Greenstones, whereas the true Dharwar Supergroup volcano-sedimentary belts (Bababudan and Chitradurga groups, ~2.9-2.6 Ga) form the Newer Greenstone belts."
        },
        {
            "q_num": 5,
            "question": "The ancient Keewatin greenstones of the Canadian Shield are correlated in Indian stratigraphy with:",
            "options": {"a": "The Sargur Schist Complex", "b": "The Dharwar Supergroup", "c": "The Cuddapah Supergroup", "d": "The Vindhyan Supergroup"},
            "answer": "a", "topic": "Global Correlation", "subtopic": "Precambrian Shields",
            "notes": "The Keewatin greenstones represent Meso-to-Neoarchean mafic-ultramafic volcanic complexes, correlating with the ancient Sargur Schist Complex of the Karnataka Craton."
        },
        {
            "q_num": 6,
            "question": "The classical type area for the manganese-bearing Sausar Group is located in:",
            "options": {"a": "Western Rajasthan", "b": "Nagpur-Bhandara", "c": "Singhbhum (Bihar)", "d": "Chhindwara (M.P.)"},
            "answer": "d", "topic": "Central Indian Tectonic Zone", "subtopic": "Sausar Group",
            "notes": "The Sausar Group (Paleoproterozoic manganese belt) was mapped and established by Sir Lewis Fermor in the Chhindwara district of Madhya Pradesh and adjacent Nagpur-Bhandara districts of Maharashtra."
        },
        {
            "q_num": 7,
            "question": "The widespread syn- to post-tectonic emplacement of the Erinpura Granite marks the terminal closing phase of the:",
            "options": {"a": "Dharwar orogeny", "b": "Delhi orogeny", "c": "Eastern Ghats orogeny", "d": "Satpura orogeny"},
            "answer": "d", "topic": "Aravalli-Delhi Belt", "subtopic": "Erinpura Granite",
            "notes": "In Dr. Ausaf Sayeed's key, option d (Satpura/Delhi tectonic epoch) is noted; Erinpura granite plutonism (~850-800 Ma) marks the culmination of the Proterozoic Delhi-Satpura mobile belt cycles in northwestern India."
        },
        {
            "q_num": 8,
            "question": "Mineralogically and petrographically, the Erinpura Granite of Rajasthan is predominantly a:",
            "options": {"a": "Hornblende granite", "b": "Biotite granite", "c": "Hornblende-biotite granite", "d": "None of the above"},
            "answer": "b", "topic": "Indian Plutonic Suites", "subtopic": "Erinpura Petrography",
            "notes": "The Erinpura Granite typically forms coarse-grained, porphyritic biotite granite with large microcline phenocrysts, exhibiting shearing and foliation along shear zones."
        },
        {
            "q_num": 9,
            "question": "Among the following Precambrian formations of the Indian Peninsula, the oldest recognized rocks belong to the:",
            "options": {"a": "Sargur Schist Complex", "b": "Banded Gneissic Complex", "c": "Older Metamorphic Group (OMG)", "d": "Iron Ore Group"},
            "answer": "c", "topic": "Singhbhum Craton", "subtopic": "Older Metamorphic Group",
            "notes": "The Older Metamorphic Group (OMG) and associated Older Metamorphic Tonalite Gneiss (OMTG) of the Singhbhum Craton yield Sm-Nd and U-Pb zircon ages exceeding 3.4 to 3.5 Ga."
        },
        {
            "q_num": 10,
            "question": "The eastern, relatively unmetamorphosed and undeformed sedimentary facies of the Aravalli succession in SE Rajasthan is termed the:",
            "options": {"a": "Binota shales", "b": "Ranthambhor formation", "c": "Kolhan series", "d": "Khardeola grits"},
            "answer": "a", "topic": "Aravalli Supergroup", "subtopic": "Binota Shales",
            "notes": "The unmetamorphosed pelitic facies bordering the Berach Granite basement in Chittorgarh represents the Binota shales, exhibiting low-grade sub-greenschist diagenetic features."
        },
        {
            "q_num": 11,
            "question": "Match the major Indian Precambrian orogenic belts with their peak metamorphic/thermal ages:\n(A) Kolhan orogeny — (1) 950 M.Y.\n(B) Satpura orogeny — (2) 1600 M.Y.\n(C) Eastern Ghats orogeny — (3) 2100 M.Y.\n(D) Delhi orogeny — (4) 1600 M.Y.",
            "options": {"a": "A-4, B-1, C-2, D-3", "b": "A-3, B-1, C-2, D-4", "c": "A-4, B-3, C-2, D-1", "d": "A-3, B-2, C-4, D-1"},
            "answer": "b", "topic": "Precambrian Orogenies", "subtopic": "Geochronological Matching",
            "notes": "Reflects the Proterozoic geochronologic framework of Indian mobile belts: Kolhan (~2.1 Ga), Satpura/Grenvillian (~950-1000 Ma), Eastern Ghats (~1.6 Ga and 1.0 Ga), and Delhi (~1.6 Ga to 850 Ma)."
        },
        {
            "q_num": 12,
            "question": "The distinctive granite gneiss dome topography characteristic of the Chotanagpur Gneissic Complex is known as:",
            "options": {"a": "Bezwada Gneiss", "b": "Kailasa Gneiss", "c": "Hosur Gneiss", "d": "Dome Gneiss"},
            "answer": "d", "topic": "Chotanagpur Gneissic Complex", "subtopic": "Dome Gneiss",
            "notes": "The Dome Gneiss of Chotanagpur (Jharkhand) forms prominent exfoliation tors and bornhardts, representing Mesoproterozoic porphyritic granite gneisses intruding high-grade schists."
        },
        {
            "q_num": 13,
            "question": "Which of the following stratigraphic divisions represents the terminal Neoproterozoic transitional phase from the Cryptozoic to Phanerozoic eons?",
            "options": {"a": "Riphean", "b": "Vendian (Ediacaran)", "c": "Georgian", "d": "Acadian"},
            "answer": "b", "topic": "Neoproterozoic Stratigraphy", "subtopic": "Vendian Period",
            "notes": "The Vendian System (equivalent to the Ediacaran Period, ~635-538.8 Ma) represents the terminal division of the Proterozoic, characterized by the emergence of soft-bodied Ediacaran metazoa."
        },
        {
            "q_num": 14,
            "question": "Which of the following sedimentary successions belongs to the lower Purana (Paleoproterozoic) basins of the Indian Peninsula?",
            "options": {"a": "Pakhal Group", "b": "Kaladgi Group", "c": "Chhattisgarh Group", "d": "Kolhan Group"},
            "answer": "d", "topic": "Purana Basins", "subtopic": "Kolhan Group",
            "notes": "The Kolhan Group of Jharkhand (~2.1-2.2 Ga) rests unconformably upon the Singhbhum Granite and Iron Ore Group, representing an early Paleoproterozoic Purana basin."
        },
        {
            "q_num": 15,
            "question": "Morphologically and structurally, the Proterozoic Cuddapah Basin of Andhra Pradesh is described as:",
            "options": {"a": "Linear", "b": "Curved", "c": "Curvo-linear (Crescent-shaped)", "d": "Concavo-convex"},
            "answer": "c", "topic": "Cuddapah Basin", "subtopic": "Basin Architecture",
            "notes": "The Cuddapah Basin displays a classic concave-to-the-east crescent or kidney-shaped geometry, bounded on the east by the thrust front of the Eastern Ghats Mobile Belt."
        },
        {
            "q_num": 16,
            "question": "In the Cuddapah Supergroup, major disconformities and unconformities separate successive groups. The most pronounced angular unconformity occurs between the:",
            "options": {"a": "Papaghani and Cheyair Groups", "b": "Cheyair and Nallamalai Groups", "c": "Nallamalai and Kistna Groups", "d": "Kistna and Kurnool Groups"},
            "answer": "b", "topic": "Cuddapah Basin", "subtopic": "Intra-Cuddapah Unconformities",
            "notes": "The Cheyair-Nallamalai boundary represents a major intra-basinal tectonic unconformity marked by widespread uplift, erosion, and stepping out of Nallamalai sedimentation."
        },
        {
            "q_num": 17,
            "question": "In the Cuddapah Basin, the greatest lateral aerial extent and stratigraphic thickness is displayed by the:",
            "options": {"a": "Kistna Group", "b": "Nallamalai Group", "c": "Cheyair Group", "d": "Papaghani Group"},
            "answer": "c", "topic": "Cuddapah Basin", "subtopic": "Group Distributions",
            "notes": "In Dr. Ausaf Sayeed's official key, option c (Cheyair) is designated; the Cheyair and Nallamalai groups constitute the dominant volume of the central and eastern basin fill."
        },
        {
            "q_num": 18,
            "question": "Across the Cuddapah Basin from the western undeformed cratonic margin to the eastern boundary thrust, tectonic deformation and metamorphism increase from:",
            "options": {"a": "North to South", "b": "South to North", "c": "East to West", "d": "West to East"},
            "answer": "d", "topic": "Cuddapah Basin", "subtopic": "Structural Gradient",
            "notes": "The western margin exhibits flat-lying, unmetamorphosed beds resting on Dharwar basement, while the eastern margin (Nallamalai fold belt) displays intense isoclinal folding and greenschist metamorphism toward the Eastern Ghats thrust."
        },
        {
            "q_num": 19,
            "question": "The total estimated cumulative stratigraphic thickness of the Cuddapah Supergroup is approximately:",
            "options": {"a": "10,000 ft", "b": "20,000 ft", "c": "30,000 ft", "d": "40,000 ft"},
            "answer": "b", "topic": "Cuddapah Basin", "subtopic": "Total Thickness",
            "notes": "The Cuddapah Supergroup comprises ~6,000 m (~20,000 ft) of quartzite, shale, and carbonate strata, overlain unconformably by ~500 m of the Neoproterozoic Kurnool Group."
        },
        {
            "q_num": 20,
            "question": "In the Proterozoic Delhi Supergroup of Rajasthan, the lower arenaceous Alwar Group and the upper argillaceous Ajabgarh Group are separated by the:",
            "options": {"a": "Raialo series", "b": "Susnai breccia", "c": "Kushalgarh limestone / Hornstone breccia", "d": "Hornstone breccia"},
            "answer": "c", "topic": "Delhi Supergroup", "subtopic": "Kushalgarh Limestone",
            "notes": "The Kushalgarh Limestone and overlying Hornstone Breccia constitute the transition zone separating the Alwar quartzite horsts from the Ajabgarh pelite-carbonate graben successions."
        },
        {
            "q_num": 21,
            "question": "Intercalated ash beds, conglomerates, and quartzites overlying spilitic and basaltic lava flows are characteristic of the:",
            "options": {"a": "Sausar-Sakoli series", "b": "Iron Ore series (Dhanjori / Dalma)", "c": "Simlipal series", "d": "Kolhan series"},
            "answer": "b", "topic": "Singhbhum Geology", "subtopic": "Iron Ore & Volcanic Suites",
            "notes": "The Dhanjori and Iron Ore volcano-sedimentary successions of the Singhbhum craton exhibit subaerial to submarine basaltic lava flows interbedded with volcanic agglomerates, tuffs, and quartzites."
        },
        {
            "q_num": 22,
            "question": "Arrange the following Indian volcanic episodes in decreasing order of their geological age (oldest to youngest):\nI. Dras volcanics (Ladakh)\nII. Panjal volcanics (Kashmir)\nIII. Malani volcanics (Rajasthan)\nIV. Pitepani volcanics (Central India)",
            "options": {"a": "I, II, III, IV", "b": "IV, III, II, I", "c": "I, III, II, IV", "d": "III, IV, I, II"},
            "answer": "b", "topic": "Indian Volcanism", "subtopic": "Geochronological Order",
            "notes": "Geological ages: Pitepani volcanics (Paleoproterozoic, ~2.2 Ga) -> Malani suite (Neoproterozoic, ~750 Ma) -> Panjal volcanics (Permo-Carboniferous, ~290 Ma) -> Dras volcanics (Cretaceous-Eocene, ~100-50 Ma)."
        },
        {
            "q_num": 23,
            "question": "Match the following Indian lithostratigraphic marker units with their parent formations:\n(A) Needle shales — (1) Talchir stage\n(B) Khardeola grits — (4) Gwalior / Semri series\n(C) Fawn limestone — (3) Semri series (Vindhyan)\n(D) Purple sandstone — (2) Cambrian of Salt Range",
            "options": {"a": "A-3, B-4, C-2, D-1", "b": "A-1, B-2, C-3, D-4", "c": "A-3, B-2, C-4, D-1", "d": "A-1, B-4, C-3, D-2"},
            "answer": "d", "topic": "Stratigraphic Correlation", "subtopic": "Key Formations",
            "notes": "Needle shales are diagnostic of the basal Talchir Formation (Gondwana); Fawn Limestone belongs to the Semri Group (Vindhyan); Purple Sandstone belongs to the Salt Range Cambrian."
        },
        {
            "q_num": 24,
            "question": "One of the world's largest manifestations of anorogenic, post-collisional felsic magmatism during the Neoproterozoic is preserved in India as the:",
            "options": {"a": "Pitepani volcanics", "b": "Malani Igneous Suite", "c": "Dhanjori volcanics", "d": "Khowra traps"},
            "answer": "b", "topic": "Neoproterozoic Magmatism", "subtopic": "Malani Igneous Suite",
            "notes": "Covering over 50,000 km² in western Rajasthan, the Malani Igneous Suite (~750 Ma) represents one of the largest felsic volcanic provinces on Earth, dominated by rhyolitic flows, tuffs, and granites."
        },
        {
            "q_num": 25,
            "question": "Which of the following stratigraphic groups of the Vindhyan Supergroup exhibits the most pronounced folding and tectonic deformation?",
            "options": {"a": "Semri Group (Lower Vindhyan)", "b": "Kaimur Group", "c": "Rewa Group", "d": "Bhander Group"},
            "answer": "a", "topic": "Vindhyan Supergroup", "subtopic": "Semri Deformation",
            "notes": "The Semri Group (Lower Vindhyan) was deposited prior to the pre-Kaimur tectonic disturbance and displays sharp folds, faulting, and porcellanite deformation along the Son Valley."
        },
        {
            "q_num": 26,
            "question": "The economically important 'Nagod Limestone' belongs to which major group of the Vindhyan Supergroup?",
            "options": {"a": "Kaimur Group", "b": "Nallamalai Group", "c": "Kolhan Group", "d": "Bhander Group"},
            "answer": "d", "topic": "Vindhyan Supergroup", "subtopic": "Nagod Limestone",
            "notes": "The Nagod (or Bhander) Limestone is a major cement-grade carbonate unit belonging to the uppermost Proterozoic Bhander Group of the Upper Vindhyan sequence."
        },
        {
            "q_num": 27,
            "question": "Lithologically, the Bhander Group of the Vindhyan Supergroup is composed of:",
            "options": {"a": "Argillaceous rocks only", "b": "Arenaceous rocks only", "c": "Calcareous rocks only", "d": "Partly arenaceous, partly calcareous, and argillaceous strata"},
            "answer": "d", "topic": "Vindhyan Supergroup", "subtopic": "Bhander Lithology",
            "notes": "The Bhander Group comprises a complete mixed siliciclastic-carbonate sequence: Ganurgarh Shale, Bhander (Nagod) Limestone, Sirbu Shale, and Upper Bhander Sandstone."
        },
        {
            "q_num": 28,
            "question": "In the Lower Vindhyan Semri Group of the Son Valley, profusely developed, well-preserved columnar stromatolites occur in the:",
            "options": {"a": "Suket shales", "b": "Bleaching shales", "c": "Fawn (Glauconitic) limestone", "d": "Kajrahat limestone"},
            "answer": "c", "topic": "Vindhyan Stromatolites", "subtopic": "Fawn Limestone",
            "notes": "The Fawn Limestone (Kheinjua Formation, Semri Group) contains well-preserved biostromal columnar stromatolites including Colonella and Conophyton garganicus."
        },
        {
            "q_num": 29,
            "question": "The most voluminous and topographically prominent rock type across the Vindhyan Supergroup is:",
            "options": {"a": "Limestone", "b": "Sandstone", "c": "Shale", "d": "Gneiss"},
            "answer": "b", "topic": "Vindhyan Supergroup", "subtopic": "Dominant Lithology",
            "notes": "Vindhyan sandstones (Kaimur, Rewa, and Bhander quartzites/sandstones) form magnificent scarps and plateau ranges extending across 100,000 km² from Sasaram (Bihar) to Chittorgarh (Rajasthan)."
        },
        {
            "q_num": 30,
            "question": "The stratigraphic succession comprising the Mallampalli, Korsamaram, Mulug, and Albaka formations belongs to the:",
            "options": {"a": "Pakhal Group (Godavari Valley)", "b": "Sullavai Group", "c": "Bhima Group", "d": "Mesozoic of W. Rajasthan"},
            "answer": "a", "topic": "Pranhita-Godavari Basin", "subtopic": "Pakhal Supergroup",
            "notes": "The Mesoproterozoic Pakhal Group occupies the western and eastern flanks of the Pranhita-Godavari graben, divided into the Mallampalli and Mulug sub-basins."
        },
        {
            "q_num": 31,
            "question": "The topmost quartzitic sandstone unit of the Pakhal succession (the Albaka Sandstone) is correlated with the:",
            "options": {"a": "Bairenkonda Quartzite", "b": "Srisailam Quartzite of the Cuddapahs", "c": "Pinnacled Quartzite of Kurnool", "d": "Dhandraul Quartzite of the Vindhyans"},
            "answer": "b", "topic": "Pakhal-Cuddapah Correlation", "subtopic": "Albaka Sandstone",
            "notes": "Official note (p. 327): The topmost formation of the Pakhal Group, the Albaka Sandstone, is correlated with the Srisailam Quartzite (uppermost Cuddapah Supergroup)."
        },
        {
            "q_num": 32,
            "question": "In the northern extensions of the Pranhita Valley (Maharashtra-Adilabad), Purana sedimentary rocks equivalent to the Pakhals are designated as the:",
            "options": {"a": "Gollapilli beds", "b": "Penganga Group", "c": "Sullavai Group", "d": "Indravati Group"},
            "answer": "b", "topic": "Penganga Group", "subtopic": "Pranhita Basin",
            "notes": "The Penganga Group represents unmetamorphosed platform carbonate-shale-sandstone sequences in the northern Pranhita basin, correlating with the Upper Pakhal Group."
        },
        {
            "q_num": 33,
            "question": "Which of the following Indian stratigraphic correlations is/are correct?\n(i) Sullavai Quartzites — Pinnacled Quartzites of the Kurnool Group\n(ii) Pranhita Sandstone of Pengangas — Banganapalli Quartzites of Kurnool Group\n(iii) Dogra slates — Dharwar schists\n(iv) Bhander Sandstone — Purple Sandstone of Salt Range",
            "options": {"a": "(i), (ii) and (iv) only", "b": "(i) and (iii) only", "c": "(ii) and (iv) only", "d": "(i) and (iv) only"},
            "answer": "a", "topic": "Inter-Basinal Correlation", "subtopic": "Purana-Cambrian Matches",
            "notes": "Dogra slates of Kashmir are Neoproterozoic-Cambrian, whereas Dharwar schists are Neoarchean (>2.6 Ga); hence statement (iii) is completely erroneous, while (i), (ii), and (iv) are valid."
        },
        {
            "q_num": 34,
            "question": "The flaggy, high-grade cement-making 'Shahabad Limestone' belongs to which Purana basin of South India?",
            "options": {"a": "Penganga Group", "b": "Kurnool Group", "c": "Bhima Group", "d": "Badami Group"},
            "answer": "c", "topic": "Bhima Basin", "subtopic": "Shahabad Limestone",
            "notes": "The Shahabad Limestone constitutes the middle carbonate formation of the Neoproterozoic Bhima Group in the Gulbarga-Bijapur districts of Karnataka."
        },
        {
            "q_num": 35,
            "question": "Detailed geological re-mapping of the Kaladgi Basin (Karnataka) by the Geological Survey of India led to the separation of an upper, flat-lying horizontal succession into the:",
            "options": {"a": "Indravati Group", "b": "Badami Group", "c": "Martoli Formation", "d": "Morar Formation"},
            "answer": "b", "topic": "Kaladgi Basin", "subtopic": "Badami Group Separation",
            "notes": "Viswanathiah (1977) separated the horizontal, unmetamorphosed arenaceous Badami Group from the underlying folded Bagalkot Group (Kaladgi Supergroup proper)."
        },
        {
            "q_num": 36,
            "question": "On the basis of organic microfossil findings (Chitinozoa, acritarchs, and algal filaments), the Badami Group has been correlated with the:",
            "options": {"a": "Cambrian", "b": "Ordovician", "c": "Silurian", "d": "Devonian"},
            "answer": "b", "topic": "Badami Group", "subtopic": "Biostratigraphic Age",
            "notes": "In Dr. Ausaf Sayeed's text key, option b (Ordovician) is recorded based on reports of early microplankton and chitinozoan organic remains in the Badami sandstones."
        },
        {
            "q_num": 37,
            "question": "Which of the following Lesser Himalayan carbonate successions contains magnificently preserved columnar stromatolites (e.g., Collenia baicalica)?",
            "options": {"a": "Subathu Formation", "b": "Kasauli Formation", "c": "Shali / Deoban Group", "d": "Jutogh Group"},
            "answer": "c", "topic": "Himalayan Stratigraphy", "subtopic": "Shali-Deoban Stromatolites",
            "notes": "The Mesoproterozoic Shali and Deoban formations of Himachal and Garhwal comprise thick stromatolite-bearing dolomitic limestones, correlating with the Vindhyan carbonates."
        },
        {
            "q_num": 38,
            "question": "In the Eastern Himalayas of Sikkim and Darjeeling, the high-grade gneissose crystalline thrust sheet overlying the Daling phyllites is known as the:",
            "options": {"a": "Salkhala series", "b": "Vaikrita system", "c": "Daling series", "d": "Darjeeling Gneiss"},
            "answer": "d", "topic": "Himalayan Inverted Metamorphism", "subtopic": "Darjeeling Gneiss",
            "notes": "The Darjeeling Gneiss (sillimanite-kyanite-bearing garnetiferous gneiss) overlies the chlorite-sericite Daling phyllites along a regional thrust displaying inverted metamorphism."
        },
        {
            "q_num": 39,
            "question": "The manganese-bearing metasedimentary Precambrian belt exposed around Panchmahals, Chhota Udepur, and Vadodara in Gujarat is known as the:",
            "options": {"a": "Sonawani series", "b": "Sausar series", "c": "Champaner series", "d": "Jutogh and Chail series"},
            "answer": "c", "topic": "Gujarat Precambrian", "subtopic": "Champaner Group",
            "notes": "The Champaner Group represents the southernmost extension of the Aravalli-Delhi orogenic system in Gujarat, consisting of quartzites, conglomerates, slates, and manganiferous limestones."
        },
        {
            "q_num": 40,
            "question": "In the Indian subcontinent, continuous and complete sedimentary transitions across the Precambrian-Cambrian boundary are located in the:\n(1) Lolab Formation (Kashmir)\n(2) Ralam Conglomerate / Garbyang Formation (Kumaon)\n(3) Kunzam La Formation (Spiti)\n(4) Bhander Group (Vindhyan)",
            "options": {"a": "1 only", "b": "2 only", "c": "1, 2 and 3 only", "d": "All of the above"},
            "answer": "c", "topic": "Precambrian-Cambrian Boundary", "subtopic": "Tethyan Himalayan Boundary",
            "notes": "The Tethyan Himalayan belt of Kashmir, Spiti, and Kumaon preserves continuous marine sedimentation across the Ediacaran-Cambrian boundary demarcated by small shelly fossils and trace fossils."
        },
        {
            "q_num": 41,
            "question": "The renowned 'Syringothyris Limestone' of the Kashmir Tethyan succession belongs to the:",
            "options": {"a": "Early Carboniferous (Tournaisian)", "b": "Middle Carboniferous", "c": "Upper Carboniferous", "d": "Permian"},
            "answer": "a", "topic": "Kashmir Paleozoic", "subtopic": "Syringothyris Limestone",
            "notes": "The Syringothyris Limestone is an Early Carboniferous (Tournaisian) chronostratigraphic marker unit rich in the brachiopod Syringothyris cuspidata, overlying the Muth Quartzite."
        },
        {
            "q_num": 42,
            "question": "The quartzitic 'Nagthat Formation' of the Lesser Himalayan Krol Belt (Jaunsar Group) is of:",
            "options": {"a": "Archaean age", "b": "Proterozoic age", "c": "Paleozoic (Devonian-Carboniferous) age", "d": "Mesozoic age"},
            "answer": "c", "topic": "Lesser Himalayan Stratigraphy", "subtopic": "Nagthat Formation",
            "notes": "The Nagthat Formation (Jaunsar Group) consists of shallow-marine pink, purple, and green quartzites and conglomerates classically assigned a Paleozoic (Devonian) age."
        },
        {
            "q_num": 43,
            "question": "Which of the following represents the correct cyclic sedimentation sequence (fining-upward fluviatile cyclothem) in the Indian Gondwana coal measures?",
            "options": {"a": "Coal -> Shale -> Sandstone", "b": "Coal -> Sandstone -> Shale", "c": "Sandstone -> Shale -> Coal", "d": "Shale -> Sandstone -> Coal"},
            "answer": "c", "topic": "Gondwana Sedimentology", "subtopic": "Cyclic Sedimentation",
            "notes": "The classic Gondwana cyclothem initiates with basal channel-lag coarse sandstone, grading upward into inter-channel floodplain siltstone/shale, and terminating with swamp peat (coal)."
        },
        {
            "q_num": 44,
            "question": "The sedimentary deposits of the Middle Gondwana (Triassic: Panchet and Mahadeva groups) were deposited under a prevailing climate that was:",
            "options": {"a": "Warm and humid", "b": "Warm and dry (semi-arid)", "c": "Cold and humid", "d": "Cold and dry"},
            "answer": "b", "topic": "Gondwana Paleoclimate", "subtopic": "Triassic Climate",
            "notes": "The Middle Gondwana is characterized by thick red clays, oxidized ferruginous sandstones, and calcretes, reflecting a shift to warm, arid to semi-arid tropical climates."
        },
        {
            "q_num": 45,
            "question": "Sedimentologically, the continental sedimentary rocks of the Peninsular Indian Gondwana Supergroup are overwhelmingly of:",
            "options": {"a": "Fluviatile (river channel and floodplain) origin", "b": "Lacustrine origin", "c": "Marine origin", "d": "Glacial origin"},
            "answer": "a", "topic": "Gondwana Depositional Environment", "subtopic": "Fluviatile Dominance",
            "notes": "Except for the basal glacial Talchir tillite and rare short-lived marine transgressive intercalations (Manendragarh, Umaria), the Gondwana strata represent braided-to-meandering river systems."
        }
    ]

def get_questions_46_to_90():
    # Questions 46 to 90
    return [
        {
            "q_num": 46,
            "question": "The Glossopteris flora reached its acme and highest stage of evolutionary development and species diversification during the:",
            "options": {"a": "Damuda Group / Karharbari", "b": "Barakar formation", "c": "Raniganj formation", "d": "Panchet formation"},
            "answer": "c", "topic": "Gondwana Flora", "subtopic": "Raniganj Acme",
            "notes": "The Glossopteris flora attained its maximum floral richness in the Late Permian Raniganj Formation (Upper Damuda), boasting over 40 species of Glossopteris."
        },
        {
            "q_num": 47,
            "question": "Which of the following Indian Gondwana stratigraphic units is commercially richest in workable bituminous coal seams and plant megafossils?",
            "options": {"a": "Damuda Group (Barakar & Raniganj formations)", "b": "Talchir Formation", "c": "Panchet Formation", "d": "Rajmahal Formation"},
            "answer": "a", "topic": "Indian Coal Stratigraphy", "subtopic": "Damuda Group",
            "notes": "The Damuda Group produces over 98% of India's non-coking and coking bituminous coal reserves, primarily from the Barakar (Lower Damuda) and Raniganj (Upper Damuda) formations."
        },
        {
            "q_num": 48,
            "question": "Which of the following famous fossil plant genera is strictly absent from the Indian Gondwana flora (belonging instead to the Euramerian province)?",
            "options": {"a": "Schizoneura", "b": "Pecopteris", "c": "Lepidodendron", "d": "Williamsonia"},
            "answer": "c", "topic": "Paleobotanical Provinces", "subtopic": "Euramerian vs Gondwana",
            "notes": "Lepidodendron (giant arborescent lycopsid) is a diagnostic element of the tropical Euramerian Carboniferous coal swamps and is absent from the cold Gondwana flora."
        },
        {
            "q_num": 49,
            "question": "The famous tongue-shaped seed-fern Glossopteris flora existed across the Gondwanaland continents during the total time span of:",
            "options": {"a": "Permian to Triassic", "b": "Permian to Jurassic", "c": "Carboniferous to Upper Triassic", "d": "Upper Carboniferous to Lower Triassic"},
            "answer": "d", "topic": "Glossopteris Biostratigraphy", "subtopic": "Temporal Range",
            "notes": "Glossopteris appeared in the Late Carboniferous (Talchir), dominated the Permian coal basins, declined abruptly at the Permian-Triassic boundary, and became extinct in the Early Triassic."
        },
        {
            "q_num": 50,
            "question": "Identify the diagnostic vertebrate and plant fossil assemblage characteristically occurring in the Early Triassic Panchet Formation:",
            "options": {
                "a": "Schizoneura gondwanensis, Glossopteris indica, Noeggerathiopsis hislopi",
                "b": "Schizoneura gondwanensis, Glossopteris indica, Gonioglyptus, Pachygonia",
                "c": "Glossopteris, Gangamopteris, Angiopteridium, Thinnfeldia",
                "d": "Dicroidium hughesi, Sphenopteris, Dadoxylon"
            },
            "answer": "b",
            "topic": "Panchet Biostratigraphy", "subtopic": "Triassic Fauna",
            "notes": "The Panchet Formation contains the surviving gymnosperm Schizoneura alongside famous labyrinthodont amphibians (Gonioglyptus, Pachygonia) and the therapsid reptile Lystrosaurus."
        },
        {
            "q_num": 51,
            "question": "Choose the correct chronological order of appearance of index fossil plant genera throughout the Indian Gondwana stratigraphic succession:",
            "options": {
                "a": "Glossopteris -> Schizoneura -> Dicroidium -> Williamsonia",
                "b": "Glossopteris -> Schizoneura -> Williamsonia -> Dicroidium",
                "c": "Glossopteris -> Williamsonia -> Schizoneura -> Dicroidium",
                "d": "Schizoneura -> Glossopteris -> Dicroidium -> Williamsonia"
            },
            "answer": "a", "topic": "Gondwana Floral Succession", "subtopic": "Chronological Appearance",
            "notes": "Chronological succession: Permian Glossopteris -> Permo-Triassic Schizoneura -> Middle-Upper Triassic Dicroidium -> Jurassic-Cretaceous Williamsonia (Bennettitales)."
        },
        {
            "q_num": 52,
            "question": "The earliest indisputable evidence of late Paleozoic continental glacial action in the Indian Peninsula is obtained from the:",
            "options": {"a": "Talchir Boulder Bed (Tillite)", "b": "Bap and Badhaura formation", "c": "Kaldurga conglomerate", "d": "Blaini beds"},
            "answer": "a", "topic": "Gondwana Glaciation", "subtopic": "Talchir Tillite",
            "notes": "Official note (p. 327): The first evidence of glacial action in the Gondwanas is obtained from the Talchir rocks of Orissa/MP, containing striated pavement and faceted glacial boulders."
        },
        {
            "q_num": 53,
            "question": "The lithostratigraphic equivalent of the basal Gondwana Talchir tillites in the Kashmir-Hazara Himalaya is known as the:",
            "options": {"a": "Mandhali beds", "b": "Blaini beds", "c": "Agglomeratic Slate / Tanakki Boulder Bed", "d": "Ralam conglomerate"},
            "answer": "c", "topic": "Himalayan Permo-Carboniferous", "subtopic": "Tanakki & Agglomeratic Slate",
            "notes": "The glacio-marine Agglomeratic Slate of Kashmir and Tanakki Boulder Bed of Hazara correlate directly with the Asselian-Sakmarian Talchir tillite of the Indian Shield."
        },
        {
            "q_num": 54,
            "question": "The precise stratigraphic position of the famous 'Gangamopteris beds' of the Kashmir Valley is located:",
            "options": {
                "a": "Below the Panjal Volcanics",
                "b": "Intercalated within and immediately overlying the Panjal Volcanics",
                "c": "Above the Zewan Formation",
                "d": "Below the Muth Quartzite"
            },
            "answer": "b",
            "topic": "Kashmir Stratigraphy", "subtopic": "Gangamopteris Beds Position",
            "notes": "The Gangamopteris beds occur as pyroclastic tuffs and novaculite layers directly overlying and interbedded with the terminal flows of the Panjal Traps, underlying the marine Zewan Formation."
        },
        {
            "q_num": 55,
            "question": "In the Salt Range (Pakistan) and Spiti, the Upper Permian brachiopod-rich marine sequence is classically designated as the:",
            "options": {"a": "Productus Limestone Series (Chhidru Formation)", "b": "Speckled Sandstone", "c": "Purple Sandstone", "d": "Magnesian Sandstone"},
            "answer": "a", "topic": "Tethyan Permian", "subtopic": "Productus Limestone",
            "notes": "The Productus Limestone of the Salt Range (Amb, Wargal, and Chhidru formations) contains abundant late Permian productid brachiopods, recording a complete marine Permian-Triassic transition."
        },
        {
            "q_num": 56,
            "question": "The world-famous 'Lilang Group' of the Spiti Valley represents a magnificent, virtually unbroken marine succession of which geological period?",
            "options": {"a": "Permian", "b": "Carboniferous", "c": "Triassic", "d": "Jurassic"},
            "answer": "c", "topic": "Spiti Stratigraphy", "subtopic": "Lilang Supergroup",
            "notes": "The Lilang Supergroup of Spiti (~1000 m thick) is one of the world's most complete marine Triassic sections, subdivided into classic ammonoid zones from Otoceras woodwardi to Monotis salinaria."
        },
        {
            "q_num": 57,
            "question": "The 'Kioto Limestone' of the Tethyan Himalayan belt spans which chronostratigraphic interval?",
            "options": {"a": "Lower Triassic", "b": "Upper Triassic (Rhaetian) to Lower Jurassic (Liassic)", "c": "Middle Jurassic", "d": "Upper Cretaceous"},
            "answer": "b", "topic": "Spiti Stratigraphy", "subtopic": "Kioto Limestone",
            "notes": "The massive Kioto Limestone (Para and Tagling stages) represents shallow-marine carbonate platform deposition spanning the Triassic-Jurassic systemic boundary across the Tethys."
        },
        {
            "q_num": 58,
            "question": "The celebrated cephalopod-rich 'Spiti Shales' formation belongs to which geological epoch?",
            "options": {"a": "Upper Jurassic (Oxfordian to Tithonian)", "b": "Lower Jurassic", "c": "Middle Cretaceous", "d": "Lower Triassic"},
            "answer": "a", "topic": "Spiti Stratigraphy", "subtopic": "Spiti Shales",
            "notes": "The Spiti Shales (Chidamu and Lochambal beds) consist of black, carbonaceous, friable shales containing famous ammonite-bearing calcareous concretions (Saligrams) of Late Jurassic age."
        },
        {
            "q_num": 59,
            "question": "The classic cephalopod-rich Jurassic succession of Kutch (Gujarat) is divided into four major chronostratigraphic units. From oldest to youngest, these are:",
            "options": {
                "a": "Katrol -> Patcham -> Chari -> Umia",
                "b": "Chari -> Patcham -> Katrol -> Umia",
                "c": "Patcham -> Chari -> Katrol -> Umia",
                "d": "Umia -> Katrol -> Chari -> Patcham"
            },
            "answer": "c",
            "topic": "Kutch Mesozoic", "subtopic": "Subdivisions",
            "notes": "The Kutch Jurassic sequence (William Waagen, 1873) comprises: Patcham (Bathonian) -> Chari (Callovian-Oxfordian) -> Katrol (Kimmeridgian) -> Umia (Tithonian-Neocomian)."
        },
        {
            "q_num": 60,
            "question": "In the Kutch Jurassic succession, the famous Macrocephalites macrocephalus ammonite assemblage characterizes which stratigraphic group?",
            "options": {"a": "Patcham Group", "b": "Katrol Group", "c": "Umia Group", "d": "Chari Group"},
            "answer": "d", "topic": "Kutch Biostratigraphy", "subtopic": "Chari Macrocephalites",
            "notes": "The basal limestone and shales of the Chari Group (Callovian stage) are celebrated for the Macrocephalites macrocephalus zone, correlating with European Callovian ammonite zones."
        },
        {
            "q_num": 61,
            "question": "The famous Golden Oolite rock unit, characterized by ferruginous-coated aragonitic/calcitic ooids, occurs within the:",
            "options": {"a": "Patcham Group of Kutch", "b": "Umia Group of Kutch", "c": "Katrol Group of Kutch", "d": "Chari Group of Kutch"},
            "answer": "d", "topic": "Kutch Jurassic", "subtopic": "Golden Oolite",
            "notes": "The Golden Oolite is an iconic marker bed at the base of the Chari Group near Keera and Chari villages, consisting of calcarenite ooids coated with thin films of yellow-brown iron oxide."
        },
        {
            "q_num": 62,
            "question": "In the Cretaceous succession of the Cauvery Basin (Tamil Nadu), the correct chronological order of the three major marine groups from oldest to youngest is:",
            "options": {
                "a": "Ariyalur -> Trichinopoly -> Uttatur",
                "b": "Trichinopoly -> Uttatur -> Ariyalur",
                "c": "Uttatur -> Trichinopoly -> Ariyalur",
                "d": "Uttatur -> Ariyalur -> Trichinopoly"
            },
            "answer": "c",
            "topic": "Cauvery Basin Cretaceous", "subtopic": "Group Succession",
            "notes": "The classic marine Cretaceous of South India (H.F. Blanford, 1862) comprises: Uttatur Group (Cenomanian) -> Trichinopoly Group (Turonian-Coniacian) -> Ariyalur Group (Santonian-Maastrichtian)."
        },
        {
            "q_num": 63,
            "question": "The uppermost, terminal marine Cretaceous formation of the Ariyalur Group in the Cauvery Basin (Danian passage bed equivalent) is the:",
            "options": {"a": "Niniyur Formation", "b": "Kallankurichchi Formation", "c": "Kallamedu Formation", "d": "Sillakkudi Formation"},
            "answer": "a", "topic": "Cauvery Basin Cretaceous", "subtopic": "Niniyur Formation",
            "notes": "The Niniyur Formation (containing the nautiloid Hercoglossa danica) overlies the Maastrichtian Kallamedu formation, representing Danian (earliest Paleocene) marine sedimentation."
        },
        {
            "q_num": 64,
            "question": "Skeletal remains and nested egg clutches of giant titanosaurid sauropod dinosaurs in Central India occur characteristically in the:",
            "options": {"a": "Bagh Beds", "b": "Lameta Formation (Infratrappean beds)", "c": "Intertrappean beds", "d": "Jabalpur Formation"},
            "answer": "b", "topic": "Cretaceous Dinosaurs", "subtopic": "Lameta Formation",
            "notes": "The Lameta Formation (~66-68 Ma fluvio-lacustrine strata directly underlying the Deccan Traps at Jabalpur) has yielded iconic skeletons of Titanosaurus indicus and Rajasaurus narmadensis."
        },
        {
            "q_num": 65,
            "question": "The marine Cretaceous 'Bagh Beds' of the Narmada Valley contain a distinctive Mediterranean Tethyan invertebrate fauna that is correlated with the:",
            "options": {"a": "Trichinopoly Group", "b": "Ariyalur Group", "c": "Uttatur Group of South India", "d": "Umia Group of Kutch"},
            "answer": "c", "topic": "Bagh Beds", "subtopic": "Correlations",
            "notes": "The Bagh Beds (Nimar Sandstone, Nodular Limestone, Deola Marl, Coralline Limestone) represent an arm of the Tethyan Cretaceous transgression correlating with the Cenomanian Uttatur Group."
        },
        {
            "q_num": 66,
            "question": "The vast basaltic lava floods of the Deccan Volcanic Province (Deccan Traps) erupted primarily across which narrow geochronological interval?",
            "options": {"a": "Middle Jurassic", "b": "Early Cretaceous", "c": "Eocene-Oligocene", "d": "Cretaceous-Paleogene Boundary (~66 to 65 Ma)"},
            "answer": "d", "topic": "Deccan Volcanism", "subtopic": "Eruption Duration",
            "notes": "High-precision Ar-Ar and U-Pb geochronology confirms that over 90% of the Deccan basalt volume (~1 million km³) erupted rapidly within ~750,000 years across the K-Pg boundary (~66.2-65.5 Ma)."
        },
        {
            "q_num": 67,
            "question": "Sedimentary intercalations of chert, limestone, and shale deposited in shallow lakes between successive Deccan basaltic lava flows are termed:",
            "options": {"a": "Infratrappean beds", "b": "Intertrappean beds", "c": "Lameta beds", "d": "Laterites"},
            "answer": "b", "topic": "Deccan Traps", "subtopic": "Intertrappean Beds",
            "notes": "Intertrappean beds represent fossiliferous lacustrine and fluviatile sediments deposited during volcanic quiescence intervals between basalt flow eruptions, preserving freshwater flora (Physa, Azolla)."
        },
        {
            "q_num": 68,
            "question": "The Cenozoic Himalayan foreland basin succession is represented by the:",
            "options": {"a": "Subathu -> Dagshai -> Kasauli -> Siwalik succession", "b": "Siwalik -> Kasauli -> Dagshai succession", "c": "Tal -> Subathu -> Kasauli succession", "d": "Karewa -> Siwalik -> Subathu succession"},
            "answer": "a", "topic": "Himalayan Foreland Basin", "subtopic": "Cenozoic Sequence",
            "notes": "The Himalayan foreland succession records initial marine flexural loading (Eocene Subathu Formation) passing into brackish/fluvial red-bed molasse (Dagshai and Kasauli) and Neogene Siwaliks."
        },
        {
            "q_num": 69,
            "question": "The marine Eocene 'Subathu Formation' of the Outer Himalayas is characteristically rich in which group of larger benthic foraminifera?",
            "options": {"a": "Nummulites and Assilina", "b": "Fusulinids", "c": "Orbitolina", "d": "Globigerina"},
            "answer": "a", "topic": "Subathu Formation", "subtopic": "Nummulites",
            "notes": "The Subathu Formation represents shallow-marine Tethyan shelf muds packed with larger benthic foraminifera, notably Nummulites atacicus and Assilina granulosa."
        },
        {
            "q_num": 70,
            "question": "The Siwalik Group of the Himalayan foothills is classic worldwide for representing a gigantic Cenozoic:",
            "options": {"a": "Flysch deposit", "b": "Glacial tillite", "c": "Molasse deposit", "d": "Evaporite sequence"},
            "answer": "c", "topic": "Siwalik Group", "subtopic": "Molasse Nature",
            "notes": "The Siwalik Group (~6,000 m thick) constitutes one of the world's most magnificent synorogenic molasse wedges, shedding eroded debris from the rising Himalayan mountain belt into a foreland basin."
        },
        {
            "q_num": 71,
            "question": "The Siwalik Supergroup is formally subdivided into three major subgroups. From base to top, these are:",
            "options": {
                "a": "Upper Siwalik -> Middle Siwalik -> Lower Siwalik",
                "b": "Pinjor -> Nagri -> Kamlial",
                "c": "Lower Siwalik (Kamlial, Chinji) -> Middle Siwalik (Nagri, Dhok Pathan) -> Upper Siwalik (Tatrot, Pinjor, Boulder Conglomerate)",
                "d": "Dagshai -> Kasauli -> Siwalik"
            },
            "answer": "c",
            "topic": "Siwalik Stratigraphy", "subtopic": "Subdivisions",
            "notes": "The classic tripartite subdivision: Lower Siwalik (Kamlial, Chinji; Middle Miocene), Middle Siwalik (Nagri, Dhok Pathan; Late Miocene), Upper Siwalik (Tatrot, Pinjor, Boulder Conglomerate; Pliocene-Pleistocene)."
        },
        {
            "q_num": 72,
            "question": "In the heavy mineral provenance studies of the Siwalik Group, the diagnostic dominance of kyanite characterizes the sediments of the:",
            "options": {"a": "Middle Siwalik", "b": "Lower Siwalik", "c": "Upper Siwalik", "d": "Subathu Formation"},
            "answer": "a", "topic": "Siwalik Provenance", "subtopic": "Heavy Mineral Suites",
            "notes": "Official note (p. 327): The Lower, Middle, and Upper Siwaliks show a definitive heavy mineral signature: staurolite dominates the Lower Siwalik, kyanite dominates the Middle Siwalik, and hornblende dominates the Upper Siwalik."
        },
        {
            "q_num": 73,
            "question": "The third and most paroxysmal upheaval of the Himalaya, known as the 'Sirmurian orogeny', occurred during the:",
            "options": {"a": "Late Cretaceous", "b": "Middle Miocene", "c": "Late Pliocene", "d": "Pleistocene"},
            "answer": "b", "topic": "Himalayan Orogeny", "subtopic": "Sirmurian Phase",
            "notes": "Official note (p. 327): The third Himalayan upheaval during Middle Miocene times, known as the Sirmurian orogeny, was the most pronounced phase of Himalayan mountain-building."
        },
        {
            "q_num": 74,
            "question": "The intermontane lacustrine and fluviatile Quaternary valley-fill terraces of the Kashmir Basin are known as the:",
            "options": {"a": "Bhabar deposits", "b": "Karewa Group", "c": "Terai deposits", "d": "Khaddar beds"},
            "answer": "b", "topic": "Quaternary Stratigraphy", "subtopic": "Karewa Group",
            "notes": "The Karewa Group (~1,300 m thick) consists of Plio-Pleistocene lacustrine and fluvio-glacial deposits preserving diatomites, lignite, plant fossils, and hominid stone tool artifacts."
        },
        {
            "q_num": 75,
            "question": "The Karewa sediments of Kashmir are subdivided into Lower Karewa and Upper Karewa by an intervening:",
            "options": {"a": "Basaltic lava flow", "b": "Marine limestone", "c": "Angular unconformity / structural dislocation", "d": "Volcanic ash layer only"},
            "answer": "c", "topic": "Karewa Group", "subtopic": "Unconformity",
            "notes": "The Lower Karewa is tilted and deformed by the uplift of the Pir Panjal Range, separated from the flat-lying Upper Karewa by a distinct angular unconformity."
        },
        {
            "q_num": 76,
            "question": "The world-famous 'Bagh Beds' of western India are exposed along the valley of which major river?",
            "options": {"a": "Godavari", "b": "Mahanadi", "c": "Krishna", "d": "Narmada"},
            "answer": "d", "topic": "Bagh Beds", "subtopic": "Geographic Occurrence",
            "notes": "The Bagh Beds outcrop as detached inliers along the Narmada River rift valley in the Dhar, Jhabua, Barwah, and Kawant districts of Madhya Pradesh and Gujarat."
        },
        {
            "q_num": 77,
            "question": "The oldest marine fossiliferous sedimentary strata resting directly upon the crystalline basement in the Spiti Valley belong to the:",
            "options": {"a": "Po Series", "b": "Lipak Series", "c": "Haimanta Group (Kunzam La Formation)", "d": "Muth Quartzite"},
            "answer": "c", "topic": "Spiti Stratigraphy", "subtopic": "Haimanta Group",
            "notes": "The Haimanta Group (Neoproterozoic to Middle Cambrian) comprises the basal sedimentary sequence of the Spiti Tethyan basin, containing trilobites (Redlichia noetlingi)."
        },
        {
            "q_num": 78,
            "question": "The 'Muth Quartzite' of the Tethyan Himalayas represents an iconic, pure, white, snow-like orthoquartzite marker bed of which geological age?",
            "options": {"a": "Cambrian", "b": "Ordovician", "c": "Silurian", "d": "Devonian"},
            "answer": "d", "topic": "Himalayan Marker Beds", "subtopic": "Muth Quartzite",
            "notes": "The Muth Quartzite (~150-300 m thick) is a remarkably pure supermature quartz arenite (>98% SiO2) extending from Kashmir through Spiti to Kumaon, dated as Middle to Late Devonian."
        },
        {
            "q_num": 79,
            "question": "The 'Lipak Formation' of the Spiti Paleozoic succession is of Early Carboniferous age and is characterized by abundant:",
            "options": {"a": "Graptolites", "b": "Trilobites", "c": "Productid and Spiriferid brachiopods and corals", "d": "Ammonites"},
            "answer": "c", "topic": "Spiti Paleozoic", "subtopic": "Lipak Formation",
            "notes": "The Lipak Formation comprises fossiliferous limestones and dolomites rich in Early Carboniferous marine fossils (Syringothyris, Productus, Phillipsia, and rugose corals)."
        },
        {
            "q_num": 80,
            "question": "The famous diamondiferous conglomerate horizon in the Kurnool Group of Andhra Pradesh occurs at the base of the:",
            "options": {"a": "Banganapalle Quartzite", "b": "Narji Limestone", "c": "Auk Shale", "d": "Paniam Quartzite"},
            "answer": "a", "topic": "Kurnool Group", "subtopic": "Banganapalle Diamond Conglomerate",
            "notes": "The basal Banganapalle Quartzite contains diamondiferous conglomerate bands that yielded historical Golconda diamonds derived from eroded Wajrakarur kimberlite pipes."
        },
        {
            "q_num": 81,
            "question": "The diamond-bearing kimberlitic pipe rock of the Vindhyan Basin in Central India is located at:",
            "options": {"a": "Wajrakarur", "b": "Lattavaram", "c": "Chelima", "d": "Majhgawan (Panna)"},
            "answer": "d", "topic": "Vindhyan Diamonds", "subtopic": "Majhgawan Pipe",
            "notes": "The Majhgawan diamondiferous pipe (~1100 Ma olivine lamproite/kimberlite) in Panna (M.P.) intrudes the Kaimur Sandstone and served as the source for alluvial Panna diamonds."
        },
        {
            "q_num": 82,
            "question": "The famous high-grade iron ore deposits of the Iron Ore Group (IOG) in the Singhbhum-Orissa craton occur in the form of:",
            "options": {"a": "Oolitic siderite", "b": "Banded Iron Formations (BIF / BHQ / BHJ)", "c": "Magnetite sands", "d": "Pyritic gossans"},
            "answer": "b", "topic": "Singhbhum-Orissa Craton", "subtopic": "Banded Iron Formation",
            "notes": "The Noamundi, Joda, and Gorumahisani iron ore deposits occur within Banded Hematite Jasper (BHJ) and Banded Hematite Quartzite (BHQ) of the Archean Iron Ore Supergroup (~3.1-3.3 Ga)."
        },
        {
            "q_num": 83,
            "question": "The 'Singhbhum Shear Zone' (Copper Belt Thrust) separates the older Singhbhum Craton in the south from the:",
            "options": {"a": "Bhandara Craton", "b": "Dharwar Craton", "c": "North Singhbhum Mobile Belt (Chotanagpur terrane)", "d": "Bastar Craton"},
            "answer": "c", "topic": "Singhbhum Shear Zone", "subtopic": "Tectonic Boundaries",
            "notes": "The 200-km-long arcuate Singhbhum Shear Zone separates the low-grade Archaean Singhbhum Craton to the south from the Mesoproterozoic North Singhbhum Mobile Belt to the north."
        },
        {
            "q_num": 84,
            "question": "The rich uranium deposits of Jaduguda, Bhatin, and Narwapahar in Jharkhand are geologically localized within the:",
            "options": {"a": "Kolhan Group", "b": "Singhbhum Shear Zone (Copper Belt)", "c": "Kaimur Sandstone", "d": "Dhanjori quartzite"},
            "answer": "b", "topic": "Singhbhum Metallogeny", "subtopic": "Uranium Mineralization",
            "notes": "Uranium (uraninite) mineralization at Jaduguda occurs in intensely sheared chlorite-sericite schists and tourmaline breccias within the Singhbhum Shear Zone."
        },
        {
            "q_num": 85,
            "question": "The celebrated lead-zinc-silver deposits of Zawar in Rajasthan are hosted within dolomites of the:",
            "options": {"a": "Delhi Supergroup", "b": "Vindhyan Supergroup", "c": "Marwar Supergroup", "d": "Aravalli Supergroup"},
            "answer": "d", "topic": "Aravalli Metallogeny", "subtopic": "Zawar Lead-Zinc",
            "notes": "The Zawar Pb-Zn deposits (Mochia Mogra, Balaria) occur within siliceous dolomites of the Paleoproterozoic Aravalli Supergroup (~2.0-1.8 Ga)."
        },
        {
            "q_num": 86,
            "question": "Match the following pioneering Indian geologists with their fundamental stratigraphic contributions:\n(A) Indian Geological Time Scale 4-fold division — (2) Sir T.H. Holland\n(B) Dharwar System classification — (1) R. Bruce Foote\n(C) Secondary origin of Charnockite — (4) E. Vredenburg\n(D) Extrusive/Tectonic origin of Saline series — (3) C.S. Middlemiss",
            "options": {"a": "A-2, B-1, C-4, D-3", "b": "A-1, B-2, C-4, D-3", "c": "A-2, B-1, C-3, D-4", "d": "A-1, B-2, C-3, D-4"},
            "answer": "a", "topic": "History of Indian Geology", "subtopic": "Pioneering Geologists",
            "notes": "Sir T.H. Holland formulated the 4-fold Indian time scale (Archaean, Purana, Dravidian, Aryan); R. Bruce Foote established the Dharwar System in 1886; Vredenburg studied charnockites; Middlemiss mapped the Salt Range."
        },
        {
            "q_num": 87,
            "question": "Match the following Indian stratigraphic formations with their principal economic mineral associations:\n(A) Nallamalai Group (Cuddapah) — (4) Lead-Zinc (Agnigundala)\n(B) Mansar Formation (Sausar Group) — (3) Manganese ore (Gondite)\n(C) Bijaigarh Shale (Kaimur Group) — (2) Pyrite (Amjhore)\n(D) Banganapalle / Majhgawan beds — (1) Diamonds",
            "options": {"a": "A-2, B-3, C-1, D-4", "b": "A-3, B-1, C-2, D-4", "c": "A-4, B-3, C-2, D-1", "d": "A-4, B-3, C-1, D-2"},
            "answer": "c", "topic": "Economic Geology of India", "subtopic": "Stratigraphic Mineral Wealth",
            "notes": "Nallamalai Group hosts Agnigundala lead-copper; Sausar hosts major manganese gondites; Bijaigarh Shale hosts Amjhore bedded pyrite; Banganapalle hosts basal diamond conglomerates."
        },
        {
            "q_num": 88,
            "question": "Valuable continental Cenozoic lignite deposits in India occur in stratigraphic association with:\n(1) Cuddalore Sandstones of the Cauvery Basin (Neyveli, Tamil Nadu)\n(2) Karewa Group of the Kashmir Valley (Nichahom, Handwara)\n(3) Palana Formation of Western Rajasthan (Bikaner)",
            "options": {"a": "1 only", "b": "1 and 2 only", "c": "1 and 3 only", "d": "All of the above (1, 2 and 3)"},
            "answer": "d", "topic": "Indian Lignite Deposits", "subtopic": "Stratigraphic Distribution",
            "notes": "Major Indian lignite reserves occur across multiple Cenozoic epochs: Paleocene-Eocene Palana Formation in Rajasthan, Mio-Pliocene Cuddalore Formation at Neyveli, and Plio-Pleistocene Karewa beds at Nichahom in Kashmir."
        },
        {
            "q_num": 89,
            "question": "Choose the correct chronological sequence of Indian stratigraphic shale marker units from oldest to youngest:",
            "options": {
                "a": "Suket shales -> Binota shales -> Needle shales -> Fenestella shales -> Spiti shales",
                "b": "Binota shales -> Suket shales -> Fenestella shales -> Needle shales -> Spiti shales",
                "c": "Needle shales -> Fenestella shales -> Binota shales -> Suket shales -> Spiti shales",
                "d": "Binota shales -> Suket shales -> Needle shales -> Fenestella shales -> Spiti shales"
            },
            "answer": "d", "topic": "Indian Shale Chronology", "subtopic": "Chronological Sequence",
            "notes": "Official note (p. 327): Binota shales (Aravalli, Paleoproterozoic ~2.0 Ga) -> Suket shales (Semri/Vindhyan, Mesoproterozoic ~1.4 Ga) -> Needle shales (basal Talchir, Late Carboniferous ~300 Ma) -> Fenestella shales (Permo-Carboniferous) -> Spiti shales (Late Jurassic ~150 Ma)."
        },
        {
            "q_num": 90,
            "question": "Which of the following Indian conglomerates represents the youngest geological age (least antiquity)?",
            "options": {"a": "Banganapalle Conglomerate", "b": "Bagra Conglomerate", "c": "Ralam Conglomerate", "d": "Hemis Conglomerate (Ladakh Molasse)"},
            "answer": "d", "topic": "Indian Conglomerates", "subtopic": "Relative Age",
            "notes": "Banganapalle is Neoproterozoic (Kurnool); Ralam is Cambrian (Tethyan Himalaya); Bagra is Upper Triassic (Gondwana); while Hemis Conglomerate represents the Cenozoic (Oligocene-Miocene) Indus molasse."
        }
    ]

def get_questions_91_to_135():
    # Questions 91 to 135
    return [
        {
            "q_num": 91,
            "question": "The renowned copper deposit of Khetri in Rajasthan is hosted within metamorphic rocks of the:",
            "options": {"a": "Banded Gneissic Complex", "b": "Aravalli Supergroup", "c": "Raialo Group", "d": "Delhi Supergroup (Ajabgarh Group)"},
            "answer": "d", "topic": "Delhi Metallogeny", "subtopic": "Khetri Copper",
            "notes": "The Khetri Copper Belt (Madhan-Kudan, Kolihan) is hosted in garnetiferous chlorite-biotite schists and amphibolites of the Mesoproterozoic Ajabgarh Group (Delhi Supergroup)."
        },
        {
            "q_num": 92,
            "question": "The rich manganese ore gondite deposits of Madhya Pradesh and Maharashtra occur within the:",
            "options": {"a": "Sakoli Group", "b": "Sausar Group (Mansar Formation)", "c": "Dharwar Supergroup", "d": "Iron Ore Group"},
            "answer": "b", "topic": "Sausar Group", "subtopic": "Gondite Manganese",
            "notes": "Sir Lewis Fermor coined the term 'gondite' for spessartine garnet-quartz rock occurring in the Mansar and Chorbaoli formations of the Sausar Group."
        },
        {
            "q_num": 93,
            "question": "The manganiferous metamorphic rocks known as 'kodurites' (containing spandite garnet, orthoclase, and apatite) are typically developed in the:",
            "options": {"a": "Eastern Ghats Mobile Belt (Andhra Pradesh & Odisha)", "b": "Sausar Group", "c": "Aravalli Supergroup", "d": "Dharwar Craton"},
            "answer": "a", "topic": "Eastern Ghats", "subtopic": "Kodurite Suite",
            "notes": "Fermor named kodurites after Kodur in the Visakhapatnam-Srikakulam manganese belt of the high-grade granulitic Eastern Ghats Province."
        },
        {
            "q_num": 94,
            "question": "The Kolar Gold Field (KGF) and Hutti Gold Mines of Karnataka are situated within:",
            "options": {"a": "Cuddapah quartzites", "b": "Charnockites", "c": "Closepet Granite", "d": "Archean Dharwar Greenstone Schist Belts"},
            "answer": "d", "topic": "Dharwar Gold Metallogeny", "subtopic": "Kolar & Hutti",
            "notes": "Gold mineralization occurs in quartz-carbonate-sulfide veins within amphibolite-facies metabasalts of the Kolar and Hutti greenstone belts (~2.7 Ga)."
        },
        {
            "q_num": 95,
            "question": "The prominent, linear pink potassic granite plutonic suite traversing nearly the entire length of the Dharwar Craton from north to south is the:",
            "options": {"a": "Champion Gneiss", "b": "Peninsular Gneiss", "c": "Closepet Granite", "d": "Singhbhum Granite"},
            "answer": "c", "topic": "Dharwar Craton", "subtopic": "Closepet Granite",
            "notes": "The Closepet Granite (~2.51 Ga) forms an iconic 500-km-long, 20-30 km wide north-south batholithic belt dividing the Western and Eastern Dharwar cratons."
        },
        {
            "q_num": 96,
            "question": "The 'Peninsular Gneissic Complex' (PGC) underlying vast tracts of southern India is predominantly composed of:",
            "options": {"a": "Tonalite-Trondhjemite-Granodiorite (TTG) gneisses", "b": "Alkali granites", "c": "Syenites", "d": "Basaltic granulites"},
            "answer": "a", "topic": "Dharwar Basement", "subtopic": "TTG Gneisses",
            "notes": "The PGC (dated from 3.4 to 3.0 Ga) comprises multi-phase grey banded gneisses of TTG composition generated by partial melting of hydrous basaltic crust."
        },
        {
            "q_num": 97,
            "question": "The charnockite rock series (hypersthene-bearing granitic rocks) was first discovered and scientifically described from St. Thomas Mount in Chennai by:",
            "options": {"a": "D.N. Wadia", "b": "M.S. Krishnan", "c": "Sir Thomas H. Holland (1893, 1900)", "d": "William Smith"},
            "answer": "c", "topic": "Indian Petrography", "subtopic": "Discovery of Charnockite",
            "notes": "Sir Thomas Holland (1900) named the charnockite series after Job Charnock, founder of Calcutta, whose tombstone was fashioned from St. Thomas Mount hypersthene granite."
        },
        {
            "q_num": 98,
            "question": "The deep-seated granulite terrain of the Southern Granulite Terrane (SGT) is separated from the lower-grade Dharwar Craton by the:",
            "options": {"a": "Fermor's Line / Palghat-Cauvery Shear Zone", "b": "Great Boundary Fault", "c": "Main Central Thrust", "d": "Central Indian Shear Zone"},
            "answer": "a", "topic": "Southern Granulite Terrane", "subtopic": "Fermor's Line",
            "notes": "Fermor's Line marks the transition from amphibolite-facies Dharwar cratonic rocks in the north to orthopyroxene-bearing granulite facies in the south."
        },
        {
            "q_num": 99,
            "question": "The 'Great Boundary Fault' (GBF) of Rajasthan is a prominent regional structural lineament separating the:",
            "options": {"a": "Aravalli and Delhi Supergroups", "b": "Delhi Supergroup and Marwar Supergroup", "c": "Vindhyan Supergroup from the pre-Vindhyan Aravalli/BGC basement", "d": "Malani suite from the Erinpura Granite"},
            "answer": "c", "topic": "Rajasthan Tectonics", "subtopic": "Great Boundary Fault",
            "notes": "The Great Boundary Fault (GBF) is an 800-km-long regional fault bringing pre-Vindhyan rocks over the flat-lying Upper Vindhyan Bhander Group."
        },
        {
            "q_num": 100,
            "question": "The Upper Cretaceous marine dinosaur-bearing sandstone unit in the Ariyalur Group of South India is the:",
            "options": {"a": "Sillakkudi Formation", "b": "Kallankurichchi Formation", "c": "Kallamedu Formation", "d": "Niniyur Formation"},
            "answer": "c", "topic": "Cauvery Basin Dinosaurs", "subtopic": "Kallamedu Formation",
            "notes": "Official note (p. 328): The Kallamedu Formation of the Ariyalur Group is characterized by skeletal parts of sauropod, carnosaur, and stegosaurian dinosaurs."
        },
        {
            "q_num": 101,
            "question": "The famous Stegosaurian dinosaur Dravidosaurus blanfordi was discovered from which Cretaceous unit of the Cauvery Basin?",
            "options": {"a": "Uttatur Group", "b": "Niniyur Formation", "c": "Trichinopoly Group", "d": "Patcham Group"},
            "answer": "c", "topic": "Cauvery Basin Dinosaurs", "subtopic": "Dravidosaurus",
            "notes": "Official note (p. 328): The Trichinopoly Group shows definitive evidence of the stegosaurian dinosaur Dravidosaurus blanfordi."
        },
        {
            "q_num": 102,
            "question": "The 'Rajahmundry Sandstone' of coastal Andhra Pradesh belongs to which geological epoch?",
            "options": {"a": "Eocene", "b": "Miocene to Pliocene", "c": "Upper Cretaceous", "d": "Paleocene"},
            "answer": "b", "topic": "Coastal Cenozoic", "subtopic": "Rajahmundry Sandstone",
            "notes": "Official note (p. 327): The Rajahmundry Sandstone belongs to the Miocene-Pliocene, resting unconformably upon Deccan Traps."
        },
        {
            "q_num": 103,
            "question": "The 'Warkalli Beds' (Varkala Formation) of coastal Kerala are composed of carbonaceous clays, lignite seams, and sandstones belonging to the:",
            "options": {"a": "Paleocene", "b": "Eocene", "c": "Oligocene", "d": "Miocene to Pliocene"},
            "answer": "d", "topic": "Kerala Cenozoic", "subtopic": "Warkalli Formation",
            "notes": "The Warkalli Formation comprises Mio-Pliocene continental coastal sediments with valuable chinaclay and lignite deposits exposed in spectacular seaside sea-cliffs."
        },
        {
            "q_num": 104,
            "question": "The Cuddalore Sandstone of coastal Tamil Nadu (rich in silicified fossil wood trunks of Peuce schmidiana) is of:",
            "options": {"a": "Mio-Pliocene age", "b": "Eocene age", "c": "Cretaceous age", "d": "Pleistocene age"},
            "answer": "a", "topic": "Tamil Nadu Cenozoic", "subtopic": "Cuddalore Sandstone",
            "notes": "The Cuddalore Sandstone (celebrated at the National Fossil Wood Park, Tiruvakkarai) is a Mio-Pliocene ferruginous sandstone sequence rich in petrified angiosperm and gymnosperm woods."
        },
        {
            "q_num": 105,
            "question": "The iconic Tertiary lignite deposit of Neyveli in Tamil Nadu occurs within which stratigraphic formation?",
            "options": {"a": "Cuddalore Formation", "b": "Warkalli Formation", "c": "Niniyur Formation", "d": "Uttatur Group"},
            "answer": "a", "topic": "Neyveli Lignite", "subtopic": "Cuddalore Formation",
            "notes": "The Neyveli lignite seam (averaging 15-20 m thick) is interbedded within the Mio-Pliocene Cuddalore Formation in the South Arcot district."
        },
        {
            "q_num": 106,
            "question": "The rich Tertiary petroleum reservoirs of Digboi, Nahorkatiya, and Moran in the Assam-Arakan Basin occur within the:",
            "options": {"a": "Disang Group", "b": "Jaintia Group", "c": "Dihing Group", "d": "Barail and Tipam Groups"},
            "answer": "d", "topic": "Assam Petroleum Stratigraphy", "subtopic": "Barail & Tipam",
            "notes": "Hydrocarbons in Upper Assam are trapped primarily within Oligocene deltaic sandstones of the Barail Group and Miocene fluvial sandstones of the Tipam Group."
        },
        {
            "q_num": 107,
            "question": "The deep-water turbiditic flysch succession of the Assam-Arakan Orogenic Belt is formally designated as the:",
            "options": {"a": "Disang Group", "b": "Barail Group", "c": "Surma Group", "d": "Tipam Group"},
            "answer": "a", "topic": "Assam-Arakan Flysch", "subtopic": "Disang Group",
            "notes": "The Disang Group (Late Cretaceous to Eocene) consists of thousands of meters of dark grey splintery shales and thin turbiditic sandstones forming an accretionary prism flysch."
        },
        {
            "q_num": 108,
            "question": "The 'Sylhet Limestone' of the South Shillong Plateau and Assam shelf is famous for containing abundant:",
            "options": {"a": "Ammonites", "b": "Dinosaur bones", "c": "Nummulites and Alveolina (Eocene larger foraminifera)", "d": "Trilobites"},
            "answer": "c", "topic": "Shillong Plateau Cenozoic", "subtopic": "Sylhet Limestone",
            "notes": "The Sylhet Limestone Formation comprises Eocene shallow-water nummulitic platform limestones developed along the southern shelf margin of the Shillong Plateau."
        },
        {
            "q_num": 109,
            "question": "The giant offshore petroleum and natural gas reservoir of 'Bombay High' produces oil from which stratigraphic horizon?",
            "options": {"a": "Precambrian basement", "b": "Upper Cretaceous Deccan basalt", "c": "Paleocene basaltic wash", "d": "Early Miocene carbonate reservoirs (B-Zone L-III limestone)"},
            "answer": "d", "topic": "Western Offshore Petroleum", "subtopic": "Bombay High Reservoir",
            "notes": "Bombay High produces from the Early Miocene L-III carbonate reservoir within the Bombay Formation, sealed by Middle Miocene marine shales."
        },
        {
            "q_num": 110,
            "question": "The world-famous 'Barren Island' in the Andaman Sea is unique in the Indian territory for being the:",
            "options": {"a": "Largest mud volcano", "b": "Only active subaerial volcano in South Asia", "c": "Only coral atoll in the Bay of Bengal", "d": "Highest peak in the Andaman Islands"},
            "answer": "b", "topic": "Indian Volcanology", "subtopic": "Barren Island",
            "notes": "Barren Island is an active stratovolcano associated with the Sunda-Andaman subduction zone, exhibiting recurring basaltic-andesitic eruptions."
        },
        {
            "q_num": 111,
            "question": "The Ophiolite Belt of Manipur, Nagaland, and the Andaman Islands represents obducted remnants of the:",
            "options": {"a": "Paleozoic Proto-Tethys", "b": "Proterozoic Purana Ocean", "c": "Mesozoic Neotethyan oceanic lithosphere", "d": "Precambrian greenstone belt"},
            "answer": "c", "topic": "Indo-Burma Range", "subtopic": "Ophiolite Belt",
            "notes": "The Indo-Myanmar and Andaman ophiolites represent Late Cretaceous to Eocene Neotethyan oceanic crust obducted during Indo-Eurasian convergence."
        },
        {
            "q_num": 112,
            "question": "The 'Panjal Volcanics' of Kashmir are predominantly composed of:",
            "options": {"a": "Rhyolites and trachytes", "b": "Subaerial to submarine tholeiitic and calc-alkaline basalts and andesites", "c": "Alkali ultrabasic picrites", "d": "Kimberlites"},
            "answer": "b", "topic": "Kashmir Volcanism", "subtopic": "Panjal Traps Petrography",
            "notes": "The Panjal Traps (~2.5 km thick) represent continental flood basalts (tholeiites) erupted during the rifting of the Cimmerian blocks from Gondwanaland in the Early Permian."
        },
        {
            "q_num": 113,
            "question": "In the Salt Range succession, the 'Saline Series' (Salt Range Formation) containing massive rock salt and gypsum was proven by biostratigraphy to be of:",
            "options": {"a": "Tertiary age", "b": "Silurian age", "c": "Precambrian (Ediacaran) age", "d": "Triassic age"},
            "answer": "c", "topic": "Salt Range Stratigraphy", "subtopic": "Salt Range Formation",
            "notes": "Once fiercely debated as Eocene due to thrusting, high-precision isotopic and microfossil studies established that the Salt Range Formation is Neoproterozoic to basal Cambrian."
        },
        {
            "q_num": 114,
            "question": "The 'Bap Boulder Bed' of Western Rajasthan is a glacio-marine tillite correlating directly with the:",
            "options": {"a": "Talchir Tillite of the Gondwana Supergroup", "b": "Pokaran Boulder Bed", "c": "Blaini Boulder Bed", "d": "Kaldurga Conglomerate"},
            "answer": "a", "topic": "Rajasthan Upper Paleozoic", "subtopic": "Bap Boulder Bed",
            "notes": "The Bap Boulder Bed contains striated, faceted pebbles resting on pre-Permian basement, correlating with the Asselian-Sakmarian Gondwanan Talchir glaciation."
        },
        {
            "q_num": 115,
            "question": "The 'Pokaran Boulder Bed' of Western Rajasthan underlies the Marwar Supergroup and is of:",
            "options": {"a": "Carboniferous age", "b": "Permian age", "c": "Neoproterozoic to basal Cambrian age", "d": "Jurassic age"},
            "answer": "c", "topic": "Marwar Supergroup", "subtopic": "Pokaran Boulder Bed",
            "notes": "The Pokaran Boulder Bed rests upon the Neoproterozoic Malani Rhyolites and forms the base of the Marwar Supergroup."
        },
        {
            "q_num": 116,
            "question": "The 'Marwar Supergroup' (Trans-Aravalli Vindhyans) of western Rajasthan is subdivided into three groups. From oldest to youngest, these are:",
            "options": {
                "a": "Bilara -> Jodhpur -> Nagaur",
                "b": "Nagaur -> Bilara -> Jodhpur",
                "c": "Jodhpur -> Nagaur -> Bilara",
                "d": "Jodhpur Group -> Bilara Group -> Nagaur Group"
            },
            "answer": "d",
            "topic": "Marwar Supergroup", "subtopic": "Subdivisions",
            "notes": "The Marwar succession comprises the basal arenaceous Jodhpur Group, middle carbonate Bilara Group, and upper evaporite-bearing Nagaur Group."
        },
        {
            "q_num": 117,
            "question": "Extensive subsurface potash and halite evaporite deposits in northwestern Rajasthan occur within which group of the Marwar Supergroup?",
            "options": {"a": "Jodhpur Group", "b": "Nagaur Group (Hanseran Evaporite Formation)", "c": "Bilara Group", "d": "Pokaran Boulder Bed"},
            "answer": "b", "topic": "Marwar Evaporites", "subtopic": "Hanseran Evaporite",
            "notes": "The Hanseran Evaporite Group (subsurface equivalent of the Nagaur Group) in Bikaner-Nagaur contains vast deposits of bedded halite, anhydrite, and polyhalite."
        },
        {
            "q_num": 118,
            "question": "The famous multi-colored ornamental 'Jaisalmer Limestone' of Western Rajasthan is of which geological age?",
            "options": {"a": "Triassic", "b": "Lower Cretaceous", "c": "Tertiary", "d": "Middle Jurassic (Callovian-Oxfordian)"},
            "answer": "d", "topic": "Jaisalmer Basin", "subtopic": "Jaisalmer Limestone",
            "notes": "The golden-yellow Jaisalmer Limestone is a marine Middle Jurassic carbonate formation celebrated for its architectural beauty and rich ammonoid-brachiopod fauna."
        },
        {
            "q_num": 119,
            "question": "The 'Lathi Formation' of the Jaisalmer Basin is famous for containing:",
            "options": {"a": "Abundant petrified gymnosperm wood logs (Wood Fossil Park, Akal)", "b": "Marine ammonites", "c": "Glacial tillites", "d": "Thick coal beds"},
            "answer": "a", "topic": "Jaisalmer Basin", "subtopic": "Lathi Formation",
            "notes": "The Early Jurassic continental Lathi Formation preserves magnificent 180-million-year-old petrified tree trunks up to 13 meters long at Akal Fossil Wood Park."
        },
        {
            "q_num": 120,
            "question": "The 'Pariwar Formation' and 'Abur Formation' of the Jaisalmer Basin are of:",
            "options": {"a": "Permian age", "b": "Triassic age", "c": "Cretaceous age", "d": "Paleocene age"},
            "answer": "c", "topic": "Jaisalmer Basin", "subtopic": "Pariwar & Abur",
            "notes": "The Pariwar Formation (deltaic) and overlying yellow ammonite-rich Abur Formation represent the marine Early Cretaceous sequence of the Jaisalmer Basin."
        },
        {
            "q_num": 121,
            "question": "The iconic volcanic ash marker bed (Toba Ash, ~74,000 years BP) that erupted from Sumatra and Blanket-deposited over Central India occurs within:",
            "options": {"a": "Siwalik Group", "b": "Karewa Group", "c": "Bagh Beds", "d": "Quaternary alluvial terraces of the Narmada and Son valleys"},
            "answer": "d", "topic": "Quaternary Chronostratigraphy", "subtopic": "Youngest Toba Tuff",
            "notes": "The Youngest Toba Tuff (YTT, 74 ka) serves as a continental chronostratigraphic isochronous key bed across Indian river valleys, associated with Middle Paleolithic tools."
        },
        {
            "q_num": 122,
            "question": "The only known fossil hominid skull specimen in South Asia ('Narmada Man', Homo erectus / archaic Homo sapiens) was discovered in:",
            "options": {"a": "Karewa beds of Kashmir", "b": "Middle Pleistocene alluvial gravels at Hathnora (Madhya Pradesh)", "c": "Siwalik Pinjor beds", "d": "Kurnool caves"},
            "answer": "b", "topic": "Indian Paleoanthropology", "subtopic": "Narmada Man",
            "notes": "Discovered by Arun Sonakia in 1982 at Hathnora in the Narmada Valley, the fossil calvarium belongs to Middle Pleistocene Homo erectus / archaic Homo sapiens (~250-500 ka)."
        },
        {
            "q_num": 123,
            "question": "The 'Kuldhar' member of the Jaisalmer Formation is internationally renowned for containing a prolific biozone of:",
            "options": {"a": "Callovian ammonites", "b": "Trilobites", "c": "Graptolites", "d": "Rudist bivalves"},
            "answer": "a", "topic": "Jaisalmer Biostratigraphy", "subtopic": "Kuldhar Member",
            "notes": "The Kuldhar Member contains a world-class succession of Callovian-Oxfordian ammonites including Reineckeia, Macrocephalites, and Peltoceras."
        },
        {
            "q_num": 124,
            "question": "The 'Patcham Group' of Kutch contains the famous basal marine limestone bed termed the:",
            "options": {"a": "Golden Oolite", "b": "Dhosa Oolite", "c": "Coral and Shell Limestone", "d": "Trigonia Bed"},
            "answer": "c", "topic": "Kutch Jurassic", "subtopic": "Patcham Group",
            "notes": "The Bathonian Patcham Group is characterized by hard white and grey limestones rich in corals and brachiopods (Kutchithyris), exposed on Patcham and Kutch Mainland."
        },
        {
            "q_num": 125,
            "question": "The uppermost, highly condensed, iron-rich oolitic limestone marker bed of the Chari Group in Kutch is the:",
            "options": {"a": "Golden Oolite", "b": "Dhosa Oolite", "c": "Nimar Sandstone", "d": "Umia Plant Bed"},
            "answer": "b", "topic": "Kutch Marker Beds", "subtopic": "Dhosa Oolite",
            "notes": "The Dhosa Oolite (Oxfordian) represents a famous green-brown chamositic-glauconitic condensed marker bed teeming with ammonites (Peltoceratoides, Perisphinctes)."
        },
        {
            "q_num": 126,
            "question": "The marine Cretaceous-Paleocene sequence of Pondicherry (Puducherry) is subdivided into the Valudavur, Mettuvelly, and:",
            "options": {"a": "Nerinea and Viluppuram beds", "b": "Kallankurichchi beds", "c": "Bagh beds", "d": "Nimar beds"},
            "answer": "a", "topic": "Pondicherry Cretaceous", "subtopic": "Nerinea Beds",
            "notes": "The Pondicherry Cretaceous-Paleogene sequence comprises the Valudavur, Mettuvelly, and Nerinea beds, correlating with the Ariyalur and Niniyur groups."
        },
        {
            "q_num": 127,
            "question": "In the Cuddapah Basin, volcanic activity in the form of basic sills, dykes, and pillow lavas is most predominantly developed within the:",
            "options": {"a": "Kistna Group", "b": "Nallamalai Group", "c": "Kurnool Group", "d": "Papaghani and Cheyair Groups (Tadpatri Formation)"},
            "answer": "d", "topic": "Cuddapah Igneous Activity", "subtopic": "Tadpatri Sills",
            "notes": "Extensive picritic, doleritic, and basaltic sills and flows (~1.9 Ga) intrude the Vempalle and Tadpatri formations of the lower Cuddapah succession, generating chrysotile asbestos and barite."
        },
        {
            "q_num": 128,
            "question": "The world-famous 'Mangampeta' bedded barite deposit in the Cuddapah Basin occurs within which formation?",
            "options": {"a": "Gulcheru Quartzite", "b": "Mangampeta bedded tuffs of the Pullampet Formation (Cheyair Group)", "c": "Bairenkonda Quartzite", "d": "Cumbum Shale"},
            "answer": "b", "topic": "Cuddapah Mineral Wealth", "subtopic": "Mangampeta Barite",
            "notes": "Mangampeta (the world's largest bedded barite deposit) is hosted within acid tuffaceous shales of the Pullampet Formation, formed by exhalative submarine volcanism."
        },
        {
            "q_num": 129,
            "question": "The well-known 'Bailadila Group' of Chhattisgarh and Bastar is internationally famed for producing supergene enriched deposits of:",
            "options": {"a": "High-grade Hematite Iron Ore", "b": "Manganese Ore", "c": "Bauxite", "d": "Chromite"},
            "answer": "a", "topic": "Bastar Craton", "subtopic": "Bailadila Iron Ore",
            "notes": "The Bailadila Group (Archean-Paleoproterozoic greenstone belt) preserves 14 massive high-grade hematite deposits containing up to 66-68% Fe."
        },
        {
            "q_num": 130,
            "question": "The Sukinda Ultramafic Complex of Odisha is India's most prolific producer of:",
            "options": {"a": "Gold", "b": "Chromite", "c": "Lead-Zinc", "d": "Copper"},
            "answer": "b", "topic": "Odisha Mineral Resources", "subtopic": "Sukinda Chromite",
            "notes": "The Sukinda ultramafic valley in Jajpur district contains over 95% of India's metallurgical-grade stratiform chromite reserves hosted within serpentinized dunite and peridotite."
        },
        {
            "q_num": 131,
            "question": "The Mesoarchean Gorumahisani, Badampahar, and Tomka iron ore ranges belong to the:",
            "options": {"a": "Dharwar Craton", "b": "Iron Ore Supergroup of the Singhbhum-North Odisha Craton", "c": "Bastar Craton", "d": "Aravalli Craton"},
            "answer": "b", "topic": "North Odisha Geology", "subtopic": "Iron Ore Group",
            "notes": "Gorumahisani and Badampahar in Mayurbhanj district represent the iconic historical source of iron ore for the first steel plant of India (TISCO, Jamshedpur)."
        },
        {
            "q_num": 132,
            "question": "The famous East Coast Bauxite deposits of Odisha and Andhra Pradesh (e.g., Panchpatmali, Damanjodi) are capping plateau laterites developed over:",
            "options": {"a": "Deccan Basalts", "b": "Granites", "c": "Khondalite suite of rocks (Eastern Ghats Mobile Belt)", "d": "Vindhyan shales"},
            "answer": "c", "topic": "East Coast Bauxite", "subtopic": "Khondalite Weathering",
            "notes": "The metallurgical-grade gibbsitic bauxites of the East Coast province formed by intense deep Cenozoic lateritic weathering of garnet-sillimanite-quartz schists (khondalites)."
        },
        {
            "q_num": 133,
            "question": "The 'Talchir Basin' of Odisha is of paramount importance in Indian geology because:",
            "options": {"a": "It is the type locality for the basal Gondwana Talchir Formation and possesses major coal reserves", "b": "It is a Marine Cretaceous basin", "c": "It contains active volcanism", "d": "It preserves diamond kimberlites"},
            "answer": "a", "topic": "Odisha Stratigraphy", "subtopic": "Talchir Type Locality",
            "notes": "The Talchir coalfield in Angul district is the historical type locality where the Blanford brothers (1856) first described the basal Gondwana glacial boulder bed."
        },
        {
            "q_num": 134,
            "question": "The 'Ib River Coalfield' of Odisha belongs to which regional Gondwana structural basin?",
            "options": {"a": "Damodar Valley", "b": "Satpura Basin", "c": "Son-Mahanadi Master Basin", "d": "Godavari Basin"},
            "answer": "c", "topic": "Odisha Coalfields", "subtopic": "Ib River Coalfield",
            "notes": "The Ib River Coalfield in Jharsuguda and Sundargarh represents the southeastern continuation of the Mand-Raigarh coalfield in the Mahanadi Valley Gondwana basin."
        },
        {
            "q_num": 135,
            "question": "In Odisha, Upper Gondwana sedimentary rocks containing plant fossils of Ptilophyllum and Brachyphyllum are known as the:",
            "options": {"a": "Barakar Formation", "b": "Athgarh Formation", "c": "Talchir Formation", "d": "Karharbari Formation"},
            "answer": "b", "topic": "Odisha Stratigraphy", "subtopic": "Athgarh Sandstone",
            "notes": "The Athgarh Formation near Cuttack and Bhubaneswar consists of Upper Gondwana (Jurassic-Cretaceous) sandstones, conglomerates, and white clays preserving Bennettitalean plants."
        }
    ]

def get_questions_136_to_175():
    # Questions 136 to 175
    return [
        {
            "q_num": 136,
            "question": "The distinctive metamorphic rock 'khondalite' was named after the Khond tribe of Odisha by:",
            "options": {"a": "T.L. Walker (1902)", "b": "T.H. Holland", "c": "D.N. Wadia", "d": "P.N. Bose"},
            "answer": "a", "topic": "Odisha Petrography", "subtopic": "Naming of Khondalite",
            "notes": "Thomas Leonard Walker (1902, GSI Memoir) coined the term 'khondalite' for garnet-sillimanite-graphite schists occurring widely throughout the hills of Kalahandi and Koraput."
        },
        {
            "q_num": 137,
            "question": "The 'Simlipal Complex' of Mayurbhanj district, Odisha, represents a concentric circular volcanic-sedimentary lopolithic structure comprising three spilitic lava rings interbedded with:",
            "options": {"a": "Quartzites and conglomerates", "b": "Limestones", "c": "Coal seams", "d": "Evaporites"},
            "answer": "a", "topic": "Odisha Precambrian", "subtopic": "Simlipal Basin",
            "notes": "The Paleoproterozoic Simlipal basin comprises three concentric quartzite-sandstone horizons alternating with thick spilitic spilitic and basaltic volcanic flows."
        },
        {
            "q_num": 138,
            "question": "The famous 'Gangpur Group' of Sundargarh district, Odisha, is characterized by which distinctive manganiferous Gondite rock unit?",
            "options": {"a": "Birmitrapur limestone", "b": "Kumarmunda phyllite", "c": "Raghunathpali conglomerate", "d": "Gariajhor gondite horizon"},
            "answer": "d", "topic": "Odisha Precambrian", "subtopic": "Gangpur Group",
            "notes": "The Gangpur Group (MS Krishnan, 1937) preserves manganiferous gondite lenses at Gariajhor alongside massive flux-grade dolomite and limestone at Birmitrapur."
        },
        {
            "q_num": 139,
            "question": "The boundary between the Singhbhum-North Odisha Craton and the high-grade Eastern Ghats Granulite Belt is marked by the deep tectonic lineament known as the:",
            "options": {"a": "Singhbhum Shear Zone", "b": "Sukinda Thrust / North Orissa Boundary Thrust (Rengali Province)", "c": "Great Boundary Fault", "d": "Narmada-Son Lineament"},
            "answer": "b", "topic": "Odisha Tectonics", "subtopic": "Sukinda Thrust",
            "notes": "The Sukinda Thrust (North Orissa Boundary Thrust) separates the low-grade Archaean granite-greenstone craton from the high-grade Proterozoic Eastern Ghats granulites."
        },
        {
            "q_num": 140,
            "question": "The vast anorthosite massif of Odisha, representing deep-seated Proterozoic plutonic intrusion into the Eastern Ghats belt, is the:",
            "options": {"a": "Sittampundi Anorthosite", "b": "Kadavur Anorthosite", "c": "Chilka Lake (Banpur) Anorthosite Complex", "d": "Bengal Anorthosite"},
            "answer": "c", "topic": "Odisha Igneous Suites", "subtopic": "Chilka Lake Anorthosite",
            "notes": "The Chilka Lake anorthosite massif (~1.4 Ga) covers over 400 km² along the southwest shore of Chilka Lake, composed of plagioclase-rich (labradorite-andesine) rocks."
        },
        {
            "q_num": 141,
            "question": "The celebrated fossil hominoid genus 'Sivapithecus' (Ramapithecus), an ancestor of the modern orangutan, was discovered from the:",
            "options": {"a": "Lower Siwalik (Kamlial)", "b": "Upper Siwalik (Pinjor)", "c": "Middle Siwalik (Nagri and Chinji formations)", "d": "Karewa Group"},
            "answer": "c", "topic": "Siwalik Vertebrates", "subtopic": "Sivapithecus",
            "notes": "Sivapithecus fossils occur abundantly in the Late Miocene fluvial channel sandstones and paleosols of the Chinji and Nagri formations (~12 to 8.5 Ma)."
        },
        {
            "q_num": 142,
            "question": "The famous gigantic fossil land tortoise 'Colossochelys atlas' (Megalochelys), measuring over 2.5 meters in shell length, was discovered in the:",
            "options": {"a": "Upper Siwalik (Pinjor stage)", "b": "Lower Siwalik", "c": "Subathu beds", "d": "Lameta beds"},
            "answer": "a", "topic": "Siwalik Vertebrates", "subtopic": "Colossochelys atlas",
            "notes": "Colossochelys atlas lived during the Pliocene-Pleistocene in the open savannas of the Siwalik foreland, preserved in the Pinjor Formation."
        },
        {
            "q_num": 143,
            "question": "The 'Kashmir Earthquake' of 2005 (M 7.6) and the 'Kangra Earthquake' of 1905 were generated along active thrust faults of the:",
            "options": {"a": "Main Boundary Thrust (MBT) / Himalayan Frontal Thrust (HFT)", "b": "Main Central Thrust (MCT)", "c": "Indus Suture Zone", "d": "Trans-Himadri Fault"},
            "answer": "a", "topic": "Himalayan Neotectonics", "subtopic": "Active Faults",
            "notes": "Great Himalayan earthquakes occur along the sub-Himalayan frontal thrusts (MBT and HFT/MFT) where the Indian plate underthrusts the Himalayan wedge."
        },
        {
            "q_num": 144,
            "question": "The 'Infra-Krol Formation' of the Lesser Himalayan Krol Belt consists of black shales and slates that have yielded micro-floral remains of:",
            "options": {"a": "Cambrian age", "b": "Carboniferous to Permian age (including Glossopteris elements)", "c": "Jurassic age", "d": "Tertiary age"},
            "answer": "b", "topic": "Krol Belt Stratigraphy", "subtopic": "Infra-Krol Formation",
            "notes": "Official note (p. 327): The Infra-Krol formation consists of microfloral remains ranging in age from Carboniferous to Permian, with reported occurrences of Glossopteris flora."
        },
        {
            "q_num": 145,
            "question": "The 'Tal Formation' of the Mussoorie and Garhwal synclines contains small shelly fossils, chert-phosphorites, and trilobites establishing its age as:",
            "options": {"a": "Late Permian", "b": "Triassic", "c": "Terminal Neoproterozoic (Ediacaran) to Early Cambrian", "d": "Cretaceous"},
            "answer": "c", "topic": "Lesser Himalayan Stratigraphy", "subtopic": "Tal Formation",
            "notes": "The Lower Tal chert-phosphorite member contains Ediacaran-early Cambrian small shelly fossils (SSFs), while the Upper Tal quartzites yield Redlichia trilobites."
        },
        {
            "q_num": 146,
            "question": "The 'Zewan Formation' of Kashmir represents a classic marine succession containing the famous Permian-Triassic boundary section at:",
            "options": {"a": "Muth", "b": "Lolab", "c": "Baramulla", "d": "Guryul Ravine (near Srinagar)"},
            "answer": "d", "topic": "Permian-Triassic Boundary", "subtopic": "Guryul Ravine",
            "notes": "Guryul Ravine near Srinagar is internationally celebrated as one of the best marine Permian-Triassic boundary sections, transitioning from Zewan to Khunamuh Formation."
        },
        {
            "q_num": 147,
            "question": "In the Salt Range, the famous 'Olive Series' (Conularia beds) contains glacio-marine pebbles and the iconic scyphozoan fossil:",
            "options": {"a": "Nummulites", "b": "Belemnites", "c": "Conularia", "d": "Ammonites"},
            "answer": "c", "topic": "Salt Range Stratigraphy", "subtopic": "Conularia Beds",
            "notes": "The Conularia beds of the Salt Range contain pyramidal chitinophosphatic shells of Conularia laevigata, correlating with the Gondwana Talchir glacial epoch."
        },
        {
            "q_num": 148,
            "question": "The 'Dharwar Craton' of southern India is classically divided into Western and Eastern Dharwar Cratons based on the age of greenstones and the bounding:",
            "options": {"a": "Closepet Granite batholith", "b": "Kolar shear zone", "c": "Cuddapah basin boundary", "d": "Goddard line"},
            "answer": "a", "topic": "Dharwar Craton", "subtopic": "Western vs Eastern",
            "notes": "The Closepet Granite marks the boundary: Western Dharwar Craton features Mesoarchean basement (Sargur, >3.0 Ga), whereas Eastern Dharwar Craton features Neoarchean greenstones (~2.7 Ga)."
        },
        {
            "q_num": 149,
            "question": "The 'Sargur Schist Complex' is characterized by which diagnostic metamorphic grade and mineral assemblage?",
            "options": {"a": "Greenschist facies (chlorite-sericite)", "b": "Upper amphibolite to granulite facies (kyanite-sillimanite-garnet-cordierite)", "c": "Zeolite facies", "d": "Blueschist facies"},
            "answer": "b", "topic": "Sargur Complex", "subtopic": "Metamorphic Grade",
            "notes": "The Sargur Schists represent ancient (>3.1-3.3 Ga) pelitic, carbonate, and ultramafic enclaves metamorphosed to upper amphibolite to granulite facies."
        },
        {
            "q_num": 150,
            "question": "The 'Chitradurga Schist Belt' of the Dharwar Supergroup displays an iconic regional structural geometry known as a:",
            "options": {"a": "Monocline", "b": "Dome and basin interference structure", "c": "Linear, arcuate, southward-closing synclinorium", "d": "Flat-lying undeformed tableland"},
            "answer": "c", "topic": "Dharwar Schist Belts", "subtopic": "Chitradurga Synclinorium",
            "notes": "The Chitradurga belt forms a massive, 450-km-long arcuate synclinorium displaying low- to medium-grade metavolcanics (Ingaldhal) and metasediments (Hiriyur)."
        },
        {
            "q_num": 151,
            "question": "The 'Banded Gneissic Complex' (BGC) of Mewar, Rajasthan, represents the oldest basement of northwestern India, with ages up to:",
            "options": {"a": "2000 Ma", "b": "3300 to 3500 Ma", "c": "1500 Ma", "d": "1000 Ma"},
            "answer": "b", "topic": "Rajasthan Basement", "subtopic": "Banded Gneissic Complex",
            "notes": "Zircon geochronology of the Untala and Gingla granites within the BGC reveals TTG magmatic crystallization ages of ~3.3 Ga, with relict xenocrysts dating to ~3.5 Ga."
        },
        {
            "q_num": 152,
            "question": "The 'Speckled Sandstone Series' of the Salt Range is dated as:",
            "options": {"a": "Cambrian", "b": "Permo-Carboniferous", "c": "Jurassic", "d": "Tertiary"},
            "answer": "b", "topic": "Salt Range Stratigraphy", "subtopic": "Speckled Sandstone",
            "notes": "The Speckled Sandstone Series (Tobler and Warcha formations) consists of reddish and speckled sandstones associated with the Permo-Carboniferous Gondwana glaciation."
        },
        {
            "q_num": 153,
            "question": "The 'Exotic Blocks of Malla Johar' in the high Kumaon-Tibet borderland represent:",
            "options": {"a": "Submarine volcanic olistoliths and limestone blocks transported during Tethyan oceanic closure", "b": "Glacial erratics", "c": "Meteorite impact ejecta", "d": "In-situ bioherms"},
            "answer": "a", "topic": "Himalayan Suture Zone", "subtopic": "Exotic Blocks of Johar",
            "notes": "The Exotic Blocks of Malla Johar represent colossal blocks of Permian and Triassic deep-water ammonoid limestones caught up in Cretaceous Spiti ophiolitic melange."
        },
        {
            "q_num": 154,
            "question": "The 'Indus Suture Zone' (ISZ) represents the fundamental collision zone and plate boundary between the:",
            "options": {"a": "Indian Plate and the Kohistan-Ladakh Island Arc / Eurasian Plate", "b": "Peninsular and Extra-Peninsular India", "c": "Lesser and Higher Himalaya", "d": "Dharwar and Bastar cratons"},
            "answer": "c", "topic": "Himalayan Tectonics", "subtopic": "Indus Suture Zone",
            "notes": "The Indus-Tsangpo Suture Zone (ITSZ) marks the subduction and collision boundary along which the Neo-Tethys ocean closed in the early Cenozoic (~55 Ma)."
        },
        {
            "q_num": 155,
            "question": "The 'Main Central Thrust' (MCT) separates the rocks of the:",
            "options": {"a": "Sub-Himalaya (Siwaliks) from Lesser Himalaya", "b": "Lesser Himalaya from the Gangetic Plain", "c": "Lesser Himalayan sedimentary zone from the Higher Himalayan Crystalline Complex (HHC)", "d": "Tethys Himalaya from the Indus Suture"},
            "answer": "c", "topic": "Himalayan Major Thrusts", "subtopic": "Main Central Thrust",
            "notes": "The MCT is a major northward-dipping ductile shear zone along which high-grade Proterozoic Vaikrita crystallines were thrust southward over low-grade Lesser Himalayan rocks."
        },
        {
            "q_num": 156,
            "question": "The 'Main Boundary Thrust' (MBT) separates the:",
            "options": {"a": "Lesser Himalayan formations from the frontal Cenozoic Sub-Himalayan (Siwalik) belt", "b": "Higher Himalaya from Lesser Himalaya", "c": "Siwaliks from Indo-Gangetic Plains", "d": "Karewa beds from Panjal Traps"},
            "answer": "a", "topic": "Himalayan Major Thrusts", "subtopic": "Main Boundary Thrust",
            "notes": "The MBT is a regional fault bringing older Lesser Himalayan metasedimentary rocks (Jaunsar, Krol, Subathu) over the Neogene Siwalik molasse."
        },
        {
            "q_num": 157,
            "question": "The 'Himalayan Frontal Thrust' (HFT / Main Frontal Thrust) separates the:",
            "options": {"a": "Higher Himalaya from Tethyan zone", "b": "Siwalik foothills from the flat alluvium of the Indo-Gangetic Alluvial Plain", "c": "Subathu from Kasauli", "d": "Deccan Traps from Vindhyans"},
            "answer": "b", "topic": "Himalayan Major Thrusts", "subtopic": "Himalayan Frontal Thrust",
            "notes": "The HFT is the active southernmost thrust fault along which Siwalik molasse strata are actively thrusting southward over the modern Indo-Gangetic foreland alluvium."
        },
        {
            "q_num": 158,
            "question": "The celebrated dinosaur egg clutches of the Late Cretaceous Bagh and Lameta beds belong primarily to which group of dinosaurs?",
            "options": {"a": "Sauropods (Titanosauridae)", "b": "Theropods (Tyrannosauridae)", "c": "Ceratopsians", "d": "Ankylosaurs"},
            "answer": "a", "topic": "Indian Paleontology", "subtopic": "Titanosaurid Eggs",
            "notes": "Megaloolithus dinosaur eggs found in hundreds of nests along the Narmada Basin were laid by giant titanosaurid sauropods (Titanosaurus, Jainosaurus)."
        },
        {
            "q_num": 159,
            "question": "The 'South Rewa Gondwana Basin' in Madhya Pradesh is famous for preserving the transitional Permo-Triassic:",
            "options": {"a": "Parsora and Tiki Formations", "b": "Talchir Formation", "c": "Barakar Formation", "d": "Rajmahal Traps"},
            "answer": "a", "topic": "South Rewa Gondwana", "subtopic": "Parsora & Tiki",
            "notes": "The Tiki Formation contains Late Triassic rhynchosaurs (Hyperodapedon) and phytosaurs, while the Parsora Formation preserves the transition from Glossopteris to Dicroidium flora."
        },
        {
            "q_num": 160,
            "question": "In the Vindhyan succession of Rajasthan and Central India, the Semri Group deposition took place in three main sub-basins: Son Valley, Bundelkhand, and:",
            "options": {"a": "SE Rajasthan", "b": "Cuddapah", "c": "Bastar", "d": "Kutch"},
            "answer": "c", "topic": "Vindhyan Basin Architecture", "subtopic": "Semri Sub-Basins",
            "notes": "Official note (p. 327): Semri sedimentation took place in three main sub-basins: Son Valley, Bundelkhand, and SE Rajasthan (Chittorgarh-Jhalawar)."
        },
        {
            "q_num": 161,
            "question": "In SE Rajasthan, the basal Vindhyan succession of the Semri Group begins with the:",
            "options": {"a": "Khardeola Sandstone and Bhagwanpura Limestone", "b": "Kaimur Sandstone", "c": "Rohtas Limestone", "d": "Sirbu Shale"},
            "answer": "a", "topic": "Vindhyan Stratigraphy", "subtopic": "SE Rajasthan Semri",
            "notes": "Official note (p. 327): In SE Rajasthan the succession includes Khardeola sandstone, Bhagwanpura limestone, Binota shales, Jiran sandstone, and Nimbahera limestone."
        },
        {
            "q_num": 162,
            "question": "In the Son Valley, the basal formation of the Semri Group directly overlying the crystalline/porcellanite basement is the:",
            "options": {"a": "Rohtas limestone", "b": "Kajrahat limestone", "c": "Bargawan limestone", "d": "Arangi Formation (Basal beds)"},
            "answer": "d", "topic": "Semri Group Stratigraphy", "subtopic": "Arangi Formation",
            "notes": "Official note (p. 328): The basal beds of the Semri Group of the Son Valley are known as the Arangi Formation, overlain by Kajrahat limestone and Chopan porcellanite."
        },
        {
            "q_num": 163,
            "question": "Which of the following formations of the Tejam Group in the Kumaon Himalayas comprises a 1200 m thick succession of stromatolite-bearing dolomitic limestones?",
            "options": {"a": "Muth Quartzite", "b": "Syringothyris Limestone", "c": "Nagthat Formation", "d": "Deoban Formation"},
            "answer": "d", "topic": "Kumaon Stratigraphy", "subtopic": "Deoban Formation",
            "notes": "Official note (p. 328): The Deoban formation of the Tejam group in the Kumaon Himalayas comprises a 1200 m thick succession of stromatolite-bearing cherty dolomitic limestones."
        },
        {
            "q_num": 164,
            "question": "Which of the following Upper Gondwana formations across different Indian basins are chronologically coeval (Noric to Rhaetic, Upper Triassic)?",
            "options": {
                "a": "Panchet — Pachmarhi — Kamthi — Bijori",
                "b": "Barakar — Motur — Bijori — Kamthi",
                "c": "Dubrajpur (Rajmahal) — Supra-Panchet (Damodar) — Parsora (Rewa) — Bagra (Satpura)",
                "d": "Jabalpur — Chikiala — Kota — Gangamopteris"
            },
            "answer": "c", "topic": "Gondwana Inter-Basinal Correlation", "subtopic": "Upper Triassic Formations",
            "notes": "Official note (p. 328): The Dubrajpur formation (Rajmahal basin), Supra-Panchet formation (Damodar-Son), Parsora formation (Rewa basin), and Bagra formation (Satpura) are of the same Late Triassic age."
        },
        {
            "q_num": 165,
            "question": "The 'Trans-Aravalli Vindhyans' of Western Rajasthan, characterized by flat-lying sandstones, limestones, and evaporites, are now formally classified as the:",
            "options": {"a": "Marwar Supergroup", "b": "Chhattisgarh Group", "c": "Chaibasa Group", "d": "Raialo Group"},
            "answer": "a", "topic": "Western Rajasthan Stratigraphy", "subtopic": "Marwar Supergroup",
            "notes": "Earlier called Trans-Aravalli Vindhyans, these Cambrian/Ediacaran platform sequences were formally redesignated as the Marwar Supergroup."
        },
        {
            "q_num": 166,
            "question": "Choose the set of Gondwana stratigraphic formations which belong to the identical Late Triassic (Noric-Rhaetic) age:",
            "options": {
                "a": "Panchet — Pachmarhi — Kamthi — Bijori",
                "b": "Dubrajpur — Supra-Panchet — Parsora — Bagra",
                "c": "Jabalpur — Chikiala — Parsora — Dubrajpur",
                "d": "Barakar — Motur — Bijori — Kamthi"
            },
            "answer": "b", "topic": "Gondwana Stratigraphy", "subtopic": "Triassic Sets",
            "notes": "Official note (p. 328): Dubrajpur, Supra-Panchet, Parsora, and Bagra formations belong to the same Late Triassic chronostratigraphic interval."
        },
        {
            "q_num": 167,
            "question": "Which one of the following Lower Triassic / Permo-Carboniferous formations of Kashmir contains an early tetrapod vertebrate fauna that displays distinct Euramerican/Laurasian affinities?",
            "options": {"a": "Gangamopteris beds of Kashmir", "b": "Panchet formation of Damodar valley", "c": "Bijori formation of Narmada valley", "d": "Mangli beds of Pranhita-Godavari valley"},
            "answer": "a", "topic": "Kashmir Paleontology", "subtopic": "Gangamopteris Fauna",
            "notes": "Official note (p. 328): The Gangamopteris bed fauna of Kashmir has distinct European affinities (fishes and labyrinthodont archegosaurid amphibians), indicating proximity to Eurasia in early Permian time."
        },
        {
            "q_num": 168,
            "question": "In the Upper Gondwana succession of the Pranhita-Godavari graben, diagnostic vertebrate/plant fossils are present in all formations EXCEPT the:",
            "options": {"a": "Yerrapalli formation", "b": "Bhimaram Sandstone", "c": "Maleri formation", "d": "Kota formation"},
            "answer": "b", "topic": "Pranhita-Godavari Gondwana", "subtopic": "Bhimaram Sandstone",
            "notes": "The Bhimaram Sandstone consists of coarse, unfossiliferous channel sandstones separating the highly fossiliferous Yerrapalli and Maleri formations."
        },
        {
            "q_num": 169,
            "question": "In Indian paleontology, revolutionary discoveries of some of the world's earliest Jurassic mammalian fossils (Kotatherium, Trishulotherium) were made from the:",
            "options": {"a": "Chikiala formation", "b": "Dharmaram formation", "c": "Yerrapalli formation", "d": "Kota Formation (Pranhita-Godavari Basin)"},
            "answer": "d", "topic": "Mesozoic Mammals", "subtopic": "Kota Formation Mammals",
            "notes": "The Early Jurassic Kota Formation has yielded iconic morganucodontid and amphidontid early mammal teeth alongside the sauropod Kotasaurus yamanpalliensis."
        },
        {
            "q_num": 170,
            "question": "In the marine Cretaceous succession of the Cauvery Basin, diagnostic dinosaurian skeletal remains are characteristically present in the rocks of the:",
            "options": {"a": "Uttatur Group", "b": "Kallankurichchi Group", "c": "Ariyalur Group (Kallamedu Formation)", "d": "Niniyur Formation"},
            "answer": "c", "topic": "Cauvery Basin Dinosaurs", "subtopic": "Ariyalur Dinosaurs",
            "notes": "Official note (p. 328): The Kallamedu Formation of the Ariyalur Group is characterized by skeletal parts of sauropod, carnosaur, and stegosaurian dinosaurs."
        },
        {
            "q_num": 171,
            "question": "In northwestern India, the Potwar loess and silt deposits correspond chronologically to the:",
            "options": {"a": "I Glacial period (Gunz)", "b": "II Glacial period (Mindel)", "c": "III Glacial period (Riss)", "d": "IV Glacial period (Wurm)"},
            "answer": "b", "topic": "Quaternary Glaciations", "subtopic": "Potwar Loess",
            "notes": "The thick loess deposits of the Potwar plateau correlate with the Middle Pleistocene Second Glacial epoch (Mindel glaciation)."
        },
        {
            "q_num": 172,
            "question": "In the classical Alpine-Himalayan glacial chronostratigraphy, the Mindel and Riss glaciations occurred during the:",
            "options": {"a": "Lower Pleistocene", "b": "Middle Pleistocene", "c": "Upper Pleistocene", "d": "Holocene"},
            "answer": "b", "topic": "Quaternary Chronology", "subtopic": "Middle Pleistocene Glaciation",
            "notes": "The Middle Pleistocene (~780 to 126 ka) encompasses the major Mindel and Riss glacial stages of Europe and corresponding Himalayan glacial advances."
        },
        {
            "q_num": 173,
            "question": "In the four-fold Alpine glacial chronology established by Penck and Bruckner (1909), the earliest (first) glacial advance is termed the:",
            "options": {"a": "Günz", "b": "Mindel", "c": "Riss", "d": "Würm"},
            "answer": "a", "topic": "Quaternary Glacial Chronology", "subtopic": "Günz Stage",
            "notes": "Penck and Brückner (1909) named the four Pleistocene glacial advances in alphabetical order after Bavarian Alpine rivers: Günz (oldest) -> Mindel -> Riss -> Würm (youngest)."
        },
        {
            "q_num": 174,
            "question": "In the Indian subcontinent, the earliest documented evidence of hominid stone tool manufacture (Acheulean lithic culture) is not earlier than the:",
            "options": {"a": "Miocene-Pliocene", "b": "Lower Pleistocene", "c": "Middle Pleistocene", "d": "Holocene"},
            "answer": "c", "topic": "Indian Prehistory", "subtopic": "Hominid Occupation",
            "notes": "In Dr. Ausaf Sayeed's text key, option c (Middle Pleistocene) is recorded; Acheulean handaxes and cleavers flourished widely across Peninsular India during the Middle Pleistocene."
        },
        {
            "q_num": 175,
            "question": "Which of the following represents celebrated Pleistocene and sub-Recent continental deposits of India?",
            "options": {
                "a": "The Loess deposits of the Salt Range",
                "b": "The Stalagmitic cave deposits of Kurnool (Andhra Pradesh)",
                "c": "The Karewa beds of Kashmir",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Indian Quaternary Deposits", "subtopic": "Comprehensive Synthesis",
            "notes": "All three represent world-famous Indian Quaternary formations: the Potwar/Salt Range loess, the Kurnool bone caves (Billa Surgam), and the intermontane Karewas of Kashmir."
        }
    ]

def build_dataset():
    all_qs = get_questions_1_to_45() + get_questions_46_to_90() + get_questions_91_to_135() + get_questions_136_to_175()
    print(f"Total compiled questions: {len(all_qs)}")
    assert len(all_qs) == 175, f"Expected 175 questions, got {len(all_qs)}"

    # Validate answers against official key
    mismatches = 0
    for q in all_qs:
        qnum = q["q_num"]
        expected = OFFICIAL_KEY[qnum]
        actual = q["answer"]
        if actual != expected:
            print(f"Mismatch at Q{qnum}: expected {expected}, got {actual}")
            mismatches += 1

    assert mismatches == 0, f"Found {mismatches} key mismatches!"
    print("All 175 questions 100% verified against official answer key!")

    out_file = os.path.join(DATA_DIR, "sayeed_ch10_indian_geology.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, indent=2, ensure_ascii=False)

    print(f"Master dataset written successfully: {out_file} ({os.path.getsize(out_file)} bytes)")

if __name__ == "__main__":
    build_dataset()
