# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 06:11:58 2013

@author: stephane
"""

from cadeau_tp_boucles import est_premier
from math import factorial, sqrt
#
# Exo 1 : Fait !
#

#
# Exo 2 :
#

somme = 0

for k in range(831, 945):
    somme = somme+k**10

autre_somme = sum(k**10 for k in range(831,945))

print(u"J'hésite entre %i et %i"%(somme,autre_somme))

#J'hésite entre 36724191150365100572161020220825 et
# 36724191150365100572161020220825

#
# Exo 3 :
#

res = 1

for i in range(1,842):
    res = res*3

print(u"La différence avec le bon résultat vaut %i"%(res-3**841))

#La différence avec le bon résultat vaut 0

#
# Exo 4 :
#

facto100 = 1

for i in range(2,101):
    facto100 = facto100*i

print(u"La différence avec le bon résultat vaut %i"%(facto100-factorial(100)))

#La différence avec le bon résultat vaut 0

#
# Exo 5 :
#

somme, n = 0, facto100

while n>0:
    somme += n%10
    n = n//10

print("La somme vaut "+str(somme))

#La somme vaut 648

#
# Exo 6 :
#

def fibo(n):
    if n <= 1:
        return n
    a,b = 0,1
    for k in range(1,n+1):
        a,b = b,a+b
    return a

#>>> list(fibo(n) for n in range(11))
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#>>> fibo(100)
#354224848179261915075L
#>>> fibo(1000)
#434665...849228875L

#
# Exo 7 :
#

for n in range(20):
    if est_premier(n):
        print(n)

#2
#3
#5
#7
#11
#13
#17
#19

#
# Exo 8 :
#

"""
Si l'entier est pair, il y a juste un ou deux tests de réalisés, et une
division euclidienne.

S'il est premier, il va y avoir grosso modo sqrt(n) divisions euclidiennes
d'effectuées
"""

#
# Exo 9 :
#

"""
Pour les entiers premiers, le coût de traitement sera de l'ordre de
(N/ln N)*sqrt(N), soit 10**9/(6*ln(10)) pour N=10**6 : c'est acceptable
(penser à la rêgle du mulliard).

C'est plus difficile à évaluer pour les composés : certains auront
un coût proche de sqrt(N), mais ils seront peu nombreux. La plupart
auront un premier diviseur faible, donc on peut espérer un coût qui soit
plus proche de N ou N.ln(N) que de N^{3/2}

On avait bien dit à la louche...
"""

#
# Exo 10 :
#


for nmax in [10**2, 10**4, 10**6]:
    cpt = 0
    for n in range(1, 1+nmax):
        if est_premier(n):
            cpt = cpt+1
    print(u"Jusqu'à "+str(nmax)+" : "+str(cpt)+" entiers sont premiers.")

#Jusqu'à 100 : 25 entiers sont premiers.
#Jusqu'à 10000 : 1229 entiers sont premiers.
#Jusqu'à 1000000 : 78498 entiers sont premiers.

#
# Exo 11 :
#

cpt = 0
for n in range(2, 10**6):
    if est_premier(n) and est_premier(n+2):
        cpt = cpt+1

print(u"Jusqu'à "+str(10**6)+" : "+str(cpt)+" couples de premiers jumeaux.")

#Jusqu'à 1000000 : 8169 couples de premiers jumeaux.

# Exercice : comment gagner quelques pouillèmes de secondes dans la boucle ?

#
# Exo 12 :
#


n = 10**10+1
while not(est_premier(n) and est_premier(n+2)):
    n = n+2

print("Premiers jumeaux après 10**10 : "+str(n)+" et "+str(n+2))

#Premiers jumeaux après 10**10 : 10000000277 et 10000000279

#
# Exo 13 :
#

"""
On modifie est_premier pour tenir à jour un compteur global
de divisions euclidiennes
"""

cpteur_divisions = 0

def est_premier_bis(n):
    global cpteur_divisions # à n'utiliser que exceptionnellement !
    if n <= 1:
        return False
    if n <= 3:
        return True
    for k in range(2,1+int(sqrt(n))):
        cpteur_divisions += 1
        if n % k ==0 :
            return False
    return True

for nmax in [10**2, 10**4, 10**6]:
    cpt = 0
    cpteur_divisions = 0
    for n in range(1, 1+nmax):
        if est_premier_bis(n):
            cpt = cpt+1
    print(u"Jusqu'à "+str(nmax)+" : "+str(cpt)+" entiers sont premiers,")
    print(u"ce qui m'a demandé "+str(cpteur_divisions)+" divisions.")

"""
Jusqu'à 100 : 25 entiers sont premiers,
ce qui m'a demandé 236 divisions euclidiennes.
Jusqu'à 10000 : 1229 entiers sont premiers,
ce qui m'a demandé 117527 divisions euclidiennes.
Jusqu'à 1000000 : 78498 entiers sont premiers,
ce qui m'a demandé 67740404 divisions euclidiennes.

>>> int((10**9)/(log(10**9)))
48254942

La majorité des divisions euclidiennes a été effectué pour la petite
proportion de nombres premiers.

