# ============================
#  Algorithme glouton :
#     "Plus proche voisin"
#  pour une tournée de livraison
# ============================

# Question 1

file=open('distances.csv','r')
contenu=file.read()
file.close()

lignes=contenu.split('\n')
distances=[]
for ligne in lignes[:-1]:
    data=ligne.split(';')
    data=[int(i) for i in data]
    distances.append(data)

print(distances[0][1])
print(distances[1][0])

#distances=[[0,10,2,9,3],[10,0,8,1,7],[2,8,0,5,4],[9,1,5,0,6],[3,7,4,6,0]]

# Question 2

villes=['Amiens','Bayonne','Caen','Dax','Evry']

def calcul_distance(ville1,ville2):
    return distances[villes.index(ville1)][villes.index(ville2)]

print(calcul_distance('Bayonne','Dax'))

# Question 3

def plus_proche(ville_base,sous_groupe_villes):
    plus_proche=sous_groupe_villes[0]
    dist_plus_proche=calcul_distance(ville_base,plus_proche)
    for ville in sous_groupe_villes:
        if calcul_distance(ville_base,ville)<dist_plus_proche:
            dist_plus_proche=calcul_distance(ville_base,ville)
            plus_proche=ville
    return plus_proche

sous_groupe_villes=['Amiens','Bayonne','Caen']

print(plus_proche('Dax',sous_groupe_villes))

# Question 4

def generer_tournee(depart,villes_a_visiter):
    visitees = [depart]
    courant = depart

    # tant qu'il reste des villes non visitées
    while len(visitees) < len(villes_a_visiter):
        non_visitees = [v for v in villes_a_visiter if v not in visitees]
        
        # choix glouton : prendre la ville la plus proche
        prochain = plus_proche(courant,non_visitees)
                
        visitees.append(prochain)
        courant = prochain

    # retour au point de départ
    visitees.append(depart)
    return visitees

tournee = generer_tournee('Amiens',villes)

print(tournee)

# Question 5

def longueur_tournee(tournee):
    total = 0
    for i in range(len(tournee) - 1):
        total += calcul_distance(tournee[i],tournee[i+1])
    return total

longueur = longueur_tournee(tournee)

print(longueur)
