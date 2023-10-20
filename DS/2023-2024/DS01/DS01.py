# Exercice 1

colonnes=['Nom pays','Victoires','Nuls','Défaites','Differences points','Points bonus','Total points']
groupe_A=[['France',3,0,0,125,1,0],['Italie',2,0,1,-14,2,0],['Namibie',0,0,4,-218,0,0],['Nouvelle-Zélande',2,0,1,133,2,0],['Urugay',1,0,2,-26,1,0]]

#Question 1:

def calcul_points(equipe):
    return equipe[1]*4+equipe[2]*2+equipe[5]

for equipe in groupe_A:
    equipe[6]=calcul_points(equipe)

def sort_key(equipe):
    return equipe[6],equipe[4]

groupe_A.sort(key=sort_key, reverse=True)

for equipe in groupe_A:
    print(equipe)

# Exercice 2

somme=0
for i in range(64):
    somme+=2**i

print(somme)

poids=0.028

total=somme*poids
print(total/1000)    

# Exercice 3


def somme_chiffres(nombre):
    somme=0
    while nombre//10>0:
        reste=nombre%10
        nombre=nombre//10
        somme+=reste
    somme+=nombre
    return somme

    
for i in range(1,10**4):
    if somme_chiffres(i)%3==0:
        if i%3!=0:
            print('Faux')
    else:
        if i%3==0:
            print('Faux')

for i in range(1,10**4):
    while i>9:
        i=somme_chiffres(i)
    if i in [3,6,9]:
        if i%3!=0:
            print('Faux')
    else:
        if i%3==0:
            print('Faux')
