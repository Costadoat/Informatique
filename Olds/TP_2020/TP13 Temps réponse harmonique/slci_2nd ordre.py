#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


# Q1 : reponse s(t)
def s(two,z):
    b=z**2-1
    if z>1:
        a=np.sqrt(b)
        return 1+np.exp(-two*(z+a))*(1./2./(z*a+b))-np.exp(-two*(z-a))*(1./2./(z*a-b))
    elif z<1:
        a=np.sqrt(-b)
        return 1-np.exp(-z*two)/a*np.sin(two*a+np.arcsin(a))
    else :
        return 1-(1+two)*np.exp(-two)

# domaine de valeurs pour two
two=[]
i=0
while i<10:
    two.append(i)
    i+=0.01


# Q2 : trace reponse z entre 1 et 10
plt.figure(1)
y=[]
for z in range(10):
    y.append([])

for z in range(10):
#    x=0
#    while x in two :
#        y[z].append(s(x,z+1))
#        x+=0.01
    for x in two:
        y[z].append(s(x,(z+1)/1.))
    plt.plot(two,y[z],label="z="+str(z+1))
plt.xlabel("two")
plt.ylabel("s(t)")
plt.title("reponse s(t) d'un 2nd ordre aperiodique")
plt.legend()
plt.grid(True)

# Q3 : trace reponse z entre 0.1 et 1

plt.figure(2)
y=[]
for z in range(10):
    y.append([])

for z in range(10):
#    x=0
#    while x in two :
#        y[z].append(s(x,(z+1)/10.))
#        x+=0.01
    for x in two:
        y[z].append(s(x,(z+1)/10.))
    plt.plot(two,y[z],label="z="+str((z+1)/10.))
plt.xlabel("two")
plt.ylabel("s(t)")
plt.title("reponse s(t)d'un 2nd ordre pseudoperiodique")
plt.legend()
plt.grid(True)


# Q4 : est dans la bande des +-5%
def dans_bande(v):
    if (v>=0.95) and (v<=1.05):
        return 1
    else:
        return 0

# temps de reponse reduit
plt.figure(3)

liste_z=[]
liste_trwo=[]
pas_z=0.01
pas_two=0.05
two=400

#z<0.6
#On teste la sortie de bande en partant d'une valeur de two suffisamment grande.
#Le temps de reponse reduit etant decroissant, on peut à chaque iteration de z,
#repartir avec la dernière valeur de trwo determinee.
z=0.01
while z<0.6 :
    while dans_bande(s(two,z)):
        two-=pas_two
    two+=pas_two
    liste_z.append(z)
    liste_trwo.append(two)
    z+=pas_z

#z>0.6 et z<=1
#On teste la sortie de bande en partant d'une valeur de two suffisamment grande.
#A chaque iteration de z, on prend two=7 comme valeur de depart.
z=0.6
while z<=1 :
    two=7
    while dans_bande(s(two,z)):
        two-=pas_two
    two+=pas_two
    liste_z.append(z)
    liste_trwo.append(two)
    z+=pas_z

# z>=1
#On teste l'entree de bande en partant d'une valeur de two suffisamment petite.
#Le temps de reponse reduit etant croissant, on peut à chaque iteration de z,
#repartir avec la dernière valeur de trwo determinee.
z=1
two=0
while z<50 :
    while not dans_bande(s(two,z)):
        two+=pas_two
    two-=pas_two
    liste_z.append(z)
    liste_trwo.append(two)
    z+=pas_z
    
plt.plot(liste_z,liste_trwo,label="trwo")
plt.xlabel("z")
plt.ylabel("trwo")
plt.title("temps de reponse reduit d'un 2nd ordre")
plt.legend()
plt.loglog()
plt.grid(which="major",axis="x",linewidth=1.5, linestyle='-')
plt.grid(which="major",axis="y",linewidth=1.5, linestyle='-')
plt.grid(which="minor",axis="x",linewidth=0.75, linestyle='-', color='0.75')
plt.grid(which="minor",axis="y",linewidth=0.75, linestyle='-', color='0.75')

# Affichage des traces

plt.show()
