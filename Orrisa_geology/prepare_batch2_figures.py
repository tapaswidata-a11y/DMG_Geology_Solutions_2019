#!/usr/bin/env python3
"""
Prepare authentic textbook plates for 2019 Batch 2 (Q011 to Q024)
"""

import os
import shutil
import glob
import subprocess

BASE_DIR = "/home/tapaswi/Mines_Geology/Orrisa_geology"
bangar_pdf = "/home/tapaswi/Mines_Geology/TEXT_BOOK/ Principle of Engieneering Geology by K M BANGAR.pdf"
boggs_pdf = "/home/tapaswi/Mines_Geology/TEXT_BOOK/principles-of-sedimentology-and-stratigraphy-by-sam-jr-boggs.pdf"
billings_pdf = "/home/tapaswi/Mines_Geology/TEXT_BOOK/geokniga-structural-geology_1.pdf"

def render_page(pdf, page_num, out_prefix, dpi=180):
    for f in glob.glob(f"{out_prefix}-*.png"):
        os.remove(f)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page_num), '-l', str(page_num), pdf, out_prefix], check=True)
    matches = glob.glob(f"{out_prefix}-*.png")
    if matches:
        return sorted(matches)[0]
    raise FileNotFoundError(f"Failed to find rendered page for {out_prefix}")

for q in range(11, 25):
    os.makedirs(os.path.join(BASE_DIR, f"figures_2019_Q{q:03d}"), exist_ok=True)

# Q011: Sand dunes (Barchan, Transverse, Longitudinal)
print("Setting up figures for Q011...")
q11_dir = os.path.join(BASE_DIR, "figures_2019_Q011")
shutil.copy("figures_Q03/bangar_fig2_3_2_4_wind_transport.png", os.path.join(q11_dir, "bangar_fig2_3_2_4_wind_transport.png"))
shutil.copy("figures_2019_Q007/boggs_fig8_17_eolian_dune_types.png", os.path.join(q11_dir, "boggs_fig8_17_barchan_transverse_dunes.png"))

# Q012: Esker (Glaciofluvial deposit)
print("Setting up figures for Q012...")
q12_dir = os.path.join(BASE_DIR, "figures_2019_Q012")
shutil.copy("figures_2019_Q009/bangar_p32_glacial_moraines_till.png", os.path.join(q12_dir, "bangar_p32_esker_glaciofluvial.png"))
shutil.copy("figures_2019_Q009/boggs_fig8_32_glacial_moraine_deposits.png", os.path.join(q12_dir, "boggs_fig8_32_esker_subglacial_tunnel.png"))

# Q013: Stalactites & Stalagmites (Karst Solution)
print("Setting up figures for Q013...")
q13_dir = os.path.join(BASE_DIR, "figures_2019_Q013")
shutil.copy("figures_2019_Q010/bangar_p38_karst_topography_limestone.png", os.path.join(q13_dir, "bangar_p38_stalactite_stalagmite_solution.png"))

# Q014: Mass Wasting (Gravity)
print("Setting up figures for Q014...")
q14_dir = os.path.join(BASE_DIR, "figures_2019_Q014")
shutil.copy("figures_Q01/bangar_p378_landslides_verbatim_definition.png", os.path.join(q14_dir, "bangar_p378_mass_wasting_gravity.png"))
shutil.copy("figures_Q01/landslide_shear_plane_mechanics.png", os.path.join(q14_dir, "mass_wasting_gravity_shear_plane.png"))

# Q015: Dendritic Drainage (No structural control)
print("Setting up figures for Q015...")
q15_dir = os.path.join(BASE_DIR, "figures_2019_Q015")
shutil.copy("figures_2019_Q004/bangar_p27_trellis_drainage_pattern.png", os.path.join(q15_dir, "bangar_p27_dendritic_trellis_drainage.png"))

# Q016: Caldera (Volcanic collapse depression)
print("Setting up figures for Q016...")
q16_dir = os.path.join(BASE_DIR, "figures_2019_Q016")
p_b15 = render_page(bangar_pdf, 15, "b_p15")
shutil.copy(p_b15, os.path.join(q16_dir, "bangar_p15_caldera_crater_volcano.png"))
os.remove(p_b15)

# Q017: Fault Gouge & Rock Flour (Brittle deformation)
print("Setting up figures for Q017...")
q17_dir = os.path.join(BASE_DIR, "figures_2019_Q017")
p_b215 = render_page(bangar_pdf, 115, "b_p115")
shutil.copy(p_b215, os.path.join(q17_dir, "bangar_p115_fault_breccia_gouge_brittle.png"))
os.remove(p_b215)

# Q018: Hade of Fault Plane
print("Setting up figures for Q018...")
q18_dir = os.path.join(BASE_DIR, "figures_2019_Q018")
p_b110 = render_page(bangar_pdf, 110, "b_p110")
shutil.copy(p_b110, os.path.join(q18_dir, "bangar_p110_fault_elements_hade_dip.png"))
os.remove(p_b110)

# Q019: Normal Fault (Hanging wall downthrown)
print("Setting up figures for Q019...")
q19_dir = os.path.join(BASE_DIR, "figures_2019_Q019")
shutil.copy("figures_Q28/bangar_fig7_24_normal_reverse_faults.png", os.path.join(q19_dir, "bangar_fig7_24_normal_fault_hanging_wall.png"))
shutil.copy("figures_Q28/fossen_fig9_2_three_fault_regimes.png", os.path.join(q19_dir, "fossen_fig9_2_normal_fault_regime.png"))

# Q020: Fold Axis parallel to Hinge Line
print("Setting up figures for Q020...")
q20_dir = os.path.join(BASE_DIR, "figures_2019_Q020")
shutil.copy("figures_Q22/bangar_fig7_5_7_8_plunge_fold_axis.png", os.path.join(q20_dir, "bangar_fig7_5_fold_axis_hinge.png"))
shutil.copy("figures_Q24/fossen_fig12_1_fold_hinge_anatomy.png", os.path.join(q20_dir, "fossen_fig12_1_fold_hinge_anatomy.png"))

# Q021: Recumbent Fold (Horizontal axial plane)
print("Setting up figures for Q021...")
q21_dir = os.path.join(BASE_DIR, "figures_2019_Q021")
p_b98 = render_page(bangar_pdf, 98, "b_p98")
shutil.copy(p_b98, os.path.join(q21_dir, "bangar_p98_recumbent_fold_axial_plane.png"))
os.remove(p_b98)

# Q022: Blended Unconformity (Residual soil contact)
print("Setting up figures for Q022...")
q22_dir = os.path.join(BASE_DIR, "figures_2019_Q022")
shutil.copy("figures_Q29/boggs_fig12_5_four_unconformities.png", os.path.join(q22_dir, "boggs_fig12_5_unconformities_blended.png"))

# Q023: Intersection Lineation (Bedding & Cleavage)
print("Setting up figures for Q023...")
q23_dir = os.path.join(BASE_DIR, "figures_2019_Q023")
p_b125 = render_page(bangar_pdf, 125, "b_p125")
shutil.copy(p_b125, os.path.join(q23_dir, "bangar_p125_cleavage_foliation_lineation.png"))
os.remove(p_b125)

# Q024: High Angle Faults (>45 degrees)
print("Setting up figures for Q024...")
q24_dir = os.path.join(BASE_DIR, "figures_2019_Q024")
shutil.copy("figures_Q21/fossen_fig9_2_three_fault_regimes.png", os.path.join(q24_dir, "fossen_fig9_2_high_angle_vs_low_angle_faults.png"))

print("All Batch 2 figures (Q011 - Q024) staged successfully!")
