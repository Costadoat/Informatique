#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:19:30 2021

@author: jg
"""

from math import atan,exp
import matplotlib.pyplot as plt

L=[1,7.6,8,10.1]
a=7

def recherche_naive(L,a):
    i=0
    while L[i]!=a and i<len(L)-1:
        i=i+1
    if L[i]==a:
	return(i)
    else:
	return(False)   


#print(recherche_naive(L,a))


def dichotomie(L, a):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == a:
            return m
        elif L[m] < a:
            debut = m + 1
        else:
            fin = m - 1
    return False



#print(dichotomie(L,a))


def dichotomie_comparatif(L, a):
    debut = 0
    fin = len(L) - 1
    compteur=0
    while debut <= fin:
        compteur=compteur+1
        m = (debut+fin) // 2
        if L[m] == a:
            return m,compteur
        elif L[m] < a:
            debut = m + 1
        else:
            fin = m - 1
    return False,compteur

L=[1,7.6,8,10,12,13,14,15,16]
a=15

#print(dichotomie_comparatif(L,a))



def dicho_zero(L):
    debut = 0
    fin = len(L) - 1
    while debut <= fin:
        m = (debut+fin) // 2
        if L[m] == 0:
            return m
        elif L[m] < 0:
            debut = m + 1
        else:
            fin = m - 1
    return(m)        
    
L=[-2,-1,0.0001,2,3]    


def f(x):
    return(exp(x)+x)

X=[]
x=-1
for i in range(1000):
    x=x+2/1000.
    X.append(x)
    
L=[]
for x in X:
    L.append(f(x)) 


print(dicho_zero(Y))
print(X[dicho_zero(L)])

import matplotlib.pyplot as plt    
plt.plot(X,L)  
plt.plot(X,[0]*len(X)) 

plt.savefig('graphe_f.pdf')

plt.show() 
