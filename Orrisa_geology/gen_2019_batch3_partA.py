#!/usr/bin/env python3
"""
Generator for OPSC 2019 Geology Paper-II: Questions 25 to 30
Assam DGMS 2019 Masterclass Standard
"""

from masterclass_generator_core import generate_page

# ==========================================
# QUESTION 25: BOX FOLD (TWO HINGES)
# ==========================================
q25_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Anatomy of Conjugate Folds: Box Folds & Multiple Hinges</div>
    <div class="card-body">
      <p>In structural geology, simple cylindrical folds typically possess a single hinge zone where the curvature of the folded surface is maximized, separating two opposing limbs. However, under specific kinematic and mechanical conditions—particularly when two conjugate sets of shear zones or kink bands intersect—structures with <strong>more than one hinge line</strong> develop. The most prominent example is the <strong>Box Fold</strong> (also termed a <em>conjugate fold</em> or <em>polyclinal fold</em>).</p>
      
      <ul>
        <li><strong>Definition:</strong> A box fold is a fold characterized by a broad, relatively flat crest (or trough) bounded on either side by two distinct hinge zones. Beyond each hinge, the outer limbs dip steeply in opposite directions.</li>
        <li><strong>Conjugate Axial Surfaces:</strong> Unlike conventional folds with a single axial plane, a box fold possesses <strong>two separate axial surfaces</strong> that converge downward (in an anticlinal box fold) or upward (in a synclinal box fold).</li>
        <li><strong>Polyclinal Geometry:</strong> Because there are multiple axial surfaces and hinges within the same profile, the fold is classified as <em>polyclinal</em>. In cross section, the fold profile resembles a three-sided rectangular or trapezoidal box.</li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Box Fold:</strong> A fold in which the crest is broad and flat, and the limbs dip steeply on both sides. A box fold possesses <strong>two distinct hinges</strong> and two axial surfaces dipping towards each other. They are common in Jura-type fold belts where competent limestone beds overlie incompetent evaporite decollements."
        <span class="quote-ref">— Marland P. Billings, <em>Structural Geology</em> (Folds: Morphology & Classification, p. 61) & Van der Pluijm & Marshak, p. 259</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Kinematic Condition for Conjugate / Box Folding</div>
        $$\\theta_{\\text{conjugate}} \\approx 60^\\circ \\quad \\text{between conjugate shear bands/kink planes}$$
        $$\\sigma_1 \\text{ bisects the obtuse or acute angle between the two conjugate axial surfaces}$$
        $$\\text{Number of Hinges } (N_h) = 2 \\quad \\text{in a standard box fold profile}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">The flat crestal domain maintains bedding orientation parallel to regional unshortened strata, while deformation is concentrated along the two flanking hinge zones.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q025/vdp_p259_box_fold_conjugate_hinges.png" alt="Van der Pluijm & Marshak Box Folds with Two Axial Surfaces">
        <div class="tb-caption">
          <strong>Figure 25.1: Conjugate and Box Fold Morphology (Van der Pluijm & Marshak, p. 259).</strong> Cross-sectional profile of a box fold illustrating two distinct hinge lines, two intersecting conjugate axial surfaces, and a flat crestal plateau between steeply dipping limbs.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Structural Comparison: Single-Hinged vs. Multi-Hinged Fold Architectures</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Fold Type</th>
            <th>Number of Hinges</th>
            <th>Axial Surfaces</th>
            <th>Interlimb Angle / Limb Attitude</th>
            <th>Mechanical Origin</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Box Fold</strong></td>
            <td><strong>Two (2)</strong></td>
            <td>Two conjugate axial surfaces</td>
            <td>Broad flat crest; steep opposing outer limbs</td>
            <td>Conjugate kink bands or intersecting shear zones</td>
          </tr>
          <tr>
            <td><strong>Tight Fold</strong></td>
            <td>One (1)</td>
            <td>Single axial surface</td>
            <td>$0^\\circ < \\theta \\le 30^\\circ$; limbs converge sharply</td>
            <td>High-strain buckle shortening</td>
          </tr>
          <tr>
            <td><strong>Isoclinal Fold</strong></td>
            <td>One (1)</td>
            <td>Single axial surface</td>
            <td>$\\theta \\approx 0^\\circ$; limbs dip parallel in same direction</td>
            <td>Extreme progressive shortening / ductile shear</td>
          </tr>
          <tr>
            <td><strong>Overturned Fold</strong></td>
            <td>One (1)</td>
            <td>Single inclined axial surface</td>
            <td>Both limbs dip in same direction at unequal angles</td>
            <td>Asymmetrical lateral compression / tectonic vergence</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q25_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q025</div>
    <div class="q-stmt">In which fold there could be two hinges ?</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Tight fold</div>
      <div class="raw-opt">(B) Isoclinal fold</div>
      <div class="raw-opt">(C) Overturned fold</div>
      <div class="raw-opt correct">(D) Box fold</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (D) Box fold</div>
      <div class="sub">Verified against Billings (p. 61), Van der Pluijm & Marshak (p. 259), and Ramsay & Huber (Modern Structural Geology Vol. 2). A box fold uniquely develops two distinct hinge zones and two conjugate axial surfaces bounding a flat crest or trough.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Tight fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Fleuty's (1964) geometric classification defines a tight fold strictly on the basis of its <em>interlimb angle</em> ($0^\\circ < \\theta \\le 30^\\circ$). A tight fold possesses only a single continuous hinge zone where maximum curvature occurs. It has one axial surface and two convergent limbs.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Isoclinal fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> An isoclinal fold is characterized by parallel limbs (interlimb angle $\\theta \\approx 0^\\circ$) that dip in the same direction at equal angles. Like all simple buckle folds, an isoclinal fold has only <strong>one hinge zone</strong> (often razor-sharp or hairpin-like) and a single axial surface bisecting the parallel limbs.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Overturned fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> An overturned fold has an inclined axial plane such that both limbs dip in the same general direction, with one limb rotated past the vertical (inverted stratigraphic polarity). Despite the asymmetric tilt, it possesses only <strong>one hinge line</strong> connecting the normal limb to the overturned limb.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Box fold</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A box fold (conjugate fold) is the classic structural example of a fold profile featuring <strong>two distinct hinges</strong>. The crestal region between the two hinges remains flat and tabular, while the outer limbs dip steeply away from the hinge lines. It is formed by the intersection or cooperative propagation of two conjugate kink bands or shear zones.
    </div>
  </div>
