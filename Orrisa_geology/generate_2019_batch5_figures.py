import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs("figures_2019_Q046", exist_ok=True)
os.makedirs("figures_2019_Q047", exist_ok=True)
os.makedirs("figures_2019_Q048", exist_ok=True)
os.makedirs("figures_2019_Q049", exist_ok=True)
os.makedirs("figures_2019_Q050", exist_ok=True)
os.makedirs("figures_2019_Q051", exist_ok=True)
os.makedirs("figures_2019_Q052", exist_ok=True)
os.makedirs("figures_2019_Q053", exist_ok=True)
os.makedirs("figures_2019_Q054", exist_ok=True)
os.makedirs("figures_2019_Q055", exist_ok=True)
os.makedirs("figures_2019_Q056", exist_ok=True)
os.makedirs("figures_2019_Q057", exist_ok=True)
os.makedirs("figures_2019_Q058", exist_ok=True)
os.makedirs("figures_2019_Q059", exist_ok=True)
os.makedirs("figures_2019_Q060", exist_ok=True)

# -------------------------------------------------------------
# Q046: Dharwarian Stratigraphy & Closepet Granite (Youngest Event)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

units = [
    ("Closepet Granite (~2.51 Ga)", "Late-to-post-tectonic granite plutonism cutting across EDC & WDC\nMarks final cratonization & craton-wide stabilization event", "#ef4444", "YOUNGEST EVENT (Correct Answer B)"),
    ("Chitradurga Group (~2.7 - 2.6 Ga)", "Upper Dharwar Supergroup: BIF, greywackes, polymict conglomerates\nVolcanosedimentary greenstone succession", "#f59e0b", "Dharwar Supergroup (Upper)"),
    ("Bababudan Group (~3.0 - 2.7 Ga)", "Lower Dharwar Supergroup: Oligomict conglomerate, amygdaloidal basalt,\narenites, banded iron formations (BIF)", "#10b981", "Dharwar Supergroup (Lower)"),
    ("Peninsular Gneissic Complex (PGC, ~3.0 - 3.4 Ga)", "Polyphase migmatitic gneisses & tonalite-trondhjemite-granodiorite (TTG)\nForms crystalline basement floor for Dharwar Supergroup", "#3b82f6", "Basement Gneisses"),
    ("Sargur Group (~3.3 - 3.5 Ga)", "Oldest recognizable supracrustal relicts: Komatiites, pelites, kyanite-\nsillimanite schists, high-grade amphibolite/granulite enclaves", "#8b5cf6", "OLDEST SUPRACRUSTALS")
]

y_pos = 4.5
for name, desc, col, tag in units:
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.7), 9.0, 0.7, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, name, fontsize=12, fontweight="bold", color="white")
    ax.text(0.7, y_pos - 0.55, desc, fontsize=8.5, color="#f1f5f9")
    ax.text(9.3, y_pos - 0.25, tag, fontsize=9.5, fontweight="bold", color="#fef08a" if "YOUNGEST" in tag else "white", ha="right")
    y_pos -= 0.88

ax.annotate("", xy=(0.2, 4.5), xytext=(0.2, 0.7),
            arrowprops=dict(arrowstyle="->", color="#0f172a", lw=2.5))
