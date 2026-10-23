import json

batch8_items = [
  {
    "q": 91,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Sedimentary Petrology & Sandstone Petrography",
    "topic": "Arkose Sandstone Contains More Than 25% Feldspar",
    "question": "Arkose contain more than 25% of :",
    "options": {
      "A": "Micas",
      "B": "Amphiboles",
      "C": "Feldspars",
      "D": "Chlorite"
    },
    "correct_option": "C",
    "correct_text": "Feldspars (By Folk and Pettijohn classification, arkose is a terrigenous sandstone containing >25% feldspar derived from granitic basements)",
    "textbook_ref": "F.J. Pettijohn (1975, Sedimentary Rocks, p. 214); R.L. Folk (1968); K.M. Bangar (p. 136)",
    "file_html": "solutions/geology_2019/Q091_Arkose_Contains_More_Than_25_Percent_Feldspars_Complete_Guide.html",
    "icon": "🧱"
  },
  {
    "q": 92,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Clastic Granulometry & Grain Size Scales",
    "topic": "Silt Grade Detrital Sediments Size Range: 1/16 mm to 1/256 mm",
    "question": "The silt grade detrital sediments would have a size range of :",
    "options": {
      "A": "1/16 mm to 1/256 mm",
      "B": "Less than 1/256 mm",
      "C": "1/16 mm to 2 mm",
      "D": "2 mm to 1 mm"
    },
    "correct_option": "A",
    "correct_text": "1/16 mm to 1/256 mm (Udden-Wentworth scale: Silt grade spans 0.0625 mm down to 0.0039 mm, or +4 phi to +8 phi)",
    "textbook_ref": "C.K. Wentworth (1922); W.C. Krumbein (1934); K.M. Bangar (Principles of Engineering Geology, p. 131)",
    "file_html": "solutions/geology_2019/Q092_Silt_Grade_Detrital_Sediments_Size_Range_1_16_To_1_256_mm_Complete_Guide.html",
    "icon": "📏"
  },
  {
    "q": 93,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Sedimentary Structures & Intraformational Clasts",
    "topic": "Hardened Clay Leaves in Sandstone are Clay Galls",
    "question": "The leaves of hardened clay deposited in a sand or similar sediment as flat or lense shaped structure are called :",
    "options": {
      "A": "Clay flakes",
      "B": "Clay balls",
      "C": "Clay stones",
      "D": "Clay galls"
    },
    "correct_option": "D",
    "correct_text": "Clay galls (Intraformational mud rip-up clasts formed when sun-cracked desiccated mud leaves are ripped up and redeposited in sand)",
    "textbook_ref": "F.J. Pettijohn (1975); K.M. Bangar (Principles of Engineering Geology, p. 134); G.B. Mahapatra",
    "file_html": "solutions/geology_2019/Q093_Leaves_Of_Hardened_Clay_In_Sand_Are_Clay_Galls_Complete_Guide.html",
    "icon": "🍂"
  },
  {
    "q": 94,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Coarse Clastic Granulometry & Conglomerates",
    "topic": "Cobble: Rounded Clast between 64 mm and 256 mm Diameter",
    "question": "Rounded to sub-rounded clast with a diameter between 64 and 256 mm is generally known as :",
    "options": {
      "A": "Gravel",
      "B": "Pebble",
      "C": "Cobble",
      "D": "Boulder"
    },
    "correct_option": "C",
    "correct_text": "Cobble (Wentworth coarse clast scale: Pebble 4-64 mm, Cobble 64-256 mm, Boulder >256 mm)",
    "textbook_ref": "C.K. Wentworth (1922); F.J. Pettijohn (Sedimentary Rocks, p. 153); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q094_Rounded_Clast_64_To_256_mm_Is_Cobble_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 95,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Primary Sedimentary Structures & Cross-Stratification",
    "topic": "Current Beds: Inclined Bedding Planes Formed by Moving Currents",
    "question": "If a series of inclined bedding planes showing some angular relationship to the direction of current flow, then they are generally called as :",
    "options": {
      "A": "Gradient beds",
      "B": "Current beds",
      "C": "Dipping beds",
      "D": "Convolute beds"
    },
    "correct_option": "B",
    "correct_text": "Current beds (Also termed cross-bedding or false bedding; inclined foreset strata formed down-current on migrating dunes and ripples)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 132); Sam Boggs Jr. (2014); Pettijohn",
    "file_html": "solutions/geology_2019/Q095_Series_Of_Inclined_Bedding_Planes_Are_Current_Beds_Complete_Guide.html",
    "icon": "🌊"
  },
  {
    "q": 96,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Sedimentary Diagenesis & Lithification",
    "topic": "Compaction and Cementation of Sediments Occur During Diagenesis",
    "question": "Compaction and cementation of sediments occur during :",
    "options": {
      "A": "Transportation",
      "B": "High temperature and pressure medium",
      "C": "High water pressure",
      "D": "Diagenesis"
    },
    "correct_option": "D",
    "correct_text": "Diagenesis (The collective post-depositional physical and chemical changes turning loose sediments into solid rock prior to metamorphism)",
    "textbook_ref": "Sam Boggs Jr. (2014, Principles of Sedimentology & Stratigraphy); K.M. Bangar (p. 130)",
    "file_html": "solutions/geology_2019/Q096_Compaction_And_Cementation_Occur_During_Diagenesis_Complete_Guide.html",
    "icon": "⚙️"
  },
  {
    "q": 97,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Wave Hydrodynamics & Ripple Bedforms",
    "topic": "Oscillation Ripples Formed in Beach Environment",
    "question": "Oscillation ripples are formed in :",
    "options": {
      "A": "Deep sea environment",
      "B": "Beach environment",
      "C": "Alluvial environment",
      "D": "Desert environment"
    },
    "correct_option": "B",
    "correct_text": "Beach environment (Symmetrical ripples with sharp crests generated by bidirectional back-and-forth orbital water motion of surface waves)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 133); Sam Boggs Jr. (2014)",
    "file_html": "solutions/geology_2019/Q097_Oscillation_Ripples_Are_Formed_In_Beach_Environment_Complete_Guide.html",
    "icon": "🏖️"
  },
  {
    "q": 98,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Carbonate Diagenesis & Redox Geochemistry",
    "topic": "Ferroan Calcite Cement: Indicator of Deep Burial Diagenesis",
    "question": "Occurrence of ferroan calcite cementing in a carbonate rock is an indicator of :",
    "options": {
      "A": "Deep burial diagenesis",
      "B": "Vadose diagenesis",
      "C": "Phreatic diagenesis",
      "D": "Sea floor diagenesis"
    },
    "correct_option": "A",
    "correct_text": "Deep burial diagenesis (Soluble Fe2+ is reduced from Fe3+ under anoxic reducing conditions isolated from oxygen, substituting for Ca2+ in burial spar)",
    "textbook_ref": "M.E. Tucker & V.P. Wright (1990, Carbonate Sedimentology, pp. 365-368); P.A. Scholle (1978)",
    "file_html": "solutions/geology_2019/Q098_Ferroan_Calcite_Cement_Indicator_Of_Deep_Burial_Diagenesis_Complete_Guide.html",
    "icon": "🧪"
  },
  {
    "q": 99,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Soft-Sediment Deformation & Sediment Mechanics",
    "topic": "Syn-Sedimentary Deformation Results from High Sedimentation",
    "question": "Syn-sedimentary deformation structures are a result of :",
    "options": {
      "A": "Massive transgression",
      "B": "Low sedimentation",
      "C": "Marine regression",
      "D": "High sedimentation"
    },
    "correct_option": "D",
    "correct_text": "High sedimentation (Rapid sediment dumping traps pore fluids, creates reverse density gradients, and triggers spontaneous liquefaction)",
    "textbook_ref": "J.D. Collinson et al. (2006, Sedimentary Structures); Sam Boggs Jr. (2014); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q099_Syn_Sedimentary_Deformation_Structures_Result_Of_High_Sedimentation_Complete_Guide.html",
    "icon": "⚡"
  },
  {
    "q": 100,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Granulometric Statistics & Skewness",
    "topic": "Organic Detritus Imparts Negative Skewness",
    "question": "If sediment is dominantly compose of organic detritus, it is known to indicate :",
    "options": {
      "A": "Complex skewness",
      "B": "Positive skewness",
      "C": "Negative skewness",
      "D": "No skewness"
    },
    "correct_option": "C",
    "correct_text": "Negative skewness (Coarse bioclastic shell fragments create an elongated tail toward coarse negative phi values, yielding negative skewness)",
    "textbook_ref": "G.M. Friedman (1961, 1967); R.L. Folk & W.C. Ward (1957); Sam Boggs Jr.",
    "file_html": "solutions/geology_2019/Q100_Sediment_Dominantly_Organic_Detritus_Indicates_Negative_Skewness_Complete_Guide.html",
    "icon": "📊"
  },
  {
    "q": 101,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Palaeocurrent Systematics & Marine Regimes",
    "topic": "Shallow Marine Palaeocurrents: Both Bimodal and Polymodal",
    "question": "In shallow marine environment, generally the palaeocurrent patterns are :",
    "options": {
      "A": "Polymodal",
      "B": "Bimodal",
      "C": "Unimodal",
      "D": "Both Bimodal and Polymodal"
    },
    "correct_option": "D",
    "correct_text": "Both Bimodal and Polymodal (Tidal estuaries yield bimodal herringbone patterns while storm-affected shelves yield polymodal patterns)",
    "textbook_ref": "F.J. Pettijohn, P.E. Potter & R. Siever (1987, Sand and Sandstone, pp. 288-292); Boggs",
    "file_html": "solutions/geology_2019/Q101_Shallow_Marine_Palaeocurrent_Patterns_Both_Bimodal_And_Polymodal_Complete_Guide.html",
    "icon": "🧭"
  },
  {
    "q": 102,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geosynclinal Theory & Basin Tectonics",
    "topic": "Miogeosyncline: Non-Volcanic Basin Adjacent to Craton",
    "question": "A basin with thinner development of sediments and no volcanic rocks, forming adjacent to a craton is called :",
    "options": {
      "A": "Parageosyncline",
      "B": "Miogeosyncline",
      "C": "Rift valley",
      "D": "Graben"
    },
    "correct_option": "B",
    "correct_text": "Miogeosyncline (Marshall Kay's term for the inner, avolcanic belt of an orthogeosyncline bordering the stable craton with shallow-marine cover)",
    "textbook_ref": "Marshall Kay (1951, GSA Memoir 48); Hans Stille (1940); K.M. Bangar (p. 155)",
    "file_html": "solutions/geology_2019/Q102_Basin_Thinner_Sediments_No_Volcanics_Adjacent_Craton_Is_Miogeosyncline_Complete_Guide.html",
    "icon": "🗺️"
  },
  {
    "q": 103,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Clastic Petrography & Matrix Classification",
    "topic": "Rock Principally Made Up of Clay Minerals: Greywacke Clay Matrix",
    "question": "Which of the following rocks is principally made up of clay minerals ?",
    "options": {
      "A": "Arkose",
      "B": "Siltstone",
      "C": "Greywacke",
      "D": "Dolostone"
    },
    "correct_option": "C",
    "correct_text": "Greywacke (Characterized by an abundant matrix >15% to 50% consisting principally of clay minerals, chlorite, and sericite)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 136); P.K. Mukherjee (p. 251); Pettijohn",
    "file_html": "solutions/geology_2019/Q103_Rock_Principally_Made_Up_Of_Clay_Minerals_Greywacke_Complete_Guide.html",
    "icon": "🔬"
  },
  {
    "q": 104,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Primary Sedimentary Structures Classification",
    "topic": "Depositional Sedimentary Structure: Graded Bedding",
    "question": "Which of the following is a depositional sedimentary structure ?",
    "options": {
      "A": "Graded bedding",
      "B": "Trough cross bedding",
      "C": "Collapse structure",
      "D": "Injection structure"
    },
    "correct_option": "A",
    "correct_text": "Graded bedding (Primary depositional settling structure from waning suspension currents; trough cross-bedding is also evaluated as a primary bedform)",
    "textbook_ref": "F.J. Pettijohn & P.E. Potter (1964); Sam Boggs Jr. (2014); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q104_Graded_Bedding_Is_A_Depositional_Sedimentary_Structure_Complete_Guide.html",
    "icon": "⏳"
  },
  {
    "q": 105,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Carbonate Rock Classification & Allochems",
    "topic": "Limestone Composed Mainly of Organic Detritus is Coquina",
    "question": "A limestone which contains mainly of organic detritus is generally called as :",
    "options": {
      "A": "Spergenite",
      "B": "Coquina",
      "C": "Oolite",
      "D": "Calc-tufa"
    },
    "correct_option": "B",
    "correct_text": "Coquina (Bioclastic limestone composed predominantly of coarse, loosely cemented broken seashells and organic skeletal debris)",
    "textbook_ref": "R.J. Dunham (1962); R.L. Folk (1962); K.M. Bangar (Principles of Engineering Geology, p. 138)",
    "file_html": "solutions/geology_2019/Q105_Limestone_Of_Organic_Detritus_Is_Coquina_Complete_Guide.html",
    "icon": "🐚"
  }
]

with open('data/geology_2019.json', 'r') as f:
    existing_data = json.load(f)

existing_qs = {item['q'] for item in existing_data}
new_items = [item for item in batch8_items if item['q'] not in existing_qs]

updated_data = existing_data + new_items
updated_data.sort(key=lambda x: x['q'])

with open('data/geology_2019.json', 'w') as f:
    json.dump(updated_data, f, indent=2)

print(f"Updated data/geology_2019.json: Total entries = {len(updated_data)}")