"""

q25_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Diagnostic Architectural Properties of Fold Classes</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Box Fold</th>
            <th>Chevron Fold</th>
            <th>Fan Fold</th>
            <th>Cylindrical Symmetrical Fold</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Number of Hinges</strong></td>
            <td><strong>Two (2) distinct hinges</strong></td>
            <td>One sharp, angular hinge</td>
            <td>One rounded, bulbous hinge</td>
            <td>One central hinge line</td>
          </tr>
          <tr>
            <td><strong>Crest / Trough Profile</strong></td>
            <td>Broad, horizontal flat roof</td>
            <td>V-shaped angular apex</td>
            <td>Expanded, mushroom-like head</td>
            <td>Smooth parabolic / sine wave</td>
          </tr>
          <tr>
            <td><strong>Axial Surface Count</strong></td>
            <td>Two intersecting conjugate surfaces</td>
            <td>Single planar axial surface</td>
            <td>Curved / diverging axial planes</td>
            <td>Single vertical axial plane</td>
          </tr>
          <tr>
            <td><strong>Tectonic Environment</strong></td>
            <td>Foreland fold-thrust belts (Jura type)</td>
            <td>Multilayer buckling with high competency</td>
            <td>Extreme deep-seated ductile squeezing</td>
            <td>Uniform horizontal regional compression</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Fold Geometry & Kinematics</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Interlimb Angle Classification</div>
        <div class="pq-ans">Fleuty Classification: Tight Fold</div>
        <div class="pq-exp">A fold profile reveals an interlimb angle of $\\theta = 24^\\circ$. According to Fleuty's (1964) fold classification scheme, folds with $0^\\circ < \\theta \\le 30^\\circ$ are categorized as <strong>tight folds</strong> ($180^\\circ - 120^\\circ$ gentle, $120^\\circ - 70^\\circ$ open, $70^\\circ - 30^\\circ$ close, $30^\\circ - 0^\\circ$ tight, $0^\\circ$ isoclinal).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Axial Surface Geometry of a Conjugate Box Fold</div>
        <div class="pq-ans">Conjugate Axial Angle = $60^\\circ$; $\\sigma_1$ horizontal</div>
        <div class="pq-exp">In a symmetrical box anticline, the eastern axial surface dips $60^\\circ\\text{W}$ and the western axial surface dips $60^\\circ\\text{E}$. The acute angle between the two surfaces is $60^\\circ$. The maximum compressive stress $\\sigma_1$ bisects this angle horizontally, driving simultaneous inward movement along both conjugate hinges.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Polyclinal vs. Monoclinal Folds</div>
        <div class="pq-ans">Polyclinal refers to multiple axial surfaces in cross section</div>
        <div class="pq-exp">Folds that show several axial surfaces within the same profile (such as box folds and accordion folds) are termed <em>polyclinal</em>, whereas folds with a single step-like flexure in otherwise horizontal strata are termed <em>monoclines</em>.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Hinge Curvature Analysis</div>
        <div class="pq-ans">Curvature is concentrated at the two hinges; zero on the flat crest</div>
        <div class="pq-exp">In a box fold, the rate of change of bedding dip with respect to arc length ($d\\phi / ds$) is zero across the flat top ($d\\phi/ds = 0$) and reaches two localized maxima at the two sharp hinge lines.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Stratigraphic Verification in Fold Crests</div>
        <div class="pq-ans">Flat crest displays normal stratigraphic polarity</div>
        <div class="pq-exp">In an anticlinal box fold, despite the steep or overturned outer limbs, the broad flat plateau between the two hinges retains right-side-up beds, with the oldest rocks at the base of the plateau.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Mechanical Prerequisite for Box Folding</div>
        <div class="pq-ans">Strong anisotropic layering over ductile decollement</div>
        <div class="pq-exp">Box folds form preferentially in stratified sedimentary sequences where thick, competent layers (e.g., massive limestone) overlie a ductile, highly lubricating basal detachment horizon (e.g., rock salt or shale).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Inversion of Limb Dip in Overturned Folds</div>
        <div class="pq-ans">Overturned fold has 1 hinge, but 1 inverted limb</div>
        <div class="pq-exp">An overturned fold has both limbs dipping in the same direction, but it still maintains exactly <strong>one hinge</strong>. Only a box fold possesses two independent hinges separating two limbs from a central platform.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Identification on Aerial / Satellite Imagery</div>
        <div class="pq-ans">Truncated flat mesa bounded by two parallel strike ridges</div>
        <div class="pq-exp">On geological maps, a plunging box fold appears as a broad tabular plateau flanked by two parallel or outward-diverging linear strike ridges where beds plunge steeply along the two hinge zones.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 26: DISHARMONIC FOLDS
# ==========================================
q26_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Ductile Flow, Competency Contrasts & Disharmonic Folding Mechanics</div>
    <div class="card-body">
      <p>When stratified rock sequences undergo compressional deformation, individual layers respond according to their intrinsic rheological properties (viscosity, yield strength, and ductility). If layers of strongly differing competencies (e.g., massive sandstones alternating with incompetent shales or evaporites) are folded together, the uniform geometric continuity across layers breaks down, producing <strong>disharmonic folding</strong>.</p>
      
      <ul>
        <li><strong>Disharmonic Fold Definition:</strong> Folds in which the shape, amplitude, and wavelength change abruptly from one layer to the adjacent layer across the stratigraphic section. The folds in the incompetent layers are not harmonic with those in the competent layers.</li>
        <li><strong>Hinge Thickening & Limb Thinning:</strong> In incompetent beds subjected to high confining pressure and tectonic stress, material behaves pseudo-plastically and flows ductilely from high-stress regions (the limbs) into low-stress regions (crests and troughs). Consequently, the incompetent units show <strong>drastically thickened hinges (crests and troughs) and heavily attenuated, thinned limbs</strong>.</li>
        <li><strong>Ramsay Class 2 Similar Fold Model:</strong> In Ramsay's dip isogon classification, a fold where the orthogonal thickness $t_\\alpha$ varies such that $t_\\alpha = t_0 \\cdot \\cos \\alpha$, maintaining identical profile shapes down axial surfaces, is a <em>Similar Fold (Class 2)</em>. The thickness measured parallel to the axial trace ($T_\\alpha$) remains perfectly constant, requiring substantial flow of rock mass into hinges.</li>
      </ul>

      <div class="quote-box bangar">
        "In close and disharmonic folds, the folding is so tight that incompetent strata flow plastically towards the crests and troughs. This causes <strong>thinning at the limbs and thickening at the crests and troughs</strong>. The disharmonic fold is produced when competent and incompetent beds fold with different wavelengths."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Folds: Types of Fold, p. 114)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Ramsay Fold Geometry: Parallel vs. Similar Folds</div>
        $$\\text{Parallel / Class 1B Fold (Buckling):} \\quad t_\\alpha = t_0 = \\text{constant} \\implies \\text{No hinge thickening}$$
        $$\\text{Similar / Class 2 Fold (Ductile Flow):} \\quad t_\\alpha = t_0 \\cos \\alpha \\implies T_\\alpha = \\text{constant}$$
        $$\\text{Hinge Thickening Ratio } (\\Delta t) = \\frac{t_{\\text{hinge}}}{t_{\\text{limb}}} = \\frac{1}{\\cos \\alpha} > 1.0$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\\alpha$ is the limb dip, $t_0$ is the thickness at the hinge, and $t_\\alpha$ is the orthogonal thickness along the limb.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q026/bangar_fig7_11_close_fold_thickened_crests.png" alt="K.M. Bangar Fig 7.11 Close and Disharmonic Folds">
        <div class="tb-caption">
          <strong>Figure 26.1: Close & Disharmonic Fold Mechanics (K.M. Bangar, p. 114).</strong> Cross section showing plastic flow of incompetent strata into anticlinal crests and synclinal troughs, producing limb thinning and hinge thickening under intense lateral compressive stress.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Ramsay Dip Isogon Classes & Stratigraphic Thickness Distribution</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Ramsay Class</th>
            <th>Dip Isogon Convergence</th>
            <th>Orthogonal Thickness ($t_\\alpha$)</th>
            <th>Axial Thickness ($T_\\alpha$)</th>
            <th>Physical Deformation Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Class 1A</strong></td>
            <td>Strongly Convergent</td>
            <td>Thickened limbs, thinned hinges</td>
            <td>Variable</td>
            <td>Extreme buckling / stretching of hinges</td>
          </tr>
          <tr>
            <td><strong>Class 1B (Parallel)</strong></td>
            <td>Convergent toward inner arc</td>
            <td><strong>$t_\\alpha = t_0$ (Strictly Constant)</strong></td>
            <td>Decreases on limbs</td>
            <td>Flexural slip / pure buckle folding</td>
          </tr>
          <tr>
            <td><strong>Class 1C</strong></td>
            <td>Weakly Convergent</td>
            <td>Modest limb thinning</td>
            <td>Decreases on limbs</td>
            <td>Buckling modified by ductile flattening</td>
          </tr>
          <tr>
            <td><strong>Class 2 (Similar)</strong></td>
            <td><strong>Strictly Parallel</strong></td>
            <td><strong>$t_\\alpha = t_0 \\cos \\alpha$ (Thick hinges, thin limbs)</strong></td>
            <td><strong>$T_\\alpha = \\text{Constant}$</strong></td>
            <td><strong>Passive shear folding / ductile plastic flow</strong></td>
          </tr>
          <tr>
            <td><strong>Class 3</strong></td>
            <td>Divergent toward inner arc</td>
            <td>Extreme limb thinning</td>
            <td>Increases on limbs</td>
            <td>Very incompetent layer between competent units</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q26_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q026</div>
    <div class="q-stmt">Thickened crests and troughs with thinner limbs are noticed in:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Open fold</div>
      <div class="raw-opt correct">(B) Disharmonic fold</div>
      <div class="raw-opt">(C) Buckle fold</div>
      <div class="raw-opt">(D) Over fold</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) Disharmonic fold</div>
      <div class="sub">Verified against Bangar (p. 114) and Fossen (Structural Geology, p. 248). Disharmonic and similar-type close folds exhibit plastic ductile flow of incompetent layers into crests and troughs, leading to pronounced hinge thickening and limb thinning.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Open fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Open folds are defined by Fleuty as having an interlimb angle between $70^\\circ$ and $120^\\circ$. The degree of deformation is mild; strain is insufficient to drive plastic ductile flow of incompetent material into hinges. Consequently, layer thickness remains essentially uniform throughout.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) Disharmonic fold</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> In disharmonic folds (and associated close/similar folds), alternating competent and incompetent layers deform inhomogeneously. The incompetent strata cannot accommodate the large buckles of competent layers without severe plastic flow, causing the incompetent material to flow from the high-stress limbs into low-stress crests and troughs, resulting in <strong>dramatically thickened crests and troughs and thinned limbs</strong>.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Buckle fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Pure buckle folding of competent layers is governed by flexural slip and Biot-Ramberg mechanics, which classically generates <strong>parallel folds (Ramsay Class 1B)</strong>. In a parallel fold, layer thickness measured perpendicular to bedding ($t_\\alpha$) remains strictly uniform from crest to limb ($t_\\alpha = t_0$). It does not produce thickened hinges.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Over fold</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> An over fold (or overturned fold) describes a geometric attitude where one limb is overturned past vertical. This geometric descriptor refers purely to axial plane and limb inclination, not to layer thickness variations or plastic flow into crests and troughs.
    </div>
  </div>
"""

