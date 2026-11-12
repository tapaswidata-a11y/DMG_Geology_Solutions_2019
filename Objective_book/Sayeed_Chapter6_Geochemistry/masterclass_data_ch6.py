#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 6: Geochemistry
Dr. Ausaf Sayeed - Objective Geology (45 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Nucleosynthesis, Oddo-Harkins & Cosmic Abundance
    if "nucleosynthesis" in t_low or "oddo" in t_low or "cosmic" in t_low or "abundance" in t_low and "universe" in t_low:
        return (
            r"\text{Oddo-Harkins Nuclear Pairing Law:} \quad \text{Even-}Z / \text{Even-}N \gg \text{Odd-}Z / \text{Odd-}N, \quad 3\,^4\text{He} \xrightarrow{\text{Triple-}\alpha} \,^{12}\text{C}",
            "Stellar nucleosynthesis synthesizes elements through proton-proton fusion and alpha-capture processes. Nuclei with even proton numbers (Z) and even neutron numbers (N) possess superior nuclear pairing energies, zero net nuclear spin, and maximal binding energy per nucleon, creating universal saw-tooth abundance peaks at even-Z elements (C, O, Ne, Mg, Si, Fe).",
            "Oddo (1914); Harkins (1917); Faure (Principles and Applications of Geochemistry, Ch. 1)"
        )

    # 2. Goldschmidt Geochemical Classification & Trace Element Rules
    if "goldschmidt" in t_low or "lithophile" in t_low or "siderophile" in t_low or "chalcophile" in t_low or "camouflage" in t_low or "capture" in t_low:
        return (
            r"\text{Goldschmidt's Rule of Substitution:} \quad \Delta R / R_{\text{host}} \le 15\% \implies \text{Extensive Solid Solution}, \quad \text{Camouflage: } z_1 = z_2, \ R_1 \approx R_2",
            "V.M. Goldschmidt classified the chemical elements according to their affinity for specific phases: Lithophiles concentrate in silicate shells (low electronegativity, forming ionic bonds with O2-), Siderophiles dissolve in metallic Fe-Ni core liquids, and Chalcophiles concentrate in sulfide melts. Trace substitutions are categorized as Camouflage (equal charge/radius), Capture (higher charge), or Admission (lower charge).",
            "V.M. Goldschmidt (1937, Geochemische Verteilungsgesetze der Elemente); Mason & Moore"
        )

    # 3. Crustal & Mantle Models: Pyrolite and Oxysphere
    if "pyrolite" in t_low or "oxysphere" in t_low or "crust" in t_low or "mantle" in t_low or "clarke" in t_low:
        return (
            r"\text{Pyrolite Mantle Formulation:} \quad 1\,\text{Part Tholeiitic Basalt} + 3\,\text{Parts Refractory Dunite} \longrightarrow \text{Pyrolite Upper Mantle}",
            "A.E. Ringwood formulated the pyrolite mantle model to satisfy seismic velocity constraints and account for primary basaltic magma generation upon partial melting. The lithosphere is chemically an 'Oxysphere' because bulky O2- anions (radius 1.40 A) pack 93.8% to 94% of total crustal volume, with cations occupying interstitial coordination polyhedra.",
            "A.E. Ringwood (1966, The Chemical Composition and Origin of the Earth); Brian Mason"
        )

    # 4. Radiometric Decay & Geochronology
    if "decay" in t_low or "potassium" in t_low or "uranium" in t_low or "tritium" in t_low or "isobar" in t_low or "isotone" in t_low or "radio" in t_low:
        return (
            r"^{40}\text{K} \xrightarrow[\lambda_{\beta^-} = 4.96 \times 10^{-10}\text{y}^{-1}]{89.5\%} \,^{40}\text{Ca} + \beta^-, \quad ^{40}\text{K} + e^- \xrightarrow[\lambda_{\text{EC}} = 0.58 \times 10^{-10}\text{y}^{-1}]{10.5\%} \,^{40}\text{Ar} + \gamma",
            "Radioactive decay proceeds at invariant statistical rates governed by quantum tunneling. The branched decay of 40K produces 40Ca via beta-minus emission (89.5%) and 40Ar via electron capture (10.5%). Tritium (3H, half-life 12.32 years) serves as an indispensable atmospheric tracer separating post-1953 modern recharge from ancient sub-fossil groundwater.",
            "Faure & Mensing (Isotopes: Principles and Applications, 3rd Ed.); Dickin (Radiogenic Isotope Geology)"
        )

    # 5. Chemical Bonding, Electronegativity & Stishovite
    if "bond" in t_low or "electronegativity" in t_low or "stishovite" in t_low or "lemberg" in t_low or "ionic" in t_low:
        return (
            r"\text{Pauling's Ionic Character:} \quad \% \text{Ionic} = 100 \times \left[1 - \exp\left(-\frac{(\chi_A - \chi_B)^2}{4}\right)\right] \approx 50\% \quad (\text{Si-O Bond})",
            "The Pauling electronegativity difference between Silicon (chi = 1.90) and Oxygen (chi = 3.44) is Delta_chi = 1.54, yielding an Si-O bond that is approximately 50% covalent and 50% ionic. Under extreme shock-metamorphic pressures (>10 GPa), silicon transitions from tetrahedral coordination (CN = 4) to dense octahedral coordination (CN = 6) in Stishovite.",
            "Linus Pauling (1960, The Nature of the Chemical Bond); Klein & Dutrow; Chao et al. (1962)"
        )

    # 6. Colloidal Geochemistry & Solutions
    if "colloid" in t_low or "sol" in t_low:
        return (
            r"\text{Colloidal Domain Size:} \quad 10^{-7}\text{ cm} \le d \le 10^{-5}\text{ cm} \quad (1\text{ nm} - 100\text{ nm}) \quad [\text{Sol: Solid Dispersed in Liquid}]",
            "Colloidal systems occupy the intermediate thermodynamic state between true molecular solutions and macroscopic suspensions. High specific surface area and net electrical surface charges (zeta potential) govern flocculation, ion adsorption, and transport of iron, aluminum, and clay mineral sols across river-estuary salinity gradients.",
            "Krauskopf & Bird (Introduction to Geochemistry, Ch. 6); Sam Boggs Jr."
        )

    # Default Fallback for General Geochemistry
    return (
        r"\text{Fundamental Geochemical Mass Balance:} \quad C_i^{\text{Bulk Earth}} = \sum x_j \cdot C_i^j \quad (\text{Core, Mantle, Crust})",
        "Geochemical differentiation of the planet into core, silicate mantle, oceanic crust, and continental crust is quantified via elemental partition coefficients and conservation of mass across global reservoirs.",
        "Mason & Moore (Principles of Geochemistry, 4th Ed.); Faure"
    )

print("Specialized Chapter 6 Masterclass Data Module ready.")
