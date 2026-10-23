import json

batch9_items = [
  {
    "q": 106,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Geology & Rock Mechanics",
    "topic": "Unconfined Compressive Strength (UCS) as Primary Index Property",
    "question": "Which type of compressive strength is taken as the most important index property of stones ?",
    "options": {
      "A": "Confined",
      "B": "Drained",
      "C": "Undrained",
      "D": "Unconfined"
    },
    "correct_option": "D",
    "correct_text": "Unconfined (Unconfined/Uniaxial Compressive Strength, UCS, is the universal index property for intact rock classification, RMR, Q-system, and IS: 9143)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 286); IS: 9143 (1979); Deere & Miller (1966)",
    "file_html": "solutions/geology_2019/Q106_Compressive_Strength_Index_Property_Is_Unconfined_Complete_Guide.html",
    "icon": "🧱"
  },
  {
    "q": 107,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Geology & Rock Mechanics",
    "topic": "Compressive Strength: Maximum Force per Unit Area Without Rupturing",
    "question": "What is the maximum force expressed per unit area, which a stone can withstand without rupturing ?",
    "options": {
      "A": "Shear strength",
      "B": "Tensile strength",
      "C": "Compressive strength",
      "D": "Bending strength"
    },
    "correct_option": "C",
    "correct_text": "Compressive strength (Also termed crushing strength; the maximum uniaxial load per unit cross-sectional area before compressive failure)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 286); Parbin Singh; IS: 1121 (Part 1)",
    "file_html": "solutions/geology_2019/Q107_Maximum_Force_Per_Unit_Area_Without_Rupturing_Is_Compressive_Strength_Complete_Guide.html",
    "icon": "🏋️"
  },
  {
    "q": 108,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Geology & Building Stones",
    "topic": "Igneous Rocks Possess Very High Compressive Strength",
    "question": "Which rocks possess very high compressive strength ?",
    "options": {
      "A": "Igneous",
      "B": "Sedimentary",
      "C": "Metamorphic",
      "D": "Both sedimentary and metamorphic"
    },
    "correct_option": "A",
    "correct_text": "Igneous (Holocrystalline interlocking texture of plutonic/hypabyssal/volcanic rocks like granite, basalt, and dolerite yields UCS of 100-350 MPa)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 287); Krynine & Judd (1957)",
    "file_html": "solutions/geology_2019/Q108_Rocks_Possessing_Very_High_Compressive_Strength_Are_Igneous_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 109,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Rock Mass Index Properties & Petrophysics",
    "topic": "Porosity: Ratio of Total Pore Volume to Total Rock Volume",
    "question": "Ratio between the total volume of pore spaces to the total volume of the rock is a measure of :",
    "options": {
      "A": "Void ratio",
      "B": "Porosity",
      "C": "Pores ratio",
      "D": "Bulk density"
    },
    "correct_option": "B",
    "correct_text": "Porosity (n = V_v / V_T, expressed as a fraction or percentage; whereas Void Ratio e = V_v / V_s compares pore volume to solid volume)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 285); D.K. Todd (Groundwater Hydrology)",
    "file_html": "solutions/geology_2019/Q109_Ratio_Pore_Spaces_To_Total_Volume_Is_Porosity_Complete_Guide.html",
    "icon": "🧽"
  },
  {
    "q": 110,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Rock Mass Index Properties & Petrophysics",
    "topic": "Bulk Density: Density of Rock with Natural Moisture Content",
    "question": "The density of the rock with natural moisture content is known as :",
    "options": {
      "A": "Dry density",
      "B": "Wet density",
      "C": "Bulk density",
      "D": "Natural density"
    },
    "correct_option": "C",
    "correct_text": "Bulk density (Total in-situ mass including solid mineral grains and natural pore water divided by total bulk volume including voids)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 284); IS: 13030; Goodman (1989)",
    "file_html": "solutions/geology_2019/Q110_Density_Of_Rock_With_Natural_Moisture_Is_Bulk_Density_Complete_Guide.html",
    "icon": "⚖️"
  },
  {
    "q": 111,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Geology & Aggregate Testing",
    "topic": "Impact Testing of Stone Determines Toughness",
    "question": "The impact testing of a stone is done to know the :",
    "options": {
      "A": "Durability",
      "B": "Porosity",
      "C": "Density",
      "D": "Toughness"
    },
    "correct_option": "D",
    "correct_text": "Toughness (Resistance of stone to fracture under sudden dynamic impact blows, measured via Page Impact Test or Aggregate Impact Value IS: 2386)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 291); IS: 2386 (Part IV); Parbin Singh",
    "file_html": "solutions/geology_2019/Q111_Impact_Testing_Of_Stone_Done_To_Know_Toughness_Complete_Guide.html",
    "icon": "🔨"
  },
  {
    "q": 112,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Tunneling & Underground Rock Mechanics",
    "topic": "Sudden Release of Tectonic/Overburden Stress in Tunneling: Rock Bursts",
    "question": "The sudden release of stress in rocks during tunneling will normally result in :",
    "options": {
      "A": "Rock fall",
      "B": "Rock bursts",
      "C": "Blockage",
      "D": "Water gush"
    },
    "correct_option": "B",
    "correct_text": "Rock bursts (Explosive, violent brittle spalling and ejection of hard rock slabs from tunnel walls due to sudden release of stored elastic strain energy)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 338); E. Hoek & E.T. Brown (1980)",
    "file_html": "solutions/geology_2019/Q112_Sudden_Release_Of_Stress_In_Tunneling_Results_In_Rock_Bursts_Complete_Guide.html",
    "icon": "💥"
  },
  {
    "q": 113,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Structural & Tunnel Engineering Geology",
    "topic": "Strata Dipping up to 45 Degrees: Moderately Inclined Strata",
    "question": "Strata dipping at angles upto 45° are called :",
    "options": {
      "A": "Moderately inclined strata",
      "B": "Steeply inclined strata",
      "C": "Plunge",
      "D": "Overturned"
    },
    "correct_option": "A",
    "correct_text": "Moderately inclined strata (In engineering geology classification of dip angles, beds dipping up to 45° are termed moderately inclined; >45° are steeply inclined)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 332); Parbin Singh",
    "file_html": "solutions/geology_2019/Q113_Strata_Dipping_Upto_45_Degrees_Are_Moderately_Inclined_Complete_Guide.html",
    "icon": "📐"
  },
  {
    "q": 114,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Dam Foundations & Geotechnical Remediation",
    "topic": "Geological Structure Rectified by Grouting: Rock Joints",
    "question": "Which type of geological structure can be rectified by grouting ?",
    "options": {
      "A": "Joints",
      "B": "Folds",
      "C": "Faults",
      "D": "Inclined strata"
    },
    "correct_option": "A",
    "correct_text": "Joints (Open fractures without displacement are completely sealed and monolithically consolidated by injecting cement or chemical slurry under pressure)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 312); IS: 6066; Krynine & Judd",
    "file_html": "solutions/geology_2019/Q114_Geological_Structure_Rectified_By_Grouting_Is_Joints_Complete_Guide.html",
    "icon": "💉"
  },
  {
    "q": 115,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Rock Mechanics & Strength Anisotropy",
    "topic": "Strength of Compact Rock is Greatest Normal to Bedding Planes",
    "question": "When is the strength of a compact rock always greater ?",
    "options": {
      "A": "When stresses are normal to bedding planes",
      "B": "When stresses are parallel to bedding planes",
      "C": "When stresses are inclined at 45° to bedding planes",
      "D": "When stresses are inclined at 60° to bedding planes"
    },
    "correct_option": "A",
    "correct_text": "When stresses are normal to bedding planes (Compressive load perpendicular to bedding closes the planes and forces shear failure across intact rock layers)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 287); F.A. Donath (1961); J.C. Jaeger (1960)",
    "file_html": "solutions/geology_2019/Q115_Strength_Of_Compact_Rock_Greater_Normal_To_Bedding_Planes_Complete_Guide.html",
    "icon": "⬇️"
  },
  {
    "q": 116,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Dam Site Selection & Foundation Geology",
    "topic": "Best Site for Dam Construction: A Site with Granitic Bedrock",
    "question": "Which of the following could be the best site for a dam construction ?",
    "options": {
      "A": "A site with a granitic bedrock",
      "B": "A site with good shear fractures",
      "C": "Lateritic zone",
      "D": "A site with limestone bedrock"
    },
    "correct_option": "A",
    "correct_text": "A site with a granitic bedrock (Massive plutonic granite offers high crushing strength 100-250 MPa, zero chemical solubility, and negligible primary permeability)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 302); Parbin Singh; F.G. Bell",
    "file_html": "solutions/geology_2019/Q116_Best_Site_For_Dam_Construction_Granitic_Bedrock_Complete_Guide.html",
    "icon": "🏞️"
  },
  {
    "q": 117,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Properties of Building Stones",
    "topic": "Granite Possesses Very High Crushing Strength",
    "question": "Which of the following is true about granite ?",
    "options": {
      "A": "It has very high crushing strength",
      "B": "It takes poor polish",
      "C": "It is a highly porous rock",
      "D": "It weathers out faster"
    },
    "correct_option": "A",
    "correct_text": "It has very high crushing strength (1000 to 2500 kg/cm2 or 100-250 MPa due to its interlocking holocrystalline quartz-feldspar texture)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 296); IS: 3316 (1974)",
    "file_html": "solutions/geology_2019/Q117_True_About_Granite_Very_High_Crushing_Strength_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 118,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Highway Engineering & Road Metal Aggregates",
    "topic": "Undesirable Property for Road Metal: Highly Porous & Permeable / Strongly Sheared",
    "question": "Which of the following is not a desirable property for a road metal ?",
    "options": {
      "A": "Should be hydrophobic",
      "B": "Should have sufficient crushing strength",
      "C": "Should be strongly sheared",
      "D": "Should be highly porous and permeable"
    },
    "correct_option": "D",
    "correct_text": "Should be highly porous and permeable (and Option C: Should be strongly sheared; road metal must be non-porous/impermeable, unsheared, hydrophobic, and strong)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 299-300); IRC / IS: 2386",
    "file_html": "solutions/geology_2019/Q118_Not_Desirable_Property_For_Road_Metal_Strongly_Sheared_Porous_Complete_Guide.html",
    "icon": "🛣️"
  },
  {
    "q": 119,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Building Stones & Quarry Economics",
    "topic": "Workability: Ease of Extracting and Dressing Building Stone",
    "question": "Ease with which a stone can be extracted and dressed is called :",
    "options": {
      "A": "Consistency",
      "B": "Workability",
      "C": "Easability",
      "D": "Permeability"
    },
    "correct_option": "B",
    "correct_text": "Workability (The ease and economy with which a stone is quarried, split, cut, chiseled, and dressed into required masonry dimensions)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 295); Parbin Singh",
    "file_html": "solutions/geology_2019/Q119_Ease_With_Which_Stone_Extracted_And_Dressed_Is_Workability_Complete_Guide.html",
    "icon": "⛏️"
  },
  {
    "q": 120,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Metamorphic Building Stones & Roofing Materials",
    "topic": "Slate Used as Roofing Slab Due to Perfect Slaty Cleavage",
    "question": "Which of the following materials is generally used as a roofing slab ?",
    "options": {
      "A": "Slate",
      "B": "Granite",
      "C": "Marble",
      "D": "Gneiss"
    },
    "correct_option": "A",
    "correct_text": "Slate (Low-grade metamorphic rock with penetrative slaty cleavage allowing splitting into thin, lightweight, impervious roofing slabs)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 298); IS: 6250 (1981)",
    "file_html": "solutions/geology_2019/Q120_Material_Generally_Used_As_Roofing_Slab_Is_Slate_Complete_Guide.html",
    "icon": "🏠"
  }
]

with open('data/geology_2019.json', 'r') as f:
    existing_data = json.load(f)

existing_qs = {item['q'] for item in existing_data}
new_items = [item for item in batch9_items if item['q'] not in existing_qs]

updated_data = existing_data + new_items
updated_data.sort(key=lambda x: x['q'])

with open('data/geology_2019.json', 'w') as f:
    json.dump(updated_data, f, indent=2)

print(f"Updated data/geology_2019.json: Total entries = {len(updated_data)}")