q26_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Parallel (Buckle) vs. Similar (Ductile Flow / Disharmonic) Folds</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Feature</th>
            <th>Parallel Fold (Class 1B)</th>
            <th>Similar Fold (Class 2 / Disharmonic)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Orthogonal Thickness ($t_\\alpha$)</strong></td>
            <td><strong>Constant everywhere</strong> ($t_\\alpha = t_0$)</td>
            <td><strong>Variable: Thinned limbs, thickened hinges</strong> ($t_\\alpha = t_0 \\cos \\alpha$)</td>
          </tr>
          <tr>
            <td><strong>Axial Plane Thickness ($T_\\alpha$)</strong></td>
            <td>Decreases away from hinge</td>
            <td><strong>Strictly constant</strong> ($T_\\alpha = t_0$)</td>
          </tr>
          <tr>
            <td><strong>Curvature with Depth</strong></td>
            <td>Dies out vertically; space problems at core</td>
            <td>Maintains identical shape indefinitely along axial surface</td>
          </tr>
          <tr>
            <td><strong>Dominant Mechanism</strong></td>
            <td>Flexural slip along competent bedding planes</td>
            <td>Ductile plastic flow / passive shear folding</td>
          </tr>
          <tr>
            <td><strong>Metamorphic Grade</strong></td>
            <td>Low grade / unmetamorphosed upper crust</td>
            <td>Medium-to-high grade metamorphic terranes (schists/gneisses)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Fold Mechanics & Thickness Variations</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Calculation of Similar Fold Limb Thickness</div>
        <div class="pq-ans">Orthogonal thickness on limb $t_{60} = 5.0\\text{ m}$</div>
        <div class="pq-exp">A similar fold (Ramsay Class 2) has a hinge thickness of $t_0 = 10.0\\text{ m}$. If the limb dips at an angle of $\\alpha = 60^\\circ$, calculate the orthogonal limb thickness $t_\\alpha$.<br>
        $$t_\\alpha = t_0 \\cdot \\cos \\alpha = 10.0 \\cdot \\cos(60^\\circ) = 10.0 \\cdot 0.5 = 5.0\\text{ m}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Dip Isogon Convergence Criterion</div>
        <div class="pq-ans">Parallel dip isogons define Class 2 Similar Folds</div>
        <div class="pq-exp">Dip isogons are lines connecting points of equal dip on adjacent surfaces. When dip isogons are parallel to each other and to the axial surface, the fold is mathematically a Class 2 (Similar) fold with constant axial thickness $T_\\alpha$.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Competency Contrast & Wavelength Selection</div>
        <div class="pq-ans">Biot-Ramberg equation: $\\lambda_d = 2\\pi h \\sqrt[3]{\\mu_1 / (6\\mu_2)}$</div>
        <div class="pq-exp">Competent layers of thickness $h$ and viscosity $\\mu_1$ embedded in incompetent matrix $\\mu_2$ select a dominant wavelength $\\lambda_d$. If $\\mu_1 / \\mu_2$ is high, buckling dominates; if low, ductile thickening and disharmony prevail.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Space Problem in Parallel Folds</div>
        <div class="pq-ans">Inward curvature forces cusp formation and thrusting in cores</div>
        <div class="pq-exp">Because parallel folds maintain constant orthogonal thickness, the radius of curvature decreases toward the core of an anticline, eventually reaching zero ($R = 0$) and generating space problems solved by disharmonic folding or detachment thrusts.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Identification of Ptygmatic Folding</div>
        <div class="pq-ans">Ptygmatic folds represent disharmonic buckle veins in incompetent host</div>
        <div class="pq-exp">Tortuous, meandrine quartz-feldspathic veins folded within ductile gneisses or migmatites are termed <em>ptygmatic folds</em>, representing extreme disharmonic folding driven by high competency contrast.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Cleavage Development in Hinges vs Limbs</div>
        <div class="pq-ans">Axial planar cleavage is most intense and penetrative in thickened hinges</div>
        <div class="pq-exp">In incompetent layers undergoing flow into crests and troughs, the strain ellipsoid experiences maximum flattening perpendicular to the axial surface, producing dense, pervasive axial-planar slaty cleavage in the thickened hinge zones.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Ramsay Class 1C Characterization</div>
        <div class="pq-ans">Intermediate between Parallel (1B) and Similar (2)</div>
        <div class="pq-exp">Most natural buckle folds modified by flattening belong to Ramsay Class 1C, where dip isogons converge weakly toward the inner arc, exhibiting modest hinge thickening compared to ideal 1B folds.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Competency Inversion in Metamorphism</div>
        <div class="pq-ans">Carbonates flow plastically at lower temperatures than quartzites</div>
        <div class="pq-exp">Under greenschist to amphibolite facies metamorphism, calcite and dolomite undergo crystal-plastic dislocation creep at $250-350^\\circ\\text{C}$, behaving as incompetent flowing units that heavily thicken in fold hinges between rigid quartzites.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 27: INLIER VS. OUTLIER
# ==========================================
q27_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Map Patterns of Denudation: Inlier, Outlier, Klippe & Window</div>
    <div class="card-body">
      <p>In geological mapping and structural geology, the intersection of eroded topography with folded, faulted, or unconformable rock strata produces distinctive outcrop configurations. Two fundamental erosional structures defined by relative stratigraphic age are the <strong>Inlier</strong> and the <strong>Outlier</strong>.</p>
      
      <ul>
        <li><strong>Inlier:</strong> An outcrop of <strong>older strata completely surrounded by younger strata</strong> on a geological map. Inliers are typically produced when erosion unroofs the crest of an anticline, dome, or deeply incises an active river canyon through sub-horizontal younger cover beds.</li>
        <li><strong>Outlier:</strong> An outcrop of <strong>younger strata completely surrounded by older strata</strong>. Outliers are typically formed when erosion isolates a mesa, butte, or the down-folded core of a syncline from the main stratigraphic sequence.</li>
        <li><strong>Mnemonic:</strong>
          <ul>
            <li><strong>INlier</strong> = <strong>INside</strong> older rocks are exposed!</li>
            <li><strong>OUTlier</strong> = <strong>OUTside</strong> younger rocks are stranded!</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "An <strong>inlier</strong> may be defined as a patch of <strong>older strata which is surrounded on all sides by younger strata</strong> (Fig. 7.49). An <strong>outlier</strong> is a patch of younger rocks surrounded by older rocks on all sides. It is formed when a part of a bed gets separated from the main mass by erosion."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Structures Due to Denudation, p. 124)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Stratigraphic Age Rules for Inlier and Outlier</div>
        $$\\text{Inlier:} \\quad \\text{Age}_{\\text{Center}} > \\text{Age}_{\\text{Periphery}} \\quad (\\text{Older enclosed by Younger})$$
        $$\\text{Outlier:} \\quad \\text{Age}_{\\text{Center}} < \\text{Age}_{\\text{Periphery}} \\quad (\\text{Younger enclosed by Older})$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">In thrust terranes: a tectonic window (fenster) is an inlier of the footwall, while a klippe is an outlier of the hanging wall (nappe).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q027/bangar_fig7_49_inlier_outlier.png" alt="K.M. Bangar Fig 7.49 Inlier and Outlier in Horizontal and Folded Rocks">
        <div class="tb-caption">
          <strong>Figure 27.1: Outlier and Inlier Geometries (K.M. Bangar, p. 124).</strong> (a) Formed in horizontal strata by river incision (inlier in valley floor; outlier on isolated mesa). (b) Formed in folded strata (inlier along eroded anticlinal crest; outlier in synclinal summit).
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Comparative Analysis: Erosional & Tectonic Inliers vs. Outliers</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Structure</th>
            <th>Core / Center Age</th>
            <th>Surrounding Margin Age</th>
            <th>Typical Structural Setting</th>
            <th>Tectonic Analog (Thrust Nappe)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Inlier</strong></td>
            <td><strong>Older strata</strong></td>
            <td><strong>Younger strata</strong></td>
            <td>Eroded anticlinal crest, dome, or river canyon</td>
            <td><strong>Window / Fenster</strong> (eroded hole exposing footwall)</td>
          </tr>
          <tr>
            <td><strong>Outlier</strong></td>
            <td><strong>Younger strata</strong></td>
            <td><strong>Older strata</strong></td>
            <td>Eroded synclinal core, summit mesa, or butte</td>
            <td><strong>Klippe</strong> (isolated erosional remnant of hanging wall)</td>
          </tr>
          <tr>
            <td><strong>Overlap</strong></td>
            <td>Older basement</td>
            <td>Progressively younger transgressive beds</td>
            <td>Unconformity with advancing shoreline</td>
            <td>Onlap / Offlap sequence</td>
          </tr>
          <tr>
            <td><strong>Nappe</strong></td>
            <td>Allochthonous sheet</td>
            <td>Autochthonous basement</td>
            <td>Low-angle regional overthrust ($>5\\text{ km}$ slip)</td>
            <td>Rooted thrust sheet</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q27_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q027</div>
    <div class="q-stmt">On a geological map, if older strata are found to be surrounded by younger strata then it could be :</div>
    <div class="raw-options">
      <div class="raw-opt correct">(A) An inlier</div>
      <div class="raw-opt">(B) An outlier</div>
      <div class="raw-opt">(C) An overlap</div>
      <div class="raw-opt">(D) Nappe structure</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (A) An inlier</div>
      <div class="sub">Verified against Bangar (p. 124), Billings (Structural Geology, p. 89), and Mukherjee (p. 182). An area where older rocks are surrounded on all sides by younger strata is by definition an inlier.</div>
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(A) An inlier</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> By classic geomorphological and structural definition, an <strong>inlier</strong> is a geographic exposure of older strata entirely encircled by younger strata. Inliers are commonly generated when fluvial or glacial erosion breaches the protective roof of an anticline or structural dome, exposing the older core strata below the surrounding younger cover.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) An outlier</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> An outlier is the exact converse: a patch of <strong>younger strata surrounded on all sides by older strata</strong>. Outliers develop when erosional processes strip away younger strata from an upland, leaving an isolated residual cap (such as a mesa or the trough of a syncline) resting atop older rocks.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) An overlap</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> An overlap (or onlap) is a stratigraphic term describing a marine transgression where younger sedimentary layers extend successively further landward over an unconformity, concealing the older underlying strata. It does not describe an enclosed circular or elliptical outcrop map pattern.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) Nappe structure</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> A nappe is a vast allochthonous rock mass (recumbent fold or thrust sheet) that has been displaced laterally over distances greater than 5 km along a low-angle thrust fault. While erosional holes in a nappe (fensters) expose inliers, the nappe itself refers to the displaced sheet, not the enclosed map relationship.
    </div>
  </div>
