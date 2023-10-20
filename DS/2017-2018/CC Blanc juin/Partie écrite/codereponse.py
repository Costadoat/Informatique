# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:36:29 2018

@author: willie
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#Exercice 1
#question 1

def f(theta,theta0,g,l):
    return 4*math.sqrt(l/(2*g*(math.cos(theta)-math.cos(theta0))))
    
#question 2
def periodeRect(f,theta0,g,l,n):
    somme=0
    for i in range(n):
        thetai = i*theta0/float(n)
        somme = somme + f(thetai,theta0,g,l)*theta0/float(n)
    return somme

theta0=math.pi/6.
g=9.81
l=1.
n=10000

#question 3

listetheta0=np.linspace(0.01,math.pi-0.01,100)
listeperiodes=[]

for theta0 in listetheta0:
    listeperiodes.append(periodeRect(f,theta0,g,l,n))
    
plt.plot(listetheta0,listeperiodes)
plt.grid()
plt.xlabel(r'$\theta_0$ (rad)')
plt.ylabel(r'$T$ (s)')
plt.show()
plt.close()

#question 4

#On cherche un angle entre et pi on initialise dans cet intervalle
#de facon raisonnable donc en excluant les divisions par zero en 0 et pi
theta1=0.01
theta2=math.pi-0.01

T0 = 2*math.pi*math.sqrt(l/g) #periode propre = periode aux faibles amplitudes

while abs(theta1-theta2)>0.0002:#tant que l intervalle est grand on le coupe en deux
    theta3=(theta1+theta2)/2.# on divise par deux la borne sup
    # on regarde si dans le nouvel intervalle la période differe de plus 
    #de un pourcent de la periode propre
    if (periodeRect(f,theta1,g,l,n)-T0*1.01)*(periodeRect(f,theta3,g,l,n)-T0*1.01)<0:
        theta2=theta3 # si oui on conserve cette valeur de borne sup
    else:
        theta1=theta3 # sinon c'est que la periode differe de plus de un pourcent 
        # de la periode propre dans l autre demi intervalle

print theta1,(theta2+theta1)/2.,theta2

#Exercice 2

def f(a):
    i=1#initialisation a 1 puis que 0 ne modifie pas la somme
    n=0#initialsiation de la somme
    while i<=a:#tant que i est inferieur a a
        if i%2==0:#test de parite via le reste de la division euclidienne de i par 2
            n=n+i#si i est pair on l ajoute a la somme
        i=i+1#on incremente i
    return n#quand la boucle est finie on renvoie la somme

def g(a):
    n=0
    for i in range(1,a+1):
        if i%2==0:
            n=n+i
    return n
