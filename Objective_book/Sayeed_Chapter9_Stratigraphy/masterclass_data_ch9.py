#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Stratigraphic Formulations, and Comparative Syntheses
for Chapter 9: Principles of Stratigraphy
Dr. Ausaf Sayeed - Objective Geology (50 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Seismic Stratigraphy & Acoustic Reflection
    if any(k in t_low for k in ["seismic", "reflection", "impedance", "acoustic", "p-wave"]):
        return (
            r"R = \frac{Z_2 - Z_1}{Z_2 + Z_1} = \frac{\rho_2 V_2 - \rho_1 V_1}{\rho_2 V_2 + \rho_1 V_1}, \quad \text{Impedance: } Z = \rho V_p",
            "Seismic stratigraphy (pioneered by Peter Vail and Exxon researchers, 1977) interprets seismic reflection configurations in terms of chronostratigraphic depositional sequences. Primary seismic reflections are generated at acoustic impedance contrasts across stratal bedding surfaces and unconformities. Because stratal surfaces represent chronostratigraphic timelines (isochronous depositional horizons across which velocity and density vary), reflection geometry faithfully maps ancient chronostratigraphic depositional geometry rather than diachronous lithofacies boundaries.",
            "Vail, P.R. et al. (1977, AAPG Memoir 26); Catuneanu, O. (Principles of Sequence Stratigraphy); Boggs, S. (Principles of Sedimentology and Stratigraphy)"
        )

    # 2. Stratigraphic Hierarchy & Dual Classification
    if any(k in t_low for k in ["hierarchy", "chronostratigraphic", "geochronologic", "stage", "series", "system", "epoch", "period", "era", "eon"]):
        return (
            r"\text{Equivalence Matrix: } \begin{cases} \text{Geochronologic (Time): } \text{Eon} \to \text{Era} \to \text{Period} \to \text{Epoch} \to \text{Age} \to \text{Chron} \\ \text{Chronostratigraphic (Strata): } \text{Eonothem} \to \text{Erathem} \to \text{System} \to \text{Series} \to \text{Stage} \to \text{Chronozone} \end{cases}",
            "International Stratigraphic Guides (Hedberg, 1976; Salvador, 1994) formalize dual classification: geochronologic units designate abstract geological time intervals, whereas chronostratigraphic units represent the physical stratal rock bodies deposited during those specific time intervals. For instance, the 'Jurassic System' represents physical rocks deposited during the 'Jurassic Period' of time.",
            "Hedberg, H.D. (1976, International Stratigraphic Guide); Salvador, A. (1994, IUGS/GSA); North American Commission on Stratigraphic Nomenclature (NACSN)"
        )

    # 3. Magnetostratigraphy & GPTS
    if any(k in t_low for k in ["magneto", "polarity", "brunhes", "matuyama", "gauss", "gilbert", "reversal"]):
        return (
            r"\text{Late Cenozoic GPTS: } \text{Gilbert (R: } 5.33\text{--}3.58\text{ Ma)} \to \text{Gauss (N: } 3.58\text{--}2.58\text{ Ma)} \to \text{Matuyama (R: } 2.58\text{--}0.78\text{ Ma)} \to \text{Brunhes (N: } 0.78\text{--}0\text{ Ma)}",
            "Magnetostratigraphy calibrates sedimentary sequences by recording periodic reversals of Earth's dipole geomagnetic field trapped as thermal or detrital remanent magnetization (TRM/DRM). Because geomagnetic field reversals are globally synchronous (occurring within ~1,000 to 5,000 years), magnetic polarity chrons provide absolute, worldwide chronostratigraphic correlation across diverse marine, lacustrine, and terrestrial facies.",
            "Opdyke, N.D. & Channell, J.E.T. (1996, Magnetic Stratigraphy); Gradstein et al. (Geologic Time Scale 2020); Cox, A. (Plate Tectonics and Geomagnetic Reversals)"
        )

    # 4. Superposition, Nicolas Steno & Way-up Criteria
    if any(k in t_low for k in ["superposition", "steno", "graded bedding", "cleavage", "way-up", "facing", "cave"]):
        return (
            r"\text{Steno's Law (1669): } t(z_{\text{lower}}) > t(z_{\text{upper}}) \iff \text{Upright Succession}, \quad \theta_{\text{cleavage}} > \theta_{\text{bedding}} \implies \text{Normal Facing}",
            "Nicolas Steno (1669, De Solido Intra Solidum) established the foundational principles of stratigraphy: Superposition, Original Horizontality, and Lateral Continuity. In deformed or overturned mountain belts, primary sedimentary structures (normal graded bedding, cross-bedding truncation, flame structures) and structural tectonite fabrics (cleavage dipping steeper than bedding in normal limbs, shallower than bedding in overturned limbs) dictate stratigraphic facing.",
            "Nicolas Steno (1669); Dunbar & Rodgers (Principles of Stratigraphy); Davis, Reynolds & Kluth (Structural Geology)"
        )

    # 5. Biostratigraphy, Faunal Succession & Biozones
    if any(k in t_low for k in ["biozone", "faunal succession", "index fossil", "smith", "epibole", "range zone", "assemblage zone"]):
        return (
            r"\text{Biozone Types: } \begin{cases} \text{Taxon-Range Zone: } \text{Total stratigraphic range between FAD and LAD of a single taxon} \\ \text{Assemblage Zone: } \text{Strata characterized by association of three or more taxa} \\ \text{Acme Zone (Epibole): } \text{Strata marking the peak abundance/climax of a taxon} \end{cases}",
            "William Smith (1799, 1815) discovered the Law of Faunal Succession: each geological formation possesses a unique and diagnostic fossil assemblage that succeeds others in a definite vertical sequence. Biostratigraphic units (biozones) operate independently of lithological boundaries, permitting inter-basinal correlation of time-equivalent strata.",
            "William Smith (1815, A Delineation of the Strata of England and Wales); Arkell, W.J. (Jurassic Geology of the World); Salvador, A. (1994)"
        )

    # 6. Indian Stratigraphy & Holland's Classification
    if any(k in t_low for k in ["holland", "indian", "purana", "dravidian", "aryan", "archaean"]):
        return (
            r"\text{Sir T.H. Holland's (1906) Scheme: } \text{Archaean (Basement)} \to \text{Purana (Proterozoic)} \to \text{Dravidian (Pz Marine)} \to \text{Aryan (Late Pz--Recent)}",
            "Sir Thomas H. Holland (1906) established the grand chronological architecture for the Indian subcontinent based on major unconformities and orogenic epochs: (1) Archaean Group (crystalline schists, gneisses, and greenstone belts); (2) Purana Group (unmetamorphosed Proterozoic intracratonic basins: Cuddapah, Vindhyan); (3) Dravidian Group (marine Paleozoic strata preserved in Extra-Peninsular Tethyan basins); and (4) Aryan Group (Upper Carboniferous to Recent: Gondwana Supergroup, Deccan Traps, and Siwaliks).",
            "Sir T.H. Holland (1906, Trans. Min. Geol. Inst. India); Krishnan, M.S. (Geology of India and Burma); Ramakrishnan & Vaidyanadhan (Geology of India, Vols. 1 & 2)"
        )

    # 7. Lithostratigraphy: Formations, Members & Walther's Law
    if any(k in t_low for k in ["formation", "member", "group", "bentonite", "lentil", "tongue", "walther"]):
        return (
            r"\text{Walther's Law of Facies (1894): } \text{Vertical Facies Succession } \equiv \text{ Lateral Facies Distribution without Unconformity}",
            "Lithostratigraphy classifies rock bodies based on macroscopic physical lithic properties. The Formation is the fundamental mapping unit (homogeneous lithology, mappable at 1:24,000 scale). Subordinate units include Members, Beds, Lentils (lens-shaped pinching units), and Tongues. Johannes Walther (1894) demonstrated that only environmentally adjacent depositional facies can succeed each other vertically in continuous conformable sedimentary sequences.",
            "Johannes Walther (1894, Einleitung in die Geologie als historische Wissenschaft); NACSN (2005, North American Stratigraphic Code); Boggs, S."
        )

    # Default Stratigraphic Framework
    return (
        r"\text{Chronostratigraphic Calibration: } \Delta t = \frac{\Delta z}{S_{\text{sed}}} + T_{\text{hiatus}}, \quad \text{GSSP Anchor: Golden Spike Datum}",
        "Principles of Stratigraphy integrate lithic, biological, geochemical, and geophysical signals to reconstruct Earth history. Modern chronostratigraphy anchors global chronostratigraphic stage boundaries with Global Boundary Stratotype Sections and Points (GSSPs), defining physical geological time-rock standards.",
        "Gradstein et al. (Geologic Time Scale 2020); Hedberg, H.D. (1976); Ausaf Sayeed (Objective Geology)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = (topic + " " + answer).lower()

    if any(k in t_low for k in ["hierarchy", "chronostratigraphic", "geochronologic", "time-rock"]):
        return {
            "title": "Comprehensive Dual Stratigraphic Hierarchy (ICS / IUGS Standards)",
            "headers": ["Chronostratigraphic (Rock Body)", "Geochronologic (Time Interval)", "Representative Global Example", "Diagnostic Formal Significance"],
            "rows": [
                ["Eonothem", r"\text{Eon}", "Phanerozoic Eonothem / Eon", "Highest formal rank; spans hundreds of millions to billions of years"],
                ["Erathem", r"\text{Era}", "Mesozoic Erathem / Era", "Major macroevolutionary and tectonic era; bounded by mass extinctions"],
                ["System", r"\text{Period}", "Devonian System / Period", "Primary chronostratigraphic unit; global correlation baseline"],
                ["Series", r"\text{Epoch}", "Upper Cretaceous Series / Epoch", "Subdivision based on major biostratigraphic / isotopic turnover"],
                ["Stage", r"\text{Age}", "Maastrichtian Stage / Age", "Fundamental working unit of chronostratigraphy; anchored by GSSP"]
            ]
        }

    if any(k in t_low for k in ["seismic", "reflection", "impedance", "p-wave"]):
        return {
            "title": "Seismic Stratigraphy: Reflection Terminations & System Tracts",
            "headers": ["Seismic Parameter / Pattern", "Acoustic / Geometric Definition", "Stratigraphic Significance", "Depositional Environment Proxy"],
            "rows": [
                ["Onlap", r"\text{Stratal termination against steeper initial slope}", "Base of transgressive / lowstand systems tract", "Relative sea-level rise and coastal encroachment"],
                ["Toplap", r"\text{Termination against upper depositional limit}", "Sedimentary bypassing / base level standstill", "Deltaic progradation and basin infill"],
                ["Truncation (Erosional)", r"\text{Lateral termination against overlying unconformity}", "Sequence boundary / subaerial erosion", "Major lowstand falling stage / tectonic uplift"],
                ["Acoustic Impedance Contrast", r"Z = \rho V_p \implies R = \frac{Z_2 - Z_1}{Z_2 + Z_1}", "Generates primary seismic reflection amplitude", "Lithological change across isochronous stratal bedding"]
            ]
        }

    if any(k in t_low for k in ["magneto", "polarity", "gpts"]):
        return {
            "title": "Late Cenozoic Geomagnetic Polarity Time Scale (GPTS)",
            "headers": ["Magnetic Polarity Chron", "Polarity State", "Numerical Age Range (Ma)", "Stratigraphic / Paleomagnetic Key Events"],
            "rows": [
                ["Brunhes", r"\text{Normal Polarity (+ve)}", "0.78 Ma to Present", "Current geomagnetic polarity epoch; contains Laschamp excursion"],
                ["Matuyama", r"\text{Reversed Polarity (--ve)}", "2.58 to 0.78 Ma", "Includes Olduvai (1.94-1.78 Ma) and Jaramillo (1.07-0.99 Ma) normal subchrons"],
                ["Gauss", r"\text{Normal Polarity (+ve)}", "3.58 to 2.58 Ma", "Pliocene warm interval; bounded by Mammoth and Kaena reversed subchrons"],
                ["Gilbert", r"\text{Reversed Polarity (--ve)}", "5.33 to 3.58 Ma", "Oldest Late Cenozoic chron; encompasses Miocene-Pliocene boundary"]
            ]
        }

    if any(k in t_low for k in ["holland", "indian", "purana", "dravidian", "aryan"]):
        return {
            "title": "Sir T.H. Holland's Classification of Indian Geological Formations",
            "headers": ["Grand Division", "Geological Age", "Key Lithological Formations", "Tectonic Setting & Stratigraphic Characteristics"],
            "rows": [
                ["Archaean Group", r"\text{Precambrian (>2500 Ma)}", "Dharwar Supergroup, Peninsular Gneiss, Charnockites", "Crystalline metamorphic basement, granite-greenstone belts"],
                ["Purana Group", r"\text{Proterozoic (2500--540 Ma)}", "Cuddapah Supergroup, Vindhyan Supergroup, Delhi System", "Unmetamorphosed, flat-lying intracratonic sedimentary basins"],
                ["Dravidian Group", r"\text{Cambrian to Carboniferous}", "Spiti Paleozoic sequence, Kashmir Paleozoic, Salt Range", "Marine fossiliferous strata restricted to Extra-Peninsular Tethys"],
                ["Aryan Group", r"\text{Upper Carboniferous to Recent}", "Gondwana Supergroup, Deccan Traps, Siwalik Group", "Continental coal basins, flood basalt volcanism, Himalayan foreland"]
            ]
        }

    # Default Stratigraphic Synthesis Matrix
    return {
        "title": f"Synthesis Matrix: {topic} - Stratigraphic Architecture",
        "headers": ["Diagnostic Parameter", "Formal Definition", "Operational Criterion", "Stratigraphic Application"],
        "rows": [
            ["Unit Classification", r"\text{" + topic[:25] + r"}", "Litho-, Bio-, or Chronostratigraphic", "Defines stratal boundaries and rank hierarchy"],
            ["Physical Continuity", r"\text{Lateral Tracing \& Correlation}", "Well logs, seismic, outcrop mapping", "Establishes inter-basinal depositional continuity"],
            ["Temporal Resolution", r"\text{Isochronous vs Diachronous}", "Biostratigraphic datums, radiometric ages", "Distinguishes time-rock units from facies boundaries"],
            ["Global Standard", r"\text{GSSP Golden Spike Reference}", "Standard stratotype section and point", "Worldwide chronostratigraphic boundary calibration"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    t_low = topic.lower()

    if any(k in t_low for k in ["hierarchy", "chronostratigraphic", "unit"]):
        return [
            {
                "question": "Which of the following represents the correct pairing between a chronostratigraphic unit and its corresponding geochronologic time unit?",
                "options": {
                    "a": "System — Epoch",
                    "b": "Series — Epoch",
                    "c": "Stage — Period",
                    "d": "Erathem — Age"
                },
                "answer": "b",
                "explanation": "In standard international stratigraphic terminology (Hedberg, 1976), the chronostratigraphic unit 'Series' (the rock body) corresponds strictly to the geochronologic time unit 'Epoch'."
            },
            {
                "question": "What is the primary operational distinction between a lithostratigraphic unit (e.g., Formation) and a chronostratigraphic unit (e.g., Stage)?",
                "options": {
                    "a": "Lithostratigraphic units are strictly isochronous, whereas chronostratigraphic units are diachronous",
                    "b": "Lithostratigraphic units are defined solely by physical lithology and are frequently diachronous, whereas chronostratigraphic units represent rocks deposited during an isochronous time interval",
                    "c": "Lithostratigraphic units cannot be mapped in the field, whereas chronostratigraphic units can",
                    "d": "Lithostratigraphic units require index fossils for their definition"
                },
                "answer": "b",
                "explanation": "Formations and members are lithostratigraphic units bounded by lithological changes that often migrate across time (diachronous via Walther's Law), whereas chronostratigraphic units are bounded by isochronous time horizons."
            }
        ]

    # Default Stratigraphy Practice
    return [
        {
            "question": "According to Walther's Law of Facies, which of the following statements is strictly correct?",
            "options": {
                "a": "Any two facies found anywhere in a basin can appear stacked vertically in conformable succession",
                "b": "Only those depositional facies that can be observed forming laterally adjacent to one another today can succeed each other in vertical conformable succession without unconformity",
                "c": "Deep abyssal facies can directly overlie terrestrial desert sands in conformable succession without a hiatus",
                "d": "Vertical facies variations are completely independent of lateral environmental shifts"
            },
            "answer": "b",
            "explanation": "Walther's Law states that only those facies that can be observed forming side-by-side in laterally adjacent environments can be superimposed in vertical conformable succession without the presence of a stratigraphic break or unconformity."
        },
        {
            "question": "Why do altered volcanic ash layers (bentonite beds) serve as superior isochronous chronostratigraphic marker horizons compared to sandstone or limestone beds?",
            "options": {
                "a": "Volcanic ash is deposited instantaneously over vast geographical areas cutting across diverse sedimentary environments",
                "b": "Volcanic ash contains abundant diagnostic macrofossils",
                "c": "Volcanic ash deposits are restricted to a single depositional basin",
                "d": "Volcanic ash never undergoes diagenetic alteration"
            },
            "answer": "a",
            "explanation": "Explosive plinian volcanic eruptions disperse ash clouds into the upper atmosphere, settling synchronously within days across thousands of square kilometers across marine and continental basins, creating perfect isochronous chronostratigraphic time-markers."
        }
    ]
