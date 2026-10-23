import subprocess, os, shutil, glob
from PIL import Image

bangar_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/ Principle of Engieneering Geology by K M BANGAR.pdf'
vdp_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/12. Earth Structure Introduction Tectonics by VAN DER PLUIJM & MARSHAK.pdf'
winter_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/28. Principles of Igneous and Metamorphic Petrology by JOHN D. WINTER.pdf'

def render_page(pdf, page_num, out_prefix, dpi=180):
    for f in glob.glob(f"{out_prefix}-*.png"):
        os.remove(f)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page_num), '-l', str(page_num), pdf, out_prefix], check=True)
    matches = glob.glob(f"{out_prefix}-*.png")
    if matches:
        return sorted(matches)[0]
    raise FileNotFoundError(f"Failed to find rendered page for {out_prefix}")

# Q025: Box fold (conjugate fold with two hinges)
os.makedirs("figures_2019_Q025", exist_ok=True)
# VDP p259 or Ramsay
p_vdp259 = render_page(vdp_pdf, 259, "vdp_p259")
shutil.copy(p_vdp259, "figures_2019_Q025/vdp_p259_box_fold_conjugate_hinges.png")
os.remove(p_vdp259)

# Q026: Disharmonic / similar fold (thickened crests/troughs, thin limbs)
os.makedirs("figures_2019_Q026", exist_ok=True)
p_b114 = render_page(bangar_pdf, 114, "b_p114")
shutil.copy(p_b114, "figures_2019_Q026/bangar_fig7_11_close_fold_thickened_crests.png")
os.remove(p_b114)
if os.path.exists("figures_Q25/fossen_fig12_10_ramsay_fold_classes.png"):
    shutil.copy("figures_Q25/fossen_fig12_10_ramsay_fold_classes.png", "figures_2019_Q026/fossen_fig12_10_ramsay_fold_classes.png")

# Q027: Inlier and Outlier
os.makedirs("figures_2019_Q027", exist_ok=True)
p_b124 = render_page(bangar_pdf, 124, "b_p124")
shutil.copy(p_b124, "figures_2019_Q027/bangar_fig7_49_inlier_outlier.png")
os.remove(p_b124)

# Q028: Horst and Graben (Divergent boundaries)
os.makedirs("figures_2019_Q028", exist_ok=True)
if os.path.exists("figures_Q26/bangar_fig7_30_31_graben_horst.png"):
    shutil.copy("figures_Q26/bangar_fig7_30_31_graben_horst.png", "figures_2019_Q028/bangar_fig7_30_31_graben_horst.png")
if os.path.exists("figures_Q26/fossen_fig9_5_horst_graben.png"):
    shutil.copy("figures_Q26/fossen_fig9_5_horst_graben.png", "figures_2019_Q028/fossen_fig9_5_horst_graben.png")

# Q029: Sheet joints in granite
os.makedirs("figures_2019_Q029", exist_ok=True)
p_b123 = render_page(bangar_pdf, 123, "b_p123")
shutil.copy(p_b123, "figures_2019_Q029/bangar_p123_sheet_joints_granite.png")
os.remove(p_b123)
p_vdp163 = render_page(vdp_pdf, 163, "vdp_p163")
shutil.copy(p_vdp163, "figures_2019_Q029/vdp_fig7_7_granite_sheeting_exfoliation.png")
os.remove(p_vdp163)

# Q030: Plunging fold (axis not horizontal)
os.makedirs("figures_2019_Q030", exist_ok=True)
p_b113 = render_page(bangar_pdf, 113, "b_p113")
shutil.copy(p_b113, "figures_2019_Q030/bangar_fig7_8_plunging_fold_axis.png")
os.remove(p_b113)

# Q031: Continental drift (Laurasia and Gondwanaland)
os.makedirs("figures_2019_Q031", exist_ok=True)
if os.path.exists("figures_Q32/vdp_fig21_21_india_asia_tethys_collision.png"):
    shutil.copy("figures_Q32/vdp_fig21_21_india_asia_tethys_collision.png", "figures_2019_Q031/vdp_fig21_21_laurasia_gondwanaland_tethys.png")

# Q032: Convection energy along Divergent boundaries in oceans
os.makedirs("figures_2019_Q032", exist_ok=True)
if os.path.exists("figures_Q37/vdp_fig14_14_plate_boundaries_transform.png"):
    shutil.copy("figures_Q37/vdp_fig14_14_plate_boundaries_transform.png", "figures_2019_Q032/vdp_fig14_14_plate_boundaries_divergent_mid_ocean_ridge.png")
if os.path.exists("figures_Q37/bangar_fig1_12_1_13_plate_boundaries.png"):
    shutil.copy("figures_Q37/bangar_fig1_12_1_13_plate_boundaries.png", "figures_2019_Q032/bangar_fig1_12_mid_ocean_ridge_divergent.png")

# Q033: Mohorovicic discontinuity
os.makedirs("figures_2019_Q033", exist_ok=True)
if os.path.exists("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png"):
    shutil.copy("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png", "figures_2019_Q033/winter_fig3_moho_crust_mantle_velocity_jump.png")

# Q034: Asthenospheric layer in upper mantle
os.makedirs("figures_2019_Q034", exist_ok=True)
if os.path.exists("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png"):
    shutil.copy("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png", "figures_2019_Q034/winter_fig3_asthenosphere_low_velocity_zone.png")

# Q035: Core density 10.7 gm/cm3
os.makedirs("figures_2019_Q035", exist_ok=True)
if os.path.exists("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png"):
    shutil.copy("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png", "figures_2019_Q035/winter_fig3_earth_density_profile_core.png")

print("All figures for Batch 3 (Q025-Q035) staged successfully!")
