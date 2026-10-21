import subprocess, os, shutil, glob
from PIL import Image

winter_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/28. Principles of Igneous and Metamorphic Petrology by JOHN D. WINTER.pdf'
bangar_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/ Principle of Engieneering Geology by K M BANGAR.pdf'
boggs_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/principles-of-sedimentology-and-stratigraphy-by-sam-jr-boggs.pdf'
mahapatra_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/A text book of GEOLOGY by G.B.Mahapatra.pdf'

def render_page(pdf, page_num, out_prefix, dpi=180):
    for f in glob.glob(f"{out_prefix}-*.png"):
        os.remove(f)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page_num), '-l', str(page_num), pdf, out_prefix], check=True)
    matches = glob.glob(f"{out_prefix}-*.png")
    if matches:
        return sorted(matches)[0]
    raise FileNotFoundError(f"Failed to find rendered page for {out_prefix}")

# Q76: Winter Ch 10 (Primary magmas & partial melting controls)
print("Q76...")
os.makedirs("figures_Q76", exist_ok=True)
p_w10 = render_page(winter_pdf, 205, "w_p205") # Winter p205 (melting curve)
shutil.copy(p_w10, "figures_Q76/winter_p205_primary_magma_melting.png")
os.remove(p_w10)

# Q77: Bangar p56 & p77 (Ophitic texture & igneous structures)
print("Q77...")
os.makedirs("figures_Q77", exist_ok=True)
p_b77 = render_page(bangar_pdf, 77, "b_p77")
shutil.copy(p_b77, "figures_Q77/bangar_p77_igneous_textures_ophitic.png")
os.remove(p_b77)

# Q78: Winter Ch 2 (IUGS Foid rocks & Ijolite)
print("Q78...")
os.makedirs("figures_Q78", exist_ok=True)
p_w28 = render_page(winter_pdf, 28, "w_p28") # IUGS QAPF classification
shutil.copy(p_w28, "figures_Q78/winter_p28_iugs_plutonic_ijolite.png")
os.remove(p_w28)

# Q79: Bangar p77 (Myrmekite texture) & Winter Ch 3
print("Q79...")
os.makedirs("figures_Q79", exist_ok=True)
p_w45 = render_page(winter_pdf, 45, "w_p45") # Winter texture chapter
shutil.copy(p_w45, "figures_Q79/winter_p45_myrmekite_intergrowth_texture.png")
os.remove(p_w45)

# Q80: Mahapatra p140 / Bangar p83 (Charnockite composition)
print("Q80...")
os.makedirs("figures_Q80", exist_ok=True)
p_m80 = render_page(mahapatra_pdf, 140, "m_p140")
shutil.copy(p_m80, "figures_Q80/mahapatra_p140_charnockite_hypersthene.png")
os.remove(p_m80)

# Q81: Perthite and Antiperthite (Copy from Assam Q41 or render Winter p105)
print("Q81...")
os.makedirs("figures_Q81", exist_ok=True)
if os.path.exists('/home/tapaswi/Mines_Geology/figures_Q41/winter_fig16_feldspar_solvus_perthite.png'):
    shutil.copy('/home/tapaswi/Mines_Geology/figures_Q41/winter_fig16_feldspar_solvus_perthite.png', 'figures_Q81/winter_fig16_feldspar_solvus_perthite.png')

# Q82: Autometamorphism (Winter Ch 3 deuteric alteration)
print("Q82...")
os.makedirs("figures_Q82", exist_ok=True)
p_w48 = render_page(winter_pdf, 48, "w_p48")
shutil.copy(p_w48, "figures_Q82/winter_p48_deuteric_autometamorphic.png")
os.remove(p_w48)

# Q83: Main Central Thrust (MCT) - Van der Pluijm Fig 21.21
print("Q83...")
os.makedirs("figures_Q83", exist_ok=True)
if os.path.exists('figures_Q32/vdp_fig21_21_india_asia_tethys_collision.png'):
    shutil.copy('figures_Q32/vdp_fig21_21_india_asia_tethys_collision.png', 'figures_Q83/vdp_fig21_21_himalayan_mct.png')

# Q84: Bysmalith (Bangar p55: Intrusive forms)
print("Q84...")
os.makedirs("figures_Q84", exist_ok=True)
p_b55 = render_page(bangar_pdf, 55, "b_p55")
shutil.copy(p_b55, "figures_Q84/bangar_p55_bysmalith_laccolith_forms.png")
os.remove(p_b55)

# Q85: Lamprophyre Panidiomorphic texture (Winter p390 / Bangar p82)
print("Q85...")
os.makedirs("figures_Q85", exist_ok=True)
p_b82 = render_page(bangar_pdf, 82, "b_p82")
shutil.copy(p_b82, "figures_Q85/bangar_p82_lamprophyre_panidiomorphic.png")
os.remove(p_b82)

# Q86: Monomineralic ultrabasic rocks (Winter p29: Ultramafic rocks)
print("Q86...")
os.makedirs("figures_Q86", exist_ok=True)
p_w29 = render_page(winter_pdf, 29, "w_p29")
shutil.copy(p_w29, "figures_Q86/winter_p29_ultramafic_monomineralic_dunite.png")
os.remove(p_w29)

# Q87: Fergusite (Winter p30: Alkaline rocks table)
print("Q87...")
os.makedirs("figures_Q87", exist_ok=True)
shutil.copy("figures_Q78/winter_p28_iugs_plutonic_ijolite.png", "figures_Q87/winter_p28_fergusite_iugs_classification.png")

