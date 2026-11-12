import json, os

def get_questions_part1():
    return [
        {
            "q_num": 1,
            "question": "Structural Geology deals with matters in the:",
            "options": {
                "a": "Solid state",
                "b": "Liquid state",
                "c": "Gaseous state",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Fundamentals of Structural Geology",
            "subtopic": "Scope of Structural Geology",
            "notes": "Structural geology primarily focuses on deformed solid rock bodies, but dynamic deformation processes directly involve magma/pore fluids (liquid state) and volcanic exhalations/fluid pressures (gaseous/supercritical fluids)."
        },
        {
            "q_num": 2,
            "question": "The 'true dip' of a bed is considered to be a:",
            "options": {
                "a": "Vector quantity",
                "b": "Scalar quantity",
                "c": "Either vector or scalar quantity",
                "d": "Neither vector nor scalar quantity"
            },
            "answer": "a",
            "topic": "Planar and Linear Structures",
            "subtopic": "True Dip and Strike",
            "notes": "True dip has both a definite magnitude (angle of maximum inclination relative to the horizontal) and a specific spatial direction (orthogonal to strike, directed down-dip) -> Vector quantity."
        },
        {
            "q_num": 3,
            "question": "The dip of a horizontal bed striking E-W is measured in the:",
            "options": {
                "a": "Horizontal plane",
                "b": "Vertical plane",
                "c": "Axial plane",
                "d": "Inclined plane"
            },
            "answer": "b",
            "topic": "Planar and Linear Structures",
            "subtopic": "Dip Measurement Geometry",
            "notes": "By geological definition, dip is the angle of inclination of a planar feature measured in a vertical plane perpendicular to the strike line."
        },
        {
            "q_num": 4,
            "question": "The amount of dip measured along the strike direction of a bed is always:",
            "options": {
                "a": "90°",
                "b": "60°",
                "c": "45°",
                "d": "Zero"
            },
            "answer": "d",
            "topic": "Planar and Linear Structures",
            "subtopic": "Apparent Dip",
            "notes": "Strike is defined as the line of intersection between a dipping bed and a horizontal datum plane; consequently, along the strike direction itself, the apparent dip is zero (tan alpha = tan delta * cos 90° = 0)."
        },
        {
            "q_num": 5,
            "question": "The maximum amount of dip of a bed is 20° and is measured along N 40°E. The strike direction of the bed is:",
            "options": {
                "a": "N-S",
                "b": "E-W",
                "c": "N 50°W - S 50°E",
                "d": "S 50°W"
            },
            "answer": "c",
            "topic": "Planar and Linear Structures",
            "subtopic": "Strike-Dip Orthogonality",
            "notes": "Strike direction is perpendicular to the true dip direction (N 40°E = 040°). Azimuth = 040° - 90° = 310° (N 50°W) or 040° + 90° = 130° (S 50°E)."
        },
        {
            "q_num": 6,
            "question": "Dip isogons are defined as the lines joining points of:",
            "options": {
                "a": "Equal thickness",
                "b": "Equal dip amount",
                "c": "Same age",
                "d": "Same strike direction"
            },
            "answer": "b",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Ramsay's Dip Isogons",
            "notes": "In Ramsay's (1967) fold classification, dip isogons connect points of identical dip (inclination) on the outer and inner bounding surfaces of a folded layer."
        },
        {
            "q_num": 7,
            "question": "In strata composed of horizontal beds, the bed outcropping at higher contours is:",
            "options": {
                "a": "Less resistant than the lower ones",
                "b": "More resistant than the lower ones",
                "c": "Older than the lower ones",
                "d": "Younger than the lower ones"
            },
            "answer": "d",
            "topic": "Geological Maps and Topography",
            "subtopic": "Rule of Superposition in Horizontal Strata",
            "notes": "In undeformed horizontal sedimentary strata, according to Steno's Law of Superposition, strata occurring at higher topographic contour elevations are stratigraphically younger than those below."
        },
        {
            "q_num": 8,
            "question": "In the case of dipping beds, progressively younger beds occur along the direction of dip if:",
            "options": {
                "a": "Dip > Slope",
                "b": "Dip < Slope",
                "c": "Dip = Slope",
                "d": "None of the above"
            },
            "answer": "a",
            "topic": "Geological Maps and Topography",
            "subtopic": "Rule of V's and Outcrop Succession",
            "notes": "When beds dip downstream or down-slope at an angle steeper than the ground slope (Dip > Slope), walking in the down-dip direction continuously exposes younger stratigraphic beds."
        },
        {
            "q_num": 9,
            "question": "The behaviour of perfectly elastic bodies is governed by:",
            "options": {
                "a": "Hooke's law",
                "b": "Hilt's law",
                "c": "Lambert's law",
                "d": "Bode's law"
            },
            "answer": "a",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Elastic Behavior",
            "notes": "Hooke's Law states that within the elastic limit, strain is directly proportional to applied stress (sigma = E * epsilon)."
        },
        {
            "q_num": 10,
            "question": "Hooke's law is applicable in the case of:",
            "options": {
                "a": "Stretching",
                "b": "Bending",
                "c": "Twisting",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Moduli of Elasticity",
            "notes": "Hooke's law governs all linearly elastic modes of deformation: uniaxial tension/compression (Young's modulus), flexural bending, and torsional shearing (Rigidity/Shear modulus)."
        },
        {
            "q_num": 11,
            "question": "Liquids and gases possess:",
            "options": {
                "a": "Bulk modulus of elasticity",
                "b": "Young's modulus of elasticity",
                "c": "Both 'a' and 'b'",
                "d": "Rigidity modulus of elasticity"
            },
            "answer": "a",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Bulk Modulus in Fluids",
            "notes": "Because fluids (liquids and gases) cannot permanently withstand shearing stress without flow, they have zero shear modulus (G=0) and zero Young's modulus (E=0). They only possess incompressibility/bulk modulus of elasticity (K)."
        },
        {
            "q_num": 12,
            "question": "Compressibility can be described as the reciprocal of:",
            "options": {
                "a": "Bulk modulus",
                "b": "Young's modulus",
                "c": "Rigidity modulus",
                "d": "None of the above"
            },
            "answer": "a",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Compressibility Definition",
            "notes": "Compressibility (beta) is quantitatively defined as the reciprocal of the bulk modulus of elasticity: beta = 1 / K = - (1/V) * (dV / dP)."
        },
        {
            "q_num": 13,
            "question": "Poisson's ratio is the ratio between:",
            "options": {
                "a": "Tangential stress and shearing strain",
                "b": "Transverse strain and axial strain",
                "c": "Hydrostatic pressure and volume strain",
                "d": "None of the above"
            },
            "answer": "b",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Poisson's Ratio",
            "notes": "Poisson's ratio (nu) is defined under uniaxial stress as the ratio of lateral/transverse strain (expansion) to longitudinal/axial strain (shortening): nu = - (epsilon_transverse / epsilon_axial)."
        },
        {
            "q_num": 14,
            "question": "The typical value of Poisson's ratio for crustal rocks is approximately:",
            "options": {
                "a": "0.25",
                "b": "0.50",
                "c": "1.00",
                "d": "1.50"
            },
            "answer": "a",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Poisson's Ratio of Rocks",
            "notes": "Most common silicate crustal rocks (granite, basalt, quartzite, limestone) exhibit Poisson's ratio in the range of 0.20 to 0.30, with an average value near 0.25 (Poisson solid: lambda = mu, nu = 0.25)."
        },
        {
            "q_num": 15,
            "question": "Substances that undergo a large plastic deformation before rupture are called:",
            "options": {
                "a": "Brittle",
                "b": "Ductile",
                "c": "Amorphous",
                "d": "Malleable"
            },
            "answer": "b",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Ductile Deformation",
            "notes": "Ductile materials sustain permanent strain exceeding 5% to 10% without loss of macroscopic cohesion or fracture before eventual rupture."
        },
        {
            "q_num": 16,
            "question": "If the strain is recoverable upon unloading but is also time-dependent, the deformation is known as:",
            "options": {
                "a": "Elastic",
                "b": "Elastoviscous (or Anelastic)",
                "c": "Plastic",
                "d": "Ductile"
            },
            "answer": "b",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Anelasticity and Viscoelasticity",
            "notes": "Anelastic / elastoviscous deformation is fully recoverable over time upon stress removal, exhibiting delayed strain recovery (elastic after-effect / Kelvin-Voigt behavior)."
        },
        {
            "q_num": 17,
            "question": "Direct stress acts:",
            "options": {
                "a": "Parallel to the surface of the body",
                "b": "Inclined to the surface of the body",
                "c": "Normal to the surface of the body",
                "d": "None of the above"
            },
            "answer": "c",
            "topic": "Stress Analysis",
            "subtopic": "Normal Stress",
            "notes": "Direct stress (normal stress, sigma_n) acts perpendicular (normal) to the reference plane, causing change in volume or longitudinal shortening/extension."
        },
        {
            "q_num": 18,
            "question": "In modern geologic practice, a compressive stress is conventionally considered:",
            "options": {
                "a": "Positive",
                "b": "Negative",
                "c": "Either positive or negative",
                "d": "Neither positive nor negative"
            },
            "answer": "a",
            "topic": "Stress Analysis",
            "subtopic": "Sign Conventions in Structural Geology",
            "notes": "In geological and rock mechanics conventions, compressive stress is treated as positive (+ve) because compressive tectonic stresses dominate the Earth's crust; tensile stress is negative (-ve)."
        },
        {
            "q_num": 19,
            "question": "If the orientations of the principal strain axes X, Y, and Z have changed relative to material lines during deformation, the process is known as:",
            "options": {
                "a": "Pure shear",
                "b": "Simple shear",
                "c": "Axial strain",
                "d": "Triaxial stress"
            },
            "answer": "b",
            "topic": "Strain Analysis",
            "subtopic": "Rotational Strain and Simple Shear",
            "notes": "In simple shear (rotational strain), the principal strain axes rotate during progressive deformation. In pure shear (irrotational strain), the principal strain axes maintain fixed spatial orientations."
        },
        {
            "q_num": 20,
            "question": "In a general stress (triaxial stress) system:",
            "options": {
                "a": "The three principal stresses are equal",
                "b": "The three principal stresses are unequal",
                "c": "The three principal stresses are unequal and have non-zero values (sigma_1 > sigma_2 > sigma_3 != 0)",
                "d": "None of the above"
            },
            "answer": "c",
            "topic": "Stress Analysis",
            "subtopic": "Triaxial Stress State",
            "notes": "A general 3D (triaxial) tectonic stress field is defined by three mutually perpendicular, unequal principal normal stresses where sigma_1 > sigma_2 > sigma_3 and all are non-zero."
        }
    ]

print("Part 1 questions loaded")

def get_questions_part2():
    return [
        {
            "q_num": 21,
            "question": "The inter-limb angles of folds give an indication of the:",
            "options": {
                "a": "Genesis of folds",
                "b": "Morphology of folds",
                "c": "Intensity of deformation",
                "d": "Type of deformation"
            },
            "answer": "c",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Inter-limb Angle and Fold Tightness",
            "notes": "According to Fleuty's (1964) classification, inter-limb angle directly reflects the intensity of tectonic shortening/deformation (gentle: 180°-120°, open: 120°-70°, close: 70°-30°, tight: 30°-0°, isoclinal: 0°)."
        },
        {
            "q_num": 22,
            "question": "Which of the following are folds characterized by a mutually parallel arrangement of limbs?",
            "options": {
                "a": "Symmetrical folds",
                "b": "Inverted folds",
                "c": "Reclined folds",
                "d": "Isoclinal folds"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Isoclinal Folds",
            "notes": "Isoclinal folds are defined by limbs that dip in the same direction at identical angles, maintaining a parallel arrangement with an interlimb angle approaching zero (0° to 10°)."
        },
        {
            "q_num": 23,
            "question": "In gentle folds ('Flexures'), the inter-limb angle lies between:",
            "options": {
                "a": "180° to 120°",
                "b": "120° to 70°",
                "c": "70° to 30°",
                "d": "30° to 0°"
            },
            "answer": "a",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Fleuty's Classification",
            "notes": "Under Fleuty's scheme, very gentle flexures have interlimb angles between 180° and 120°, representing minimal bulk tectonic shortening."
        },
        {
            "q_num": 24,
            "question": "A fold axis geometrically lies in the direction:",
            "options": {
                "a": "Parallel to hinges",
                "b": "Normal to hinges",
                "c": "Inclined to hinges",
                "d": "None of the above"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Fold Axis vs Hinge Line",
            "notes": "Strictly in structural geometry, the fold axis is an imaginary reference line of constant orientation which, when moved parallel to itself in space, generates the folded surface (applicable only to cylindrical folds). A hinge line is a physical line of maximum curvature."
        },
        {
            "q_num": 25,
            "question": "A fold profile is observed and drawn in a plane:",
            "options": {
                "a": "Parallel to fold axis",
                "b": "Perpendicular to fold axis",
                "c": "At 45° to fold axis",
                "d": "At 60° to fold axis"
            },
            "answer": "b",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Fold Profile Plane",
            "notes": "The true geometric profile of a cylindrical fold can only be viewed in the profile plane, which is oriented strictly perpendicular (orthogonal) to the fold axis/hinge line."
        },
        {
            "q_num": 26,
            "question": "A fold which is convex upwards and contains younger rocks in its core is termed a/an:",
            "options": {
                "a": "Anticline",
                "b": "Antiform",
                "c": "Antiformal syncline",
                "d": "Synform"
            },
            "answer": "c",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Facing and Inverted Folds",
            "notes": "Convex-upward geometry defines an 'antiform', but younger strata in the core defines a 'syncline'. Hence, an upward-closing fold in an inverted stratigraphic succession is an 'antiformal syncline'."
        },
        {
            "q_num": 27,
            "question": "A synform can be described as a/an:",
            "options": {
                "a": "Downward-facing syncline",
                "b": "Downward-closing fold structure",
                "c": "Upward-facing syncline",
                "d": "Upward-facing anticline"
            },
            "answer": "b",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Synform Geometry",
            "notes": "A synform is purely a morphological term denoting any fold that is concave upward (closes downward), irrespective of the stratigraphic age of the beds in its core."
        },
        {
            "q_num": 28,
            "question": "Folds characterized by sharp angular hinges and smooth planar limbs are termed:",
            "options": {
                "a": "Concertina folds",
                "b": "Concentric folds",
                "c": "Chevron folds",
                "d": "Cuspate folds"
            },
            "answer": "c",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Chevron and Accordion Folds",
            "notes": "Chevron folds (also termed accordion or concertina folds) exhibit straight, planar limbs meeting at narrow, acute, sharp angular hinges."
        },
        {
            "q_num": 29,
            "question": "Folds which exhibit a constant geometric profile across their entire lateral extent are termed:",
            "options": {
                "a": "Curvilinear folds",
                "b": "Concentric folds",
                "c": "Concertina folds",
                "d": "Cylindrical folds"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Cylindrical Folds",
            "notes": "A cylindrical fold has a rectilinear hinge line and maintains an unvarying cross-sectional profile when translated parallel to its fold axis."
        },
        {
            "q_num": 30,
            "question": "Match the fold types with their diagnostic geometric characteristics: (A) Conjugate folds, (B) Polyclinal folds, (C) Fan folds, (D) Cross folds:",
            "options": {
                "a": "A-1, B-2, C-3, D-4",
                "b": "A-4, B-3, C-2, D-1",
                "c": "A-2, B-1, C-4, D-3",
                "d": "A-2, B-3, C-4, D-1"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Complex Fold Terminology",
            "notes": "Conjugate folds feature paired axial surfaces dipping towards each other (2); Polyclinal folds exhibit multiple, variable axial surfaces (3); Fan folds have both limbs overturned dipping towards the core/axial plane (4); Cross folds result from superposed folding in multiple stages (1)."
        },
        {
            "q_num": 31,
            "question": "Which of the following statements is correct regarding parallel (concentric) folds?",
            "options": {
                "a": "Parallel folds maintain their shapes both upwards and downwards",
                "b": "Parallel folds maintain their shape upwards only",
                "c": "Parallel folds maintain their shape downwards only",
                "d": "Parallel folds do not maintain their shape either upwards or downwards indefinitely"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Space Problems in Parallel Folds",
            "notes": "Parallel (concentric) folds maintain constant orthogonal bed thickness (t = constant); consequently, radii of curvature change systematically from layer to layer, creating severe geometric space problems (anticlines become sharp cusps downwards; synclines become cusps upwards)."
        },
        {
            "q_num": 32,
            "question": "In parallel (concentric) folds, with increasing depth towards the core:",
            "options": {
                "a": "Anticlines and synclines become sharper with depth",
                "b": "Anticlines and synclines become broader with depth",
                "c": "Synclines become sharper with depth",
                "d": "Anticlines become sharper with depth"
            },
            "answer": "d",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Curvature Changes in Concentric Folds",
            "notes": "In concentric folding of an anticline, the center of curvature lies below the fold; as depth increases toward the center of curvature, the radius decreases (r -> 0), causing anticlinal cores to become progressively tighter, sharper, and eventually disharmonic/faulted."
        },
        {
            "q_num": 33,
            "question": "Systematic thickening of beds at fold crests/troughs and thinning along limbs is diagnostic of:",
            "options": {
                "a": "Parallel folds",
                "b": "Similar folds",
                "c": "Concentric folds",
                "d": "Flexural slip folds"
            },
            "answer": "b",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Similar Folds (Ramsay Class 2)",
            "notes": "Similar folds (Ramsay Class 2) maintain constant thickness parallel to the axial surface (T = constant), which geometrically requires extreme thinning along dipping limbs and thick accumulation at hinges/crests."
        },
        {
            "q_num": 34,
            "question": "Match the profile diagrams with their correct structural descriptions (Anticline, Antiform, Syncline, Synform):",
            "options": {
                "a": "A-1, B-2, C-3, D-4",
                "b": "A-2, B-1, C-3, D-4",
                "c": "A-2, B-1, C-4, D-3",
                "d": "A-1, B-2, C-4, D-3"
            },
            "answer": "c",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Facing and Curvature Relationships",
            "notes": "Profile distinctions correctly match morphological curvature (antiform vs synform) with stratigraphic facing (younging directions)."
        },
        {
            "q_num": 35,
            "question": "In which of the following fold types do both limbs dip towards each other?",
            "options": {
                "a": "Normal anticlines",
                "b": "Antiforms",
                "c": "Anticlinal fan folds",
                "d": "Synclinal fan folds"
            },
            "answer": "c",
            "topic": "Fold Geometry and Classification",
            "subtopic": "Fan Folds",
            "notes": "In an anticlinal fan fold, both limbs are overturned and dip inwardly towards each other and toward the axial plane."
        },
        {
            "q_num": 36,
            "question": "Choose the non-tectonic (gravitational or compactional) fold(s) from the following: (i) Décollement gliding folds, (ii) Supratenuous folds, (iii) Generative folds, (iv) Brachymorphic folds:",
            "options": {
                "a": "(i) only",
                "b": "(i) and (ii) only",
                "c": "(ii) and (iii) only",
                "d": "(i), (ii) and (iv) only"
            },
            "answer": "b",
            "topic": "Fold Mechanisms",
            "subtopic": "Non-Tectonic Folds",
            "notes": "Supratenuous folds form by differential compaction of sediments over pre-existing buried topographic highs; décollement gravity gliding folds originate primarily from gravitational downslope sliding rather than deep crustal tectonic compression."
        },
        {
            "q_num": 37,
            "question": "In supratenuous (compaction) folds, the sedimentary beds are characteristically:",
            "options": {
                "a": "Thick at the limbs but thinned at the crests",
                "b": "Thin at the crests but thickened along the flanks/limbs",
                "c": "Uniformly thick across crests and troughs",
                "d": "Thickened at the crests due to ductile flow"
            },
            "answer": "b",
            "topic": "Fold Mechanisms",
            "subtopic": "Supratenuous Fold Morphology",
            "notes": "In supratenuous folds developed by compaction over rigid bedrock ridges, the sedimentary column deposited over the ridge crest is thin, while off-structure basinal flank sediments are significantly thicker."
        },
        {
            "q_num": 38,
            "question": "A complex fold is structurally defined as one in which:",
            "options": {
                "a": "Smaller parasitic folds are superimposed on larger folds",
                "b": "Hinges are numerous and curved",
                "c": "The fold axis is itself folded by superposed deformation",
                "d": "The structure is too complex to be identified"
            },
            "answer": "c",
            "topic": "Superposed Folding",
            "subtopic": "Complex Folds",
            "notes": "A complex (refolded) fold displays non-rectilinear, curved, or refolded fold axes resulting from polyphase tectonic deformation (superposition of F2 on F1)."
        },
        {
            "q_num": 39,
            "question": "A map pattern displaying parallel straight outcrop bands that do not converge indicates a:",
            "options": {
                "a": "Non-plunging anticline or syncline",
                "b": "Plunging anticline",
                "c": "Doubly plunging syncline",
                "d": "Doubly plunging anticline"
            },
            "answer": "a",
            "topic": "Geological Maps and Topography",
            "subtopic": "Non-plunging vs Plunging Fold Outcrops",
            "notes": "Non-plunging folds (horizontal fold axis) produce parallel, un-converging linear outcrop bands on level ground. Plunging folds produce V-shaped or parabolic outcrop closures."
        },
        {
            "q_num": 40,
            "question": "The fundamental mechanical difference between folds and faults is that:",
            "options": {
                "a": "Folds are two-dimensional while faults are three-dimensional",
                "b": "Folds are three-dimensional while faults are two-dimensional",
                "c": "Folds are continuous ductile deformations of rock volumes while faults are planar mechanical discontinuities with displacement",
                "d": "Folds are associated with sedimentary rocks while faults occur only in igneous rocks"
            },
            "answer": "c",
            "topic": "Brittle vs Ductile Deformation",
            "subtopic": "Continuity of Deformation",
            "notes": "Folds represent continuous ductile strain without loss of rock cohesion throughout a 3D rock volume, whereas faults are brittle/frictional surfaces of discrete shear displacement (discontinuities)."
        }
    ]

print("Part 2 questions loaded")

def get_questions_part3():
    return [
        {
            "q_num": 41,
            "question": "Faults can be generated by tectonic regimes characterized by: (1) Extension, (2) Shear, (3) Compression, (4) Torsion:",
            "options": {
                "a": "1 and 2 only",
                "b": "1, 2 and 3 only",
                "c": "2, 3 and 4 only",
                "d": "3 and 4 only"
            },
            "answer": "b",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Fault Generation Regimes",
            "notes": "Anderson's classic dynamical fault theory identifies three fundamental tectonic stress regimes: extensional (normal faults), compressional (thrust/reverse faults), and strike-shear (wrench/strike-slip faults)."
        },
        {
            "q_num": 42,
            "question": "Faults are classified into parallel faults, en échelon faults, peripheral faults, and radial faults on the basis of:",
            "options": {
                "a": "Fault pattern in plan / map view",
                "b": "Rake of the net slip",
                "c": "Dip amount",
                "d": "Apparent movement of the blocks"
            },
            "answer": "a",
            "topic": "Fault Classification",
            "subtopic": "Geometric Patterns of Faults",
            "notes": "Parallel, en échelon (stepped), peripheral (ring-like), and radial (emanating from a central dome/intrusion) fault systems represent geometric map patterns of fault arrays."
        },
        {
            "q_num": 43,
            "question": "If the pitch (rake) of the net slip on a fault plane is 90°, the fault is strictly classified as a:",
            "options": {
                "a": "Strike-slip fault",
                "b": "Dip-slip fault",
                "c": "Diagonal-slip fault",
                "d": "Tear fault"
            },
            "answer": "b",
            "topic": "Fault Geometry",
            "subtopic": "Rake and Slip Vector",
            "notes": "When rake (pitch) = 90°, the net slip vector lies directly parallel to the true dip line of the fault plane, making it a pure dip-slip fault (normal or reverse)."
        },
        {
            "q_num": 44,
            "question": "The hade of a fault plane is defined as:",
            "options": {
                "a": "90° + Dip",
                "b": "90° - Dip",
                "c": "Plunge + Rake",
                "d": "Plunge + Dip"
            },
            "answer": "b",
            "topic": "Fault Geometry",
            "subtopic": "Hade Definition",
            "notes": "Hade is the complement of dip; it is the angle between the fault plane and the vertical plane: Hade = 90° - Dip."
        },
        {
            "q_num": 45,
            "question": "Tear faults are a specific genetic variety of:",
            "options": {
                "a": "Strike faults",
                "b": "Dip faults",
                "c": "Strike-slip faults",
                "d": "Dip-slip faults"
            },
            "answer": "c",
            "topic": "Fault Classification",
            "subtopic": "Tear Faults",
            "notes": "Tear faults (transverse faults) are strike-slip faults oriented transverse to regional fold axes or thrust fronts, accommodating differential forward displacement."
        },
        {
            "q_num": 46,
            "question": "Low-angle faults with normal stratigraphic displacement in extensional or gravity-collapse terrains are called:",
            "options": {
                "a": "Detachment faults (or Lag faults)",
                "b": "Underthrust faults",
                "c": "Gravity faults",
                "d": "Step faults"
            },
            "answer": "a",
            "topic": "Fault Classification",
            "subtopic": "Low-Angle Normal Faults",
            "notes": "Low-angle normal faults (dip < 30°) formed in regional extensional core complexes or gravity collapse are designated detachment faults or lag faults."
        },
        {
            "q_num": 47,
            "question": "Which of the following are NOT typically low-angle faults?",
            "options": {
                "a": "Overthrusts",
                "b": "Underthrusts",
                "c": "High-angle cylindrical / planar normal faults",
                "d": "Detachment faults"
            },
            "answer": "c",
            "topic": "Fault Classification",
            "subtopic": "Low-Angle vs High-Angle Faults",
            "notes": "Overthrusts, underthrusts, and basal detachment/décollement zones typically have low dips (< 30°), whereas standard Andersonian normal faults initiate at high angles (~60°)."
        },
        {
            "q_num": 48,
            "question": "In the case of an Andersonian normal fault, the hade is directed towards the:",
            "options": {
                "a": "Footwall side",
                "b": "Upthrown side",
                "c": "Either downthrown or upthrown side",
                "d": "Downthrown side"
            },
            "answer": "d",
            "topic": "Fault Geometry",
            "subtopic": "Normal Fault Geometry",
            "notes": "In a normal fault, the fault dips towards the downthrown block (hanging wall drops relative to footwall); therefore, the inclination (hade) is directed towards the downthrown side."
        },
        {
            "q_num": 49,
            "question": "The primary kinematic and tectonic consequence of thrust faulting is:",
            "options": {
                "a": "The footwall moves down relative to the hanging wall",
                "b": "The footwall moves up relative to the hanging wall",
                "c": "Substantial shortening and tectonic thickening of the crustal rocks",
                "d": "Very large stratigraphic omission"
            },
            "answer": "c",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Crustal Shortening",
            "notes": "Thrust faults accommodate horizontal crustal shortening (compression parallel to sigma_1), causing repetition of strata and vertical structural thickening."
        },
        {
            "q_num": 50,
            "question": "Thrust faults are structurally defined as:",
            "options": {
                "a": "Low-angle faults with reverse displacement (dip <= 45° or <= 30°)",
                "b": "Low-angle faults with normal displacement",
                "c": "High-angle normal faults",
                "d": "High-angle reverse faults"
            },
            "answer": "a",
            "topic": "Fault Classification",
            "subtopic": "Thrust Fault Definition",
            "notes": "A thrust fault is a reverse fault where the dip of the fault plane is gentle (typically <= 30° or <= 45°), placing older hanging-wall rocks over younger footwall rocks."
        },
        {
            "q_num": 51,
            "question": "Gravity faults (normal faults) develop primarily under a/an:",
            "options": {
                "a": "Compressive stress regime",
                "b": "Tensional / Extensional stress regime",
                "c": "Pure strike-shear regime",
                "d": "Isostatic hydrostatic regime"
            },
            "answer": "b",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Extensional Tectonics",
            "notes": "Gravity (normal) faults form in extensional stress regimes where the minimum principal stress (sigma_3) is horizontal and the maximum principal stress (sigma_1) is the vertical overburden load."
        },
        {
            "q_num": 52,
            "question": "Schuppen (imbricate) structures are characteristically associated with:",
            "options": {
                "a": "Normal faulting in rift basins",
                "b": "Transform strike-slip faulting",
                "c": "Thrust faulting in fold-and-thrust belts",
                "d": "Recumbent folding without shearing"
            },
            "answer": "c",
            "topic": "Thrust Tectonics",
            "subtopic": "Schuppen / Imbricate Structure",
            "notes": "Schuppen structure (German for 'scale structure') consists of a series of closely spaced, subparallel thrust sheets dipping in the same direction and overlapping like roof shingles."
        },
        {
            "q_num": 53,
            "question": "Thrust faults differ fundamentally from reverse faults in their:",
            "options": {
                "a": "Sense of relative movement",
                "b": "Type of tectonic stress regime",
                "c": "Amount of dip of the fault plane",
                "d": "Stratigraphic repetition effect"
            },
            "answer": "c",
            "topic": "Fault Classification",
            "subtopic": "Thrust vs Reverse Faults",
            "notes": "Both thrust and reverse faults exhibit hanging-wall-up displacement under compression; they are separated strictly by dip angle (thrust: dip <= 30° to 45°; reverse: dip > 45°)."
        },
        {
            "q_num": 54,
            "question": "Overthrusts can be dynamically described as:",
            "options": {
                "a": "Low-angle normal faults",
                "b": "High-angle reverse faults",
                "c": "Low-angle reverse faults with active footwall push",
                "d": "Low-angle thrust faults where the hanging wall is the active advancing element"
            },
            "answer": "d",
            "topic": "Thrust Tectonics",
            "subtopic": "Overthrust Dynamics",
            "notes": "In an overthrust, the upper/hanging wall block (allochthon) actively drives forward over the stationary or passive lower/footwall block (autochthon)."
        },
        {
            "q_num": 55,
            "question": "According to Anderson's dynamical theory of faulting, the greatest principal stress axis (sigma_1) is vertical in:",
            "options": {
                "a": "Normal faults",
                "b": "Reverse faults",
                "c": "Thrust faults",
                "d": "Strike-slip faults"
            },
            "answer": "a",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Anderson's Normal Faulting Criteria",
            "notes": "Anderson (1905, 1951) established that for normal faulting, sigma_1 (maximum compression) is vertical (overburden weight), sigma_2 is horizontal parallel to fault strike, and sigma_3 is horizontal extensional."
        },
        {
            "q_num": 56,
            "question": "The principal stress configuration diagnostic of Wrench (strike-slip) faults is that:",
            "options": {
                "a": "sigma_1 is horizontal and sigma_3 is vertical",
                "b": "sigma_2 is vertical while sigma_1 and sigma_3 are horizontal",
                "c": "sigma_1 is vertical and sigma_2 is horizontal",
                "d": "sigma_3 is vertical and sigma_1 is vertical"
            },
            "answer": "b",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Anderson's Strike-Slip Criteria",
            "notes": "In wrench/strike-slip faulting, the intermediate principal stress (sigma_2) is vertical, while the maximum (sigma_1) and minimum (sigma_3) stresses are both horizontal."
        },
        {
            "q_num": 57,
            "question": "Splay faults are geometrically described as:",
            "options": {
                "a": "Faults which display arc-like outcrops on a level surface",
                "b": "Short faults that overlap each other en échelon",
                "c": "Normal or reverse faults with parallel strikes",
                "d": "A complex branching arrangement of subsidiary faults diverging from a master fault"
            },
            "answer": "d",
            "topic": "Fault Geometry",
            "subtopic": "Splay Faults / Horsetail Termination",
            "notes": "Splay faults (horsetail splays) are subsidiary fractures that branch off from a master fault terminus or bend to dissipate shear stress."
        },
        {
            "q_num": 58,
            "question": "Match the tectonic/fault structures with their correct definitions: (A) Graben, (B) Klippe, (C) Step fault, (D) Triangle zone:",
            "options": {
                "a": "A-5, B-3, C-1, D-2",
                "b": "A-4, B-3, C-1, D-2",
                "c": "A-5, B-3, C-1, D-4",
                "d": "A-5, B-2, C-4, D-3"
            },
            "answer": "c",
            "topic": "Fault and Thrust Terminology",
            "subtopic": "Structural Complexes",
            "notes": "Graben = miniature rift valley bounded by conjugate normal faults (5); Klippe = erosional isolated remnant of a thrust sheet/nappe (3); Step fault = series of parallel normal faults stepping down in one direction (1); Triangle zone = wedge-like structure formed by opposing thrust and back-thrust (4)."
        },
        {
            "q_num": 59,
            "question": "Which of the following structural pairs is INCORRECT?",
            "options": {
                "a": "Triangular facets — normal fault scarps",
                "b": "Offset streams — strike-slip faults",
                "c": "Plumose markings — thrust faults",
                "d": "Palaeontologic break — disconformity"
            },
            "answer": "c",
            "topic": "Joints vs Faults",
            "subtopic": "Plumose Markings",
            "notes": "Plumose (hackle/feather) markings are delicate surface fringe ridges formed during rapid extensional propagation of mode-I tensile joints, NOT compressive shear thrust faults."
        },
        {
            "q_num": 60,
            "question": "Fluccan (or 'Pug') in fault terminology consists of:",
            "options": {
                "a": "Large angular blocks caught along faults",
                "b": "Broken angular fragments in a dark microcrystalline matrix",
                "c": "Minute glassy pseudotachylyte spherulites",
                "d": "Fine clayey powder / soft mud gouge developed along fault surfaces"
            },
            "answer": "d",
            "topic": "Fault Rocks",
            "subtopic": "Fault Gouge and Fluccan",
            "notes": "Fluccan (pug) is an old Cornish mining term for soft, water-saturated, un-indurated clay-rich fault gouge formed by frictional attrition of wall rocks."
        }
    ]

print("Part 3 questions loaded")

def get_questions_part4():
    return [
        {
            "q_num": 61,
            "question": "Joints are ubiquitously encountered in:",
            "options": {
                "a": "Sedimentary rocks only",
                "b": "Igneous rocks only",
                "c": "Metamorphic rocks only",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Joints and Fractures",
            "subtopic": "Occurrence of Joints",
            "notes": "Joints are the most widespread structural features in the lithosphere, cutting across all sedimentary, igneous, and metamorphic rock types without visible shear displacement."
        },
        {
            "q_num": 62,
            "question": "The orthogonal distance measured between two consecutive parallel joints in a set is defined as:",
            "options": {
                "a": "Slip cleavage",
                "b": "Crenulation cleavage",
                "c": "Joint spacing",
                "d": "Bedding fissility"
            },
            "answer": "c",
            "topic": "Joints and Fractures",
            "subtopic": "Joint Spacing",
            "notes": "Joint spacing is the perpendicular distance between adjacent fractures in a systematic joint set, governed by layer thickness and rock mechanical competence."
        },
        {
            "q_num": 63,
            "question": "Match the joint types with their genetic mechanisms: (A) Extension joints, (B) Sheeting / Exfoliation joints, (C) Conjugate joints, (D) Columnar joints:",
            "options": {
                "a": "A-2, B-1, C-4, D-3",
                "b": "A-3, B-4, C-1, D-2",
                "c": "A-2, B-1, C-4, D-3",
                "d": "A-2, B-4, C-1, D-3"
            },
            "answer": "c",
            "topic": "Joints and Fractures",
            "subtopic": "Genesis of Joints",
            "notes": "Extension joints form parallel to sigma_1 under tension (2); Sheeting results from unloading/unroofing residual stresses (1); Conjugate joints represent intersecting shear fractures (4); Columnar joints form by contractional thermal stresses during lava cooling (3)."
        },
        {
            "q_num": 64,
            "question": "Joints that develop strictly perpendicular to the fold axis/hinge line are termed:",
            "options": {
                "a": "Cross joints (ac-joints)",
                "b": "Release joints",
                "c": "Tension joints",
                "d": "Shear joints"
            },
            "answer": "a",
            "topic": "Joints and Fractures",
            "subtopic": "Cross Joints (ac-joints)",
            "notes": "In Sander's kinematic coordinate system, joints perpendicular to the b-axis (fold hinge) lie in the ac-plane and are termed cross joints (ac-joints), formed by longitudinal axial stretching."
        },
        {
            "q_num": 65,
            "question": "Cross joints (ac-joints) in folded strata are structurally defined as:",
            "options": {
                "a": "Columnar joints produced due to thermal contraction",
                "b": "Mud cracks formed by subaerial desiccation",
                "c": "Joints formed perpendicular to the fold axes",
                "d": "Joints formed parallel to the fold axes"
            },
            "answer": "c",
            "topic": "Joints and Fractures",
            "subtopic": "ac-Joint Definition",
            "notes": "Cross joints are tensile fractures striking normal to the fold hinge line, accommodating elongation parallel to the fold axis (b-axis)."
        },
        {
            "q_num": 66,
            "question": "Select the correct matches: (1) Cleat, (2) Mural joints, (3) Sheeting, (4) Systematic joints:",
            "options": {
                "a": "1-E (Jointing in coal), 2-A (Three mutually perpendicular sets in granites), 3-D (Unloading sheets), 4-B (Planar parallel sets)",
                "b": "1-E, 2-A, 3-D, 4-C",
                "c": "1-E, 2-A, 3-C, 4-B",
                "d": "1-D, 2-B, 3-C, 4-A"
            },
            "answer": "a",
            "topic": "Joints and Fractures",
            "subtopic": "Special Joint Types",
            "notes": "Cleat represents orthogonal joint sets in coal beds (E); Mural joints are three mutually orthogonal joint sets dividing granites into cuboidal blocks (A); Sheeting is curved sub-horizontal exfoliation (D); Systematic joints are planar, parallel sets cutting across other structures (B)."
        },
        {
            "q_num": 67,
            "question": "Delicate, plume-like ridges and microscopic arrest lines on planar joint surfaces are termed:",
            "options": {
                "a": "Slickensides",
                "b": "Feather joints",
                "c": "Plumose markings (or Hackle marks)",
                "d": "Piedmont scarps"
            },
            "answer": "c",
            "topic": "Joints and Fractures",
            "subtopic": "Plumose Structure",
            "notes": "Plumose (hackle) markings radiate from an initiation origin along joint faces, recording the direction and velocity of mode-I tensile fracture propagation."
        },
        {
            "q_num": 68,
            "question": "Match the standard geological map symbols: (A) Vertical foliation, (B) Vertical joint, (C) Vertical cleavage, (D) Vertical lineation:",
            "options": {
                "a": "A-1, B-2, C-3, D-4",
                "b": "A-2, B-1, C-4, D-3",
                "c": "A-3, B-2, C-4, D-1",
                "d": "A-2, B-3, C-1, D-4"
            },
            "answer": "d",
            "topic": "Geological Maps and Topography",
            "subtopic": "Structural Map Symbols",
            "notes": "Standard cartographic conventions distinguish planar structural attitudes (strike/dip of bedding, foliation, joints, cleavage) and linear plunges."
        },
        {
            "q_num": 69,
            "question": "When two sets of sedimentary strata are inclined at discordant angles to each other across an erosional surface, the contact is termed a/an:",
            "options": {
                "a": "Angular unconformity",
                "b": "Disconformity",
                "c": "Non-conformity",
                "d": "Paraconformity"
            },
            "answer": "a",
            "topic": "Unconformities",
            "subtopic": "Angular Unconformity",
            "notes": "An angular unconformity separates younger, gently dipping or horizontal strata from older, deformed, tilted, or folded strata below an erosional bevel."
        },
        {
            "q_num": 70,
            "question": "Which of the following statements is geometrically true regarding unconformities?",
            "options": {
                "a": "Unconformities are three-dimensional, non-directional stratigraphic surfaces / volumes",
                "b": "Unconformities are two-dimensional, directional features",
                "c": "Unconformities are three-dimensional, directional features",
                "d": "Unconformities are two-dimensional, non-directional features"
            },
            "answer": "a",
            "topic": "Unconformities",
            "subtopic": "Geometry of Unconformity Surfaces",
            "notes": "An unconformity represents a regional paleogeographic chronostratigraphic hiatus and ancient erosional land surface across a three-dimensional geological domain."
        },
        {
            "q_num": 71,
            "question": "A fundamental regional unconformity that marks a major crustal discontinuity and abrupt jump in seismic velocity is termed a:",
            "options": {
                "a": "Angular unconformity",
                "b": "First-order unconformity",
                "c": "Second-order unconformity",
                "d": "Zero-order unconformity"
            },
            "answer": "b",
            "topic": "Unconformities",
            "subtopic": "First-Order Unconformities",
            "notes": "First-order unconformities (megasequence boundaries) represent major inter-regional tectonic-eustatic breaks spanning tens of millions of years, often separating cratonic crystalline basement from overlying cover."
        },
        {
            "q_num": 72,
            "question": "Very brief depositional interruptions in sedimentation without discernible tectonic tilting or subaerial erosion are known as:",
            "options": {
                "a": "Blended unconformities",
                "b": "Heterolithic unconformities",
                "c": "Pinch-outs",
                "d": "Diastems"
            },
            "answer": "d",
            "topic": "Unconformities",
            "subtopic": "Diastems",
            "notes": "A diastem is a brief hiatus in sedimentation representing localized non-deposition or minor scour within a continuous depositional sequence, lacking significant faunal change."
        },
        {
            "q_num": 73,
            "question": "An unconformity where sedimentary strata are deposited upon an eroded surface of crystalline plutonic or deep metamorphic rocks is termed a/an:",
            "options": {
                "a": "Angular unconformity",
                "b": "Disconformity",
                "c": "Non-conformity",
                "d": "Blended unconformity"
            },
            "answer": "c",
            "topic": "Unconformities",
            "subtopic": "Non-conformity",
            "notes": "A non-conformity separates younger sedimentary or extrusive volcanic rocks above from older, deeply eroded intrusive igneous or high-grade metamorphic rocks below."
        },
        {
            "q_num": 74,
            "question": "Disconformities (parallel unconformities) are most definitively identified and distinguished by:",
            "options": {
                "a": "Visible angular discordance of beds",
                "b": "Variation in dip amounts across the contact",
                "c": "A significant faunal hiatus / break in the paleontological record",
                "d": "Differences in magnetic susceptibility"
            },
            "answer": "c",
            "topic": "Unconformities",
            "subtopic": "Identification of Disconformities",
            "notes": "Because strata above and below a disconformity are mutually parallel, the erosional gap is primarily detected by an abrupt biozonal/evolutionary break (faunal hiatus) in the fossil succession."
        },
        {
            "q_num": 75,
            "question": "In the field, an unconformable sedimentary contact can be distinguished from a fault contact by:",
            "options": {
                "a": "1 and 2 only",
                "b": "Presence of a basal conglomerate containing pebbles of the underlying rock (vs fault gouge/breccia)",
                "c": "2 and 3 only",
                "d": "1, 2 and 4 only"
            },
            "answer": "b",
            "topic": "Unconformities vs Faults",
            "subtopic": "Diagnostic Criteria",
            "notes": "A basal conglomerate containing water-worn, rounded pebbles of the underlying rock conclusively proves sedimentation upon an eroded substrate, whereas a fault contact exhibits cataclastic breccia, gouge, slickensides, and drag."
        },
        {
            "q_num": 76,
            "question": "An exposure of older rocks completely surrounded geographically and geologically by younger rocks is called a/an:",
            "options": {
                "a": "Inlier",
                "b": "Outlier",
                "c": "Overstep",
                "d": "Overlap"
            },
            "answer": "a",
            "topic": "Geological Maps and Topography",
            "subtopic": "Inliers",
            "notes": "An inlier is an outcrop area of older rocks surrounded on all sides by younger rocks, commonly exposed by erosion along an anticlinal crest or river valley."
        },
        {
            "q_num": 77,
            "question": "An isolated erosional remnant of younger rocks completely surrounded by older rocks is designated a/an:",
            "options": {
                "a": "Inlier",
                "b": "Fenster",
                "c": "Outlier",
                "d": "Diapir"
            },
            "answer": "c",
            "topic": "Geological Maps and Topography",
            "subtopic": "Outliers",
            "notes": "An outlier is an isolated patch of younger rocks surrounded by older strata, typically preserved in synclinal depressions or on isolated hilltops (buttes/mesas)."
        },
        {
            "q_num": 78,
            "question": "When younger beds in an unconformable marine transgressive succession progressively extend laterally beyond older beds, the relationship is termed:",
            "options": {
                "a": "Offlap",
                "b": "Overlap (or Onlap)",
                "c": "Overstep",
                "d": "Downlap"
            },
            "answer": "b",
            "topic": "Stratigraphic Terminology",
            "subtopic": "Onlap and Overlap",
            "notes": "Marine onlap (overlap) occurs during transgression when each younger sedimentary unit extends beyond the shoreline of the preceding unit, encroaching upon the paleotopographic high."
        },
        {
            "q_num": 79,
            "question": "A low-angle fault where the upper hanging-wall block appears to lag behind as the lower footwall block moves forward is termed a:",
            "options": {
                "a": "Normal fault",
                "b": "Lag fault",
                "c": "Thrust fault",
                "d": "Step fault"
            },
            "answer": "b",
            "topic": "Fault Classification",
            "subtopic": "Lag Faults",
            "notes": "A lag fault is a low-angle normal fault where the upper plate lags behind relative to the forward-moving lower mass (extensional attenuation behind an advancing nappe)."
        },
        {
            "q_num": 80,
            "question": "Which of the following statements are correct regarding a 'Geologic window' (Fenster)? (I) Older rocks are surrounded by younger rocks, (II) They are erosional depressions in large thrust sheets/nappes, (III) Older rocks crop out through the window, (IV) Younger autochthonous rocks crop out through the window:",
            "options": {
                "a": "I and III only",
                "b": "II and IV only",
                "c": "I, II and III only",
                "d": "II, III and IV only"
            },
            "answer": "b",
            "topic": "Thrust Tectonics",
            "subtopic": "Fenster / Geologic Window",
            "notes": "In a fenster (window), deep erosion through an allochthonous thrust sheet exposes the younger autochthonous (footwall) rocks, which are completely surrounded by older allochthonous rocks."
        }
    ]

print("Part 4 questions loaded")

def get_questions_part5():
    return [
        {
            "q_num": 81,
            "question": "The pitch (rake) and plunge of a fold hinge line coincide strictly when:",
            "options": {
                "a": "The axial plane of the fold is vertical",
                "b": "The axial plane is horizontal",
                "c": "The fold is asymmetrical",
                "d": "The fold is isoclinal"
            },
            "answer": "a",
            "topic": "Fold Geometry",
            "subtopic": "Pitch and Plunge Equivalence",
            "notes": "When the axial plane (or limb containing the lineation) is vertical (dip = 90°), the angle within the plane measured from the horizontal strike line (pitch) equals the vertical inclination angle (plunge): sin(plunge) = sin(pitch) * sin(dip)."
        },
        {
            "q_num": 82,
            "question": "An anticlinal bend is defined as a localized fold structure in which the dip of a bed:",
            "options": {
                "a": "Increases suddenly",
                "b": "Decreases suddenly",
                "c": "First increases and then decreases",
                "d": "Remains more or less constant"
            },
            "answer": "a",
            "topic": "Fold Terminology",
            "subtopic": "Anticlinal Bend",
            "notes": "In a structural monocline or flexural bend, the localized step where beds abruptly steepen downwards is termed an anticlinal bend; the lower bend where dip flattens back out is a synclinal bend."
        },
        {
            "q_num": 83,
            "question": "A fold in which the beds become progressively thicker towards the axial plane is termed a:",
            "options": {
                "a": "Parallel fold",
                "b": "Concentric fold",
                "c": "Chevron fold",
                "d": "Similar fold (or Class 2 / Generative fold)"
            },
            "answer": "d",
            "topic": "Fold Classification",
            "subtopic": "Similar Folds",
            "notes": "Similar folds exhibit convergence of dip isogons toward the inner arc, where orthogonal thickness increases substantially toward the hinge zone while thinning along the limbs."
        },
        {
            "q_num": 84,
            "question": "Folds that display multiple distinct hinge lines bounding a flattened crestal region are called:",
            "options": {
                "a": "Concentric folds",
                "b": "Chevron folds",
                "c": "Box folds (or Polyclinal folds)",
                "d": "Curvilinear folds"
            },
            "answer": "c",
            "topic": "Fold Classification",
            "subtopic": "Box Folds",
            "notes": "Box folds possess two or more separate hinges and two distinct axial surfaces that dip towards each other, creating a broad, flat crest flanked by steep limbs."
        },
        {
            "q_num": 85,
            "question": "A pericline is structurally defined as a fold in which:",
            "options": {
                "a": "The axial plane is tightly curved",
                "b": "Crests are thick while limbs are thinned",
                "c": "The diameter increases indefinitely along strike",
                "d": "The amplitude decreases regularly to zero in both axial directions (doubly plunging fold)"
            },
            "answer": "d",
            "topic": "Fold Classification",
            "subtopic": "Periclines",
            "notes": "A pericline (quaquaversal fold / brachy-anticline) plunges symmetrically in both directions along strike, such that fold amplitude vanishes at both terminations, yielding oval/elliptical outcrops."
        },
        {
            "q_num": 86,
            "question": "A set of minor folds of small wavelength systematically superimposed on major regional folds of large wavelength are termed:",
            "options": {
                "a": "Disharmonic folds",
                "b": "En échelon folds",
                "c": "Parasitic folds (Z, S, and M folds)",
                "d": "Digitational folds"
            },
            "answer": "c",
            "topic": "Fold Geometry",
            "subtopic": "Parasitic Folds and Pumpelly's Rule",
            "notes": "Parasitic folds obey Pumpelly's Rule: their axes, axial planes, and senses of asymmetry (S-folds on one limb, Z-folds on the other, M-folds at the hinge) mirror the parent regional fold structure."
        },
        {
            "q_num": 87,
            "question": "A structural 'Culmination' on a geological map is formed by:",
            "options": {
                "a": "The intersection of two anticlines belonging to different deformation generations (F1 and F2)",
                "b": "The intersection of two synclines",
                "c": "An anticline and a syncline crossing at right angles",
                "d": "A thrust fault cutting a recumbent fold"
            },
            "answer": "a",
            "topic": "Superposed Folding",
            "subtopic": "Culminations and Depressions",
            "notes": "Under Ramsay's Type 1 interference (dome-and-basin pattern), a culmination (structural dome) develops where the anticlinal crest of an F1 fold is crossed by the anticlinal crest of an F2 fold."
        },
        {
            "q_num": 88,
            "question": "In polyclinal folds, the multiple axial planes are characteristically:",
            "options": {
                "a": "Strictly horizontal",
                "b": "Strictly vertical",
                "c": "Inclined at varying orientations to one another",
                "d": "Mutually parallel"
            },
            "answer": "c",
            "topic": "Fold Classification",
            "subtopic": "Polyclinal Folds",
            "notes": "Polyclinal folds feature several intersecting or divergent axial surfaces that are inclined relative to each other within the same deformed packet."
        },
        {
            "q_num": 89,
            "question": "If the plunge of a fold hinge line reverses its direction along strike within a structural domain, the fold is described as a:",
            "options": {
                "a": "Doubly plunging fold",
                "b": "Non-plunging fold",
                "c": "Reclined fold",
                "d": "Linear fold"
            },
            "answer": "a",
            "topic": "Fold Geometry",
            "subtopic": "Doubly Plunging Folds",
            "notes": "When the hinge line undulates along strike such that its plunge angle reverses from one quadrant to the opposite, it creates a doubly plunging anticline (culmination) or doubly plunging syncline (depression)."
        },
        {
            "q_num": 90,
            "question": "A sudden horizontal flattening of dip in a uniformly dipping monocline produces a:",
            "options": {
                "a": "Anticlinal bend",
                "b": "Synclinal bend",
                "c": "Structural terrace",
                "d": "Recumbent fold"
            },
            "answer": "d",
            "topic": "Fold Terminology",
            "subtopic": "Structural Terraces",
            "notes": "A structural terrace is a local shelf-like flattening of dip within an otherwise uniformly dipping homoclinal series, bounded by an anticlinal bend above and synclinal bend below."
        },
        {
            "q_num": 91,
            "question": "Match the tectonic terms with their diagnostic structural characteristics: (A) Imbricate zone, (B) Structural depression, (C) Accordion fold, (D) Back-thrust:",
            "options": {
                "a": "A-4 (Stacking of thrust sheets), B-3 (Crossing synclines), C-2 (Sharp angular hinges), D-1 (Thrust directed opposite to main transport)",
                "b": "A-1, B-3, C-2, D-4",
                "c": "A-1, B-4, C-2, D-3",
                "d": "A-4, B-2, C-3, D-1"
            },
            "answer": "a",
            "topic": "Thrust and Fold Systems",
            "subtopic": "Structural Matching",
            "notes": "Imbricate zones represent stacked, roof-tile thrust sheets (4); structural depressions form at intersecting synclines (3); accordion folds have sharp angular hinges (2); back-thrusts propagate counter to regional transport (1)."
        },
        {
            "q_num": 92,
            "question": "Thrust faults in which the upper hanging-wall plate represents the actively translated kinematic element are called:",
            "options": {
                "a": "Underthrusts",
                "b": "Overthrusts",
                "c": "Upthrusts",
                "d": "Oversteps"
            },
            "answer": "b",
            "topic": "Thrust Tectonics",
            "subtopic": "Overthrust vs Underthrust",
            "notes": "In an overthrust, the hanging wall (allochthon) undergoes active forward horizontal transport over a relatively stationary footwall substrate."
        },
        {
            "q_num": 93,
            "question": "An 'overstep' (or out-of-sequence) thrust sequence is one in which newly generated thrust faults develop:",
            "options": {
                "a": "Exclusively in the footwall",
                "b": "In the hanging wall of older thrusts, breaching earlier structures",
                "c": "Alternately between footwall and hanging wall",
                "d": "Concurrently with blind décollements"
            },
            "answer": "b",
            "topic": "Thrust Tectonics",
            "subtopic": "Out-of-Sequence / Overstep Thrusts",
            "notes": "In contrast to normal 'piggy-back' (in-sequence, footwall-propagating) thrusting, an overstep (out-of-sequence) thrust cuts through pre-existing hanging-wall thrust sheets."
        },
        {
            "q_num": 94,
            "question": "In strike-slip (wrench) faulting, the kinematic simple shear regime induces:",
            "options": {
                "a": "Horizontal contraction parallel to sigma_1 and vertical extension parallel to sigma_2",
                "b": "Horizontal extension parallel to sigma_1 and vertical contraction parallel to sigma_3",
                "c": "Vertical contraction parallel to sigma_1 and horizontal extension parallel to sigma_3",
                "d": "Horizontal crustal contraction parallel to sigma_1 and horizontal crustal extension parallel to sigma_3"
            },
            "answer": "d",
            "topic": "Fault Mechanics and Andersonian Regimes",
            "subtopic": "Strike-Slip Kinematics",
            "notes": "In strike-slip tectonics, both sigma_1 (maximum compression) and sigma_3 (minimum compression / extension) are horizontal, producing horizontal shortening along sigma_1 and lateral extension along sigma_3."
        },
        {
            "q_num": 95,
            "question": "Transverse strike-slip faults that accommodate differential displacement across fold-and-thrust belts are known as:",
            "options": {
                "a": "Transform faults",
                "b": "Tear faults (or Compartmental faults)",
                "c": "Transcurrent faults",
                "d": "Lag faults"
            },
            "answer": "b",
            "topic": "Fault Classification",
            "subtopic": "Tear Faults",
            "notes": "Tear faults are steep, strike-slip faults oriented transverse to regional fold axes or thrust fronts, compartmentalizing segments moving at different velocities."
        },
        {
            "q_num": 96,
            "question": "The horizontal component of fault displacement measured perpendicular to the strike of the fault is termed:",
            "options": {
                "a": "Throw",
                "b": "Stratigraphic separation",
                "c": "Heave",
                "d": "Net slip"
            },
            "answer": "c",
            "topic": "Fault Geometry",
            "subtopic": "Heave and Throw",
            "notes": "On a dipping fault plane, the vertical component of dip slip is the 'throw', and the horizontal component measured perpendicular to fault strike is the 'heave' (Heave = Dip slip * cos(dip))."
        },
        {
            "q_num": 97,
            "question": "The sense of relative slip along a brittle fault plane is most reliably determined in the field using:",
            "options": {
                "a": "Rock color variations",
                "b": "Slickenside striations, polished surfaces, and fibrous mineral growth steps",
                "c": "Dip isogons",
                "d": "Boudinage necking"
            },
            "answer": "b",
            "topic": "Fault Kinematics",
            "subtopic": "Kinematic Indicators on Fault Planes",
            "notes": "Slickenside lineations define the slip lineation, and asymmetric quartz/calcite accretionary fiber steps indicate the direction in which the opposing wall block moved (rough-to-smooth tactile rule)."
        },
        {
            "q_num": 98,
            "question": "Mylonite rock fabrics are produced along ductile shear zones when:",
            "options": {
                "a": "Confining pressures are very low and strain rates are catastrophic",
                "b": "Deformation is purely brittle cataclastic crushing",
                "c": "Elevated temperatures and confining pressures favor crystal-plastic flow and dynamic recrystallization",
                "d": "Pore fluid pressure drops to zero"
            },
            "answer": "c",
            "topic": "Fault Rocks and Shear Zones",
            "subtopic": "Mylonite Genesis",
            "notes": "Mylonites are foliated, lineated metamorphic fault rocks formed at depths > 10-15 km by intense ductile shear strain involving dynamic recrystallization (grain-size reduction without loss of cohesion)."
        },
        {
            "q_num": 99,
            "question": "Pseudotachylyte is an enigmatic fault rock that originates primarily by:",
            "options": {
                "a": "Extreme frictional heating and melting of wall rocks during rapid seismic fault rupture",
                "b": "Hydrothermal quartz precipitation",
                "c": "Slow aseismic creep in salt domes",
                "d": "Diagenetic compaction of clay gouge"
            },
            "answer": "a",
            "topic": "Fault Rocks and Shear Zones",
            "subtopic": "Pseudotachylyte Genesis",
            "notes": "Pseudotachylytes are dark, aphanitic to glassy fault rocks formed by frictional melting along fault interfaces during high-velocity seismic coseismic slip (earthquake faulting)."
        },
        {
            "q_num": 100,
            "question": "Cataclasites are non-foliated fault rocks characterized by:",
            "options": {
                "a": "Intense plastic mylonitic foliation",
                "b": "Pseudomorphous replacement of feldspars",
                "c": "Angular rock fragments set in a finer matrix of crushed grains formed by brittle fracture without a coherent foliation",
                "d": "Presence of glass shards and quench microlites"
            },
            "answer": "c",
            "topic": "Fault Rocks and Shear Zones",
            "subtopic": "Cataclasite Characteristics",
            "notes": "Cataclasites form in the upper brittle crust by brittle fracturing, crushing, and comminution (cataclasis), exhibiting an un-foliated, random fabric of angular porphyroclasts in a microcrystalline matrix."
        },
        {
            "q_num": 101,
            "question": "In a ductile shear zone, progressive simple shear causes pre-existing planar markers and developing schistosity to curve:",
            "options": {
                "a": "Perpendicular to the shear zone boundaries",
                "b": "At a constant 90° angle to the slip direction",
                "c": "Asymptotically towards parallelism with the shear zone boundaries with increasing shear strain (gamma)",
                "d": "Into upright chevron folds"
            },
            "answer": "c",
            "topic": "Fault Rocks and Shear Zones",
            "subtopic": "Sigmoidal Foliation in Shear Zones",
            "notes": "Ramsay (1980) demonstrated that the inclination theta of the XY flattening plane decreases according to cot(2*theta) = gamma / 2, causing mylonitic foliation to rotate progressively toward the shear zone boundary."
        },
        {
            "q_num": 102,
            "question": "S-C mylonitic fabrics (where S is schistosity and C is cisaillement/shear bands) are invaluable for determining:",
            "options": {
                "a": "Absolute metamorphic temperature",
                "b": "Sense of tectonic shear (kinematic vorticity)",
                "c": "Stratigraphic facing",
                "d": "Poisson's ratio"
            },
            "answer": "b",
            "topic": "Fault Rocks and Shear Zones",
            "subtopic": "S-C Fabrics as Kinematic Indicators",
            "notes": "In S-C mylonites (Berthé et al., 1979), the oblique acute angle between the flattening foliation (S-surfaces) and the parallel shear bands (C-surfaces) definitively indicates the dextral or sinistral shear sense."
        },
        {
            "q_num": 103,
            "question": "In Ramsay's fold classification based on dip isogons, Class 1B folds represent:",
            "options": {
                "a": "Similar folds with parallel isogons",
                "b": "Parallel (concentric) folds with constant orthogonal thickness (t_alpha = 1.0)",
                "c": "Folds with widely divergent isogons",
                "d": "Shear folds with thickened limbs"
            },
            "answer": "b",
            "topic": "Ramsay's Fold Classification",
            "subtopic": "Class 1B Folds",
            "notes": "In Ramsay's system, Class 1B folds are true parallel/concentric folds where dip isogons are strictly perpendicular to layer boundaries, and orthogonal layer thickness remains perfectly constant (t_alpha = 1.0)."
        },
        {
            "q_num": 104,
            "question": "Ramsay's Class 3 folds are geometrically characterized by:",
            "options": {
                "a": "Parallel dip isogons of equal length",
                "b": "Strongly convergent dip isogons",
                "c": "Orthogonal thickness remaining uniform everywhere",
                "d": "Divergent dip isogons where the inner arc curvature is less than the outer arc, causing limbs to be thicker than the hinge zone"
            },
            "answer": "d",
            "topic": "Ramsay's Fold Classification",
            "subtopic": "Class 3 Folds",
            "notes": "In Class 3 folds, dip isogons diverge downward toward the inner arc, meaning the curvature of the outer arc exceeds that of the inner arc, and layers thicken along limbs relative to the hinge (incompetent layers between competent Class 1 layers)."
        }
    ]

print("Part 5 questions loaded")

def get_questions_part6():
    return [
        {
            "q_num": 105,
            "question": "A regional structural unit exhibiting uniform, constant planar dip and strike over a broad geographic extent without reversal of dip is termed a:",
            "options": {
                "a": "Plane homocline",
                "b": "Antihomocline",
                "c": "Synclinorium",
                "d": "Monocline"
            },
            "answer": "a",
            "topic": "Homoclines and Monoclines",
            "subtopic": "Homocline Definition",
            "notes": "A homocline represents a general succession of strata dipping uniformly in a single direction over large areas, without anticlinal or synclinal reversals."
        },
        {
            "q_num": 106,
            "question": "Folds whose lateral strike length is only moderately greater than their breadth, exhibiting an axial length-to-width ratio of less than 3:1, are called:",
            "options": {
                "a": "Linear folds",
                "b": "Cylindrical folds",
                "c": "Brachymorphic folds (or Brachy-anticlines / domes)",
                "d": "Cleavage folds"
            },
            "answer": "c",
            "topic": "Fold Classification",
            "subtopic": "Brachymorphic Folds",
            "notes": "Linear folds have length:width ratios > 3:1 (often 10:1 to 50:1); brachymorphic folds (domes, basins, periclines) are short, stubby folds with length:width ratios < 3:1."
        },
        {
            "q_num": 107,
            "question": "In linear or cylindrical folds, the axial ratio of strike length to fold width is characteristically:",
            "options": {
                "a": "Less than 3",
                "b": "More than 3 (typically exceeding 5 to 10)",
                "c": "Approximately equal to unity",
                "d": "Approaching zero"
            },
            "answer": "b",
            "topic": "Fold Classification",
            "subtopic": "Linear Fold Ratios",
            "notes": "Linear folds extend along their hinge lines for distances many times greater than their wavelength or breadth (length/width > 3)."
        },
        {
            "q_num": 108,
            "question": "The capacity of a deformed rock to split cleanly along closely spaced, smooth, parallel planar surfaces of secondary mechanical origin is defined as:",
            "options": {
                "a": "Bedding fissility",
                "b": "Sedimentary lamination",
                "c": "Rock cleavage (tectonic cleavage)",
                "d": "Jointing"
            },
            "answer": "c",
            "topic": "Cleavage and Foliation",
            "subtopic": "Rock Cleavage Definition",
            "notes": "Rock cleavage is a penetrative planar fabric of tectonic origin along which a deformed rock splits preferentially, produced by recrystallization and preferred dimensional orientation of platy minerals."
        },
        {
            "q_num": 109,
            "question": "Tectonic cleavage structures are broadly divided on the basis of their relationship to bedding and folds into:",
            "options": {
                "a": "Slaty cleavage and schistosity",
                "b": "Fracture cleavage and slip cleavage",
                "c": "Continuous cleavage and spaced cleavage",
                "d": "Axial plane cleavage and bedding cleavage"
            },
            "answer": "d",
            "topic": "Cleavage and Foliation",
            "subtopic": "Structural Classification of Cleavage",
            "notes": "Structurally, cleavage is classified into axial plane cleavage (oriented roughly parallel to the axial surface of regional folds) and bedding-parallel cleavage (parallel to original sedimentary layering)."
        },
        {
            "q_num": 110,
            "question": "In microscopic structural fabric classification, continuous cleavage comprises:",
            "options": {
                "a": "Slaty cleavage and schistosity",
                "b": "Slaty cleavage and fracture cleavage",
                "c": "Fracture cleavage and crenulation cleavage",
                "d": "Stylolitic cleavage and jointing"
            },
            "answer": "a",
            "topic": "Cleavage and Foliation",
            "subtopic": "Continuous Cleavage",
            "notes": "Continuous cleavage (slaty cleavage in slates, schistosity in schists) exhibits preferred alignment of phyllosilicates down to the sub-microscopic scale throughout the entire rock volume without un-cleaved microlithons."
        },
        {
            "q_num": 111,
            "question": "Regarding the spatial geometric relationship of cleavage to fold geometry, which of the following is correct?",
            "options": {
                "a": "Slaty cleavage converges upwards towards the anticlinal crest",
                "b": "Slaty cleavage converges downwards towards the anticlinal core while fracture cleavage fans out, converging upwards towards the top of an anticline",
                "c": "Both slaty and fracture cleavages converge downwards",
                "d": "Neither slaty nor fracture cleavage shows fanning"
            },
            "answer": "b",
            "topic": "Cleavage and Foliation",
            "subtopic": "Cleavage Refraction and Fanning",
            "notes": "Author Note 111 (b): In folded competent/incompetent layers, slaty cleavage displays an upward-diverging fan (converges downwards into the anticlinal core), while fracture cleavage in competent layers displays an upward-converging fan."
        },
        {
            "q_num": 112,
            "question": "The broad structural category of 'Spaced cleavage' includes:",
            "options": {
                "a": "Fracture cleavage + Slaty cleavage",
                "b": "Fracture cleavage + Flow cleavage",
                "c": "Fracture cleavage + Crenulation (slip) cleavage + Disjunctive cleavage",
                "d": "Mylonitic foliation + Schistosity"
            },
            "answer": "c",
            "topic": "Cleavage and Foliation",
            "subtopic": "Spaced Cleavage",
            "notes": "Spaced cleavage (Powell, 1979) consists of distinct cleavage domains (microshears/pressure solution seams) separated by wider slabs of relatively undeformed rock (microlithons), including fracture, crenulation, and disjunctive cleavages."
        },
        {
            "q_num": 113,
            "question": "Cleavage or schistosity that lies strictly parallel to original sedimentary bedding can originate from: (i) Static mimetic recrystallization during burial, (ii) Bedding-parallel flexural slip shear, (iii) Isoclinal folding where limbs and axial planes parallel bedding, (iv) Gravitational compaction:",
            "options": {
                "a": "(i) and (iv) only",
                "b": "(i), (ii) and (iv) only",
                "c": "(i), (iii) and (iv) only",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Cleavage and Foliation",
            "subtopic": "Bedding-Parallel Cleavage",
            "notes": "Bedding cleavage can result from burial/compaction, mimetic growth along pre-existing fissility, intense bedding-plane shear, or tight isoclinal transposition where axial surfaces and limbs become coplanar."
        },
        {
            "q_num": 114,
            "question": "Major regional fold axes can be accurately delineated in the field by measuring:",
            "options": {
                "a": "Joint strikes",
                "b": "Fault heaves",
                "c": "The Cleavage-Bedding intersection lineation (delta-lineation / L1)",
                "d": "Stylolite amplitudes"
            },
            "answer": "c",
            "topic": "Linear Structures",
            "subtopic": "Cleavage-Bedding Intersection Lineation",
            "notes": "Because axial planar cleavage intersects folded bedding surfaces along lines that run parallel to the regional fold hinge, the cleavage-bedding intersection lineation (L_intersection) directly defines the orientation and plunge of the fold axis."
        },
        {
            "q_num": 115,
            "question": "Lineations defined by the preferred dimensional orientation and ductile stretching of quartz ribbons, feldspar augen, or pebbles are called:",
            "options": {
                "a": "Mineral / Stretching lineation (X-direction)",
                "b": "Crenulation lineation",
                "c": "Intersection lineation",
                "d": "Striations"
            },
            "answer": "a",
            "topic": "Linear Structures",
            "subtopic": "Stretching Lineation",
            "notes": "Stretching lineations represent ductile finite elongation of rock elements, parallel to the maximum finite strain axis (X-axis of the strain ellipsoid)."
        },
        {
            "q_num": 116,
            "question": "Sausage-like, pinched, or boudinaged segments of a competent rock layer embedded within a more ductile incompetent matrix are termed:",
            "options": {
                "a": "Boudinage",
                "b": "Mullion",
                "c": "Crenulation",
                "d": "Ptygmatic folds"
            },
            "answer": "a",
            "topic": "Boudinage and Competence Contrast",
            "subtopic": "Boudinage Structure",
            "notes": "Boudinage (Ramberg, 1955) forms when a competent layer (e.g., amphibolite, sandstone) undergoes layer-parallel extension while being flattened between ductile incompetent layers (e.g., marble, shale), necking and fracturing into boudins."
        },
        {
            "q_num": 117,
            "question": "Mullion structures are structurally described as:",
            "options": {
                "a": "Linear arrays of tension gashes",
                "b": "Cylindrical, fluted, or cuspate ribbed columns formed along the boundary between rocks of contrasting competence during folding",
                "c": "Stylolitic columns in limestone",
                "d": "Striations on a fault mirror"
            },
            "answer": "b",
            "topic": "Linear Structures",
            "subtopic": "Mullions",
            "notes": "Mullions are cylindrical, corrugated rock columns parallel to the fold axis, formed at interfaces between layers of high competence contrast (e.g., quartzite and pelite), with cusps pointing into the more competent rock."
        },
        {
            "q_num": 118,
            "question": "Pure shear is mathematically and dynamically defined as a deformation in which:",
            "options": {
                "a": "Volumetric expansion occurs without shape change",
                "b": "Deformation is irrotational, such that the principal strain axes X, Y, and Z maintain constant orientations relative to material lines",
                "c": "Principal strain axes rotate continuously through 90°",
                "d": "Deformation occurs exclusively by slip along one set of planes"
            },
            "answer": "b",
            "topic": "Strain Analysis",
            "subtopic": "Pure Shear (Irrotational Strain)",
            "notes": "In pure shear (coaxial/irrotational strain), material lines parallel to the principal strain axes do not rotate during deformation; shortening occurs along Z and extension along X without rotation of the axes."
        },
        {
            "q_num": 119,
            "question": "In a coaxial triaxial stress and strain regime (pure shear), the kinematic relationship between principal stress and finite strain axes is:",
            "options": {
                "a": "X // sigma_1, Y // sigma_2, and Z // sigma_3",
                "b": "X // sigma_3 (minimum compression = maximum extension), Y // sigma_2, and Z // sigma_1 (maximum compression)",
                "c": "X // sigma_2, Y // sigma_1, and Z // sigma_3",
                "d": "Only Y corresponds with sigma_1"
            },
            "answer": "b",
            "topic": "Stress-Strain Relationships",
            "subtopic": "Principal Axes Correspondence in Coaxial Strain",
            "notes": "Maximum compressive stress (sigma_1) produces maximum shortening (Z-axis of finite strain ellipsoid), while minimum compressive stress (sigma_3) allows maximum elongation (X-axis of strain ellipsoid): X // sigma_3, Y // sigma_2, Z // sigma_1."
        },
        {
            "q_num": 120,
            "question": "In general, the three principal finite strain axes satisfy X >= Y >= Z. A deformation state of 'Plane Strain' is specifically defined by:",
            "options": {
                "a": "X > Y > Z with no constraints on Y",
                "b": "X = Y = Z (hydrostatic strain)",
                "c": "X > Y = 1 > Z (where the intermediate strain axis Y maintains its initial unit length without extension or shortening)",
                "d": "X = Y > Z (uniaxial oblate flattening)"
            },
            "answer": "c",
            "topic": "Strain Ellipsoid",
            "subtopic": "Plane Strain (Flinn k = 1)",
            "notes": "Author Note 120 (c): Plane strain is a special state of triaxial strain where the intermediate axis undergoes zero elongation (1 + e_2 = 1.0, Y = 1); shortening in Z is exactly balanced by elongation in X, plotting at k = 1 on the Flinn diagram."
        }
    ]

print("Part 6 questions loaded")

def get_questions_part7():
    return [
        {
            "q_num": 121,
            "question": "In Sander's kinematic fabric coordinate system (a, b, c), the 'a-axis' is defined as:",
            "options": {
                "a": "The direction of tectonic transport in which rock sheets slide past one another",
                "b": "The axis of rotation / fold axis",
                "c": "The normal to the slip plane",
                "d": "The pole to the axial surface"
            },
            "answer": "a",
            "topic": "Petrofabrics and Kinematic Coordinate Systems",
            "subtopic": "Kinematic a-axis",
            "notes": "Author Note 121 (a): The a-axis is the direction of tectonic transport (slip direction on an S-surface or direction of maximum particle elongation). The b-axis is the axis of rotation/fold axis. The c-axis is perpendicular to the ab slip plane."
        },
        {
            "q_num": 122,
            "question": "The fundamental linear relationship between shear stress (tau) and normal stress (sigma_n) required for frictional shear failure of rocks is expressed by the:",
            "options": {
                "a": "Hooke's law equation",
                "b": "Griffith failure criterion",
                "c": "Coulomb-Navier failure criterion (tau = C + sigma_n * tan(phi))",
                "d": "Tresca yield condition"
            },
            "answer": "c",
            "topic": "Rock Mechanics and Failure Criteria",
            "subtopic": "Coulomb-Navier Criterion",
            "notes": "The Coulomb-Navier failure criterion states that shear failure occurs along a plane when tau = C + mu * sigma_n, where C is cohesive shear strength, mu = tan(phi) is the coefficient of internal friction, and phi is the angle of internal friction."
        },
        {
            "q_num": 123,
            "question": "In graphical stress analysis, the envelope tangent to a series of Mohr stress circles representing rock failure under varying confining pressures is the:",
            "options": {
                "a": "Mohr equation",
                "b": "Mohr failure envelope",
                "c": "Yield locus",
                "d": "Flinn diagram boundary"
            },
            "answer": "b",
            "topic": "Stress Analysis and Failure Criteria",
            "subtopic": "Mohr Failure Envelope",
            "notes": "The Mohr failure envelope is the empirical curve tangent to all critical Mohr stress circles at failure, separating stable stress states from failure conditions."
        },
        {
            "q_num": 124,
            "question": "A rock or material that exhibits instantaneous recoverable elastic strain followed by time-dependent viscous relaxation is rheologically classified as:",
            "options": {
                "a": "Viscoelastic (Maxwell or Kelvin-Voigt body)",
                "b": "Elastoviscous",
                "c": "Bingham plastic",
                "d": "Purely ductile"
            },
            "answer": "a",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Viscoelastic Rheology",
            "notes": "Viscoelastic materials combine elastic springs and viscous dashpots, exhibiting instantaneous elastic strain upon loading and delayed time-dependent strain recovery upon unloading."
        },
        {
            "q_num": 125,
            "question": "Under progressively increasing differential stress and confining pressure, a crustal rock typically transitions through the sequential behavioral stages:",
            "options": {
                "a": "Elastic -> Viscous -> Viscoelastic -> Rupture",
                "b": "Viscous -> Viscoelastic -> Elastic -> Rupture",
                "c": "Viscous -> Anelastic -> Accelerated viscous -> Rupture",
                "d": "Elastic -> Viscoelastic -> Ductile / Viscous plastic -> Rupture (or ultimate ductile failure)"
            },
            "answer": "d",
            "topic": "Rock Mechanics and Rheology",
            "subtopic": "Progressive Deformation Sequence",
            "notes": "With increasing load, rock deformation progresses from linearly elastic, through viscoelastic/anelastic, to ductile plastic flow, ultimately terminating in shear rupture or cataclastic failure."
        },
        {
            "q_num": 126,
            "question": "In quantitative petrofabric analysis and structural stereographic projection, structural geologists exclusively employ:",
            "options": {
                "a": "Wulff stereonet (equal-angle projection)",
                "b": "Gnomonic projection",
                "c": "Orthographic net",
                "d": "Schmidt net (Lambert equal-area lower-hemisphere projection)"
            },
            "answer": "d",
            "topic": "Stereographic Projections and Petrofabrics",
            "subtopic": "Schmidt Equal-Area Net",
            "notes": "For statistical contouring of directional data (poles to bedding, foliation, mineral lineations, c-axes), an equal-area (Schmidt) net must be used to eliminate spatial area distortion across the projection."
        },
        {
            "q_num": 127,
            "question": "Petrofabric analysis encompasses the systematic microscopic and macroscopic investigation of:",
            "options": {
                "a": "Sedimentary grain size distribution only",
                "b": "Chemical assays of ore veins",
                "c": "Isotopic fractionation in zircons",
                "d": "The spatial preferred orientation (CPO and SPO) of all fabric elements, microstructures, and mineral lattices to decipher kinematic history"
            },
            "answer": "d",
            "topic": "Petrofabrics",
            "subtopic": "Scope of Petrofabric Analysis",
            "notes": "Petrofabrics (structural petrology, founded by Bruno Sander) studies the spatial distribution and preferred crystallographic/shape orientation of mineral grains to reconstruct finite strain and kinematic transport."
        },
        {
            "q_num": 128,
            "question": "Which of the following secondary structural fabrics represents an intermediate combination of both planar and linear fabric components?",
            "options": {
                "a": "Systematic joints",
                "b": "Pure slickensides",
                "c": "S-L tectonites (cleavage/schistosity combined with stretching lineation)",
                "d": "Columnar joints"
            },
            "answer": "c",
            "topic": "Fabric Classification",
            "subtopic": "S-L Tectonites",
            "notes": "Flinn classified deformed rocks into S-tectonites (pure planar flattening), L-tectonites (pure constrictional linear stretching), and S-L tectonites (exhibiting both strong planar schistosity and penetrative linear stretching)."
        },
        {
            "q_num": 129,
            "question": "In Sander's orthogonal kinematic fabric reference frame (a, b, c), which fabric axis corresponds to the direction of tectonic transport?",
            "options": {
                "a": "a-axis",
                "b": "b-axis",
                "c": "c-axis",
                "d": "None of the above"
            },
            "answer": "a",
            "topic": "Petrofabrics and Kinematic Coordinate Systems",
            "subtopic": "Transport Direction (a-axis)",
            "notes": "The a-axis represents the slip vector and direction of tectonic transport in the slip plane (ab-plane); b is the rotation/fold axis; c is normal to ab."
        },
        {
            "q_num": 130,
            "question": "Which groups of minerals are most commonly and effectively utilized in petrofabric universal-stage analysis?",
            "options": {
                "a": "Trigonal and Hexagonal minerals with uniaxial optical symmetry (e.g., Quartz and Calcite)",
                "b": "Tetragonal + Hexagonal + Orthorhombic minerals",
                "c": "Orthorhombic + Monoclinic + Triclinic minerals",
                "d": "Cubic isotropic minerals"
            },
            "answer": "a",
            "topic": "Petrofabrics",
            "subtopic": "Minerals in Petrofabric Analysis",
            "notes": "Author Note 130 (a): Uniaxial minerals (quartz in quartzites, calcite/dolomite in marbles) are favored because their single optic c-axis directly reveals crystallographic preferred orientation (CPO). Pseudo-hexagonal micas (biotite, muscovite) are also widely measured."
        },
        {
            "q_num": 131,
            "question": "Which of the following geological structures or fabric elements exhibits spherical (isotropic) fabric symmetry?",
            "options": {
                "a": "Spherulites",
                "b": "Geodes with concentric radial infillings",
                "c": "Undeformed spherical ooliths",
                "d": "All of the above"
            },
            "answer": "d",
            "topic": "Fabric Symmetry",
            "subtopic": "Spherical Fabric Symmetry",
            "notes": "Spherulites, concentric geodes, and undeformed spherical ooids possess infinite axes of rotational symmetry in all spatial directions, defining spherical Curie fabric symmetry (K_infinity_h)."
        },
        {
            "q_num": 132,
            "question": "A petrofabric pole diagram of rock samples collected from an orogenic terrain that has experienced multiple polyphase deformations typically displays:",
            "options": {
                "a": "Axial symmetry",
                "b": "Orthorhombic symmetry",
                "c": "Monoclinic symmetry",
                "d": "Triclinic symmetry (lowest symmetry, lacking any planes or axes of symmetry)"
            },
            "answer": "d",
            "topic": "Fabric Symmetry",
            "subtopic": "Triclinic Fabric Symmetry",
            "notes": "Superposition of multiple non-coaxial deformation phases (F1, F2, F3) destroys higher fabric symmetry planes, reducing the overall fabric symmetry of the petrofabric diagram to triclinic (asymmetry)."
        },
        {
            "q_num": 133,
            "question": "An asymmetric petrofabric diagram where fabric contours lack any mirror planes of symmetry is classified as possessing:",
            "options": {
                "a": "Axial symmetry",
                "b": "Orthorhombic symmetry",
                "c": "Monoclinic symmetry",
                "d": "Triclinic symmetry"
            },
            "answer": "d",
            "topic": "Fabric Symmetry",
            "subtopic": "Triclinic Symmetry Identification",
            "notes": "When fabric contours have no twofold rotation axis or mirror plane, the fabric possesses triclinic symmetry, characteristic of complex progressive non-coaxial shear."
        },
        {
            "q_num": 134,
            "question": "A B-tectonite (or L-tectonite) in Sander's classification is characteristically dominated by:",
            "options": {
                "a": "Penetrative planar flattening fabric",
                "b": "Penetrative linear fabric oriented parallel to the b-axis (fold hinge)",
                "c": "Non-penetrative planar fabric",
                "d": "Non-penetrative linear fabric"
            },
            "answer": "b",
            "topic": "Fabric Classification",
            "subtopic": "B-Tectonites",
            "notes": "A B-tectonite displays dominant linear fabric elements (mineral rodding, fold hinges, intersection lineations) aligned parallel to the regional b-axis of rotation."
        },
        {
            "q_num": 135,
            "question": "A vertical sectional diagram constructed along a designated line of exploration to portray subsurface geological structures is termed a:",
            "options": {
                "a": "Isolith map",
                "b": "Outcrop map",
                "c": "Contour map",
                "d": "Geological profile / Cross-section"
            },
            "answer": "d",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Geological Profile",
            "notes": "A geological cross-section or structural profile illustrates the subsurface spatial geometric arrangement, thickness, and attitudes of rock strata and faults along a chosen vertical plane."
        }
    ]

print("Part 7 questions loaded")

def get_questions_part8():
    return [
        {
            "q_num": 136,
            "question": "On a geological map, when an outcrop boundary of a planar bed cuts straight across topographic contours in a straight line regardless of elevation, it indicates the presence of a:",
            "options": {
                "a": "Vertical bed",
                "b": "Horizontal bed",
                "c": "Gently dipping bed",
                "d": "Fold hinge"
            },
            "answer": "a",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Rule of V's for Vertical Beds",
            "notes": "A perfectly vertical bed (dip = 90°) crops out as a straight line across all topography and contours, independent of topographic elevation differences (Rule of V's: vertical beds show no V-pattern)."
        },
        {
            "q_num": 137,
            "question": "On a topographic or structural contour map, if the spacing between consecutive contour lines is very narrow, it indicates the presence of a:",
            "options": {
                "a": "Steeply inclined / precipitous terrain",
                "b": "Gently sloping plain",
                "c": "Nearly horizontal plateau",
                "d": "Broad synclinal basin"
            },
            "answer": "a",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Contour Spacing and Slope",
            "notes": "Topographic slope angle is given by tan(theta) = contour interval / horizontal distance; closely spaced contours indicate high gradient and steep slopes."
        },
        {
            "q_num": 138,
            "question": "On a level erosional ground surface, concentric closed elliptical outcrop patterns are characteristically formed by:",
            "options": {
                "a": "Non-plunging cylindrical folds",
                "b": "Monoclines",
                "c": "Doubly plunging folds (anticlinal domes and synclinal basins / periclines)",
                "d": "Horizontal beds"
            },
            "answer": "c",
            "topic": "Geological Maps and Outcrops",
            "subtopic": "Elliptical Outcrops of Doubly Plunging Folds",
            "notes": "When an anticlinal dome or synclinal basin is truncated by a horizontal erosion plane, concentric elliptical outcrop rings are produced, with older rocks in the center for domes and younger rocks in the center for basins."
        },
        {
            "q_num": 139,
            "question": "On a geological map, closed concentric contours or outcrop bands where beds dip away in all directions from a central point represent a:",
            "options": {
                "a": "Synclinal basin",
                "b": "Structural dome (quaquaversal fold)",
                "c": "Graben",
                "d": "Horst"
            },
            "answer": "b",
            "topic": "Geological Maps and Outcrops",
            "subtopic": "Structural Domes and Basins",
            "notes": "In a structural dome, strata dip outward in all 360° directions (quaquaversal dip) away from the central crest, exposing the oldest rocks in the middle."
        },
        {
            "q_num": 140,
            "question": "When the spacing between successive contours on a topographic map remains perfectly constant across a slope, it signifies a:",
            "options": {
                "a": "Convex slope",
                "b": "Uniform (constant gradient) slope",
                "c": "Concave slope",
                "d": "Stepped terrace slope"
            },
            "answer": "b",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Uniform Slope",
            "notes": "Equidistant contour spacing reflects a constant horizontal equivalent per unit vertical elevation change, defining a uniform, planar slope."
        },
        {
            "q_num": 141,
            "question": "The simplest and most fundamental natural example of a topographic contour line on Earth is a/an:",
            "options": {
                "a": "Orocline",
                "b": "Coastline (shoreline at mean sea level)",
                "c": "Continental slope",
                "d": "Continental shelf break"
            },
            "answer": "b",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Coastline as Datum Contour",
            "notes": "A coastline is the intersection between the horizontal sea surface (mean sea level datum) and the terrestrial landmass, representing the zero-meter elevation contour line."
        },
        {
            "q_num": 142,
            "question": "Topographically and structurally, closed contour lines where higher elevation contours completely encircle lower inner contours define a:",
            "options": {
                "a": "Hill / Peak",
                "b": "Plateau",
                "c": "Depression / Basin (or crater/sinkhole)",
                "d": "Spur"
            },
            "answer": "c",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Topographic Depressions",
            "notes": "When closed contours decrease in elevation towards the interior, they define a topographic depression, caldera, or sinkhole (often marked with hachures pointing down-slope)."
        },
        {
            "q_num": 143,
            "question": "Match the typical contour patterns with their corresponding geomorphic features: (1) V-shaped contours pointing upstream, (2) Closely spaced parallel contours along a narrow corridor, (3) Widely spaced contours bounded by steep scarps:",
            "options": {
                "a": "1-A (River valley), 2-B (Ridge/escarpment), 3-C (Plateau)",
                "b": "1-A (River valley), 2-C (Ridge), 3-B (Plateau)",
                "c": "1-C, 2-A, 3-B",
                "d": "1-B, 2-A, 3-C"
            },
            "answer": "b",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Geomorphic Contour Forms",
            "notes": "River valleys display distinctive V-shaped contours pointing upstream toward higher elevations; ridges have elongated closely spaced contours; plateaus show broad flat areas (widely spaced contours) bounded by perimeter cliffs."
        },
        {
            "q_num": 144,
            "question": "As a rule of cartography, topographic contour lines can NEVER cross or merge with one another EXCEPT in the specific case of a/an:",
            "options": {
                "a": "Escarpment",
                "b": "Scarp slope",
                "c": "Vertical cliff or overhanging waterfall",
                "d": "Structural terrace"
            },
            "answer": "c",
            "topic": "Geological Maps and Field Methods",
            "subtopic": "Contour Intersection Rules",
            "notes": "Because a single point on the Earth's surface cannot possess two different elevations, contours cannot intersect except where a vertical cliff causes them to merge, or an overhanging rock ledge/waterfall causes higher contours to cross lower ones."
        },
        {
            "q_num": 145,
            "question": "A standard geologist's clinometer compass (e.g., Brunton, Freiberger) is designed to measure:",
            "options": {
                "a": "Strike direction only",
                "b": "Strike and dip directions only",
                "c": "Strike direction, dip direction, and dip angle (inclination)",
                "d": "Geomagnetic declination only"
            },
            "answer": "c",
            "topic": "Field Methods",
            "subtopic": "Clinometer Compass Usage",
            "notes": "A geological compass with an internal clinometer level measures the magnetic azimuth of strike and dip directions, as well as the vertical inclination angle (dip/plunge) using the clinometer pendulum."
        },
        {
            "q_num": 146,
            "question": "When non-oriented core drilling is employed to explore stratified beds, which structural attribute CANNOT be determined from a single vertical drill hole?",
            "options": {
                "a": "Rock thickness",
                "b": "Apparent inclination relative to core axis",
                "c": "Both true strike direction and true dip direction",
                "d": "Stratigraphic lithology"
            },
            "answer": "c",
            "topic": "Field Methods and Subsurface Exploration",
            "subtopic": "Borehole Structural Constraints",
            "notes": "A single non-oriented vertical drill core reveals only the dip angle relative to the core axis; true azimuths of strike and dip cannot be determined without a three-point borehole calculation or oriented core logging."
        },
        {
            "q_num": 147,
            "question": "Pi (pi) diagrams (pole nets) and Beta (beta) diagrams on an equal-area stereonet are classical graphical tools used for analyzing:",
            "options": {
                "a": "Folds (determining cylindrical fold axis orientation and interlimb angle)",
                "b": "Fault heaves",
                "c": "Joint spacing",
                "d": "Paleomagnetic polar wander"
            },
            "answer": "a",
            "topic": "Stereographic Projections",
            "subtopic": "Pi and Beta Diagrams for Folds",
            "notes": "In a pi-diagram, poles to folded bedding (pi-poles) define a great circle (pi-circle); the pole to this pi-circle defines the fold axis (beta-axis). In a beta-diagram, intersections of bedding planes directly locate the fold axis."
        },
        {
            "q_num": 148,
            "question": "Diapiric (piercement) structures, such as salt domes and mud diapirs, result dynamically from:",
            "options": {
                "a": "Horizontal tectonic compression in an initially competent rock",
                "b": "Purely vertical elastic rebound",
                "c": "Gravitational buoyancy (Rayleigh-Taylor instability) combined with differential overburden and tectonic stress acting on incompetent mobile layers",
                "d": "Thermal contraction"
            },
            "answer": "c",
            "topic": "Diapirs and Salt Tectonics",
            "subtopic": "Diapiric Folding",
            "notes": "Diapirs originate because low-density, ductile evaporites (halite) or overpressured shales become buoyant beneath denser overburden rock, piercing upward along faults and anticlinal cores."
        },
        {
            "q_num": 149,
            "question": "Gleitbrett (slip-board) folds originate primarily through:",
            "options": {
                "a": "Shear folding (differential slip along discrete parallel shear planes / microshears)",
                "b": "Homogeneous flow folding",
                "c": "Pure flexural slip folding",
                "d": "Gravitational compaction"
            },
            "answer": "a",
            "topic": "Fold Mechanisms",
            "subtopic": "Gleitbrett / Shear Folds",
            "notes": "Gleitbrett (German for 'slip board') folds develop where a rock mass is sliced by numerous parallel shear planes, with individual slabs sliding forward by differential amounts to produce passive fold geometries."
        },
        {
            "q_num": 150,
            "question": "Major strike-slip fault zones that strike perpendicularly across mid-oceanic ridge axes, accommodating differential seafloor spreading and terminating abruptly at ridge crests, are designated:",
            "options": {
                "a": "Tear faults",
                "b": "Transcurrent faults",
                "c": "Transform faults (J. Tuzo Wilson, 1965)",
                "d": "Lag faults"
            },
            "answer": "c",
            "topic": "Plate Tectonics and Fault Mechanics",
            "subtopic": "Transform Faults",
            "notes": "J. Tuzo Wilson (1965) recognized that ridge-ridge strike-slip boundaries are 'transform faults', where active seismic slip occurs only along the segment connecting offset spreading centers, with slip sense opposite to apparent map offset."
        }
    ]

print("Part 8 questions loaded")

def build_complete_dataset():
    all_q = (
        get_questions_part1() +
        get_questions_part2() +
        get_questions_part3() +
        get_questions_part4() +
        get_questions_part5() +
        get_questions_part6() +
        get_questions_part7() +
        get_questions_part8()
    )
    print(f"Total compiled questions: {len(all_q)}")
    assert len(all_q) == 150, f"Expected 150 questions, got {len(all_q)}"
    
    out_dir = "/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter7_StructuralGeology/data"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "sayeed_ch7_structural_geology.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_q, f, indent=2, ensure_ascii=False)
    
    print(f"Saved complete dataset to {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    build_complete_dataset()
