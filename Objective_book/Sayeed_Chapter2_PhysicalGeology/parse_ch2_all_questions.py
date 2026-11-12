#!/usr/bin/env python3
"""
Comprehensive Verified Dataset Builder for Chapter 2: Physical Geology and Geomorphology
Dr. Ausaf Sayeed - Objective Geology (145 Questions)
"""

import os
import json
import re

BASE_DIR = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter2_PhysicalGeology"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Complete Official Answer Key (Q1 to Q145) from Book pp. 142-143
ANS_KEY = {
    1: 'C', 2: 'D', 3: 'D', 4: 'A', 5: 'A', 6: 'A', 7: 'B', 8: 'D', 9: 'D', 10: 'B',
    11: 'D', 12: 'C', 13: 'B', 14: 'B', 15: 'C', 16: 'C', 17: 'A', 18: 'C', 19: 'B', 20: 'D',
    21: 'C', 22: 'A', 23: 'B', 24: 'A', 25: 'B', 26: 'A', 27: 'C', 28: 'A', 29: 'A', 30: 'C',
    31: 'D', 32: 'D', 33: 'D', 34: 'B', 35: 'C', 36: 'A', 37: 'A', 38: 'B', 39: 'A', 40: 'C',
    41: 'B', 42: 'A', 43: 'D', 44: 'B', 45: 'A', 46: 'D', 47: 'A', 48: 'A', 49: 'B', 50: 'C',
    51: 'A', 52: 'D', 53: 'A', 54: 'B', 55: 'C', 56: 'B', 57: 'B', 58: 'D', 59: 'A', 60: 'B',
    61: 'B', 62: 'C', 63: 'B', 64: 'B', 65: 'A', 66: 'C', 67: 'B', 68: 'B', 69: 'D', 70: 'C',
    71: 'A', 72: 'C', 73: 'C', 74: 'D', 75: 'B', 76: 'C',
    77: 'D', 78: 'D', 79: 'B', 80: 'C', 81: 'D', 82: 'B', 83: 'B', 84: 'A', 85: 'C', 86: 'C',
    87: 'A', 88: 'C', 89: 'A', 90: 'D', 91: 'C', 92: 'C', 93: 'D', 94: 'C', 95: 'A', 96: 'B',
    97: 'A', 98: 'D', 99: 'A', 100: 'B', 101: 'A', 102: 'A', 103: 'C', 104: 'B', 105: 'A', 106: 'C',
    107: 'D', 108: 'A', 109: 'C', 110: 'B', 111: 'B', 112: 'C', 113: 'C', 114: 'A', 115: 'D', 116: 'C',
    117: 'B', 118: 'B', 119: 'C', 120: 'B', 121: 'D', 122: 'D', 123: 'D', 124: 'A', 125: 'B', 126: 'B',
    127: 'C', 128: 'C', 129: 'A', 130: 'D', 131: 'B', 132: 'D', 133: 'A', 134: 'C', 135: 'C', 136: 'C',
    137: 'A', 138: 'B', 139: 'C', 140: 'D', 141: 'C', 142: 'C', 143: 'C', 144: 'A', 145: 'A'
}

# 2. Authoritative Explanatory Notes transcribed from pp. 143-144
EXPLANATORY_NOTES = {
    7: "Hydrated minerals tend to expand many times their original volume of anhydrous minerals. Therefore, they become more porous and attain a lower density (e.g., Anhydrite CaSO4: density 2.61 g/cm³; Gypsum CaSO4·2H2O: density 2.32 g/cm³, volume change +42.27%).",
    18: "Serir is a stony desert composed of extensive sheets of gravel or boulders. It is also known as Reg or Harras.",
    39: "Radial drainage patterns are associated with domal uplifts, slopes of volcanoes, large basins and gulf depressions. Choices (b) and (c) exhibit trellis pattern while (d) exhibits dendritic pattern.",
    41: "The other three features (meanders, piedmont plains, and sloughs) are associated with the middle/lower course of a river. River piracy (stream capture) is characteristic of vigorous headward erosion in the youthful upper course. Piedmont plains are formed by coalescing alluvial fans; sloughs are depressions on floodplains.",
    48: "Nunataks are isolated rocky mountain peaks projecting above surrounding ice sheets or glaciers. Choice (b) refers to knob and kettle topography, (c) refers to pingos, and (d) refers to incised meanders.",
    119: "'Island of Mountains' refers to inselbergs (isolated pillar-like or domal steep-sided rock masses in arid/semi-arid plains). Kame terraces are flat-topped alluvial depositional terraces along glaciated valley walls, not islands of mountains.",
    122: "Star dunes (radially symmetrical pyramidal dunes) have 3 or more sinuous arms and slip faces radiating from a central peak, formed by multidirectional, variable wind regimes.",
    130: "Yazoo-type rivers run parallel to the master stream on the floodplain for tens to hundreds of miles before entering it, blocked from immediate junction by well-developed natural levees. Named after the Yazoo River which parallels the Mississippi River for nearly 200 miles.",
    132: "Pater noster lakes are a chain of small glacial rock-basin tarns or tarn lakes stepped down a glaciated U-shaped valley, resembling beads of a rosary, excavated by glacial plucking behind resistant rock bars.",
    134: "Lahars are catastrophic volcanic mudflows/debris flows formed when pyroclastic debris mixes with torrential rain, snowmelt, or crater lake waters. Bioherms are ancient mound-like limestone deposits of organic origin. Faros are small circular or oblong reef atolls enclosing shallow lagoons.",
    135: "Uplifted (rejuvenated) peneplains are diagnostically identified by: accordant interstream summit levels; topographic unconformities (nick points); truncation of diverse strata and rock formations of varying resistance; drainage superimposition or adaptation; monadnocks/erosion remnants; incised meanders; and deep residual paleosols on summits.",
    145: "Basin and Range topography is formed by crustal extension and normal faulting (tilted fault blocks / horsts and grabens), producing alternating linear mountain ranges and sediment-filled downfaulted basins, exemplified by the Great Basin province in the American Cordillera."
}

print(f"Loaded {len(ANS_KEY)} official answers and {len(EXPLANATORY_NOTES)} explanatory notes.")
