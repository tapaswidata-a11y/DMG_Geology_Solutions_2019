import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

for q in range(61, 76):
    os.makedirs(f"figures_2019_Q{q:03d}", exist_ok=True)

# -------------------------------------------------------------
# Q061: Archaeocyatha Confined to Lower Palaeozoic (Cambrian)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

# Archaeocyathan cup schematic
y_cone = np.linspace(0.8, 4.0, 100)
x_outer_r = 0.5 + 0.35 * y_cone
x_outer_l = -(0.5 + 0.35 * y_cone)
x_inner_r = 0.25 + 0.25 * y_cone
x_inner_l = -(0.25 + 0.25 * y_cone)

ax.plot(x_outer_r + 5.0, y_cone, color="#0f172a", lw=2)
ax.plot(x_outer_l + 5.0, y_cone, color="#0f172a", lw=2)
ax.plot(x_inner_r + 5.0, y_cone, color="#0f172a", lw=1.5, linestyle="--")
ax.plot(x_inner_l + 5.0, y_cone, color="#0f172a", lw=1.5, linestyle="--")

# Intervallum fill
ax.fill_betweenx(y_cone, x_inner_r + 5.0, x_outer_r + 5.0, color="#fde68a", alpha=0.7)
ax.fill_betweenx(y_cone, x_outer_l + 5.0, x_inner_l + 5.0, color="#fde68a", alpha=0.7)
ax.text(5.0, 2.4, "Central\nCavity", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#78350f")
ax.text(6.0, 3.2, "Intervallum\n(with Septa & Pores)", ha="left", va="center", fontsize=8.5, color="#92400e")

# Information cards
ax.text(0.8, 4.8, "Archaeocyatha: Earth's First Skeletal Reef-Builders", fontsize=12, fontweight="bold", color="#0f172a")
ax.text(0.8, 4.3, "• Biological Affinity: Sessile, calcareous sponge-grade metazoans (Phylum Porifera).\n• Double-Walled Calcareous Skeletons: Outer wall, inner wall, radial septa, and porous intervallum.\n• Chronostratigraphic Range: Exclusively restricted to the LOWER PALAEOZOIC (Lower to Middle Cambrian, ~525 - 505 Ma).\n• Extinction: Nearly wiped out at the end of the Early Cambrian; vanished completely by Late Cambrian.",
        fontsize=8.8, color="#1e293b", bbox=dict(boxstyle="round,pad=0.5", facecolor="#e0f2fe", edgecolor="#0284c7", lw=1.2))

ax.text(5.0, 0.4, "ARCHAEOCYATHA: Strictly confined to the LOWER PALAEOZOIC (Option A: Correct Answer)",
        ha="center", fontsize=10, fontweight="bold", color="#065f46", bbox=dict(boxstyle="round,pad=0.4", facecolor="#d1fae5", edgecolor="#059669", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.3)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q061/archaeocyatha_lower_palaeozoic_sponge.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q062: Trilobites Lived During Cambrian to Permian
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

periods = [
    ("Cambrian (~539 - 485 Ma)", "Explosive radiation: Redlichia, Olenellus, Fallotaspis, Paradoxides (Age of Trilobites)", "#059669"),
    ("Ordovician (~485 - 443 Ma)", "Peak morphological diversity: Asaphus, Trinucleus, Calymene (Hirnantian drop)", "#0284c7"),
    ("Silurian (~443 - 419 Ma)", "Post-extinction recovery: Encrinurus, Dalmanites, Bumastus", "#0284c7"),
    ("Devonian (~419 - 359 Ma)", "Proetida & Phacopida flourish: Phacops rana; Kellwasser event wipes out all but Proetida", "#d97706"),
    ("Carboniferous (~359 - 299 Ma)", "Sole surviving order (Proetida): Phillipsia, Griffithides (low diversity)", "#64748b"),
    ("Permian (~299 - 252 Ma)", "Final survivors (Proetidae: Pseudophillipsia); wiped out permanently at P-Tr Boundary", "#dc2626")
]

y_tr = 4.4
for name, desc, col in periods:
    rect = patches.FancyBboxPatch((0.5, y_tr - 0.55), 9.0, 0.55, boxstyle="round,pad=0.06",
                                  facecolor=col, edgecolor="#1e293b", lw=1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_tr - 0.22, name, fontsize=10.5, fontweight="bold", color="white")
    ax.text(0.7, y_tr - 0.45, desc, fontsize=8.0, color="#f8fafc")
    y_tr -= 0.68

ax.text(5.0, 4.9, "Class Trilobita Stratigraphic Range: CAMBRIAN TO PERMIAN (Option B)",
        ha="center", fontsize=12, fontweight="bold", color="#0f172a")

ax.text(5.0, 0.35, "Trilobites appeared in the Early Cambrian (~521 Ma) and became completely EXTINCT in the End-Permian Event (~252 Ma).",
        ha="center", fontsize=9.2, fontweight="bold", color="#7f1d1d", bbox=dict(boxstyle="round,pad=0.4", facecolor="#fee2e2", edgecolor="#ef4444", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.3)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q062/trilobite_geological_range_cambrian_permian.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q063: First Tetrapods to Colonize Land: Amphibia
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

nodes = [
    ("Sarcopterygian Lobe-Finned Fish (~385 Ma)", "Eusthenopteron: Internal paired humerus-radius-ulna fin bones", "#64748b", 1.2),
    ("Fishapod Transitional Fossil (~375 Ma)", "Tiktaalik roseae: Wrist joints, flexible neck, ribs for air breathing", "#0284c7", 2.3),
    ("FIRST LAND-COLONIZING TETRAPODS (~365 Ma)", "STEM AMPHIBIANS: Acanthostega & Ichthyostega (Labyrinthodontia)\nPossessed dactyly (limbs with digits), robust pectoral girdles, lungs", "#059669", 3.4),
    ("Amniote Divergence (~312 Ma)", "Reptilia (Hylonomus) & Synapsida: Shelled amniotic egg, dry skin", "#d97706", 4.5)
]

for title, desc, col, y in nodes:
    is_targ = "FIRST" in title
    rect = patches.FancyBboxPatch((0.6, y - 0.45), 8.8, 0.85, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_targ else 1.2, alpha=0.95)
    ax.add_patch(rect)
    ax.text(0.8, y + 0.15, title, fontsize=11, fontweight="bold", color="#fef08a" if is_targ else "white")
    ax.text(0.8, y - 0.22, desc, fontsize=8.2, color="#f8fafc")
    if is_targ:
        ax.text(9.2, y + 0.15, "CORRECT ANSWER (C)", fontsize=9.5, fontweight="bold", color="#fef08a", ha="right")

ax.text(5.0, 5.3, "The Fish-to-Tetrapod Transition: Amphibia as First Land Colonizers",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.5, 5.7)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q063/first_tetrapods_colonize_land_amphibia.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q064: Crinoids Range: Cambrian to Recent
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

# Crinoid sketch
ax.plot([2.5, 2.5], [1.0, 3.2], color="#0f172a", lw=4) # stalk
ax.text(2.8, 2.1, "Columnar Stem\n(Ossicles/Columnals)", fontsize=8.5, color="#1e293b")
ax.add_patch(patches.Ellipse((2.5, 3.5), 0.8, 0.6, facecolor="#f59e0b", edgecolor="#0f172a", lw=1.5))
ax.text(2.5, 3.5, "Calyx", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#78350f")
# Arms
for angle in [-40, -20, 0, 20, 40]:
    rad = np.radians(angle + 90)
    ax.plot([2.5, 2.5 + 0.8*np.cos(rad)], [3.8, 3.8 + 0.8*np.sin(rad)], color="#d97706", lw=2)

ax.text(6.2, 4.8, "Class Crinoidea (Echinodermata): 'Sea Lilies'", fontsize=12, fontweight="bold", color="#0f172a")
crin_info = [
    ("Origin (Early Cambrian, ~520 Ma):", "Echmatocrinus and primitive stem-group crinoids in Cambrian seas."),
    ("Paleozoic Heyday (Ordovician - Carboniferous):", "Prolific limestone builders; 'encrinites' formed of billions of columnals."),
    ("Mesozoic Radiation (Triassic - Cretaceous):", "Encrinus liliformis (Triassic); evolution of free-swimming comatulids."),
    ("Modern Era (Cenozoic to RECENT):", "Still thriving today: Stalked sea lilies in abyssal depths & unstalked feather stars on coral reefs.")
]
y_c = 4.2
for h, d in crin_info:
    ax.text(4.0, y_c, h, fontsize=9.2, fontweight="bold", color="#0369a1")
    ax.text(4.0, y_c - 0.28, d, fontsize=8.2, color="#334155")
    y_c -= 0.68

ax.text(5.0, 0.4, "CRINOID STRATIGRAPHIC RANGE: CAMBRIAN TO RECENT (Option C)",
        ha="center", fontsize=10.5, fontweight="bold", color="#065f46", bbox=dict(boxstyle="round,pad=0.4", facecolor="#d1fae5", edgecolor="#059669", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.4)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q064/crinoid_morphology_range_cambrian_recent.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q065: Epizoic Organisms Attached to Larger Organisms
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

terms = [
    ("Epizoic (Epizoan — Question 65)", "Organisms that live attached non-parasitically to the exterior surface of another living host organism\nExamples: Acorn barnacles on whale skin, serpulid worms on ammonite shells, bryozoans on brachiopods", "#059669", "CORRECT (C)"),
    ("Epifauna (Epibenthos)", "Aquatic animals that live on the surface of the seabed or sedimentary substrate\nExamples: Sea stars, crabs, crawling snails, sea urchins living upon the ocean floor", "#0284c7", "Substrate Dwellers"),
    ("Infauna (Endobenthos)", "Aquatic animals that burrow beneath the sediment-water interface into the soft substrate\nExamples: Burrowing bivalves (Mya, Ensis), polychaete worms, lugworms", "#d97706", "Sediment Burrowers"),
    ("Epitheca / Eozoon", "Epitheca is the outermost skeletal layer of coral corallites; Eozoon canadense was a pseudofossil\n(metamorphic calcite-serpentine banding mistakenly identified as a primordial foraminifer)", "#64748b", "Anatomical / False Term")
]

y_ep = 4.4
for title, desc, col, tag in terms:
    is_ep = "Epizoic" in title
    rect = patches.FancyBboxPatch((0.5, y_ep - 0.75), 9.0, 0.75, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_ep else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_ep - 0.22, title, fontsize=11, fontweight="bold", color="#fef08a" if is_ep else "white")
    ax.text(9.3, y_ep - 0.22, tag, fontsize=9.5, fontweight="bold", color="#fef08a" if is_ep else "white", ha="right")
    ax.text(0.7, y_ep - 0.52, desc, fontsize=8.2, color="#f8fafc")
    y_ep -= 0.95

ax.text(5.0, 5.1, "Marine Ecological Classification: Epizoic Mode of Life",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q065/epizoic_organisms_marine_ecology.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q066: Plankton: Drifting Organisms in Water Column
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

zones = [
    ("PLANKTON (From Greek 'Planktos' = Drifter / Wanderer)", "Passively drifting or weakly swimming organisms swept along by water currents\nPhytoplankton (diatoms, dinoflagellates) & Zooplankton (foraminifera, radiolaria, copepods)\n*Frequently tested in elementary syllabi under pelagic water-column organisms or unicellular microfossils*", "#0284c7"),
    ("NEKTON (Active Swimmers)", "Pelagic organisms capable of actively swimming against horizontal tides and currents\nExamples: Teleost fish, sharks, squids, marine reptiles, whales", "#059669"),
    ("BENTHOS (Seafloor Dwellers)", "Organisms living directly upon (epifauna) or within (infauna) the ocean bottom\nExamples: Corals, brachiopods, bivalves, crinoids, benthic foraminifera", "#d97706")
]

y_z = 4.3
for title, desc, col in zones:
    rect = patches.FancyBboxPatch((0.5, y_z - 0.95), 9.0, 0.95, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=1.5, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_z - 0.25, title, fontsize=11, fontweight="bold", color="white")
    ax.text(0.7, y_z - 0.60, desc, fontsize=8.2, color="#f8fafc")
    y_z -= 1.15

ax.text(5.0, 5.1, "Marine Ecological Divisions: Plankton vs. Nekton vs. Benthos",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q066/plankton_nekton_benthos_divisions.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q067: Evolution of Horse: First Stage is Hyracotherium (Eohippus)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

stages = [
    ("Stage 1: Hyracotherium (Eohippus)", "Early Eocene (~55 Ma)", "Small fox-sized (~40 cm); 4 toes on front foot, 3 on hind foot; low-crowned brachydont teeth for browsing foliage.", "#059669", "FIRST STAGE (A)"),
    ("Stage 2: Mesohippus / Miohippus", "Oligocene (~35 Ma)", "Sheep-sized (~60 cm); 3 toes on all feet with enlarged middle digit; pad-supported walking.", "#0284c7", "Oligocene Stage"),
    ("Stage 3: Merychippus", "Miocene (~16 Ma)", "Pony-sized (~100 cm); 3 toes with spring-foot mechanism; high-crowned hypsodont cement-covered teeth for abrasive grass.", "#d97706", "Miocene Grazer"),
    ("Stage 4: Pliohippus", "Pliocene (~5 Ma)", "First true single-toed (monodactyl) horse; lateral side toes reduced to splint bones.", "#7c3aed", "Monodactyl Transition"),
    ("Stage 5: Equus", "Pleistocene to RECENT", "Modern horse (~150 cm); fully single hoof (digit III), deep hypsodont molars with complex enamel folds.", "#64748b", "Modern Horse")
]

y_s = 4.4
for name, age, desc, col, tag in stages:
    is_first = "Stage 1" in name
    rect = patches.FancyBboxPatch((0.5, y_s - 0.72), 9.0, 0.72, boxstyle="round,pad=0.06",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_first else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_s - 0.22, f"{name} [{age}]", fontsize=11, fontweight="bold", color="#fef08a" if is_first else "white")
    ax.text(9.3, y_s - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_first else "white", ha="right")
    ax.text(0.7, y_s - 0.50, desc, fontsize=8.0, color="#f8fafc")
    y_s -= 0.82

ax.text(5.0, 5.1, "Evolutionary Lineage of the Equidae: Hyracotherium as the Foundational Stage",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q067/horse_evolution_hyracotherium_stages.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q068: Lower Gondwana Flora Conifer: Buriadia
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

taxa = [
    ("Buriadia (Buriadia sewardii)", "Primitive Conifer (Order Coniferales / Voltziales)", "Branched woody gymnosperm shoots bearing bifid and single needle-like linear leaves with terminal,\nsolitary erect seeds. Landmark earliest conifer of the Lower Gondwana (Karharbari / Talchir beds).", "#059669", "CONIFER (B)"),
    ("Glossopteris", "Pteridosperm (Seed Fern / Glossopteridales)", "Tongue-shaped net-veined leaves with distinct midrib; signature plant of Gondwanaland coal measures.", "#0284c7", "Seed Fern"),
    ("Gangamopteris", "Pteridosperm (Seed Fern / Glossopteridales)", "Tongue-shaped leaves lacking a central midrib; diagnostic of Early Permian Talchir & Karharbari beds.", "#0284c7", "Seed Fern"),
    ("Schizoneura (Schizoneura gondwanensis)", "Sphenopsid / Articulate (Equisetales / Horsetail)", "Jointed fluted ribbed stems with whorls of strap-like leaves; swamp-dwelling sphenopsid.", "#d97706", "Horsetail")
]

y_t = 4.4
for name, affil, desc, col, tag in taxa:
    is_bur = "Buriadia" in name
    rect = patches.FancyBboxPatch((0.5, y_t - 0.78), 9.0, 0.78, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_bur else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_t - 0.22, f"{name} — {affil}", fontsize=11, fontweight="bold", color="#fef08a" if is_bur else "white")
    ax.text(9.3, y_t - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_bur else "white", ha="right")
    ax.text(0.7, y_t - 0.52, desc, fontsize=8.0, color="#f8fafc")
    y_t -= 0.95

ax.text(5.0, 5.1, "Gondwana Paleobotany: Identification of Buriadia as a True Conifer",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q068/buriadia_gondwana_conifer_paleobotany.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q069: Primate Fossil: Ramapithecus
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

primates = [
    ("Ramapithecus (Sivapithecus) — Question 69", "Order Primates (Suborder Anthropoidea, Family Hominidae / Pongidae)", "Discovered by G.E. Pilgrim & G.E. Lewis in the Middle Siwaliks (Nagri / Dhok Pathan formations).\nCharacterized by parabolic dental arch, low-crowned molars with thick enamel, and reduced canines.", "#059669", "PRIMATE FOSSIL (C)"),
    ("Hipparion (Hipparion theobaldi)", "Order Perissodactyla (Family Equidae)", "Three-toed grazing horse of the Middle Siwaliks; diagnostic index fossil for the Nagri stage (~10.7 Ma).", "#0284c7", "Ungulate Horse"),
    ("Equus (Equus sivalensis)", "Order Perissodactyla (Family Equidae)", "Modern single-toed horse appearing in the Upper Siwalik Pinjor Formation (Early Pleistocene).", "#0284c7", "Ungulate Horse"),
    ("Stegolophodon", "Order Proboscidea (Family Stegodontidae)", "Extinct primitive elephantoid with crested (lophodont) molar teeth; ancestor of Stegodon.", "#d97706", "Elephant Ancestor")
]

y_pr = 4.4
for name, cl, desc, col, tag in primates:
    is_pr = "Ramapithecus" in name
    rect = patches.FancyBboxPatch((0.5, y_pr - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_pr else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_pr - 0.22, f"{name}", fontsize=11, fontweight="bold", color="#fef08a" if is_pr else "white")
    ax.text(9.3, y_pr - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_pr else "white", ha="right")
    ax.text(0.7, y_pr - 0.44, f"Taxonomic Classification: {cl}", fontsize=8.2, fontweight="bold", color="#fef08a")
    ax.text(0.7, y_pr - 0.65, desc, fontsize=7.8, color="#f8fafc")
    y_pr -= 0.98

ax.text(5.0, 5.1, "Siwalik Vertebrate Fauna: Ramapithecus as the Distinct Primate Genus",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q069/ramapithecus_primate_fossil_siwaliks.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q070: Mesozoic Ammonoid Sutures
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

sutures = [
    ("Ammonitic Suture (MESOZOIC ERA — Jurassic & Cretaceous)", "Both lobes AND saddles are complexly frilled and fluted with multi-order foliations\nSupreme biostratigraphic index fossils for Jurassic (Kutch) and Cretaceous (Cauvery Basin)", "#059669", "TARGET ERA (C)"),
    ("Ceratitic Suture (Triassic Period — Early Mesozoic)", "Smooth rounded saddles and denticulated/serrated fluted lobes (e.g., Ceratites)", "#0284c7", "Triassic"),
    ("Goniatitic Suture (Late Paleozoic — Devonian to Permian)", "Sharp, angular pointed lobes and simple smooth rounded saddles (e.g., Goniatites)", "#d97706", "Late Paleozoic"),
    ("Nautilitic Suture (Early Paleozoic to Recent)", "Simple, straight to gently undulating suture lines devoid of complex subdivisions (Nautilus)", "#64748b", "Primitive / Non-Ammonoid")
]

y_su = 4.4
for name, desc, col, tag in sutures:
    is_mes = "MESOZOIC" in name
    rect = patches.FancyBboxPatch((0.5, y_su - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_mes else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_su - 0.22, name, fontsize=11, fontweight="bold", color="#fef08a" if is_mes else "white")
    ax.text(9.3, y_su - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_mes else "white", ha="right")
    ax.text(0.7, y_su - 0.55, desc, fontsize=8.0, color="#f8fafc")
    y_su -= 0.98

ax.text(5.0, 5.1, "Ammonoid Suture Evolution: Peak Structural Complexity in the Mesozoic",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q070/ammonoid_suture_evolution_mesozoic.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q071: Gastropod Coiling: Physa is Sinistrally Coiled
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5.5), dpi=180)
fig.patch.set_facecolor("#f8fafc")
ax1.set_facecolor("#f1f5f9")
ax2.set_facecolor("#f1f5f9")

# Diagram 1: Sinistral (Physa)
ax1.text(0, 2.5, "SINISTRAL (Left-Handed)\nGenus: Physa", ha="center", fontsize=11, fontweight="bold", color="#059669")
# Shell outline
theta = np.linspace(0, 3*np.pi, 200)
r = np.exp(0.15*theta)
ax1.plot(-r*np.cos(theta), r*np.sin(theta), color="#0f172a", lw=2)
# Aperture on Left
ax1.add_patch(patches.Ellipse((-1.5, 0), 1.2, 1.8, facecolor="#86efac", edgecolor="#065f46", lw=2))
ax1.text(-1.5, 0, "Aperture\non LEFT", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#065f46")
ax1.set_xlim(-4, 4)
ax1.set_ylim(-3, 3)
ax1.axis("off")

# Diagram 2: Dextral (Turritella, Helix)
ax2.text(0, 2.5, "DEXTRAL (Right-Handed)\nMost Gastropods", ha="center", fontsize=11, fontweight="bold", color="#0284c7")
ax2.plot(r*np.cos(theta), r*np.sin(theta), color="#0f172a", lw=2)
# Aperture on Right
ax2.add_patch(patches.Ellipse((1.5, 0), 1.2, 1.8, facecolor="#bae6fd", edgecolor="#0369a1", lw=2))
ax2.text(1.5, 0, "Aperture\non RIGHT", ha="center", va="center", fontsize=9.5, fontweight="bold", color="#0369a1")
ax2.set_xlim(-4, 4)
ax2.set_ylim(-3, 3)
ax2.axis("off")

plt.suptitle("Gastropod Shell Coiling Chirality: Physa is Sinistrally Coiled (Option D)", fontsize=12.5, fontweight="bold", y=0.98, color="#0f172a")
plt.tight_layout()
plt.savefig("figures_2019_Q071/physa_sinistral_gastropod_coiling.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q072: Brachiopod Articulata Has Dental System
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

classes = [
    ("Class Articulata (Rhynchonelliformea — Question 72)", "POSSESSES WELL-DEVELOPED DENTAL SYSTEM", "Valves articulate via a rigid hinge mechanism: Two calcareous hinge teeth on the pedicle\n(ventral) valve fit snugly into dental sockets on the brachial (dorsal) valve.\nIncludes: Spirifer, Productus, Terebratula, Rhynchonella.", "#059669", "HAS DENTAL SYSTEM (B)"),
    ("Class Inarticulata (Linguliformea / Craniiformea)", "COMPLETELY DEVOID OF DENTAL SYSTEM", "Valves lack teeth and sockets entirely; held together solely by complex adductor and diductor\nmuscles. Valves composed of calcium phosphate (chitinophosphatic) or calcite.\nIncludes: Lingula, Crania, Obolus.", "#dc2626", "NO Dental System"),
    ("Delthyrium & Deltidium", "Apertural Features on Pedicle Valve", "Delthyrium is the triangular opening beneath the beak for pedicle emergence.\nDeltidium consists of calcareous plates closing or restricting the delthyrium.", "#64748b", "Morphological Parts")
]

y_br = 4.3
for name, cap, desc, col, tag in classes:
    is_art = "Articulata" in name
    rect = patches.FancyBboxPatch((0.5, y_br - 0.9), 9.0, 0.9, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_art else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_br - 0.22, name, fontsize=11, fontweight="bold", color="#fef08a" if is_art else "white")
    ax.text(9.3, y_br - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_art else "white", ha="right")
    ax.text(0.7, y_br - 0.44, cap, fontsize=8.2, fontweight="bold", color="#fef08a")
    ax.text(0.7, y_br - 0.68, desc, fontsize=7.8, color="#f8fafc")
    y_br -= 1.15

ax.text(5.0, 5.1, "Brachiopod Articulation: Class Articulata Possesses Dental System (Teeth & Sockets)",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q072/brachiopod_dental_system_articulata.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q073: Conodont is a Phosphatic Microfossil
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ax.text(5.0, 5.1, "Conodont Anatomy, Mineralogy, and Biostratigraphic Role", ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

props = [
    ("Mineralogical Composition: Carbonate-Apatite (Francolite)", "Conodont elements are composed strictly of microcrystalline CALCIUM PHOSPHATE: Ca5(PO4, CO3)3F\nThey are unequivocally PHOSPHATIC MICROFOSSILS (Question 73: Option B).", "#059669"),
    ("Biological Affinity: Primitive Agnathous Chordates", "Represent tooth-like food-processing elements located in the pharyngeal apparatus of eel-like chordates.\nExtensive apparatus: Coniform (simple cones), Ramiform (blades/bars), and Pectiniform (platforms).", "#0284c7"),
    ("Biostratigraphic & Thermal Maturity Index (CAI)", "High evolutionary turnover makes conodonts the global standard for Cambrian to Triassic biozones.\nConodont Alteration Index (CAI 1 to 8): Organic matter darkens with burial temperature, indexing oil/gas windows.", "#d97706")
]

y_co = 4.3
for title, desc, col in props:
    rect = patches.FancyBboxPatch((0.5, y_co - 0.9), 9.0, 0.9, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=1.5, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_co - 0.25, title, fontsize=11, fontweight="bold", color="white")
    ax.text(0.7, y_co - 0.60, desc, fontsize=8.2, color="#f8fafc")
    y_co -= 1.15

ax.text(5.0, 0.4, "CONODONT: Phosphatic Microfossil (Option B: Correct Answer)",
        ha="center", fontsize=10.5, fontweight="bold", color="#065f46", bbox=dict(boxstyle="round,pad=0.4", facecolor="#d1fae5", edgecolor="#059669", lw=1.2))

ax.set_xlim(0, 10)
ax.set_ylim(0, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q073/conodont_phosphatic_microfossil.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q074: Bivalve Dentition: Arca Has Taxodont Dentition
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

dent = [
    ("Taxodont Dentition (Archetypal Genus: Arca)", "Continuous row of numerous, small, similar, comb-like alternating transverse teeth and sockets\nalong a straight or arched hinge margin. Typical of primitive bivalves (Arcidae, Nuculidae).", "#059669", "TAXODONT (A)"),
    ("Heterodont Dentition (e.g., Venus, Cardium, Mercenaria)", "Differentiated into a few distinct cardinal teeth beneath the beak and anterior/posterior lateral teeth.", "#0284c7", "Heterodont"),
    ("Dysodont Dentition (e.g., Mytilus, Perna)", "Teeth are extremely weak, reduced to tiny denticles, or absent; valves anchored by byssus threads.", "#d97706", "Dysodont"),
    ("Desmodont Dentition (e.g., Pholadomya, Mya)", "Teeth replaced by a large, internal spatulate chondrophore carrying an internal resilient ligament.", "#64748b", "Desmodont")
]

y_de = 4.4
for name, desc, col, tag in dent:
    is_arc = "Taxodont" in name
    rect = patches.FancyBboxPatch((0.5, y_de - 0.8), 9.0, 0.8, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_arc else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_de - 0.22, name, fontsize=11, fontweight="bold", color="#fef08a" if is_arc else "white")
    ax.text(9.3, y_de - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_arc else "white", ha="right")
    ax.text(0.7, y_de - 0.52, desc, fontsize=8.0, color="#f8fafc")
    y_de -= 0.98

ax.text(5.0, 5.1, "Bivalve Hinge Dentition: Arca as the Classic Representative of Taxodont Dentition",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q074/arca_taxodont_bivalve_dentition.png", dpi=180)
plt.close()

# -------------------------------------------------------------
# Q075: Ichnofossils: Trace Fossils (Footprints & Trails)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5.8), dpi=180)
ax.set_facecolor("#f8fafc")
fig.patch.set_facecolor("#f8fafc")

ichno = [
    ("ICHNOFOSSILS (Trace Fossils — Greek 'Ichnos' = Footprint)", "Preserved indirect geological records of biological activity and behavior (NOT body shells/bones)\nExamples: Footprints (Horse/Dinosaur tracks), walking trails (Serpent trails), burrows, borings, coprolites.", "#059669", "TRACE FOSSILS"),
    ("Seilacher's Ethological Behavioral Classification:", "• Repichnia: Locomotion tracks & trails (footprints, serpent trails, Cruziana)\n• Pascichnia: Winding grazing trails on sediment surface (Helminthopsis)\n• Fodinichnia: Deposit-feeding burrows inside sediment (Thalassinoides)\n• Domichnia: Permanent dwelling burrows (Skolithos pipe-rock)\n• Cubichnia: Resting traces (Rusophycus)", "#0284c7", "Behavioral Categories"),
    ("Body Fossils (Contrasting Distractors):", "Preserved actual physical skeletal remains of the organism (e.g., Lamellibranch bivalve shell, Trilobite carapace).\nOption A and Option B represent BODY fossils, whereas footprints/trails are ICHNOFOSSILS.", "#dc2626", "Body Fossils")
]

y_ic = 4.3
for name, desc, col, tag in ichno:
    is_targ = "ICHNOFOSSILS" in name
    rect = patches.FancyBboxPatch((0.5, y_ic - 0.95), 9.0, 0.95, boxstyle="round,pad=0.08",
                                  facecolor=col, edgecolor="#1e293b", lw=2.0 if is_targ else 1.2, alpha=0.92)
    ax.add_patch(rect)
    ax.text(0.7, y_ic - 0.22, name, fontsize=11, fontweight="bold", color="#fef08a" if is_targ else "white")
    ax.text(9.3, y_ic - 0.22, tag, fontsize=9.2, fontweight="bold", color="#fef08a" if is_targ else "white", ha="right")
    ax.text(0.7, y_ic - 0.58, desc, fontsize=8.0, color="#f8fafc")
    y_ic -= 1.15

ax.text(5.0, 5.1, "Ichnology: Trace Fossils vs. Body Fossils (Footprints & Trails)",
        ha="center", fontsize=12.5, fontweight="bold", color="#0f172a")

ax.set_xlim(0, 10)
ax.set_ylim(0.4, 5.5)
ax.axis("off")
plt.tight_layout()
plt.savefig("figures_2019_Q075/ichnofossils_trace_fossils_classification.png", dpi=180)
plt.close()

print("Successfully generated all 15 scientific plates for Batch 6 (Q061 to Q075)!")