ax.text(0.12, 2.6, "YOUNGERING DIRECTION (UPWARD)", rotation=90, fontsize=10, fontweight="bold", color="#0f172a", ha="center")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.0)
ax.axis("off")
plt.title("Dharwar Craton Lithostratigraphic Succession & Chronology (GSI / Ramakrishnan & Vaidyanadhan)", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q046/dharwar_craton_stratigraphy_closepet_granite.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q047: Stratigraphic Pairs: Cauvery Basin & Niniyur Formation
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

stages = [
    ("Niniyur Formation", "Danian (~66 - 61 Ma)", "Sandy & clayey limestone, chert, algae, Cardita beaumonti\nUppermost division in classic Indian Cretaceous-Tertiary succession", "#059669", "CORRECT PAIR (B)"),
    ("Ariyalur Group", "Campanian - Maastrichtian", "Sandstones, fossiliferous calcareous grits, Pachydiscus, dinosaur bones\nKallankurichi, Sillakkudi, and Ottakovil Formations", "#0284c7", "Late Cretaceous"),
    ("Trichinopoly Group", "Turonian - Coniacian", "Gravel beds, shell limestones, cross-bedded sandstones, Placenticeras\nRepresents marine transgression during early collision phase", "#d97706", "Upper Cretaceous"),
    ("Uttatur Group", "Upper Albian - Cenomanian", "Basal coral reef limestone, gypseous clays, Acanthoceras, belemnites\nOldest marine transgressive marine cycle of Cauvery Basin", "#7c3aed", "Mid-Cretaceous")
]

y_pos = 4.2
for name, age, desc, col, tag in stages:
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.75), 9.0, 0.75, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, f"{name} ({age})", fontsize=11.5, fontweight="bold", color="white")
    ax.text(0.7, y_pos - 0.58, desc, fontsize=8.5, color="#f8fafc")
    ax.text(9.3, y_pos - 0.25, tag, fontsize=9.5, fontweight="bold", color="#fde047" if "CORRECT" in tag else "white", ha="right")
    y_pos -= 0.95

# Summary box for incorrect pairs
ax.text(5.0, 0.35, "INCORRECT DISTRACTORS FORENSIC CHECK:\n• Bhander Group: Neoproterozoic (~650-850 Ma), NOT Early Proterozoic\n• Long Formation (Andaman): Middle to Late Miocene, NOT Oligocene\n• Bheema Group (Karnataka): Neoproterozoic Purana Basin (~800 Ma), NOT Cambrian",
        ha="center", fontsize=8.5, color="#1e293b", bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor="#ef4444", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 4.8)
ax.axis("off")
plt.title("Cauvery Basin Mesozoic-Tertiary Stratigraphy & Niniyur Formation Placement", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q047/cauvery_basin_niniyur_stratigraphy.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q048: Kutch Jurassic Type Area & Cephalopod Biozones
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

kutch_units = [
    ("Umia Formation (~500 m)", "Tithonian to Early Cretaceous", "Sandstones, shales, Trigonia beds, Ukra bed (Aptian ammonites)\nPlant beds with Ptilophyllum flora (Gondwana affinity)", "#0284c7", "Ammonites: Virgatosphinctes, Ptychites"),
    ("Katrol Formation (~300 m)", "Kimmeridgian", "Red sandstones, shales, gritty flags, ironstone nodules\nMarine shelf deposit with rich ammonite and bivalve fauna", "#059669", "Ammonites: Katroloceras, Waagenia"),
    ("Chari Formation (~360 m)", "Callovian to Oxfordian", "Fossiliferous oolitic limestones, shales, Dhosa Oolite marker bed\nWorld-standard reference for Middle Jurassic cephalopod biozones", "#d97706", "Ammonites: Macrocephalites, Reineckeia, Peltoceras"),
    ("Patcham Formation (~300 m)", "Bathonian", "Yellow limestones, corals, lamellibranchs, basal calc-arenites\nOldest exposed Mesozoic rocks in the Kutch Mainland & Island belt", "#7c3aed", "Ammonites: Macrocephalites triangularis, Sivajiceras")
]

y_pos = 4.4
for name, age, desc, col, bio in kutch_units:
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, f"{name} — {age}", fontsize=11.5, fontweight="bold", color="white")
    ax.text(0.7, y_pos - 0.52, desc, fontsize=8.2, color="#f8fafc")
    ax.text(0.7, y_pos - 0.72, f"Key Biozone / Diagnostic Fossils: {bio}", fontsize=8.0, fontweight="bold", color="#fef08a")
    y_pos -= 0.98

