# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np
import matplotlib.pyplot as plt

E=10
tau=0.06

def f(t):
    return E*(1-np.exp(-t/tau))

plt.figure(1)
t=np.arange(0,1,0.01)
plt.plot(t,f(t))

print f(1)

print 0.95*f(1)

def g(t):
    return f(t)-0.95*f(1)

p=10**(-6)

def dichotomie(f,p):
    a=-10
    i=1
    b=10
    while (b-a)>p :
        if f(a)*f((a+b)/2)<=0:
            a, b=a, (a+b)/2.
        else:
            a, b=(a+b)/2., b
        i=i+1
        e=b-a
    return "Resultat {} (Erreur:{})".format(a, e)

print dichotomie(g,p)
print 3*tau

fichier=open("trace.csv",'r')
contenu=fichier.read()

lignes=contenu.split("\n")
temps=[]
consigne=[]
sortie=[]
for ligne in lignes[0:-1]:
    temps.append(float(ligne.split(';')[0]))
    consigne.append(float(ligne.split(';')[1]))
    sortie.append(float(ligne.split(';')[2]))

fichier.close()
smoins=0.95*sortie[np.shape(temps)[0]-1]
splus=1.05*sortie[np.shape(temps)[0]-1]

plt.figure(2)
plt.plot(temps,sortie,'g')
plt.plot(temps,consigne,'b')
plt.plot(temps,splus*np.ones(np.shape(temps)[0]),'r')
plt.plot(temps,smoins*np.ones(np.shape(temps)[0]),'r')

tr=0
for i in range(len(sortie)):
    if sortie[i] < splus and sortie[i] > smoins and (sortie[i-1] > splus or sortie[i-1] < smoins) :
        tr=temps[i]
        
print tr