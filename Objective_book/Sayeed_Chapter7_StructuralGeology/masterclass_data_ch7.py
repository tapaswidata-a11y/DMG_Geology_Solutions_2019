#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 7: Structural Geology
Dr. Ausaf Sayeed - Objective Geology (150 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Stress Tensor, Principal Stresses & Mohr Circle
    if "stress" in t_low or "mohr" in t_low or "principal" in t_low or "triaxial" in t_low or "shear stress" in t_low:
        return (
            r"\sigma_n = \frac{\sigma_1 + \sigma_3}{2} + \frac{\sigma_1 - \sigma_3}{2}\cos(2\theta), \quad \tau = \frac{\sigma_1 - \sigma_3}{2}\sin(2\theta)",
            "The state of stress at any point in the lithosphere is fully defined by the second-rank Cauchy stress tensor. Resolving these forces across any plane inclined at angle theta to the maximum principal stress sigma_1 yields normal stress sigma_n and shear stress tau. In rock mechanics and structural geology, compressive stresses are conventionally treated as positive (+ve), with sigma_1 > sigma_2 > sigma_3.",
            "E.M. Anderson (1951, The Dynamics of Faulting); Jaeger, Cook & Zimmerman (Fundamentals of Rock Mechanics, 4th Ed.); Ramsay & Lisle"
        )

    # 2. Strain Ellipsoid, Flinn Diagram & Coaxiality
    if "strain" in t_low or "pure shear" in t_low or "simple shear" in t_low or "flinn" in t_low or "ellipsoid" in t_low or "plane strain" in t_low:
        return (
            r"k = \frac{(X/Y) - 1}{(Y/Z) - 1}, \quad \text{Plane Strain: } k = 1.0 \iff X > Y = 1.0 > Z, \quad \Delta = 0",
            "Finite strain is geometrically modeled by the deformation of an initial unit sphere into a triaxial strain ellipsoid with principal semi-axes X >= Y >= Z. Pure shear is coaxial and irrotational (material lines along principal axes do not rotate in space), whereas simple shear is non-coaxial and rotational (kinematic vorticity W_k = 1.0), causing continuous rotation of principal strain axes during progressive deformation.",
            "Derek Flinn (1962, On Folding during Three-Dimensional Progressive Deformation); J.G. Ramsay (1967, Folding and Fracturing of Rocks)"
        )

    # 3. Anderson's Dynamical Theory of Faulting
    if "anderson" in t_low or "normal fault" in t_low or "wrench" in t_low or "thrust fault" in t_low or "reverse fault" in t_low or "overthrust" in t_low or "strike-slip" in t_low:
        return (
            r"\text{Andersonian Stress Regimes:} \quad \begin{cases} \text{Normal Faults: } \sigma_1 \text{ Vertical}, \quad \text{Dip} \approx 60^\circ \\ \text{Thrust Faults: } \sigma_3 \text{ Vertical}, \quad \text{Dip} \approx 30^\circ \\ \text{Strike-Slip Faults: } \sigma_2 \text{ Vertical}, \quad \text{Dip} \approx 90^\circ \end{cases}",
            "E.M. Anderson (1905, 1951) recognized that the Earth's free surface cannot support shear stresses, requiring one of the three principal stress axes to be oriented perpendicular to the surface (vertical). Coulomb-Navier frictional shearing dictates that conjugate shear fracture planes form at an acute angle theta = 45° - phi/2 (typically ~30°) to the maximum compressive stress axis sigma_1.",
            "E.M. Anderson (1951, The Dynamics of Faulting and Dyke Formation); Davis, Reynolds & Kluth (Structural Geology, 3rd Ed.)"
        )

    # 4. Fold Classification, Dip Isogons & Ramsay's Classes
    if "isogon" in t_low or "ramsay" in t_low or "concentric" in t_low or "similar fold" in t_low or "class 1" in t_low or "class 2" in t_low or "class 3" in t_low:
        return (
            r"\text{Ramsay's Fold Metric: } t_\alpha = \frac{t_\alpha}{t_0}, \quad T_\alpha = \frac{T_\alpha}{T_0} = t_\alpha \sec\alpha, \quad \begin{cases} \text{Class 1B: } t_\alpha = 1.0 \ (\text{Parallel}) \\ \text{Class 2: } T_\alpha = 1.0 \ (\text{Similar}) \\ \text{Class 3: } \text{Divergent Isogons} \end{cases}",
            "J.G. Ramsay (1967) classified folded layers based on dip isogons—lines connecting points of equal inclination alpha on the outer and inner bounding surfaces. Class 1 folds display convergent isogons toward the inner arc (subdivided into 1A with thickened limbs, 1B true concentric parallel folds with constant orthogonal thickness, and 1C with thinned limbs). Class 2 folds have parallel isogons with constant thickness parallel to axial surface (similar folds). Class 3 folds show divergent isogons (incompetent layers).",
            "J.G. Ramsay (1967, Folding and Fracturing of Rocks, Ch. 7); Ramsay & Huber (Techniques of Modern Structural Geology, Vol. 2)"
        )

    # 5. Fleuty's Inter-limb Tightness & Fold Morphology
    if "inter-limb" in t_low or "fleuty" in t_low or "chevron" in t_low or "isoclinal" in t_low or "fan fold" in t_low or "pericline" in t_low or "box fold" in t_low:
        return (
            r"\text{Fleuty (1964) Tightness:} \quad \begin{cases} \text{Gentle: } 180^\circ - 120^\circ, & \text{Open: } 120^\circ - 70^\circ \\ \text{Close: } 70^\circ - 30^\circ, & \text{Tight: } 30^\circ - 0^\circ, \quad \text{Isoclinal: } 0^\circ \end{cases}",
            "Fold morphology and tightness record progressive tectonic shortening. Gentle folds (flexures) accommodate minimal crustal shortening (<15%), while tight and isoclinal folds reflect extreme shortening (>50% to >75%). In isoclinal folds, the interlimb angle approaches 0°, rendering both limbs mutually parallel and dipping in the same direction at equal angles.",
            "M.J. Fleuty (1964, The Description of Folds, Proc. Geol. Assoc.); George H. Davis"
        )

    # 6. Cleavage, Foliation, S-C Fabrics & Shear Zones
    if "cleavage" in t_low or "schistosity" in t_low or "foliation" in t_low or "mylonite" in t_low or "shear zone" in t_low or "boudinage" in t_low or "mullion" in t_low:
        return (
            r"\text{Shear Zone Trajectory: } \cot(2\theta) = \frac{\gamma}{2}, \quad \text{S-C Angle: } \theta \to 0^\circ \text{ as } \gamma \to \infty, \quad L_{\text{int}} = S_0 \cap S_1 \parallel \mathbf{b}",
            "Tectonic cleavage develops perpendicular to the finite maximum shortening axis Z (parallel to the XY flattening plane). In ductile shear zones, progressive simple shear rotates foliation (S-surfaces) asymptotically toward the shear zone boundary (C-surfaces). Cleavage-bedding intersection lineations (L_int) lie parallel to regional fold hinges (b-axis).",
            "Berthé, Choukroune & Jegouzo (1979); J.G. Ramsay (1980, Shear Zone Geometry); Passchier & Trouw (Microtectonics)"
        )

    # 7. Petrofabrics, Bruno Sander & Kinematic Coordinates
    if "petrofabric" in t_low or "sander" in t_low or "tectonite" in t_low or "a-axis" in t_low or "b-axis" in t_low or "symmetry" in t_low:
        return (
            r"\text{Sander's Kinematic Axes:} \quad \mathbf{a} \parallel \text{Slip / Transport}, \quad \mathbf{b} \parallel \text{Rotation / Fold Axis}, \quad \mathbf{c} \perp \mathbf{ab} \text{ Slip Plane}",
            "Bruno Sander (1930, 1970) established Gefügekunde (petrofabric analysis), establishing an orthogonal reference frame where 'a' is the tectonic transport direction, 'b' is the axis of external rotation (fold hinge line), and 'c' is normal to the slip surface. Fabric symmetries reflect deformation history: axial/spheroidal (pure compaction), orthorhombic (coaxial pure shear), monoclinic (non-coaxial simple shear), and triclinic (polyphase deformation).",
            "Bruno Sander (1930, Gefügekunde der Gesteine); F.J. Turner & L.E. Weiss (Structural Analysis of Metamorphic Tectonites)"
        )

    # 8. Unconformities, Outliers, Inliers & Geologic Maps
    if "unconformity" in t_low or "inlier" in t_low or "outlier" in t_low or "fenster" in t_low or "contour" in t_low or "dip" in t_low and "strike" in t_low:
        return (
            r"\text{Apparent Dip Formula:} \quad \tan\alpha = \tan\delta \cdot \cos\beta, \quad \text{Outcrop Width: } W = \frac{T}{\sin(\delta \pm \sigma)}",
            "Structural relationships on geological maps are governed by the Rule of V's and trigonometric spatial projections. An inlier exposes older rocks surrounded by younger ones; an outlier preserves younger rocks surrounded by older ones. In a fenster (window), deep erosion cuts through an allochthonous thrust sheet to expose younger autochthonous footwall rocks beneath.",
            "Billings (Structural Geology, 4th Ed.); Robert R. Compton (Geology in the Field); Bennison & Moseley"
        )

    # Default Structural Geology Fallback
    return (
        r"\text{Coulomb Failure Law: } \tau = C + \mu \sigma_n = C + \sigma_n \tan\phi, \quad \theta_{\text{fail}} = 45^\circ - \frac{\phi}{2} \approx 30^\circ \text{ to } \sigma_1",
        "Deformation of rock bodies represents the mechanical response to crustal stresses operating under varying confining pressures, temperatures, strain rates, and pore fluid pressures, creating systematic planar (foliations, faults, joints) and linear (fold axes, boudins, lineations) geometric structures.",
        "Twiss & Moores (Structural Geology, 2nd Ed.); Fossen (Structural Geology, 2nd Ed., Cambridge University Press)"
    )


def get_synthesis_table(q_num, topic, answer):
    t_low = topic.lower()

    if "stress" in t_low or "rheology" in t_low or "mechanics" in t_low:
        return {
            "title": "Mechanical and Rheological Properties of Crustal Rocks",
            "headers": ["Elastic Modulus / Parameter", "Mathematical Definition", "Typical Crustal Value", "Geological Significance"],
            "rows": [
                ["Young's Modulus (E)", r"E = \sigma / \epsilon", "20 - 80 GPa", "Uniaxial stiffness; governs flexural bending resistance"],
                ["Bulk Modulus (K)", r"K = - V (\Delta P / \Delta V)", "30 - 100 GPa", "Incompressibility; sole elastic modulus possessed by fluids"],
                ["Rigidity / Shear Modulus (G)", r"G = \tau / \gamma", "15 - 45 GPa", "Resistance to shear deformation; zero in liquids and gases"],
                ["Poisson's Ratio (nu)", r"\nu = - \epsilon_{\text{trans}} / \epsilon_{\text{axial}}", "0.20 - 0.30 (Avg ~0.25)", "Transverse strain expansion under axial compression"],
                ["Compressibility (beta)", r"\beta = 1 / K", "10^{-11} \text{ Pa}^{-1}", "Reciprocal of bulk modulus; crucial in basin compaction"]
            ]
        }

    if "fold" in t_low or "ramsay" in t_low or "fleuty" in t_low:
        return {
            "title": "Ramsay's (1967) Fold Classification Based on Dip Isogons",
            "headers": ["Fold Class", "Dip Isogon Geometry", "Thickness Relationship", "Dominant Kinematic Mechanism"],
            "rows": [
                ["Class 1A", "Strongly convergent toward inner arc", r"t_\alpha > 1.0 \text{ on limbs}", "Competent layer buckling under low ductility contrast"],
                ["Class 1B", "Perpendicular to bedding boundaries", r"t_\alpha = 1.0 \text{ (Constant)}", "True parallel / concentric folding via flexural slip"],
                ["Class 1C", "Weakly convergent toward inner arc", r"t_\alpha < 1.0 \text{ on limbs}", "Modified concentric fold with superimposed flattening"],
                ["Class 2", "Strictly parallel to axial surface", r"T_\alpha = 1.0 \text{ (Constant)}", "True similar fold; passive flow or shear folding"],
                ["Class 3", "Divergent downward toward inner arc", r"t_\alpha \gg 1.0 \text{ on limbs}", "Incompetent layers accommodated between stiff Class 1 layers"]
            ]
        }

    if "fault" in t_low or "thrust" in t_low or "anderson" in t_low:
        return {
            "title": "Anderson's (1905, 1951) Dynamical Classification of Tectonic Faults",
            "headers": ["Fault Class", "Stress State Orientation", "Nominal Dip Angle", "Tectonic Regime & Strain"],
            "rows": [
                ["Normal Fault", r"\sigma_1 \text{ Vertical}, \ \sigma_2, \sigma_3 \text{ Horizontal}", r"\approx 60^\circ", "Crustal extension; minimum stress horizontal"],
                ["Thrust / Reverse Fault", r"\sigma_3 \text{ Vertical}, \ \sigma_1, \sigma_2 \text{ Horizontal}", r"\le 30^\circ - 45^\circ", "Crustal shortening & thickening; maximum stress horizontal"],
                ["Wrench / Strike-Slip", r"\sigma_2 \text{ Vertical}, \ \sigma_1, \sigma_3 \text{ Horizontal}", r"\approx 90^\circ \text{ (Vertical)}", "Transcurrent / shear deformation; lateral simple shear"],
                ["Detachment / Lag Fault", r"\sigma_1 \text{ Vertical (Extensional gravity collapse)}", r"< 30^\circ \text{ (Low-angle)}", "Core complexes and extensional attenuation behind nappes"],
                ["Transform Fault", r"\text{Horizontal strike-slip offsetting spreading ridges}", r"90^\circ \text{ (Conservative)}", "Plate boundary shear active strictly between ridge crests"]
            ]
        }

    # Default Structural Features Table
    return {
        "title": "Kinematic Fabric Coordinates and Structural Elements",
        "headers": ["Fabric Axis / Feature", "Kinematic Role", "Associated Microstructure", "Regional Field Orientation"],
        "rows": [
            ["a-axis", "Tectonic transport / slip direction", "Stretching lineations, quartz ribbons", "Parallel to slip vector on thrusts / shear zones"],
            ["b-axis", "Axis of internal / external rotation", "Fold hinges, intersection lineations", "Coincides with regional cylindrical fold axes"],
            ["c-axis", "Normal to principal slip surface (ab)", "Poles to foliation, cleavage poles", "Direction of crustal tectonic shortening"],
            ["ac-joints (Cross joints)", "Perpendicular to fold axis (b-axis)", "Plumose markings, mode-I tension", "Accommodate axial elongation along fold chains"],
            ["S-surfaces / C-surfaces", "Flattening vs shear band foliation", "Mica fish, asymmetric porphyroclasts", "Defines shear sense (dextral vs sinistral) in mylonites"]
        ]
    }


def get_practice_problems(q_num, topic, answer):
    return [
        {
            "question": f"In a structural terrain, an overturned bed strikes N 30°E and dips 70° toward N 60°W. A bore hole is drilled vertically. What is the apparent dip observed in a vertical cross-section oriented N 30°W (perpendicular to strike)?",
            "options": {
                "a": "20°",
                "b": "70° (equals true dip)",
                "c": "45°",
                "d": "0°"
            },
            "answer": "b",
            "explanation": "Because the section line (N 30°W) is oriented strictly perpendicular to the strike (N 30°E), the cross-section plane coincides with the true dip direction (azimuth 300°), thereby displaying the full true dip magnitude of 70° without apparent dip reduction."
        },
        {
            "question": f"A deformed conglomerate contains ellipsoidal pebbles whose principal strain ratios are X/Y = 3.0 and Y/Z = 1.5. Calculate Flinn's k-parameter and classify the finite strain ellipsoid.",
            "options": {
                "a": "k = 0.5 (Oblate flattening)",
                "b": "k = 4.0 (Prolate constriction)",
                "c": "k = 1.0 (Plane strain)",
                "d": "k = 0 (Uniaxial flattening)"
            },
            "answer": "b",
            "explanation": "Flinn's parameter k = [(X/Y) - 1] / [(Y/Z) - 1] = (3.0 - 1) / (1.5 - 1) = 2.0 / 0.5 = 4.0. Because k > 1.0, the finite strain state plots in the field of apparent prolate constriction (cigar-shaped strain ellipsoid / L-tectonite)."
        }
    ]
