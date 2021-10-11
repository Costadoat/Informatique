#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:44:01 2021

@author: jg
"""

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


#==============================================================================
# Exercice 1, Dichotomie
#==============================================================================

# question 1 
def f(x):
    return(x**(n+1)-x**n-1)

#
## question 2
#n=10
#print(f(1))
#
#
## question 3
#for n in range(1,11):
#    X=np.linspace(1,2,100)
#    Y=f(X)
#    plt.plot(X,Y,label=n) 
#    plt.xlim(1,2)
#    plt.ylim(-1,1)  
#    plt.legend()  
#    
#    
## question 4
## conjecture : la suite est décroissante et converge vers un nombre plus grand que 1. 
    

# question 5
def dicho(f,a,b,e):
    while(abs(b-a)>e):
        c=(a+b)/2.
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    return(a) 


## question 6
#ALPHA=[]
#for n in range(2,201):
#    ALPHA.append(dicho(f,1,2,10**(-6)))    
## Conjecture : la suite converge vers 1


#==============================================================================
# Exercice 2, listes    
#==============================================================================

## question 1
#def maxi(L):
#    valeur_max=L[0]
#    indice_max=0
#    for i in enumerate(L):
#        if i[1]>valeur_max:
#            valeur_max=i[1]
#            indice_max=i[0]
#    return(valeur_max,indice_max)       
            


## question 2a
#def estCroissante(L):
#    i=0
#    while i<len(L)-1 and L[i]<=L[i+1]:
#        i=i+1
#    if i==len(L)-1:
#        return(True)
#    else:
#        return(False)
#    
#    
## question 2b
#L=[0,1,3,8,8]
#print(estCroissante(L))   
#
#
## question 2c
#def estDecroissante(L):
#    i=0
#    while i<len(L)-1 and L[i]>=L[i+1]:
#        i=i+1
#    if i==len(L)-1:
#        return(True)
#    else:
#        return(False)
#    
#    
## question 2d 
#def estMonotone(L):
#    return(estCroissante(L) or estDecroissante(L))
    
    
# question 3a
def LC(L,p):
    i=p
    while i<len(L)-1 and L[i]<=L[i+1]:
        i=i+1
    return(i)  


## question 3b
#L=[0,1,0,1,3,3,5,0,1,7]
#print(LC(L,2))   
#
#
## question 3c
#def maxCroissante(L):
#    Longueur_max=0
#    indice=0
#    indice_max=0
#    while indice<len(L)-1 :
#        d=LC(L,indice)
#        if d-indice+1>Longueur_max:
#            Longueur_max=d-indice+1
#            indice_max=indice
#            
#        indice=d+1
#    return(Longueur_max,L[indice_max:indice_max+Longueur_max])        
#
#
## question 4a
##[1,2,1,2,1] ou [2,0,7,-9,15]
#
#
## question 4b
#def cahots(L):
#    i=1
#    while i<len(L)-1 and (L[i-1]-L[i])*(L[i]-L[i+1])<0:
#        i=i+1
#    if i==len(L)-1:
#        return(True)
#    else:
#        return(False)
#    
#L=[0,1,-1,6,0,-1]    
#print(cahots(L))
#
#
## question 4c
#L=[5,8,9,0,-1,7,16]
#L.sort()
#CAHOTS=[]
#for i in range(0,int(len(L)/2)):
#     CAHOTS.append(L[i])
#     CAHOTS.append(L[len(L)-i-1])
#if len(L)%2!=0:
#     CAHOTS.append(L[int(len(L)/2)])
#     
#print(CAHOTS)     
     
