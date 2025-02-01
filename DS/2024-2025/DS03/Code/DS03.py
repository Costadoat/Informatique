import random
listeint=list(range(100))
random.shuffle(listeint)
#print(listeint)

#ici on utilise un tri par sélection
def tri(liste): 
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)-1):
        # Initialiser le min
        min=liste[i]
        jmin=i
        for j in range(i, len(liste)):
            # Chercher le min
            if liste[j]<min:
                jmin=j
                min=liste[j]
        # Permuter le min et l'élément i
        liste[i],liste[jmin]=liste[jmin],liste[i]

tri(listeint)
#print(listeint)

from os import listdir
liste_pieces = listdir('/home/eleve/Ressources/PTSI/boite')
liste_pieces.sort()
#print(liste_pieces)

print(liste_pieces[0][2:6])

def tri_pieces(liste): 
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)-1):
        # Initialiser le min
        min=liste[i][2:6]
        jmin=i
        for j in range(i, len(liste)):
            # Chercher le min
            if liste[j][2:6]<min:
                jmin=j
                min=liste[j][2:6]
        # Permuter le min et l'élément i
        liste[i],liste[jmin]=liste[jmin],liste[i]

tri_pieces(liste_pieces)
#print(liste_pieces)

from PIL import Image
piece0 = Image.open('/home/eleve/Ressources/PTSI/boite/{}'.format(liste_pieces[0]))
lx,ly=piece0.size
dx,dy=12,12
image = Image.new('RGB', (lx*dx, ly*dy))
i=0
py=0
for y in range(dy):
    px=0
    for x in range(dx):
        nom_piece='/home/eleve/Ressources/PTSI/boite/{}'.format(liste_pieces[i])
        piece = Image.open(nom_piece)
        image.paste(piece, (px, py))
        i+=1
        px+=lx
    py+=ly

#image.show()

piece0 = Image.open('/home/eleve/Ressources/PTSI/boite/{}'.format(liste_pieces[0]))
lx,ly=piece0.size
dx,dy=12,12
image = Image.new('RGB', (lx*dx, ly*dy))
i=0
px=0
for x in range(dx):
    py=0
    for y in range(dy):
        nom_piece='/home/eleve/Ressources/PTSI/boite/{}'.format(liste_pieces[i])
        piece = Image.open(nom_piece)
        image.paste(piece, (px, py))
        i+=1
        py+=ly
    px+=lx
    
image.save('puzzle.png')

import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

image = img.imread('puzzle.png')
image = img.imread('puzzle_annee_derniere.png')
plt.imshow(image)
plt.show()

def convert_nb_evol(image):
    image_out=np.zeros(np.shape(image))
    coefficients=[0.2125,0.7154,0.0721]
    for j in range(3):
        for i in range(3):
            image_out[:,:,j]+=image[:,:,i]*coefficients[i]
    return image_out

plt.imshow(convert_nb_evol(image))
plt.show()