ax.text(5.0, 0.25, "KUTCH: Global Type Area for Middle to Late Jurassic Cephalopod Biostratigraphy (Waagen, Rajnath, Arkell)",
        ha="center", fontsize=9.5, fontweight="bold", color="#0f172a", bbox=dict(boxstyle="round,pad=0.4", facecolor="#e0f2fe", edgecolor="#0284c7", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 4.9)
ax.axis("off")
plt.title("Classic Jurassic Succession of Kutch (Patcham - Chari - Katrol - Umia)", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q048/kutch_jurassic_stratigraphy_biozones.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q049: Siwalik Group & Rich Mammalian Fauna
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

siwalik_subs = [
    ("Upper Siwalik (~2,000 m)", "Pliocene to Early Pleistocene (~3.5 - 0.6 Ma)", "Boulder Conglomerate, Pinjor, Tatrot Formations\nAbundant large herbivore mammals: Equus sivalensis, Elephas hysudricus,\nStegodon ganesa, Hexaprotodon sivalensis, Cervus, Rhinoceros", "#059669", "Stage of Advanced Equids & Elephants"),
    ("Middle Siwalik (~1,800 m)", "Late Miocene to Early Pliocene (~10.5 - 3.5 Ma)", "Dhok Pathan & Nagri Formations (Arkosaic sandstones & clays)\nGolden Age of Hominoids & Giraffids: Sivapithecus indicus / punjabicus,\nHipparion theobaldi (three-toed horse), Bramatherium, Mastodon", "#d97706", "Stage of Hominoids (Sivapithecus) & Hipparion"),
    ("Lower Siwalik (~1,500 m)", "Middle Miocene (~18.0 - 10.5 Ma)", "Chinji & Kamlial Formations (Hard sandstones & red shales)\nEarly mammalian radiation: Anthracotheres, primitive suids, Listriodon,\nDeinotherium, Gomphotherium, early primates", "#7c3aed", "Early Proboscideans & Artiodactyls")
]

y_pos = 4.3
for name, age, desc, col, stage in siwalik_subs:
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.95), 9.0, 0.95, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, f"{name} [{age}]", fontsize=11.5, fontweight="bold", color="white")
    ax.text(0.7, y_pos - 0.55, desc, fontsize=8.5, color="#f8fafc")
    ax.text(0.7, y_pos - 0.85, f"Biostratigraphic Milestone: {stage}", fontsize=8.2, fontweight="bold", color="#fef08a")
    y_pos -= 1.15

