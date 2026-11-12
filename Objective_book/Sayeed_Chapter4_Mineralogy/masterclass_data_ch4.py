#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 4: Mineralogy
Dr. Ausaf Sayeed - Objective Geology (180 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Silicate Structures: Nesosilicates, Sorosilicates, Cyclosilicates, Inosilicates, Phyllosilicates, Tectosilicates
    if "silicate" in t_low or "nesosilicate" in t_low or "sorosilicate" in t_low or "cyclosilicate" in t_low or "inosilicate" in t_low or "phyllosilicate" in t_low or "tectosilicate" in t_low:
        if "ring" in t_low or "cyclosilicate" in t_low or "beryl" in t_low or "tourmaline" in t_low:
            return (
                r"\text{Cyclosilicates (Ring Silicates):} \quad [\text{Si}_n\text{O}_{3n}]^{2n-} \quad \text{Si}:\text{O} = 1:3 \quad (n=6: [\text{Si}_6\text{O}_{18}]^{12-})",
                "In cyclosilicates, silicon-oxygen tetrahedra are linked into closed rings by sharing two oxygen atoms per tetrahedron. Six-membered rings [Si6O18]12- form the fundamental structural backbone of Beryl (Be3Al2Si6O18) and Tourmaline, creating hexagonal open channels along the vertical c-axis.",
                "Klein & Dutrow (Manual of Mineral Science, 23rd Ed., pp. 445–450); Deer, Howie & Zussman"
            )
        elif "soro" in t_low or "epidote" in t_low or "pair" in t_low:
            return (
                r"\text{Sorosilicates (Disilicates):} \quad [\text{Si}_2\text{O}_7]^{6-} \quad \text{Si}:\text{O} = 2:7 \quad [\text{One Shared Apical Oxygen}]",
                "Sorosilicates are characterized by isolated tetrahedral doublets [Si2O7]6- formed by two SiO4 tetrahedra sharing a single apical bridging oxygen atom. In epidote Ca2(Al,Fe)3(SiO4)(Si2O7)O(OH), independent [SiO4] nesosilicate groups and linked [Si2O7] sorosilicate pairs coexist within the same crystalline lattice.",
                "Klein & Dutrow (Manual of Mineral Science, pp. 440–444, 453); Sam Boggs Jr."
            )
        elif "phylls" in t_low or "sheet" in t_low or "mica" in t_low or "clay" in t_low:
            return (
                r"\text{Phyllosilicates (Sheet Silicates):} \quad [\text{Si}_2\text{O}_5]^{2-} \quad \text{Si}:\text{O} = 2:5 \quad [\text{Three Shared Basal Oxygens}]",
                "Phyllosilicates consist of continuous infinite two-dimensional sheets of SiO4 tetrahedra in which each tetrahedron shares three basal oxygens with adjacent tetrahedra, forming a hexagonal pseudo-hexagonal mesh. Sheets are bonded to octahedral cation layers (t-o or t-o-t) producing perfect basal cleavage {001}.",
                "Klein & Dutrow (Manual of Mineral Science, pp. 488–495); Deer, Howie & Zussman"
            )
        elif "tecto" in t_low or "framework" in t_low or "network" in t_low or "quartz" in t_low or "feldspar" in t_low:
            return (
                r"\text{Tectosilicates (Framework Silicates):} \quad [\text{SiO}_2]^0 \quad \text{Si}:\text{O} = 1:2 \quad [\text{All Four Oxygens Shared}]",
                "In tectosilicates, every single oxygen atom of each SiO4 tetrahedron is shared with an adjacent tetrahedron, creating a rigid three-dimensional framework. Substitution of Al3+ for Si4+ (up to 50% in Anorthite) introduces negative framework charges that are balanced by interstitial large cations (K+, Na+, Ca2+, Ba2+).",
                "Klein & Dutrow (Manual of Mineral Science, pp. 526–535); Sam Boggs Jr."
            )
        elif "chain" in t_low or "pyroxene" in t_low or "amphibole" in t_low:
            return (
                r"\text{Single Chain (Pyroxenes): } [\text{Si}_2\text{O}_6]^{4-} \ (\text{Si}:\text{O} = 1:3), \quad \text{Double Chain (Amphiboles): } [\text{Si}_4\text{O}_{11}]^{6-} \ (\text{Si}:\text{O} = 4:11)",
                "Inosilicates comprise single or double chains of corner-sharing SiO4 tetrahedra extending parallel to the c-axis. Pyroxenes feature single chains yielding ~87°/93° prismatic cleavage, whereas amphiboles feature double chains yielding diagnostic ~56°/124° cleavage.",
                "Klein & Dutrow (Manual of Mineral Science, pp. 458–478); Deer, Howie & Zussman"
            )
        else:
            return (
                r"\text{Nesosilicates (Orthosilicates):} \quad [\text{SiO}_4]^{4-} \quad \text{Si}:\text{O} = 1:4 \quad [\text{Zero Shared Oxygens}]",
                "Nesosilicates consist of isolated, independent [SiO4]4- tetrahedra bonded to one another exclusively through intermediate interstitial cations in 6-fold or 8-fold coordination. This dense ionic packing imparts high refractive index, high specific gravity, and pronounced chemical durability.",
                "Klein & Dutrow (Manual of Mineral Science, pp. 434–438); Deer, Howie & Zussman"
            )

    # 2. Pauling's Rules & Crystal Chemistry
    if "pauling" in t_low or "radius ratio" in t_low or "coordination" in t_low or "electrostatic" in t_low or "bond" in t_low:
        return (
            r"\text{Pauling's First Rule: } \frac{R_c}{R_a} \in [0.225, 0.414] \implies \text{CN} = 4 \ (\text{Tetrahedral}), \quad s = \frac{z}{\text{CN}} = \frac{4}{4} = 1.00",
            "Linus Pauling (1929) formulated fundamental crystal chemical principles governing ionic polyhedra: a coordination polyhedron of anions forms around each cation, with the cation-anion distance determined by the radius sum and the coordination number determined by the radius ratio Rc/Ra. Electrostatic bond strength s = z/CN dictates lattice stability.",
            "Linus Pauling (1929, J. Am. Chem. Soc.); Klein & Dutrow (pp. 78–84)"
        )

    # 3. Solid Solution, Isomorphism & Exsolution
    if "solid solution" in t_low or "exsolution" in t_low or "perthite" in t_low or "diadochy" in t_low or "isomorphism" in t_low or "coupled" in t_low:
        return (
            r"\text{Coupled Plagioclase Substitution:} \quad \text{Ca}^{2+} + \text{Al}^{3+} \longleftrightarrow \text{Na}^{+} + \text{Si}^{4+} \quad [\text{Albite: } \text{NaAlSi}_3\text{O}_8 \longleftrightarrow \text{Anorthite: } \text{CaAl}_2\text{Si}_2\text{O}_8]",
            "Solid solution represents the mutual substitution of chemical elements within specific atomic lattice sites. When substituting ions possess different valencies (e.g. Ca2+ vs Na+), electrostatic neutrality requires simultaneous coupled substitution in adjacent tetrahedral sites (Al3+ for Si4+). At low temperatures, cooling across a solvus promotes exsolution.",
            "Klein & Dutrow (Manual of Mineral Science, pp. 106–112); Deer, Howie & Zussman"
        )

    # 4. Polymorphism & Phase Transformations
    if "polymorph" in t_low or "quartz" in t_low and "inversion" in t_low or "stishovite" in t_low or "coesite" in t_low or "diamond" in t_low:
        return (
            r"\text{Silica Polymorphism:} \quad \alpha\text{-Quartz} \xrightarrow{573^\circ\text{C}} \beta\text{-Quartz} \xrightarrow{870^\circ\text{C}} \text{Tridymite} \xrightarrow{1470^\circ\text{C}} \text{Cristobalite} \xrightarrow{\text{Shock / High } P} \text{Coesite} / \text{Stishovite}",
            "Polymorphism describes substances possessing identical chemical formulas that crystallize in distinctly different space groups and crystal structures. Displacive transformations (e.g. alpha- to beta-quartz) involve only minor bond bending, while reconstructive transformations (e.g. quartz to stishovite) require extensive bond rupture and reorganization.",
            "Klein & Dutrow (Manual of Mineral Science, pp. 102–106, 526–530); Putnis (Mineral Sciences)"
        )

    # 5. Physical Properties: Hardness, Cleavage, Density, Magnetism, Luminescence
    if "hardness" in t_low or "mohs" in t_low or "cleavage" in t_low or "specific gravity" in t_low or "pycnometer" in t_low or "magnet" in t_low:
        return (
            r"\text{Specific Gravity Formula:} \quad G = \frac{W_{\text{air}}}{W_{\text{air}} - W_{\text{water}}} = \frac{\rho_{\text{mineral}}}{\rho_{\text{water}}} \quad [\text{Mohs Ordinal Hardness: } 1 \text{ (Talc)} \rightarrow 10 \text{ (Diamond)}]",
            "Physical properties in minerals directly express internal crystal structure and chemical bonding anisotropy. Cleavage planes represent structural directions of weakest bonding density across lattice planes. Specific gravity measures atomic mass packing density, accurately quantified via pycnometric displacement or heavy-liquid Archimedean suspension.",
            "Klein & Dutrow (Manual of Mineral Science, Ch. 2, pp. 19–38); Friedrich Mohs (1812)"
        )

    # 6. Olivine & Garnet Mineral Groups
    if "olivine" in t_low or "garnet" in t_low or "forsterite" in t_low or "fayalite" in t_low or "pyralspite" in t_low or "ugrandite" in t_low:
        return (
            r"\text{Olivine Series: } (\text{Mg},\text{Fe})_2\text{SiO}_4 \ [\text{Fo}_{100} (T_m = 1890^\circ\text{C}) \longleftrightarrow \text{Fa}_{100} (T_m = 1205^\circ\text{C})], \quad \text{Garnet: } X_3 Y_2 (\text{SiO}_4)_3",
            "The olivine series forms a complete solid solution where Mg2+ (0.66 A) and Fe2+ (0.74 A) occupy octahedral M1 and M2 sites. In the garnet supergroup, divalent X-cations (Mg, Fe, Mn, Ca) occupy 8-fold dodecahedral sites and trivalent Y-cations (Al, Fe3+, Cr) occupy 6-fold octahedral sites.",
            "Deer, Howie & Zussman (Rock-Forming Minerals, pp. 3–35); Bowen & Schairer (1935)"
        )

    # 7. Feldspar Supergroup: Alkali Feldspars, Plagioclase, Ordering & Zoning
    if "feldspar" in t_low or "plagioclase" in t_low or "orthoclase" in t_low or "microcline" in t_low or "sanidine" in t_low or "albite" in t_low or "anorthite" in t_low or "zoning" in t_low:
        return (
            r"\text{Ternary Feldspar System: } \text{KAlSi}_3\text{O}_8\ (\text{Or}) - \text{NaAlSi}_3\text{O}_8\ (\text{Ab}) - \text{CaAl}_2\text{Si}_2\text{O}_8\ (\text{An}) \quad [\text{Al-Si Ordering: Monoclinic } \rightarrow \text{Triclinic}]",
            "Feldspars are the dominant mineral group of Earth's crust. Alkali feldspars display complex temperature-dependent Al/Si tetrahedral ordering, degrading high-temperature monoclinic Sanidine (disordered) to low-temperature triclinic Microcline (ordered). Plagioclase exhibits normal, reverse, and oscillatory zoning in magmatic phenocrysts.",
            "Deer, Howie & Zussman (Rock-Forming Minerals, pp. 380–415); Klein & Dutrow (pp. 530–540)"
        )

    # 8. Pyroxenes, Amphiboles & Pyroxenoids
    if "pyroxene" in t_low or "amphibole" in t_low or "augite" in t_low or "diopside" in t_low or "enstatite" in t_low or "rhodonite" in t_low or "wollastonite" in t_low:
        return (
            r"\text{Pyroxene: } X Y \text{Si}_2\text{O}_6 \ (\text{Repeat: } 2 \text{ Tetrahedra}), \quad \text{Pyroxenoid (Wollastonite): } \text{Ca}_3\text{Si}_3\text{O}_9 \ (\text{Repeat: } 3 \text{ Tetrahedra})",
            "Pyroxenes contain single silicate chains with a 2-tetrahedron repeat unit linked to octahedral M1 and M2 sites. When large Ca2+ cations dominate, structural strain twists the chain into pyroxenoid architectures with 3-tetrahedron repeats (Wollastonite) or 5-tetrahedron repeats (Rhodonite).",
            "Deer, Howie & Zussman (Rock-Forming Minerals, pp. 105–160); Klein & Dutrow (pp. 458–475)"
        )

    # 9. Carbonates, Sulfates, Oxides, Halides
    if "carbonate" in t_low or "calcite" in t_low or "aragonite" in t_low or "dolomite" in t_low or "gypsum" in t_low or "anhydrite" in t_low or "spinel" in t_low:
        return (
            r"\text{Carbonate Polymorphism: } \text{CaCO}_3 \ [\text{Calcite (Trigonal } R\bar{3}c) \longleftrightarrow \text{Aragonite (Orthorhombic } Pmcn)], \quad \text{Dolomite: } \text{CaMg}(\text{CO}_3)_2",
            "Carbonates contain planar trigonal [CO3]2- ionic groups. Cations with ionic radii < 1.0 A (Mg, Fe, Mn) crystallize in the calcite trigonal structure, whereas cations > 1.0 A (Sr, Ba, Pb) adopt the aragonite orthorhombic structure. Dolomite features ordered alternating Ca and Mg sheets along the c-axis.",
            "Deer, Howie & Zussman (Rock-Forming Minerals, pp. 305–328); Klein & Dutrow (pp. 410–416)"
        )

    # Default Fallback for General Mineralogy
    return (
        r"\text{Fundamental Stoichiometric Law of Mineral Chemistry:} \quad A_m B_n X_p \quad \Longleftrightarrow \quad \sum (z_c \cdot n_c) = \sum (z_a \cdot n_a)",
        "Every crystalline mineral species is defined by a specific chemical composition with fixed stoichiometric ratios or well-defined solid-solution substitution limits, governed strictly by electrostatic neutrality and spatial lattice geometry.",
        "Klein & Dutrow (Manual of Mineral Science, 23rd Ed., Ch. 1); Deer, Howie & Zussman"
    )

print("Specialized Chapter 4 Masterclass Data Module ready.")
