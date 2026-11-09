import re
import parse_all_applied_2019 as p

EXPLICIT_OVERRIDE = {
    3: {
        "A": "Epsilon cross bedding",
        "B": "Herringbone cross bedding",
        "C": "Hummocky cross bedding",
        "D": "Trough cross bedding"
    },
    6: {
        "A": "-1",
        "B": "0",
        "C": "1",
        "D": "2"
    },
    15: {
        "A": "Recrystallization of minerals",
        "B": "Parallel arrangement of clay minerals",
        "C": "Shearing",
        "D": "Presence of mica plates"
    },
    17: {
        "A": "48% porosity",
        "B": "26% porosity",
        "C": "32% porosity",
        "D": "65% porosity"
    },
    18: {
        "A": "Polar regions",
        "B": "Tropical regions",
        "C": "Mid-latitude region",
        "D": "Subtropical region"
    },
    21: {
        "A": "Back-arc Basin",
        "B": "Fore-arc Basin",
        "C": "Foreland Basin",
        "D": "Intracratonic Basin"
    },
    28: {
        "A": "V",
        "B": "V^2",
        "C": "V^3",
        "D": "sqrt(V)"
    },
    29: {
        "A": "Resistivity",
        "B": "Sonic",
        "C": "Induction",
        "D": "Gamma ray"
    },
    30: {
        "A": "Uranium — Jaduguda",
        "B": "Lead — Khetri",
        "C": "Gold — Panna",
        "D": "Iron — Malanjkhand"
    },
    31: {
        "A": "Coquina",
        "B": "Encrinite",
        "C": "Spergenite",
        "D": "Oolite"
    },
    33: {
        "A": "Slickenside",
        "B": "Lamination",
        "C": "Ventifact",
        "D": "None of these"
    },
    34: {
        "A": "Vertical",
        "B": "Horizontal",
        "C": "Along the dip of fault",
        "D": "Along the dip of bed"
    },
    36: {
        "A": "Moon",
        "B": "Fe-Ni meteorites",
        "C": "Chondrites",
        "D": "Basaltic chondrites"
    },
    37: {
        "A": "Chemical analysis",
        "B": "Scanning Electron Microscopy",
        "C": "X-ray diffraction",
        "D": "ICP-MS"
    },
    39: {
        "A": "Lithophile only",
        "B": "Chalcophile only",
        "C": "Siderophile only",
        "D": "Both chalcophile and siderophile"
    },
    40: {
        "A": "1 mm to 1 m",
        "B": "1.3 to 3 um",
        "C": "3 to 14 um",
        "D": "0.4 to 0.7 um"
    },
    42: {
        "A": "Gabbro",
        "B": "Granite",
        "C": "Peridotite",
        "D": "Tonalite"
    },
    43: {
        "A": "Island Arc",
        "B": "Benioff Zone",
        "C": "Canyon",
        "D": "Trench"
    },
    45: {
        "A": "Palana",
        "B": "Neyveli",
        "C": "Jharia",
        "D": "Kutch"
    },
    50: {
        "A": "Gondwana",
        "B": "Cuddapah",
        "C": "Jurassic of Kutch",
        "D": "Siwalik"
    },
    54: {
        "A": "Topaz",
        "B": "Apatite",
        "C": "Fluorite",
        "D": "Corundum"
    },
    56: {
        "A": "Nesosilicate",
        "B": "Inosilicate",
        "C": "Tectosilicate",
        "D": "Sorosilicate"
    },
    58: {
        "A": "75 Ma",
        "B": "65 Ma",
        "C": "45 Ma",
        "D": "110 Ma"
    },
    61: {
        "A": "Lengthening of the strata",
        "B": "Shortening of the strata",
        "C": "Overturning of the strata",
        "D": "Thinning of the strata"
    },
    62: {
        "A": "High angle fault",
        "B": "Low angle fault",
        "C": "Horizontal fault",
        "D": "Vertical fault"
    },
    64: {
        "A": "Rohini",
        "B": "IRS-1A",
        "C": "Bhaskara-1",
        "D": "Cartosat"
    },
    65: {
        "A": "235U - 207Pb",
        "B": "14C",
        "C": "K - Ar",
        "D": "87Rb - 87Sr"
    },
    67: {
        "A": "Miocene age",
        "B": "Oligocene age",
        "C": "Eocene age",
        "D": "Jurassic age"
    },
    68: {
        "A": "TIN models",
        "B": "Raster data models",
        "C": "Vector data models",
        "D": "Georelational data models"
    },
    69: {
        "A": "Uranium deposits",
        "B": "Bauxite deposits",
        "C": "Iron ore deposits",
        "D": "Copper ore deposits"
    },
    71: {
        "A": "Propane",
        "B": "Butane",
        "C": "Methane",
        "D": "Ethane"
    },
    72: {
        "A": "Muscovite",
        "B": "Biotite",
        "C": "Calcite",
        "D": "Quartz"
    },
    73: {
        "A": "Carlsbad twinning",
        "B": "Polysynthetic twinning",
        "C": "Penetration twinning",
        "D": "Cross-hatch twinning"
    },
    75: {
        "A": "Density",
        "B": "Porosity",
        "C": "Durability",
        "D": "Permeability"
    },
    76: {
        "A": "Landsat",
        "B": "INSAT",
        "C": "SPOT",
        "D": "IRS"
    },
    77: {
        "A": "Granite",
        "B": "Basic granulite",
        "C": "Charnockite",
        "D": "Khondalite"
    },
    80: {
        "A": "Copper",
        "B": "Iron",
        "C": "Manganese",
        "D": "Graphite"
    },
    81: {
        "A": "2.65",
        "B": "2.87",
        "C": "3.00",
        "D": "3.87"
    },
    83: {
        "A": "Gulcheru",
        "B": "Vempalle",
        "C": "Cumbum",
        "D": "Bairenkonda"
    },
    84: {
        "A": "Green band",
        "B": "Red Band",
        "C": "Infrared band",
        "D": "Blue band"
    },
    88: {
        "A": "RADAR",
        "B": "LIDAR",
        "C": "Thermal Image",
        "D": "Microwave"
    },
    89: {
        "A": "Ruby",
        "B": "Diamond",
        "C": "Kyanite",
        "D": "Sapphire"
    },
    92: {
        "A": "Rajasthan",
        "B": "Bihar",
        "C": "Odisha",
        "D": "Jharkhand"
    },
    96: {
        "A": "Shells",
        "B": "Bones",
        "C": "Teeth",
        "D": "Burrows"
    },
    99: {
        "A": "Crust and Upper Mantle",
        "B": "Mantle and Outer core",
        "C": "Outer core and inner core",
        "D": "Upper mantle and lower mantle"
    },
    103: {
        "A": "Rohini",
        "B": "Bhaskara",
        "C": "INSAT",
        "D": "Aryabhata"
    },
    104: {
        "A": "Temporal variation",
        "B": "Spectral variation",
        "C": "Altitude variation",
        "D": "Spatial variation"
    },
    108: {
        "A": "Khondalite",
        "B": "Limestone",
        "C": "Sandstone",
        "D": "Unconsolidated sand"
    },
    110: {
        "A": "20-30%",
        "B": "60%",
        "C": "80%",
        "D": "90%"
    },
    111: {
        "A": "Ruby",
        "B": "Emerald",
        "C": "Peridot",
        "D": "Zircon"
    },
    113: {
        "A": "Perthite",
        "B": "Syenite",
        "C": "Graphic granite",
        "D": "Graphic rhyolite"
    },
    115: {
        "A": "Late Precambrian",
        "B": "Permo-Carboniferous",
        "C": "Mesozoic",
        "D": "Devonian"
    },
    117: {
        "A": "Angular relationship",
        "B": "Presence of conglomerate",
        "C": "Residual soil",
        "D": "All of these"
    },
    118: {
        "A": "40-100 km",
        "B": "100-300 km",
        "C": "200-40000 km",
        "D": "1000-2000 km"
    },
    120: {
        "A": "2007",
        "B": "2006",
        "C": "2012",
        "D": "2016"
    },
    122: {
        "A": "Venus",
        "B": "Pluto",
        "C": "Earth",
        "D": "Mars"
    },
    123: {
        "A": "250 m",
        "B": "100 m",
        "C": "350 m",
        "D": "500 m"
    },
    134: {
        "A": "Nickel and iron",
        "B": "Nickel and chromium",
        "C": "Iron and calcium",
        "D": "Silica and Iron"
    },
    135: {
        "A": "Kyanite",
        "B": "Actinolite",
        "C": "Mica",
        "D": "Uranium"
    },
    139: {
        "A": "F = C + 2 - P",
        "B": "F = C + P - 2",
        "C": "F = C + 2",
        "D": "F = C - P + 1"
    },
    141: {
        "A": "Pb204",
        "B": "Pb206",
        "C": "Pb207",
        "D": "Pb208"
    },
    142: {
        "A": "Cretaceous fossils",
        "B": "Cambrian fossils",
        "C": "Carboniferous fossils",
        "D": "Jurassic fossils"
    },
    146: {
        "A": "Mercury",
        "B": "Earth",
        "C": "Mars",
        "D": "Venus"
    },
    150: {
        "A": "II",
        "B": "III",
        "C": "IV",
        "D": "V"
    }
}

print('Explicit overrides defined:', len(EXPLICIT_OVERRIDE))