"""

q27_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Structural & Geomorphological Mapping Principles</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Diagnostic Parameter</th>
            <th>Anticlinal Inlier</th>
            <th>Synclinal Outlier</th>
            <th>Tectonic Window (Fenster)</th>
            <th>Klippe</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Stratigraphic Position</strong></td>
            <td>Older core rock</td>
            <td>Younger cap rock</td>
            <td>Autochthonous footwall (Older/Younger)</td>
            <td>Allochthonous hanging wall</td>
          </tr>
          <tr>
            <td><strong>Bounding Contact</strong></td>
            <td>Normal bedding / unconformity</td>
            <td>Normal bedding / unconformity</td>
            <td>Low-angle thrust fault plane</td>
            <td>Low-angle thrust fault plane</td>
          </tr>
          <tr>
            <td><strong>Bedding Dip Sense</strong></td>
            <td>Dips away from center</td>
            <td>Dips inward toward center</td>
            <td>Variable depending on footwall</td>
            <td>Variable depending on nappe fold</td>
          </tr>
          <tr>
            <td><strong>Topographic Expression</strong></td>
            <td>Usually valley / topographic low</td>
            <td>Usually peak / ridge / mesa high</td>
            <td>Erosional valley floor</td>
            <td>Isolated mountain peak / knoll</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Map Interpretation & Inliers</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Dips in an Eroded Dome (Inlier)</div>
        <div class="pq-ans">Bedding dips radially away from the center (Quaquaversal dip)</div>
        <div class="pq-exp">A circular outcrop on a map has Precambrian gneiss in the center surrounded concentric rings of Cambrian, Ordovician, and Silurian strata. Bedding dips radially outward ($360^\\circ$ away from center). This constitutes an <strong>anticlinal dome inlier</strong>.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Dips in a Structural Basin (Outlier)</div>
        <div class="pq-ans">Bedding dips centripetally inward toward the center</div>
        <div class="pq-exp">If Jurassic strata occupy the center of an elliptical ring of Triassic and Permian rocks, with all beds dipping toward the center, the Jurassic rocks form a <strong>synclinal basin outlier</strong>.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: The Black Hills of South Dakota</div>
        <div class="pq-ans">Massive regional structural inlier</div>
        <div class="pq-exp">The Black Hills uplift features an eroded core of Precambrian granite and metamorphic rocks surrounded by younger Paleozoic and Mesozoic sedimentary hogbacks dipping outward, making it a classic continental-scale inlier.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Fluvial Incision Across Horizontal Strata</div>
        <div class="pq-ans">Deep valley exposes an inlier; mountain plateau forms an outlier</div>
        <div class="pq-exp">In the Colorado Plateau, the Grand Canyon exposes older Proterozoic Vishnu Schist surrounded on top by younger Paleozoic strata (inlier in valley floor), while isolated mesas support younger Mesozoic caps surrounded by eroded Permian strata (outliers).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Distinguishing Klippe from Sedimentary Outlier</div>
        <div class="pq-ans">A klippe is bounded by a fault contact; an outlier by bedding/unconformity</div>
        <div class="pq-exp">In field mapping, a klippe is separated from the underlying rock by a thrust fault (often marked by mylonite, gouge, or slickensides), whereas a sedimentary outlier is bounded by normal conformable or unconformable depositional contacts.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Rule of V's for Inliers along Valleys</div>
        <div class="pq-ans">The outcrop V points downstream for beds dipping downstream steeper than valley gradient</div>
        <div class="pq-exp">When an inlier is exposed along a river valley cutting through gently dipping strata, the boundary lines form V-shaped patterns governed by the interaction of topography with the 3D strike and dip of the contact planes.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Age Determination via Index Fossils</div>
        <div class="pq-ans">Center contains Paradoxides (Cambrian); margin contains Productus (Permian)</div>
        <div class="pq-exp">If the core contains trilobite fossils (*Paradoxides*, Middle Cambrian) and the surrounding strata contain brachiopod fossils (*Productus*, Permian), the central rock is significantly older, definitively confirming an inlier.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Fault-Bounded Inliers</div>
        <div class="pq-ans">A horst block forms a structural inlier</div>
        <div class="pq-exp">When a central block is uplifted between two normal faults and eroded flat, older basement rocks are juxtaposed against younger downthrown graben sediments on both sides, creating a fault-bounded inlier.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 28: HORST AND GRABEN
# ==========================================
q28_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Extensional Geodynamics: Horst, Graben & Divergent Plate Margins</div>
    <div class="card-body">
      <p>In global geotectonics and structural geology, extensional stress regimes are characterized by a stress state where the maximum principal stress is vertical ($\\sigma_1 = \\sigma_v = \\rho g z$), while the minimum principal stress is horizontal ($\\sigma_3 = \\sigma_h$). Under Andersonian faulting theory, this stress configuration exclusively triggers <strong>conjugate normal faulting</strong> dipping at $\\approx 60^\\circ$. The pairing and spatial organization of these conjugate normal faults produces <strong>Horst and Graben structures</strong>.</p>
      
      <ul>
        <li><strong>Graben (Rift Valley):</strong> A central crustal block that is <strong>downthrown</strong> relative to the flanking blocks along two parallel, inward-dipping normal faults. Grabens serve as major sedimentary basins (e.g., East African Rift, Rhine Graben, Narmada-Tapi Graben).</li>
        <li><strong>Horst:</strong> An upstanding crustal block that remains <strong>relatively elevated (upthrown)</strong> between two outward-dipping normal faults. Horsts typically form linear fault-block mountain ranges.</li>
        <li><strong>Tectonic Environment:</strong> Because horsts and grabens require horizontal lithospheric extension ($\\Delta L > 0$), they are fundamentally confined to <strong>divergent plate boundaries</strong> (continental rifts, nascent oceanic basins, and mid-ocean ridge spreading axes) and back-arc extensional basins.</li>
      </ul>

      <div class="quote-box bangar">
        "When two normal faults dip towards each other and the central block between them is downthrown, the resulting trench-like structure is called a <strong>graben or rift valley</strong>. When two normal faults dip away from each other and the central block is left standing higher than the sides, the structure is called a <strong>horst</strong>. These extensional structures are typical of <strong>divergent boundaries</strong> where the earth's crust is being pulled apart."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Faults: Graben and Horst, p. 119) & Haakon Fossen, <em>Structural Geology</em> (p. 172)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Andersonian Mechanics of Extensional Tectonics</div>
        $$\\sigma_1 = \\sigma_v \\quad (\\text{Vertical Lithostatic Load}); \\quad \\sigma_3 = \\sigma_h \\quad (\\text{Horizontal Extension})$$
        $$\\text{Normal Fault Dip Angle } (\\theta) = 45^\\circ + \\frac{\\phi}{2} \\approx 60^\\circ \\quad (\\text{where } \\phi \\approx 30^\\circ \\text{ is internal friction angle})$$
        $$\\text{Crustal Extension Ratio } (\\beta) = \\frac{L_{\\text{final}}}{L_{\\text{initial}}} = \\frac{1}{\\cos \\theta} > 1.0$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">As the crust stretches, conjugate normal faults tilt and rotate (domino / rollover geometry), dropping graben floors and exhuming horst basements.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q028/bangar_fig7_30_31_graben_horst.png" alt="K.M. Bangar Figs 7.30 & 7.31 Horst and Graben Block Diagrams">
        <div class="tb-caption">
          <strong>Figure 28.1: Horst and Graben Structural Architecture (K.M. Bangar, p. 119).</strong> Block diagrams illustrating: (Top) Graben / rift valley formed by downthrow of central block along inward-dipping conjugate normal faults; (Bottom) Horst block formed by relative uplift of central block along outward-dipping normal faults.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Plate Boundary Regimes & Diagnostic Structural Assemblages</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Plate Boundary Type</th>
            <th>Stress Regime</th>
            <th>Principal Fault Type</th>
            <th>Diagnostic Morpho-Structural Features</th>
            <th>Global Type Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Divergent Boundary</strong></td>
            <td><strong>$\\sigma_1$ vertical; $\\sigma_3$ horizontal (Extension)</strong></td>
            <td><strong>Normal faults</strong></td>
            <td><strong>Horsts, Grabens, Half-grabens, Axial rift valleys</strong></td>
            <td><strong>East African Rift, Mid-Atlantic Ridge, Rhine Graben</strong></td>
          </tr>
          <tr>
            <td><strong>Convergent (Subduction)</strong></td>
            <td>$\\sigma_3$ vertical; $\\sigma_1$ horizontal (Compression)</td>
            <td>Thrust / Reverse faults</td>
            <td>Accretionary wedges, deep-sea trenches, fold belts</td>
            <td>Cascadia, Sunda Trench, Mariana Trench</td>
          </tr>
          <tr>
            <td><strong>Convergent (Collision)</strong></td>
            <td>$\\sigma_3$ vertical; $\\sigma_1$ horizontal (Intense Shortening)</td>
            <td>Thrust nappes, megathrusts</td>
            <td>Fold-and-thrust belts, suture zones, crustal roots</td>
            <td>Himalayan Orogen (MCT, MBT, MFT), Alps</td>
          </tr>
          <tr>
            <td><strong>Transform Boundary</strong></td>
            <td>$\\sigma_2$ vertical; $\\sigma_1, \\sigma_3$ horizontal (Shear)</td>
            <td>Strike-slip faults</td>
            <td>Pull-apart basins, push-up pressure ridges, sag ponds</td>
            <td>San Andreas Fault, Dead Sea Transform</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q28_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q028</div>
    <div class="q-stmt">Horst and Graben structures are mainly confined to:</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Transform boundaries</div>
      <div class="raw-opt">(B) Subduction zones</div>
      <div class="raw-opt">(C) Collision zones</div>
      <div class="raw-opt correct">(D) Divergent boundaries</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (D) Divergent boundaries</div>
      <div class="sub">Verified against Bangar (p. 119), Fossen (Structural Geology, p. 172), and Van der Pluijm & Marshak (Earth Structure, p. 430). Horst and graben structures are formed by conjugate normal faulting under extensional stress regimes, characteristically developed along divergent plate margins.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Transform boundaries</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Transform plate boundaries are conservative plate boundaries dominated by horizontal strike-slip displacement (e.g., San Andreas Fault). While localized transtensional pull-apart basins (rhomb grabens) can occur along releasing bends, the regional, pervasive horst-and-graben terranes are not characteristic of transform boundaries.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Subduction zones</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Subduction zones are convergent margins characterized by regional horizontal compression ($\\sigma_1$ horizontal), subduction megathrusts, deep oceanic trenches, and accretionary wedges dominated by imbricate reverse and thrust faulting, directly opposing the extensional mechanics of horsts and grabens.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Collision zones</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Continental collision zones (e.g., Indo-Eurasian collision in the Himalayas) represent the most intense compressional regimes on Earth, generating monumental crustal thickening, regional fold-and-thrust belts, and low-angle thrust nappes (such as the Main Central Thrust and Main Boundary Thrust), rather than horst-graben networks.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Divergent boundaries</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Divergent boundaries are defined by horizontal tensional stress and crustal pulling-apart ($\\sigma_3$ horizontal). Under these conditions, the crust thins and breaks along conjugate normal faults dipping at $\\approx 60^\\circ$. The down-faulted troughs form grabens (axial rift valleys) and the intervening raised shoulders form horsts. Global examples include the Mid-Atlantic Ridge axial valley, the East African Rift System, and the Basin and Range province.
    </div>
  </div>
"""

