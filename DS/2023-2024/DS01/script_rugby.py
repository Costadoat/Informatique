# Exercice 1

colonnes=['Nom pays','Victoires','Nuls','Défaites','Differences points','Points bonus','Total points']
groupe_A=[['France',3,0,0,125,1,0],['Italie',2,0,1,-14,2,0],['Namibie',0,0,4,-218,0,0],['Nouvelle-Zélande',2,0,1,133,2,0],['Urugay',1,0,2,-26,1,0]]

#Question 1:

def calcul_points(equipe):
    return equipe[1]+equipe[2]

for equipe in groupe_A:
    equipe[...]=calcul_points(equipe)

def sort_key(equipe):
    return equipe[6],equipe[4]

groupe_A.sort(key=sort_key, reverse=True)

for equipe in groupe_A:
    print(equipe)
