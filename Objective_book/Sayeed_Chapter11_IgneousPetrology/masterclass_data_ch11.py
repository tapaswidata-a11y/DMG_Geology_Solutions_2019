#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Petrological Formulations, and Syntheses for Chapter 11: Igneous Petrology
Dr. Ausaf Sayeed - Objective Geology (175 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Geochemical Indices & CIPW Norm Differentiation
    if any(k in t_low for k in ["differentiation index", "thornton", "tuttle", "di ="]):
        return (
            r"\text{DI} = \sum (\text{Normative } \text{Qz} + \text{Or} + \text{Ab} + \text{Ne} + \text{Ks} + \text{Lc}) \quad [0 \le \text{DI} \le 100]",
            "Thornton and Tuttle's (1960) Differentiation Index (DI) quantifies the degree of magmatic evolution toward Petrogeny's Residua System. In basaltic and intermediate magmas undergoing fractional crystallization, early-crystallizing mafic silicates deplete Mg, Fe, and Ca, causing the residual liquid to become progressively enriched in petrogeny's salic normative constituents. Values near 20-30 represent primitive basaltic melts, whereas values approaching 95-100 characterize highly evolved rhyolites and phonolites.",
            "Thornton, C.P. & Tuttle, O.F. (1960, Chemistry of the igneous rocks: I. Differentiation index. Am. J. Sci. 258: 664-684); Best, M.G. (2003, Igneous and Metamorphic Petrology)"
        )

    if any(k in t_low for k in ["solidification index", "kuno", "si ="]):
        return (
            r"\text{SI} = \frac{100 \times \text{MgO}}{\text{MgO} + \text{FeO} + \text{Fe}_2\text{O}_3 + \text{Na}_2\text{O} + \text{K}_2\text{O}} \quad (\text{wt.}\%)",
            "Kuno's (1959) Solidification Index (SI) tracks the consumption of magnesium during fractional crystallization of basaltic magmas. Because olivine and magnesian pyroxenes are the highest-temperature phases to crystallize, primitive mantle-derived magmas have SI values between 40 and 45. As crystallization advances, SI monotonically decreases down to <10 in felsic differentiates (dacites and rhyolites).",
            "Kuno, H. (1959, Origin of Cenozoic petrographic provinces of Japan and surrounding areas. Bull. Volcanol. 20: 37-76); Rollinson, H.R. (1993, Using Geochemical Data)"
        )

    if any(k in t_low for k in ["shand", "peraluminous", "metaluminous", "peralkaline", "a/cnk", "a/nk"]):
        return (
            r"\text{Peraluminous: } \frac{\text{Al}_2\text{O}_3}{\text{CaO} + \text{Na}_2\text{O} + \text{K}_2\text{O}} > 1.0; \quad \text{Metaluminous: } \frac{\text{Al}_2\text{O}_3}{\text{CaO} + \text{Na}_2\text{O} + \text{K}_2\text{O}} < 1.0 < \frac{\text{Al}_2\text{O}_3}{\text{Na}_2\text{O} + \text{K}_2\text{O}}",
            "S.J. Shand's (1927) alumina saturation classification organizes igneous rocks according to molecular proportions of Al2O3 relative to alkali and alkaline-earth oxides. Peraluminous rocks (A/CNK > 1.0) contain excess alumina accommodated in diagnostic minerals such as muscovite, biotite, garnet (almandine), cordierite, and andalusite/sillimanite. Peralkaline rocks (A/NK < 1.0) possess molar alkalis in excess of alumina, crystallizing sodic pyroxenes (aegirine) and sodic amphiboles (riebeckite, arfvedsonite).",
            "Shand, S.J. (1927, The Eruptive Rocks. D. Van Nostrand Co.); Frost, B.R. et al. (2001, A Geochemical Classification for Granitic Rocks. J. Petrol. 42: 2033-2048)"
        )

    if any(k in t_low for k in ["cipw", "norm", "normative", "cross, iddings", "hypersthene", "quartz norm"]):
        return (
            r"\text{Normative Balance: } \text{Ne} + \text{Qz} = \emptyset, \quad \text{Fo} + \text{Qz} \to 2\text{En}, \quad \text{Di} = \text{Wo} + \text{En/Fs}",
            "The CIPW normative calculation (Cross, Iddings, Pirsson, Washington, 1902) converts whole-rock chemical analyses into an idealized anhydrous mineral assemblage based on rigorous stoichiometric rules and affinities. Elements are allocated sequentially: P to apatite, S to pyrite, Ti to ilmenite/sphene, then alkalis and alumina to feldspars and feldspathoids. A key thermodynamic boundary is the critical plane of silica saturation: quartz and nepheline are mutually exclusive normative phases.",
            "Cross, W., Iddings, J.P., Pirsson, L.V., Washington, H.S. (1902, J. Geol. 10: 555-690); Cox, K.G., Bell, J.D., Pankhurst, R.J. (1979, The Interpretation of Igneous Rocks)"
        )

    # 2. Phase Equilibria & Binary/Ternary Systems
    if any(k in t_low for k in ["bowen", "reaction series", "discontinuous", "continuous"]):
        return (
            r"\begin{aligned} \text{Discontinuous: } & \text{Olivine} \to \text{Opx} \to \text{Cpx} \to \text{Amphibole} \to \text{Biotite} \\ \text{Continuous: } & \text{Anorthite (Ca)} \to \text{Bytownite} \to \dots \to \text{Albite (Na)} \end{aligned}",
            "N.L. Bowen's (1928) Reaction Principle describes the sequential crystallization and reaction of minerals with cooling silicate melt. The discontinuous series involves structural reorganization of silicate polyhedra from isolated tetrahedra (nesosilicates) to single chains (inosilicates), double chains, and sheets (phyllosilicates). The continuous series represents progressive solid solution substitution of CaAl by NaSi in plagioclase without structural phase transitions.",
            "Bowen, N.L. (1928, The Evolution of the Igneous Rocks. Princeton Univ. Press); Philpotts, A. & Ague, J. (2009, Principles of Igneous and Metamorphic Petrology)"
        )

    if any(k in t_low for k in ["forsterite", "enstatite", "peritectic", "incongruent melting", "fo-sio2"]):
        return (
            r"\text{Incongruent Melting: } \text{Mg}_2\text{Si}_2\text{O}_6 \text{ (Enstatite)} \xrightarrow{1557^\circ\text{C}} \text{Mg}_2\text{SiO}_4 \text{ (Forsterite)} + \text{Liquid } (\approx 65\text{ wt}\% \text{ SiO}_2)",
            "In the Forsterite-Silica system at 1 atm, protoenstatite melts incongruently at 1557°C to produce solid forsterite plus a silica-rich liquid. Upon cooling an intermediate melt, forsterite crystallizes first; upon reaching the peritectic reaction point (1557°C), liquid reacts with early-formed forsterite to produce enstatite. If fractional crystallization removes forsterite before this reaction occurs, the residual liquid diverges toward silica oversaturation (eutectic crystallization with tridymite/cristobalite).",
            "Bowen, N.L. & Andersen, O. (1914, The binary system MgO-SiO2. Am. J. Sci. 37: 487-500); Ehlers, E.G. (1972, The Interpretation of Geological Phase Diagrams)"
        )

    if any(k in t_low for k in ["diopside-anorthite", "di-an", "binary eutectic", "eutectic"]):
        return (
            r"T_E = 1274^\circ\text{C}, \quad X_E = 58\text{ wt}\% \text{ Diopside} + 42\text{ wt}\% \text{ Anorthite}, \quad F = C - P + 1 = 0",
            "The Diopside-Anorthite system represents a fundamental binary eutectic without solid solution, serving as a simplified model for the crystallization of basaltic magmas (pyroxene + calcic plagioclase). At the invariant eutectic point (1274°C, 1 atm), three phases (Di + An + Liquid) coexist, and crystallization proceeds at constant temperature until the remaining melt is completely exhausted.",
            "Bowen, N.L. (1915, The crystallization of haplobasaltic, haplodioritic, and related magmas. Am. J. Sci. 40: 161-185); Winter, J.D. (2014, Principles of Igneous and Metamorphic Petrology)"
        )

    if any(k in t_low for k in ["haplogranite", "ab-or-qz", "petrogeny's residua", "minimum melt", "tuttle"]):
        return (
            r"\text{Petrogeny's Residua System: } \text{Ab} - \text{Or} - \text{Qz} - \text{H}_2\text{O}, \quad T_{\text{eutectic/minimum}} \approx 650^\circ\text{--}720^\circ\text{C at } 1\text{--}5\text{ kbar}",
            "Tuttle and Bowen's (1958) experimental study of the haplogranite system (Ab-Or-Qz-H2O) proved conclusively that granitic rocks originate via magmatic crystallization at thermal minima. With increasing water vapor pressure ($P_{\text{H}_2\text{O}}$), the quaternary eutectic temperature drops substantially, and the eutectic composition shifts toward the albite apex, expanding the primary field of quartz.",
            "Tuttle, O.F. & Bowen, N.L. (1958, Origin of Granite in the Light of Experimental Studies. GSA Memoir 74); Johannes, W. & Holtz, F. (1996, Petrogenesis and Experimental Petrology of Granitic Rocks)"
        )

    # 3. Granite Classification & Petrogenesis
    if any(k in t_low for k in ["i-type", "s-type", "m-type", "a-type", "chappell", "white"]):
        return (
            r"\text{Granite Typology: } \begin{cases} \text{I-type: } \text{Igneous protolith, } \text{A/CNK} < 1.1, \text{ hornblende, magnetite, } {}^{87}\text{Sr}/{}^{86}\text{Sr} < 0.706 \\ \text{S-type: } \text{Sedimentary protolith, } \text{A/CNK} > 1.1, \text{ cordierite/garnet, } {}^{87}\text{Sr}/{}^{86}\text{Sr} > 0.708 \\ \text{A-type: } \text{Anorogenic/Anhydrous, high Ga/Al, Fe-rich, Zr, Nb, REE-rich} \end{cases}",
            "Chappell and White (1974) introduced the genetic I- and S-type granite classification for the Lachlan Fold Belt of Australia. I-type granites derive from partial melting of mantle-derived igneous or meta-igneous underplates (metaluminous, hornblende/sphene-bearing). S-type granites originate by anatexis of supracrustal pelitic or psammitic sedimentary rocks (strongly peraluminous, muscovite/biotite/cordierite/almandine-bearing). Loiselle and Wones (1979) subsequently defined A-type granites as anorogenic, anhydrous, and alkaline.",
            "Chappell, B.W. & White, A.J.R. (1974, Two contrasting granite types. Pac. Geol. 8: 173-174); Loiselle, M.C. & Wones, D.R. (1979, Characteristics and origin of anorogenic granites. GSA Abstr. Prog. 11: 468)"
        )

    # 4. Layered Intrusions & Cumulate Rocks
    if any(k in t_low for k in ["skaergaard", "bushveld", "stillwater", "wager", "cryptic layering", "cumulate", "orthocumulate", "adcumulate"]):
        return (
            r"v = \frac{2 r^2 (\rho_s - \rho_m) g}{9 \eta}, \quad \text{Cumulate Texture: } \text{Cumulus crystals} + \text{Intercumulus melt} \to \begin{cases} \text{Orthocumulate} \\ \text{Adcumulate} \\ \text{Mesocumulate} \end{cases}",
            "Layered mafic-ultramafic intrusions (e.g., Skaergaard in East Greenland studied by Wager and Brown; Bushveld Complex in South Africa; Stillwater in Montana) demonstrate closed-system fractional crystallization and gravitational crystal settling governed by Stokes' law. Cryptic layering reflects continuous Fe-enrichment in olivine and pyroxenes alongside Na-enrichment in plagioclase as the magma chamber differentiates from base to roof.",
            "Wager, L.R. & Brown, G.M. (1967, Layered Igneous Rocks. W.H. Freeman & Co.); Irvine, T.N. (1982, Terminology for layered intrusions. J. Petrol. 23: 127-162)"
        )

    # 5. Lamprophyres, Alkaline Suites & Carbonatites
    if any(k in t_low for k in ["lamprophyre", "minette", "vogesite", "kersantite", "spessartite", "camptonite", "monchiquite"]):
        return (
            r"\text{Lamprophyre Classification: } \begin{cases} \text{Calc-Alkaline: } \text{Biotite/Phlogopite} + \text{K-spar (Minette) or Plagioclase (Kersantite)} \\ \text{Calc-Alkaline: } \text{Hornblende} + \text{K-spar (Vogesite) or Plagioclase (Spessartite)} \\ \text{Alkaline: } \text{Camptonite (Plag + Amph), Monchiquite (Foids/Glass)} \end{cases}",
            "Lamprophyres are melanocratic hypabyssal porphyritic rocks characterized by panidiomorphic (automorphic) textures containing phenocrysts exclusively of mafic minerals (biotite/phlogopite, amphibole, clinopyroxene) set in a fine-grained groundmass of feldspars and/or feldspathoids. Feldspars never form phenocrysts. They represent volatile-rich (H2O, CO2, F, Cl), high-Mg, high-LILE primitive melts derived from metasomatized subcontinental lithospheric mantle.",
            "Rock, N.M.S. (1991, Lamprophyres. Blackie & Son); Streckeisen, A. (1979, Classification and nomenclature of volcanic rocks, lamprophyres, carbonatites, and melilitic rocks. Geology 7: 331-335)"
        )

    if any(k in t_low for k in ["carbonatite", "sovite", "alvikite", "beforsite", "rauhaugite"]):
        return (
            r"\text{Carbonatite: } > 50\text{ vol}\% \text{ primary carbonate}, \quad \begin{cases} \text{Calcite-carbonatite: } \text{S\o vite (coarse plutonic), Alvikite (fine hypabyssal/volcanic)} \\ \text{Dolomite-carbonatite: } \text{Beforsite (medium-coarse), Rauhaugite (plutonic)} \\ \text{Ferrocarbonatite: } \text{Fe-rich carbonates (ankerite, siderite)} \end{cases}",
            "Carbonatites are rare mantle-derived igneous rocks containing >50% primary igneous carbonate minerals (calcite, dolomite, ankerite). They occur predominantly in continental intraplate rift zones (e.g., East African Rift, Oldoinyo Lengai natrocarbonatite volcano; Amba Dongar in Gujarat, India). Carbonatites represent extreme enrichments in incompatible elements, serving as the world's primary economic repositories of Rare Earth Elements (REE: Ce, La, Nd), niobium (pyrochlore), and phosphate (apatite).",
            "Bell, K. (1989, Carbonatites: Genesis and Evolution. Unwin Hyman); Le Maitre, R.W. (2002, Igneous Rocks: A Classification and Glossary of Terms. Cambridge Univ. Press)"
        )

    # 6. Komatiites & Archaean Magmatism
    if any(k in t_low for k in ["komatiite", "spinifex", "mgo", "viljoen"]):
        return (
            r"\text{Komatiite Definition: } \text{MgO} > 18\text{ wt}\%, \quad T_{\text{liquidus}} \ge 1600^\circ\text{C}, \quad \text{Spinifex Texture: Skeletal bladed olivine grew under extreme thermal quench}",
            "Komatiites are ultramafic volcanic rocks discovered by the Viljoen brothers (1969) in the Barberton Greenstone Belt of South Africa. They are characterized by exceptionally high MgO (>18-32 wt%), low TiO2, and diagnostic spinifex texture formed by rapid radiant heat loss from 1600°C liquidus ultramafic flows. Because modern mantle potential temperatures are ~200-300°C cooler, true high-Mg komatiites are virtually restricted to the Archean and Paleoproterozoic eons.",
            "Viljoen, M.J. & Viljoen, R.P. (1969, The geology and geochemistry of the lower ultramafic unit of the Onverwacht Group. GSA Spec. Publ. 2: 55-85); Arndt, N., Lesher, C.M., Barnes, S.J. (2008, Komatiite. Cambridge Univ. Press)"
        )

    # 7. Basalts, Ophiolites & Tectonic Environments
    if any(k in t_low for k in ["ophiolite", "sheeted dyke", "pillow basalt", "penrose", "serpentinite"]):
        return (
            r"\text{Penrose Ophiolite Architecture (Top to Base): } \text{Pelagic Sediments} \to \text{Pillow Basalt} \to \text{Sheeted Dyke Complex} \to \text{Layered Gabbros} \to \text{Moho} \to \text{Harzburgite/Lherzolite Mantle}",
            "The 1972 Penrose Conference defined the classic ophiolite pseudostratigraphy as an on-land fragment of oceanic lithosphere obducted onto continental margins during tectonic collisions. The presence of the sheeted dyke complex provides definitive proof of seafloor spreading, where successive 100% basaltic dyke intrusions accommodate continuous divergent plate separation at ocean ridges or back-arc basins.",
            "Penrose Conference Participants (1972, Ophiolites. Geotimes 17: 24-25); Dilek, Y. & Furnes, H. (2011, Ophiolite genesis and global tectonics. Elements 7: 369-374)"
        )

    if any(k in t_low for k in ["morb", "oib", "tholeiite", "alkali basalt", "chassigny", "normative quartz", "ne-normative"]):
        return (
            r"\text{Yoder \& Tilley Basalt Tetrahedron: } \begin{cases} \text{Tholeiitic Series: Hypersthene-normative (subalkaline, silica-saturated to oversaturated)} \\ \text{Alkaline Series: Nepheline-normative (silica-undersaturated)} \\ \text{Dividing Plane: Critical Plane of Silica Undersaturation (Di-Ab-Fo)} \end{cases}",
            "H.S. Yoder and C.E. Tilley (1962) established the basalt tetrahedron (Nepheline-Diopside-Forsterite-Quartz) as the foundational framework for basalt petrogenesis. Tholeiitic basalts plot on the silica-saturated to oversaturated side of the Di-Ab critical divide, crystallizing low-Ca pyroxene (orthopyroxene/pigeonite) and late interstitial quartz. Alkaline basalts plot on the silica-undersaturated side, crystallizing titanaugite, olivine, and late feldspathoids.",
            "Yoder, H.S. & Tilley, C.E. (1962, Origin of basalt magmas: An experimental study of natural and synthetic rock systems. J. Petrol. 3: 342-532); Wilson, M. (1989, Igneous Petrogenesis. Chapman & Hall)"
        )

    # 8. Igneous Textures & Microstructures
    if any(k in t_low for k in ["texture", "ophitic", "subophitic", "poikilitic", "myrmekite", "granophyre", "rapakivi", "perthite"]):
        return (
            r"\text{Crystallization Kinetics: } \Delta G_v = -\frac{L \Delta T}{T_m}, \quad \text{Texture reflects nucleation rate } (I) \text{ vs growth rate } (Y) \text{ as a function of undercooling } (\Delta T)",
            "Igneous textures preserve the kinetic thermal history of magma crystallization. Ophitic texture (calcic plagioclase laths completely enclosed poikilitically within titanaugite oikocrysts) diagnostic of diabases/dolerites develops when augite nucleation is inhibited relative to plagioclase, allowing pyroxene to grow around pre-existing plagioclase crystals. Granophyric and myrmekitic textures record eutectic intergrowth and metasomatic replacement, respectively.",
            "Harker, A. (1909, The Natural History of Igneous Rocks); Vernon, R.H. (2004, A Practical Guide to Rock Microstructure. Cambridge Univ. Press); Cox, Bell & Pankhurst (1979)"
        )

    # 9. Pyroclastic & Volcanological Mechanics
    if any(k in t_low for k in ["pyroclastic", "ignimbrite", "tuff", "fiamme", "ash", "lapilli", "volcanic bomb", "caldera"]):
        return (
            r"\text{Grain Size Classification (Fisher, 1961): } \text{Ash } (< 2\text{ mm}) \quad \text{Lapilli } (2\text{--}64\text{ mm}) \quad \text{Blocks/Bombs } (> 64\text{ mm})",
            "Pyroclastic deposits form through explosive volcanic fragmentation driven by rapid gas exsolution and decompression of volatile-charged silicic to intermediate melts. Welded ignimbrites (pyroclastic flow deposits) develop eutaxitic fabrics where hot, malleable pumice clasts undergo ductile compaction and collapse beneath overburden pressure into dark, glassy lens-shaped ribbons termed fiamme.",
            "Fisher, R.V. (1961, Proposed classification of volcaniclastic sediments and rocks. GSA Bull. 72: 1409-1414); Cas, R.A.F. & Wright, J.V. (1987, Volcanic Successions: Modern and Ancient. Allen & Unwin)"
        )

    # Default Igneous Petrology Mechanics
    return (
        r"\text{Magmatic Evolution: } \text{Basaltic Parent} \xrightarrow{\text{Fractional Crystallization}} \text{Andesite} \xrightarrow{-\text{Plag, Cpx, Mag}} \text{Dacite} \xrightarrow{-\text{Amp, Bt}} \text{Rhyolite (Residuum)}",
        "Igneous petrology deciphers the thermodynamic, chemical, and physical principles that control magma generation in Earth's mantle and crust, melt ascent through lithospheric pathways, and magma crystallization in plutonic, hypabyssal, and volcanic environments. Modern petrology couples multi-component phase equilibria with high-precision trace element and radiogenic isotope geochemistry to constrain lithospheric geodynamics.",
        "Winter, J.D. (2014, Principles of Igneous and Metamorphic Petrology. Pearson); Philpotts & Ague (2009); Best, M.G. (2003); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["differentiation", "index", "kuno", "thornton", "norm"]):
        return {
            "title": "Comprehensive Petrological & Geochemical Differentiation Indices",
            "headers": ["Index Name", "Mathematical Formulation", "Physical Significance", "Diagnostic Rock Range"],
            "rows": [
                ["Thornton-Tuttle DI", r"\text{Qz} + \text{Or} + \text{Ab} + \text{Ne} + \text{Ks} + \text{Lc}", "Measures progress toward Petrogeny's Residua System", "Primitive basalts: 15-25; Granites/Rhyolites: 85-98"],
                ["Kuno Solidification Index (SI)", r"\frac{100 \times \text{MgO}}{\text{MgO} + \text{FeO} + \text{Fe}_2\text{O}_3 + \text{Na}_2\text{O} + \text{K}_2\text{O}}", "Tracks depletion of high-T magnesian mafic phases", "Picrites/Tholeiites: 40-45; Rhyolites: < 5-10"],
                ["Poldervaart Crystallization Index (CI)", r"\text{An} + \text{Di}' + \text{Fo}' + \text{Sp}'", "Quantifies crystallization of basic/mafic phases", "Decreases monotonically as magmas evolve"],
                ["Agpaitic Index (Alkalinity)", r"\frac{\text{Na}_2\text{O} + \text{K}_2\text{O}}{\text{Al}_2\text{O}_3} \text{ (molar)}", "Discriminated peralkaline vs miaskitic alkaline rocks", "Peralkaline rocks: > 1.0 (aegirine, arfvedsonite)"],
                ["Shand's Alumina Index (A/CNK)", r"\frac{\text{Al}_2\text{O}_3}{\text{CaO} + \text{Na}_2\text{O} + \text{K}_2\text{O}} \text{ (molar)}", "Defines peraluminous, metaluminous, peralkaline", "Peraluminous (S-type): > 1.1; Metaluminous: < 1.0"]
            ]
        }

    if any(k in t_low for k in ["lamprophyre", "minette", "vogesite", "kersantite", "spessartite"]):
        return {
            "title": "IUGS Systematic Classification of Lamprophyres (Streckeisen, 1979)",
            "headers": ["Lamprophyre Class", "Dominant Mafic Phenocryst", "Dominant Groundmass Feldspar", "Associated Magmatic Clan"],
            "rows": [
                ["Minette", "Biotite / Phlogopite", "Potassium Feldspar (Orthoclase / Sanidine)", "Calc-Alkaline / Potassic Suite"],
                ["Vogesite", "Amphibole (Hornblende) / Cpx", "Potassium Feldspar", "Calc-Alkaline Suite"],
                ["Kersantite", "Biotite / Phlogopite", "Plagioclase (Oligoclase - Andesine)", "Calc-Alkaline Suite"],
                ["Spessartite", "Amphibole (Hornblende) / Cpx", "Plagioclase", "Calc-Alkaline Suite"],
                ["Camptonite", "Titanaugite + Kaersutite", "Plagioclase", "Alkaline Lamprophyre Suite"],
                ["Monchiquite", "Titanaugite + Kaersutite + Ol", "Feldspathoids / Analcime / Glass", "Alkaline Lamprophyre Suite"]
            ]
        }

    if any(k in t_low for k in ["granite", "i-type", "s-type", "a-type", "m-type"]):
        return {
            "title": "Diagnostic Genetic Typology of Granitic Rocks (Chappell & White, 1974; Loiselle & Wones, 1979)",
            "headers": ["Granite Type", "Protolith / Source", "Diagnostic Mineralogy", "Geochemical Signature"],
            "rows": [
                ["I-Type (Infracrustal)", "Meta-igneous or mantle underplate", "Hornblende, biotite, sphene, magnetite", r"\text{A/CNK} < 1.1, \text{ normative diopside}, {}^{87}\text{Sr}/{}^{86}\text{Sr} < 0.706"],
                ["S-Type (Supracrustal)", "Metasedimentary pelites/psammites", "Muscovite, cordierite, almandine, ilmenite", r"\text{A/CNK} > 1.1, \text{ normative corundum} > 1\%, {}^{87}\text{Sr}/{}^{86}\text{Sr} > 0.708"],
                ["M-Type (Mantle)", "Subducted oceanic slab / mantle wedge", "Pyroxenes, calcic amphibole, plagioclase", r"\text{Extremely low } {}^{87}\text{Sr}/{}^{86}\text{Sr} (0.703\text{--}0.704), \text{ oceanic arcs}"],
                ["A-Type (Anorogenic)", "Anhydrous granulitic crustal residue / rifting", "Annite, fluorite, riebeckite, aegirine", r"\text{High } \text{Ga/Al}, \text{ high } \text{FeO}^*/\text{MgO}, \text{ Zr, Nb, Y enriched}"]
            ]
        }

    if any(k in t_low for k in ["texture", "ophitic", "poikilitic", "rapakivi", "spinifex"]):
        return {
            "title": "Fundamental Diagnostic Igneous Textures and Cooling Kinetics",
            "headers": ["Texture Name", "Diagnostic Microstructural Geometry", "Kinetic / Thermodynamic Origin", "Classic Rock Example"],
            "rows": [
                ["Ophitic", "Plagioclase laths completely enclosed within pyroxene", "Pyroxene nucleation delayed relative to plagioclase", "Diabase / Dolerite sill"],
                ["Subophitic", "Plagioclase laths partially enclosed within pyroxene", "Intermediate undercooling and growth rates", "Basalt flows / Gabbro"],
                ["Poikilitic", "Small mineral inclusions enclosed in large oikocryst", "Early crystallizing phase engulfed by late host", "Peridotite, Harzburgite"],
                ["Spinifex", "Elongated, skeletal/sheaf-like olivine and pyroxene blades", "Extreme radiative thermal quench of high-Mg melt", "Komatiite flows"],
                ["Rapakivi", "Potassium feldspar ovoids mantled by sodic plagioclase", "Decompression or magma mixing shifting feldspar equilibria", "Wiborgite granite"],
                ["Granophyric", "Micrographic quartz-alkali feldspar cuneiform intergrowth", "Rapid simultaneous crystallization at thermal eutectic", "Granophyre, Microgranite"]
            ]
        }

    if any(k in t_low for k in ["ophiolite", "penrose", "dyke", "serpentine", "mantle"]):
        return {
            "title": "Penrose Classic Ophiolite Pseudostratigraphy and Oceanic Crust Architecture",
            "headers": ["Ophiolite Tier", "Dominant Rock Unit", "Geodynamic Formation Process", "Diagnostic Mineral Assemblage"],
            "rows": [
                ["Sedimentary Cover", "Pelagic cherts, micritic limestones", "Pelagic pelagic settling on active ocean floor", "Radiolaria, microfossils, clay"],
                ["Pillow Basalts", "Subaqueous pillow lavas, hyaloclastites", "Extrusive submarine volcanism at ridge axis", "Plagioclase, augite, glass, smectite"],
                ["Sheeted Dyke Complex", "100% basaltic/diabasic parallel dykes", "Continuous divergent seafloor spreading", "Plagioclase, clinopyroxene, chlorite"],
                ["High-Level Gabbro", "Isotropic and quartz-bearing gabbro/trondhjemite", "Roof crystallization of axial magma chamber", "Plagioclase, uralitic amphibole, quartz"],
                ["Layered Cumulates", "Layered olivine gabbro, troctolite, anorthosite", "Gravitational crystal settling in magma chamber", "Calcic plagioclase + olivine + clinopyroxene"],
                ["Tectonized Mantle", "Harzburgite, dunite, podiform chromite", "Residual mantle depleted by basalt extraction", "Forsteritic olivine + enstatite + chromite"]
            ]
        }

    # Default Igneous Petrology Synthesis Table
    return {
        "title": "Comparative Lithological Framework of Major Igneous Rock Clans",
        "headers": ["Igneous Clan", "Essential Mineralogy", "Silica Saturation", "Plutonic vs Volcanic Equivalent"],
        "rows": [
            ["Granite-Rhyolite Clan", "Quartz (20-60%), K-feldspar, plagioclase, biotite", "Oversaturated (Qz normative)", "Granite / Rhyolite"],
            ["Syenite-Trachyte Clan", "Alkali feldspar (>65% total feldspar), hornblende", "Saturated to undersaturated", "Syenite / Trachyte"],
            ["Diorite-Andesite Clan", "Andesine-oligoclase plagioclase, hornblende, pyroxene", "Saturated to slightly oversaturated", "Diorite / Andesite"],
            ["Gabbro-Basalt Clan", "Calcic plagioclase (labradorite-bytownite), augite", "Saturated (tholeiite) or undersaturated (alkali)", "Gabbro / Basalt"],
            ["Peridotite Clan", "Olivine (>40%), orthopyroxene, clinopyroxene", "Strongly undersaturated (ultramafic)", "Peridotite / Komatiite"],
            ["Carbonatite Clan", "Primary carbonate (>50% calcite, dolomite)", "Carbonate-dominant mantle melt", "S\u00f6vite / Alvikite"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["differentiation", "index", "kuno", "thornton", "norm"]):
        return [
            {
                "question": "A rhyolite chemical analysis yields normative quartz = 32%, orthoclase = 28%, albite = 26%, and nepheline = 0%. According to Thornton and Tuttle (1960), what is its Differentiation Index (DI)?",
                "options": {
                    "a": "60",
                    "b": "86",
                    "c": "54",
                    "d": "92"
                },
                "answer": "b",
                "explanation": "Thornton-Tuttle DI equals the arithmetic sum of the normative salic components: DI = Qz + Or + Ab + Ne + Ks + Lc = 32 + 28 + 26 + 0 = 86."
            },
            {
                "question": "According to Kuno's Solidification Index (SI), which of the following magmas would exhibit the highest SI value?",
                "options": {
                    "a": "Calc-alkaline dacite",
                    "b": "Tholeiitic andesite",
                    "c": "Picritic basalt",
                    "d": "Alkaline rhyolite"
                },
                "answer": "c",
                "explanation": "Kuno's SI = 100 * MgO / (MgO + FeO + Fe2O3 + Na2O + K2O). Primitive high-Mg melts such as picritic basalts contain abundant MgO (12-20 wt%), yielding the highest SI values (~40-48), whereas evolved silicic magmas have SI < 10."
            }
        ]

    if any(k in t_low for k in ["lamprophyre", "minette", "vogesite", "kersantite", "spessartite"]):
        return [
            {
                "question": "A porphyritic hypabyssal igneous rock displays prominent phenocrysts of phlogopite and diopside within a groundmass dominated by orthoclase, with zero feldspar phenocrysts. This rock is classified as a:",
                "options": {
                    "a": "Kersantite",
                    "b": "Vogesite",
                    "c": "Minette",
                    "d": "Spessartite"
                },
                "answer": "c",
                "explanation": "By definition in the IUGS classification, a calc-alkaline lamprophyre with biotite/phlogopite phenocrysts and an alkali feldspar (orthoclase) matrix is a minette."
            },
            {
                "question": "What is the defining textural hallmark of all true lamprophyres under thin-section microscopy?",
                "options": {
                    "a": "Glomeroporphyritic clusters of plagioclase",
                    "b": "Panidiomorphic texture with phenocrysts restricted to mafic minerals",
                    "c": "Eutaxitic banding of collapsed pumice fiamme",
                    "d": "Micrographic intergrowth of quartz and anorthite"
                },
                "answer": "b",
                "explanation": "Lamprophyres exhibit a diagnostic panidiomorphic texture wherein euhedral phenocrysts consist exclusively of dark ferromagnesian minerals (biotite, amphibole, pyroxene), while feldspars are strictly confined to the groundmass."
            }
        ]

    if any(k in t_low for k in ["granite", "i-type", "s-type", "a-type", "m-type"]):
        return [
            {
                "question": "A granite pluton contains primary muscovite, cordierite, and almandine garnet, and yields an A/CNK ratio of 1.25. What is its genetic classification?",
                "options": {
                    "a": "I-type granite",
                    "b": "S-type granite",
                    "c": "M-type granite",
                    "d": "A-type granite"
                },
                "answer": "b",
                "explanation": "An A/CNK ratio > 1.1 combined with diagnostic aluminous minerals (muscovite, cordierite, almandine) definitively identifies an S-type granite generated by anatexis of pelitic metasedimentary crust."
            },
            {
                "question": "Which suite of geochemical characteristics is uniquely diagnostic of anorogenic A-type granites?",
                "options": {
                    "a": "Extremely low Ga/Al and depletion in HFSE",
                    "b": "High Ga/Al ratio, high FeO*/MgO, and enrichment in Zr, Nb, and REE",
                    "c": "Initial 87Sr/86Sr ratios strictly below 0.703",
                    "d": "Ubiquitous primary normative corundum > 3%"
                },
                "answer": "b",
                "explanation": "A-type granites are characterized by high Ga/Al ratios, elevated FeO*/MgO, high halogen contents (F, Cl), and substantial enrichments in High Field Strength Elements (HFSE: Zr, Nb, Y, REE)."
            }
        ]

    # Default Igneous Petrology Practice Problems
    return [
        {
            "question": "In the Forsterite-Silica binary phase system at 1 atm, enstatite melts incongruently at 1557°C into:",
            "options": {
                "a": "Diopside + Quartz",
                "b": "Forsterite + Liquid",
                "c": "Periclase + Liquid",
                "d": "Tridymite + Cristobalite"
            },
            "answer": "b",
            "explanation": "Enstatite (Mg2Si2O6) breaks down peritectically at 1557°C to produce solid forsterite (Mg2SiO4) plus a silica-rich liquid containing ~65 wt% SiO2."
        },
        {
            "question": "Which of the following textures is specifically diagnostic of komatiitic ultramafic lava flows?",
            "options": {
                "a": "Ophitic texture",
                "b": "Spinifex texture",
                "c": "Rapakivi texture",
                "d": "Poikilitic texture"
            },
            "answer": "b",
            "explanation": "Spinifex texture—comprising long, intersecting skeletal blades of olivine and pyroxene—forms exclusively by rapid thermal quenching of exceptionally high-temperature (>1600°C) ultramafic komatiite flows."
        }
    ]
