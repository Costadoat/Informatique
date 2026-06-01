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


# Question 1 : Lecture CSV

file=open('grille.csv','r')
contenu=file.read()
file.close()
lignes=contenu.split('\n')

grille=[]
for ligne in lignes[:-1]:
    data=[int(i) for i in ligne.split(';')]
    grille.append(data)

# Question 2 : Afficher le labyrinthe

afficher(grille,[])

# Question 3 : Rechercher les cases vides

cases_libres=[]
for i in range(LIGNES):
    for j in range(COLS):
        if grille[i][j]==0:
            cases_libres.append([i,j])
#print(cases_libres)

# Question 4 : Nommer les cases

def nom_case(case):
    return '['+str(case[0])+','+str(case[1])+']'

print(nom_case([1,2]))

# Question 5 : Recherche la prochaine case

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def prochaine_case(case,direction):
    return [case[0]+direction[0],case[1]+direction[1]]

print(prochaine_case([0,1],directions[2]))

# Question 6 : Générer le dictionnaire du graphe

graphe={}
for case_libre in cases_libres:
    graphe[nom_case(case_libre)]=[]
    for direction in directions:
        prochaine=prochaine_case(case_libre,direction)
        if prochaine[0]>=0 and prochaine[0]<LIGNES and prochaine[1]>=0 and prochaine[1]<COLS:
            if grille[prochaine[0]][prochaine[1]]==0:
                graphe[nom_case(case_libre)].append(nom_case(prochaine))
            
print(graphe['[1,1]'])    

# Question 7 : Trouver tous les chemins du départ à l'arrivée

def tous_les_chemins(graph, depart, arrivee):

    chemins_a_explorer = [[depart]]
    resultats = []

    while len(chemins_a_explorer)>0:
        # Récupérer le premier chemin des chemins a explorer
        # Le supprimer des chemins a explorer
        chemin = chemins_a_explorer.pop(0)
        # Partir du dernier sommet de ce chemin
        sommet = chemin[-1]
        # Si on atteint l'arrivée
        if sommet == arrivee:
            # Stocker le chemin dans la liste resultats
            resultats.append(chemin)
        else:
            # Pour chaque voisin de ce sommet
            for voisin in graph[sommet]:
                # On regarde si on est pas déjà passé par ce sommer
                if voisin not in chemin:
                    # On ajoute ce voisin à ce chemin
                    nouveau_chemin = chemin + [voisin]
                    # On intègre ce chemin à la liste des chemins à explorer
                    chemins_a_explorer.append(nouveau_chemin)
    return resultats

chemins = list(tous_les_chemins(graphe, nom_case(DEPART), nom_case(ARRIVEE)))

# Question 8

chemin_plus_court=chemins[0]
for c in chemins:
#    print(len(c))
#    print(' -> '.join(c))
    if len(c)<len(chemin_plus_court):
        chemin_plus_court=c
print(' -> '.join(chemin_plus_court))

afficher(grille,chemin_plus_court)
