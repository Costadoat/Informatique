from PIL import Image
import numpy as np

# Charger le masque PNG
img = Image.open("joconde_masque_l.png").convert("L")  # niveaux de gris

# Conversion en tableau numpy
mask = np.array(img)

# Binarisation : blanc → 1, noir → 0
mask = (mask > 127).astype(int)

# Sauvegarde en CSV
np.savetxt("masque_mona_lisa.csv", mask, fmt="%d", delimiter=",")
