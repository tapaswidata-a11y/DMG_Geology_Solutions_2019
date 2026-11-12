#!/usr/bin/env python3
"""
Specialized Knowledge Bases, Formulas, and Syntheses for Chapter 5: Optical Mineralogy
Dr. Ausaf Sayeed - Objective Geology (125 Questions)
"""

def get_formula_and_mechanics(q_num, topic, q_text):
    t_low = (topic + " " + q_text).lower()

    # 1. Birefringence, Retardation & Michel-Levy Interference
    if "retardation" in t_low or "birefringence" in t_low or "michel" in t_low or "interference color" in t_low or "thickness" in t_low:
        return (
            r"\text{Optical Retardation:} \quad \Delta = d\,(n_2 - n_1) = d\,\delta, \quad I = I_0 \sin^2(2\theta)\,\sin^2\left(\frac{\pi \Delta}{\lambda}\right)",
            "When polarized light traverses an anisotropic mineral plate of thickness d with principal indices n2 and n1, the slow wave lags behind the fast wave by an optical retardation Delta = d(n2 - n1). Under crossed polarizers, vector recombination produces constructive or destructive interference colors depending on Delta, reaching maximum intensity at 45° to the polarizer crosshairs.",
            "Nesse (Introduction to Optical Mineralogy, 3rd Ed., Ch. 5); Auguste Michel-Lévy (1888)"
        )

    # 2. Polarization, Brewster's Law, Snell's Law & Refraction
    if "brewster" in t_low or "snell" in t_low or "refraction" in t_low or "wavefront" in t_low or "polariz" in t_low or "nicol" in t_low:
        return (
            r"\text{Brewster's Law: } \tan\theta_p = n \iff \theta_p + \theta_r = 90^\circ, \quad \text{Snell's Law: } n_1 \sin\theta_1 = n_2 \sin\theta_2",
            "Brewster's Law establishes that light reflected from a transparent dielectric medium is completely plane-polarized when the angle between the reflected ray and refracted ray is exactly 90°. In Nicol prisms, calcite's extraordinary birefringence (delta = 0.172) enables total internal reflection of the ordinary ray at the balsam boundary.",
            "David Brewster (1815); Jenkins & White (Fundamentals of Optics); Nesse"
        )

    # 3. Optical Indicatrix: Uniaxial & Biaxial Geometry
    if "indicatrix" in t_low or "optic axis" in t_low or "uniaxial" in t_low or "biaxial" in t_low or "positive" in t_low or "negative" in t_low:
        if "biaxial" in t_low or "2v" in t_low or "bxa" in t_low:
            return (
                r"\text{Biaxial Indicatrix: } \frac{x^2}{n_\alpha^2} + \frac{y^2}{n_\beta^2} + \frac{z^2}{n_\gamma^2} = 1, \quad \tan^2 V_z = \frac{n_\alpha^{-2} - n_\beta^{-2}}{n_\beta^{-2} - n_\gamma^{-2}} \quad [\text{Positive: } Z = \text{Bxa}]",
                "The biaxial optical indicatrix is a triaxial ellipsoid with three mutually perpendicular principal refractive indices n_alpha < n_beta < n_gamma. Two circular sections of radius n_beta define two optic axes perpendicular to them. The crystal is optically positive when the slow vibration direction Z (n_gamma) bisects the acute optic axial angle 2V.",
                "L. Fletcher (1892, The Optical Indicatrix); Bloss (Optical Crystallography, Ch. 7); Nesse"
            )
        else:
            return (
                r"\text{Uniaxial Indicatrix: } \frac{x^2 + y^2}{n_\omega^2} + \frac{z^2}{n_\epsilon^2} = 1 \quad [\text{Positive: } n_\epsilon > n_\omega \ (\text{Prolate}), \quad \text{Negative: } n_\omega > n_\epsilon \ (\text{Oblate})]",
                "The uniaxial optical indicatrix is an ellipsoid of revolution about the single optic axis (the crystallographic c-axis). Light propagating in any direction vibrates along an ordinary ray of constant refractive index n_omega and an extraordinary ray whose index varies from n_omega to n_epsilon. It is positive if prolate (n_epsilon > n_omega) and negative if oblate.",
                "Bloss (Optical Crystallography, Ch. 6); Nesse (Introduction to Optical Mineralogy)"
            )

    # 4. Conoscopic Interference Figures & Mallard's Law
    if "figure" in t_low or "conoscopic" in t_low or "isogyre" in t_low or "melatope" in t_low or "mallard" in t_low:
        return (
            r"\text{Mallard's Law: } D = K \sin E = K\,n_\beta \sin V, \quad \Delta_{\text{total}} = \Delta_{\text{mineral}} \pm 550\text{ nm}",
            "Under convergent polarized light (conoscopy), interference figures form in the back focal plane of the objective, displaying isogyres (regions where wave vibration directions parallel polarizer crosshairs) and isochromes (curves of equal retardation). Mallard's formula relates melatope separation 2D to the true optic axial angle 2V.",
            "Ernest Mallard (1882); Bloss (Optical Crystallography, pp. 140–145); Nesse"
        )

    # 5. Extinction, Twinning & Cleavage Optics
    if "extinction" in t_low or "twinning" in t_low or "albite" in t_low or "tartan" in t_low or "undulose" in t_low:
        return (
            r"\text{Extinction Angle: } \epsilon = \angle (\text{Vibration Direction}, \text{Crystallographic Axis}) \quad [\text{Orth: Straight, Mono: Inclined, Tri: Oblique}]",
            "Extinction occurs when a mineral's optical vibration directions align exactly parallel with the privileged directions of the microscope polarizers, extinguishing all light. Orthorhombic crystals display straight/symmetrical extinction, monoclinic crystals display inclined extinction on {010}, and triclinic crystals show oblique extinction in all orientations.",
            "Nesse (Introduction to Optical Mineralogy, pp. 38–40); Kerr (Optical Mineralogy)"
        )

    # 6. Becke Line, Relief & Refractometry
    if "becke" in t_low or "relief" in t_low or "refract" in t_low or "immersion" in t_low:
        return (
            r"\text{Becke Line Convergence: } \text{Tube Raised} \implies \text{Bright Halo Moves into Denser Medium } (n_{\text{high}})",
            "The Becke line is a bright halo of light concentrated along the boundary of a mineral grain submerged in an immersion medium, produced by total reflection and lens-action of the grain edge. On raising the microscope tube (or lowering the stage), the Becke line always migrates toward the medium of higher refractive index.",
            "Friedrich Becke (1893); Bloss (Optical Crystallography, pp. 54–58); Nesse"
        )

    # 7. Pleochroism, Halos & Absorption
    if "pleochro" in t_low or "halo" in t_low or "absorption" in t_low:
        return (
            r"\text{Pleochroic Absorption Formula: } I(\lambda) = I_0(\lambda)\,e^{-\alpha(\lambda)\,d} \quad [\alpha_X \ne \alpha_Y \ne \alpha_Z]",
            "Pleochroism arises from anisotropic differential absorption of specific visible wavelengths along different optical vibration directions within the crystal lattice. Pleochroic halos in biotite and cordierite represent radiogenic lattice damage produced by alpha-particle radiation from radioactive zircon or monazite inclusions.",
            "John Joly (1907); Deer, Howie & Zussman; Nesse (Optical Mineralogy)"
        )

    # Default Fallback for General Optical Mineralogy
    return (
        r"\text{Electromagnetic Wave Equation in Crystals:} \quad \mathbf{D} = \boldsymbol{\varepsilon}\,\mathbf{E} \quad \Longleftrightarrow \quad v_i = \frac{c}{n_i}",
        "In anisotropic crystalline media, the dielectric tensor epsilon produces direction-dependent permittivity, causing the phase velocity v_i of propagating light waves to vary inversely with the directional refractive index n_i.",
        "Nesse (Introduction to Optical Mineralogy, Ch. 1); Born & Wolf (Principles of Optics)"
    )

print("Specialized Chapter 5 Masterclass Data Module ready.")
