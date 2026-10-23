import json

data_file = "data/geology_2019.json"
with open(data_file, "r", encoding="utf-8") as f:
    items = json.load(f)

# Ensure only up to Q35 exists currently before appending
items = [item for item in items if item["q"] < 36]

new_items = [
  {
    "q": 36,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geomorphology & Weathering Dynamics",
    "topic": "Physical Weathering: Exfoliation & Spheroidal Spalling in Massive Rocks",
    "question": "The process of weathering by exfoliating activity is very effective in:",
    "options": {
      "A": "Layered rocks",
      "B": "Massive rocks",
      "C": "Jointed rocks",
      "D": "Foliated rocks"
    },
    "correct_option": "B",
    "correct_text": "Massive rocks (Homogeneous isotropic rocks devoid of bedding or foliation spall off curved concentric shells due to thermal insolation and chemical hydration stresses)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 20); G.B. Mahapatra (Textbook of Geology, p. 45); P.K. Mukherjee (p. 28)",
    "file_html": "solutions/geology_2019/Q036_Weathering_Exfoliating_Activity_Massive_Rocks_Complete_Guide.html",
    "icon": "🪨"
  },
  {
    "q": 37,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Volcanology & Igneous Petrology",
    "topic": "Eruption Mechanics: Pelean Type Volcanoes & Most Violent Activity",
    "question": "Pelean type of volcano is known for:",
    "options": {
      "A": "Most violent activity",
      "B": "Quiet flow",
      "C": "Submarine flow",
      "D": "Ropy type flow"
    },
    "correct_option": "A",
    "correct_text": "Most violent activity (Characterized by extremely viscous dacitic lava spines, catastrophic dome collapses, lateral blasts, and incandescent nuées ardentes)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 49); Cas & Wright (Volcanic Successions); G.B. Mahapatra (p. 55)",
    "file_html": "solutions/geology_2019/Q037_Pelean_Volcano_Most_Violent_Activity_Complete_Guide.html",
    "icon": "🌋"
  },
  {
    "q": 38,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Volcanology & Geomorphology",
    "topic": "Volcanic Edifices: Stratovolcanoes & Composite Cone Architecture",
    "question": "Composite cones are the characteristics of :",
    "options": {
      "A": "Strato volcanoes",
      "B": "Cinder cone volcanoes",
      "C": "Shield volcano",
      "D": "Lava domes"
    },
    "correct_option": "A",
    "correct_text": "Strato volcanoes (Stratified conical edifices constructed from alternating layers of explosive pyroclastic tephra and solidified intermediate/felsic lava flows)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 48); Tarbuck & Lutgens (Earth Science); Philpotts & Ague (Igneous Petrology)",
    "file_html": "solutions/geology_2019/Q038_Composite_Cones_Stratovolcanoes_Characteristics_Complete_Guide.html",
    "icon": "🗻"
  },
  {
    "q": 39,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geophysics & Planetary Geodynamics",
    "topic": "Isostasy: Airy's Model of Mountain Roots & Flotation in Denser Substratum",
    "question": "According to Airy’s theory of isostasy :",
    "options": {
      "A": "Lighter mountains are floating on the lighter substratum",
      "B": "Lighter mountains are floating on the denser substratum",
      "C": "Denser mountains are floating on denser substratum",
      "D": "Denser mountains are floating on the lighter substratum"
    },
    "correct_option": "B",
    "correct_text": "Lighter mountains are floating on the denser substratum (Light crustal rocks of uniform density ~2.8 g/cm³ float in hydrostatic equilibrium upon a denser ~3.3 g/cm³ mantle substratum, supported by deep roots)",
    "textbook_ref": "Sir George Biddell Airy (1855); K.M. Bangar (p. 32); C.M.R. Fowler (The Solid Earth, p. 195); Turcotte & Schubert (Geodynamics)",
    "file_html": "solutions/geology_2019/Q039_Airy_Theory_Isostasy_Mountains_Floating_Denser_Substratum_Complete_Guide.html",
    "icon": "⚖️"
  },
  {
    "q": 40,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geotectonics & Marine Geology",
    "topic": "Continental Margins: Atlantic Passive Margin Architecture",
    "question": "The Atlantic continental margin of North America is known to be :",
    "options": {
      "A": "An active margin",
      "B": "Passive margin",
      "C": "Suture zone",
      "D": "Collision zone"
    },
    "correct_option": "B",
    "correct_text": "Passive margin (Stable intraplate trailing margin devoid of active subduction, volcanism, or trenches, featuring wide continental shelves and thick post-rift sedimentary prisms)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 34); Van der Pluijm & Marshak (Earth Structure, p. 437); Sam Boggs Jr. (p. 434)",
    "file_html": "solutions/geology_2019/Q040_Atlantic_Margin_North_America_Passive_Margin_Complete_Guide.html",
    "icon": "🏖️"
  },
  {
    "q": 41,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Oceanography & Marine Geology",
    "topic": "Planetary Hypsometry: Average Depth of the Global Ocean (3,729 m)",
    "question": "The average depth of the ocean is:",
    "options": {
      "A": "5,200 meters",
      "B": "4,630 meters",
      "C": "3,729 meters",
      "D": "3,062 meters"
    },
    "correct_option": "C",
    "correct_text": "3,729 meters (Classical geodetic datum representing total oceanic volume divided by oceanic surface area, forming the lower peak of Earth's bimodal hypsographic curve)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 35); Sverdrup, Johnson & Fleming (The Oceans, 1942); Thurman & Trujillo (Oceanography)",
    "file_html": "solutions/geology_2019/Q041_Average_Depth_Ocean_3729_Meters_Complete_Guide.html",
    "icon": "🌊"
  },
  {
    "q": 42,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Paleomagnetism & Geotectonics",
    "topic": "Paleomagnetism: Geomagnetic Pole Reversals & Seafloor Striping",
    "question": "Palaeomagnetic data is useful for understanding :",
    "options": {
      "A": "Pole reversals",
      "B": "Composition of mantle",
      "C": "Internal structure of the earth",
      "D": "Origin of life on earth"
    },
    "correct_option": "A",
    "correct_text": "Pole reversals (Thermo-remanent magnetization in basalt records spontaneous flips of Earth's magnetic dipole, proving the Vine-Matthews-Morley seafloor spreading hypothesis)",
    "textbook_ref": "Bernard Brunhes (1906); Motonori Matuyama (1929); K.M. Bangar (p. 28); Van der Pluijm & Marshak (Earth Structure, p. 445)",
    "file_html": "solutions/geology_2019/Q042_Palaeomagnetic_Data_Pole_Reversals_Complete_Guide.html",
    "icon": "🧭"
  },
  {
    "q": 43,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Marine Geomorphology",
    "topic": "Seamount Morphometry: Guyots as Wave-Beveled Flat-Topped Seamounts",
    "question": "Guyot is a :",
    "options": {
      "A": "Ridge of a fold mountain",
      "B": "Major depression in a continental area",
      "C": "Flat topped seamount",
      "D": "Flat topped hill on the surface"
    },
    "correct_option": "C",
    "correct_text": "Flat topped seamount (Submerged volcanic mountain whose peak was beveled flat by wave action at sea level and subsequently drowned to deep water by lithospheric thermal subsidence)",
    "textbook_ref": "Harry H. Hess (1946); K.M. Bangar (Principles of Engineering Geology, p. 36); Thurman & Trujillo (Essentials of Oceanography)",
    "file_html": "solutions/geology_2019/Q043_Guyot_Flat_Topped_Seamount_Complete_Guide.html",
    "icon": "⛰️"
  },
  {
    "q": 44,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Geotectonics & Subduction Zones",
    "topic": "Subduction Geomorphology: Deep Sea Trenches of the Circum-Pacific Belt",
    "question": "Deep sea trenches are generally associated with :",
    "options": {
      "A": "Circum pacific belt",
      "B": "Mid-oceanic ridges",
      "C": "Island arcs",
      "D": "Collisional areas"
    },
    "correct_option": "A",
    "correct_text": "Circum pacific belt (Over 80% of Earth's oceanic deep-sea trenches encircle the Pacific Ocean basin along convergent subduction zones consuming oceanic lithosphere)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 36 & p. 50); C.M.R. Fowler (The Solid Earth); Tarbuck & Lutgens (Earth Science)",
    "file_html": "solutions/geology_2019/Q044_Deep_Sea_Trenches_Circum_Pacific_Belt_Complete_Guide.html",
    "icon": "🕳️"
  },
  {
    "q": 45,
    "paper_id": "geology_2019",
    "paper_name": "Geology Paper-II (2019)",
    "paper_code": "GGM - 2/2019",
    "section": "Solid Earth Geophysics & Geothermics",
    "topic": "Crustal Geothermics: Temperature in the Upper Lower Crust (400-500°C)",
    "question": "The temperature regime in the upper part of the lower crust is:",
    "options": {
      "A": "400-500°C",
      "B": "300-400°C",
      "C": "100-200°C",
      "D": "200-250°C"
    },
    "correct_option": "A",
    "correct_text": "400-500°C (Under standard continental geothermal gradients of 20-25°C/km, depths of 20-25 km at the Conrad discontinuity reach 400° to 500°C, marking plagioclase plastic creep)",
    "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 22); John D. Winter (Petrology, Ch. 1, p. 5); C.M.R. Fowler (The Solid Earth, p. 235)",
    "file_html": "solutions/geology_2019/Q045_Temperature_Regime_Upper_Lower_Crust_400_500_Complete_Guide.html",
    "icon": "🌡️"
  }
]

items.extend(new_items)
items.sort(key=lambda x: x["q"])

with open(data_file, "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)

print(f"data/geology_2019.json updated successfully! Total questions: {len(items)}")
