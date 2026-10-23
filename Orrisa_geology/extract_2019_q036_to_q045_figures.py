import subprocess, os, shutil, glob
from PIL import Image

bangar_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/ Principle of Engieneering Geology by K M BANGAR.pdf'
vdp_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/12. Earth Structure Introduction Tectonics by VAN DER PLUIJM & MARSHAK.pdf'
winter_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/28. Principles of Igneous and Metamorphic Petrology by JOHN D. WINTER.pdf'
boggs_pdf = '/home/tapaswi/Mines_Geology/TEXT_BOOK/principles-of-sedimentology-and-stratigraphy-by-sam-jr-boggs.pdf'

def render_page(pdf, page_num, out_prefix, dpi=180):
    for f in glob.glob(f"{out_prefix}-*.png"):
        os.remove(f)
    subprocess.run(['pdftoppm', '-png', '-r', str(dpi), '-f', str(page_num), '-l', str(page_num), pdf, out_prefix], check=True)
    matches = glob.glob(f"{out_prefix}-*.png")
    if matches:
        return sorted(matches)[0]
    raise FileNotFoundError(f"Failed to find rendered page for {out_prefix}")

# Q036: Weathering by exfoliation in massive rocks
os.makedirs("figures_2019_Q036", exist_ok=True)
if os.path.exists("figures_Q94/bangar_p20_spheroidal_weathering_exfoliation.png"):
    shutil.copy("figures_Q94/bangar_p20_spheroidal_weathering_exfoliation.png", "figures_2019_Q036/bangar_p20_exfoliation_weathering_massive_rocks.png")
if os.path.exists("figures_2019_Q029/bangar_p123_sheet_joints_granite.png"):
    shutil.copy("figures_2019_Q029/bangar_p123_sheet_joints_granite.png", "figures_2019_Q036/bangar_p123_massive_granite_exfoliation.png")

# Q037: Pelean type volcano (violent activity)
os.makedirs("figures_2019_Q037", exist_ok=True)
p_b49 = render_page(bangar_pdf, 49, "b_p49")
shutil.copy(p_b49, "figures_2019_Q037/bangar_p49_pelean_volcano_types.png")
os.remove(p_b49)

# Q038: Composite cones / Strato volcanoes
os.makedirs("figures_2019_Q038", exist_ok=True)
p_b48 = render_page(bangar_pdf, 48, "b_p48")
shutil.copy(p_b48, "figures_2019_Q038/bangar_p48_composite_stratovolcano.png")
os.remove(p_b48)

# Q039: Airy's theory of isostasy
os.makedirs("figures_2019_Q039", exist_ok=True)
if os.path.exists("figures_Q45/bangar_fig1_7_airy_isostasy.png"):
    shutil.copy("figures_Q45/bangar_fig1_7_airy_isostasy.png", "figures_2019_Q039/bangar_fig1_7_airy_isostasy_crustal_roots.png")
if os.path.exists("figures_Q45/vdp_fig14_12_isostasy_airy_concept.png"):
    shutil.copy("figures_Q45/vdp_fig14_12_isostasy_airy_concept.png", "figures_2019_Q039/vdp_fig14_12_isostasy_airy_concept.png")

# Q040: Atlantic continental margin of North America (Passive margin)
os.makedirs("figures_2019_Q040", exist_ok=True)
# VDP p437 / Boggs
p_vdp437 = render_page(vdp_pdf, 437, "vdp_p437")
shutil.copy(p_vdp437, "figures_2019_Q040/vdp_p437_atlantic_passive_continental_margin.png")
os.remove(p_vdp437)

# Q041: Average depth of ocean (3,729 m) / Ocean floor hypsography
os.makedirs("figures_2019_Q041", exist_ok=True)
p_b35 = render_page(bangar_pdf, 35, "b_p35")
shutil.copy(p_b35, "figures_2019_Q041/bangar_p35_ocean_depth_zones_shelf_abyssal.png")
os.remove(p_b35)

# Q042: Paleomagnetic data and pole reversals
os.makedirs("figures_2019_Q042", exist_ok=True)
p_vdp445 = render_page(vdp_pdf, 445, "vdp_p445")
shutil.copy(p_vdp445, "figures_2019_Q042/vdp_p445_paleomagnetic_pole_reversals_stripes.png")
os.remove(p_vdp445)

# Q043: Guyot (Flat topped seamount)
os.makedirs("figures_2019_Q043", exist_ok=True)
p_b36 = render_page(bangar_pdf, 36, "b_p36")
shutil.copy(p_b36, "figures_2019_Q043/bangar_p36_seamounts_guyots_trenches.png")
os.remove(p_b36)

# Q044: Deep sea trenches in Circum-Pacific belt
os.makedirs("figures_2019_Q044", exist_ok=True)
if os.path.exists("figures_Q37/global_mid_ocean_ridges_trenches_tectonic_map.png"):
    shutil.copy("figures_Q37/global_mid_ocean_ridges_trenches_tectonic_map.png", "figures_2019_Q044/global_circum_pacific_trenches_map.png")
p_b50 = render_page(bangar_pdf, 50, "b_p50")
shutil.copy(p_b50, "figures_2019_Q044/bangar_p50_subduction_trenches_ring_of_fire.png")
os.remove(p_b50)

# Q045: Temperature regime in lower crust (400-500°C)
os.makedirs("figures_2019_Q045", exist_ok=True)
if os.path.exists("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png"):
    shutil.copy("figures_Q39/winter_fig3_seismic_velocity_prem_profile.png", "figures_2019_Q045/winter_continental_geotherm_crustal_temperatures.png")

print("All figures for Batch 4 (Q036-Q045) staged successfully!")
