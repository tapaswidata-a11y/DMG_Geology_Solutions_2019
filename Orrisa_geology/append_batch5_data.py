import json

batch5_items = [
  {
    "q": 46,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Indian Stratigraphy & Precambrian Geology",
    "topic": "Dharwar Craton Stratigraphy & Youngest Event: Closepet Granite (~2.51 Ga)",
    "question": "Which of the following represents the youngest event in the Dharwarian stratigraphy ?",
    "options": {
      "A": "Sargur Group",
      "B": "Closepet Granite",
      "C": "Dharwar SuperGroup",
      "D": "Peninsular Gneissic Complex"
    },
    "correct_option": "B",
    "correct_text": "Closepet Granite (Late-to-post-tectonic granite batholith dated at 2.51 Ga, terminating Dharwar cratonization)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 277-279); M. Ramakrishnan & R. Vaidyanadhan (Geology of India, Vol. 1, pp. 79-115)",
    "file_html": "solutions/geology_2019/Q046_Youngest_Event_Dharwar_Stratigraphy_Closepet_Granite_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 47,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Indian Stratigraphy & Chronostratigraphy",
    "topic": "Chronostratigraphic Pair: Niniyur Formation & Cretaceous-Tertiary Marine Transition",
    "question": "Choose the correct pair of stratigraphic formation and its corresponding age :",
    "options": {
      "A": "Bhander Group — Early Proterozoic",
      "B": "Niniyur Formation — Cretaceous",
      "C": "Long Formation — Oligocene",
      "D": "Bheema Group — Cambrian"
    },
    "correct_option": "B",
    "correct_text": "Niniyur Formation — Cretaceous (Uppermost terminal division of the classic Cauvery Basin Cretaceous-Tertiary marine succession in Trichinopoly)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 296); M.S. Krishnan (Geology of India and Burma, pp. 410-425)",
    "file_html": "solutions/geology_2019/Q047_Stratigraphic_Pair_Niniyur_Formation_Cretaceous_Complete_Guide.html",
    "icon": "📐"
  },
  {
    "q": 48,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Mesozoic Stratigraphy & Cephalopod Biozones",
    "topic": "Kutch Basin: Global Type Area for the Indian Jurassic System",
    "question": "Kutch is the type Area in India for :",
    "options": {
      "A": "Jurassic formation",
      "B": "Early archean rocks",
      "C": "Late Archean rocks",
      "D": "Cambrian formation"
    },
    "correct_option": "A",
    "correct_text": "Jurassic formation (Iconic Patcham, Chari, Katrol, and Umia Formations with world-standard cephalopod ammonite biozones)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 291-293); W. Waagen (Jurassic Fauna of Kutch, Pal. Ind.)",
    "file_html": "solutions/geology_2019/Q048_Kutch_Type_Area_Jurassic_Formation_Complete_Guide.html",
    "icon": "🐚"
  },
  {
    "q": 49,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Cenozoic Stratigraphy & Vertebrate Paleontology",
    "topic": "Siwalik Foreland Molasse: Global Treasury of Mammal Fossils",
    "question": "Siwaliks are well known for:",
    "options": {
      "A": "Dinosaur fossil",
      "B": "Invertebrate fossils",
      "C": "Mammal fossils",
      "D": "Plant fossils"
    },
    "correct_option": "C",
    "correct_text": "Mammal fossils (World's richest Neogene terrestrial record: Sivapithecus hominoids, Hipparion and Equus horses, Stegodon elephants, bovids)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 302-304); G.E. Pilgrim & E.H. Colbert (Siwalik Vertebrates)",
    "file_html": "solutions/geology_2019/Q049_Siwaliks_Well_Known_For_Mammal_Fossils_Complete_Guide.html",
    "icon": "🐘"
  },
  {
    "q": 50,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Tethyan Himalayan Stratigraphy & Paleozoic Geology",
    "topic": "Spiti Tethyan Basin: Permian System Represented by Kuling Group",
    "question": "In Spiti, the Permians are represented by :",
    "options": {
      "A": "Muth quartzite",
      "B": "Kanawar Group",
      "C": "Kuling group",
      "D": "Agglomerate shale"
    },
    "correct_option": "C",
    "correct_text": "Kuling group (Comprises the basal Gechang sandstone and upper Gungri / Productus Shales with Cyclolobus and Marginifera)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 287-288); S.V. Srikantia & O.N. Bhargava (Geology of Spiti)",
    "file_html": "solutions/geology_2019/Q050_Spiti_Permians_Represented_By_Kuling_Group_Complete_Guide.html",
    "icon": "🏔️"
  },
  {
    "q": 51,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Precambrian Geology & Magmatism",
    "topic": "Aravalli-Delhi Orogenic Belt: Delhi System Intrusion by Erinpura Granite",
    "question": "Dalhi system is intruded by:",
    "options": {
      "A": "Erinpura Granite",
      "B": "Malani Rhyolite",
      "C": "Singhbhum Granite",
      "D": "Bundelkhand Granite"
    },
    "correct_option": "A",
    "correct_text": "Erinpura Granite (Post-tectonic Neoproterozoic calc-alkaline batholiths dated at ~850-800 Ma cross-cutting folded Delhi metasediments)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 280-281); A.M. Heron (Geology of Central Rajputana, GSI Memoir 79)",
    "file_html": "solutions/geology_2019/Q051_Delhi_System_Intruded_By_Erinpura_Granite_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 52,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Sedimentary Basin Analysis & Lithofacies",
    "topic": "Lithofacies Analysis: Mesozoic Bhuj Formation Predominantly Sandstones",
    "question": "Which of the following statement is correct ?",
    "options": {
      "A": "The Mesozoic Bhuj formation consists predominantly of sandstones",
      "B": "Kaladgi basin is predominantly made of slates",
      "C": "Vindhyan supergroup is devoid of limestone",
      "D": "Cuddapah basin is predominantly made of metadacites"
    },
    "correct_option": "A",
    "correct_text": "The Mesozoic Bhuj formation consists predominantly of sandstones (Thick, cross-bedded fluvial to deltaic quartzose sandstones with minor plant shales)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 297); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 5)",
    "file_html": "solutions/geology_2019/Q052_Bhuj_Formation_Predominantly_Sandstones_Correct_Statement_Complete_Guide.html",
    "icon": "🏜️"
  },
  {
    "q": 53,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Tethyan Himalayan Stratigraphy & Marker Horizons",
    "topic": "Muth Quartzite: Devonian Regional Marker Horizon in the Himalaya",
    "question": "Marker horizon for Devonian in Himalaya is called ;",
    "options": {
      "A": "Lipak formation",
      "B": "Po formation",
      "C": "Muth quartzites",
      "D": "Syringothyris limestone"
    },
    "correct_option": "C",
    "correct_text": "Muth quartzites (Ubiquitous snow-white super-mature quartz arenite cliff-former across Kashmir, Spiti, Zanskar, and Kumaon)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 286); F. Stoliczka (Mem. GSI, 1865)",
    "file_html": "solutions/geology_2019/Q053_Devonian_Marker_Horizon_Himalaya_Muth_Quartzites_Complete_Guide.html",
    "icon": "⛰️"
  },
  {
    "q": 54,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Paleobiology & Geobiology",
    "topic": "Stromatolites: Direct Windows into the Origin and Evolution of Life",
    "question": "Stromatolites provide insight for:",
    "options": {
      "A": "Origin and Evolution of life",
      "B": "Recognizing boundary between Cambrian and Ordovician",
      "C": "Glaciation process",
      "D": "Weathering cycles"
    },
    "correct_option": "A",
    "correct_text": "Origin and Evolution of life (Organo-sedimentary laminations constructed by cyanobacteria dating back to 3.5 Ga in Archean cherts)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 273-274); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 6, p. 195)",
    "file_html": "solutions/geology_2019/Q054_Stromatolites_Provide_Insight_Origin_Evolution_Life_Complete_Guide.html",
    "icon": "🧬"
  },
  {
    "q": 55,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Himalayan Regional Tectonics",
    "topic": "Main Boundary Thrust (MBT) Juxtaposing Siwaliks and Lesser Himalaya",
    "question": "In Himalayas, the main boundary fault separates ;",
    "options": {
      "A": "Siwalik and Tertiary",
      "B": "Siwalik and Archean",
      "C": "Vindhyan and Aravalli",
      "D": "Siwalik and Delhi Group"
    },
    "correct_option": "A",
    "correct_text": "Siwalik and Tertiary (Crustal-scale thrust fault placing the Lesser Himalayan pre-Tertiary and Paleogene belt over the Sub-Himalayan Siwalik molasse)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 306-307); B.A. van der Pluijm & S. Marshak (Earth Structure, Ch. 21)",
    "file_html": "solutions/geology_2019/Q055_Himalayas_Main_Boundary_Fault_Separates_Siwalik_Tertiary_Complete_Guide.html",
    "icon": "⚡"
  },
  {
    "q": 56,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Continental Flood Basalts & Volcanology",
    "topic": "Deccan Large Igneous Province: Cretaceous Volcanic Eruptive Pulse",
    "question": "The Volumincus Deccan Flood Basalts occurred during :",
    "options": {
      "A": "Ordovician",
      "B": "Triassic",
      "C": "Cretaceous",
      "D": "Pleistocene"
    },
    "correct_option": "C",
    "correct_text": "Cretaceous (Massive tholeiitic outpourings spanning 66.4 to 64.5 Ma across the Late Cretaceous Maastrichtian and K-Pg boundary)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 297-299); John D. Winter (Principles of Igneous and Metamorphic Petrology, Ch. 15)",
    "file_html": "solutions/geology_2019/Q056_Voluminous_Deccan_Flood_Basalts_Cretaceous_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 57,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geologic Time Scale & Chronostratigraphy",
    "topic": "Mesozoic-Cenozoic (K-Pg) Boundary at Approximately 65 Ma",
    "question": "Mesozoic and Cenozoic boundary lies approximately at :",
    "options": {
      "A": "75 Ma",
      "B": "60 Ma",
      "C": "120 Ma",
      "D": "65 Ma"
    },
    "correct_option": "D",
    "correct_text": "65 Ma (Precisely calibrated at 66.0 Ma in ICS chronostratigraphy, marked by the Chicxulub bolide impact and iridium anomaly)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 272); International Commission on Stratigraphy (ICS Time Scale 2024)",
    "file_html": "solutions/geology_2019/Q057_Mesozoic_Cenozoic_Boundary_Approximately_65_Ma_Complete_Guide.html",
    "icon": "⏱️"
  },
  {
    "q": 58,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Northwest Himalayan Stratigraphy & Basement Complexes",
    "topic": "Salkhala Series: Archean-Precambrian Crystalline Basement of Kashmir-Hazara",
    "question": "In Kashmir-Hazara area, the Archean rocks are called:",
    "options": {
      "A": "Buxa series",
      "B": "Salkhala series",
      "C": "Sakarsanahalli series",
      "D": "Aravalli series"
    },
    "correct_option": "B",
    "correct_text": "Salkhala series (Metamorphic complex of graphitic schists, phyllites, crystalline marbles, and gneisses underlying the Dogra Slates)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 281); D.N. Wadia (Geology of India, pp. 112-120)",
    "file_html": "solutions/geology_2019/Q058_Kashmir_Hazara_Archean_Rocks_Called_Salkhala_Series_Complete_Guide.html",
    "icon": "💎"
  },
  {
    "q": 59,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Planetary Geochronology & Earth History",
    "topic": "Precambrian Supereon Occupying the Longest Time Period (>88% of History)",
    "question": "in the geological history, which of the following occupies longest time period.?",
    "options": {
      "A": "Paleozoic",
      "B": "Mesozoic",
      "C": "Precambrian",
      "D": "Cenozoic"
    },
    "correct_option": "C",
    "correct_text": "Precambrian (Spans ~4,000 million years from 4.54 Ga to 539 Ma, representing over 88% of all geological time on Earth)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 273); Arthur Holmes (Principles of Physical Geology)",
    "file_html": "solutions/geology_2019/Q059_Geological_History_Precambrian_Longest_Time_Period_Complete_Guide.html",
    "icon": "⏳"
  },
  {
    "q": 60,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Global Biotic Catastrophes & Macroevolution",
    "topic": "Cretaceous-Tertiary (K-Pg) Boundary Mass Extinction Event",
    "question": "Which of the following is known to be the boundary of mass extinction ?",
    "options": {
      "A": "Proterozoic Cambrian",
      "B": "Miocene - Pliocene",
      "C": "Triassic — Jurassic",
      "D": "Cretaceous — Tertiary"
    },
    "correct_option": "D",
    "correct_text": "Cretaceous — Tertiary (Wiped out 76% of species including non-avian dinosaurs, ammonites, and marine reptiles at ~66 Ma)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 299); L. Alvarez et al. (Science, 1980)",
    "file_html": "solutions/geology_2019/Q060_Boundary_Of_Mass_Extinction_Cretaceous_Tertiary_Complete_Guide.html",
    "icon": "☄️"
  }
]

with open("data/geology_2019.json", "r") as f:
    existing = json.load(f)

# Filter out any existing entries with q in 46..60 to allow clean updates
existing_dict = {item["q"]: item for item in existing if item["q"] < 46 or item["q"] > 60}
for it in batch5_items:
    existing_dict[it["q"]] = it

sorted_items = [existing_dict[k] for k in sorted(existing_dict.keys())]

with open("data/geology_2019.json", "w", encoding="utf-8") as f:
    json.dump(sorted_items, f, indent=2)

print(f"Updated data/geology_2019.json: Total entries = {len(sorted_items)}")