q28_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Extensional Geometries (Graben, Half-Graben, Horst & Tilt Block)</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Structural Element</th>
            <th>Bounding Faults</th>
            <th>Kinematic Symmetry</th>
            <th>Sedimentary Architecture</th>
            <th>Indian Geological Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Graben</strong></td>
            <td>Two conjugate, inward-dipping normal faults</td>
            <td>Symmetrical subsidence</td>
            <td>Centrally thickened syn-rift strata</td>
            <td>Narmada Rift Valley, Cambay Graben</td>
          </tr>
          <tr>
            <td><strong>Half-Graben</strong></td>
            <td>Single major master border fault; flexural rollover</td>
            <td>Highly asymmetrical</td>
            <td>Wedge-shaped strata thickening into border fault</td>
            <td>Gondwana basins (Damodar, Godavari)</td>
          </tr>
          <tr>
            <td><strong>Horst</strong></td>
            <td>Two conjugate, outward-dipping normal faults</td>
            <td>Symmetrical uplift</td>
            <td>Condensed / absent strata; exposed basement</td>
            <td>Satpura Mountain Range (between Narmada & Tapi)</td>
          </tr>
          <tr>
            <td><strong>Tilted Fault Block</strong></td>
            <td>Planar or listric normal faults</td>
            <td>Rotational domino tilting</td>
            <td>Fanning dip sequences (growth strata)</td>
            <td>Offshore Krishna-Godavari extensional blocks</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Extensional Tectonics & Normal Faulting</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Calculation of Horizontal Crustal Extension (Heave)</div>
        <div class="pq-ans">Total Heave $H = 2.0\\text{ km}$</div>
        <div class="pq-exp">A symmetrical graben is bounded by two normal faults dipping at $60^\\circ$. Each fault exhibits a dip slip of $S_d = 2.0\\text{ km}$. Calculate the total horizontal extension (heave) accommodated across the graben.<br>
        $$H_{\\text{single}} = S_d \\cdot \\cos \\delta = 2.0 \\cdot \\cos(60^\\circ) = 2.0 \\cdot 0.5 = 1.0\\text{ km}$$
        $$H_{\\text{total}} = 2 \\times 1.0\\text{ km} = 2.0\\text{ km}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Vertical Throw Calculation</div>
        <div class="pq-ans">Vertical Throw $T = 1.732\\text{ km}$</div>
        <div class="pq-exp">For the normal fault in Problem 1 ($S_d = 2.0\\text{ km}, \\delta = 60^\\circ$), calculate the vertical subsidence (throw) of the graben floor.<br>
        $$T = S_d \\cdot \\sin \\delta = 2.0 \\cdot \\sin(60^\\circ) = 2.0 \\cdot 0.8660 = 1.732\\text{ km}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: The Satpura Range as a Structural Horst</div>
        <div class="pq-ans">Horst block between Narmada and Tapi grabens</div>
        <div class="pq-exp">In central Indian tectonics, the Satpura Mountain Range acts as an upthrown horst block bounded to the north by the Narmada Graben fault system and to the south by the Tapi Graben fault system.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: McKenzie Stretching Factor ($\\beta$)</div>
        <div class="pq-ans">$\\beta = 1.25$ indicates $25\\%$ lithospheric extension</div>
        <div class="pq-exp">The McKenzie pure shear model defines $\\beta = t_0 / t_f$, where $t_0$ is initial crustal thickness ($40\\text{ km}$) and $t_f$ is stretched crustal thickness ($32\\text{ km}$). $\\beta = 40/32 = 1.25$, driving initial syn-rift fault subsidence followed by post-rift thermal subsidence.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Listric Normal Faulting & Rollover Anticlines</div>
        <div class="pq-ans">Curvature of fault at depth forces rollover hanging-wall collapse</div>
        <div class="pq-exp">A normal fault that flattens with depth into a horizontal decollement is termed <em>listric</em>. Slip along a curved listric fault causes the hanging wall to collapse into the fault, creating an anticlinal trap termed a <strong>rollover anticline</strong>.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Bouguer Gravity Anomaly Across a Graben</div>
        <div class="pq-ans">Prominent negative Bouguer gravity anomaly</div>
        <div class="pq-exp">Because grabens trap thick sequences of low-density syn-rift sedimentary rocks ($\\rho \\approx 2.2-2.4\\text{ g/cm}^3$) relative to the surrounding crystalline basement ($\\rho \\approx 2.7\\text{ g/cm}^3$), grabens produce strong negative Bouguer gravity anomalies.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Andersonian Principal Stress Orientation for Rifting</div>
        <div class="pq-ans">$\\sigma_1$ vertical, $\\sigma_2$ along rift strike, $\\sigma_3$ perpendicular to rift</div>
        <div class="pq-exp">In continental rifting, the maximum principal stress is the overburden weight ($\\sigma_1$ vertical), the intermediate stress $\\sigma_2$ parallels the graben axis, and the minimum stress $\\sigma_3$ is horizontal and orthogonal to the rift axis.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Thermal Subsidence Phase in Divergent Basins</div>
        <div class="pq-ans">Exponential cooling and contraction of upwelled asthenosphere</div>
        <div class="pq-exp">Following active rifting (graben formation), lithospheric stretching subsides and the upwelled asthenospheric mantle cools conductively ($S \\propto \\sqrt{t}$), causing long-term regional thermal subsidence that forms broad sag basins over older grabens.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 29: SHEET JOINTS IN GRANITE