Chaque nombre composé a demandé en moyenne un peu moins de 20 divisions.
"""

#
# Exo 14 :
#

un = 42
for n in range(1,10**6+1):
    un = (15091*un) % 64007
    if n in {1,10,10**6}:
        print("u[%i]=%i"%(n,un))
#u[1]=57759
#u[10]=15421
#u[1000000]=14918


#
# Exo 15 :
#

"""
On va calculer les u_n et dénombrer ceux vérifiant les différentes
propriétés à la volée, avec un tableau de 6 compteurs
Mais on aurait pu prendre 6 variables évidemment
"""

cpts = [0] * 6

# héhé
#>>> cpts
#[0, 0, 0, 0, 0, 0]

"""
On va tabuler la primalité des entiers <= 64006 pour ne pas refaire
les mêmes tests en permanence
"""
premier = [est_premier(k) for k in range(64007)] # on peut aussi maper...

# sliçons :
#>>> premier[ : 10]
#[False, False, True, True, False, True, False, True, False, False]

un = 42
for n in range(1,10**7+1):
    un = (15091*un) % 64007
    if (un % 2) == 0:
        cpts[0] += 1
    if premier[un]:
        cpts[1] += 1
    if (un % 3) == 1:
        cpts[2] += 1
    if ((un % 3) == 1) and premier[un]:
        cpts[3] += 1
    if ((un % 2) == 0) and premier[un]:
        cpts[4] += 1
    if ((n % 2) == 0) and premier[un]:
        cpts[5] += 1

#>>> cpts
#[4999968, 1001923, 3333434, 499050, 156, 493240]

#
# Exo 16 :
#

#>>> (17*923)%10
#1
#>>> (12345678987654*836548971236)%10
#4L



#
# Exo 17 :
#

somme = 0
for k in range(1,1001):
    res = 1
    for i in range(k):
        res = (res*k) % 10**10
    somme = (somme + res) % 10**10

print("Les dernières décimales de la somme sont "+str(somme))

#Les dernières décimales de la somme sont 9110846700

#
# Exo 18 :
#

res = 1
for i in range(1, 1+654321):
    res = (res*123456) % 1234567

print(u"%i est plus rapide à calculer que %i"%(res,(123456**654321)%1234567))

#
# Exo 19 :
#

nb_pbs = 0
for p in range(2,1+10**4):
    facto_mod = 1
    for i in range(2,p):
        facto_mod = (facto_mod*i)%p
    if (est_premier(p) and not((facto_mod+1)%p == 0))\
    or (not(est_premier(p)) and (facto_mod+1)%p == 0):
        print(u"Problème avec "+str(p))
        nb_pbs += 1

# Aucun affichage; ouf !
#>>> nb_pbs
#0


#
# Exo 20 :
#

for n in range(3,31):
    cpt = 0
    for k in range(2,n):
        if (k**2 % n)== n-1:
            cpt += 1
    print("%i -> %i"%(n,cpt))

"""
C'est 0 ou 2, avec 2 pour les entiers suivants :
    5, 10, 13, 17, 25, 26, 29

    Les suivants ?
"""

liste = []
for n in range(3,101):
    cpt = 0
    for k in range(2,n):
        if (k**2 % n)== n-1:
            cpt += 1
    if cpt == 2:
        liste.append(n)

#>>> liste
#[5, 10, 13, 17, 25, 26, 29, 34, 37, 41, 50, 53, 58, 61, 73, 74, 82, 89, 97]

cpt0 = 0
for n in range(3,1001):
    cpt = 0
    for k in range(2,n):
        if (k**2 % n)== n-1:
            cpt += 1
    if cpt>0:
        cpt0 += 1

#>>> cpt0
#186

#
# Exo 21 :
#

for p in range(100):
    if est_premier(p):
        a = 0
        trouve = False
        while not(trouve) and a**2 <= p/2:
            trouve = (p-a**2 == (int(sqrt(p-a**2)))**2) # :-)
            a += 1
        if trouve:
            print(p)

"""
2, 5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97

On récupère 2 et les premiers congrus à 1 modulo 4; c'est un grand classique !
"""

solutions = []
for n in range(1,50):
        a = 0
        trouve = False
        while not(trouve) and a**2 <= n/2:
            trouve = (n-a**2 == (int(sqrt(n-a**2)))**2) # :-)
            a += 1
        if trouve:
            solutions.append(n)

#>>> solutions
#[1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25, 26, 29, 32, 34, 36, 37, 40, 41, 45, 49]

"""
Alors, comment caractériser ces entiers ? :-)

Si vous voyez passer un prof de maths, demandez-lui !
"""

#
# Exo 22 :
#

fibo = [0]*(1+10**6)
fibo[1] = 1
for n in range(10**6-99):
    fibo[n+100] = (fibo[n]+fibo[n+1]) % 1515

print(fibo[10**6])

# 741

"""
On pouvait aussi économiser de la place !
"""

fibo = [0]*100
fibo[1] = 1

for n in range(10**6-99):
    fibo[(n+100)%100] = (fibo[n%100]+fibo[(n+1)%100]) % 1515

print(fibo[10**6%100])

# 741

"""
Pour 10**15, un calcul en temps linéaire est exclu; on va donc suivre
l'indication, qui va se ramener à un calcul de la forme A^n avec A une
matrice : un tel calcul demande de l'ordre de ln(n) multiplications

On utilise la bibliothèque numpy pour faire les produits matriciels
"""

import numpy as np

A1 = np.zeros((100,100),int)
for i in range(99):
    A1[i,i+1] = 1

A1[99,0] = 1
A1[99,1] = 1

"""
On va effectuer une exponentiation rapide
"""

n = 10**15
modu = 10**4

A = A1.copy()

res = np.identity(100,int)
while n>0:
    if n%2 == 1:
        res = res.dot(A)
    A = A.dot(A)
    n = n // 2
    for i in range(100):
        for j in range(100):
            A[i,j] = A[i,j] % modu
            res[i,j] = res[i,j] % modu


print(res[0,1]) # si si, c'est ici qu'on doit trouver le résultat !

# 3265

# pour n=10^6 et modu=1515, on trouve bien 741 !

"""
Temps de calcul pour l'ensemble du tp : 1'41''
"""