# Q88: Quartz Monzonite (Winter p28: QAPF field 8*)
print("Q88...")
os.makedirs("figures_Q88", exist_ok=True)
shutil.copy("figures_Q78/winter_p28_iugs_plutonic_ijolite.png", "figures_Q88/winter_p28_quartz_monzonite_qapf.png")

# Q89: Harzburgite (Winter p29: Ultramafic ternary Ol-Opx-Cpx)
print("Q89...")
os.makedirs("figures_Q89", exist_ok=True)
shutil.copy("figures_Q86/winter_p29_ultramafic_monomineralic_dunite.png", "figures_Q89/winter_p29_harzburgite_ultramafic_ternary.png")

# Q90: Andesite (Bangar p80: Intermediate volcanic rocks)
print("Q90...")
os.makedirs("figures_Q90", exist_ok=True)
p_b80 = render_page(bangar_pdf, 80, "b_p80")
shutil.copy(p_b80, "figures_Q90/bangar_p80_andesite_petrology.png")
os.remove(p_b80)

# Q91: Argillaceous sandstone (Boggs p145: Sandstone classification & cements)
print("Q91...")
os.makedirs("figures_Q91", exist_ok=True)
p_bg145 = render_page(boggs_pdf, 145, "bg_p145")
shutil.copy(p_bg145, "figures_Q91/boggs_p145_sandstone_cements_argillaceous.png")
os.remove(p_bg145)

# Q92: Shale fissility and laminations (Boggs p155: Shales & mudrocks)
print("Q92...")
os.makedirs("figures_Q92", exist_ok=True)
p_bg155 = render_page(boggs_pdf, 155, "bg_p155")
shutil.copy(p_bg155, "figures_Q92/boggs_p155_shale_laminar_structure_fissility.png")
os.remove(p_bg155)

# Q93: Clastic / Siliciclastic rocks (Boggs p130: Major clastic rock groups)
print("Q93...")
os.makedirs("figures_Q93", exist_ok=True)
p_bg130 = render_page(boggs_pdf, 130, "bg_p130")
shutil.copy(p_bg130, "figures_Q93/boggs_p130_siliciclastic_classification.png")
os.remove(p_bg130)

# Q94: Spheroidal weathering (Bangar p20)
print("Q94...")
os.makedirs("figures_Q94", exist_ok=True)
p_b20 = render_page(bangar_pdf, 20, "b_p20")
shutil.copy(p_b20, "figures_Q94/bangar_p20_spheroidal_weathering_exfoliation.png")
os.remove(p_b20)

# Q95: Karst topography & sinkholes (Bangar p30)
print("Q95...")
os.makedirs("figures_Q95", exist_ok=True)
p_b30 = render_page(bangar_pdf, 30, "b_p30")
shutil.copy(p_b30, "figures_Q95/bangar_p30_karst_topography_limestone.png")
os.remove(p_b30)

# Q96: Sedimentary Red Beds (Boggs p170: Red beds in arid continental basins)
print("Q96...")
os.makedirs("figures_Q96", exist_ok=True)
p_bg170 = render_page(boggs_pdf, 170, "bg_p170")
shutil.copy(p_bg170, "figures_Q96/boggs_p170_sedimentary_red_beds_arid.png")
os.remove(p_bg170)

# Q97: Chemical Sedimentary Rocks (Gypsum / Evaporites) (Boggs p215: Evaporites)
print("Q97...")
os.makedirs("figures_Q97", exist_ok=True)
if os.path.exists('/home/tapaswi/Mines_Geology/figures_Q65/boggs_table7_1_evaporite_salts.png'):
    shutil.copy('/home/tapaswi/Mines_Geology/figures_Q65/boggs_table7_1_evaporite_salts.png', 'figures_Q97/boggs_table7_1_chemical_evaporite_gypsum.png')
else:
    p_bg215 = render_page(boggs_pdf, 215, "bg_p215")
    shutil.copy(p_bg215, "figures_Q97/boggs_p215_chemical_evaporite_gypsum.png")
    os.remove(p_bg215)

# Q98: Diagenesis (Boggs p180: Diagenetic processes)
print("Q98...")
os.makedirs("figures_Q98", exist_ok=True)
p_bg180 = render_page(boggs_pdf, 180, "bg_p180")
shutil.copy(p_bg180, "figures_Q98/boggs_p180_diagenesis_stages.png")
os.remove(p_bg180)

# Q99: ZTR Index and Mineralogical Maturity (Boggs p140 / Hubert 1962)
print("Q99...")
os.makedirs("figures_Q99", exist_ok=True)
p_bg140 = render_page(boggs_pdf, 140, "bg_p140")
shutil.copy(p_bg140, "figures_Q99/boggs_p140_ztr_index_mineralogical_maturity.png")
os.remove(p_bg140)

# Q100: Granulometric Analysis (Boggs p60: Grain size analysis & sieving)
print("Q100...")
os.makedirs("figures_Q100", exist_ok=True)
p_bg60 = render_page(boggs_pdf, 60, "bg_p60")
shutil.copy(p_bg60, "figures_Q100/boggs_p60_granulometric_grain_size_analysis.png")
os.remove(p_bg60)

print("Batch 5 (Q76-Q100) figure extraction complete!")