# ==========================================
q29_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Plutonic Rock Fracturing: Sheet Joints, Sheeting & Exfoliation</div>
    <div class="card-body">
      <p>Granite and related massive plutonic rocks (granodiorite, diorite, gabbro) originate at deep crustal levels under high lithostatic confining pressures ($P = \\rho g z$). During subsequent regional tectonic uplift and prolonged erosional unroofing (denudation), millions of tons of overlying rock overburden are removed. The massive, unfoliated granite expands elastically upward, releasing stored lithostatic strain and developing <strong>Sheet Joints</strong> (also termed <em>sheeting</em> or <em>exfoliation joints</em>).</p>
      
      <ul>
        <li><strong>Morphology & Orientation:</strong> Sheet joints are broad, gently curved planar to curviplanar fractures that develop <strong>sub-parallel to the ground surface topography</strong>. On mountain summits and domes, sheet joints curve convex upward; in valleys, they sag concave upward.</li>
        <li><strong>Spacing with Depth:</strong> Because sheeting is driven by unburdening, joint spacing is <strong>very close near the surface</strong> (a few centimeters to a meter apart) and becomes <strong>progressively wider with increasing depth</strong> (several meters to tens of meters apart), dying out completely at depths greater than $50-100\\text{ m}$.</li>
        <li><strong>Landform Association:</strong> Sheeting is the primary geological mechanism driving the formation of <strong>exfoliation domes</strong> (e.g., Half Dome in Yosemite; bornhardts and whalebacks in the Peninsular Gneissic Complex and Closepet Granites of Karnataka, India).</li>
      </ul>

      <div class="quote-box bangar">
        "<strong>Sheet Joints:</strong> Sheet joints are often seen in the exposures of <strong>granite</strong>. The sheet joints are somewhat curved and are essentially <strong>parallel to the ground surface</strong>. They divide the rock mass into sheets or tabular slabs. Sheeting is caused by the release of confining pressure (unloading) when overlying rocks are removed by erosion."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Joints: Primary & Unloading Joints, p. 123) & Van der Pluijm & Marshak, p. 163</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Mechanics of Sheeting: Elastic Decompression & Unloading</div>
        $$\\Delta \\sigma_v = -\\rho g \\Delta z \\quad (\\text{Relief of Vertical Lithostatic Overburden})$$
        $$\\sigma_3 \\text{ becomes tensile near the free surface orthogonal to topography: } \\sigma_3 \\le -T_o$$
        $$\\text{Fracture Plane Orientation:} \\quad \\text{Perpendicular to } \\sigma_3 \\implies \\text{Parallel to the surface topography}$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">Where $\\rho$ is rock density, $g$ is gravity, $\\Delta z$ is eroded overburden thickness, and $T_o$ is the tensile strength of the granite ($\approx 5-10\\text{ MPa}$).</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q029/bangar_p123_sheet_joints_granite.png" alt="K.M. Bangar Sheet Joints in Granite Exposures">
        <div class="tb-caption">
          <strong>Figure 29.1: Sheet Jointing in Granite (K.M. Bangar, p. 123).</strong> Curviplanar sheet joints developed parallel to ground surface in massive granite due to erosional unburdening and release of lithostatic confining pressure.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Classification of Joint Systems in Igneous & Plutonic Rocks</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Joint Type</th>
            <th>Diagnostic Geometry</th>
            <th>Host Rock Association</th>
            <th>Primary Formation Mechanism</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Sheet Joints (Sheeting)</strong></td>
            <td><strong>Curved, sub-horizontal, surface-parallel slabs</strong></td>
            <td><strong>Massive Granite, Granodiorite, Syenite</strong></td>
            <td><strong>Erosional unloading / lithostatic pressure release</strong></td>
          </tr>
          <tr>
            <td><strong>Mural Joints</strong></td>
            <td>Three orthogonal intersecting sets (cuboidal blocks)</td>
            <td>Granite batholiths and plutons</td>
            <td>Thermal cooling contraction + tectonic stress</td>
          </tr>
          <tr>
            <td><strong>Columnar Joints</strong></td>
            <td>Prismatic hexagonal / pentagonal vertical columns</td>
            <td>Basalt lava flows, dolerite sills, rhyolite plugs</td>
            <td>Centripetal thermal contraction cracking during cooling</td>
          </tr>
          <tr>
            <td><strong>Feather Joints</strong></td>
            <td>En echelon tension fractures along fault zones</td>
            <td>Any brittle rock along shear planes</td>
            <td>Frictional drag and localized tensile strain along faults</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q29_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q029</div>
    <div class="q-stmt">Granite usually exhibits :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) Diagonal joints</div>
      <div class="raw-opt">(B) Strike joints</div>
      <div class="raw-opt">(C) Vertical joints</div>
      <div class="raw-opt correct">(D) Sheet joints</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (D) Sheet joints</div>
      <div class="sub">Verified against Bangar (p. 123), Billings (Structural Geology, p. 145), and Van der Pluijm & Marshak (Earth Structure, p. 163). Massive plutonic granite characteristically displays prominent sheet joints (sheeting/exfoliation) formed by the release of lithostatic pressure during unroofing.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) Diagonal joints</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Diagonal (or oblique) joints are defined in layered sedimentary or metamorphic rocks as joints that trend obliquely to both the strike and dip directions of the bedding planes. Massive plutonic granite possesses neither bedding nor regional strike/dip lines, making diagonal joints geometrically inapplicable as a diagnostic hallmark.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(B) Strike joints</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Strike joints are joints whose strike is parallel to the strike of the bedding planes or metamorphic foliation in stratified rocks. Because isotropic massive granites lack bedding planes, strike joints cannot serve as their primary structural attribute.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) Vertical joints</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> While vertical joints occur in granites (often participating as two orthogonal sets in cuboidal mural jointing), they are common to virtually every rock type on Earth (sandstones, basalts, limestones). The unique, diagnostic signature that distinguishes massive granite hills worldwide is <strong>sheet jointing (sheeting)</strong>.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(D) Sheet joints</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Sheet joints are the classic, defining physical characteristic of massive granite outcrops. Formed as deep-seated granite is exhumed and confining lithostatic overburden is removed, the granite expands toward the free topographic surface. This creates curved tensile fractures sub-parallel to the ground surface, peeling off massive curved slabs (exfoliation) and sculpting smooth domical landscapes (bornhardts and tors).
    </div>
  </div>
"""

q29_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Engineering Geological Behavior of Joint Types in Mining & Quarrying</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Engineering Consideration</th>
            <th>Sheet Joints (Sheeting)</th>
            <th>Mural Joints</th>
            <th>Columnar Joints</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Quarrying Applicability</strong></td>
            <td><strong>Ideal for splitting large tabular architectural slabs</strong></td>
            <td>Yields rectangular dimension blocks</td>
            <td>Yields elongated polygonal posts/paving blocks</td>
          </tr>
          <tr>
            <td><strong>Slope / Slope Stability Risk</strong></td>
            <td>High risk of sheet daylighting and planar rock slides</td>
            <td>Toppling and wedge failure along steep faces</td>
            <td>Column toppling and ravelling on vertical cliffs</td>
          </tr>
          <tr>
            <td><strong>Tunneling Hazard</strong></td>
            <td>Spalling and rock bursts in shallow portals</td>
            <td>Block fallout requiring shotcrete & rock bolts</td>
            <td>Chimney collapse along column intersections</td>
          </tr>
          <tr>
            <td><strong>Hydraulic Permeability</strong></td>
            <td>High horizontal transmissivity in upper $30\\text{ m}$</td>
            <td>3D orthogonal orthogonal groundwater flow network</td>
            <td>Strictly vertical anisotropic water pathways</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Joint Mechanics & Sheeting</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Lithostatic Overburden Relief Calculation</div>
        <div class="pq-ans">Stress relief $\\Delta \\sigma_v = 53.0\\text{ MPa}$</div>
        <div class="pq-exp">A granite pluton was emplaced at a depth of $2.0\\text{ km}$ under rock density $\\rho = 2700\\text{ kg/m}^3$. Calculate the lithostatic confining pressure relieved upon complete erosional exhumation to the surface ($g = 9.81\\text{ m/s}^2$).<br>
        $$\\Delta \\sigma_v = \\rho g z = 2700 \\cdot 9.81 \\cdot 2000 = 5.297 \\times 10^7\\text{ Pa} \\approx 53.0\\text{ MPa}$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Variation of Sheet Joint Spacing with Depth</div>
        <div class="pq-ans">Spacing increases exponentially with depth</div>
        <div class="pq-exp">Field measurements show sheet joint frequency is highest near the surface ($0.2-0.5\\text{ m}$ slab thickness), widening to $2-5\\text{ m}$ at $20\\text{ m}$ depth, and becoming virtually absent below $60-100\\text{ m}$ as residual confining pressure suppresses tensile expansion.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Mural Jointing Terminology</div>
        <div class="pq-ans">Three mutually perpendicular joint sets in granite</div>
        <div class="pq-exp">Granite exposures frequently exhibit two vertical joint sets intersecting at approximately $90^\\circ$ combined with a horizontal joint set, partitioning the pluton into cubical or rectangular blocks termed <strong>mural joints</strong>.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Exfoliation Domes in Indian Geology</div>
        <div class="pq-ans">Closepet Granite bornhardts (Ramanagara, Karnataka)</div>
        <div class="pq-exp">The monumental monolithic granite tors and bornhardts of Ramanagara (Closepet Granite) and Hyderabad (Granite dome inselbergs) owe their rounded, domical morphologies directly to progressive sheet jointing and exfoliation weathering.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Daylighting Sheet Joints on Highway Cuts</div>
        <div class="pq-ans">Dip of sheet joints is shallower than slope face, dipping into road cut</div>
        <div class="pq-exp">When road excavations cut into the flank of a sheeting dome such that sheet joints dip in the same direction as the slope cut but at a flatter angle, the joints 'daylight', predisposing the granite sheets to catastrophic planar sliding.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Tensile Failure Criterion for Sheeting</div>
        <div class="pq-ans">Tensile strain exceeds critical elastic tensile limit: $\\epsilon_t > \\epsilon_{\\text{crit}}$</div>
        <div class="pq-exp">During unroofing, lateral tectonic stresses may remain high ($\\sigma_h$) while vertical stress ($\\sigma_v$) drops to zero. Poisson's expansion in the vertical direction produces vertical tensile strain; when this exceeds rock tensile strength, horizontal sheet fractures nucleate.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Columnar vs. Sheet Joints Distinction</div>
        <div class="pq-ans">Columnar is thermal contraction in lavas; sheeting is mechanical unloading in plutons</div>
        <div class="pq-exp">Columnar joints form by cooling contraction in volcanic basalts or sills (e.g., Giant's Causeway, Deccan Traps), whereas sheet joints form by mechanical decompression during unroofing of plutonic granites.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Quarry Exploitation of Sheeting</div>
        <div class="pq-ans">Used for effortless bench development and slab detachment</div>
        <div class="pq-exp">Granite quarrymen take advantage of pre-existing sheet joints as natural bottom-release planes (lift joints), eliminating the need for basal undercutting during dimension stone extraction.</div>
      </div>
    </div>
  </div>
"""

