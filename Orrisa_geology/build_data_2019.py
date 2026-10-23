#!/usr/bin/env python3
"""
Populate data/geology_2019.json for Batch 1 (Q001 - Q010)
"""

import json
import os

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
JSON_PATH = os.path.join(DATA_DIR, "geology_2019.json")

batch1_data = [
    {
        "q": 1,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Bajada Geomorphology & Piedmont Alluvial Fan Coalescence",
        "question": "‘Bajada’ is a type of :",
        "options": {
            "A": "Glacial deposit",
            "B": "Alluvial fan",
            "C": "Meandering stream",
            "D": "Sand dune"
        },
        "correct_option": "B",
        "correct_text": "Alluvial fan (Compound coalescing alluvial fan apron along a mountain piedmont)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 25); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 8, pp. 235-242)",
        "file_html": "solutions/geology_2019/Q001_Bajada_Alluvial_Fan_Geomorphology_Complete_Guide.html",
        "icon": "⛰️"
    },
    {
        "q": 2,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Braided Stream Morphology & Leopold-Wolman Threshold",
        "question": "A stream consisting of interwoven channels is known as :",
        "options": {
            "A": "Fluvioglacial stream",
            "B": "Braided stream",
            "C": "Meandering stream",
            "D": "Matured valley stream"
        },
        "correct_option": "B",
        "correct_text": "Braided stream (Multi-thread interwoven channels separated by mobile braid bars)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 25); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 8, pp. 244-248); Leopold & Wolman (1957)",
        "file_html": "solutions/geology_2019/Q002_Braided_Stream_Interwoven_Channels_Complete_Guide.html",
        "icon": "🌊"
    },
    {
        "q": 3,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Canyon & Gorge Geomorphology: Vertical Bedrock Downcutting",
        "question": "A canyon is a :",
        "options": {
            "A": "A deep valley with vertical sides",
            "B": "A deep asymmetrical valley",
            "C": "Broad, matured stream course",
            "D": "Valley formed by aeolian activity"
        },
        "correct_option": "A",
        "correct_text": "A deep valley with vertical sides (Steep-walled chasm carved by vertical river incision exceeding slope wasting)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 24); Arthur Holmes (Principles of Physical Geology, pp. 524-528)",
        "file_html": "solutions/geology_2019/Q003_Canyon_Gorge_Vertical_Valley_Complete_Guide.html",
        "icon": "🏞️"
    },
    {
        "q": 4,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Structural Geology & Fault Mechanics",
        "topic": "Trellis Drainage Pattern & Structural Strike-Dip Control",
        "question": "A network of parallel or subparallel streams developed along strike and dip directions are known as :",
        "options": {
            "A": "Dendritic",
            "B": "Radial",
            "C": "Trellis",
            "D": "Domal"
        },
        "correct_option": "C",
        "correct_text": "Trellis (Parallel master streams along strike joined at right angles by dip tributaries)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 27); Arthur L. Bloom (Geomorphology, Ch. 11, pp. 272-276)",
        "file_html": "solutions/geology_2019/Q004_Trellis_Drainage_Pattern_Folded_Strata_Complete_Guide.html",
        "icon": "📐"
    },
    {
        "q": 5,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Global Geotectonics & Paleontology",
        "topic": "The Physics of Eustasy: Global Sea-Level Dynamics",
        "question": "The term ‘eustatic’ implies :",
        "options": {
            "A": "Worldwide changes in sea level",
            "B": "Erosion of land to peneplanation",
            "C": "Exhumation of rocks",
            "D": "Confluence of river streams"
        },
        "correct_option": "A",
        "correct_text": "Worldwide changes in sea level (Global synchronous sea-level changes driven by glacio-eustasy & tectono-eustasy)",
        "textbook_ref": "Eduard Suess (Das Antlitz der Erde, 1888); K.M. Bangar (Principles of Engineering Geology, p. 33); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 12)",
        "file_html": "solutions/geology_2019/Q005_Eustatic_Sea_Level_Fluctuations_Complete_Guide.html",
        "icon": "🌐"
    },
    {
        "q": 6,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Glacial Fiords: Overdeepened Troughs & Marine Drowning",
        "question": "Fiords are formed due to :",
        "options": {
            "A": "Lacustrine process",
            "B": "Wind action",
            "C": "Glacial activity",
            "D": "Alluvial activity"
        },
        "correct_option": "C",
        "correct_text": "Glacial activity (Submerged U-shaped glacial troughs overdeepened below sea level with a shallow seaward sill)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 31); Arthur L. Bloom (Geomorphology, Ch. 15, pp. 378-384)",
        "file_html": "solutions/geology_2019/Q006_Fiords_Glacial_Trough_Drowned_Valley_Complete_Guide.html",
        "icon": "❄️"
    },
    {
        "q": 7,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Sedimentary Petrology & Carbonates",
        "topic": "Aeolian Granulometry: Bagnold Saltation Physics & Sand Sorting",
        "question": "Well sorted aeolian deposits are chiefly composed of :",
        "options": {
            "A": "Clay",
            "B": "Sand",
            "C": "Sand and Silt",
            "D": "Silt and Clay"
        },
        "correct_option": "B",
        "correct_text": "Sand (Medium to fine quartz sand concentrated into dunes via saltation while silt/clay is winnowed into suspension)",
        "textbook_ref": "Ralph A. Bagnold (The Physics of Blown Sand, 1941); K.M. Bangar (Principles of Engineering Geology, p. 23); Sam Boggs Jr. (Ch. 8, pp. 268-274)",
        "file_html": "solutions/geology_2019/Q007_Aeolian_Sand_Sorting_Bagnold_Physics_Complete_Guide.html",
        "icon": "🏜️"
    },
    {
        "q": 8,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Horton's Drainage Density & Basin Morphometry",
        "question": "Drainage density of a basin is a measure of :",
        "options": {
            "A": "Total number of the highest order streams divided by the total number of the next lower order streams",
            "B": "Length of the largest stream divided by the total area of the basin",
            "C": "Total length of streams of all orders divided by the total area of the basin",
            "D": "Total number of streams of all orders"
        },
        "correct_option": "C",
        "correct_text": "Total length of streams of all orders divided by the total area of the basin (Horton, 1945: D_d = ΣL / A)",
        "textbook_ref": "Robert E. Horton (GSA Bulletin, 1945); Arthur N. Strahler (GSA Bulletin, 1957); K.M. Bangar (Principles of Engineering Geology, p. 27)",
        "file_html": "solutions/geology_2019/Q008_Drainage_Density_Horton_Basin_Morphometry_Complete_Guide.html",
        "icon": "📊"
    },
    {
        "q": 9,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Geomorphology & Quaternary Geology",
        "topic": "Glacial Moraines, Till Dynamics & Depositional Landforms",
        "question": "Moraines are formed in :",
        "options": {
            "A": "Lacustrine Environment",
            "B": "Glacial Environment",
            "C": "Alluvial Environment",
            "D": "Marine Environment"
        },
        "correct_option": "B",
        "correct_text": "Glacial Environment (Unsorted, unstratified till/diamicton ridges deposited by glacial ice)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 32); Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 8, pp. 275-282)",
        "file_html": "solutions/geology_2019/Q009_Glacial_Moraines_Till_Diamicton_Complete_Guide.html",
        "icon": "🏔️"
    },
    {
        "q": 10,
        "paper_id": "geology_2019",
        "paper_name": "Geology Paper-II (2019)",
        "paper_code": "GGM - 2/2019",
        "section": "Sedimentary Petrology & Carbonates",
        "topic": "Karst Topography, Carbonate Thermodynamics & Speleothems",
        "question": "Karst topography is most commonly developed in :",
        "options": {
            "A": "Shale bearing areas",
            "B": "Sandstone bearing areas",
            "C": "Laterite bearing areas",
            "D": "Limestone bearing areas"
        },
        "correct_option": "D",
        "correct_text": "Limestone bearing areas (Subterranean dissolution of soluble CaCO3 by carbonic acid forming sinkholes & caves)",
        "textbook_ref": "K.M. Bangar (Principles of Engineering Geology, p. 38); Derek Ford & Paul Williams (Karst Hydrogeology and Geomorphology, 2007)",
        "file_html": "solutions/geology_2019/Q010_Karst_Topography_Limestone_Dissolution_Complete_Guide.html",
        "icon": "🪨"
    }
]

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(batch1_data, f, indent=2)

print(f"Created {JSON_PATH} with {len(batch1_data)} questions.")
