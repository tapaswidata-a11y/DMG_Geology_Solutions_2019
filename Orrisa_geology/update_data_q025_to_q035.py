import json

data_file = "data/geology_2019.json"
with open(data_file, "r", encoding="utf-8") as f:
    items = json.load(f)

# Ensure only up to Q24 exists currently before appending
items = [item for item in items if item["q"] < 25]

new_items = [
  {
    "q": 25,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Structural Geology & Fold Geometry",
    "topic": "Conjugate Folds: Box Folds & Multiple Hinge Lines",
    "question": "In which fold there could be two hinges ?",
    "options": {
      "A": "Tight fold",
      "B": "Isoclinal fold",
      "C": "Overturned fold",
      "D": "Box fold"
    },
    "correct_option": "D",
    "correct_text": "Box fold (Conjugate fold possessing two distinct hinge lines and two intersecting axial surfaces bounding a flat crest or trough)",
    "textbook_ref": "K.M. Bangar (p. 115); Marland P. Billings (p. 61); Van der Pluijm & Marshak (Earth Structure, p. 259)",
    "file_html": "solutions/geology_2019/Q025_Box_Fold_Two_Hinges_Conjugate_Complete_Guide.html",
    "icon": "📦"
  },
  {
    "q": 26,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Structural Geology & Fold Geometry",
    "topic": "Fold Rheology: Disharmonic & Similar Folds (Hinge Thickening)",
    "question": "Thickened crests and troughs with thinner limbs are noticed in:",
    "options": {
      "A": "Open fold",
      "B": "Disharmonic fold",
      "C": "Buckle fold",
      "D": "Over fold"
    },
    "correct_option": "B",
    "correct_text": "Disharmonic fold (Incompetent strata undergo plastic ductile flow from limbs into crests and troughs, producing pronounced hinge thickening)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 114); Haakon Fossen (Structural Geology, p. 248); John G. Ramsay (Class 2 Folds)",
    "file_html": "solutions/geology_2019/Q026_Disharmonic_Folds_Hinge_Thickening_Limb_Thinning_Complete_Guide.html",
    "icon": "🌊"
  },
  {
    "q": 27,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Structural Geology & Map Interpretation",
    "topic": "Denudation Structures: Inlier vs. Outlier Map Patterns",
    "question": "On a geological map, if older strata are found to be surrounded by younger strata then it could be :",
    "options": {
      "A": "An inlier",
      "B": "An outlier",
      "C": "An overlap",
      "D": "Nappe structure"
    },
    "correct_option": "A",
    "correct_text": "An inlier (An exposure of older rocks completely surrounded by younger strata on a map, formed by erosion unroofing anticlines, domes, or valleys)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 124, Fig 7.49); Marland P. Billings (p. 89); P.K. Mukherjee (p. 182)",
    "file_html": "solutions/geology_2019/Q027_Inlier_Older_Strata_Surrounded_by_Younger_Complete_Guide.html",
    "icon": "🗺️"
  },
  {
    "q": 28,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geotectonics & Extensional Structures",
    "topic": "Plate Tectonics: Horst, Graben & Divergent Boundary Rifting",
    "question": "Horst and Graben structures are mainly confined to:",
    "options": {
      "A": "Transform boundaries",
      "B": "Subduction zones",
      "C": "Collision zones",
      "D": "Divergent boundaries"
    },
    "correct_option": "D",
    "correct_text": "Divergent boundaries (Extensional regimes with vertical maximum stress trigger conjugate normal faults, producing horsts and graben rift valleys)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 119); Haakon Fossen (p. 172); Van der Pluijm & Marshak (p. 430)",
    "file_html": "solutions/geology_2019/Q028_Horst_Graben_Divergent_Boundaries_Complete_Guide.html",
    "icon": "⛰️"
  },
  {
    "q": 29,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Engineering Geology & Petrology",
    "topic": "Plutonic Fracturing: Sheet Joints & Exfoliation in Granite",
    "question": "Granite usually exhibits :",
    "options": {
      "A": "Diagonal joints",
      "B": "Strike joints",
      "C": "Vertical joints",
      "D": "Sheet joints"
    },
    "correct_option": "D",
    "correct_text": "Sheet joints (Curvilinear fractures parallel to ground topography formed by elastic rebound and lithostatic pressure release during unroofing)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 123); Van der Pluijm & Marshak (Earth Structure, p. 163, Fig 7.7); Marland P. Billings",
    "file_html": "solutions/geology_2019/Q029_Sheet_Joints_Granite_Exfoliation_Unloading_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 30,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Structural Geology & Fold Kinematics",
    "topic": "Fold Attitude: Plunging Folds & Inclined Hinge Lines",
    "question": "The fold is said to have plunge if :",
    "options": {
      "A": "The axis is horizontal",
      "B": "The axis is not horizontal",
      "C": "It is asymmetrical",
      "D": "It is tightly folded"
    },
    "correct_option": "B",
    "correct_text": "The axis is not horizontal (A fold has a plunge if its hinge line/axis is inclined to the horizontal plane, causing V-shaped map outcrop closures)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 113, Fig 7.8); Marland P. Billings (p. 53); Haakon Fossen (p. 238)",
    "file_html": "solutions/geology_2019/Q030_Plunging_Fold_Axis_Not_Horizontal_Complete_Guide.html",
    "icon": "📐"
  },
  {
    "q": 31,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geotectonics & Continental Drift",
    "topic": "Paleogeography: Pangea Rifting into Laurasia & Gondwanaland",
    "question": "The two super continental blocks separated due to drifting are :",
    "options": {
      "A": "Pangea and Laurasia",
      "B": "Pangea and Gondwanaland",
      "C": "Laurasia and Gondwanaland",
      "D": "Laurasia and Panthalassa"
    },
    "correct_option": "C",
    "correct_text": "Laurasia and Gondwanaland (Early Mesozoic Tethyan rifting split Pangea into northern Laurasia and southern Gondwanaland)",
    "textbook_ref": "Alfred Wegener (1915); Eduard Suess (1885); K.M. Bangar (p. 28); Van der Pluijm & Marshak (Earth Structure, p. 580)",
    "file_html": "solutions/geology_2019/Q031_Laurasia_and_Gondwanaland_Pangea_Drift_Complete_Guide.html",
    "icon": "🌍"
  },
  {
    "q": 32,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geophysics & Geodynamics",
    "topic": "Earth's Thermal Engine: Convective Venting along Mid-Ocean Ridges",
    "question": "The convection energy of the earth is commonly released along:",
    "options": {
      "A": "Transform fault boundaries",
      "B": "Subduction zones",
      "C": "Divergent boundaries in oceans",
      "D": "Collision zones"
    },
    "correct_option": "C",
    "correct_text": "Divergent boundaries in oceans (Mid-ocean ridge spreading axes release over 70% of Earth's internal convective heat via decompression magma & hydrothermal venting)",
    "textbook_ref": "K.M. Bangar (p. 30); C.M.R. Fowler (The Solid Earth, Ch. 7); Turcotte & Schubert (Geodynamics); Van der Pluijm & Marshak (p. 438)",
    "file_html": "solutions/geology_2019/Q032_Convection_Energy_Divergent_Boundaries_Oceans_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 33,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Solid Earth Geophysics",
    "topic": "Planetary Discontinuities: The Mohorovicic Boundary (Moho)",
    "question": "Mohorovicic discontinuity separates :",
    "options": {
      "A": "Crust and Mantle",
      "B": "Inner core from outer core",
      "C": "Upper mantle from lower mantle",
      "D": "Mantle and core"
    },
    "correct_option": "A",
    "correct_text": "Crust and Mantle (Major seismic discontinuity where P-wave velocity jumps abruptly from ~6.8 km/s in the lower crust to ~8.1 km/s in uppermost peridotite mantle)",
    "textbook_ref": "Andrija Mohorovičić (1909); K.M. Bangar (p. 23); John D. Winter (Petrology, p. 3); C.M.R. Fowler (p. 102)",
    "file_html": "solutions/geology_2019/Q033_Mohorovicic_Discontinuity_Crust_Mantle_Complete_Guide.html",
    "icon": "⚡"
  },
  {
    "q": 34,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Solid Earth Geophysics & Rheology",
    "topic": "Rheological Stratification: Asthenosphere in the Upper Mantle",
    "question": "The asthenospheric layer inclued :",
    "options": {
      "A": "Crust and upper mantle",
      "B": "Lower and upper mantle",
      "C": "Crust and mantle",
      "D": "Mantle and core"
    },
    "correct_option": "B",
    "correct_text": "Upper mantle beneath lithosphere (Ductile, mechanically weak layer of the upper mantle between ~100 km and 410 km depth enabling plate drift)",
    "textbook_ref": "Joseph Barrell (1914); K.M. Bangar (p. 25); C.M.R. Fowler (The Solid Earth, p. 104); Turcotte & Schubert (Geodynamics)",
    "file_html": "solutions/geology_2019/Q034_Asthenosphere_Upper_Mantle_Layer_Complete_Guide.html",
    "icon": "🔥"
  },
  {
    "q": 35,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Solid Earth Geophysics & Planetary Interior",
    "topic": "Planetary Density Distribution: Earth's Core Density (10.7 g/cm³)",
    "question": "An average density of 1 0.7 gmicm? prevails at:",
    "options": {
      "A": "Upper mantle",
      "B": "Core",
      "C": "Lower crust",
      "D": "Lower mantle"
    },
    "correct_option": "B",
    "correct_text": "Core (Under the PREM model, density ranges from 9.9 to 12.2 g/cm³ in the outer core, averaging precisely 10.7 g/cm³)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 24); Dziewonski & Anderson (PREM, 1981); C.M.R. Fowler (p. 110)",
    "file_html": "solutions/geology_2019/Q035_Earth_Core_Density_10_7_gm_cm3_Complete_Guide.html",
    "icon": "🔬"
  }
]

items.extend(new_items)
items.sort(key=lambda x: x["q"])

with open(data_file, "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)

print(f"data/geology_2019.json updated successfully! Total questions: {len(items)}")
