#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 2
Dr. Ausaf Sayeed - Physical Geology and Geomorphology (145 Questions)
"""

# Specialized formula mapping based on topic keywords
def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()
    
    # 1. Weathering & Chemistry
    if "hydration" in t_low or "salt" in t_low or "volume" in t_low and "weather" in t_low:
        return (
            r"\text{CaSO}_4\ (\text{Anhydrite}) + 2\text{H}_2\text{O} \longrightarrow \text{CaSO}_4\cdot 2\text{H}_2\text{O}\ (\text{Gypsum}) \quad [\Delta V = +42.27\%,\ \rho: 2.61 \rightarrow 2.32\text{ g/cm}^3]",
            "Mineral hydration involves the stoichiometric incorporation of water molecules into the crystal lattice of anhydrous minerals, driving massive volumetric lattice expansion, increasing rock porosity, and precipitating micro-fracturing.",
            "Arthur Holmes (Principles of Physical Geology, p. 382); Winkler (Stone: Properties and Durability in Man's Environment)"
        )
    if "goldich" in t_low or "stability" in t_low and "mineral" in t_low or "anorthite" in t_low or "olivine" in t_low:
        return (
            r"\text{Olivine} < \text{Pyroxene} < \text{Amphibole} < \text{Biotite} < \text{K-Feldspar} < \text{Muscovite} < \text{Quartz}",
            "The Goldich Dissolution Series mirrors Bowen's Reaction Series in reverse: minerals formed at the highest magmatic temperatures and pressures (isolated silica tetrahedra, nesosilicates) possess the lowest thermodynamic stability at Earth's surface conditions.",
            "S.S. Goldich (1938, A Study in Rock-Weathering, J. Geol. 46); Sam Boggs Jr. (pp. 14–18)"
        )
    if "sodium" in t_low and "potassium" in t_low or "oceanic" in t_low and "enrich" in t_low:
        return (
            r"\text{Weathering Flux:} \quad 2\text{KAlSi}_3\text{O}_8 + 2\text{H}^+ + 9\text{H}_2\text{O} \longrightarrow \text{Al}_2\text{Si}_2\text{O}_5(\text{OH})_4\ (\text{Kaolinite}) + 2\text{K}^+ + 4\text{H}_4\text{SiO}_4",
            "While crustal rocks supply equal stoichiometric amounts of Na and K during silicate weathering, potassium ions (K+) have a lower hydrated ionic radius and high charge density, causing them to be preferentially adsorbed into the interlayer sites of illite and smectite clays, while sodium (Na+) remains conservatively dissolved in oceanic water.",
            "Krauskopf & Bird (Introduction to Geochemistry, Ch. 13); Faure (Principles of Geochemistry)"
        )
    if "aluminium" in t_low or "insolub" in t_low or "bauxite" in t_low:
        return (
            r"\text{Al}^{3+} + 3\text{H}_2\text{O} \rightleftharpoons \text{Al(OH)}_3\ (\text{Gibbsite}) + 3\text{H}^+ \quad [\text{pH } 4.5 - 9.0: \text{Solubility } < 10^{-8}\text{ mol/L}]",
            "Under standard terrestrial near-surface pH regimes (pH 5 to 8.5), aluminum behaves as an immobile chemical component, precipitating as insoluble hydroxides and phyllosilicates, residual enrichment of which drives the formation of laterites and bauxites.",
            "Mason & Moore (Principles of Geochemistry); Sam Boggs Jr. (Principles of Sedimentology and Stratigraphy)"
        )
    # 2. Fluvial & Stream Hydraulics
    if "velocity" in t_low and ("erosive" in t_low or "power" in t_low or "competence" in t_low):
        return (
            r"E_k = \frac{1}{2}m v^2 \propto v^2 \quad \text{and} \quad \text{Competence } (M_{\text{max}}) \propto v^6",
            r"A stream's kinetic energy and erosive capability scale quadratically ($E_k \propto v^2$) with mean flow velocity, while its hydraulic competence—the maximum mass of a transportable particle—scales to the sixth power of velocity ($v^6$) according to the Sixth Power Law of Stream Transport.",
            "Arthur Holmes (Principles of Physical Geology, p. 518); Leopold, Wolman & Miller (Fluvial Processes in Geomorphology)"
        )
    if "meander" in t_low or "cut-off" in t_low or "oxbow" in t_low or "sinuosity" in t_low:
        return (
            r"v_{\text{outer}} > v_{\text{inner}} \implies \tau_{\text{outer}} > \tau_c \ (\text{Cut Bank Erosion}), \quad \tau_{\text{inner}} < \tau_c \ (\text{Point Bar Deposition})",
            r"Centrifugal acceleration and helicoidal cross-channel secondary circulation deflect maximum shear stress ($\tau_{\text{outer}}$) against the outer concave cut bank, inducing continuous lateral migration and point-bar accretion until neck cut-off forms an isolated oxbow lake.",
            "Leopold, Wolman & Miller (1964); Sam Boggs Jr. (Principles of Sedimentology and Stratigraphy, pp. 242–248)"
        )
    if "cavitation" in t_low or "bubble" in t_low:
        return (
            r"P < P_{\text{vapor}} \implies \text{Bubble Formation}; \quad P > P_{\text{vapor}} \implies \text{Violent Implosion } [P_{\text{shock}} > 1000\text{ MPa}]",
            "Where turbulent stream velocities exceed ~10–12 m/s over irregular rock steps, localized pressure drops below the saturation vapor pressure of water, nucleating vapor cavities. Immediate advection into higher-pressure zones causes explosive bubble collapse, unleashing microscopic water hammer shockwaves that shatter crystalline bedrock.",
            "Barnes (1956, Cavitation in Stream Hydraulics); K.M. Bangar (Principles of Engineering Geology, p. 69)"
        )
    if "delta" in t_low or "topset" in t_low or "foreset" in t_low or "bird" in t_low:
        return (
            r"\text{Delta Architecture:} \quad \text{Topset (Fluvial-Marsh)} \longrightarrow \text{Foreset (Clinoform Slope)} \longrightarrow \text{Bottomset (Prodelta Basinal Clay)}",
            r"Gilbert-type deltas exhibit a three-fold tripartite architectural hierarchy: horizontal subaerial topset gravels/sands, inclined foreset cross-beds dipping at the angle of repose ($25^\circ-35^\circ$), and flat basinal bottomset clay beds prograding into the receiving basin.",
            "G.K. Gilbert (1885, USGS 5th Ann. Rep.); Sam Boggs Jr. (pp. 295–305)"
        )
    # 3. Aeolian & Desert
    if "star dune" in t_low or "slip face" in t_low or "barchan" in t_low or "dune" in t_low:
        return (
            r"\text{Wind Regime Index } (RDP/DP): \quad \text{Unidirectional } (RDP/DP > 0.8 \rightarrow \text{Barchan/Transverse}) \longleftrightarrow \text{Multidirectional } (RDP/DP < 0.3 \rightarrow \text{Star Dune})",
            "Star dunes originate under complex, multidirectional wind regimes characterized by high directional variability (low RDP/DP ratios), causing sand to accumulate vertically into giant pyramidal peaks flanked by three or more radiating sinuous slip faces.",
            "Bagnold (1941, The Physics of Blown Sand); Fryberger (1979, USGS Prof. Pap. 1052)"
        )
    if "yardang" in t_low or "abrasion" in t_low or "deflation" in t_low or "ventifact" in t_low:
        return (
            r"q_s \propto (u_* - u_{*t})^3 \quad [\text{Saltation Flux Sandblasting Dominance}]",
            "Yardangs are sculpted into cohesive mudstones or crystalline strata through the synergistic action of aerodynamic sandblasting (abrasion) concentrated within 1–2 meters of the surface, coupled with downwind deflationary evacuation of fine suspended dust.",
            "Blackwelder (1934, Yardangs, GSA Bull.); Arthur Holmes (pp. 493–498)"
        )
    # 4. Glacial & Periglacial
    if "glen" in t_low or "glacier" in t_low and "flow" in t_low or "velocity" in t_low and "ice" in t_low:
        return (
            r"\dot{\epsilon} = A \tau^n \quad [\text{Glen's Flow Law: } n \approx 3], \quad u(z) = u_b + \frac{2A}{n+1} (\rho g \sin\alpha)^n (H^{n+1} - (H-z)^{n+1})",
            "Glacial ice deforms as a non-linear, shear-thinning viscoplastic fluid governed by Glen's Flow Law. Horizontal flow velocity reaches its theoretical maximum at the glacier centerline and upper surface, decreasing with depth towards the bed and margins due to boundary frictional shear.",
            "J.W. Glen (1955, Proc. R. Soc. London); Paterson (The Physics of Glaciers, 3rd Ed.)"
        )
    if "iceberg" in t_low or "density" in t_low and "ice" in t_low or "archimedes" in t_low:
        return (
            r"\frac{V_{\text{submerged}}}{V_{\text{total}}} = \frac{\rho_{\text{ice}}}{\rho_{\text{seawater}}} = \frac{0.917\text{ g/cm}^3}{1.025\text{ g/cm}^3} \approx 0.895 \implies V_{\text{above}} \approx \frac{1}{9}\ (\sim 10.5\%)",
            "By Archimedes' Principle, a floating body displaces a volume of fluid equal to its total mass. Because glacial freshwater ice has a bulk density of ~0.917 g/cm³ compared to ~1.025 g/cm³ for oceanic seawater, approximately 8/9 of an iceberg's volume remains submerged beneath sea level.",
            "Arthur Holmes (Principles of Physical Geology, p. 623); Paterson (Physics of Glaciers)"
        )
    if "roches" in t_low or "drumlin" in t_low or "nivation" in t_low:
        return (
            r"\text{Stoss Side: } \sigma_n > 0 \implies \text{Abrasion (Striations/Polish)}; \quad \text{Lee Side: } \sigma_n \rightarrow 0,\ P_w \uparrow \implies \text{Quarrying / Plucking}",
            "Roches moutonnées are sculpted by moving subglacial ice across bedrock knolls: the upstream stoss face undergoes high compressive stress and intense striating abrasion, while the downstream lee face experiences localized cavitation and subglacial plucking along unconfined joint blocks.",
            "Benn & Evans (Glaciers and Glaciation, Ch. 9); Arthur Holmes (p. 632)"
        )
    # 5. Karst
    if "karst" in t_low or "stalactite" in t_low or "helictite" in t_low or "lapies" in t_low or "polje" in t_low:
        return (
            r"\text{CaCO}_3 + \text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{Ca}^{2+} + 2\text{HCO}_3^- \quad [\text{Degassing } \text{CO}_2 \uparrow \implies \text{Speleothem Precipitation}]",
            "Karstification is driven by carbonic acid dissolution along limestone discontinuities. As percolating waters charged with soil CO2 enter aerated cave chambers, CO2 degasses into the cave atmosphere, supersaturating the dripwater in calcite and depositing stalactites and stalagmites.",
            "Ford & Williams (Karst Hydrogeology and Geomorphology); W.D. Thornbury (pp. 317–335)"
        )
    # 6. Volcanism & Calderas
    if "volcan" in t_low or "caldera" in t_low or "lahar" in t_low or "nu" in t_low or "pelean" in t_low:
        return (
            r"\Delta V_{\text{chamber}} \gg \text{Magma Replenishment} \implies \sigma_t > \sigma_{\text{roof}} \implies \text{Piston / Ring-Fracture Collapse}",
            "Calderas are macroscopic collapse basins formed when rapid catastrophic drainage or violent explosive evacuation of an underlying shallow magma chamber leaves the volcanic edifice roof unsupported, inducing structural ring-fault collapse.",
            "Howel Williams (1941, Calderas and Their Origin); Cas & Wright (Volcanic Successions)"
        )
    # 7. Geomorphic Theories (Davis, Penck, Crickmay)
    if "davis" in t_low or "penck" in t_low or "panplain" in t_low or "peneplain" in t_low or "inversion" in t_low or "basin and range" in t_low:
        return (
            r"\text{Landscape} = f(\text{Structure, Process, Stage}) \quad [\text{Davisian Postulate}] \quad \text{vs.} \quad \frac{dz}{dt} = U(t) - E(t) \quad [\text{Penckian Dynamic Model}]",
            "William Morris Davis conceptualized landscape evolution as a sequential cycle operating through Youth, Maturity, and Old Age towards a featureless peneplain. Walter Penck countered that landforms reflect the simultaneous dynamic interaction between crustal uplift velocity U(t) and denudation rate E(t).",
            "W.M. Davis (1899); Walter Penck (1924, Morphologische Analyse); Thornbury (Principles of Geomorphology, Chs. 1–3)"
        )
        
    # Default Physical Geology fallback formula
    return (
        r"\text{Rate of Denudation } (D) = f(\text{Climate, Lithology, Relief, Time}) \quad \text{where } \nabla z = \frac{\partial z}{\partial t} + \vec{v}\cdot\nabla z",
        "Landscape evolution represents the conservation of mass and momentum across Earth's surface, governed by the continuous interplay between endogenic tectonic uplift and exogenic denudational processes.",
        "Arthur Holmes (Principles of Physical Geology); W.D. Thornbury (Principles of Geomorphology)"
    )

print("Specialized masterclass data module loaded successfully!")
