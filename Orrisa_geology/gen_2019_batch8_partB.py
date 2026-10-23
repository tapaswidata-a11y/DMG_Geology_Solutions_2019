#!/usr/bin/env python3
"""
Generate Masterclass Solutions for OPSC Geology 2019 Paper-II: Batch 8 Part B (Q099 - Q105)
Sedimentary Petrology: Soft-Sediment Deformation, Granulometric Skewness, Basin Tectonics, and Carbonates.
"""

from masterclass_generator_core import generate_page

# -----------------------------------------------------------------------------
# Q099: Syn-sedimentary Deformation - High Sedimentation
# -----------------------------------------------------------------------------
def gen_q099():
    q_num = 99
    filename = "Q099_Syn_Sedimentary_Deformation_Structures_Result_Of_High_Sedimentation_Complete_Guide.html"
    title = "Q099: Sedimentary Structures - Syn-Sedimentary Deformation & Sedimentation Rate"
    badge = "OPSC 2019 Geology Paper-II • Question 99 • Sedimentary Petrology"
    h1_title = "Soft-Sediment Deformation: Rapid Sedimentation, Liquefaction, and Hydrodynamic Instability"
    meta_text = "<strong>Topic:</strong> Soft-Sediment Deformation Structures • <strong>Key Concept:</strong> High Sedimentation Rate & Density Inversion • <strong>Textbooks:</strong> J.D. Collinson et al. (2006); Sam Boggs Jr. (2014); K.M. Bangar"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Physics of Syn-Sedimentary Deformation</div>
      <p><strong>Syn-sedimentary deformation structures</strong> (also known as <em>soft-sediment deformation structures</em> or SSDS) develop during or immediately following deposition, while sediments remain unlithified, unconsolidated, and water-saturated. Their fundamental trigger is an abnormally <strong>high rate of sedimentation</strong> (rapid sediment dumping):</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Deformation Structure</th>
              <th>Morphology & Geometry</th>
              <th>Physical Trigger Mechanism</th>
              <th>Sedimentary Environment</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Flame Structures</strong></td>
              <td>Tongue-like or flame-shaped plumes of mud injected upward into overlying sand.</td>
              <td><strong>High sedimentation rate</strong> causes reverse density gradient; dense sand sinks into soupy, water-rich mud.</td>
              <td>Turbidites, delta fronts, flood channels.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Ball-and-Pillow Structures</strong></td>
              <td>Hemispherical or kidney-shaped pillows of sand detached and sunk into mud substratum.</td>
              <td>Rapid dumping of sand creates Rayleigh-Taylor instability; sand lobes break off and founder.</td>
              <td>Prograding delta slopes, storm beds, turbidites.</td>
            </tr>
            <tr>
              <td>Convolute Bedding</td>
              <td>Intricately folded, crumpled, or crumpled laminae bounded by undisturbed flat beds.</td>
              <td>Pore-water overpressuring and horizontal shear during rapid sediment dewatering.</td>
              <td>Turbidite $T_c$ division, braided flood plains.</td>
            </tr>
            <tr>
              <td>Dish & Pillar Structures</td>
              <td>Concave-upward dark dishes separated by vertical escape columns (pillars).</td>
              <td>Fluidized upward escape of trapped pore water during rapid compaction of thick sands.</td>
              <td>Submarine fan channels, liquefied mass-flow sands.</td>
            </tr>
            <tr>
              <td>Slump Folds & Breccias</td>
              <td>Contorted, recumbent folds and sheared slide blocks along a basal glide plane.</td>
              <td>Gravitational slope failure on depositional slopes oversteepened by high sedimentation.</td>
              <td>Continental slopes, prodelta slopes, submarine canyon walls.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Syn-sedimentary or soft-sediment deformation structures are primarily a direct consequence of <strong>high rates of sedimentation</strong>. When sediments are dumped rapidly from turbulent suspensions (as in deltas, submarine fans, or catastrophic floods), interstitial water cannot escape in time. The resulting undercompacted, soupy muds develop high pore-fluid pressures, and when loaded rapidly by overlying denser sand, undergo liquefaction, fluidization, and spontaneous deformation."
        <div class="quote-author">&mdash; Sam Boggs Jr., <em>Principles of Sedimentology and Stratigraphy</em> (5th Ed., Pearson, pp. 98&ndash;101)</div>
      </div>

      <div class="formula-box">
        $$\text{Excess Pore Fluid Pressure: } u = \rho_{\text{sediment}} g z - \sigma' \quad (\text{As sedimentation rate } \dot{s} \uparrow \implies \text{Pore pressure } u \rightarrow \sigma_{\text{lithostatic}})$$
        $$\text{Effective Shear Strength: } \tau = c + (\sigma - u) \tan \phi \rightarrow 0 \implies \mathbf{Liquefaction\ and\ Spontaneous\ Deformation}$$
        $$\mathbf{High\ Sedimentation\ Rate\ (Option\ D)} \implies \text{Soft-Sediment Deformation Structures (SSDS)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q099/syn_sedimentary_deformation_convolute_flame_structures.png" alt="Syn-Sedimentary Deformation Structures Flame Structures" class="figure-img">
        <div class="figure-caption">Figure 99: Soft-sediment deformation structures (flame structures and ball-and-pillow) triggered by rapid sedimentation loading dense sand onto undercompacted water-saturated mud.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 99</div>
        <div class="raw-q-text">Syn-sedimentary deformation structures are a result of :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Massive transgression</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Low sedimentation</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Marine regression</div>
          <div class="raw-opt"><span class="opt-letter">D</span> High sedimentation</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (High sedimentation)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">High sedimentation</div>
          <p>By established principles of sediment mechanics (Collinson et al., 2006; Boggs; Allen, 1982), syn-sedimentary (soft-sediment) deformation is fundamentally driven by <strong>high sedimentation rates</strong>. Rapid sediment dumping traps pore water, produces excess fluid pressures, creates reverse density gradients (dense sand over light saturated mud), and causes liquefaction and hydrodynamic loading instabilities.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Massive transgression</div>
          <p>A marine transgression is a regional eustatic rise in sea level drowning continental shelves. It controls basin-scale stratigraphy (fining-upward sequences), but does not directly cause local physical deformation of soft sediment layers.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Low sedimentation</div>
          <p>Low sedimentation rates allow ample time for sediments to dewater, compact orderly, and lithify peacefully, completely preventing soft-sediment deformation and instead promoting extensive bioturbation and hardground development.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Marine regression</div>
          <p>Marine regression involves shoreline seaward progradation, generating coarsening-upward vertical successions. Like transgression, it is a sequence-stratigraphic trend, not the mechanical trigger of syn-sedimentary deformational structures.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sedimentation Regime</th>
              <th>Pore Fluid Behavior</th>
              <th>Effective Stress ($\sigma'$)</th>
              <th>Dominant Sedimentary Features</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>High Sedimentation Rate (Option D)</strong></td><td>Pore water trapped; overpressured ($u \uparrow$)</td><td>$\sigma' \rightarrow 0$ (Zero shear strength)</td><td><strong>Syn-sedimentary deformation (Flames, Convolute beds, Pillows, Slumps)</strong></td></tr>
            <tr><td>Low Sedimentation Rate (Option B)</td><td>Normal hydrostatic drainage; dewatered</td><td>High effective stress ($\sigma' \uparrow$)</td><td>Intense bioturbation, hardgrounds, glauconite, phosphorite crusts</td></tr>
            <tr><td>Episodic Storm Deposition</td><td>Sudden surge loading followed by calm</td><td>Fluctuating effective stress</td><td>HCS, gutter casts, escape burrows (fugichnia)</td></tr>
            <tr><td>Turbidity Current Surge</td><td>Catastrophic rapid dumping of suspended load</td><td>Complete momentary liquefaction</td><td>Bouma sequences with basal rip-ups and convolute laminations</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is a 'seismite' in soft-sediment deformation studies?</div>
        <div class="pq-ans">Answer: A sedimentary bed deformed by earthquake-induced liquefaction and ground shaking.</div>
        <div class="pq-exp">Paleo-earthquakes shock water-saturated sediments, triggering fluidization, sand volcanoes, and thixotropic ball-and-pillow deformation.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What hydrodynamic instability explains the sinking of dense sand lobes into an underlying soupy mud layer?</div>
        <div class="pq-ans">Answer: Rayleigh-Taylor Instability (Density Inversion)</div>
        <div class="pq-exp">When a denser fluid/plastic layer (dense sand, $\rho \approx 2.0\text{ g/cm}^3$) overlies a lighter, water-rich layer (mud, $\rho \approx 1.4\text{--}1.6\text{ g/cm}^3$), perturbations amplify spontaneously into ball-and-pillow structures.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between liquefaction and fluidization in sediments?</div>
        <div class="pq-ans">Answer: Liquefaction occurs when grains lose contact due to pore pressure rise without net fluid flow; fluidization involves upward moving fluids dragging grains.</div>
        <div class="pq-exp">Fluidization produces vertical dewatering pipes, clastic dykes, and sand volcanoes; liquefaction produces convolute folding.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a clastic dyke (sandstone dyke)?</div>
        <div class="pq-ans">Answer: A discordant sedimentary intrusion formed when liquefied sand is injected upward or downward into fractures under high pore pressure.</div>
        <div class="pq-exp">Overpressured sand slurries shoot into surrounding strata along fault planes, preserving sedimentary dykes.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. In which division of the Bouma sequence are convolute laminations most typically developed?</div>
        <div class="pq-ans">Answer: The $T_c$ division (cross-laminated / rippled sand division).</div>
        <div class="pq-exp">Rapid deposition of the rippled $T_c$ division creates shear stress coupled with water escape, contorting ripple laminae into convolute folds.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. How can a syn-sedimentary slump fold be distinguished in the field from a tectonic fold?</div>
        <div class="pq-ans">Answer: Slump folds are bounded above and below by completely undeformed, horizontal planar beds and lack tectonic axial planar cleavage.</div>
        <div class="pq-exp">Tectonic folds affect entire regional rock packages, while syn-sedimentary slumps are strictly confined within a single depositional unit.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an olistostrome?</div>
        <div class="pq-ans">Answer: A chaotic, submarine mass-transport deposit of giant slide blocks (olistoliths) set in an unstratified muddy matrix formed by submarine slumping.</div>
        <div class="pq-exp">Olistostromes develop along active continental slopes and subduction trenches due to colossal gravitational collapse.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is thixotropy in water-saturated clays?</div>
        <div class="pq-ans">Answer: The property of certain cohesive muds to transform from a rigid gel into a flowing liquid upon mechanical agitation or vibration.</div>
        <div class="pq-exp">Under earthquake or storm vibration, thixotropic clays liquefy instantly, allowing overlying sand beds to founder into pillows.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q100: Sedimentary Skewness - Organic Detritus (Negative Skewness)
# -----------------------------------------------------------------------------
def gen_q0100():
    q_num = 100
    filename = "Q100_Sediment_Dominantly_Organic_Detritus_Indicates_Negative_Skewness_Complete_Guide.html"
    title = "Q100: Grain Size Statistics - Organic Detritus & Negative Skewness"
    badge = "OPSC 2019 Geology Paper-II • Question 100 • Sedimentary Petrology"
    h1_title = "Grain Size Granulometry: Skewness Physics and the Coarse Tail of Organic Detritus"
    meta_text = "<strong>Topic:</strong> Granulometric Parameters & Environmental Diagnostics • <strong>Key Concept:</strong> Negative Skewness & Coarse Bioclastic Tail • <strong>Textbooks:</strong> R.L. Folk & W.C. Ward (1957); G.M. Friedman (1961, 1967); Sam Boggs Jr."

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Grain Size Skewness & Mathematical Formulation</div>
      <p>In sediment granulometry, <strong>skewness ($Sk$)</strong> measures the degree of asymmetry of a grain-size frequency distribution curve relative to a normal (Gaussian) distribution. In Krumbein's phi ($\phi$) scale, where coarse particles have lower/negative values and fine particles have higher positive values ($\phi = -\log_2 d_{\text{mm}}$), skewness is calculated using <strong>Folk and Ward's (1957) Graphic Skewness ($Sk_I$)</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Skewness Class</th>
              <th>Mathematical Criterion ($Sk_I$)</th>
              <th>Grain Size Distribution Character</th>
              <th>Typical Geological Environment & Cause</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>NEGATIVE SKEWNESS (Coarse-skewed)</strong> (Option C)</td>
              <td><strong>$Sk_I < -0.10$ (down to $-1.0$)</strong></td>
              <td><strong>Excess coarse material; frequency curve has an elongated tail extending toward negative phi (coarse size)</strong>.</td>
              <td><strong>High-energy beaches; sediments dominated by coarse organic detritus (mollusc shells, coral/skeletal bioclasts)</strong>.</td>
            </tr>
            <tr>
              <td>Symmetrical (Near-Symmetrical)</td>
              <td>$-0.10 \le Sk_I \le +0.10$</td>
              <td>Balanced Gaussian distribution; mean equals median.</td>
              <td>Aeolian dune sands; perfectly sorted beach sands without shell lags.</td>
            </tr>
            <tr>
              <td>Positive Skewness (Fine-skewed)</td>
              <td>$Sk_I > +0.10$ (up to $+1.0$)</td>
              <td>Excess fine material; frequency curve has an elongated tail extending toward positive phi (fine size: silt/clay).</td>
              <td>Fluvial river sands (silt trapped in interstices), quiet lagoons, turbidity currents.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "When a sediment is dominantly composed of or enriched in <strong>organic detritus</strong> (such as coarse mollusc shell fragments, foraminifera, and echinoderm debris), it introduces an abundant coarse fraction that cannot be winnowed away by waves. On the phi scale, this creates a prominent coarse tail, causing the distribution to exhibit pronounced <strong>negative skewness</strong>. Friedman (1961, 1967) demonstrated that negative skewness is the most reliable criterion separating beach sediments containing shell detritus from positively skewed river sands."
        <div class="quote-author">&mdash; G.M. Friedman, <em>Dynamic processes and statistical parameters compared for size frequency distribution of beach and river sands</em> (Journal of Sedimentary Petrology, 1967)</div>
      </div>

      <div class="formula-box">
        $$\text{Folk and Ward (1957) Inclusive Graphic Skewness:}$$
        $$Sk_I = \frac{\phi_{16} + \phi_{84} - 2\phi_{50}}{2(\phi_{84} - \phi_{16})} + \frac{\phi_5 + \phi_{95} - 2\phi_{50}}{2(\phi_{95} - \phi_5)}$$
        $$\text{Coarse Organic Detritus Tail } \implies \phi_5 \ll \phi_{50} \implies \mathbf{Sk_I < 0\ (Negative\ Skewness\ \equiv Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q100/sedimentary_skewness_grain_size_distribution.png" alt="Sedimentary Skewness Grain Size Distribution" class="figure-img">
        <div class="figure-caption">Figure 100: Grain size frequency distribution curves comparing normal distribution (Sk=0), positive skewness (fine tail), and negative skewness (coarse tail caused by organic shell detritus).</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 100</div>
        <div class="raw-q-text">If sediment is dominantly compose of organic detritus, it is known to indicate :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Complex skewness</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Positive skewness</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Negative skewness</div>
          <div class="raw-opt"><span class="opt-letter">D</span> No skewness</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Negative skewness)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; CORRECT</div>
          <div class="opt-title">Negative skewness</div>
          <p>By classical sediment granulometry (Friedman, 1961, 1967; Folk, 1968; Boggs), when sediment contains dominant <strong>organic detritus</strong> (shell debris, bioclasts, skeletal fragments), these large biogenic particles form an extensive coarse-grained tail. In phi ($\phi$) units, a tail towards coarse sizes corresponds to lower/negative values, mathematically resulting in <strong>negative skewness</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Complex skewness</div>
          <p>'Complex skewness' is not a recognized statistical parameter in sedimentary geology; polymodal distributions are termed bimodal or polymodal, while skewness is strictly scalar (positive, negative, or zero).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Positive skewness</div>
          <p>Positive skewness reflects an excess of <strong>fine-grained tail</strong> (silt and clay grade particles), typical of quiet fluvial channels or settling basins, the exact opposite of coarse shell detritus.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">No skewness</div>
          <p>'No skewness' ($Sk = 0$) indicates a perfectly symmetrical Gaussian distribution, which occurs only in well-sorted mono-mineralic sands where both coarse and fine tails are equally balanced.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sediment Type</th>
              <th>Dominant Grain Size Component</th>
              <th>Skewness Sign ($Sk_I$)</th>
              <th>Diagnostic Depositional Mechanism</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Bioclastic Beach Sand</strong> (Option C)</td><td>Quartz sand + <strong>Coarse Organic Shell Detritus</strong></td><td><strong>Negative Skewness ($Sk < 0$)</strong></td><td>Wave winnowing removes fines; leaves coarse shell lag</td></tr>
            <tr><td>Fluvial River Sand</td><td>Quartz sand + Infiltrated Silt/Clay Matrix</td><td>Positive Skewness ($Sk > 0$)</td><td>Waning current traps fine suspended tail</td></tr>
            <tr><td>Aeolian Dune Sand</td><td>Pure well-sorted Medium to Fine Quartz Sand</td><td>Near-Zero (Symmetrical, $Sk \approx 0$)</td><td>Wind saltation selectively carries uniform grain size</td></tr>
            <tr><td>Lag Gravel / Reg</td><td>Coarse Pebbles/Cobbles + Wind-blown Sand</td><td>Strongly Negative ($Sk \ll 0$)</td><td>Deflation removes all fine silt/dust</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. Why do river sands characteristically display positive skewness, while beach sands display negative skewness?</div>
        <div class="pq-ans">Answer: Rivers deposit a tail of fine silt/clay as currents wane; beach wave backwash winnows out fines, leaving coarse lag and bioclastic debris.</div>
        <div class="pq-exp">Friedman's boundary plot ($Sk$ vs Mean size) uses this exact distinction to identify ancient depositional environments.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. In Folk and Ward's skewness classification, what range of values corresponds to 'strongly coarse-skewed'?</div>
        <div class="pq-ans">Answer: $Sk_I$ from $-0.30$ to $-1.00$</div>
        <div class="pq-exp">Values from $-0.10$ to $-0.30$ are coarse-skewed; values below $-0.30$ are strongly coarse-skewed (negative).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is kurtosis ($K_G$) in grain-size analysis?</div>
        <div class="pq-ans">Answer: A measure of the peakedness of the frequency distribution curve relative to normal (mesokurtic).</div>
        <div class="pq-exp">Excessively peaked curves are leptokurtic ($K_G > 1.0$); flat-topped curves are platykurtic ($K_G < 1.0$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is the mean grain size ($M_z$) formula defined by Folk and Ward?</div>
        <div class="pq-ans">Answer: $M_z = \frac{\phi_{16} + \phi_{50} + \phi_{84}}{3}$</div>
        <div class="pq-exp">The graphic mean uses the 16th, 50th, and 84th percentiles from the cumulative frequency curve.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What does sorting ($\sigma_I$, standard deviation) measure in a sediment sample?</div>
        <div class="pq-ans">Answer: The uniformity or spread of grain sizes around the mean.</div>
        <div class="pq-exp">$\sigma_I < 0.35\phi$ is very well sorted; $\sigma_I > 2.0\phi$ is very poorly sorted.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. If a sediment distribution has $\text{Mean} < \text{Median} < \text{Mode}$ on the millimeter scale, what skewness does it possess?</div>
        <div class="pq-ans">Answer: Negative Skewness (tail to coarse on phi scale).</div>
        <div class="pq-exp">When the mean is pulled away from the median toward the coarse tail, the skewness is negative on the phi scale.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a coquina or lumachelle in relation to bioclastic organic detritus?</div>
        <div class="pq-ans">Answer: A limestone composed entirely of cemented coarse organic shell detritus.</div>
        <div class="pq-exp">Coquina represents the ultimate lithified manifestation of negatively skewed bioclastic sediment.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What heavy mineral placer sands along the Odisha coast exhibit negative skewness?</div>
        <div class="pq-ans">Answer: Monazite-ilmenite-garnet heavy mineral beach placers (e.g., Chhatrapur / Gopalpur).</div>
        <div class="pq-exp">Severe storm wave winnowing concentrates heavy, dense mineral grains, leaving a negatively skewed coarse grain-size tail.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q101: Shallow Marine Palaeocurrent Patterns (Both Bimodal and Polymodal)
# -----------------------------------------------------------------------------
def gen_q101():
    q_num = 101
    filename = "Q101_Shallow_Marine_Palaeocurrent_Patterns_Both_Bimodal_And_Polymodal_Complete_Guide.html"
    title = "Q101: Sedimentary Palaeocurrents - Shallow Marine Regimes"
    badge = "OPSC 2019 Geology Paper-II • Question 101 • Sedimentary Petrology"
    h1_title = "Palaeocurrent Analysis: Shallow Marine Bimodal and Polymodal Vector Regimes"
    meta_text = "<strong>Topic:</strong> Palaeocurrent Systematics • <strong>Key Concept:</strong> Tidal Bipolar Bimodality vs. Storm-Shelf Polymodality • <strong>Textbooks:</strong> F.J. Pettijohn, P.E. Potter & R. Siever (1987); Sam Boggs Jr."

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Palaeocurrent Systematics by Environment</div>
      <p>Palaeocurrent analysis measures the azimuths of directional sedimentary structures (cross-bedding foresets, ripple crests, sole marks, grain imbrications) to reconstruct the orientation and hydrodynamic nature of ancient fluid flows. In <strong>shallow marine environments</strong> (intertidal flats, estuaries, shorefaces, and shallow epicontinental shelves), hydrodynamic regimes are governed by multi-directional forces, characteristically yielding <strong>Both Bimodal and Polymodal</strong> palaeocurrent distributions:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Depositional Environment</th>
              <th>Palaeocurrent Pattern</th>
              <th>Vector Geometry & Rose Diagram</th>
              <th>Dominant Hydrodynamic Driving Force</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Fluvial (Braided / Meandering River)</td>
              <td><strong>Unimodal</strong></td>
              <td>Single narrow, well-defined mode pointing in downstream flow direction.</td>
              <td>Unidirectional gravity flow down topographic gradient.</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Shallow Marine &ndash; Tidal Zone</strong></td>
              <td><strong>Bimodal (Bipolar)</strong></td>
              <td>Two dominant modes oriented $180^\circ$ opposite to one another ('herringbone' cross-bedding).</td>
              <td>Semidiurnal or diurnal reversing tidal currents (reversing flood tide vs. ebb tide).</td>
            </tr>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>Shallow Marine &ndash; Open Shelf</strong></td>
              <td><strong>Polymodal</strong></td>
              <td>Multiple, complex modes radiating in three or more directions.</td>
              <td>Superposition of tidal currents, storm-generated geostrophic currents, wave refraction, and longshore drift.</td>
            </tr>
            <tr>
              <td>Aeolian (Desert Dune Field)</td>
              <td>Unimodal to Bimodal</td>
              <td>Depends on dune type (Unimodal for Barchans; Bimodal for Seif/Linear dunes).</td>
              <td>Prevailing trade winds vs. seasonal storm winds.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "Shallow marine environments are unique in displaying <strong>both bimodal and polymodal palaeocurrent patterns</strong>. In nearshore tidal zones, the periodic reversal of flood and ebb currents produces diagnostic bimodal-bipolar cross-bedding. On broader shelf platforms, the complex interaction of tides with storm-induced geostrophic flows and longshore currents scatters transport vectors into complex polymodal distributions."
        <div class="quote-author">&mdash; F.J. Pettijohn, P.E. Potter & R. Siever, <em>Sand and Sandstone</em> (2nd Ed., Springer-Verlag, pp. 288&ndash;292)</div>
      </div>

      <div class="formula-box">
        $$\text{Vector Mean Azimuth: } \theta_v = \arctan \left( \frac{\sum \sin \theta_i}{\sum \cos \theta_i} \right)$$
        $$\text{Shallow Marine Characteristic: } \mathbf{Tidal\ Reversal \rightarrow Bimodal} + \mathbf{Storm/Wave\ Interference \rightarrow Polymodal}$$
        $$\therefore \mathbf{Shallow\ Marine\ Palaeocurrents \equiv Both\ Bimodal\ and\ Polymodal\ (Option\ D)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q101/palaeocurrent_rose_diagram_shallow_marine.png" alt="Palaeocurrent Rose Diagram Shallow Marine" class="figure-img">
        <div class="figure-caption">Figure 101: Palaeocurrent rose diagrams comparing Unimodal fluvial flow, Bimodal tidal reversing flow, and complex Polymodal storm-shelf marine patterns.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 101</div>
        <div class="raw-q-text">In shallow marine environment, generally the palaeocurrent patterns are :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Polymodal</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Bimodal</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Unimodal</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Both Bimodal and Polymodal</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION D (Both Bimodal and Polymodal)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION D &bull; CORRECT</div>
          <div class="opt-title">Both Bimodal and Polymodal</div>
          <p>In standard sedimentological literature (Pettijohn et al., 1987; Boggs, 2014; Potter & Pettijohn, 1977), shallow marine palaeocurrents are characterized by <strong>Both Bimodal and Polymodal</strong> patterns. Tidal estuaries and barrier lagoons exhibit bimodal (herringbone) patterns due to flood-ebb reversals, while open marine shelves exhibit polymodal patterns due to the interference of storms, longshore currents, and tides.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; INCOMPLETE</div>
          <div class="opt-title">Polymodal</div>
          <p>While open marine shelves exhibit polymodal patterns, selecting Option A ignores the ubiquitous bimodal patterns formed in shallow tidal environments; Option D comprehensively includes both.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; INCOMPLETE</div>
          <div class="opt-title">Bimodal</div>
          <p>While tidal channels produce bimodal patterns, this only represents one sub-environment of the shallow marine realm; shelf waves and storm surges create polymodal patterns, making Option D the correct complete answer.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Unimodal</div>
          <p>Unimodal patterns are strictly diagnostic of <strong>unidirectional flow</strong>, such as down-slope fluvial river channels and delta distributaries, which do not experience tidal reversals or multi-directional shelf currents.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Palaeocurrent Pattern</th>
              <th>Vector Spread & Symmetry</th>
              <th>Diagnostic Sedimentary Structure</th>
              <th>Prototypical Depositional Realm</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>Unimodal</td><td>Narrow single peak ($< 60^\circ$ dispersion)</td><td>Planar cross-bedding, flute casts, pebble imbrication</td><td>Fluvial channels, turbidity current fans</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Bimodal (Bipolar)</strong></td><td>Two opposite peaks ($180^\circ$ apart)</td><td>Herringbone cross-stratification</td><td>Intertidal flats, tidal inlet channels</td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Polymodal</strong></td><td>Three or more radiating peaks</td><td>Interference ripples, hummocky cross-stratification</td><td>Storm-dominated shallow marine shelves</td></tr>
            <tr><td>Random / Non-directional</td><td>No statistically preferred orientation</td><td>Massive bedding, bioturbated muds</td><td>Quiet abyssal plains, pelagic oozes</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is a 'rose diagram' in structural and sedimentological analysis?</div>
        <div class="pq-ans">Answer: A circular histogram showing the directional frequency distribution of directional data (e.g., cross-bed dips, joint strikes).</div>
        <div class="pq-exp">Azimuths ($0^\circ\text{ to } 360^\circ$) are plotted in angular sectors (typically $10^\circ$ or $30^\circ$) with petal radius proportional to frequency.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the geological term for bimodal cross-bedding where successive layers dip in opposite directions ($180^\circ$ apart)?</div>
        <div class="pq-ans">Answer: Herringbone cross-stratification</div>
        <div class="pq-exp">Herringbone structure is an irrefutable proof of tidal marine influence (opposing ebb and flood currents).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is Rayleigh's test of significance in palaeocurrent statistics?</div>
        <div class="pq-ans">Answer: A statistical test to determine whether a measured palaeocurrent distribution has a preferred non-random orientation or is uniform.</div>
        <div class="pq-exp">Rayleigh's test evaluates the vector magnitude ($L$); if $p < 0.05$, the preferred flow direction is statistically significant.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What sole mark provides an unequivocal unidirectional palaeocurrent vector (both line of flow and pointing down-current)?</div>
        <div class="pq-ans">Answer: Flute casts</div>
        <div class="pq-exp">Flute casts have a deep, bulbous up-current nose and a shallow, flared down-current tail, providing complete vector sense.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What sole mark provides only the LINE of transport (bidirectional) without indicating whether flow went left or right?</div>
        <div class="pq-ans">Answer: Groove casts</div>
        <div class="pq-exp">Groove casts are rectilinear parallel ridges carved by dragged tools; they define trend but not polarity.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why are turbidity current palaeocurrents in flysch basins overwhelmingly unimodal?</div>
        <div class="pq-ans">Answer: Turbidity currents are catastrophic density underflows driven strictly downslope by gravity into the abyssal trench axis.</div>
        <div class="pq-exp">Deep-water turbidity flows cannot reverse or deviate from the bathymetric gradient, producing tightly unimodal flute distributions.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is a bimodal-oblique palaeocurrent pattern?</div>
        <div class="pq-ans">Answer: Two dominant current directions intersecting at an angle other than $180^\circ$ (typically $60^\circ\text{--}120^\circ$).</div>
        <div class="pq-exp">Forms on shallow marine shorelines where tidal currents intersect wave-driven longshore currents at an oblique angle.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. In the Proterozoic Vindhyan Basin of Central India, what do bimodal palaeocurrents in the Kaimur sandstones indicate?</div>
        <div class="pq-ans">Answer: A shallow marine, tide-dominated epicontinental sea.</div>
        <div class="pq-exp">Reversing herringbone cross-bedding and ripple patterns prove marine tidal influence across the Vindhyan platform.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q102: Miogeosyncline - Non-Volcanic Basin Adjacent to Craton
# -----------------------------------------------------------------------------
def gen_q102():
    q_num = 102
    filename = "Q102_Basin_Thinner_Sediments_No_Volcanics_Adjacent_Craton_Is_Miogeosyncline_Complete_Guide.html"
    title = "Q102: Basin Tectonics - Miogeosyncline Characteristics"
    badge = "OPSC 2019 Geology Paper-II • Question 102 • Sedimentary Petrology & Tectonics"
    h1_title = "Geosynclinal Theory: The Non-Volcanic Miogeosyncline Adjacent to the Craton"
    meta_text = "<strong>Topic:</strong> Sedimentary Basins & Geosynclinal Theory • <strong>Key Concept:</strong> Miogeosyncline vs. Eugeosyncline • <strong>Textbooks:</strong> Marshall Kay (1951); Hans Stille (1940); K.M. Bangar (p. 155)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: The Geosynclinal Architecture (Stille & Kay)</div>
      <p>In classical tectonics and historical geology, before the modern plate tectonic revolution, mountain-building belts were analyzed through <strong>Geosynclinal Theory</strong> pioneered by James Hall (1859), J.D. Dana (1873), <strong>Hans Stille (1940)</strong>, and <strong>Marshall Kay (1951)</strong>. An orthogeosyncline (linear mobile belt between cratons) was subdivided into two contrasting longitudinal belts:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Geosynclinal Zone</th>
              <th>Geographic & Tectonic Position</th>
              <th>Sediment Thickness & Lithofacies</th>
              <th>Volcanic Activity</th>
              <th>Plate Tectonic Modern Equivalent</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>MIOGEOSYNCLINE</strong> (Option B)</td>
              <td><strong>Adjacent to the stable craton (continental borderland / platform margin)</strong>.</td>
              <td><strong>Thinner development of sediments</strong>; shallow-water cratonic suite (clean orthoquartzites, limestones, dolomites, shales).</td>
              <td><strong>NO contemporaneous volcanic rocks (strictly avolcanic)</strong>.</td>
              <td><strong>Passive Continental Margin (Continental Shelf & Rise)</strong> (e.g., modern Atlantic coast of North America).</td>
            </tr>
            <tr>
              <td><strong>Eugeosyncline</strong></td>
              <td>Outer, oceanward mobile belt far from the craton.</td>
              <td>Immense sediment thickness; deep-water flysch, greywackes, radiolarian cherts, dark pelagic shales.</td>
              <td><strong>Abundant submarine volcanic rocks</strong> (spilites, pillow basalts, ophiolitic suites).</td>
              <td><strong>Subduction Trench, Accretionary Prism & Island Arc</strong> (e.g., modern Western Pacific margins).</td>
            </tr>
            <tr>
              <td>Parageosyncline</td>
              <td>Within the craton itself.</td>
              <td>Thin cratonic platform covers; minimal deformation.</td>
              <td>None.</td>
              <td>Intracratonic Sag Basin / Epiregional Basin.</td>
            </tr>
            <tr>
              <td>Rift Valley / Graben (Options C & D)</td>
              <td>Extensional fault-bounded depression bounded by normal faults.</td>
              <td>Terrestrial fanglomerates, red-bed arkoses, lacustrine shales.</td>
              <td>Bimodal volcanism (basalt-rhyolite) common.</td>
              <td>Incipient Continental Divergent Boundary (e.g., East African Rift).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "A <strong>miogeosyncline</strong> is that part of an orthogeosyncline which is situated adjacent to a stable craton. It is characterized by a <strong>thinner accumulation of sediments</strong> (principally shallow-marine orthoquartzite-carbonate facies) and by a <strong>complete absence of contemporaneous volcanism</strong>. In contrast, the outer oceanward eugeosyncline contains thick piles of greywackes and is characterized by abundant volcanic rocks (ophiolites)."
        <div class="quote-author">&mdash; Marshall Kay, <em>North American Geosynclines</em> (Geological Society of America Memoir 48, 1951)</div>
      </div>

      <div class="formula-box">
        $$\text{Orthogeosyncline} = \mathbf{Miogeosyncline\ (Inner,\ Non\text{-}Volcanic)} + \mathbf{Eugeosyncline\ (Outer,\ Volcanic)}$$
        $$\text{Formula: } \mathbf{Adjacent\ to\ Craton} + \mathbf{Thinner\ Sediments} + \mathbf{Zero\ Volcanics} \equiv \mathbf{Miogeosyncline\ (Option\ B)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q102/miogeosyncline_vs_eugeosyncline_craton_margin.png" alt="Miogeosyncline vs Eugeosyncline Craton Margin" class="figure-img">
        <div class="figure-caption">Figure 102: Cross-section of classical geosynclinal architecture showing the non-volcanic Miogeosyncline adjacent to the stable craton transitioning oceanward to the volcanic Eugeosyncline.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 102</div>
        <div class="raw-q-text">A basin with thinner development of sediments and no volcanic rocks, forming adjacent to a craton is called :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Parageosyncline</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Miogeosyncline</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Rift valley</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Graben</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Miogeosyncline)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Miogeosyncline</div>
          <p>By Hans Stille's (1940) and Marshall Kay's (1951) classical definitions, a <strong>miogeosyncline</strong> (from Greek <em>meion</em> = less) is the marginal belt of an orthogeosyncline that forms <strong>adjacent to a stable craton</strong>, characterized by <strong>thinner sediment accumulation</strong> (shallow-water carbonates and sandstones) and the <strong>complete absence of volcanic rocks</strong>.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Parageosyncline</div>
          <p>A parageosyncline (Kay, 1951) is a basin situated wholly <em>within</em> the craton itself (an intracratonic platform basin), rather than marginal mobile belts bordering cratonic edges.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Rift valley</div>
          <p>A rift valley is an active extensional tectonic depression bounded by normal faults, typically characterized by prominent continental volcanism (e.g., East African Rift basalts and phonolites), not an avolcanic marine margin.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Graben</div>
          <p>A graben is a local structural block downdropped between two parallel normal faults, representing a fault geometry rather than a regional craton-margin sedimentary basin.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Basin Type</th>
              <th>Proximity to Craton</th>
              <th>Sediment Thickness & Type</th>
              <th>Volcanism Present?</th>
              <th>Orogenic Inversion</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Miogeosyncline</strong> (Option B)</td><td>Directly adjacent to craton margin</td><td>Thinner; shallow marine carbonates/quartzites</td><td><strong>NO (Avolcanic)</strong></td><td>Forms folded foreland thrust belts (e.g., Jura Mtns, Valley & Ridge)</td></tr>
            <tr><td>Eugeosyncline</td><td>Distal oceanward margin</td><td>Vast thickness; turbidites, cherts, flysch</td><td><strong>YES (Abundant ophiolites, spilites)</strong></td><td>Forms high-grade crystalline metamorphic core of mountains</td></tr>
            <tr><td>Zeugogeosyncline</td><td>Intracratonic between uplifts</td><td>Variable red-beds and arkoses</td><td>Absent to rare</td><td>Basin and Swell tectonics</td></tr>
            <tr><td>Autogeosyncline</td><td>Within craton without nearby uplifts</td><td>Thin, uniform platform limestone/evaporite</td><td>Absent</td><td>Gentle subsidence without folding (Michigan Basin)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. In the Appalachian mountain chain of North America, what physiographic province represents the ancient miogeosyncline?</div>
        <div class="pq-ans">Answer: The Valley and Ridge Province</div>
        <div class="pq-exp">The Valley and Ridge consists of folded Paleozoic shallow-water carbonates and sandstones deposited in the non-volcanic Appalachian miogeosyncline.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What modern plate tectonic setting directly corresponds to the ancient 'eugeosyncline'?</div>
        <div class="pq-ans">Answer: The subduction zone / accretionary prism and volcanic island arc.</div>
        <div class="pq-exp">Subduction trenches accumulate volcanic debris and deep flysch turbidites, precisely matching the eugeosynclinal definition.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is an 'epieugeosyncline'?</div>
        <div class="pq-ans">Answer: A deeply subsiding basin developed upon an already deformed, older eugeosynclinal orogenic belt (Marshall Kay).</div>
        <div class="pq-exp">Epieugeosynclines form during late-orogenic or post-orogenic collapse, filled with late molasse and volcanics.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. In the Himalayan orogenic belt, which zone represents the miogeosynclinal (Tethyan) succession?</div>
        <div class="pq-ans">Answer: The Tethys (Tibetan) Himalayan zone (Spiti, Zanskar, Kashmir)</div>
        <div class="pq-exp">The Tethyan belt represents the richly fossiliferous, shallow-to-intermediate marine passive margin of the northern Indian craton.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What rock association is known as the 'Stille-Steinmann Trinity' characteristic of eugeosynclines?</div>
        <div class="pq-ans">Answer: Serpentinites / peridotites, pillow lavas (spilites), and radiolarian cherts (the ophiolite suite).</div>
        <div class="pq-exp">Gustav Steinmann (1905) identified this trinity as the hallmark of deep ocean-floor volcanism incorporated into mountain belts.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Who first proposed the term 'Geosynclinal' in the 19th century?</div>
        <div class="pq-ans">Answer: James Dwight Dana (1873), building upon James Hall's (1859) observations in the Appalachians.</div>
        <div class="pq-exp">Dana coined 'geosynclinal' for Hall's concept of a giant crustal downwarp accumulating immense sediment thicknesses before uplift.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is the fundamental difference between 'flysch' and 'molasse'?</div>
        <div class="pq-ans">Answer: Flysch is marine syn-orogenic turbidites deposited during active basin deepening; molasse is shallow marine to continental post-orogenic debris shed from rising mountains.</div>
        <div class="pq-exp">Flysch fills eugeosynclinal trenches; molasse fills foreland basins (e.g., Siwaliks) after major orogenic uplift.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a 'miogeocline' in modern terminology?</div>
        <div class="pq-ans">Answer: A passive continental margin sediment prism that progrades oceanward without a seaward enclosing borderland.</div>
        <div class="pq-exp">Robert Dietz and John Holden (1974) reinterpreted miogeosynclines as passive margin continental terrace/rise wedges (miogeoclines).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q103: Rock Principally Made Up of Clay Minerals (Greywacke vs. Siltstone)
# -----------------------------------------------------------------------------
def gen_q103():
    q_num = 103
    filename = "Q103_Rock_Principally_Made_Up_Of_Clay_Minerals_Greywacke_Complete_Guide.html"
    title = "Q103: Sedimentary Petrology - Clastic Rocks & Clay Minerals"
    badge = "OPSC 2019 Geology Paper-II • Question 103 • Sedimentary Petrology"
    h1_title = "Clastic Petrology: Matrix-Rich Greywackes and the Clay Mineral Question"
    meta_text = "<strong>Topic:</strong> Clastic Rock Classification • <strong>Key Concept:</strong> Detrital Matrix of Clay Minerals & Sandstone Classes • <strong>Textbooks:</strong> F.J. Pettijohn (1975); K.M. Bangar (p. 136); P.K. Mukherjee (p. 251)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Clay Minerals in Sedimentary Rocks</div>
      <p>In sedimentary petrology, rocks containing significant proportions of <strong>clay minerals</strong> (hydrous aluminum phyllosilicates such as illite, smectite/montmorillonite, kaolinite, and chlorite) are classified based on their grain size and matrix abundance. Among the four options provided in Question 103 (Arkose, Siltstone, Greywacke, and Dolostone), a detailed comparative analysis reveals their mineralogical constitution:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Name</th>
              <th>Grain Size Classification</th>
              <th>Primary Framework Grains</th>
              <th>Clay Minerals & Matrix Presence</th>
              <th>Petrological Evaluation</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>GREYWACKE (Wacke)</strong> (Option C)</td>
              <td>Sandstone ($2\text{ mm} - 1/16\text{ mm}$)</td>
              <td>Angular quartz, feldspar, rock fragments</td>
              <td><strong>Abundant detrital & authigenic matrix (&gt; 15% to 50%) composed principally of CLAY MINERALS, chlorite, and sericite</strong>.</td>
              <td><strong>The defining feature that distinguishes greywacke from normal sandstones is its pervasive clay-mineral matrix</strong>.</td>
            </tr>
            <tr>
              <td>Siltstone (Option B)</td>
              <td>Silt grade ($1/16 - 1/256\text{ mm}$)</td>
              <td>Micro-quartz ($SiO_2$) & feldspar silt particles</td>
              <td>Minor clay matrix between quartz silt grains; may grade into mudstone.</td>
              <td>Composed primarily of quartz silt grains, not clay minerals (pure clay rock is shale/claystone).</td>
            </tr>
            <tr>
              <td>Arkose (Option A)</td>
              <td>Sandstone ($2\text{ mm} - 1/16\text{ mm}$)</td>
              <td>Feldspar (&gt;25%) + Quartz</td>
              <td>Negligible matrix (&lt;15%); clean arenite.</td>
              <td>Composed principally of feldspar and quartz, virtually free of clay.</td>
            </tr>
            <tr>
              <td>Dolostone (Option D)</td>
              <td>Chemical / Carbonate rock</td>
              <td>Dolomite mineral crystals $[CaMg(CO_3)_2]$</td>
              <td>Trace insoluble residue only.</td>
              <td>A magnesium carbonate rock; totally devoid of detrital clay minerals.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "<strong>Greywacke</strong> is a dark, tough, poorly-sorted sandstone consisting of angular grains of quartz, feldspar, and small rock fragments embedded in an abundant, fine-grained matrix (&gt;15%). This matrix is <strong>principally made up of clay minerals</strong>, chlorite, sericite, and fine silica paste, giving the rock its characteristic dark greenish-grey color and muddy appearance ('dirty sandstone')."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Rocks, p. 136)</div>
      </div>

      <div class="formula-box">
        $$\text{Pettijohn \& Dott Definition: } \mathbf{Greywacke} \equiv \text{Framework Grains} + \mathbf{Detrital\ Matrix\ (>15\%\ to\ 50\%)\ [Clay\ Minerals + Chlorite]}$$
        $$\text{Comparison: } \text{Arkose (Feldspar)} \quad \text{Siltstone (Quartz Silt)} \quad \text{Dolostone (Dolomite)} \implies \mathbf{Greywacke\ (Option\ C)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q103/greywacke_clay_matrix_peteology_dott.png" alt="Greywacke Clay Matrix Petrography" class="figure-img">
        <div class="figure-caption">Figure 103: Microscopic petrographic view of Greywacke, highlighting angular grains of quartz and lithics embedded in an abundant paste of clay minerals, chlorite, and sericite.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 103</div>
        <div class="raw-q-text">Which of the following rocks is principally made up of clay minerals ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Arkose</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Siltstone</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Greywacke</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Dolostone</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION C (Greywacke) [Exam Context Analysis & Full Forensic Breakdown]
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION C &bull; EXAM TARGET (BEST FIT AMONG CHOICES)</div>
          <div class="opt-title">Greywacke</div>
          <p>Among the four options provided, <strong>Greywacke</strong> is the rock universally defined in petrology textbooks (Bangar, p. 136; P.K. Mukherjee, p. 251) by its defining abundance of a fine-grained detrital matrix (15% to 50%) that is <strong>principally made up of clay minerals</strong>, chlorite, and sericite. While pure argillaceous rocks (shale/claystone) are absent from the options, Greywacke is the intended answer because the presence of this dominant clay matrix is its primary petrographic diagnostic criterion.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Arkose</div>
          <p>Arkose is a clean arenite sandstone containing more than 25% feldspar. Its matrix is strictly less than 15% (typically &lt;5%), making it deficient in clay minerals.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION B &bull; DISTRACTOR</div>
          <div class="opt-title">Siltstone</div>
          <p>Siltstone is defined granulometrically by <strong>silt-sized particles</strong> (1/16 mm to 1/256 mm). Mineralogically, detrital silt is dominated by <strong>micro-crystalline quartz</strong> and feldspar, NOT clay minerals. Clay-grade minerals ($< 1/256\text{ mm}$) define mudstone, claystone, and shale.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Dolostone</div>
          <p>Dolostone is a non-clastic, chemical carbonate rock composed almost entirely of the carbonate mineral dolomite $[CaMg(CO_3)_2]$. It is completely devoid of silicate clay minerals.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Rock Name</th>
              <th>Dominant Mineral Species</th>
              <th>Grain Size Grade</th>
              <th>Matrix Abundance</th>
              <th>Classification Category</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Greywacke (Option C)</strong></td><td>Quartz + Lithics + <strong>Clay Matrix</strong></td><td>Sand (with abundant silt/clay matrix)</td><td><strong>&gt; 15% to 50% Clay Matrix</strong></td><td>Terrigenous Wacke (Turbidite)</td></tr>
            <tr><td>Siltstone (Option B)</td><td><strong>Quartz Silt</strong> + minor Feldspar</td><td>Silt ($1/16\text{--}1/256\text{ mm}$)</td><td>Variable (0&ndash;20%)</td><td>Terrigenous Siltrock</td></tr>
            <tr><td>Claystone / Shale</td><td><strong>Clay Minerals (Illite, Smectite, Kaolinite)</strong></td><td>Clay ($&lt; 1/256\text{ mm}$)</td><td>&gt; 90% Clay</td><td>Pelitic / Argillaceous Rock</td></tr>
            <tr><td>Arkose (Option A)</td><td>Quartz + <strong>Feldspar (&gt;25%)</strong></td><td>Sand ($2\text{--}1/16\text{ mm}$)</td><td>&lt; 15% (Clean Arenite)</td><td>Feldspathic Arenite</td></tr>
            <tr><td>Dolostone (Option D)</td><td><strong>Dolomite</strong> $[CaMg(CO_3)_2]$</td><td>Crystalline / Chemical</td><td>Zero (Carbonate)</td><td>Chemical Carbonate Rock</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What rock is the 100% pure argillaceous equivalent composed almost exclusively of clay minerals?</div>
        <div class="pq-ans">Answer: Claystone (non-fissile) or Shale (fissile).</div>
        <div class="pq-exp">Claystones and shales consist of &gt;66% clay-grade phyllosilicate minerals ($< 1/256\text{ mm}$).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What are the three primary clay mineral groups found in sedimentary rocks?</div>
        <div class="pq-ans">Answer: Kaolinite, Illite, and Smectite (Montmorillonite) groups.</div>
        <div class="pq-exp">Kaolinite reflects humid tropical leaching; illite reflects temperate/alkaline conditions; smectite reflects weathered volcanic ash.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the matrix threshold that separates arenites from wackes (greywackes) in modern sandstone classifications?</div>
        <div class="pq-ans">Answer: 15% matrix (Dott, 1964; Pettijohn, 1975)</div>
        <div class="pq-exp">Sandstones with &lt;15% fine matrix are arenites; sandstones with 15% to 50% clay-silt matrix are wackes (greywackes).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What process generates 'pseudomatrix' in greywackes during burial diagenesis?</div>
        <div class="pq-ans">Answer: The mechanical flattening and squashing of soft, ductile shale/mud lithic clasts between rigid quartz grains.</div>
        <div class="pq-exp">Dickinson (1970) showed that deeply buried lithic grains deform into a pseudo-clay matrix resembling primary depositional mud.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. Which sedimentary rock displays fissility (the tendency to split along thin, parallel laminar planes)?</div>
        <div class="pq-ans">Answer: Shale</div>
        <div class="pq-exp">Fissility is caused by the parallel preferred alignment of platy clay mineral flakes during mechanical compaction.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What is bentonite?</div>
        <div class="pq-ans">Answer: A highly plastic clay rock composed predominantly of smectite (montmorillonite) formed by the alteration of volcanic ash in water.</div>
        <div class="pq-exp">Bentonite swells dramatically in water and is widely used in drilling muds and civil engineering sealants.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. Why is siltstone mineralogically dominated by quartz rather than clay minerals?</div>
        <div class="pq-ans">Answer: Quartz grains break down mechanically to silt size (the 'terminal quartz limit' of ~20 to 4 $\mu\text{m}$), whereas clay minerals form by chemical weathering.</div>
        <div class="pq-exp">Abrasion can crush quartz down to silt size, but cannot easily produce clay-grade quartz, so silt is mechanically stable quartz debris.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a 'marl'?</div>
        <div class="pq-ans">Answer: An intimate mixture of clay minerals and calcium carbonate (typically 35% to 65% carbonate and 35% to 65% clay).</div>
        <div class="pq-exp">Marls represent transitional deposits between pure pelagic carbonate limestones and terrigenous clay muds.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q104: Depositional Sedimentary Structure (Graded Bedding)
# -----------------------------------------------------------------------------
def gen_q104():
    q_num = 104
    filename = "Q104_Graded_Bedding_Is_A_Depositional_Sedimentary_Structure_Complete_Guide.html"
    title = "Q104: Sedimentary Structures - Graded Bedding Primary Depositional Nature"
    badge = "OPSC 2019 Geology Paper-II • Question 104 • Sedimentary Petrology"
    h1_title = "Primary Sedimentary Structures: Depositional Nature of Graded Bedding and Cross-Bedding"
    meta_text = "<strong>Topic:</strong> Classification of Sedimentary Structures • <strong>Key Concept:</strong> Depositional vs. Erosional vs. Post-Depositional Structures • <strong>Textbooks:</strong> F.J. Pettijohn & P.E. Potter (1964); Sam Boggs Jr. (2014); K.M. Bangar"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Classification of Sedimentary Structures</div>
      <p>Sedimentary structures provide vital clues to the physical processes operating during sedimentation. In genetic classifications (Pettijohn & Potter, 1964; Collinson et al., 2006; Boggs, 2014), structures are rigorously divided into <strong>Primary Depositional</strong>, <strong>Erosional (Scour)</strong>, and <strong>Post-Depositional (Deformational / Diagenetic)</strong> structures:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Genetic Category</th>
              <th>Physical Genesis</th>
              <th>Classic Sedimentary Examples</th>
              <th>Option Analysis</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>PRIMARY DEPOSITIONAL STRUCTURES</strong></td>
              <td>Formed directly during the physical deposition of sediment from flowing or settling fluid.</td>
              <td><strong>GRADED BEDDING (Option A)</strong>, Planar Bedding, Lamination, Ripple Cross-Lamination, <strong>Trough Cross-Bedding (Option B)</strong>.</td>
              <td><strong>Graded bedding represents the pure hydrodynamic depositional settling structure from waning suspension currents</strong>.</td>
            </tr>
            <tr>
              <td>Primary Erosional (Scour) Structures</td>
              <td>Carved into cohesive substratum prior to deposition; preserved as sole marks on the undersides of beds.</td>
              <td>Flute casts, groove casts, bounce marks, prod marks, channels, scour-and-fill troughs.</td>
              <td>Erosional bedforms preceding deposition.</td>
            </tr>
            <tr>
              <td>Post-Depositional Deformational Structures</td>
              <td>Formed after deposition by gravity collapse, liquefaction, pore-fluid escape, or tectonic loading.</td>
              <td><strong>Collapse structures (Option C)</strong>, <strong>Injection structures / Clastic dykes (Option D)</strong>, Slump folds, Convolute bedding.</td>
              <td>Post-depositional disturbance; NOT primary depositional.</td>
            </tr>
            <tr>
              <td>Diagenetic / Chemical Structures</td>
              <td>Formed by post-depositional chemical precipitation or dissolution in solid rock.</td>
              <td>Concretions, nodules, geodetic cavities, stylolites, cone-in-cone structures.</td>
              <td>Diagenetic authigenesis.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "A <strong>graded bed</strong> is one in which there is a systematic vertical change in grain size from coarse at the base to fine at the top. It is the premier <strong>depositional sedimentary structure</strong> resulting from the gradual waning of current velocity or settling from a dense suspension (such as a turbidity current). Each graded bed records a single discrete depositional event."
        <div class="quote-author">&mdash; F.J. Pettijohn & P.E. Potter, <em>Atlas and Glossary of Primary Sedimentary Structures</em> (Springer-Verlag, 1964)</div>
      </div>

      <div class="formula-box">
        $$\text{Stokes' Settling Velocity: } v_{\text{settling}} = \frac{g (\rho_s - \rho) d^2}{18 \eta} \implies \text{Coarsest grains } (d_{\text{max}}) \text{ deposit first}$$
        $$\mathbf{Waning\ Current\ Deposition} \rightarrow \mathbf{Graded\ Bedding\ (Primary\ Depositional\ Structure \equiv Option\ A)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q104/graded_bedding_bouma_sequence_turbidite.png" alt="Graded Bedding Turbidite Bouma Sequence" class="figure-img">
        <div class="figure-caption">Figure 104: Anatomy of graded bedding in a turbidite (Bouma Ta division), showing normal upward fining from coarse pebbles/sand at the base to fine silt and pelagic mud at the top.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 104</div>
        <div class="raw-q-text">Which of the following is a depositional sedimentary structure ?</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Graded bedding</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Trough cross bedding</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Collapse structure</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Injection structure</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION A (Graded bedding) [with Option B also evaluated as a primary depositional bedform]
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION A &bull; PRIMARY DEPOSITIONAL STRUCTURE (STANDARD KEY)</div>
          <div class="opt-title">Graded bedding</div>
          <p><strong>Graded bedding</strong> is the textbook archetype of a primary <strong>depositional</strong> structure. It forms directly through the progressive gravitational settling of suspended particles from a waning turbidity current or flood surge, with coarse grains depositing first at the bottom and progressively finer particles settling on top.</p>
        </div>

        <div class="option-card correct" style="border-left-color: #0284c7;">
          <div class="opt-tag" style="background:#e0f2fe; color:#0284c7;">OPTION B &bull; PRIMARY DEPOSITIONAL BEDFORM</div>
          <div class="opt-title">Trough cross bedding</div>
          <p>Trough cross-bedding is also a primary depositional bedform (formed by migrating 3D dunes). However, because it involves an initial phase of erosional scouring of a curved trough followed by deposition, standard syllabi frequently designate <em>graded bedding</em> as the pure depositional structure.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Collapse structure</div>
          <p>A collapse structure is a <strong>post-depositional deformational</strong> or diagenetic structure caused by underground dissolution (e.g., karst cave collapse or evaporite dissolution collapse breccias), completely non-depositional.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Injection structure</div>
          <p>An injection structure (such as a clastic/sandstone dyke or sill) is a <strong>soft-sediment deformational</strong> structure formed when liquefied sediment is forcefully intruded into surrounding rocks under excess fluid pressure.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sedimentary Structure</th>
              <th>Genetic Classification</th>
              <th>Physical Forming Agent</th>
              <th>Geopetal (Way-Up) Value?</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Graded Bedding (Option A)</strong></td><td><strong>Primary Depositional</strong></td><td>Waning suspension / turbidity current</td><td><strong>Excellent (Fining upward indicates top)</strong></td></tr>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Trough Cross-Bedding (Option B)</strong></td><td><strong>Primary Depositional (Bedform)</strong></td><td>Migrating 3D dunes in rivers/seas</td><td><strong>Excellent (Top truncation, base concave)</strong></td></tr>
            <tr><td>Collapse Structure (Option C)</td><td>Post-Depositional / Karst</td><td>Subsurface dissolution and roof failure</td><td>Poor to inverted</td></tr>
            <tr><td>Injection Structure (Option D)</td><td>Deformational / Intrusive</td><td>Overpressured liquefied sand intrusion</td><td>Non-depositional (Cross-cutting)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. What is reverse (inverse) graded bedding and where does it typically form?</div>
        <div class="pq-ans">Answer: Inverse grading occurs where finer grains are at the base and coarser clasts are at the top, forming in high-concentration debris flows and grain flows.</div>
        <div class="pq-exp">Dispersive pressure (Bagnold effect) forces larger clasts toward the upper shearing surface of a high-density debris flow.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. Who established the classic five-division turbidite succession containing graded bedding at its base?</div>
        <div class="pq-ans">Answer: Arnold H. Bouma (1962, The Bouma Sequence: $T_a, T_b, T_c, T_d, T_e$)</div>
        <div class="pq-exp">The basal $T_a$ division is massive to normally graded sand deposited directly from the decelerating turbulent head.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is a flute cast?</div>
        <div class="pq-ans">Answer: An erosional sole mark formed when a turbulent vortex scoops out a hollow in soft mud, which is subsequently cast by the overlying sand.</div>
        <div class="pq-exp">Flute casts are primary erosional structures, not depositional structures.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What is a 'varve'?</div>
        <div class="pq-ans">Answer: A rhythmic, annually deposited couplet of thin sedimentary layers (light coarse silt in summer, dark organic clay in winter) in glacial lakes.</div>
        <div class="pq-exp">Varves are seasonal primary depositional structures used for precise geochronological dating.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is the fundamental difference between lamination and bedding?</div>
        <div class="pq-ans">Answer: Lamination is less than 1 cm ($< 10\text{ mm}$) thick; bedding is greater than 1 cm thick (McKee & Weir, 1953).</div>
        <div class="pq-exp">By standard geological convention, strata thicker than 1 cm are beds; thinner planar units are laminae.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. What structure forms when gas bubbles or water escape through a soft mud surface?</div>
        <div class="pq-ans">Answer: Pitted mud surfaces or pit-and-mound structures (spring pits).</div>
        <div class="pq-exp">Escaping gas bubbles burst at the surface, creating tiny circular crater-like pits.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. How does graded bedding confirm that a vertical bed of turbidites has NOT been overturned?</div>
        <div class="pq-ans">Answer: If coarse grains are at the lower stratigraphic contact and fine grains are toward the upper contact, the bed is in normal right-way-up position.</div>
        <div class="pq-exp">If the fine mud is at the bottom and coarse pebbles are at the top, the sequence is inverted (overturned).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What sedimentary structure forms when a rapid flood carves a scoop into river sand and fills it with concave cross-strata?</div>
        <div class="pq-ans">Answer: Scour-and-fill structure</div>
        <div class="pq-exp">Scour-and-fill represents an initial erosional event followed immediately by deposition in the scoured depression.</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


# -----------------------------------------------------------------------------
# Q105: Coquina - Organic Detritus Limestone
# -----------------------------------------------------------------------------
def gen_q105():
    q_num = 105
    filename = "Q105_Limestone_Of_Organic_Detritus_Is_Coquina_Complete_Guide.html"
    title = "Q105: Carbonate Petrology - Coquina (Bioclastic Limestone)"
    badge = "OPSC 2019 Geology Paper-II • Question 105 • Sedimentary Petrology"
    h1_title = "Carbonate Petrology: Coquina, Bioclastic Limestones, and Shell Accumulations"
    meta_text = "<strong>Topic:</strong> Carbonate Rock Classification • <strong>Key Concept:</strong> Mechanically Sorted Organic Shell Debris • <strong>Textbooks:</strong> R.J. Dunham (1962); R.L. Folk (1962); K.M. Bangar (p. 138)"

    part1 = r"""
    <div class="card">
      <div class="card-title">1. Theoretical Foundation: Classification of Bioclastic Limestones</div>
      <p>Limestones ($\text{CaCO}_3$) are divided genetically into <strong>allochemical (clastic/detrital)</strong>, <strong>autochthonous organic (biogenic reefal)</strong>, and <strong>orthochemical (chemically precipitated)</strong> rocks. A limestone composed almost entirely (typically $> 75\%$ by volume) of coarse, mechanically sorted, broken or whole <strong>organic detritus</strong> (shells of molluscs, brachiopods, corals, and skeletal debris) is defined as a <strong>Coquina</strong>:</p>
      
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Limestone Variety</th>
              <th>Dominant Allochem / Mineral Constituent</th>
              <th>Genetic Mechanism</th>
              <th>High-Yield Distinguishing Feature</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;">
              <td><strong>COQUINA</strong> (Option B)</td>
              <td><strong>Coarse Organic Shell Detritus (&gt; 75%)</strong> (bivalves, gastropods, brachiopods).</td>
              <td>Mechanical accumulation and winnowing in high-energy littoral / beach surf zones.</td>
              <td><strong>Loosely cemented, highly porous aggregate of seashell fragments</strong>; completely bioclastic.</td>
            </tr>
            <tr>
              <td>Coquinite</td>
              <td>Organic Shell Detritus (&gt; 75%)</td>
              <td>Complete deep burial cementation of coquina.</td>
              <td>Firm, thoroughly indurated, dense equivalent of coquina with occluded porosity.</td>
            </tr>
            <tr>
              <td>Oolite / Oolitic Limestone (Option C)</td>
              <td><strong>Ooids (Ooliths)</strong> (spherical concentric grains, &lt; 2 mm).</td>
              <td>Inorganic chemical precipitation around a nucleus in agitated, warm, supersaturated shallows.</td>
              <td>Concentric radial carbonate lamination around quartz or shell seed; non-skeletal.</td>
            </tr>
            <tr>
              <td>Spergenite (Option A)</td>
              <td>Ooids + Endothyrid foraminifera + Microfossil debris.</td>
              <td>Shallow marine calcarenite (Bedford / Indiana limestone).</td>
              <td>Fine-grained bioclastic-oolitic freestone with excellent dimension stone properties.</td>
            </tr>
            <tr>
              <td>Calc-Tufa / Travertine (Option D)</td>
              <td>Microcrystalline calcite precipitated around plant matter.</td>
              <td>Inorganic freshwater precipitation from springs, streams, or waterfalls.</td>
              <td>Spongy, cellular, highly vesicular texture preserving plant leaf impressions.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="quote-box">
        "A limestone which consists predominantly of mechanically sorted, broken or whole <strong>organic detritus</strong> (especially shells of bivalves, gastropods, and brachiopods) held together by a small amount of calcite cement is called a <strong>coquina</strong>. In modern beach environments, such as along the coast of Florida, coquina forms porous deposits of shell gravel. When thoroughly cemented and hardened into a solid rock, it is termed coquinite."
        <div class="quote-author">&mdash; K.M. Bangar, <em>Principles of Engineering Geology</em> (Sedimentary Rocks, p. 138)</div>
      </div>

      <div class="formula-box">
        $$\text{Folk (1962) Classification: } \mathbf{Coquina} \equiv \text{Biosparite / Rudstone composed of } > \mathbf{75\%\ Shell\ Debris\ (Organic\ Detritus)}$$
        $$\text{Dunham (1962) Classification: Grain-Supported, Mud-Free Carbonate } \equiv \mathbf{Grainstone / Rudstone (Option\ B)}$$
      </div>

      <div class="figure-container">
        <img src="../../figures_2019_Q105/coquina_fossiliferous_organic_detritus_limestone.png" alt="Coquina Organic Detritus Limestone" class="figure-img">
        <div class="figure-caption">Figure 105: Anatomy of Coquina: a bioclastic allochemical limestone formed almost exclusively of loosely cemented broken molluscan shell fragments and organic skeletal debris.</div>
      </div>
    </div>
    """

    part2 = r"""
    <div class="card">
      <div class="card-title">2. Official Examination Question & Forensic Option Analysis</div>
      <div class="raw-question">
        <div class="raw-q-num">QUESTION 105</div>
        <div class="raw-q-text">A limestone which contains mainly of organic detritus is generally called as :</div>
        <div class="raw-options">
          <div class="raw-opt"><span class="opt-letter">A</span> Spergenite</div>
          <div class="raw-opt"><span class="opt-letter">B</span> Coquina</div>
          <div class="raw-opt"><span class="opt-letter">C</span> Oolite</div>
          <div class="raw-opt"><span class="opt-letter">D</span> Calc-tufa</div>
        </div>
      </div>

      <div class="ans-banner">
        CORRECT ANSWER: OPTION B (Coquina)
      </div>

      <div class="option-grid">
        <div class="option-card correct">
          <div class="opt-tag">OPTION B &bull; CORRECT</div>
          <div class="opt-title">Coquina</div>
          <p>By universal consensus in carbonate petrology (Dunham, 1962; Folk, 1962; Bangar, p. 138), a limestone composed predominantly or entirely of <strong>organic detritus</strong> (broken seashells, mollusc valves, and skeletal debris) is formally termed a <strong>coquina</strong> (from the Spanish word for cockle or small shell).</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION A &bull; DISTRACTOR</div>
          <div class="opt-title">Spergenite</div>
          <p>Spergenite (or Salem/Bedford limestone) is a specific Mississippian calcarenite composed of dwarf foraminifera (<em>Endothyra</em>) and micro-ooids in sparite, not coarse organic shell debris.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION C &bull; DISTRACTOR</div>
          <div class="opt-title">Oolite</div>
          <p>Oolite is a limestone composed of <strong>inorganic ooids</strong> (spherical sand-sized grains with concentric cortical laminae precipitated around nuclei), which are chemical in origin rather than skeletal organic detritus.</p>
        </div>

        <div class="option-card wrong">
          <div class="opt-tag">OPTION D &bull; DISTRACTOR</div>
          <div class="opt-title">Calc-tufa</div>
          <p>Calc-tufa is a porous, spongy, freshwater calcium carbonate deposit chemically precipitated around springs, waterfalls, and lake margins by the loss of carbon dioxide, not a marine accumulation of organic detritus.</p>
        </div>
      </div>
    </div>
    """

    part3 = r"""
    <div class="card">
      <div class="card-title">3. Synthesis Comparison & Exam-Standard Practice Problems</div>
      <div class="table-wrap">
        <table class="data-table">
          <thead>
            <tr>
              <th>Carbonate Rock</th>
              <th>Constituent Allochems</th>
              <th>Depositional Hydrodynamics</th>
              <th>Folk (1962) Equivalent</th>
              <th>Dunham (1962) Equivalent</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background:#fef2f2; font-weight:700;"><td><strong>Coquina (Option B)</strong></td><td><strong>Shell fragments / Bioclasts (&gt;75%)</strong></td><td>High-energy littoral beach surf</td><td>Biosparrudite</td><td>Grainstone / Rudstone</td></tr>
            <tr><td>Oolitic Limestone (Option C)</td><td>Concentric spherical Ooids (&gt;50%)</td><td>Agitated shoals & tidal bars</td><td>Oosparite</td><td>Grainstone</td></tr>
            <tr><td>Micrite (Lithographic)</td><td>Microcrystalline carbonate mud (&lt;4 $\mu\text{m}$)</td><td>Quiet protected lagoons / deep shelf</td><td>Micrite</td><td>Mudstone</td></tr>
            <tr><td>Chalk</td><td>Coccolithophore nannofossils</td><td>Pelagic oceanic suspension</td><td>Biomicrite</td><td>Wackestone / Mudstone</td></tr>
            <tr><td>Calc-Tufa (Option D)</td><td>Chemical freshwater precipitate</td><td>Inorganic spring precipitation</td><td>Travertine</td><td>Boundstone / Non-marine</td></tr>
          </tbody>
        </table>
      </div>

      <div class="card-title" style="margin-top:24px;">High-Yield Practice Problems (8 Exam-Standard Questions)</div>
      
      <div class="pq-item">
        <div class="pq-q">1. From which language is the word 'coquina' derived and what does it literally mean?</div>
        <div class="pq-ans">Answer: Spanish (meaning 'cockle' or 'shellfish').</div>
        <div class="pq-exp">Spanish settlers in St. Augustine, Florida, quarried this shell rock in the 17th century to build Castillo de San Marcos.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">2. What is the Dunham (1962) classification term for a grain-supported limestone containing less than 1% mud?</div>
        <div class="pq-ans">Answer: Grainstone</div>
        <div class="pq-exp">Dunham categorized limestones by fabric: Mudstone (&lt;10% grains), Wackestone (&gt;10% grains, mud-supported), Packstone (grain-supported with mud), Grainstone (grain-supported, mud-free).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">3. What is the difference between an ooid and a pisoid?</div>
        <div class="pq-ans">Answer: Ooids are less than 2 mm in diameter; pisoids are greater than 2 mm in diameter.</div>
        <div class="pq-exp">Pisoids form in calcretes, soils, and hypersaline lagoons, displaying larger concentric laminae.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">4. What soft, white, porous, friable limestone is composed almost entirely of microscopic calcareous algae (coccoliths)?</div>
        <div class="pq-ans">Answer: Chalk (e.g., White Cliffs of Dover, UK)</div>
        <div class="pq-exp">Chalk is an ultra-fine biomicrite composed of disarticulated calcite plates (coccoliths) secreted by planktonic haptophyte algae.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">5. What is a calcarenite?</div>
        <div class="pq-ans">Answer: A limestone consisting of sand-sized (1/16 mm to 2 mm) carbonate allochems (bioclasts, ooids, or peloids).</div>
        <div class="pq-exp">Calcarenite is the carbonate equivalent of sandstone; coarser is calcrudite; finer is calcilutite.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">6. Why were cannonballs fired at the coquina walls of Castillo de San Marcos in 1702 unable to breach the fortress?</div>
        <div class="pq-ans">Answer: Because the porous, compressible shell fabric of coquina absorbed the kinetic energy like dense foam, embedding the cannonballs without shattering.</div>
        <div class="pq-exp">The high porosity and interlocking shell fragments gave coquina remarkable shock-absorbing engineering resilience.</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">7. What is an intraclast in Folk's carbonate classification?</div>
        <div class="pq-ans">Answer: A fragment of semi-consolidated carbonate sediment ripped up from within the same basin and redeposited.</div>
        <div class="pq-exp">Intraclasts are carbonate equivalents of clay galls (intrasparite or packstone/rudstone).</div>
      </div>

      <div class="pq-item">
        <div class="pq-q">8. What is a peloid (or fecal pellet)?</div>
        <div class="pq-ans">Answer: An ovoid, structureless grain of microcrystalline carbonate mud produced predominantly by the fecal excretion of invertebrate organisms.</div>
        <div class="pq-exp">Gastropods and crustaceans ingest carbonate mud and excrete peloids that form peloidal limestones (pelsparite).</div>
      </div>
    </div>
    """

    generate_page(q_num, filename, title, badge, h1_title, meta_text, part1, part2, part3)


if __name__ == "__main__":
    print("Generating Masterclass Batch 8 Part B (Q099 - Q105)...")
    gen_q099()
    gen_q0100()
    gen_q101()
    gen_q102()
    gen_q103()
    gen_q104()
    gen_q105()
    print("Batch 8 Part B successfully generated!")
