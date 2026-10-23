import json

batch7_items = [
  {
    "q": 76,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Igneous Petrology & Chemical Classification",
    "topic": "Acid Igneous Rocks: 10% or More Free Quartz Criterion",
    "question": "Generally, acid igneous rocks contain :",
    "options": {
      "A": "10% or more free quartz",
      "B": "15% or more free quartz",
      "C": "60% or more free quartz",
      "D": "65% or more free quartz"
    },
    "correct_option": "A",
    "correct_text": "10% or more free quartz (Acid rocks have >65-66% total silica, saturating all silicate bases and yielding at least 10% modal free quartz)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 110-112); John D. Winter (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q076_Acid_Igneous_Rocks_Contain_10_Percent_Or_More_Free_Quartz_Complete_Guide.html",
    "icon": "💎"
  },
  {
    "q": 77,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Volcanic Petrology & TAS Classification",
    "topic": "Andesite is an Intermediate Volcanic Rock",
    "question": "Andesite is :",
    "options": {
      "A": "A coarse grained acid plutonic rock",
      "B": "A fine grained hypabyssal rock",
      "C": "An intermediate volcanic rock",
      "D": "An ultrabasic volcanic rock"
    },
    "correct_option": "C",
    "correct_text": "An intermediate volcanic rock (52-63 wt% SiO2, fine-grained/porphyritic extrusive equivalent of diorite characteristic of subduction arcs)",
    "textbook_ref": "John D. Winter (Principles of Igneous and Metamorphic Petrology); K.M. Bangar (p. 125)",
    "file_html": "solutions/geology_2019/Q077_Andesite_Is_An_Intermediate_Volcanic_Rock_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 78,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Magmatic Crystallization & Bowen's Principles",
    "topic": "Bowen's Continuous Reaction Series: Calcic Plagioclase First Formed",
    "question": "The first mineral formed in the continuous series of Bowen reaction principle is :",
    "options": {
      "A": "Sodic-Calcic plagioclase",
      "B": "Potash feldspar",
      "C": "Calcic-sodic plagioclase",
      "D": "Calcic plagioclase"
    },
    "correct_option": "D",
    "correct_text": "Calcic plagioclase (Pure anorthite CaAl2Si2O8 has highest melting point ~1553°C and crystallizes first from cooling basic melt)",
    "textbook_ref": "N.L. Bowen (1928, The Evolution of the Igneous Rocks); John D. Winter (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q078_First_Mineral_Formed_Bowen_Continuous_Series_Calcic_Plagioclase_Complete_Guide.html",
    "icon": "🧪"
  },
  {
    "q": 79,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Alkaline Magmatism & Carbonatites",
    "topic": "Carbonatite: Magmatic Carbonate Rock & REE Mineralization",
    "question": "A magmatic rock rich in calcium carbonate and often containing rare earth minerals is :",
    "options": {
      "A": "Alkali basalt",
      "B": "Syenite porphyry",
      "C": "Carbonatite",
      "D": "Granodiorite"
    },
    "correct_option": "C",
    "correct_text": "Carbonatite (Mantle-derived igneous rock containing >50% modal carbonate minerals, hosting world-class reserves of REEs and Niobium)",
    "textbook_ref": "Keith Bell (Carbonatites); K.M. Bangar (p. 128); Winter (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q079_Carbonatite_Magmatic_Rock_Rich_In_Calcium_Carbonate_REE_Complete_Guide.html",
    "icon": "🪙"
  },
  {
    "q": 80,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Granulite Facies & Charnockite Series",
    "topic": "Charnockite Mineral Composition: Quartz-Feldspar-Hypersthene",
    "question": "Generally, a charnockite has a mineral composition of :",
    "options": {
      "A": "Quartz-Hornblende-Oligoclase",
      "B": "Quartz-Epidote-Andesine",
      "C": "Quartz-Feldspar-Hypersthene",
      "D": "Quartz-Feldspar-Augite"
    },
    "correct_option": "C",
    "correct_text": "Quartz-Feldspar-Hypersthene (Sir Thomas Holland's hypersthene-bearing granite formed under high-grade dry granulite facies conditions)",
    "textbook_ref": "Sir Thomas Holland (1900, Memoirs of GSI); K.M. Bangar; Winter (Metamorphic Petrology)",
    "file_html": "solutions/geology_2019/Q080_Charnockite_Mineral_Composition_Quartz_Feldspar_Hypersthene_Complete_Guide.html",
    "icon": "🟩"
  },
  {
    "q": 81,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Intermediate & Ultramafic Petrology",
    "topic": "Diorite 100% Ferromagnesian Content: Perkinite",
    "question": "If the ferromagnesian content of diorite is 100%, then it is called :",
    "options": {
      "A": "Perkinite",
      "B": "Leptinite",
      "C": "Meladiorite",
      "D": "Leucodiorite"
    },
    "correct_option": "A",
    "correct_text": "Perkinite (An ultramafic amphibole-pyroxene plutonic rock representing the 100% ferromagnesian, feldspar-free end-member of diorite)",
    "textbook_ref": "P.K. Mukherjee (A Textbook of Geology, p. 249); L. Duparc (1907); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q081_Ferromagnesian_Content_Of_Diorite_100_Percent_Is_Perkinite_Complete_Guide.html",
    "icon": "⬛"
  },
  {
    "q": 82,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Basic Mafic Igneous Suite",
    "topic": "Dolerite Compositional Equivalence to Basalt",
    "question": "By mineral composition, dolerite is equivalent to :",
    "options": {
      "A": "Pitchstone",
      "B": "Syenite",
      "C": "Peridotite",
      "D": "Basalt"
    },
    "correct_option": "D",
    "correct_text": "Basalt (Dolerite is the medium-grained hypabyssal intrusive equivalent of extrusive volcanic basalt, both consisting of labradorite + augite)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 126); John D. Winter (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q082_By_Mineral_Composition_Dolerite_Is_Equivalent_To_Basalt_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 83,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Basic Rock Clan & Varieties",
    "topic": "Beerbachite is a Variety of Gabbro",
    "question": "Beerbachite is a variety of :",
    "options": {
      "A": "Gabbro",
      "B": "Basalt",
      "C": "Dolerite",
      "D": "Monzonite"
    },
    "correct_option": "A",
    "correct_text": "Gabbro (A fine-grained, granular/aplitic microgabbro or pyroxene-hornfels composed of equigranular labradorite and pyroxene)",
    "textbook_ref": "C. Chelius (1892); P.K. Mukherjee (A Textbook of Geology, p. 251); IUGS Systematics",
    "file_html": "solutions/geology_2019/Q083_Beerbachite_Is_A_Variety_Of_Gabbro_Complete_Guide.html",
    "icon": "🔬"
  },
  {
    "q": 84,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Granitoids & QAPF Systematics",
    "topic": "Adamellite (Quartz Monzonite): Equal Amounts of Oligoclase & K-feldspar",
    "question": "Adamellite contains :",
    "options": {
      "A": "Roughly equal amounts of Oligoclase and K-feldspar",
      "B": "Roughly equal amounts of Quartz and Oligoclase",
      "C": "Roughly equal amounts of Quartz and K-feldspar",
      "D": "Roughly equal amounts of Quartz and Albite"
    },
    "correct_option": "A",
    "correct_text": "Roughly equal amounts of Oligoclase and K-feldspar (QAPF Field 3b Quartz Monzonite with P/(A+P) ratio between 35% and 65%)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 123); IUGS Systematics (Le Maitre, 2002)",
    "file_html": "solutions/geology_2019/Q084_Adamellite_Contains_Equal_Amounts_Oligoclase_And_K_Feldspar_Complete_Guide.html",
    "icon": "⚖️"
  },
  {
    "q": 85,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Igneous Textures & Pegmatites",
    "topic": "Graphic Texture Normally Exhibited by Pegmatite",
    "question": "Graphic texture is normally exhibited by :",
    "options": {
      "A": "Komatiite",
      "B": "Pegmatite",
      "C": "Phonolite",
      "D": "Anorthosite"
    },
    "correct_option": "B",
    "correct_text": "Pegmatite (Runic cuneiform intergrowth formed by simultaneous eutectic crystallization of quartz rods within microcline host)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 115); John D. Winter (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q085_Graphic_Texture_Normally_Exhibited_By_Pegmatite_Complete_Guide.html",
    "icon": "📜"
  },
  {
    "q": 86,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Pluton Morphology & Concordant Bodies",
    "topic": "Laccolith: Igneous Body that has Domed Up Overlying Strata",
    "question": "An igneous body that has doomed up the strata into which it has been inserted is known as :",
    "options": {
      "A": "Lopolith",
      "B": "Dyke",
      "C": "Bysmalith",
      "D": "Laccolith"
    },
    "correct_option": "D",
    "correct_text": "Laccolith (Concordant plano-convex blister-like intrusion with a flat floor and an arched/domed roof flexing overlying strata)",
    "textbook_ref": "G.K. Gilbert (1877, Henry Mountains); K.M. Bangar (p. 118); G.B. Mahapatra",
    "file_html": "solutions/geology_2019/Q086_Igneous_Body_Domed_Up_Strata_Is_Laccolith_Complete_Guide.html",
    "icon": "🍄"
  },
  {
    "q": 87,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Magma Ascent & Emplacement Mechanisms",
    "topic": "Magmatic Stoping: Process Whereby Magma Works Way into Crust",
    "question": "A process whereby magma works its way up into the crust of the earth is known as :",
    "options": {
      "A": "Magmatic injection",
      "B": "Magmatic thrusting",
      "C": "Magmatic stoping",
      "D": "Magmatic intrusion"
    },
    "correct_option": "C",
    "correct_text": "Magmatic stoping (R.A. Daly's mechanism of thermal shattering, overhead block detachment, and gravitational sinking of country rock xenoliths)",
    "textbook_ref": "R.A. Daly (1903, 1914); K.M. Bangar (Principles of Engineering Geology, p. 119)",
    "file_html": "solutions/geology_2019/Q087_Magma_Works_Way_Into_Crust_Is_Magmatic_Stoping_Complete_Guide.html",
    "icon": "⛏️"
  },
  {
    "q": 88,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Alkaline Dyke Rocks & Lamprophyres",
    "topic": "Minette is a Type of Lamprophyre",
    "question": "Minette is a type of :",
    "options": {
      "A": "Diorite",
      "B": "Tonalite",
      "C": "Aplite",
      "D": "Lamprophyre"
    },
    "correct_option": "D",
    "correct_text": "Lamprophyre (Calc-alkaline lamprophyre characterized by essential biotite/phlogopite phenocrysts in an orthoclase-dominated groundmass)",
    "textbook_ref": "N.M.S. Rock (1991, Lamprophyres); K.M. Bangar (p. 128); John D. Winter",
    "file_html": "solutions/geology_2019/Q088_Minette_Is_A_Type_Of_Lamprophyre_Complete_Guide.html",
    "icon": "✨"
  },
  {
    "q": 89,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Magma Generation & Petrogenesis",
    "topic": "Palingenesis: Complete or Partial Melting of Pre-Existing Rock",
    "question": "The process of complete or partial melting of a rock is known as :",
    "options": {
      "A": "Migmatization",
      "B": "Assimilation",
      "C": "Juvenile magmatism",
      "D": "Palingenesis"
    },
    "correct_option": "D",
    "correct_text": "Palingenesis (J.J. Sederholm's classical term for the rebirth/remelting of pre-existing crustal rocks to generate new magmatic melts)",
    "textbook_ref": "J.J. Sederholm (1907); P.K. Mukherjee (A Textbook of Geology, p. 238); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q089_Process_Of_Complete_Or_Partial_Melting_Of_Rock_Is_Palingenesis_Complete_Guide.html",
    "icon": "🔄"
  },
  {
    "q": 90,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Magmatic Differentiation & Phase Thermodynamics",
    "topic": "Liquid Immiscibility: Unmixing of Two Liquids of Different Composition",
    "question": "Liquid imissibility generally results from :",
    "options": {
      "A": "Mixing of two liquids of two different composition",
      "B": "Mixing of two liquids of same composition",
      "C": "Unmixing of two liquids of different composition",
      "D": "Unmixing of two liquids of same composition"
    },
    "correct_option": "C",
    "correct_text": "Unmixing of two liquids of different composition (Thermodynamic solvus phenomenon where a parent melt splits into two distinct, mutually insoluble liquid phases)",
    "textbook_ref": "Edwin Roedder (1979); John D. Winter (Principles of Igneous Petrology); K.M. Bangar",
    "file_html": "solutions/geology_2019/Q090_Liquid_Immiscibility_Results_From_Unmixing_Two_Liquids_Different_Composition_Complete_Guide.html",
    "icon": "🫧"
  }
]

with open('data/geology_2019.json', 'r') as f:
    existing_data = json.load(f)

# Ensure no duplicate questions
existing_qs = {item['q'] for item in existing_data}
new_items = [item for item in batch7_items if item['q'] not in existing_qs]

updated_data = existing_data + new_items
# sort by q
updated_data.sort(key=lambda x: x['q'])

with open('data/geology_2019.json', 'w') as f:
    json.dump(updated_data, f, indent=2)

print(f"Updated data/geology_2019.json: Total entries = {len(updated_data)}")