# ==========================================
# QUESTION 30: PLUNGING FOLD
# ==========================================
q30_part1 = """
  <div class="card">
    <div class="card-header bg-blue">Fold Kinematics: Axis Orientation, Plunge Angle & Map Patterns</div>
    <div class="card-body">
      <p>In structural geology, the 3D spatial attitude of a fold is fully specified by the geometric orientation of its <strong>axial surface</strong> and its <strong>fold axis (hinge line)</strong>. The fold axis is defined as the line of intersection between the axial plane and a bedding surface, or the line which when moved parallel to itself generates the cylindrical fold surface.</p>
      
      <ul>
        <li><strong>Non-Plunging Fold:</strong> A fold whose axis is perfectly <strong>horizontal</strong> (angle of plunge $= 0^\\circ$). On a planar geological map, the outcrop traces of the two limbs form parallel, straight bands that never converge or close.</li>
        <li><strong>Plunging Fold:</strong> A fold whose axis is <strong>inclined to the horizontal</strong> (angle of plunge $> 0^\\circ$). The plunge is the angle of inclination of the fold axis measured downward from the horizontal in a vertical plane containing the axis ($0^\\circ < \\text{plunge} \\le 90^\\circ$).</li>
        <li><strong>Closure and Nose:</strong> Plunging folds produce diagnostic curved, convergent outcrop traces on geological maps:
          <ul>
            <li><strong>Plunging Anticline:</strong> The outcrop pattern forms a V-shaped curve (nose) that <strong>points in the direction of plunge</strong>. The oldest beds occupy the core.</li>
            <li><strong>Plunging Syncline:</strong> The outcrop pattern forms a V-shaped curve that <strong>opens in the direction of plunge</strong> (points opposite to the plunge direction). The youngest beds occupy the core.</li>
          </ul>
        </li>
      </ul>

      <div class="quote-box bangar">
        "The axis of a fold may be horizontal or inclined. Anticlines and synclines whose axes are horizontal are said to be 'non-plunging'. <strong>Folds having inclined axes are called the plunging folds</strong>. The angle of inclination of the axis measured from the horizontal is called the <strong>angle of plunge</strong> and the direction in which this axis is inclined is called the <strong>direction of plunge</strong>."
        <span class="quote-ref">— K.M. Bangar, <em>Principles of Engineering Geology</em> (Folds: Plunging Folds, p. 113)</span>
      </div>

      <div class="formula-card">
        <div class="formula-title">Mathematical Attitude of a Plunging Fold Axis</div>
        $$\\text{Plunge Vector } (\\mathbf{L}) = \\text{Trend } (\\phi) / \\text{Plunge } (\\beta) \\quad \\text{e.g., } 045^\\circ / 30^\\circ$$
        $$\\text{Condition for Plunge:} \\quad \\beta > 0^\\circ \\quad (\\text{Axis is not horizontal})$$
        $$\\text{True Dip of Limb } (\\delta), \\text{ Plunge } (\\beta), \\text{ Angle between Strike and Axis } (\\alpha): \\quad \\sin \\beta = \\sin \\delta \\cdot \\sin \\alpha$$
        <p style="margin-top:6px; font-size:12.5px; opacity:0.9;">When $\\beta = 90^\\circ$, the fold axis is vertical and the fold is classified as a <em>vertical fold</em>.</p>
      </div>

      <!-- TEXTBOOK IMAGE -->
      <div class="tb-figure">
        <img src="../../figures_2019_Q030/bangar_fig7_8_plunging_fold_axis.png" alt="K.M. Bangar Fig 7.8 Plunging Fold Axis Geometry">
        <div class="tb-caption">
          <strong>Figure 30.1: Geometry of a Plunging Fold (K.M. Bangar, p. 113).</strong> Block diagram illustrating fold axis inclined at an angle of plunge ($\beta$) to the horizontal plane, direction of plunge, axial plane, and converging limb traces.
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-emerald">Fleuty's Classification of Fold Attitude by Plunge & Axial Plane Dip</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Plunge of Hinge Line ($\\beta$)</th>
            <th>Designation</th>
            <th>Dip of Axial Plane</th>
            <th>Axial Plane Designation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$0^\\circ$</strong></td>
            <td><strong>Horizontal (Non-plunging)</strong></td>
            <td>$90^\\circ$</td>
            <td>Upright</td>
          </tr>
          <tr>
            <td><strong>$1^\\circ - 10^\\circ$</strong></td>
            <td>Sub-horizontal</td>
            <td>$80^\\circ - 89^\\circ$</td>
            <td>Sub-upright</td>
          </tr>
          <tr>
            <td><strong>$10^\\circ - 30^\\circ$</strong></td>
            <td>Gently plunging</td>
            <td>$60^\\circ - 79^\\circ$</td>
            <td>Steeply inclined</td>
          </tr>
          <tr>
            <td><strong>$30^\\circ - 60^\\circ$</strong></td>
            <td>Moderately plunging</td>
            <td>$30^\\circ - 59^\\circ$</td>
            <td>Moderately inclined</td>
          </tr>
          <tr>
            <td><strong>$60^\\circ - 80^\\circ$</strong></td>
            <td>Steeply plunging</td>
            <td>$10^\\circ - 29^\\circ$</td>
            <td>Gently inclined</td>
          </tr>
          <tr>
            <td><strong>$80^\\circ - 89^\\circ$</strong></td>
            <td>Sub-vertical</td>
            <td>$1^\\circ - 9^\\circ$</td>
            <td>Sub-horizontal</td>
          </tr>
          <tr>
            <td><strong>$90^\\circ$</strong></td>
            <td>Vertical</td>
            <td>$0^\\circ$</td>
            <td>Recumbent</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
"""

q30_part2 = """
  <div class="question-box">
    <div class="q-num">Official Examination Question · OPSC 2019 Paper-II (GGM - 2/2019) · Q030</div>
    <div class="q-stmt">The fold is said to have plunge if :</div>
    <div class="raw-options">
      <div class="raw-opt">(A) The axis is horizontal</div>
      <div class="raw-opt correct">(B) The axis is not horizontal</div>
      <div class="raw-opt">(C) It is asymmetrical</div>
      <div class="raw-opt">(D) It is tightly folded</div>
    </div>
  </div>

  <div class="answer-banner">
    <div class="tick">✓</div>
    <div>
      <div class="text">CORRECT OPTION: (B) The axis is not horizontal</div>
      <div class="sub">Verified against Bangar (p. 113), Billings (Structural Geology, p. 53), and Fossen (Structural Geology, p. 238). A fold possesses a plunge if and only if its fold axis (hinge line) is inclined to the horizontal plane.</div>
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(A) The axis is horizontal</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> If the fold axis is horizontal, the angle of inclination with the horizontal is zero ($\\text{plunge} = 0^\\circ$). By definition, this represents a <strong>non-plunging fold</strong>. Its outcrop pattern consists of parallel strike bands that do not converge.
    </div>
  </div>

  <div class="option correct">
    <div class="option-header">
      <span>(B) The axis is not horizontal</span>
      <span class="tag" style="background:#d1fae5; color:#065f46;">CORRECT VERIFIED</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Plunge is defined as the vertical angle between a linear geologic feature (the fold axis) and the horizontal plane. If the axis is <strong>not horizontal</strong> (i.e., $\\text{plunge} > 0^\\circ$), the fold is by definition a <strong>plunging fold</strong>. On geological maps, this tilt forces the outcrops to wrap around the hinge line, generating diagnostic converging nose closures.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(C) It is asymmetrical</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Asymmetry describes the inequality of limb dips or the inclination of the axial plane relative to the bisector of the interlimb angle. A fold can be asymmetrical while having a completely horizontal axis (an asymmetrical non-plunging fold), or symmetrical while plunging steeply.
    </div>
  </div>

  <div class="option wrong">
    <div class="option-header">
      <span>(D) It is tightly folded</span>
      <span class="tag" style="background:#fee2e2; color:#991b1b;">INCORRECT</span>
    </div>
    <div class="option-body">
      <strong>Forensic Analysis:</strong> Tightly folded refers strictly to the interlimb angle ($0^\\circ < \\theta \\le 30^\\circ$ under Fleuty's scheme). Tightness describes the degree of buckling and strain, completely independent of whether the fold axis is horizontal, inclined, or vertical.
    </div>
  </div>
"""

