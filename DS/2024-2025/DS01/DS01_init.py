# -*- coding: utf-8 -*-

#Question 1:

# Import des bibliotheques
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Fonction qui détermine la couleur d'un pixel
# en fonction de sa position
def colorFader(mix=0):
    c1=np.array([1,0,0])
    c2=np.array([0,1,0])
    return (1-mix)*c1 + mix*c2

# Parcours de la spirale a partir du centre
# en fonction de la valeur de entier
# a recopier pour la question 1 et à copier et
# modifier pour la question 3
max=2000
imagebase = np.ones([int(max**0.5)+1,int(max**0.5)+1,3])
coords=[0,0]
i=0
entier=0
while entier<max:
    entier+=1
    # le pixel de imagebase qui a pour coordonnées
    # [coords[0]+(int(max**0.5))//2,coords[1]+(int(max**0.5))//2]
    # est coloré avec une couleur déterminée par la fonction colorFader
    dec=(int(max**0.5))//2
    imagebase[coords[0]+dec,coords[1]+dec]=colorFader(entier/max)
    # on passe ensuite au pixel suivant pour parcourir toute la spirale
    if coords==[i,-i]:
        coords[0]+=1
        i+=1
    elif coords[0]==i and coords[1]<i:
        coords[1]+=1
    elif coords[0]>-i and coords[1]==i:
        coords[0]-=1
    elif coords[0]==-i and coords[1]>-i:
        coords[1]-=1
    elif coords[0]<i and coords[1]==-i:
        coords[0]+=1

# Tracé de la figure de la réponse
plt.imshow(imagebase)
plt.show()

# Question 2:
def est_pair(n):
    return n%2==1

print(est_pair(3))


