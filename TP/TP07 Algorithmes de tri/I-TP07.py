# Programme Python pour l'implémentation du tri par insertion
import time
from random import randrange

# Question 1
def tri_selection(liste): 
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

# Question 2
liste=[6,3,4,2,7,1,5]
tri_selection(liste) 
print(liste)

# Question 3
def tri_insertion(liste): 
    # Parcour de 1 à la taille de la liste
    for i in range(1, len(liste)):
        # On mémorise la position initiale de l'élément
        k = liste[i]
        # On décale cet élément vers la gauche tant que
        # l'élément précédent est plus grand que lui
        j = i-1
        while j >= 0 and k < liste[j] : 
                liste[j + 1] = liste[j] 
                j -= 1
        liste[j + 1] = k

# Question 4
liste=[6,3,4,2,7,1,5]
tri_insertion(liste) 
print(liste)

# Question 5
def tri_bulle(liste):
    # Parcours de 1 à la taille de la liste
    for i in range(1, len(liste)):
        # Parcours des éléments précédents
        for j in range(0, len(liste)-i):
            # On permutte les deux éléments successifs
            if liste[j] > liste[j+1] :
                liste[j], liste[j+1] = liste[j+1], liste[j]
            #print(liste)

# Question 6
liste=[6,3,4,2,7,1,5]
tri_bulle(liste) 
print(liste)

# Question 7
liste=[6,3,4,2,7,1,5]
start = time.time()
tri_selection(liste)
end = time.time()
print(end - start)

liste=[6,3,4,2,7,1,5]
start = time.time()
tri_insertion(liste)
end = time.time()
print(end - start)

liste=[6,3,4,2,7,1,5]
start = time.time()
tri_bulle(liste)
end = time.time()
print(end - start)

# Question 9
size=100
tirages=2

t=[[],[],[]]
fonction=[tri_selection,tri_insertion,tri_bulle]
nom_fonction=["Tri par sélection","Tri par insertion","Tri à bulles"]
for i in range(tirages):
    print(i)
    liste0=[randrange(size) for i in range(size)]
    for j in range(3):
        liste = liste0
        #print(liste)
        start = time.time()
        fonction[j](liste) 
        end = time.time()
        #print(liste)
        t[j].append(end - start)
        
def moyenne(l):
    somme=0
    for i in l:
        somme+=i
    return somme/len(l)

for i in range(3):
    print(nom_fonction[i],min(t[i]),max(t[i]),moyenne(t[i]))