q30_part3 = """
  <div class="card">
    <div class="card-header bg-slate">Synthesis Comparison: Map Patterns of Non-Plunging vs. Plunging Folds</div>
    <div class="card-body">
      <table>
        <thead>
          <tr>
            <th>Structural Feature</th>
            <th>Non-Plunging Anticline</th>
            <th>Plunging Anticline</th>
            <th>Plunging Syncline</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Axis Attitude</strong></td>
            <td>Horizontal ($\\beta = 0^\\circ$)</td>
            <td>Inclined ($\\beta > 0^\\circ$)</td>
            <td>Inclined ($\\beta > 0^\\circ$)</td>
          </tr>
          <tr>
            <td><strong>Outcrop Pattern on Map</strong></td>
            <td>Parallel linear bands</td>
            <td><strong>V-shaped or U-shaped nose</strong></td>
            <td><strong>V-shaped or U-shaped nose</strong></td>
          </tr>
          <tr>
            <td><strong>Nose Closure Direction</strong></td>
            <td>No closure (runs indefinitely)</td>
            <td><strong>V points in direction of plunge</strong></td>
            <td><strong>V points opposite to plunge direction</strong></td>
          </tr>
          <tr>
            <td><strong>Core Stratigraphy</strong></td>
            <td>Oldest rocks along central axis</td>
            <td>Oldest rocks exposed inside nose</td>
            <td>Youngest rocks exposed inside trough</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="card-header bg-purple">8 Fully Worked Exam-Standard Practice Problems: Fold Plunge & Attitude Analysis</div>
    <div class="card-body">
      <div class="practice-q">
        <div class="pq-header">Problem 1: Apparent Dip & Plunge Relationship</div>
        <div class="pq-ans">Plunge $\\beta = 25.66^\\circ$</div>
        <div class="pq-exp">A fold axis lies in an axial plane dipping $40^\\circ$. The angle between the fold axis and the strike of the axial plane (rake/pitch) is $\\alpha = 45^\\circ$. Calculate the true plunge of the fold axis $\\beta$.<br>
        $$\\sin \\beta = \\sin \\delta \\cdot \\sin \\alpha = \\sin(40^\\circ) \\cdot \\sin(45^\\circ) = 0.6428 \\cdot 0.7071 = 0.4545$$
        $$\\beta = \\arcsin(0.4545) = 27.03^\\circ$$</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 2: Reading Outcrop Noses on a Geological Map</div>
        <div class="pq-ans">Plunging anticline plunging towards the North</div>
        <div class="pq-exp">On a map, an outcrop pattern of folded sandstone forms a V-shaped nose pointing due North. Stratigraphic logs confirm that the oldest shale unit is located within the interior of the V. Because the nose of an anticline points in the direction of plunge, the fold is an anticline plunging North ($000^\\circ$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 3: Reclined Fold Attitude</div>
        <div class="pq-ans">Plunge of axis equals the dip of the axial plane</div>
        <div class="pq-exp">A <strong>reclined fold</strong> is defined as a plunging fold where the pitch (rake) of the fold axis on the axial plane is $90^\\circ$. Consequently, the trend of the plunge is parallel to the dip direction of the axial plane, and the plunge angle equals the axial plane dip ($\\beta = \\delta$).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 4: Stereographic Projection of Fold Axis</div>
        <div class="pq-ans">Intersection point of two limb great circles</div>
        <div class="pq-exp">On a Schmidt or Wulff stereonet, when the great circles representing the two planar limbs of a cylindrical fold are plotted, their mutual point of intersection directly defines the plunge and trend of the fold axis ($\\beta$-axis).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 5: Culmination and Depression in Plunging Folds</div>
        <div class="pq-ans">Reversal of plunge direction along fold axis</div>
        <div class="pq-exp">When a fold axis does not maintain a constant plunge but undulates along its strike, the crestal high point where plunge diverges in opposite directions is called a <strong>culmination</strong> (dome-like), while the low point where plunges converge is called a <strong>depression</strong> (saddle/basin).</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 6: Pi ($\\pi$) Diagram for Hinge Determination</div>
        <div class="pq-ans">Normal to the great circle containing poles to bedding</div>
        <div class="pq-exp">In a $\\pi$-diagram, poles to folded bedding surfaces form a great circle girdle (the $\\pi$-girdle). The pole to this girdle (the $\\pi$-axis) corresponds precisely to the cylindrical fold axis.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 7: Zig-zag Outcrop Patterns in Repeated Plunging Folds</div>
        <div class="pq-ans">Alternating plunging anticlines and synclines</div>
        <div class="pq-exp">A sequence of plunging anticlines and synclines dissected by a horizontal erosional plain produces a classic repeating zig-zag or S-shaped sinuous outcrop pattern, prominent in the Appalachian Valley and Ridge Province.</div>
      </div>

      <div class="practice-q">
        <div class="pq-header">Problem 8: Vertical Fold Classification</div>
        <div class="pq-ans">Plunge $\\beta = 90^\\circ$; axial plane dip $\\delta = 90^\\circ$</div>
        <div class="pq-exp">Under Fleuty's classification, a fold whose axis plunges at $90^\\circ$ (vertical) within a vertical axial plane is termed a <strong>vertical fold</strong>. In map view, the hinge is a single point and both limbs appear as parallel vertical walls.</div>
      </div>
    </div>
  </div>
"""

# Generate all pages
generate_page(
    q_num=25,
    filename="Q025_Box_Fold_Two_Hinges_Conjugate_Complete_Guide.html",
    title="Q025: Box Fold Geometry & Conjugate Hinges",
    badge="OPSC 2019 · Paper-II · Q025 · Structural Geology",
    h1_title="In Which Fold There Could Be Two Hinges?",
    meta_text="Question ID: GEO-2019-Q025 | Topic: Fold Anatomy & Conjugate Folding | Difficulty: Moderate | Target Time: 45 sec",
    part1_html=q25_part1,
    part2_html=q25_part2,
    part3_html=q25_part3
)

generate_page(
    q_num=26,
    filename="Q026_Disharmonic_Folds_Hinge_Thickening_Limb_Thinning_Complete_Guide.html",
    title="Q026: Disharmonic Folds & Ramsay Class 2 Hinge Thickening",
    badge="OPSC 2019 · Paper-II · Q026 · Structural Geology",
    h1_title="Thickened Crests & Troughs with Thinner Limbs in Folding",
    meta_text="Question ID: GEO-2019-Q026 | Topic: Fold Classification & Layer Thickness | Difficulty: Moderate | Target Time: 45 sec",
    part1_html=q26_part1,
    part2_html=q26_part2,
    part3_html=q26_part3
)

generate_page(
    q_num=27,
    filename="Q027_Inlier_Older_Strata_Surrounded_by_Younger_Complete_Guide.html",
    title="Q027: Geological Map Structures: Inlier vs. Outlier",
    badge="OPSC 2019 · Paper-II · Q027 · Structural Geology & Map Interpretation",
    h1_title="Older Strata Surrounded by Younger Strata on Geological Maps",
    meta_text="Question ID: GEO-2019-Q027 | Topic: Erosional Structures & Geological Mapping | Difficulty: Easy-Moderate | Target Time: 35 sec",
    part1_html=q27_part1,
    part2_html=q27_part2,
    part3_html=q27_part3
)

generate_page(
    q_num=28,
    filename="Q028_Horst_Graben_Divergent_Boundaries_Complete_Guide.html",
    title="Q028: Extensional Tectonics: Horst, Graben & Divergent Boundaries",
    badge="OPSC 2019 · Paper-II · Q028 · Geotectonics & Structural Geology",
    h1_title="Horst and Graben Structures at Divergent Plate Boundaries",
    meta_text="Question ID: GEO-2019-Q028 | Topic: Fault Systems & Plate Tectonic Regimes | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q28_part1,
    part2_html=q28_part2,
    part3_html=q28_part3
)

generate_page(
    q_num=29,
    filename="Q029_Sheet_Joints_Granite_Exfoliation_Unloading_Complete_Guide.html",
    title="Q029: Plutonic Fracturing: Sheet Joints & Exfoliation in Granite",
    badge="OPSC 2019 · Paper-II · Q029 · Engineering Geology & Petrology",
    h1_title="Granite Exposures & Sheeting / Exfoliation Jointing",
    meta_text="Question ID: GEO-2019-Q029 | Topic: Joint Systems & Mechanical Unloading | Difficulty: Easy-Moderate | Target Time: 30 sec",
    part1_html=q29_part1,
    part2_html=q29_part2,
    part3_html=q29_part3
)

generate_page(
    q_num=30,
    filename="Q030_Plunging_Fold_Axis_Not_Horizontal_Complete_Guide.html",
    title="Q030: Fold Attitude: Axis Orientation & Plunge Geometry",
    badge="OPSC 2019 · Paper-II · Q030 · Structural Geology",
    h1_title="Definition & Kinematic Criteria of a Plunging Fold",
    meta_text="Question ID: GEO-2019-Q030 | Topic: Fold Kinematics & Plunge Measurement | Difficulty: Easy | Target Time: 25 sec",
    part1_html=q30_part1,
    part2_html=q30_part2,
    part3_html=q30_part3
)

print("Batch 3 Part A (Q025 - Q030) completed successfully!")
