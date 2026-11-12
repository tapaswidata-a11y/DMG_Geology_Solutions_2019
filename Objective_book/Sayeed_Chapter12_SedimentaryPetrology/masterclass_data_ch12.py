#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Granulometric Formulations, and Syntheses for Chapter 12: Sedimentary Petrology
Dr. Ausaf Sayeed - Objective Geology (162 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Granulometry & Folk-Ward Statistical Parameters
    if any(k in t_low for k in ["folk and ward", "mean grain size", "mz =", "inclusive graphic", "standard deviation", "sorting", "skewness", "kurtosis"]):
        return (
            r"M_z = \frac{\phi_{16} + \phi_{50} + \phi_{84}}{3}, \quad \sigma_I = \frac{\phi_{84} - \phi_{16}}{4} + \frac{\phi_{95} - \phi_5}{6.6}, \quad Sk_I = \frac{\phi_{16} + \phi_{84} - 2\phi_{50}}{2(\phi_{84} - \phi_{16})} + \frac{\phi_5 + \phi_{95} - 2\phi_{50}}{2(\phi_{95} - \phi_5)}",
            "Folk and Ward's (1957) graphic statistical parameters represent the international standard for interpreting clastic granulometry. Using percentiles extracted from cumulative frequency curves on the phi scale (phi = -log2 d), Graphic Mean (Mz) measures average transport competence; Inclusive Graphic Standard Deviation (sigma_I) quantifies sorting efficiency (<0.35 phi = very well sorted; >2.0 phi = very poorly sorted); and Inclusive Graphic Skewness (SkI) tracks excess fine (+ve) or coarse (-ve) tails, diagnosing beach vs fluvial vs aeolian depositional dynamics.",
            "Folk, R.L. & Ward, W.C. (1957, Brazos River bar: A study in the significance of grain size parameters. J. Sediment. Petrol. 27: 3-26); Boggs, S. (2009, Petrology of Sedimentary Rocks)"
        )

    if any(k in t_low for k in ["phi-scale", "krumbein", "wentworth", "grade scale"]):
        return (
            r"\phi = -\log_2 (d_{\text{mm}}) = -\frac{\ln (d_{\text{mm}})}{\ln 2}, \quad d_{\text{mm}} = 2^{-\phi}",
            "W.C. Krumbein's (1938) logarithmic transformation converts C.K. Wentworth's (1922) geometric grade scale into an equidistant arithmetic scale. Because hydraulic transport fractionates sediment by geometric ratios of two (e.g., 2, 4, 8, 16 mm), the negative base-2 logarithm yields integer values for class boundaries (-2 phi for 4 mm pebbles, 1 phi for 0.5 mm medium sand, 4 phi for 0.0625 mm silt boundary), enabling rigorous Gaussian normal statistical modeling.",
            "Krumbein, W.C. (1938, Size frequency distributions of sediments and their normal statistical significance. J. Sediment. Petrol. 8: 84-90); Wentworth, C.K. (1922, A scale of grade and class terms for clastic sediments)"
        )

    # 2. Hydrodynamics, Bedforms & Flow Regimes
    if any(k in t_low for k in ["ripple index", "ripples", "flow regime", "parting lineation", "flaser", "herringbone"]):
        return (
            r"Fr = \frac{U}{\sqrt{g D}}, \quad \text{RI} = \frac{\lambda}{H} \quad \begin{cases} \text{Aqueous Ripples: } 5 \le \text{RI} \le 15, & Fr < 1 \text{ (Lower Flow Regime)} \\ \text{Aeolian Ripples: } 15 < \text{RI} \le 50+, & \text{Impact saltation} \\ \text{Parting Lineation: } \text{Plane bed, } & Fr \approx 1 \text{ (Upper Flow Regime)} \end{cases}",
            "Bedform morphology directly reflects the hydrodynamic flow regime governed by the dimensionless Froude number (Fr = U / sqrt(gD)). Under lower flow regime (Fr < 1), subaqueous current ripples and dunes form with low Ripple Index (wavelength / height = 5 to 15). Under aeolian conditions, grain impact saltation produces widespread ripples with RI > 15 to 30+. In the upper flow regime (Fr approaching or exceeding 1), planar beds develop with characteristic primary current lineation (parting lineation) oriented parallel to flow.",
            "Simons, D.B. & Richardson, E.V. (1966, Forms of bed roughness in alluvial channels. USGS Prof. Pap. 422-J); Allen, J.R.L. (1982, Sedimentary Structures: Their Character and Physical Basis)"
        )

    # 3. Turbidites & The Bouma Sequence
    if any(k in t_low for k in ["bouma", "turbidite", "flysch", "graded bedding", "flute mark"]):
        return (
            r"\text{Bouma Sequence: } T_a \text{ (Graded sand)} \to T_b \text{ (Lower plane bed)} \to T_c \text{ (Rippled/convolute)} \to T_d \text{ (Upper plane silt)} \to T_e \text{ (Pelagic mud)}",
            "Arnold Bouma (1962) established the idealized five-division vertical sequence produced by a single decelerating turbidity current event. As the suspension cloud expands and wanes down-slope, it records a continuous drop in flow regime and shear stress: from high-density rapid fallout producing massive to graded bedding (Ta), through upper-flow-regime flat bed traction (Tb), lower-flow-regime climbing and current ripples (Tc), upper flat-laminated silts (Td), terminating in slow hemipelagic mud settling (Te).",
            "Bouma, A.H. (1962, Sedimentology of Some Flysch Deposits. Elsevier); Walker, R.G. (1992, Turbidites and submarine fans. In: Facies Models)"
        )

    # 4. Siliciclastic Sandstone Classification & Provenance
    if any(k in t_low for k in ["arkose", "graywacke", "orthoquartzite", "sandstone", "provenance", "pettijohn", "matrix"]):
        return (
            r"\text{QFL System: } \begin{cases} \text{Quartz Arenite: } Q > 95\%, \quad \text{Supermature cratonic platform} \\ \text{Arkose: } Q < 75\%, \ F/L > 3:1, \quad \text{Granitic basement / Rift block} \\ \text{Litharenite: } Q < 75\%, \ L/F > 3:1, \quad \text{Orogenic recycled orogen} \\ \text{Wacke (Graywacke): } \text{Detrital matrix } > 15\%, \quad \text{Turbidite trench / Forearc} \end{cases}",
            "Pettijohn, Potter, and Siever (1987) organize sandstones based on a two-tier framework: matrix proportion (arenites <15% vs wackes 15-75%) followed by framework QFL grain composition (Quartz, Feldspar, Lithic fragments). Quartz arenites reflect prolonged weathering and multicyclic recycling on stable cratonic shelves. Arkoses require high-relief mechanical erosion of granitic/gneissic basement in active fault rifts. Graywackes contain abundant clay/chlorite matrix resulting from deep-water turbidity current deposition.",
            "Pettijohn, F.J., Potter, P.E., Siever, R. (1987, Sand and Sandstone. Springer); Dickinson, W.R. & Suczek, C.A. (1979, Plate tectonics and sandstone compositions. AAPG Bull. 63: 2164-2182)"
        )

    # 5. Carbonate Petrology (Folk & Dunham Classifications)
    if any(k in t_low for k in ["limestone", "folk", "dunham", "micrite", "sparite", "allochem", "coquina", "oolite", "biosparite"]):
        return (
            r"\text{Folk: } \text{Allochems (Intraclasts, Oolites, Pellets, Fossils)} + \text{Orthochems (Micrite } < 4\,\mu\text{m}, \text{ Sparite } > 10\,\mu\text{m}) \implies \begin{cases} \text{Biosparite} \\ \text{Biomicrite} \\ \text{Oosparite} \end{cases}",
            "R.L. Folk (1959) and R.J. Dunham (1962) established the foundational nomenclature for carbonate rocks. Folk's system couples the dominant allochem type (bio-, oo-, pel-, intra-) with the binding matrix or cement (-micrite for lime mud; -sparite for clear crystalline cement). Dunham's system evaluates depositional texture and fabric: mudstone (<10% grains), wackestone (>10% grains, mud-supported), packstone (grain-supported with mud), grainstone (grain-supported, mud-free), and boundstone (biogenically bound in life).",
            "Folk, R.L. (1959, Practical petrographic classification of limestones. AAPG Bull. 43: 1-38); Dunham, R.J. (1962, Classification of carbonate rocks according to depositional texture)"
        )

    # 6. Evaporites & Marine Salt Crystallization Sequence
    if any(k in t_low for k in ["evaporite", "bar theory", "ochsenius", "usiglio", "gypsum", "halite", "potash", "sabkha"]):
        return (
            r"\text{Seawater Evaporation Cycle: } V_0 \xrightarrow{50\%} \text{CaCO}_3 \xrightarrow{19\%} \text{Gypsum } (\text{CaSO}_4\cdot 2\text{H}_2\text{O}) \xrightarrow{9.5\%} \text{Halite } (\text{NaCl}) \xrightarrow{<4\%} \text{Potash salts (Sylvite, Carnallite)}",
            "J. Usiglio (1849) experimentally established the invariant precipitation sequence during solar evaporation of marine brine. Calcium carbonate begins precipitating when seawater volume is reduced by half; gypsum precipitates at 19% volume; halite begins at 9.5% volume; and highly soluble potash/magnesium bitterns (sylvite KCl, carnallite KMgCl3·6H2O) crystallize only when <4% of original brine remains. Ochsenius' (1877) Bar Theory explains thick evaporite deposits via continuous marine replenishment across a shallow sill.",
            "Usiglio, J. (1849, Ann. Chim. Phys. 27: 92-107); Ochsenius, C. (1877, Die Bildung der Steinsalzlager. Halle); Sonnenfeld, P. (1984, Brines and Evaporites. Academic Press)"
        )

    # 7. Diagenesis & Weathering Geochemistry
    if any(k in t_low for k in ["goldich", "stability", "diagenesis", "catagenesis", "syneresis", "weathering", "intrastratal"]):
        return (
            r"\text{Goldich Stability Series: } \text{Olivine} < \text{Augite} < \text{Hornblende} < \text{Biotite} < \text{K-feldspar} < \text{Muscovite} < \text{Quartz (Most Stable)}",
            "S.S. Goldich's (1938) Mineral Stability Series demonstrates that the relative susceptibility of silicate minerals to chemical weathering is inversely proportional to their stability at Earth-surface conditions, precisely mirroring Bowen's reaction series in reverse. High-temperature, anhydrous minerals with isolated silicate tetrahedra (olivine) possess the highest lattice strain and decompose most rapidly, whereas highly polymerized framework silicates (quartz) and aluminous phyllosilicates persist indefinitely.",
            "Goldich, S.S. (1938, A study in rock-weathering. J. Geol. 46: 17-58); Pettijohn, F.J. (1941, Persistence of heavy minerals and geologic age. J. Geol. 49: 610-625)"
        )

    # 8. Fluvial & Deltaic Environments
    if any(k in t_low for k in ["fluvial", "meandering", "point bar", "crevasse", "levee", "delta", "bird's foot"]):
        return (
            r"\text{Fining-Upwards Cycle: } \text{Basal Lag (Gravel)} \to \text{Trough Cross-Bed Sand} \to \text{Planar Laminated Sand} \to \text{Climbing Ripple Silt} \to \text{Overbank Mud}",
            "Meandering fluvial channels construct characteristically fining-upward point-bar successions through continuous lateral accretion and channel migration. Scouring at the outer cut bank deposits a coarse basal gravel lag, which is succeeded upward by lower point-bar dune cross-strata, middle point-bar planar and ripple-laminated fine sands, and upper floodplain overbank silts, muds, and crevasse splays.",
            "Allen, J.R.L. (1970, Studies in fluviatile sedimentation. J. Sediment. Petrol. 40: 298-323); Miall, A.D. (1996, The Geology of Fluvial Deposits. Springer)"
        )

    # Default Sedimentary Petrology Principles
    return (
        r"\text{Sedimentary Cycle: } \text{Weathering} \to \text{Erosion} \to \text{Hydraulic Transport} \to \text{Depositional Basin} \to \text{Diagenetic Lithification}",
        "Sedimentary petrology investigates the physical, chemical, and biological processes governing the genesis, transport, deposition, and lithification of sedimentary rocks. Integrating grain-size distribution, primary structures, detrital mineralogy, and diagenetic cements allows geologists to reconstruct paleoenvironments, paleocurrents, and tectonic provenance across Earth history.",
        "Boggs, S. (2009, Petrology of Sedimentary Rocks. Cambridge Univ. Press); Folk, R.L. (1980, Petrology of Sedimentary Rocks. Hemphill Publishing); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["folk and ward", "sorting", "skewness", "kurtosis", "phi"]):
        return {
            "title": "Folk & Ward (1957) Graphic Granulometric Indices & Environmental Significance",
            "headers": ["Statistical Parameter", "Mathematical Formula", "Numerical Range & Classification", "Diagnostic Depositional Environment"],
            "rows": [
                ["Graphic Mean (Mz)", r"\frac{\phi_{16} + \phi_{50} + \phi_{84}}{3}", "Reflects overall average kinetic energy of transporting medium", "Fluvial gravels (<0 phi) to shelf muds (>8 phi)"],
                ["Inclusive Graphic Sorting (sigma_I)", r"\frac{\phi_{84} - \phi_{16}}{4} + \frac{\phi_{95} - \phi_5}{6.6}", "<0.35 phi: Very well sorted; 0.5-1.0 phi: Moderately sorted; >2.0 phi: Very poorly sorted", "Beach sands (<0.35 phi); Glacial till (>3.0 phi)"],
                ["Inclusive Graphic Skewness (SkI)", r"\frac{\phi_{16} + \phi_{84} - 2\phi_{50}}{2(\phi_{84} - \phi_{16})} + \frac{\phi_5 + \phi_{95} - 2\phi_{50}}{2(\phi_{95} - \phi_5)}", "+0.3 to -0.3: Strongly fine-skewed to strongly coarse-skewed", "Beach sands: Negatively skewed; Rivers: Positively skewed"],
                ["Graphic Kurtosis (KG)", r"\frac{\phi_{95} - \phi_5}{2.44(\phi_{75} - \phi_{25})}", "<0.67: Platykurtic; 0.90-1.11: Mesokurtic; >1.50: Very leptokurtic", "Monosource well-sorted sands: Leptokurtic"]
            ]
        }

    if any(k in t_low for k in ["sandstone", "arkose", "graywacke", "orthoquartzite"]):
        return {
            "title": "Pettijohn & Folk Siliciclastic Sandstone Classification Framework",
            "headers": ["Sandstone Class", "Framework Composition", "Matrix Content", "Tectonic Setting & Provenance"],
            "rows": [
                ["Quartz Arenite (Orthoquartzite)", "Quartz > 95%, ultra-stable heavy minerals (ZTR)", "< 15% (commonly < 1%)", "Stable cratonic platforms, passive margins; multicyclic recycling"],
                ["Arkose / Subarkose", "Feldspar > 25% (K-feldspar > plagioclase)", "< 15% matrix; chemical cement present", "Tectonic rifts, block-faulted granitic basement, arid climate"],
                ["Lithic Arenite", "Rock fragments (lithics) > 25% > feldspar", "< 15% matrix", "Orogenic collision belts, foreland basins, volcanic arcs"],
                ["Wacke (Graywacke)", "Quartz, lithics, feldspars in chloritic clay matrix", "> 15% detrital matrix; chemical cement absent", "Deep-sea submarine fans, trench turbidites, active margins"]
            ]
        }

    if any(k in t_low for k in ["limestone", "folk", "dunham", "allochem", "micrite"]):
        return {
            "title": "Comparative Carbonate Classification: Folk (1959) vs Dunham (1962)",
            "headers": ["Carbonate Type", "Folk Allochem / Matrix Term", "Dunham Texture Term", "Depositional Energy & Environment"],
            "rows": [
                ["Lime Mudstone", "Micrite (pure microcrystalline calcite)", "Mudstone (<10% grains, mud-supported)", "Quiet low-energy protected lagoons, deep shelf"],
                ["Fossiliferous Lime Wackestone", "Biomicrite (fossil clasts in lime mud)", "Wackestone (>10% grains, mud-supported)", "Subtidal open marine shelf below wave base"],
                ["Fossiliferous Packstone", "Biomicrite / Biosparite transition", "Packstone (grain-supported with mud matrix)", "Moderate-energy shallow marine shelf/ramp"],
                ["Oolitic Grainstone", "Oosparite (ooids cemented by sparry calcite)", "Grainstone (grain-supported, mud-free)", "High-energy agitated shoals, tidal bars, barrier beaches"],
                ["Reef Framework", "Biolithite (skeletal in-situ framework)", "Boundstone (biogenically bound in life)", "High-energy wave-resistant organic reef front"]
            ]
        }

    if any(k in t_low for k in ["evaporite", "bar theory", "sabkha", "gypsum", "halite"]):
        return {
            "title": "Marine Evaporite Precipitation Sequence (Usiglio, 1849; Sonnenfeld, 1984)",
            "headers": ["Evaporite Stage", "Brine Concentration", "Precipitating Mineral Suite", "Diagnostic Sedimentological Feature"],
            "rows": [
                ["Carbonate Stage", "Volume reduced to 50%", "Calcite, Aragonite, Dolomite", "Fine micritic laminae, peloids, stromatolites"],
                ["Sulfate Stage", "Volume reduced to 19%", "Gypsum (CaSO4·2H2O), Anhydrite", "Enterolithic folds, nodular chicken-wire fabric"],
                ["Halite Stage", "Volume reduced to 9.5%", "Halite (NaCl)", "Hopper crystals, chevron bands, salt pseudomorphs"],
                ["Bittern / Potash Stage", "Volume reduced to < 4%", "Sylvite (KCl), Carnallite, Polyhalite", "Highly deliquescent, terminal restricted basin floor"]
            ]
        }

    # Default Sedimentary Petrology Synthesis Table
    return {
        "title": "Comprehensive Environmental Facies Spectrum of Sedimentary Environments",
        "headers": ["Depositional Realm", "Dominant Hydrodynamic Process", "Diagnostic Sedimentary Structures", "Characteristic Lithofacies Suite"],
        "rows": [
            ["Fluvial (Meandering)", "Unidirectional channel flow & overbank suspension", "Point bar fining-upward, trough cross-bedding, mudcracks", "Conglomeratic lag, lithic/arkosic sandstones, siltstones, coal"],
            ["Eolian (Dune)", "Wind traction, saltation, grainfall/grainflow", "Large-scale planar/wedge cross-bedding, high RI ripples", "Supermature quartz arenite, frosted grains, red beds"],
            ["Tidal Flat", "Bidirectional reversing flood/ebb & slack water", "Herringbone cross-bedding, flaser/lenticular bedding, stromatolites", "Interbedded sand-mud, mud drapes, flasers, tidal channels"],
            ["Deep Marine (Turbidite)", "Episodic density-driven turbidity current suspensions", "Bouma sequence (Ta-Te), flute marks, groove casts, load casts", "Rhythmic flysch graywackes and pelagic shales"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["folk and ward", "sorting", "skewness", "kurtosis", "phi"]):
        return [
            {
                "question": "A sediment sample cumulative curve yields phi16 = 1.0, phi50 = 2.0, and phi84 = 3.0. According to Folk and Ward (1957), what is its Graphic Mean (Mz)?",
                "options": {
                    "a": "1.50 phi",
                    "b": "2.00 phi",
                    "c": "2.50 phi",
                    "d": "3.00 phi"
                },
                "answer": "b",
                "explanation": "Mz = (phi16 + phi50 + phi84) / 3 = (1.0 + 2.0 + 3.0) / 3 = 6.0 / 3 = 2.00 phi (medium sand grade)."
            },
            {
                "question": "Persistent backwash wave action on a marine beach winnows away fine silt and clay particles, leaving an excess of coarse grains. This process characteristically imparts to the beach sand:",
                "options": {
                    "a": "Strongly positive skewness",
                    "b": "Negative skewness",
                    "c": "Platykurtic sorting",
                    "d": "Extremely poor sorting"
                },
                "answer": "b",
                "explanation": "On the phi scale, coarse particles have lower/negative values. Depletion of fines creates an asymmetric tail toward coarse phi values, producing diagnostic negative skewness."
            }
        ]

    if any(k in t_low for k in ["sandstone", "arkose", "graywacke", "orthoquartzite"]):
        return [
            {
                "question": "A sandstone contains 60% quartz, 30% potassium feldspar, 5% rock fragments, and 5% detrital clay matrix, bonded by calcite cement. In the Pettijohn classification, this rock is a/an:",
                "options": {
                    "a": "Lithic arenite",
                    "b": "Arkose",
                    "c": "Graywacke",
                    "d": "Quartz arenite"
                },
                "answer": "b",
                "explanation": "With <15% matrix, it is an arenite; with feldspar > 25% and F/L ratio of 30:5 (6:1 > 3:1), it is classified precisely as an arkose."
            },
            {
                "question": "Which of the following suites of heavy minerals defines Hubert's (1962) ZTR index of mineralogical maturity?",
                "options": {
                    "a": "Zircon, Titanite, Rutile",
                    "b": "Zircon, Tourmaline, Rutile",
                    "c": "Zoisite, Tremolite, Riebeckite",
                    "d": "Zeolite, Topaz, Rhodonite"
                },
                "answer": "b",
                "explanation": "The ZTR index measures the combined percentage of the three most chemically and mechanically ultra-stable non-opaque minerals: Zircon, Tourmaline, and Rutile."
            }
        ]

    # Default Sedimentary Petrology Practice Problems
    return [
        {
            "question": "In an ideal Bouma turbidite sequence, which division is characterized by current-ripple and convolute lamination representing lower flow regime conditions?",
            "options": {
                "a": "Division Ta",
                "b": "Division Tb",
                "c": "Division Tc",
                "d": "Division Td"
            },
            "answer": "c",
            "explanation": "Division Tc of the Bouma sequence represents lower flow regime bedform migration, characterized by small-scale climbing ripple, wavy, and convolute lamination."
        },
        {
            "question": "According to Carl Ochsenius' Bar Theory, thick accumulations of marine evaporites develop when:",
            "options": {
                "a": "An inland lake completely dries up without any external water influx",
                "b": "A shallow submarine bar restricts circulation, allowing continuous influx of seawater into an intensely evaporating lagoon",
                "c": "Deep abyssal ocean currents freeze under polar ice caps",
                "d": "Volcanic hydrothermal fluids boil along mid-ocean ridges"
            },
            "answer": "b",
            "explanation": "The Bar Theory explains thick evaporites via a shallow sill (bar) that permits continuous influx of fresh seawater to balance intense evaporation in a restricted lagoon."
        }
    ]
