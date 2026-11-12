#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 3: Crystallography
Dr. Ausaf Sayeed - Objective Geology (150 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Axial Ratios & Crystallographic Axes
    if "axial ratio" in t_low or "b-axis" in t_low or "unity" in t_low or "elements" in t_low:
        return (
            r"\text{Axial Ratio Convention:} \quad a : b : c = \frac{a}{b} : 1.000 : \frac{c}{b} \quad (\alpha, \beta, \gamma)",
            "In morphological crystallography, axial ratios quantify the relative unit cell dimensions along the three reference axes. By international convention established by Christian Samuel Weiss, the intermediate lateral b-axis is arbitrarily fixed as unity (b = 1.000). The relative lengths along the front-to-back a-axis and vertical c-axis are calibrated relative to b.",
            "Klein & Dutrow (Manual of Mineral Science, 23rd Ed., pp. 115–125); F.C. Phillips (An Introduction to Crystallography)"
        )

    # 2. Miller Indices & Weiss Intercepts
    if "miller" in t_low or "weiss" in t_low or "indices" in t_low or "intercept" in t_low:
        return (
            r"(hkl) = \left( \frac{a}{r_a}, \frac{b}{r_b}, \frac{c}{r_c} \right) \xrightarrow{\text{clearing fractions}} (h, k, l) \in \mathbb{Z}",
            "Miller indices (hkl) are defined as the reciprocals of the fractional intercepts that a crystal face makes with the crystallographic reference axes, cleared of fractions and reduced to the lowest whole integers. A face parallel to an axis intersects it at infinity, yielding an index of 1/\infty = 0.",
            "W.H. Miller (1839, A Treatise on Crystallography); Donald E. Sands (Introduction to Crystallography, pp. 45–52)"
        )

    # 3. Bragg's Law & X-ray Diffraction
    if "bragg" in t_low or "x-ray" in t_low or "diffraction" in t_low or "interplanar" in t_low or "d-spacing" in t_low:
        return (
            r"n\lambda = 2d_{hkl} \sin\theta \quad \Longleftrightarrow \quad d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}} \quad (\text{Isometric})",
            "Bragg's Law governs the coherent constructive interference of monochromatic X-rays scattered from parallel lattice planes of spacing d_hkl at glancing angle theta. It provides the definitive experimental bridge between macroscopic crystal morphology and internal atomic space lattice architecture.",
            "W.L. Bragg (1913, The Diffraction of Short Electromagnetic Waves by a Crystal); Cullity (Elements of X-Ray Diffraction)"
        )

    # 4. Zone Law & Zone Axis
    if "zone" in t_low or "weiss zone" in t_low or "zone axis" in t_low:
        return (
            r"\text{Weiss Zone Law:} \quad hu + kv + lw = 0, \quad [uvw] = (k_1 l_2 - l_1 k_2,\ l_1 h_2 - h_1 l_2,\ h_1 k_2 - k_1 h_2)",
            "A crystallographic zone comprises a series of faces whose intersection edges are mutually parallel to a common spatial line termed the zone axis [uvw]. A face (hkl) belongs to zone [uvw] if and only if the linear scalar product hu + kv + lw equals zero.",
            "F.C. Phillips (An Introduction to Crystallography, pp. 48–56); Klein & Dutrow (p. 124)"
        )

    # 5. Bravais Space Lattices & Unit Cells
    if "bravais" in t_low or "lattice" in t_low or "space lattice" in t_low or "unit cell" in t_low:
        return (
            r"N_{\text{lattice}} = N_{\text{interior}} + \frac{N_{\text{face}}}{2} + \frac{N_{\text{corner}}}{8} = 14 \text{ Bravais Lattices in 7 Systems}",
            "Auguste Bravais (1848) mathematically demonstrated that infinite, periodic 3-dimensional translational lattices can assume only 14 geometrically unique arrangements: Primitive (P), Body-Centered (I), Face-Centered (F), and Base/End-Centered (C), distributed across the 7 crystal systems.",
            "Auguste Bravais (1848, Memoir on the Systems of Points); Donald E. Sands (Introduction to Crystallography, pp. 30–42)"
        )

    # 6. Rotational Symmetry Restrictions (5-fold Forbidden)
    if "5-fold" in t_low or "forbidden" in t_low or "symmetry" in t_low and ("axis" in t_low or "rotation" in t_low):
        return (
            r"\cos\alpha = \frac{m}{2} \quad (m \in \{0, \pm 1, \pm 2\}) \implies n \in \{1, 2, 3, 4, 6\} \quad [5\text{-fold and } \ge 7\text{-fold forbidden}]",
            "The crystallographic restriction theorem dictates that only 1-, 2-, 3-, 4-, and 6-fold rotational symmetries are mathematically compatible with infinite translational periodicity in 3D space lattices. A 5-fold (pentagonal) or 7-fold axis cannot tile Euclidean space without leaving gaps or overlapping.",
            "Klein & Dutrow (Manual of Mineral Science, p. 117); Donald E. Sands (p. 15)"
        )

    # 7. Hermann-Mauguin Symbols & 32 Crystal Classes
    if "hermann" in t_low or "mauguin" in t_low or "point group" in t_low or "class" in t_low and ("32" in t_low or "holohedral" in t_low):
        return (
            r"\text{Isometric Holohedral: } \frac{4}{m} \bar{3} \frac{2}{m} \quad (\text{Shorthand: } m\bar{3}m) \implies 3A_4, 4A_3, 6A_2, 9M, C",
            "Hermann-Mauguin notation precisely designates point-group symmetry operations along primary, secondary, and tertiary crystallographic directions. Across the 32 crystal classes, the holohedral classes possess the full, highest symmetry of their parent crystal system.",
            "International Tables for Crystallography (Vol. A); Klein & Dutrow (pp. 120–125)"
        )

    # 8. Twinning Laws & Intergrowths
    if "twin" in t_low or "albite" in t_low or "carisbad" in t_low or "carlsbad" in t_low or "pericline" in t_low or "staurolite" in t_low or "spinel" in t_low:
        return (
            r"\text{Twinning Operation:} \quad \mathbf{r}' = \mathbf{R}_{\pi}(\mathbf{u})\,\mathbf{r} \quad \text{or} \quad \mathbf{r}' = \mathbf{M}_{(\mathbf{n})}\,\mathbf{r} \quad [\text{Composition Plane } \parallel \mathbf{n}]",
            "Crystal twinning is a rational, symmetrical intergrowth of two or more individual crystals of the same species related by a specific crystallographic symmetry operation (rotation around a twin axis or reflection across a twin plane) that is not part of the normal point-group symmetry of the untwinned crystal.",
            "Klein & Dutrow (Manual of Mineral Science, Ch. 10, pp. 188–198); Deer, Howie & Zussman (Rock-Forming Minerals)"
        )

    # 9. Stereographic Projection & Goniometry
    if "stereographic" in t_low or "wulff" in t_low or "goniometer" in t_low or "steno" in t_low or "pole" in t_low:
        return (
            r"r = R \tan\left(\frac{\rho}{2}\right), \quad \text{Steno's Law (1669): } \angle (\mathbf{n}_1, \mathbf{n}_2) = \text{Constant}",
            "The stereographic projection projects face poles from the surface of a reference sphere onto the equatorial plane via the south pole, preserving angular conformal relationships. Nicolaus Steno (1669) established the Law of Constancy of Interfacial Angles: the angles between corresponding faces on crystals of the same mineral are constant regardless of size or irregular face development.",
            "F.C. Phillips (An Introduction to Crystallography, Ch. 2); E.E. Wahlstrom (Optical Crystallography)"
        )

    # 10. Crystal Forms: Open vs. Closed, Limiting & Polyhedra
    if "form" in t_low or "closed" in t_low or "open" in t_low or "pinacoid" in t_low or "prism" in t_low or "pyramid" in t_low or "scalenohedron" in t_low or "rhombohedron" in t_low:
        return (
            r"\text{Euler's Polyhedral Formula:} \quad F - E + V = 2 \quad [\text{Closed Forms Enclose Space Completely}]",
            "A crystal form is a group of crystal faces that are related to one another by the symmetry elements of the crystal class. Closed forms (e.g. cube, octahedron, rhombohedron) enclose space completely on their own, whereas open forms (e.g. pedion, pinacoid, prism, dome) cannot enclose space and must combine with other forms.",
            "Klein & Dutrow (Manual of Mineral Science, pp. 125–135); F.C. Phillips (pp. 50–70)"
        )

    # Default Fallback for General Crystallography
    return (
        r"\text{Fundamental Law of Rational Intercepts (Haüy, 1784):} \quad \frac{a}{h} : \frac{b}{k} : \frac{c}{l} \quad (h, k, l \in \mathbb{Z})",
        "René-Just Haüy demonstrated that the faces of crystals intersect the fundamental crystallographic axes at rational, small integer multiples of fundamental unit parameters, establishing the mathematical foundations of morphological crystallography.",
        "René-Just Haüy (1784, Essai d'une théorie sur la structure des crystaux); Klein & Dutrow (p. 116)"
    )

print("Specialized Chapter 3 Masterclass Data Module ready.")
