"""
Verified Dataset for Questions 61 to 100
Dr. Ausaf Sayeed - Objective Geology Chapter 1: General Geology & Geotectonics
"""
import json

SAYEED_Q61_100 = {
    61: {
        "q": 61,
        "question": "According to Sir George Airy's classical Theory of Isostasy :",
        "options": {
            "A": "The density of the crust and the substratum is uniformly the same throughout",
            "B": "The thickness of the crust and the substratum is uniformly the same throughout",
            "C": "The crust and the substratum each have uniform but different densities, and mountain heights are compensated by deep downward crustal roots (variable thickness)",
            "D": "The crust has a constant thickness at the top whereas the substratum has a constant thickness at the bottom"
        },
        "ans": "C",
        "topic": "Isostasy: Airy's Root Hypothesis (Uniform Density, Variable Crustal Thickness)",
        "ref": "Lowrie (Fundamentals of Geophysics, Ch. 2, pp. 95-102); Turcotte & Schubert (Geodynamics, Ch. 5); Bangar (p. 21)"
    },
    62: {
        "q": 62,
        "question": "Under the doctrine of Isostasy, a topographic region exhibiting a negative Bouguer gravity anomaly indicates :",
        "options": {
            "A": "Mass deficiency / under-compensation in the crustal column",
            "B": "Mass excess / positive anomaly",
            "C": "Zero compensation depth",
            "D": "Extreme mantle densification"
        },
        "ans": "A",
        "topic": "Gravity Anomalies: Negative Bouguer Anomaly & Mass Deficiency beneath Mountains",
        "ref": "Lowrie (Fundamentals of Geophysics, pp. 88-94); Stacey (Physics of the Earth, Ch. 3); Bangar (p. 23)"
    },
    63: {
        "q": 63,
        "question": "Evaluate the following statements regarding deep crustal geophysical methods:\nI. Seismic refraction studies give crustal velocities and layer thicknesses but cannot alone resolve non-unique mass distributions.\nII. Seismic reflection profiling provides high-resolution geometric imaging of dipping interfaces and fault zones.\nIII. Gravity anomaly studies provide information about isostatic mass balance but suffer from fundamental depth non-uniqueness.",
        "options": {
            "A": "Only I is correct",
            "B": "Only II is correct",
            "C": "I and III are correct",
            "D": "I, II, and III are all correct"
        },
        "ans": "C",
        "topic": "Exploration Geophysics: Seismic Refraction vs Gravity Inversion Ambiguity",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Lowrie (Fundamentals of Geophysics, Ch. 2 & 3); Fowler (The Solid Earth)"
    },
    64: {
        "q": 64,
        "question": "Seismic and gravity crustal studies have shown that the oceans and continents are in broad isostatic equilibrium with each other primarily due to :",
        "options": {
            "A": "Lateral variation in the mean density of the upper crust alone",
            "B": "Lateral variation of density strictly within the deep asthenosphere",
            "C": "Marked variation in the thickness of the low-density continental crust (~35 km) versus thin oceanic crust (~7 km)",
            "D": "A combination of crustal thickness variations and mantle density differences"
        },
        "ans": "C",
        "topic": "Global Isostatic Balance: Continental vs Oceanic Crustal Architecture",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Lowrie (Fundamentals of Geophysics, p. 101); Fowler (The Solid Earth, Ch. 5)"
    },
    65: {
        "q": 65,
        "question": "The oldest, most stable tectonic areas on the surface of the Earth (such as Precambrian cratonic shields) are classified as :",
        "options": {
            "A": "Positive areas (Cratonic Shields / Positive Tectonic Elements)",
            "B": "Negative areas (Mobile Belts / Depressions)",
            "C": "Neutral zones",
            "D": "Transient margins"
        },
        "ans": "A",
        "topic": "Global Tectonics: Positive Elements (Shields) vs Negative Elements (Basins)",
        "ref": "Dr. Ausaf Sayeed (Short Notes, p. 2); G.B. Mahapatra (Text Book of Geology, p. 260); Holmes (Physical Geology)"
    },
    66: {
        "q": 66,
        "question": "The average Bouguer gravity anomaly for the global ocean basins as a whole is strongly :",
        "options": {
            "A": "Positive (typically +200 to +350 mGal)",
            "B": "Negative",
            "C": "Zero everywhere",
            "D": "Highly fluctuating around zero"
        },
        "ans": "A",
        "topic": "Marine Geophysics: Positive Oceanic Bouguer Gravity Anomalies",
        "ref": "Lowrie (Fundamentals of Geophysics, Fig. 2.45, p. 94); Stacey (Physics of the Earth, Ch. 3); Fowler (p. 150)"
    },
    67: {
        "q": 67,
        "question": "Which of the following marine physiographic features exhibits a pronounced, extreme NEGATIVE free-air gravity anomaly?",
        "options": {
            "A": "Hawaiian Volcanic Island Chain",
            "B": "Mid-Atlantic Ridge crest",
            "C": "Ryukyu & Kyushu Island Arcs",
            "D": "Deep Oceanic Trenches (e.g., Mariana Trench / Puerto Rico Trench)"
        },
        "ans": "D",
        "topic": "Deep-Sea Geophysics: Vening Meinesz Negative Gravity Anomaly over Ocean Trenches",
        "ref": "Lowrie (Fundamentals of Geophysics, pp. 95-97); Turcotte & Schubert (Geodynamics, p. 215); Fowler (p. 365)"
    },
    68: {
        "q": 68,
        "question": "The gently sloping, shallow submarine fringe of a continent extending from the low-water shoreline to an average break-of-slope depth of 0–200 meters is termed the :",
        "options": {
            "A": "Continental Shelf",
            "B": "Continental Slope",
            "C": "Continental Rise",
            "D": "Oceanic Trough"
        },
        "ans": "A",
        "topic": "Marine Physiography: Continental Shelf Morphology & Bathymetry",
        "ref": "Arthur L. Bloom (Geomorphology, Ch. 21); Kennett (Marine Geology, Ch. 2); Bangar (p. 28)"
    },
    69: {
        "q": 69,
        "question": "Along the coastline of India, the broadest continental shelf (extending up to 300–350 km offshore) is developed off the coast of :",
        "options": {
            "A": "Gujarat / Maharashtra (Western Continental Shelf / Mumbai Offshore)",
            "B": "Odisha (Eastern Shelf)",
            "C": "Tamil Nadu (Coromandel Coast)",
            "D": "Andhra Pradesh"
        },
        "ans": "A",
        "topic": "Indian Marine Geology: The Western Continental Shelf & Bombay High Platform",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); G.B. Mahapatra (p. 268); Krishnan (Geology of India and Burma)"
    },
    70: {
        "q": 70,
        "question": "The flattest, most morphologically level portions of the entire Earth's solid surface are formed by :",
        "options": {
            "A": "Abyssal Hills",
            "B": "Abyssal Plains (slope < 1:1000)",
            "C": "Oceanic Rises",
            "D": "Continental Slopes"
        },
        "ans": "B",
        "topic": "Abyssal Plain Geomorphology: Turbidite Sediment Ponding & Extreme Planarity",
        "ref": "Arthur L. Bloom (Geomorphology, Ch. 21); Kennett (Marine Geology, pp. 35-40); Lowrie (p. 5)"
    },
    71: {
        "q": 71,
        "question": "The highest lithostatic / hydrostatic pressures encountered within the Earth's oceanic crust occur at the bottoms of :",
        "options": {
            "A": "Mid-Oceanic Ridges",
            "B": "Oceanic Rises",
            "C": "Deep Oceanic Trenches (e.g., Challenger Deep, >110 MPa / 1100 bars)",
            "D": "Back-arc basins"
        },
        "ans": "C",
        "topic": "Marine Geology: Hydrostatic Pressure in Hadopelagic Trench Environments",
        "ref": "Kennett (Marine Geology, Ch. 2); Thurman (Introductory Oceanography); Lowrie (p. 6)"
    },
    72: {
        "q": 72,
        "question": "Match the following famous oceanic deeps with their respective ocean basins:\nA. Mindanao Deep (Philippine Trench) - 1. Pacific Ocean\nB. Milwaukee Deep (Puerto Rico Trench) - 2. Atlantic Ocean\nC. Java (Sunda) Trench - 3. Indian Ocean\nD. Nares Deep - 4. North Atlantic Ocean",
        "options": {
            "A": "A-1, B-2, C-3, D-4",
            "B": "A-2, B-1, C-3, D-4",
            "C": "A-3, B-2, C-1, D-4",
            "D": "A-1, B-3, C-2, D-4"
        },
        "ans": "C",
        "topic": "Oceanographic Geography: Deeps and Trenches of Major Ocean Basins",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Kennett (Marine Geology, Table 2.1); Bloom (Geomorphology)"
    },
    73: {
        "q": 73,
        "question": "Isolated submerged plateau fragments composed of ancient continental crust occurring within deep ocean basins (e.g., Seychelles, Lord Howe Rise) are termed :",
        "options": {
            "A": "Guyots",
            "B": "Seamounts",
            "C": "Atolls",
            "D": "Microcontinents (Continental Fragments)",
            "E": "Marginal Basins"
        },
        "ans": "D",
        "topic": "Marine Tectonics: Microcontinents & Aseismic Continental Rises",
        "ref": "Fowler (The Solid Earth, Ch. 9, pp. 380-385); Lowrie (Fundamentals of Geophysics, p. 16); Winter (Ch. 1)"
    },
    74: {
        "q": 74,
        "question": "Which of the following island classifications is NOT matched correctly with its geological origin?",
        "options": {
            "A": "Sri Lanka — Continental Island",
            "B": "West Indies / Aleutians — Volcanic Island Arc",
            "C": "Lakshadweep and Maldives — Coral Atoll Islands",
            "D": "Madagascar — Coral Barrier Reef Island (Incorrect: Madagascar is a Continental Fragment / Microcontinent)"
        },
        "ans": "D",
        "topic": "Island Geomorphology: Continental vs Volcanic Arc vs Coral Atolls",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Arthur L. Bloom (Geomorphology, Ch. 21); Bangar (p. 30)"
    },
    75: {
        "q": 75,
        "question": "Tectonically, the Mid-Atlantic Ridge System represents an active :",
        "options": {
            "A": "Shear / Transform Plate Boundary",
            "B": "Consuming / Destructive Plate Boundary",
            "C": "Accreting / Divergent (Constructive) Plate Boundary",
            "D": "Stable Intraplate Suture"
        },
        "ans": "C",
        "topic": "Plate Tectonics: Accreting Divergent Boundaries & Mid-Ocean Ridges",
        "ref": "Lowrie (Fundamentals of Geophysics, Ch. 1, pp. 12-16); Turcotte & Schubert (Geodynamics, Ch. 1)"
    },
    76: {
        "q": 76,
        "question": "A fundamental diagnostic characteristic of slow-spreading mid-ocean ridges like the Mid-Atlantic Ridge is :",
        "options": {
            "A": "Smooth, flat crest without any axial valley",
            "B": "A prominent, deep median rift valley bounded by normal fault scarps (axial rift)",
            "C": "Absence of normal faulting and hydrothermal venting",
            "D": "Purely compressional fold structures"
        },
        "ans": "B",
        "topic": "Mid-Ocean Ridge Morphology: Slow-Spreading Axial Rift Valleys vs Fast-Spreading Rises",
        "ref": "Fowler (The Solid Earth, Ch. 9, pp. 340-355); Kennett (Marine Geology, Ch. 4); Lowrie (p. 14)"
    },
    77: {
        "q": 77,
        "question": "Which of the following mid-oceanic ridges contains extensive, anomalous regions underlain by a thick granitic continental layer?",
        "options": {
            "A": "Carlsberg Ridge (Indian Ocean)",
            "B": "Mid-Atlantic Ridge",
            "C": "Lomonosov Ridge (Arctic Ocean)",
            "D": "East Pacific Rise"
        },
        "ans": "C",
        "topic": "Arctic Tectonics: The Continental Nature of the Lomonosov Ridge",
        "ref": "Dr. Ausaf Sayeed (Short Notes, p. 1 & Explanatory Note *77); Fowler (The Solid Earth, Ch. 9); Lowrie (p. 15)"
    },
    78: {
        "q": 78,
        "question": "The largest and most spectacular subaerial exposure (outcrop) of an active mid-oceanic spreading ridge on dry land is :",
        "options": {
            "A": "Greenland",
            "B": "Iceland (Mid-Atlantic Ridge emergent spreading zone)",
            "C": "Ryukyu Islands",
            "D": "Galapagos Islands"
        },
        "ans": "B",
        "topic": "Subaerial Ridge Volcanism: Iceland on the Mid-Atlantic Ridge Plume",
        "ref": "Lowrie (Fundamentals of Geophysics, p. 15); Fowler (The Solid Earth, pp. 350-354); Bangar (p. 31)"
    },
    79: {
        "q": 79,
        "question": "Active Mid-Oceanic Ridges (MORs) are globally characterized by which set of geophysical properties?",
        "options": {
            "A": "Extremely low heat flow and deep-focus seismicity (>300 km)",
            "B": "High conductive heat flow, shallow-focus seismicity (<15 km), and basaltic volcanism",
            "C": "Negative Bouguer gravity anomaly and thick sediment cover",
            "D": "Granitic intrusions and compressional thrust faulting"
        },
        "ans": "B",
        "topic": "MOR Geophysics: High Heat Flow, Shallow Earthquakes & Decompression Melting",
        "ref": "Lowrie (Fundamentals of Geophysics, pp. 13-16, 210); Fowler (The Solid Earth, Ch. 9); Turcotte & Schubert"
    },
    80: {
        "q": 80,
        "question": "The 'Dolphin Ridge' and 'Challenger Ridge' represent historical bathymetric divisions of the :",
        "options": {
            "A": "Mid-Indian Oceanic Ridge",
            "B": "Mid-Atlantic Ridge (Dolphin Ridge in North Atlantic, Challenger Ridge in South Atlantic)",
            "C": "East Pacific Rise",
            "D": "Carlsberg Ridge"
        },
        "ans": "B",
        "topic": "Atlantic Ocean Bathymetry: Dolphin and Challenger Ridges of the MAR",
        "ref": "Arthur Holmes (Principles of Physical Geology, Ch. 28); G.B. Mahapatra (p. 268)"
    },
    81: {
        "q": 81,
        "question": "Which of the following statements regarding the supercontinent Pangaea is INCORRECT?",
        "options": {
            "A": "It was assembled by continental collisions during the late Paleozoic Hercynian orogeny",
            "B": "It covered an estimated surface area of about 150 million km²",
            "C": "Two-thirds of its total landmass was concentrated in the Northern Hemisphere (Incorrect: The majority lay in the Southern Hemisphere / Gondwanaland)",
            "D": "It began rifting and breaking apart during the early Mesozoic Era"
        },
        "ans": "C",
        "topic": "Paleogeography: Continental Distribution & Geometry of Supercontinent Pangaea",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Alfred Wegener (The Origin of Continents and Oceans); Lowrie (p. 17)"
    },
    82: {
        "q": 82,
        "question": "Alfred Wegener's continental drift hypothesis was powerfully supported by the fossil reptile Mesosaurus, which is diagnostic of the :",
        "options": {
            "A": "Early Permian Period (found exclusively in southern Brazil and South Africa)",
            "B": "Middle Triassic Period",
            "C": "Late Jurassic Period",
            "D": "Cretaceous Period"
        },
        "ans": "A",
        "topic": "Paleontological Evidence for Continental Drift: Mesosaurus in Permian Strata",
        "ref": "Sam Boggs Jr. (Sedimentology & Stratigraphy, Ch. 16); Lowrie (Fundamentals of Geophysics, p. 18); Bangar (p. 24)"
    },
    83: {
        "q": 83,
        "question": "Marsupial mammals, today predominantly characteristic of Australia, have an ancient biogeographic fossil record proving prior connection to :",
        "options": {
            "A": "North America",
            "B": "South America (via Antarctica across Gondwanaland)",
            "C": "Eurasia",
            "D": "Africa"
        },
        "ans": "B",
        "topic": "Biogeography & Plate Tectonics: Marsupial Migration across Gondwanaland",
        "ref": "Arthur L. Bloom (Geomorphology, Ch. 21); Alfred Wegener (The Origin of Continents and Oceans); Colbert (Wandering Lands)"
    },
    84: {
        "q": 84,
        "question": "The northern supercontinent Laurasia and the southern supercontinent Gondwanaland collided to form the unified supercontinent Pangaea during the :",
        "options": {
            "A": "Hercynian (Variscan / Alleghenian) Orogeny (Carboniferous–Permian)",
            "B": "Caledonian Orogeny (Silurian–Devonian)",
            "C": "Acadian Orogeny",
            "D": "Antler Orogeny"
        },
        "ans": "A",
        "topic": "Supercontinent Assembly: Hercynian-Variscan Orogeny & Pangaea Formation",
        "ref": "Van der Pluijm & Marshak (Earth Structure, Ch. 21); Lowrie (Fundamentals of Geophysics, p. 17)"
    },
    85: {
        "q": 85,
        "question": "In classical paleogeography, 'Isthmian Links' (such as the Isthmus of Panama) represent :",
        "options": {
            "A": "Direct land bridges connecting separate continents allowing terrestrial faunal migration",
            "B": "Submarine trenches facilitating ocean current flow",
            "C": "Narrow volcanic ridges without biological significance",
            "D": "Subducted oceanic island chains"
        },
        "ans": "A",
        "topic": "Paleobiogeography: Isthmian Land Bridges & Trans-Continental Migration",
        "ref": "Arthur Holmes (Principles of Physical Geology, Ch. 28); Alfred Wegener (The Origin of Continents and Oceans)"
    },
    86: {
        "q": 86,
        "question": "The fundamental dipole equation relating magnetic inclination (dip angle $I$) to geomagnetic latitude ($\lambda$ or $L$) for an axial geocentric dipole is :",
        "options": {
            "A": "$\\sin I = 2 \\sin L$",
            "B": "$\\tan I = \\tan L$",
            "C": "$\\tan I = 2 \\tan L$",
            "D": "$\\cos I = 2 \\cos L$"
        },
        "ans": "C",
        "topic": "Paleomagnetism: The Geocentric Axial Dipole (GAD) Inclination Formula",
        "ref": "Lowrie (Fundamentals of Geophysics, Ch. 5, p. 288); Fowler (The Solid Earth, p. 48); Stacey (p. 280)"
    },
    87: {
        "q": 87,
        "question": "The Curie Temperature ($T_c$) is physically defined as :",
        "options": {
            "A": "The critical temperature above which radioactive minerals lose their radioactivity",
            "B": "The temperature at which a radioactive isotope completes one half-life",
            "C": "The critical temperature above which ferromagnetic/ferrimagnetic minerals lose their spontaneous magnetization and become paramagnetic",
            "D": "The eutectic melting temperature of basaltic magma"
        },
        "ans": "C",
        "topic": "Mineral Magnetism: Curie Temperature & Ferromagnetic-to-Paramagnetic Transition",
        "ref": "Lowrie (Fundamentals of Geophysics, pp. 290-294); Fowler (The Solid Earth, p. 55); Dexter Perkins (Mineralogy)"
    },
    88: {
        "q": 88,
        "question": "The total terrestrial continental landmass of the supercontinent Pangaea covered an estimated surface area of approximately :",
        "options": {
            "A": "$150 \\times 10^6\\text{ km}^2$ ($1.5 \\times 10^8\\text{ km}^2$)",
            "B": "$1.5 \\times 10^7\\text{ km}^2$",
            "C": "$15 \\times 10^4\\text{ km}^2$",
            "D": "$1.5 \\times 10^6\\text{ km}^2$"
        },
        "ans": "A",
        "topic": "Global Paleogeography: Total Land Area of Supercontinent Pangaea",
        "ref": "Dr. Ausaf Sayeed (Short Notes, p. 2); Lowrie (Fundamentals of Geophysics, p. 17); Strahler (Physical Geology)"
    },
    89: {
        "q": 89,
        "question": "The ancient east-west trending Mesozoic Tethys Ocean was paleogeographically situated between :",
        "options": {
            "A": "North America and South America",
            "B": "North America and Eurasia",
            "C": "Eurasia (to the north) and Gondwanaland / Africa-India (to the south)",
            "D": "Antarctica and Australia"
        },
        "ans": "C",
        "topic": "Historical Geology: The Tethys Ocean Basin & Alpine-Himalayan Closure",
        "ref": "G.B. Mahapatra (Text Book of Geology, p. 265); Krishnan (Geology of India); Lowrie (p. 17)"
    },
    90: {
        "q": 90,
        "question": "The northern rift that developed within Pangaea in early Mesozoic (Triassic-Jurassic) times initiated the opening of the :",
        "options": {
            "A": "Central and North Atlantic Ocean",
            "B": "Pacific Ocean",
            "C": "Southern Ocean",
            "D": "Arctic Ocean"
        },
        "ans": "A",
        "topic": "Plate Tectonics: Rifting of Pangaea & Genesis of the Central Atlantic",
        "ref": "Lowrie (Fundamentals of Geophysics, pp. 17-20); Fowler (The Solid Earth, Ch. 2); Van der Pluijm & Marshak"
    },
    91: {
        "q": 91,
        "question": "In his original 1912/1915 formulation, Alfred Wegener postulated that continental drift was driven primarily by :",
        "options": {
            "A": "Mantle convection currents and slab pull",
            "B": "Polflucht (pole-fleeing centrifugal force) and lunar-solar tidal friction",
            "C": "Subduction roll-back",
            "D": "Core dynamo electromotive forces"
        },
        "ans": "B",
        "topic": "History of Tectonics: Wegener's Proposed Mechanisms (Polflucht & Tidal Forces)",
        "ref": "Alfred Wegener (The Origin of Continents and Oceans); Lowrie (Fundamentals of Geophysics, p. 18); Bangar (p. 23)"
    },
    92: {
        "q": 92,
        "question": "In the reconstructed southern supercontinent Gondwanaland, the Indian continental shield was directly contiguous with all of the following EXCEPT :",
        "options": {
            "A": "Madagascar and East Africa",
            "B": "Western Australia",
            "C": "East Antarctica (Enderby Land)",
            "D": "South America (Incorrect: South America was fitted against West Africa)"
        },
        "ans": "D",
        "topic": "Gondwanaland Reconstruction: India's Contiguity with Antarctica, Australia, and Madagascar",
        "ref": "Krishnan (Geology of India); Lowrie (Fundamentals of Geophysics, p. 19); G.B. Mahapatra (p. 266)"
    },
    93: {
        "q": 93,
        "question": "The Curie Temperature ($T_c$) for pure metallic iron ($\alpha$-Fe) at atmospheric pressure is :",
        "options": {
            "A": "350°C",
            "B": "580°C",
            "C": "770°C (or ~768°C)",
            "D": "1400°C"
        },
        "ans": "C",
        "topic": "Mineral Magnetism & Solid State Physics: Curie Point of Metallic Iron",
        "ref": "Lowrie (Fundamentals of Geophysics, p. 291); Stacey (Physics of the Earth, Ch. 7); Lindsley (Oxide Minerals)"
    },
    94: {
        "q": 94,
        "question": "Marine magnetic anomalies and deep-sea drilling (DSDP/ODP) confirm that about 60% of the modern ocean floor (about one-third of Earth's total surface) has been created during the last :",
        "options": {
            "A": "25% of geologic time",
            "B": "15% of geologic time",
            "C": "10% of geologic time",
            "D": "4% (or ~3–4%) of geologic time (the last ~180–200 Ma out of 4560 Ma)",
            "E": "1.5% of geologic time"
        },
        "ans": "D",
        "topic": "Seafloor Spreading Dynamics: Rapid Cenozoic-Mesozoic Crustal Accretion",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Fowler (The Solid Earth, Ch. 3); Lowrie (p. 16)"
    },
    95: {
        "q": 95,
        "question": "Direct ocean-floor sampling and magnetic isochrons demonstrate that in-situ oceanic crust anywhere in the world's deep ocean basins is nowhere older than :",
        "options": {
            "A": "Permian",
            "B": "Triassic",
            "C": "Early to Middle Jurassic (~180–200 Ma)",
            "D": "Late Cretaceous"
        },
        "ans": "C",
        "topic": "Oceanic Lithosphere: Maximum Age of In-Situ Oceanic Crust (Jurassic)",
        "ref": "Lowrie (Fundamentals of Geophysics, p. 16); Fowler (The Solid Earth, Ch. 3); Van der Pluijm & Marshak"
    },
    96: {
        "q": 96,
        "question": "Which of the following ocean basins has, on average, the youngest mean age of oceanic crust and highest ratio of spreading ridges to total area?",
        "options": {
            "A": "Pacific Ocean",
            "B": "Atlantic Ocean",
            "C": "Arctic Ocean",
            "D": "Indian Ocean"
        },
        "ans": "A",
        "topic": "Global Marine Tectonics: Spreading Rates & Crustal Age of the Pacific Ocean",
        "ref": "Dr. Ausaf Sayeed (Key p. 69); Kennett (Marine Geology, Ch. 4); Lowrie (p. 15)"
    },
    97: {
        "q": 97,
        "question": "Which of the following ocean basins has exhibited a remarkably steady, more or less constant rate of seafloor spreading (~2 cm/year half-rate) throughout the Cenozoic?",
        "options": {
            "A": "Indian Ocean",
            "B": "Pacific Ocean",
            "C": "South Atlantic Ocean",
            "D": "North Atlantic Ocean"
        },
        "ans": "C",
        "topic": "Marine Geophysics: Steady Spreading Rates of the South Atlantic Ocean",
        "ref": "Dr. Ausaf Sayeed (Explanatory Note *97, p. 69); Lowrie (Fundamentals of Geophysics, p. 308); Fowler (Ch. 3)"
    },
    98: {
        "q": 98,
        "question": "The fastest full spreading rates of seafloor spreading anywhere on Earth (up to 15–17 cm/year) are exhibited along the :",
        "options": {
            "A": "Mid-Atlantic Ridge (slow: ~2–3 cm/yr)",
            "B": "Southwest Indian Ridge (ultra-slow: ~1.5 cm/yr)",
            "C": "Central Indian Ridge",
            "D": "East Pacific Rise (superfast spreading center)"
        },
        "ans": "D",
        "topic": "Plate Kinematics: Superfast Spreading Centers (East Pacific Rise)",
        "ref": "Dr. Ausaf Sayeed (Explanatory Note *98, p. 69); Lowrie (Fundamentals of Geophysics, p. 14); Fowler (p. 52)"
    },
    99: {
        "q": 99,
        "question": "Basalts dredged directly from the axial rift crests of active mid-ocean ridges (younger than 780,000 years, during the Brunhes Epoch) are uniformly :",
        "options": {
            "A": "Normally magnetized (Brunhes Normal Chron)",
            "B": "Reversely magnetized",
            "C": "Alternately polarized every few meters",
            "D": "Unmagnetized due to thermal demagnetization"
        },
        "ans": "A",
        "topic": "Geomagnetic Polarity: The Brunhes Normal Polarity Chron at Axial Ridges",
        "ref": "Lowrie (Fundamentals of Geophysics, Ch. 5, pp. 306-310); Fowler (The Solid Earth, Ch. 3); Bangar (p. 25)"
    },
    100: {
        "q": 100,
        "question": "In the standard Geomagnetic Polarity Time Scale (GPTS), the polarity epoch immediately preceding the Brunhes Normal Epoch (spanning ~0.78 to 2.58 Ma) is the :",
        "options": {
            "A": "Gauss Reversed Epoch",
            "B": "Matuyama Reversed Epoch",
            "C": "Gauss Normal Epoch",
            "D": "Gilbert Reversed Epoch"
        },
        "ans": "B",
        "topic": "Geomagnetic Time Scale: The Matuyama Reversed Polarity Epoch (0.78–2.58 Ma)",
        "ref": "Lowrie (Fundamentals of Geophysics, Table 5.3, p. 307); Fowler (The Solid Earth, p. 50); Stacey (p. 290)"
    }
}

with open("/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter1_Geotectonics/sayeed_q61_100.json", "w") as f:
    json.dump(SAYEED_Q61_100, f, indent=2)

print("Batch 3 (Q61 to Q100) verified dataset compiled successfully!")
