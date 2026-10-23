#!/usr/bin/env python3
"""
Update data/geology_2019.json with Batch 1 and Batch 2 (Q001 to Q024)
"""

import json
import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
JSON_PATH = os.path.join(BASE_DIR, "data", "geology_2019.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    existing_data = json.load(f)

# Keep first 10
master_data = existing_data[:10]

batch2_entries = [
    {
        "q": 11,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Aeolian Dune Classification: Barchans & Transverse Wind Dynamics",
        "question": "A sand dune with its long axis transverse to wind direction is called :",
        "options": {
            "A": "Longitudinal dune",
            "B": "Sand ridge",
            "C": "Parallel dune",
            "D": "Barchan"
        },
        "correct_option": "D",
        "correct_text": "Barchan (Crescentic dune with crest axis oriented transverse to wind and horns pointing downwind)",
        "textbook_ref": "Ralph A. Bagnold (The Physics of Blown Sand, 1941); K.M. Bangar (Principles of Engineering Geology, p. 23); Sam Boggs Jr. (Ch. 8, pp. 268-274)",
        "file_html": "solutions/geology_2019/Q011_Sand_Dune_Barchan_Transverse_Axis_Complete_Guide.html",
        "icon": "🏜️"
    },
    {
        "q": 12,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Glaciofluvial Eskers: Subglacial Pressurized Channel Drift",
        "question": "Esker is a :",
        "options": {
            "A": "Thoroughly graded bed",
            "B": "Deposit formed by wind action",
            "C": "Glaciofluvial deposit",
            "D": "Alluvial deposit rich in clay matter"
        },
        "correct_option": "C",
        "correct_text": "Glaciofluvial deposit (Stratified sand and gravel ridge deposited by subglacial meltwater streams)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 32); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 8, pp. 280-285)",
        "file_html": "solutions/geology_2019/Q012_Esker_Glaciofluvial_Deposit_Complete_Guide.html",
        "icon": "❄️"
    },
    {
        "q": 13,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Sedimentary Petrology & Carbonates",
        "topic": "Speleothem Morphogenesis: Stalactites, Stalagmites & Karst Solution",
        "question": "Development of stalactite and stalagmite is associated with :",
        "options": {
            "A": "Abrasion of valley floor",
            "B": "Solution activity",
            "C": "Sorting process",
            "D": "Organic activity in ocean beds"
        },
        "correct_option": "B",
        "correct_text": "Solution activity (Chemical dissolution of carbonate rock followed by CO2 degassing and calcite precipitation)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 38); Derek Ford & Paul Williams (Karst Hydrogeology and Geomorphology, 2007)",
        "file_html": "solutions/geology_2019/Q013_Stalactite_Stalagmite_Solution_Activity_Complete_Guide.html",
        "icon": "🪨"
    },
    {
        "q": 14,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Engineering Geology & Geomorphology",
        "topic": "Mechanics of Mass Wasting: Gravitational Driving Forces & Limit Equilibrium",
        "question": "Mass wasting is primarily affected by :",
        "options": {
            "A": "Force of gravity",
            "B": "Intensity of oxidation",
            "C": "Intensity of carbonization",
            "D": "Strength of streams"
        },
        "correct_option": "A",
        "correct_text": "Force of gravity (Direct downslope movement of rock and soil driven by gravitational shear stress)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, pp. 377-380); Karl Terzaghi (Theoretical Soil Mechanics, 1943); D.J. Varnes (1978)",
        "file_html": "solutions/geology_2019/Q014_Mass_Wasting_Force_of_Gravity_Complete_Guide.html",
        "icon": "⛰️"
    },
    {
        "q": 15,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Dendritic Drainage Networks: Structural Isotropy & Topologic Branching",
        "question": "If a region is lacking in structural control, then the drainage pattern in such regions will be :",
        "options": {
            "A": "Dendritic",
            "B": "Trellis",
            "C": "Rectangular",
            "D": "Radial"
        },
        "correct_option": "A",
        "correct_text": "Dendritic (Tree-like branching network developing on homogeneous, structurally isotropic rocks)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 27); Arthur L. Bloom (Geomorphology, Ch. 11, pp. 272-276)",
        "file_html": "solutions/geology_2019/Q015_Dendritic_Drainage_Pattern_No_Structural_Control_Complete_Guide.html",
        "icon": "🌳"
    },
    {
        "q": 16,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Volcanology, Weathering & Mass Wasting",
        "topic": "Volcanic Calderas: Summit Collapse & Magma Chamber Drainage",
        "question": "A Caldera is :",
        "options": {
            "A": "A very large crater",
            "B": "A long mountain chain",
            "C": "A gorge formed due to faulting",
            "D": "A U-shaped valley"
        },
        "correct_option": "A",
        "correct_text": "A very large crater (Large basin-shaped collapse depression formed by roof subsidence into an evacuated magma chamber)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 15); Gordon A. Macdonald (Volcanoes, 1972); Peter W. Lipman (1997)",
        "file_html": "solutions/geology_2019/Q016_Caldera_Large_Volcanic_Crater_Complete_Guide.html",
        "icon": "🌋"
    },
    {
        "q": 17,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Fault Rocks: Rock Flour, Fault Gouge & Brittle Cataclasis",
        "question": "Rock flour or gouge is closely linked to :",
        "options": {
            "A": "Ductile deformation",
            "B": "Brittle deformation",
            "C": "Flow of incompetent beds",
            "D": "Collapse structures"
        },
        "correct_option": "B",
        "correct_text": "Brittle deformation (Mechanical pulverization, crushing, and frictional grinding in upper crustal shear zones)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 215); Marland P. Billings (Structural Geology, pp. 150-154); Richard H. Sibson (1977)",
        "file_html": "solutions/geology_2019/Q017_Fault_Gouge_Rock_Flour_Brittle_Deformation_Complete_Guide.html",
        "icon": "🔨"
    },
    {
        "q": 18,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Fault Plane Attitude: Hade, Dip & Coordinate Transformations",
        "question": "The angle which the fault plane makes with vertical plane is known as :",
        "options": {
            "A": "Net slip",
            "B": "Heave",
            "C": "Strike slip",
            "D": "Hade"
        },
        "correct_option": "D",
        "correct_text": "Hade (Complement of the dip angle: Hade = 90° - Dip)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 208); Marland P. Billings (Structural Geology, pp. 138-142)",
        "file_html": "solutions/geology_2019/Q018_Fault_Hade_Angle_with_Vertical_Plane_Complete_Guide.html",
        "icon": "📐"
    },
    {
        "q": 19,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Normal Faulting Kinematics & Andersonian Extensional Tectonics",
        "question": "If the hanging wall in a fault is in downthrown side, it is called :",
        "options": {
            "A": "Reverse fault",
            "B": "Normal fault",
            "C": "Tear fault",
            "D": "Hinge fault"
        },
        "correct_option": "B",
        "correct_text": "Normal fault (Dip-slip fault where hanging wall moves downward relative to footwall under extensional stress)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 209); E.M. Anderson (The Dynamics of Faulting, 1905); Haakon Fossen (Ch. 9)",
        "file_html": "solutions/geology_2019/Q019_Normal_Fault_Hanging_Wall_Downthrown_Complete_Guide.html",
        "icon": "⚡"
    },
    {
        "q": 20,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Fold Geometry: Hinge Lines, Fold Axes & Profile Planes",
        "question": "The line which is parallel to the hinge in a fold is called :",
        "options": {
            "A": "Axis of the fold",
            "B": "Axial plane of the fold",
            "C": "Crest of the fold",
            "D": "Plunge of the fold"
        },
        "correct_option": "A",
        "correct_text": "Axis of the fold (The imaginary line generator which is parallel to the hinge line in cylindrical folds)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 185); Marland P. Billings (Structural Geology, pp. 35-42); John G. Ramsay (1967)",
        "file_html": "solutions/geology_2019/Q020_Fold_Axis_Parallel_to_Hinge_Complete_Guide.html",
        "icon": "➰"
    },
    {
        "q": 21,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Recumbent Folds: Horizontal Axial Planes & Nappe Tectonics",
        "question": "If the axial plane of the fold is horizontal, then it is said to be :",
        "options": {
            "A": "Open fold",
            "B": "Tight fold",
            "C": "Recumbent fold",
            "D": "Isoclinal fold"
        },
        "correct_option": "C",
        "correct_text": "Recumbent fold (Fold with subhorizontal axial plane, dip <10°, and completely inverted lower limb)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 190); M.J. Fleuty (Proceedings of the Geologists' Association, 1964)",
        "file_html": "solutions/geology_2019/Q021_Recumbent_Fold_Horizontal_Axial_Plane_Complete_Guide.html",
        "icon": "🔄"
    },
    {
        "q": 22,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Global Geotectonics & Paleontology",
        "topic": "Unconformity Taxonomy: Blended Contacts & Paleosol Preservation",
        "question": "A contact of younger sediments deposited over a thick residual soil that grades into underlying bedrock is called :",
        "options": {
            "A": "Discontinuity",
            "B": "Non-conformity",
            "C": "Blended unconformity",
            "D": "Angular unconformity"
        },
        "correct_option": "C",
        "correct_text": "Blended unconformity (Transitional, fuzzy contact preserving in-situ residual soil grading downward into bedrock)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 225); Dunbar & Rodgers (Principles of Stratigraphy, 1957); Sam Boggs Jr. (Ch. 12)",
        "file_html": "solutions/geology_2019/Q022_Blended_Unconformity_Residual_Soil_Contact_Complete_Guide.html",
        "icon": "⏳"
    },
    {
        "q": 23,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Tectonic Fabric: Bedding-Cleavage Intersection Lineations (L0xS1)",
        "question": "The intersection of bedding and cleavage produces :",
        "options": {
            "A": "Lineation",
            "B": "Boudin",
            "C": "Mullion structure",
            "D": "Joint"
        },
        "correct_option": "A",
        "correct_text": "Lineation (Intersection lineation parallel to fold hinge line formed by intersection of S0 bedding and S1 cleavage)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 235); John G. Ramsay & Martin I. Huber (Vol. 2, 1983); Marland P. Billings (pp. 340-345)",
        "file_html": "solutions/geology_2019/Q023_Intersection_Bedding_Cleavage_Lineation_Complete_Guide.html",
        "icon": "✏️"
    },
    {
        "q": 24,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Fault Classification: High-Angle vs. Low-Angle (45° Threshold)",
        "question": "High angle faults are those that dip greater than :",
        "options": {
            "A": "60 degree",
            "B": "65 degree",
            "C": "40 degree",
            "D": "45 degree"
        },
        "correct_option": "D",
        "correct_text": "45 degree (High-angle faults dip >45° where throw exceeds heave; low-angle faults dip ≤45° where heave exceeds throw)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 212); Marland P. Billings (Structural Geology, pp. 145-148); Haakon Fossen (Ch. 9)",
        "file_html": "solutions/geology_2019/Q024_High_Angle_Faults_Dip_Greater_45_Degrees_Complete_Guide.html",
        "icon": "📏"
    }
]

master_data.extend(batch2_entries)

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(master_data, f, indent=2)

print(f"Updated {JSON_PATH} successfully with {len(master_data)} questions (Q001 - Q024).")
