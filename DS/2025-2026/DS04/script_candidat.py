# ──────────────────────────────────────────────────────────────
# Code donné au départ
# ──────────────────────────────────────────────────────────────


from collections import deque
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ──────────────────────────────────────────────────────────────
# Paramètres
# ──────────────────────────────────────────────────────────────
# Grille importée (20 colonnes × 14 lignes)
# 1 = mur  |  0 = case libre
# Départ  D : (ligne=1,  col=0)
# Arrivée A : (ligne=12, col=19)
# ──────────────────────────────────────────────────────────────

DEPART  = [1, 0]
ARRIVEE = [12, 19]
LIGNES  = 14
COLS    = 20

# ──────────────────────────────────────────────────────────────
# Affichage matplotlib
# ──────────────────────────────────────────────────────────────

def afficher(grille, chemin):
    img = np.zeros((LIGNES, COLS, 3))

    for r in range(LIGNES):
        for c in range(COLS):
            img[r, c] = [0.17, 0.17, 0.17] if grille[r][c] == 1 else [0.95, 0.95, 0.95]

    if chemin:
        for case in chemin:
            (r,c)=[int(coord) for coord in case[1:-1].split(',')]            
            if (r, c) not in (DEPART, ARRIVEE):
                img[r, c] = [0.94, 0.62, 0.15]  # orange – chemin optimal

    img[DEPART[0],  DEPART[1]]  = [0.11, 0.62, 0.46]  # vert  – D
    img[ARRIVEE[0], ARRIVEE[1]] = [0.85, 0.35, 0.19]  # rouge – A

    fig, ax = plt.subplots(figsize=(13, 8))
    ax.imshow(img, interpolation='nearest', aspect='equal')

    # Lettre S et E
    for (pos, lettre) in [(DEPART, 'D'), (ARRIVEE, 'A')]:
        ax.text(pos[1], pos[0], lettre, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')
        
    ax.set_title('Résolution du labyrinthe', fontsize=14, pad=12)

    legendes = [
        mpatches.Patch(color=[0.17,0.17,0.16], label='Mur'),
        mpatches.Patch(color=[0.95,0.94,0.91], label='Case libre'),
        mpatches.Patch(color=[0.94,0.62,0.15], label='Chemin optimal'),
        mpatches.Patch(color=[0.11,0.62,0.46], label='Départ D'),
        mpatches.Patch(color=[0.85,0.35,0.19], label='Arrivée A'),
    ]
    ax.legend(handles=legendes, loc='lower center',
              bbox_to_anchor=(0.5, -0.09), ncol=6, fontsize=9, framealpha=0.9)

    plt.tight_layout()
    plt.show()

# ──────────────────────────────────────────────────────────────
# Fin du code donné au départ
# ──────────────────────────────────────────────────────────────
