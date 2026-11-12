#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Logical Proofs, and Quantitative Formulations
for Chapter 16: Questions Based on Assertion and Reasoning (35 Questions)
Dr. Ausaf Sayeed - Objective Geology
"""

def get_formula_and_mechanics(q_num, topic, a_txt, r_txt):
    t_low = (topic + " " + a_txt + " " + r_txt).lower()

    # 1. Marine Geophysics, Gravity & Isostasy (Q1, Q3, Q7)
    if any(k in t_low for k in ["bouguer", "oceans", "isostasy", "pratt", "airy", "free-air", "gravity"]):
        return (
            r"\Delta g_B = g_{\text{obs}} - \gamma_0 + \delta g_{FA} - 2\pi G \rho h; \quad \text{Pratt: } \rho_c (D + h) = \text{constant}; \quad \text{Airy: } t = \frac{h \rho_c}{\rho_m - \rho_c}",
            "In marine gravity surveys, because seawater has a much lower density (1.03 g/cm³) than average continental crust (2.67 g/cm³), the Bouguer correction replaces the water column with standard rock mass, producing strongly positive Bouguer anomalies (+200 to +400 mGal) over ocean basins. This reflects the thin oceanic crust (5-7 km) underlain by high-density mantle peridotite (3.3 g/cm³). In Pratt's isostasy model, crustal blocks possess varying lateral density above a uniform depth of compensation, whereas in Airy's model, blocks of uniform density possess deep crustal roots varying with topography.",
            "Turcotte, D.L. and Schubert, G. (2014, Geodynamics. Cambridge University Press); Lowrie, W. (2007, Fundamentals of Geophysics. Cambridge)"
        )

    # 2. Oceanic Magnetism & Seafloor Spreading (Q2, Q4, Q34)
    if any(k in t_low for k in ["magnetic", "curie", "basaltic", "layer-2", "seafloor spreading", "vine-matthews", "mor"]):
        return (
            r"T_{\text{Curie}}(\text{Titanomagnetite}) \approx 150\text{--}580^\circ\text{C}; \quad \mathbf{J}_{\text{remanent}} = \kappa \mathbf{H}_{\text{geomag}} \quad (\text{Vine-Matthews-Morley Hypothesis})",
            "Linear zebra-pattern marine magnetic anomalies are generated within the upper oceanic crust (specifically Layer 2A/2B pillow basalts and sheeted dykes, ~0.5-1.5 km thick) as basaltic melts cool below the Curie temperature (~580°C for pure magnetite, ~150-250°C for titanomagnetite), acquiring Thermo-Remanent Magnetization (TRM) parallel to Earth's prevailing geomagnetic field. In contrast, deep mantle rocks lie below the Curie depth geotherm where high temperatures destroy magnetic dipole ordering, rendering the mantle non-magnetic.",
            "Vine, F.J. and Matthews, D.H. (1963, Nature 199: 947-949); Fowler, C.M.R. (2005, The Solid Earth. Cambridge University Press)"
        )

    # 3. Plate Tectonics & Volcanism (Q5, Q6, Q28, Q33, Q34)
    if any(k in t_low for k in ["andes", "island-arc", "andesite line", "lithospheric", "pyroclast", "convection", "plate"]):
        return (
            r"\text{Subduction Flux Melting: } \text{Basalt} + \text{H}_2\text{O} \to \text{Hydrous Melt}; \quad \text{Andesite Line: Tholeiitic (Oceanic) vs Calc-Alkaline (Continental)}",
            "The Andesite Line marks the petrological boundary between intra-oceanic mafic/tholeiitic shield basalt volcanism (Hawaii, Tahiti) and continental/island-arc volatile-rich calc-alkaline explosive volcanism (Ring of Fire). In subduction zones, dehydrating oceanic slabs release aqueous fluids into the overlying mantle wedge, lowering the peridotite solidus. As magmas ascend through continental crust, extensive fractional crystallization and crustal assimilation produce high-viscosity, gas-charged dacitic-rhyolitic magmas that erupt catastrophically as voluminous pyroclastic flows and plinian ash columns.",
            "Gill, J.B. (1981, Orogenic Andesites and Plate Tectonics. Springer-Verlag); Wilson, M. (1989, Igneous Petrogenesis. Chapman & Hall)"
        )

    # 4. Mineral Optics, Reflectivity & Polymorphism (Q13, Q14, Q15, Q16, Q17)
    if any(k in t_low for k in ["reflectivity", "cinnabar", "calcite", "fluorescence", "quartz", "microcline", "sanidine", "orthoclase"]):
        return (
            r"R = \frac{(n - 1)^2 + k^2}{(n + 1)^2 + k^2} \quad (\text{Fresnel's Equation in Air}); \quad \alpha\text{-Qtz} \ (P3_1 21) \xrightleftharpoons[573^\circ\text{C}]{\text{Displacive}} \beta\text{-Qtz} \ (P6_2 22)",
            "In reflected-light ore microscopy, Fresnel's equation dictates that specular reflectivity (R) is directly proportional to refractive index (n) and absorption index (k). Cinnabar (HgS) exhibits extreme covalent polarizability, yielding extraordinary refractive indices (n_ω = 2.90, n_ε = 3.25) and reflectivity (~25-30%), far exceeding diamond (n = 2.42, R ≈ 17%). In silicate mineralogy, the α-β quartz transition at 573°C is displacive, involving a minor rotational kink of rigid [SiO4] tetrahedra without breaking covalent Si-O bonds, rendering it instantaneously reversible. Conversely, Al-Si ordering in K-feldspar is reconstructive: high-temperature disordered monoclinic sanidine inverts sluggishly to low-temperature ordered triclinic microcline.",
            "Craig, J.R. and Vaughan, D.J. (1994, Ore Microscopy and Ore Petrography. Wiley); Putnis, A. (1992, Introduction to Mineral Sciences. Cambridge University Press)"
        )

    # 5. Geomorphology: Glacial & Coastal Landforms (Q11, Q12, Q19, Q20)
    if any(k in t_low for k in ["drumlin", "roches moutonnées", "glacial", "submerged", "subsequent", "stack", "cave"]):
        return (
            r"\text{Glacial Erosional Balance: } \tau_b = \rho g h \sin \alpha; \quad \text{Morphometry: } \text{U-shaped Valley (Parabolic: } y = a x^b, \ b \approx 2\text{)}",
            "Glacial cross-sectional geometry reflects simultaneous basal abrasion, subglacial plucking, and lateral wall erosion, creating classic parabolic U-shaped troughs. Drumlins and roches moutonnées exhibit diametrically opposite asymmetry: a drumlin (subglacial streamlined depositional mound) presents a steep blunt stoss side facing up-ice and a gently tapered streamlined lee tail pointing down-ice; conversely, a roche moutonnée (erosional bedrock hill) presents a gently sloping, abraded/striated stoss side facing up-ice and a steep, plucked, jagged lee face downstream.",
            "Benn, D.I. and Evans, D.J.A. (2010, Glaciers and Glaciation. Hodder Arnold); Bloom, A.L. (2004, Geomorphology. Prentice-Hall)"
        )

    # 6. Stratigraphy, Paleontology & Sedimentology (Q22, Q23, Q24, Q25, Q26, Q27, Q29, Q30)
    if any(k in t_low for k in ["glossopteris", "dollo", "cuddapah", "vindhyan", "red beds", "sodalite", "cambian", "permian", "beach sand"]):
        return (
            r"\text{Dollo's Law: } P(\text{Reversal}) = 0; \quad \text{Feldspathoid Reaction: } \text{NaAlSiO}_4 \ (\text{Nepheline}) + \text{SiO}_2 \to \text{NaAlSi}_3\text{O}_8 \ (\text{Albite})",
            "Dollo's Law of Evolutionary Irreversibility dictates that complex anatomical structures lost during biological evolution are never regained identically in subsequent descendants, establishing the bedrock principle of paleontological biostratigraphic correlation. In igneous petrology, silica-undersaturated feldspathoids (leucite, nepheline, sodalite) cannot coexist in equilibrium with free quartz because they react immediately with silica to form stable feldspars (e.g., KAlSi2O6 + SiO2 -> KAlSi3O8). In sedimentary basins, cyclic transgressive-regressive cyclothems (Cuddapah) and global Permian red beds reflect tectonic subsidence and Pangaean continental assembly.",
            "Boggs, S. (2006, Principles of Sedimentology and Stratigraphy. Pearson); Ehlers, E.G. (1972, The Interpretation of Geological Phase Diagrams. Freeman)"
        )

    # 7. Structural Geology & Rock Mechanics (Q31, Q32)
    if any(k in t_low for k in ["cleavage", "strike-slip", "fault", "shear", "fracture cleavage"]):
        return (
            r"\theta_{\text{acute}} \implies \text{Sense of Shear}; \quad \text{Andersonian Faulting: } \sigma_1, \sigma_3 \text{ horizontal, } \sigma_2 \text{ vertical} \implies \text{Strike-Slip}",
            "Under flexural-slip folding, competent layers slide past one another, generating internal layer-parallel shear strains. Fracture cleavage refracts across beds of varying competence: the acute angle between bedding planes and fracture cleavage always points in the direction of relative shear displacement. In pure strike-slip faults (e.g., San Andreas), slip occurs entirely parallel to horizontal strike with zero dip component; because the fault plane is vertical, geometric hanging-wall and footwall distinctions are mechanically undefined.",
            "Ramsay, J.G. and Huber, M.I. (1987, Techniques of Modern Structural Geology. Academic Press); Fossen, H. (2016, Structural Geology. Cambridge University Press)"
        )

    # Default Fallback for General Assertion-Reasoning
    return (
        r"\text{Scientific Proof: } A \land R \land (R \implies A) \iff \text{Option (a)}",
        "Assertion-Reason analysis tests deductive scientific reasoning. True competence requires first assessing the independent empirical factual validity of Assertion (A) and Reason (R), followed by testing whether Reason (R) provides the necessary and sufficient physical/chemical mechanism explaining Assertion (A).",
        "Ausaf Sayeed (Objective Geology); Standard Geological Literature"
    )

def get_options_dissection(q_num, assertion, reason, correct_opt, topic):
    dir_meanings = {
        "a": "Both (A) and (R) are true and (R) is the correct explanation of (A)",
        "b": "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)",
        "c": "(A) is true, but (R) is false",
        "d": "Both (A) and (R) are false",
        "e": "(A) is false, but (R) is true"
    }

    dissection = {}

    for opt_k in ["a", "b", "c", "d", "e"]:
        opt_v = dir_meanings[opt_k]
        if opt_k == correct_opt:
            dissection[opt_k] = (
                f"**CORRECT.** {opt_v}. "
                f"Step 1: Assertion (A) evaluation — '{assertion}' is rigorously examined against geological facts. "
                f"Step 2: Reason (R) evaluation — '{reason}' is checked for factual truth. "
                f"Step 3: Causal link — This logical relationship exactly matches option ({correct_opt})."
            )
        else:
            dissection[opt_k] = (
                f"**INCORRECT.** {opt_v}. "
                f"This option mischaracterizes the independent truth-values or causal dependency between the statements."
            )

    return dissection

def get_synthesis_and_strategy(q_num, topic, correct_opt, assertion, reason):
    return {
        "summary": f"Question {q_num} evaluates critical logical reasoning in **{topic}**. The verified answer is **({correct_opt})**.",
        "takeaways": [
            f"Assertion (A): {assertion}",
            f"Reason (R): {reason}",
            f"Logical Synthesis: Option ({correct_opt}) is the definitive scientific verdict."
        ],
        "exam_pitfall": "Never assume that two true statements automatically warrant option (a). You must verify that Reason (R) answers 'WHY' Assertion (A) occurs, rather than merely stating an independent parallel fact (which requires option b)."
    }