ax.text(5.0, 0.45, "THE FORENSIC CONCLUSION: The Siwalik molasse basin represents the world's most continuous and richest\nterrestrial Neogene vertebrate record, globally celebrated specifically for MAMMAL FOSSILS (Answer C).",
        ha="center", fontsize=8.5, fontweight="bold", color="#064e3b", bbox=dict(boxstyle="round,pad=0.4", facecolor="#d1fae5", edgecolor="#059669", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 4.8)
ax.axis("off")
plt.title("Siwalik Foreland Molasse Succession & Vertebrate Mammalian Faunal Stages", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q049/siwalik_mammalian_fauna_stratigraphy.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q050: Spiti Permians: Kuling Group
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

spiti_seq = [
    ("Lilang Group (Triassic)", "Otoceras bed at base marking P-Tr Boundary", "Nodular limestone, Daonella & Halobia beds, Megalodon limestone", "#64748b"),
    ("Kuling Group (Permian — Question 50)", "Gungri Formation (Productus Shale) & Gechang Formation", "Black splintery carbonaceous shales with Cyclolobus, Marginifera himalayensis,\nand calcareous sandstone. Defines complete Permian marine succession in Spiti", "#dc2626"),
    ("Kanawar Group (Carboniferous)", "Po Formation (Fenestella Shale) & Lipak Formation", "Early to Late Carboniferous: brachiopod & bryozoan rich limestones/shales", "#2563eb"),
    ("Muth Quartzite (Devonian)", "Snow-white pure orthoquartzite regional marker horizon", "Eolian to shallow marine super-mature quartz arenite across Tethyan Himalaya", "#059669")
]

y_pos = 4.3
for name, unit, desc, col in spiti_seq:
    is_target = "Kuling" in name
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.85), 9.0, 0.85, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=2.0 if is_target else 1.2, alpha=0.95)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, name, fontsize=12, fontweight="bold", color="#fef08a" if is_target else "white")
    ax.text(0.7, y_pos - 0.52, f"Subdivisions: {unit}", fontsize=9.0, fontweight="bold" if is_target else "normal", color="white")
    ax.text(0.7, y_pos - 0.74, desc, fontsize=8.0, color="#f1f5f9")
    if is_target:
        ax.text(9.3, y_pos - 0.25, "TARGET PERMIAN SYSTEM (C)", fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")
    y_pos -= 1.05

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 4.8)
ax.axis("off")
plt.title("Spiti Tethyan Basin Paleozoic Stratigraphy Highlighting Permian Kuling Group", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q050/spiti_tethyan_himalaya_kuling_group.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q051: Delhi Supergroup Intruded by Erinpura Granite (~850 Ma)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.text(5.0, 5.2, "Aravalli-Delhi Orogenic Belt Magmatic & Tectonic Evolution", ha="center", fontsize=13, fontweight="bold", color="#0f172a")

# Blocks
ax.add_patch(patches.Rectangle((0.8, 0.8), 8.4, 1.0, facecolor="#475569", edgecolor="#1e293b", lw=1.5))
ax.text(5.0, 1.3, "Basement Complex: Banded Gneissic Complex (BGC) / Mewar Gneiss (~3.3 - 2.8 Ga)", ha="center", va="center", color="white", fontweight="bold", fontsize=10)

ax.add_patch(patches.Rectangle((0.8, 2.0), 8.4, 1.0, facecolor="#0284c7", edgecolor="#1e293b", lw=1.5))
ax.text(5.0, 2.5, "Aravalli Supergroup (Paleoproterozoic, ~2.2 - 1.8 Ga)\nBasal quartzites, dolomites, phosphorites, phyllites, volcanics", ha="center", va="center", color="white", fontweight="bold", fontsize=9.5)

ax.add_patch(patches.Rectangle((0.8, 3.2), 8.4, 1.2, facecolor="#10b981", edgecolor="#1e293b", lw=1.5))
ax.text(5.0, 3.8, "Delhi Supergroup (Mesoproterozoic, ~1.7 - 1.0 Ga)\nAlwar Group (Arenaceous quartzites) & Ajabgarh Group (Calcareous/Pelitic schists)", ha="center", va="center", color="white", fontweight="bold", fontsize=10)

# Pluton intrusion cutting across Delhi
ax.add_patch(patches.Ellipse((5.0, 3.6), 4.2, 1.4, facecolor="#ef4444", edgecolor="#7f1d1d", lw=2, alpha=0.9))
ax.text(5.0, 3.6, "ERINPURA GRANITE PLUTONS (~850 Ma)\nPost-tectonic intrusive granite cutting across folded Delhi rocks", ha="center", va="center", color="white", fontweight="bold", fontsize=9.5)

ax.annotate("Intrusive Contact", xy=(3.0, 3.6), xytext=(1.4, 4.6),
            arrowprops=dict(arrowstyle="->", color="#b91c1c", lw=2), fontsize=9.5, fontweight="bold", color="#b91c1c")

ax.set_xlim(0, 10)
ax.set_ylim(0.5, 5.6)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q051/delhi_supergroup_erinpura_granite.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q052: Bhuj Formation Sandstones & Proterozoic Basin Facies
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

categories = [
    ("Bhuj Formation (Mesozoic of Kutch)", "Predominantly Sandstones (True — Correct Option A)", "Fluvial to deltaic medium-to-coarse quartz sandstones with giant planar & trough cross-stratification,\ninterbedded with thin siltstones and plant fossil beds (Ptilophyllum floral beds).", "#059669"),
    ("Kaladgi Basin (Karnataka)", "Quartzites, Sandstones & Carbonates (Option B is False)", "Dominated by quartz arenites (Bagalkot Group) and stromatolitic limestones/dolomites.\nContains minor argillites, but is emphatically NOT 'predominantly made of slates'.", "#dc2626"),
    ("Vindhyan Supergroup (Central India)", "Immense Limestone Sequences (Option C is False)", "World-renowned for thick commercial carbonate formations (Kajrahat, Rohtas, Lakheri, Bhander limestones).\nClaiming Vindhyan is 'devoid of limestone' is completely contradictory to Indian stratigraphy.", "#dc2626"),
    ("Cuddapah Basin (Andhra Pradesh)", "Siliciclastics & Carbonates (Option D is False)", "Composed of quartzites, conglomerates, shales, and dolomitic limestones (Papaghni, Chitravati, Nallamalai).\nMetadacites are rare volcanic flows; the basin is definitely NOT predominantly metadacite.", "#dc2626")
]

y_pos = 4.4
for title, status, desc, col in categories:
    rect = patches.FancyBboxPatch((0.5, y_pos - 0.82), 9.0, 0.82, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=1.5, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_pos - 0.25, title, fontsize=11.5, fontweight="bold", color="white")
    ax.text(9.3, y_pos - 0.25, status, fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")
    ax.text(0.7, y_pos - 0.58, desc, fontsize=8.2, color="#f8fafc")
    y_pos -= 0.98

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 4.8)
ax.axis("off")
plt.title("Comparative Lithofacies Analysis: Bhuj Sandstone vs. Proterozoic Purana Basins", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q052/bhuj_sandstone_sedimentary_facies.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q053: Devonian Marker Horizon: Muth Quartzites
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.text(5.0, 5.1, "Tethyan Himalayan Stratigraphic Column: Devonian Muth Quartzite Marker", ha="center", fontsize=13, fontweight="bold", color="#0f172a")

units_muth = [
    ("Lipak & Po Formations (Carboniferous)", "Fossiliferous limestone & Fenestella shales", "#475569"),
    ("MUTH QUARTZITE (Devonian Regional Marker Horizon)", "Snow-white, massive, vitreous, super-mature quartz arenite (>98% pure SiO2)\nThickness: 150 - 500 m. Forms prominent white cliffs across Kashmir, Spiti, Zanskar, and Kumaon", "#0284c7"),
    ("Pin Formation / Sanugba Group (Silurian)", "Shales, siltstones, and coral-bearing limestones", "#059669"),
    ("Shian Slates / Thango Formation (Ordovician)", "Purple quartzites, diamictites, and fossiliferous siltstones", "#d97706")
]

y = 4.2
for name, desc, col in units_muth:
    is_muth = "MUTH" in name
    rect = patches.FancyBboxPatch((0.6, y - 0.8), 8.8, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=2.2 if is_muth else 1.2, alpha=0.95)
    ax.add_patch(rect)
    ax.text(0.8, y - 0.28, name, fontsize=11.5, fontweight="bold", color="#fef08a" if is_muth else "white")
    ax.text(0.8, y - 0.60, desc, fontsize=8.2, color="#f8fafc")
    if is_muth:
        ax.text(9.2, y - 0.28, "DEVONIAN MARKER (C)", fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")
    y -= 0.95

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q053/muth_quartzite_devonian_marker.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q054: Stromatolites: Origin and Evolution of Life
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.5), dpi=180)
fig.patch.set_facecolor("#f8fafc")
ax1.set_facecolor("#f1f5f9")
ax2.set_facecolor("#f1f5f9")

# Diagram 1: Internal structure of stromatolite dome
theta = np.linspace(0, np.pi, 100)
for r in np.linspace(0.8, 3.0, 12):
    x = r * np.cos(theta)
    y = r * np.sin(theta) * 0.7
    ax1.plot(x, y, color="#047857", lw=1.5 if r in [1.6, 2.4] else 1.0)
ax1.fill_between(3.0 * np.cos(theta), 3.0 * np.sin(theta) * 0.7, color="#d1fae5", alpha=0.6)
ax1.text(0, 1.2, "Concentric Laminae\nFormed by Microbe\nSediment Trapping", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#064e3b")
ax1.set_title("Stromatolite Internal Lamination Fabric", fontsize=11, fontweight="bold", color="#0f172a")
ax1.set_xlim(-3.5, 3.5)
ax1.set_ylim(0, 2.5)
ax1.axis("off")

# Diagram 2: Key Milestones of Early Life
milestones = [
    ("Modern Era (Phanerozoic)", "Metazoan radiation & terrestrial colonization", "#64748b"),
    ("Proterozoic Stromatolites (2.5 - 0.54 Ga)", "Peak stromatolite diversity; Great Oxidation Event (GOE)", "#059669"),
    ("Oldest Stromatolites (~3.5 - 3.7 Ga)", "Pilbara (Australia) & Isua (Greenland) cyanobacterial mats", "#0284c7"),
    ("Prebiotic Earth (~4.5 - 3.8 Ga)", "Abiogenesis, RNA world, proto-cellular life", "#d97706")
]
y_m = 3.6
for name, desc, col in milestones:
    rect = patches.FancyBboxPatch((0.2, y_m - 0.65), 5.6, 0.65, boxstyle="round,pad=0.06",
                                  facecolor=col, edgecolor="#1e293b", lw=1.2, alpha=0.92)
    ax2.add_patch(rect)
    ax2.text(0.35, y_m - 0.24, name, fontsize=9.5, fontweight="bold", color="white")
    ax2.text(0.35, y_m - 0.50, desc, fontsize=7.8, color="#f8fafc")
    y_m -= 0.85

ax2.set_xlim(0, 6)
ax2.set_ylim(0.4, 4.0)
ax2.axis("off")
ax2.set_title("Evolutionary Timeline of Early Biosphere", fontsize=11, fontweight="bold", color="#0f172a")

plt.suptitle("Stromatolites: Direct Fossil Windows into the Origin and Evolution of Life (Question 54: A)", fontsize=12, fontweight="bold", y=0.98, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q054/stromatolites_cyanobacteria_life_evolution.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q055: Main Boundary Thrust (MBT): Himalayan Tectonic Architecture
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

# Balanced cross-section of Himalayan orogenic wedge
x = np.linspace(0, 10, 500)
# Topography
topo = 1.0 + 0.3*x + 0.05*x**2
ax.plot(x, topo, color="#0f172a", lw=2.5, label="Topography")
ax.fill_between(x, 0, topo, color="#f1f5f9", alpha=0.5)

# Thrust faults
ax.plot([2.5, 1.2], [1.9, 0.2], color="#dc2626", lw=2.5, linestyle="--")
ax.text(1.85, 1.1, "HFT / MFT", color="#dc2626", fontweight="bold", fontsize=10, rotation=50)

ax.plot([5.5, 3.5], [3.2, 0.2], color="#dc2626", lw=3.0)
ax.text(4.5, 1.8, "MBT (Main Boundary Thrust)", color="#b91c1c", fontweight="bold", fontsize=11, rotation=52)

ax.plot([8.2, 5.8], [4.8, 0.2], color="#dc2626", lw=2.5, linestyle="-.")
ax.text(7.0, 2.6, "MCT (Main Central Thrust)", color="#dc2626", fontweight="bold", fontsize=10, rotation=55)

# Zone labels
ax.text(1.0, 2.2, "Indo-Gangetic\nPlains (Foreland)", ha="center", fontsize=9, fontweight="bold", color="#475569")
ax.text(3.8, 3.0, "Sub-Himalaya\n(Siwaliks: Molasse)", ha="center", fontsize=9.5, fontweight="bold", color="#1e40af")
ax.text(6.8, 4.2, "Lesser Himalaya\n(Pre-Tertiary Sediments\n& Metasediments)", ha="center", fontsize=9.5, fontweight="bold", color="#065f46")
ax.text(9.2, 5.3, "Higher Himalaya\nCrystalline (HHC)", ha="center", fontsize=9, fontweight="bold", color="#854d0e")

# MBT separating Siwalik and Lesser Himalaya (Tertiary / Pre-Tertiary)
ax.text(5.0, 0.5, "MBT strictly separates Sub-Himalayan Siwaliks from the Lesser Himalayan formations (Answer A)",
        ha="center", fontsize=9.5, fontweight="bold", color="#991b1b", bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor="#dc2626", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 6.0)
ax.axis("off")
plt.title("Himalayan Major Longitudinal Fault Architecture: MFT -> MBT -> MCT", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q055/himalayan_thrust_architecture_mbt.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q056: Deccan Flood Basalts Erupted in Cretaceous (~66 Ma)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.text(5.0, 5.2, "Deccan Continental Flood Basalt Volcanism: Cretaceous-Paleogene Boundary", ha="center", fontsize=13, fontweight="bold", color="#0f172a")

deccan_data = [
    ("Tertiary / Paleocene Post-Deccan Units", "~61 - 55 Ma", "Laterite caps, intertrappean marine beds, Bombay intertrappean frog beds", "#64748b"),
    ("Wai Subgroup (Deccan Traps: ~50% of Total Volume)", "~65.5 - 64.5 Ma (Spans K-Pg Boundary)", "Mahabaleshwar, Panhala, and Desur Formations; erupted across K-Pg boundary", "#dc2626"),
    ("Lonavala & Kalsubai Subgroups (Main Volume)", "~66.5 - 65.5 Ma (LATE CRETACEOUS)", "Igatpuri, Jawhar, Poladpur, Bushe, and Khandala basalt formations\nVoluminous flood basalt pulse (~1.5 million km3) driven by Reunion mantle plume", "#ef4444"),
    ("Infratrappean / Lameta Formation", "Late Cretaceous (Maastrichtian, ~68 Ma)", "Fluvial & lacustrine limestones, sandstones, titanosaurs, dinosaur nesting sites", "#d97706")
]

y_d = 4.3
for name, age, desc, col in deccan_data:
    is_main = "Deccan" in name or "Lonavala" in name
    rect = patches.FancyBboxPatch((0.5, y_d - 0.85), 9.0, 0.85, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=2.0 if is_main else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_d - 0.25, name, fontsize=11.5, fontweight="bold", color="white")
    ax.text(9.3, y_d - 0.25, age, fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")
    ax.text(0.7, y_d - 0.58, desc, fontsize=8.2, color="#f8fafc")
    y_d -= 1.0

ax.text(5.0, 0.35, "Forensic Determination: Deccan volcanism initiated and reached peak eruptive flux during the CRETACEOUS (Answer C).",
        ha="center", fontsize=9.5, fontweight="bold", color="#7f1d1d", bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor="#dc2626", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.6)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q056/deccan_traps_flood_basalts_cretaceous.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q057: Mesozoic - Cenozoic Boundary at ~65 Ma (66 Ma)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.text(5.0, 5.2, "Chronostratigraphic Boundary: Mesozoic vs. Cenozoic Eras", ha="center", fontsize=13, fontweight="bold", color="#0f172a")

# Timeline bar
ax.add_patch(patches.Rectangle((1.0, 3.2), 3.8, 1.4, facecolor="#f59e0b", edgecolor="#1e293b", lw=2))
ax.text(2.9, 4.1, "MESOZOIC ERA", ha="center", fontsize=12, fontweight="bold", color="white")
ax.text(2.9, 3.6, "Triassic • Jurassic • Cretaceous\nDuration: ~186 Ma (252 to ~66 Ma)", ha="center", fontsize=8.5, color="#fef3c7")

ax.add_patch(patches.Rectangle((5.2, 3.2), 3.8, 1.4, facecolor="#0284c7", edgecolor="#1e293b", lw=2))
ax.text(7.1, 4.1, "CENOZOIC ERA", ha="center", fontsize=12, fontweight="bold", color="white")
ax.text(7.1, 3.6, "Paleogene • Neogene • Quaternary\nDuration: ~66 Ma to Present Day", ha="center", fontsize=8.5, color="#e0f2fe")

# The boundary line
ax.plot([5.0, 5.0], [2.2, 5.0], color="#dc2626", lw=3.5, linestyle="--")
ax.scatter([5.0], [3.9], color="#dc2626", s=180, zorder=5)

ax.text(5.0, 2.5, "K-Pg / K-T BOUNDARY\n~65 - 66 Ma (Answer D)\nChicxulub Asteroid Impact & Iridium Layer",
        ha="center", fontsize=10.5, fontweight="bold", color="#991b1b", bbox=dict(boxstyle="round,pad=0.5", facecolor="#fee2e2", edgecolor="#ef4444", lw=1.5))

ax.set_xlim(0, 10)
ax.set_ylim(1.5, 5.6)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q057/mesozoic_cenozoic_k_pg_boundary_65ma.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q058: Kashmir-Hazara Archean: Salkhala Series
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

kash_strat = [
    ("Upper Paleozoic to Triassic", "Panjal Traps (Permian), Gangamopteris Beds, Zewan Formation, Triassic Limestone", "#64748b"),
    ("Middle Paleozoic (Devonian - Carboniferous)", "Muth Quartzite (Devonian marker), Syringothyris Limestone, Fenestella Shales", "#0284c7"),
    ("Lower Paleozoic (Cambrian - Silurian)", "Fossiliferous Cambrian shales/slates with Redlichia noetlingi, Ordovician-Silurian beds", "#059669"),
    ("Dogra Slate (Late Neoproterozoic)", "Thick, cleaved dark green, purple & black slates with minor quartzites", "#d97706"),
    ("SALKHALA SERIES (Archean / Early Precambrian — Answer B)", "Crystalline metamorphic basement of Kashmir, Hazara & Nanga Parbat:\nGraphitic schists, phyllites, quartzites, crystalline dolomites, marbles, and migmatites", "#7c3aed")
]

y_k = 4.4
for name, desc, col in kash_strat:
    is_salk = "SALKHALA" in name
    rect = patches.FancyBboxPatch((0.5, y_k - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=2.0 if is_salk else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_k - 0.25, name, fontsize=11.5, fontweight="bold", color="#fef08a" if is_salk else "white")
    ax.text(0.7, y_k - 0.55, desc, fontsize=8.2, color="#f8fafc")
    if is_salk:
        ax.text(9.3, y_k - 0.25, "BASEMENT COMPLEX (B)", fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")
    y_k -= 0.95

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 4.9)
ax.axis("off")
plt.title("Stratigraphic Succession of Kashmir Basin: Salkhala Crystalline Basement to Triassic", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q058/kashmir_hazara_salkhala_series.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q059: Geologic Time Scale: Precambrian Occupies Longest Time
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6.0), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

# Pie chart showing relative time
sizes = [88.2, 6.3, 4.1, 1.4]
labels = [
    'Precambrian (>4,000 Ma)\n88.2% of Earth History (Answer C)',
    'Paleozoic (289 Ma)\n6.3%',
    'Mesozoic (186 Ma)\n4.1%',
    'Cenozoic (66 Ma)\n1.4%'
]
colors = ['#1e40af', '#059669', '#f59e0b', '#dc2626']
explode = (0.05, 0.05, 0.05, 0.05)

wedges, texts, autotexts = ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                                  autopct='%1.1f%%', startangle=140, pctdistance=0.75,
                                  wedgeprops=dict(edgecolor="#0f172a", linewidth=1.5),
                                  textprops=dict(fontsize=9.5, fontweight="bold"))
for at in autotexts:
    at.set_color("white")

plt.title("Proportional Distribution of Geological Time Across Earth's 4.54 Billion Year History", fontsize=13, fontweight="bold", pad=20, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q059/geologic_time_scale_precambrian_duration.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q060: Cretaceous-Tertiary (K-T / K-Pg) Mass Extinction Boundary
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

events = [
    ("End-Cretaceous (K-Pg / K-T)", "~66 Ma", "Extinction of non-avian dinosaurs, ammonites, marine reptiles; 76% species loss", "#dc2626", "QUESTION 60 (D)"),
    ("End-Triassic (Tr-J)", "~201 Ma", "Conodonts, early archosaurs, many therapsids; 80% species loss", "#f59e0b", "Triassic-Jurassic"),
    ("End-Permian (P-Tr)", "~252 Ma", "'The Great Dying' - Trilobites, eurypterids, blastoids; 96% marine species extinct", "#b91c1c", "Largest in Earth History"),
    ("Late Devonian (Frasnian-Famennian)", "~375 Ma", "Extinction of reef-builders (stromatoporoids, tabulate corals); 75% species loss", "#475569", "Kellwasser Event"),
    ("End-Ordovician (Hirnantian)", "~444 Ma", "Graptolites, trilobites, brachiopods; glacio-eustatic cooling; 85% species loss", "#64748b", "Glacial Epoche")
]

y_e = 4.4
for name, age, desc, col, tag in events:
    is_target = "K-Pg" in name
    rect = patches.FancyBboxPatch((0.5, y_e - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", linewidth=2.0 if is_target else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_e - 0.25, f"{name} ({age})", fontsize=11.5, fontweight="bold", color="white")
    ax.text(9.3, y_e - 0.25, tag, fontsize=9.5, fontweight="bold", color="#fef08a" if is_target else "white", ha="right")
    ax.text(0.7, y_e - 0.55, desc, fontsize=8.2, color="#f8fafc")
    y_e -= 0.95

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 4.9)
ax.axis("off")
plt.title("The 'Big Five' Phanerozoic Mass Extinction Events Highlighting the K-T Boundary", fontsize=13, fontweight="bold", pad=15, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q060/mass_extinction_k_t_boundary.png", dpi=180)
plt.close()

print("Successfully generated all 15 scientific plates for Batch 5 (Q046 to Q060)!")
