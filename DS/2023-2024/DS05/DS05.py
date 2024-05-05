###############PROF######################

import json
import matplotlib.pyplot as plt
import numpy as np
import random as rd

dictionary={}

U0=2
tau=0.13
var=100
lt=[]
lu=[]
data=[[0,U0*0.98]]
datalog=[[0,np.log(U0*0.98)]]
for i in range(20):
    t=rd.randrange(0, 1000)/1000
    u=U0*np.exp(-t/tau)*(1+rd.randrange(-var, var)/var*t)
    if not t in lt:
        lt.append(t)
        lu.append(u)
        data.append([t,u])
        datalog.append([t,np.log(u)])

dictionary['temps']=lt
dictionary['U']=lu
dictionary['log(U)']=[np.log(u) for u in lu]
dictionary['datalog']=datalog
dictionary['titre']='Tension décharge condensateur (V)'

#with open("donnees.json", "w") as outfile:
#    json.dump(dictionary, outfile)
    
#########################################

# Question 1

import json

with open('donnees.json', 'r') as openfile:
    dictionnaire = json.load(openfile)

print(dictionnaire['titre'])

# Question 2

import numpy as np

lt=np.array(dictionnaire['temps'])
lu=np.array(dictionnaire['U'])
loglu=np.array(dictionnaire['log(U)'])
datalog=dictionnaire['datalog']

print(datalog)

# Question 3

import matplotlib.pyplot as plt

plt.scatter(lt,lu)
plt.show()

plt.scatter(lt,loglu)
plt.show()

# Question 4

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


liste=[2,4,3,1,5]
tri(liste)
print(liste)

# Question 5

def tri2(liste):
    # Parcours de 1 à la taille de la liste
    for i in range(len(liste)-1):
        # Initialiser le min
        min=liste[i][0]
        jmin=i
        for j in range(i, len(liste)):
            # Chercher le min
            if liste[j][0]<min:
                jmin=j
                min=liste[j][0]
        # Permuter le min et l'élément i
        liste[i],liste[jmin]=liste[jmin],liste[i]

#On peut également comparer deux listes en utilisant les opérateurs >, <, >=
#et <=. Dans ce cas, les listes sont comparées en suivant l'ordre lexicographique.
#Les premiers éléments de chaque liste sont d'abord comparés entre eux.
#Si celui de la première liste est plus petit (resp. plus grand) que celui de la
#seconde liste, alors la première liste est plus petite (resp. plus grande) que
#la seconde. Si les premiers éléments sont égaux, alors la comparaison continue
#avec les deuxièmes éléments

print(datalog)
tri2(datalog)
print(datalog)

# Question 6

print("L'ordonnée à l'origine est {:.2f}".format(datalog[0][1]))

# Question 7

datalog0=[]
for t,data in datalog:
    datalog0.append([t,data-datalog[0][1]])

for t,data in datalog0:
    plt.scatter(t,data)
plt.show()

# Question 8

def ecart(liste,pente):
    somme=0
    for i in range(len(liste)):
        somme+=(liste[i][0]*pente-liste[i][1])**2
    return somme

print(ecart(datalog0,-5),ecart(datalog0,-10))

# Question 9

pentes=np.linspace(-20,0,1000)
ecarts=[ecart(datalog0,pente) for pente in pentes]

# Question 10

imin=0
min=ecarts[imin]
for i in range(1,len(ecarts)):
    if ecarts[i]<min:
        imin=i
        min=ecarts[i]
pente=pentes[imin]
print('On trouve une pente de {:.2f}'.format(pente))
print('La valeur de tau est {:.2f}'.format(-1/pente))

# Question 11

# Intro
datalog=np.array(datalog)
x=[0,1,2,3]
y=[0.86,3.3,4.8,6.9]
result=np.polyfit(x,y,1)
print("La fonction polyfit donne une pente de {:.2f} et une ordonnée à l'origine {:.2f} => OK.".format(result[0],result[1]))

# Réponse
datalog=np.array(datalog)
x=datalog[:,0]
y=datalog[:,1]
result=np.polyfit(x,y,1)
print("Notre script donne une pente de {:.2f} et une ordonnée à l'origine {:.2f}.".format(pente,datalog[0][1]))
print("La fonction polyfit donne une pente de {:.2f} et une ordonnée à l'origine {:.2f} => OK.".format(result[0],result[1]))

# Question 12

for x1,y1 in datalog:
    plt.scatter(x1,y1)
plt.plot(x,pente*x+datalog[0][1])
plt.plot(x,result[0]*x+result[1])
plt.show()
