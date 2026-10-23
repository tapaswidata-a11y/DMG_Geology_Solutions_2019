import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def create_figure(q_dir, filename, draw_func):
    os.makedirs(q_dir, exist_ok=True)
    filepath = os.path.join(q_dir, filename)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    draw_func(ax)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300)
    plt.close()
    print(f"Generated: {filepath}")

# Q076: Acid Igneous Rocks - Total Silica vs Free Quartz
def draw_q076(ax):
    categories = ['Ultrabasic', 'Basic', 'Intermediate', 'Acidic']
    silica_ranges = [38, 48.5, 59, 72] # midpoints
    silica_err_low = [38-30, 48.5-45, 59-52, 72-66]
    silica_err_high = [45-38, 52-48.5, 66-59, 78-72]
    free_quartz = [0, 0, 4, 25] # modal free quartz

    x = np.arange(len(categories))
    width = 0.35

    rects1 = ax.bar(x - width/2, silica_ranges, width, label='Total Silica (SiO2 wt%)', color='#3b82f6', edgecolor='#1d4ed8')
    rects2 = ax.bar(x + width/2, free_quartz, width, label='Modal Free Quartz (vol%)', color='#f59e0b', edgecolor='#b45309')

    ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
    ax.set_title('Q076: Chemical & Mineralogical Classification of Igneous Rocks\nTotal Silica Content vs. Modal Free Quartz', fontsize=14, fontweight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=11, fontweight='bold')
    ax.legend(fontsize=11, loc='upper left')
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Highlight Acid threshold
    ax.axhline(10, color='#dc2626', linestyle=':', linewidth=2, label='Min Free Quartz in Acid Rocks (>=10%)')
    ax.text(2.6, 12, 'Acid Rocks: >= 10% Free Quartz\n(Total SiO2 > 66%)', color='#dc2626', fontweight='bold', fontsize=10, bbox=dict(facecolor='#fee2e2', edgecolor='#dc2626', boxstyle='round,pad=0.5'))

    for r in rects1:
        h = r.get_height()
        ax.annotate(f'{h:.1f}%', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')
    for r in rects2:
        h = r.get_height()
        ax.annotate(f'{h:.0f}%', xy=(r.get_x() + r.get_width()/2, h), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

create_figure('figures_2019_Q076', 'acid_intermediate_basic_ultrabasic_quartz_silica.png', draw_q076)

# Q077: Andesite - Intermediate Volcanic Rock
def draw_q077(ax):
    ax.set_xlim(35, 80)
    ax.set_ylim(0, 16)
    ax.set_xlabel('Silica Content (SiO2 wt%)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Alkalis (Na2O + K2O wt%)', fontsize=12, fontweight='bold')
    ax.set_title('Q077: TAS (Total Alkali-Silica) Classification Field\nAndesite: Intermediate Extrusive Volcanic Rock (52 - 63 wt% SiO2)', fontsize=13, fontweight='bold', pad=15)

    # TAS simplified fields
    # Basalt (45-52, 0-5)
    ax.add_patch(patches.Rectangle((45, 1), 7, 4, facecolor='#cbd5e1', edgecolor='#475569', alpha=0.7))
    ax.text(48.5, 3, 'BASALT\n(Basic)', ha='center', va='center', fontweight='bold', fontsize=10)

    # Andesite (52-63, 1-6) - Highlighted
    ax.add_patch(patches.Rectangle((52, 1.5), 11, 4.5, facecolor='#fde047', edgecolor='#ca8a04', linewidth=2.5, alpha=0.9))
    ax.text(57.5, 3.75, 'ANDESITE\n(Intermediate Volcanic)\n52-63% SiO2\nExtrusive = Diorite', ha='center', va='center', fontweight='bold', fontsize=11, color='#854d0e')

    # Dacite & Rhyolite
    ax.add_patch(patches.Rectangle((63, 2), 7, 5, facecolor='#fed7aa', edgecolor='#ea580c', alpha=0.7))
    ax.text(66.5, 4.5, 'DACITE\n(Acidic)', ha='center', va='center', fontweight='bold', fontsize=10)

    ax.add_patch(patches.Rectangle((70, 3), 9, 6, facecolor='#fbcfe8', edgecolor='#db2777', alpha=0.7))
    ax.text(74.5, 6, 'RHYOLITE\n(Acidic)', ha='center', va='center', fontweight='bold', fontsize=10)

    # Volcanic vs Plutonic Table
    cell_text = [
        ['Composition', 'Plutonic (Intrusive)', 'Hypabyssal', 'Volcanic (Extrusive)'],
        ['Acidic (>66% SiO2)', 'Granite', 'Quartz Porphyry', 'Rhyolite'],
        ['Intermediate (52-66%)', 'Diorite', 'Microdiorite', 'ANDESITE (Correct: C)'],
        ['Basic (45-52%)', 'Gabbro', 'Dolerite', 'Basalt'],
        ['Ultrabasic (<45%)', 'Peridotite', 'Picrite', 'Komatiite']
    ]
    tab = ax.table(cellText=cell_text, loc='upper left', bbox=[0.05, 0.55, 0.45, 0.4], cellLoc='center')
    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    tab.scale(1, 1.3)
    tab[(2, 3)].set_facecolor('#fef08a')

    ax.grid(True, linestyle=':', alpha=0.6)

create_figure('figures_2019_Q077', 'andesite_intermediate_volcanic_rock_tas_qapf.png', draw_q077)

# Q078: Bowen's Reaction Series - Calcic Plagioclase
def draw_q078(ax):
    ax.axis('off')
    ax.set_title("Q078: Bowen's Reaction Principle (1928)\nContinuous vs. Discontinuous Reaction Series", fontsize=14, fontweight='bold', pad=20)

    # Temperature Arrow
    ax.annotate('', xy=(0.08, 0.1), xytext=(0.08, 0.9), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=4))
    ax.text(0.04, 0.88, 'HIGH TEMP\n(~1200°C)\nEarly Crystals', color='#dc2626', fontweight='bold', fontsize=9, ha='center')
    ax.text(0.04, 0.12, 'LOW TEMP\n(~600°C)\nLate Crystals', color='#2563eb', fontweight='bold', fontsize=9, ha='center')

    # Discontinuous Series (Left)
    ax.text(0.3, 0.92, 'DISCONTINUOUS SERIES\n(Fe-Mg Silicates)', fontweight='bold', fontsize=11, ha='center', color='#047857')
    disc = [('Olivine (Mg-rich Forsterite)', 0.82), ('Pyroxene (Augite/Enstatite)', 0.68), ('Amphibole (Hornblende)', 0.54), ('Biotite Mica', 0.40)]
    for name, y in disc:
        ax.text(0.3, y, name, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.5', facecolor='#d1fae5', edgecolor='#059669', lw=1.5), fontweight='bold', fontsize=9.5)
        if y > 0.40:
            ax.annotate('', xy=(0.3, y-0.08), xytext=(0.3, y-0.04), arrowprops=dict(arrowstyle="->", color='#047857', lw=2))

    # Continuous Series (Right) - Highlighted
    ax.text(0.75, 0.92, 'CONTINUOUS SERIES\n(Feldspar Solid Solution)', fontweight='bold', fontsize=11, ha='center', color='#b45309')
    cont = [
        ('CALCIC PLAGIOCLASE (Anorthite 100-90% An)\n★ FIRST FORMED (Option D) ★', 0.82, '#fef08a', '#ca8a04', True),
        ('Bytownite (An90-70) -> Labradorite (An70-50)', 0.68, '#ffedd5', '#ea580c', False),
        ('Andesine (An50-30) -> Oligoclase (An30-10)', 0.54, '#fef3c7', '#d97706', False),
        ('SODIC PLAGIOCLASE (Albite An10-0%)\n(Last formed plagioclase)', 0.40, '#fed7aa', '#c2410c', False)
    ]
    for item in cont:
        name, y, fc, ec, bold_border = item
        lw = 2.5 if bold_border else 1.2
        ax.text(0.75, y, name, ha='center', va='center', bbox=dict(boxstyle='round,pad=0.5', facecolor=fc, edgecolor=ec, lw=lw), fontweight='bold', fontsize=9.5)
        if y > 0.40:
            ax.annotate('', xy=(0.75, y-0.08), xytext=(0.75, y-0.04), arrowprops=dict(arrowstyle="->", color='#b45309', lw=2))

    # Converging Residual System
    ax.text(0.52, 0.28, 'Potash Feldspar (Orthoclase / Microcline)', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#e0e7ff', edgecolor='#4338ca'), fontweight='bold', fontsize=9.5)
    ax.text(0.52, 0.18, 'Muscovite Mica', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#f3e8ff', edgecolor='#7e22ce'), fontweight='bold', fontsize=9.5)
    ax.text(0.52, 0.08, 'QUARTZ (Final Crystallizate)', ha='center', va='center', bbox=dict(boxstyle='round,pad=0.4', facecolor='#fae8ff', edgecolor='#a21caf'), fontweight='bold', fontsize=10)

    ax.annotate('', xy=(0.52, 0.31), xytext=(0.3, 0.37), arrowprops=dict(arrowstyle="->", color='#475569', lw=1.5))
    ax.annotate('', xy=(0.52, 0.31), xytext=(0.75, 0.37), arrowprops=dict(arrowstyle="->", color='#475569', lw=1.5))

create_figure('figures_2019_Q078', 'bowen_reaction_series_continuous_calcic_plagioclase.png', draw_q078)

# Q079: Carbonatite - Magmatic Carbonate Rock & REE Mineralization
def draw_q079(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q079: Anatomy of an Alkaline-Carbonatite Magmatic Complex\nRich in Primary Carbonates (>50%) & World-Class REE / Niobium Reserves', fontsize=13, fontweight='bold', pad=15)

    # Country rock
    ax.fill([0, 10, 10, 0], [0, 0, 7, 7], color='#f1f5f9')
    ax.text(1, 6.3, 'Precambrian Country Gneiss / Granite', fontsize=9, fontweight='bold', color='#64748b')

    # Fenitization halo
    ax.fill([2.5, 7.5, 8.5, 1.5], [0, 0, 7, 7], color='#fed7aa', alpha=0.5)
    ax.text(1.8, 4.5, 'FENITIZATION\nAUREOLE\n(Alkali Metasomatism:\nAegirine + K-feldspar)', fontsize=8.5, fontweight='bold', color='#c2410c')

    # Alkaline silicate ring
    ax.fill([3.2, 6.8, 7.5, 2.5], [0, 0, 7, 7], color='#dcfce7')
    ax.text(3.3, 5.5, 'Ijolite - Nephelinite Syenite Ring', fontsize=8.5, fontweight='bold', color='#15803d')

    # Central Carbonatite Core
    ax.fill([4.2, 5.8, 6.2, 3.8], [0, 0, 7, 7], color='#fbcfe8', edgecolor='#be185d', lw=2)
    ax.text(5.0, 3.5, 'CENTRAL\nCARBONATITE\nCORE PLUG\n(>50% Modal Carbonate:\nCalcite, Dolomite, Ankerite)\n\n★ REE Minerals ★\nBastnasite, Monazite,\nPyrochlore (Nb-Ta)', ha='center', va='center', fontsize=9.5, fontweight='bold', color='#831843')

    # Key callout box
    box_text = (
        "IUGS Carbonatite Definition:\n"
        "• > 50% modal primary igneous carbonate minerals (Calcite sovite, Dolomite beforsite).\n"
        "• Enriched in LREEs (La, Ce, Pr, Nd), HFSEs (Nb, Ta, Zr), P (Apatite), Ba, Sr, F.\n"
        "• Indian Type Locality: Amba Dongar Complex, Chhota Udepur district, Gujarat."
    )
    ax.text(0.5, 0.8, box_text, fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', edgecolor='#d97706'))

create_figure('figures_2019_Q079', 'carbonatite_magmatic_carbonate_ree_deposit.png', draw_q079)

# Q080: Charnockite Mineral Composition (Qtz - Feldspar - Hypersthene)
def draw_q080(ax):
    # Ternary representation
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_title('Q080: Charnockite Series Mineral Composition (Sir Thomas Holland, 1900)\nHypersthene (Orthopyroxene) + Quartz + Feldspar (Perthite & Plagioclase)', fontsize=13, fontweight='bold', pad=15)

    # Triangle vertices: Q (top), A (bottom left), P (bottom right)
    Q = np.array([0.5, 0.9])
    A = np.array([0.1, 0.1])
    P = np.array([0.9, 0.1])

    ax.plot([Q[0], A[0]], [Q[1], A[1]], 'k-', lw=1.5)
    ax.plot([A[0], P[0]], [A[1], P[1]], 'k-', lw=1.5)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', lw=1.5)

    ax.text(Q[0], Q[1]+0.04, 'QUARTZ (Q)', ha='center', fontweight='bold', fontsize=11, color='#2563eb')
    ax.text(A[0]-0.05, A[1]-0.04, 'ALKALI FELDSPAR (A)\n(K-Feldspar / Microperthite)', ha='center', fontweight='bold', fontsize=9.5, color='#d97706')
    ax.text(P[0]+0.05, P[1]-0.04, 'PLAGIOCLASE (P)\n(Oligoclase - Andesine)', ha='center', fontweight='bold', fontsize=9.5, color='#059669')

    # Charnockite Field (Center-top)
    ax.add_patch(patches.Polygon([[0.4, 0.55], [0.6, 0.55], [0.65, 0.35], [0.35, 0.35]], facecolor='#fef08a', edgecolor='#ca8a04', lw=2))
    ax.text(0.5, 0.45, 'CHARNOCKITE\n(s.s.)\nQtz + K-Feldspar +\nPlag + HYPERSTHENE', ha='center', va='center', fontweight='bold', fontsize=10, color='#854d0e')

    # Enderbite & Norite fields
    ax.text(0.72, 0.38, 'Enderbite\n(Plagioclase-rich)', fontsize=8.5, color='#047857', ha='center')
    ax.text(0.28, 0.38, 'Charnockite\n(Alkali-rich)', fontsize=8.5, color='#b45309', ha='center')

    # Key characteristics box
    desc = (
        "Essential Diagnostic Properties of Charnockite:\n"
        "1. Orthopyroxene (Hypersthene / Ferrohypersthene) is the ESSENTIAL mafic mineral.\n"
        "2. Waxy / greasy bluish-green or dark brownish resinous lustre (due to submicroscopic inclusions).\n"
        "3. High-grade metamorphic/granulite facies P-T condition (T: 750-900°C, P: 5-10 kbar, low a_H2O).\n"
        "4. Type Locality: St. Thomas Mount, Pallavaram, Chennai, Tamil Nadu."
    )
    ax.text(0.5, -0.05, desc, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f0fdf4', edgecolor='#16a34a'))

create_figure('figures_2019_Q080', 'charnockite_hypersthene_granite_mineralogy_qapf.png', draw_q080)

# Q081: Diorite Mafic Content - Perkinite (100% Ferromagnesian)
def draw_q081(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_title('Q081: Diorite Classification by Color Index (M = % Ferromagnesian Minerals)\nPerkinite: 90 - 100% Mafic (Hornblende + Pyroxene Ultramafic)', fontsize=13, fontweight='bold', pad=15)

    # Color index scale bar
    # 0 - 35% Leucodiorite
    ax.add_patch(patches.Rectangle((5, 5), 25, 2, facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))
    ax.text(17.5, 6, 'LEUCODIORITE\n(M = 0 - 35% Mafic)', ha='center', va='center', fontweight='bold', fontsize=9)

    # 35 - 65% Diorite (s.s.)
    ax.add_patch(patches.Rectangle((30, 5), 25, 2, facecolor='#cbd5e1', edgecolor='#475569', lw=1.5))
    ax.text(42.5, 6, 'DIORITE (s.s.)\n(M = 35 - 65% Mafic)', ha='center', va='center', fontweight='bold', fontsize=9)

    # 65 - 90% Meladiorite
    ax.add_patch(patches.Rectangle((55, 5), 20, 2, facecolor='#64748b', edgecolor='#334155', lw=1.5))
    ax.text(65, 6, 'MELADIORITE\n(M = 65 - 90%)', ha='center', va='center', fontweight='bold', fontsize=9, color='white')

    # 90 - 100% Perkinite
    ax.add_patch(patches.Rectangle((75, 5), 20, 2, facecolor='#1e293b', edgecolor='#dc2626', lw=2.5))
    ax.text(85, 6, '★ PERKINITE ★\n(M = 90 - 100%)\n(Option A)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#fef08a')

    # Arrows and explanations
    ax.text(50, 3.2, 'Diorite Plagioclase: Andesine / Oligoclase | Mafics: Hornblende, Biotite, Augite', ha='center', fontsize=10, fontweight='bold', color='#334155')

    def_box = (
        "Historical Petrographic Definition of Perkinite (Duparc, 1907; P.K. Mukherjee, p. 249):\n"
        "• An ultramafic coarse-grained rock composed essentially of Amphibole (hornblende) and Pyroxene.\n"
        "• Represents the 100% ferromagnesian extreme of the diorite / gabbro family (free of feldspar).\n"
        "• In classical Indian curricula, if ferromagnesian content of diorite is 100%, it is termed Perkinite."
    )
    ax.text(50, 1.2, def_box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee2e2', edgecolor='#ef4444'))

create_figure('figures_2019_Q081', 'diorite_perkinite_meladiorite_ultramafic_spectrum.png', draw_q081)

# Q082: Dolerite vs Basalt vs Gabbro Compositional Triad
def draw_q082(ax):
    ax.axis('off')
    ax.set_title('Q082: Compositional Equivalence of Dolerite, Basalt, and Gabbro\nIdentical Mafic Chemical Composition across Different Cooling Regimes', fontsize=13, fontweight='bold', pad=15)

    triad = [
        ('PLUTONIC (Intrusive)\nCoarse-grained (Phaneritic)\nDeep crustal plutons', 'GABBRO', 0.2, 0.65, '#dbeafe', '#1d4ed8'),
        ('HYPABYSSAL (Subvolcanic)\nMedium-grained (Diabasic/Ophitic)\nDykes & Sills', 'DOLERITE (Diabase)', 0.5, 0.65, '#fef08a', '#ca8a04'),
        ('VOLCANIC (Extrusive)\nFine-grained (Aphanitic)\nLava flows & Plateaus', 'BASALT (Option D)', 0.8, 0.65, '#fee2e2', '#b91c1c')
    ]

    for env, rock, x, y, fc, ec in triad:
        ax.text(x, y+0.12, env, ha='center', va='center', fontsize=9, fontweight='bold', color='#475569')
        ax.text(x, y, rock, ha='center', va='center', fontsize=11, fontweight='bold', bbox=dict(boxstyle='round,pad=0.6', facecolor=fc, edgecolor=ec, lw=2))

    # Bidirectional equivalence arrows
    ax.annotate('', xy=(0.32, 0.65), xytext=(0.38, 0.65), arrowprops=dict(arrowstyle="<->", color='#ca8a04', lw=2.5))
    ax.annotate('', xy=(0.62, 0.65), xytext=(0.68, 0.65), arrowprops=dict(arrowstyle="<->", color='#ca8a04', lw=2.5))

    comp_box = (
        "SHARED IDENTICAL MINERALOGICAL & CHEMICAL COMPOSITION:\n"
        "• Calcic Plagioclase (Labradorite An50-70 or Bytownite)\n"
        "• Clinopyroxene (Augite / Titanaugite / Pigeonite)\n"
        "• Fe-Ti Oxides (Magnetite, Ilmenite) +/- Olivine (in olivine-dolerite/basalt)\n"
        "• SiO2: 45 - 52 wt% (Basic / Mafic Igneous Chemistry)\n"
        "• Key Difference: TEXTURE (Dolerite = Ophitic/Subophitic, Basalt = Intersertal/Hyalopilitic, Gabbro = Granular)."
    )
    ax.text(0.5, 0.28, comp_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))

create_figure('figures_2019_Q082', 'dolerite_basalt_gabbro_compositional_equivalents.png', draw_q082)

# Q083: Beerbachite - Variety of Gabbro
def draw_q083(ax):
    ax.axis('off')
    ax.set_title('Q083: Beerbachite Petrography & Classification\nFine-Grained Granular Variety of Gabbro / Microgabbro', fontsize=13, fontweight='bold', pad=15)

    ax.text(0.5, 0.82, 'GABBRO FAMILY (Basic Plutonic / Hypabyssal)', ha='center', fontsize=12, fontweight='bold', color='#1e3a8a')

    varieties = [
        ('Norite\n(Orthopyroxene-rich)', 0.2, 0.65),
        ('Troctolite\n(Olivine + Plagioclase)', 0.4, 0.65),
        ('Anorthosite\n(>90% Plagioclase)', 0.6, 0.65),
        ('BEERBACHITE\n(Fine-grained Granular)\n★ (Option A) ★', 0.8, 0.65)
    ]
    for name, x, y in varieties:
        fc = '#fef08a' if 'BEERBACHITE' in name else '#e2e8f0'
        ec = '#ca8a04' if 'BEERBACHITE' in name else '#64748b'
        lw = 2 if 'BEERBACHITE' in name else 1
        ax.text(x, y, name, ha='center', va='center', fontsize=9.5, fontweight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=fc, edgecolor=ec, lw=lw))

    desc_box = (
        "Petrological Definition of Beerbachite (Chelius, 1892; IUGS Glossary):\n"
        "1. Named after Beerbach in the Odenwald, Germany.\n"
        "2. A fine-grained, granular microgabbro or pyroxene-granulite hornfels.\n"
        "3. Mineralogy: Granular calcic plagioclase (labradorite/bytownite) + pyroxene (diallage/hypersthene/augite) + magnetite.\n"
        "4. Exhibits saccharoidal (sugar-like) or granoblastic texture, occurring as dykes in gabbro or contact-metamorphosed basaltic walls."
    )
    ax.text(0.5, 0.35, desc_box, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f0fdf4', edgecolor='#16a34a', lw=1.5))

create_figure('figures_2019_Q083', 'beerbachite_microgabbro_hornfelsic_granular_texture.png', draw_q083)

# Q084: Adamellite (Quartz Monzonite) QAPF Diagram
def draw_q084(ax):
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.1, 1.1)
    ax.axis('off')
    ax.set_title('Q084: IUGS QAPF Classification of Granitoids: Adamellite (Field 3b / Quartz Monzonite)\nCharacterized by Roughly Equal Amounts of Oligoclase (Plagioclase) and K-Feldspar', fontsize=12.5, fontweight='bold', pad=15)

    Q = np.array([0.5, 0.9])
    A = np.array([0.1, 0.1])
    P = np.array([0.9, 0.1])

    ax.plot([Q[0], A[0]], [Q[1], A[1]], 'k-', lw=1.5)
    ax.plot([A[0], P[0]], [A[1], P[1]], 'k-', lw=1.5)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', lw=1.5)

    ax.text(Q[0], Q[1]+0.04, 'QUARTZ (Q = 20-60%)', ha='center', fontweight='bold', fontsize=10, color='#2563eb')
    ax.text(A[0]-0.05, A[1]-0.04, 'ALKALI FELDSPAR (A)\n(K-Feldspar)', ha='center', fontweight='bold', fontsize=9, color='#d97706')
    ax.text(P[0]+0.05, P[1]-0.04, 'PLAGIOCLASE (P)\n(Oligoclase)', ha='center', fontweight='bold', fontsize=9, color='#059669')

    # Adamellite field 3b (Center between A and P, with Q 20-60%)
    # P/(A+P) ratio between 35% and 65%
    ax.add_patch(patches.Polygon([[0.43, 0.55], [0.57, 0.55], [0.62, 0.25], [0.38, 0.25]], facecolor='#fef08a', edgecolor='#ca8a04', lw=2))
    ax.text(0.5, 0.40, 'ADAMELLITE\n(Quartz Monzonite)\n\nP / (A + P) = 35 - 65%\nRoughly EQUAL amounts of\nOligoclase & K-feldspar\n(Option A)', ha='center', va='center', fontweight='bold', fontsize=9.5, color='#854d0e')

    ax.text(0.28, 0.40, 'Syenogranite\n(K-feldspar > Plag)', fontsize=8.5, color='#b45309', ha='center')
    ax.text(0.72, 0.40, 'Granodiorite\n(Plag > K-feldspar)', fontsize=8.5, color='#047857', ha='center')

create_figure('figures_2019_Q084', 'adamellite_quartz_monzonite_qapf_diagram.png', draw_q084)

# Q085: Graphic Texture in Pegmatite
def draw_q085(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q085: Graphic (Runic) Texture in Granitic Pegmatite\nSimultaneous Eutectic Intergrowth of Quartz Rods in Host Microcline Feldspar', fontsize=12.5, fontweight='bold', pad=15)

    # Background host: Microcline / Orthoclase
    ax.add_patch(patches.Rectangle((1, 1.5), 8, 5.5, facecolor='#fef3c7', edgecolor='#b45309', lw=2))
    ax.text(1.3, 6.6, 'Host Mineral: Microcline / Alkali Feldspar (Pink / Buff)', fontsize=10, fontweight='bold', color='#92400e')

    # Angular quartz ichnoliths / runic characters
    chars = [
        [(2, 5), (2.4, 5.8), (2.2, 4.8)],
        [(3.5, 4.5), (3.8, 5.5), (4.2, 5.2), (3.9, 4.2)],
        [(5.2, 5.2), (5.8, 5.8), (5.5, 4.6), (6.0, 4.4)],
        [(7.0, 5.0), (7.5, 5.7), (7.8, 4.8)],
        [(2.5, 3.2), (3.0, 3.8), (3.4, 3.0)],
        [(4.5, 2.5), (5.0, 3.4), (5.4, 2.8), (4.8, 2.2)],
        [(6.5, 3.0), (7.0, 3.6), (7.3, 2.6)],
    ]
    for poly in chars:
        ax.add_patch(patches.Polygon(poly, facecolor='#93c5fd', edgecolor='#1d4ed8', lw=1.5))

    ax.text(5.0, 4.0, 'Quartz Rods / Skeletal Crystals\n(Resembling Cuneiform / Hebrew letters)', ha='center', fontsize=9.5, fontweight='bold', color='#1e40af')

    text_box = (
        "Key Petrological Facts (Bangar, p. 115; Winter, 2014):\n"
        "• Graphic texture is the classic diagnostic signature of granitic PEGMATITES.\n"
        "• Represents simultaneous crystallization at the eutectic minimum (~72% K-spar, ~28% Qtz).\n"
        "• Also known as 'runic texture' from resemblance to ancient Nordic runes."
    )
    ax.text(5.0, 0.7, text_box, ha='center', fontsize=9, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q085', 'graphic_texture_runic_pegmatite_eutectic.png', draw_q085)

# Q086: Laccolith vs Lopolith vs Bysmalith
def draw_q086(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title('Q086: Pluton Morphology: Concordant Igneous Intrusions\nLaccolith: Domed-Up Overlying Strata with a Flat Floor', fontsize=13, fontweight='bold', pad=15)

    # Sedimentary strata layers
    for y in [1.5, 2.5, 6.5, 7.2]:
        ax.plot([0.5, 9.5], [y, y], color='#94a3b8', linestyle='--', lw=1)

    # Laccolith (Left)
    # Domed up strata
    arc_x = np.linspace(1, 5, 100)
    arc_y = 2.5 + 2.5 * np.sin(np.pi * (arc_x - 1) / 4)
    ax.fill_between(arc_x, 2.5, arc_y, color='#fbcfe8', edgecolor='#be185d', lw=2)
    ax.plot(arc_x, arc_y, color='#be185d', lw=2)
    # Overlying strata arched
    ax.plot(arc_x, arc_y + 0.5, color='#475569', lw=1.5)
    ax.plot(arc_x, arc_y + 1.0, color='#475569', lw=1.5)
    # Feeder pipe
    ax.fill([2.8, 3.2, 3.2, 2.8], [0.5, 0.5, 2.5, 2.5], color='#fbcfe8', edgecolor='#be185d')

    ax.text(3.0, 3.6, 'LACCOLITH\n(Domed up roof,\nflat floor)\n★ (Option D) ★', ha='center', va='center', fontweight='bold', fontsize=10, color='#831843')

    # Lopolith (Right) - Saucer shaped
    saucer_x = np.linspace(5.5, 9.5, 100)
    saucer_y = 4.5 - 2.0 * np.sin(np.pi * (saucer_x - 5.5) / 4)
    ax.fill_between(saucer_x, saucer_y, 4.5, color='#fed7aa', edgecolor='#ea580c', lw=2)
    ax.plot(saucer_x, saucer_y, color='#ea580c', lw=2)
    ax.text(7.5, 3.6, 'LOPOLITH\n(Saucer-shaped,\nsagged floor & roof)', ha='center', va='center', fontweight='bold', fontsize=10, color='#9a3412')

    comp = (
        "Pluton Form Definitions (G.K. Gilbert, 1877; K.M. Bangar, p. 118):\n"
        "• Laccolith: Concordant body that arches/domes up overlying strata while retaining a flat floor.\n"
        "• Lopolith: Large concordant saucer-shaped intrusion with a depressed central basin (e.g., Bushveld).\n"
        "• Bysmalith: Cylindrical plug-like laccolith whose roof has been lifted by vertical boundary faults.\n"
        "• Phacolith: Crescentic intrusion occupying crests of anticlines or troughs of synclines."
    )
    ax.text(5.0, 0.7, comp, ha='center', fontsize=8.8, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q086', 'laccolith_vs_lopolith_bysmalith_pluton_morphology.png', draw_q086)

# Q087: Magmatic Stoping (R.A. Daly)
def draw_q087(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title("Q087: Mechanism of Pluton Emplacement: Magmatic Stoping (R.A. Daly, 1903)\nUpward Migration of Magma by Thermal Shattering and Sinking of Country Rock Blocks", fontsize=12.5, fontweight='bold', pad=15)

    # Country rock roof
    ax.fill([0, 10, 10, 0], [5.5, 5.5, 7.5, 7.5], color='#cbd5e1')
    ax.text(5.0, 7.0, 'Host Country Rock (Roof & Walls undergoing thermal jointing)', ha='center', fontweight='bold', fontsize=10)

    # Magma chamber
    ax.fill([0, 10, 10, 0], [0.5, 0.5, 5.5, 5.5], color='#fee2e2')
    ax.text(8.5, 3.5, 'Ascending\nMagma\nChamber', ha='center', fontweight='bold', fontsize=11, color='#b91c1c')

    # Stoping blocks (xenoliths detaching and sinking)
    blocks = [
        (2.5, 5.0, 'Detaching roof block'),
        (3.2, 3.8, 'Sinking xenolith'),
        (5.5, 4.6, 'Thermal fracture fragment'),
        (4.2, 2.2, 'Partially assimilated block'),
        (6.0, 1.2, 'Sunken floor restite')
    ]
    for x, y, label in blocks:
        ax.add_patch(patches.Rectangle((x-0.4, y-0.3), 0.8, 0.6, facecolor='#64748b', edgecolor='#334155', lw=1.5))
        ax.annotate('', xy=(x, y-0.6), xytext=(x, y-0.35), arrowprops=dict(arrowstyle="->", color='#dc2626', lw=2))

    ax.text(2.5, 2.8, 'Magmatic Stoping Process:\n1. Thermal fracturing of roof\n2. Magma penetrates joints\n3. Blocks (xenoliths) detach & sink\n4. Space opened for magma ascent', fontsize=9.5, fontweight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef3c7', edgecolor='#d97706'))

create_figure('figures_2019_Q087', 'magmatic_stoping_piecemeal_roof_shattering.png', draw_q087)

# Q088: Lamprophyre Classification - Minette
def draw_q088(ax):
    ax.axis('off')
    ax.set_title('Q088: Classification Matrix of Calc-Alkaline Lamprophyres\nMinette: Characterized by Essential Biotite / Phlogopite + Orthoclase (Alkali Feldspar)', fontsize=12.5, fontweight='bold', pad=15)

    cell_data = [
        ['Dominant Mafic Phenocryst', 'Predominant Alkali Feldspar (Orthoclase)', 'Predominant Plagioclase Feldspar'],
        ['BIOTITE / PHLOGOPITE', '★ MINETTE ★\n(Option D)\n(Biotite + Orthoclase)', 'KERSANTITE\n(Biotite + Plagioclase)'],
        ['HORNBLENDE / AMPHIBOLE\n(± Augite / Diopside)', 'VOGESITE\n(Hornblende + Orthoclase)', 'SPESSARTITE\n(Hornblende + Plagioclase)']
    ]
    tab = ax.table(cellText=cell_data, loc='center', cellLoc='center', bbox=[0.05, 0.35, 0.9, 0.5])
    tab.auto_set_font_size(False)
    tab.set_fontsize(9.5)
    tab.scale(1, 2.0)
    tab[(1, 1)].set_facecolor('#fef08a')
    tab[(0, 0)].set_facecolor('#e2e8f0')
    tab[(0, 1)].set_facecolor('#bae6fd')
    tab[(0, 2)].set_facecolor('#bbf7d0')

    notes = (
        "Characteristics of Lamprophyres (IUGS / Rock, 1991):\n"
        "• Porphyritic alkaline/subalkaline dyke rocks with mafic phenocrysts (NO felsic phenocrysts!).\n"
        "• Panidiomorphic texture (euhedral crystals of biotite, amphibole, or pyroxene).\n"
        "• Volatile-rich (H2O, CO2, F, Cl) with primary carbonates, apatite, and titanite."
    )
    ax.text(0.5, 0.15, notes, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#64748b'))

create_figure('figures_2019_Q088', 'lamprophyre_classification_minette_vogesite_kersantite.png', draw_q088)

# Q089: Palingenesis - Magmatic Melting of Crustal Rocks
def draw_q089(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_title("Q089: The Crustal Melting Cycle: Palingenesis & Anatexis (J.J. Sederholm, 1907)\n'Palingenesis': The Complete or Partial Remelting of Pre-Existing Rocks to Form Magma", fontsize=12.5, fontweight='bold', pad=15)

    steps = [
        ("1. Pre-existing Rock\n(Sediment / Metasediment)", 1.5, 5.5, '#e0f2fe', '#0284c7'),
        ("2. High-Grade Metamorphism\n(Amphibolite / Granulite)", 4.0, 5.5, '#dcfce7', '#16a34a'),
        ("3. Partial Melting (Anatexis)\nMigmatite (Leucosome+Melanosome)", 6.5, 5.5, '#fef08a', '#ca8a04'),
        ("4. PALINGENESIS\nComplete/Partial Remelting\n★ New Magma Born (Option D) ★", 9.0, 5.5, '#fee2e2', '#dc2626')
    ]
    for text, x, y, fc, ec in steps:
        ax.text(x, y, text, ha='center', va='center', fontsize=9, fontweight='bold', bbox=dict(boxstyle='round,pad=0.5', facecolor=fc, edgecolor=ec, lw=1.8))
        if x < 9.0:
            ax.annotate('', xy=(x+1.1, y), xytext=(x+0.6, y), arrowprops=dict(arrowstyle="->", color='#475569', lw=2))

    # Cyclic descent into deep crust
    palingenesis_desc = (
        "Etymology & Classical Concept (Sederholm, 1907; Eskola, 1932):\n"
        "• Greek 'palin' (again) + 'genesis' (birth) = 'Rebirth of Magma'.\n"
        "• Represents the plutonic process whereby deeply buried crustal rocks melt under extreme geothermal\n"
        "  gradients and volatile fluxing, generating S-type granitic plutons and batholiths.\n"
        "• Distinct from: Assimilation (contamination), Juvenile magmatism (mantle-derived virgin melt), Migmatization (rock hybrid)."
    )
    ax.text(5.0, 2.2, palingenesis_desc, ha='center', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8fafc', edgecolor='#64748b', lw=1.5))

create_figure('figures_2019_Q089', 'palingenesis_crustal_melting_anatexis_cycle.png', draw_q089)

# Q090: Liquid Immiscibility - Unmixing of Two Liquids of Different Composition
def draw_q090(ax):
    ax.set_xlim(0, 100)
    ax.set_ylim(800, 1500)
    ax.set_xlabel('Composition (% SiO2)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Temperature (°C)', fontsize=11, fontweight='bold')
    ax.set_title('Q090: Silicate Melt Liquid Immiscibility (Solvus Phenomenon)\nUnmixing of a Homogeneous Melt into Two Coexisting Liquids of Different Composition', fontsize=12.5, fontweight='bold', pad=15)

    # Solvus curve
    x_curve = np.linspace(20, 80, 100)
    # parabolic solvus peak at (50, 1350)
    y_curve = 1350 - 0.5 * (x_curve - 50)**2

    ax.plot(x_curve, y_curve, color='#dc2626', lw=2.5, label='Solvus (Two-Liquid Boundary)')
    ax.fill_between(x_curve, 800, y_curve, color='#fee2e2', alpha=0.6)

    ax.text(50, 1420, 'HOMOGENEOUS SINGLE LIQUID (L)', ha='center', fontweight='bold', fontsize=11, color='#1e3a8a')
    ax.text(50, 1100, 'TWO IMMISCIBLE LIQUIDS\n(L1 + L2)\nUnmixing into:\n• L1: Fe-rich / Carbonate Melt\n• L2: Si-rich / Felsic Melt', ha='center', va='center', fontweight='bold', fontsize=10.5, color='#991b1b')

    # Arrows indicating separation
    ax.annotate('', xy=(25, 1050), xytext=(45, 1150), arrowprops=dict(arrowstyle="->", color='#b91c1c', lw=2))
    ax.annotate('', xy=(75, 1050), xytext=(55, 1150), arrowprops=dict(arrowstyle="->", color='#b91c1c', lw=2))
    ax.text(25, 1000, 'L1 (Fe/Ca-rich)', ha='center', fontweight='bold', fontsize=9.5, color='#047857')
    ax.text(75, 1000, 'L2 (Si-rich)', ha='center', fontweight='bold', fontsize=9.5, color='#1d4ed8')

    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend(loc='upper right', fontsize=9.5)

create_figure('figures_2019_Q090', 'liquid_immiscibility_silicate_melt_phase_diagram.png', draw_q090)
