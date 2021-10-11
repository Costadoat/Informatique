# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:29:36 2016

@author: G
"""

import numpy as np
from math import *
from time import time

 
def carre(x):
    return(x**2-2)
def carre_prime(x):
    return(2*x) 

    
#==============================================================================
# Dichotomie
#==============================================================================
def dicho(f,a,b,eps):               
    if f(a)*f(b)>0:
        return('nous ne savons pas si f s annule entre a et b')
    while (b-a)>2*eps:
        c=(float(a)+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c    
    return((a+b)/2)

#print(dicho(carre,0,2,0.01))            

#==============================================================================
# Exerice 3 : methode de Newton avec derivee, critere d arret : nb iteration
#==============================================================================
def Newton1(f,fprime,u0,nb_iteration):
    u=float(u0)
    for i in range(nb_iteration):
        u=u-f(u)/fprime(u)
    return(u) 
   
    
# en 5 etapes, on obtient une approximation de sqrt(2) de 1e-12    
#print(Newton1(carre,carre_prime,2,3)-sqrt(2))    
#print(Newton1(carre,carre_prime,2,4)-sqrt(2))    
 

#==============================================================================
# Exerice 4 : methode de Newton qui diverge
#==============================================================================

def h(x):
    return(x**3-2*x+2)
def h_prime(x):
    return(3*x**2-2)  

#for i in range(1,6):    
#    print(Newton1(h,h_prime,0,i))  
# 
#for i in range(1,15):    
#    print(Newton1(h,h_prime,0.1,i)) 

 
#==============================================================================
# Exerice 5 : methode de Newton avec derivee, critere d arret : ecart
#==============================================================================
   
nb_iteration=1000 # pour stopper la boucle meme si la suite diverge
# methode 1
def Newton2(f,fprime,u0,epsilon):
    u0=float(u0)
    u1=u0-f(u0)/fprime(u0)
    compteur=0    # on compte le nb d iterations de la boucle
    while abs(u1-u0)>epsilon and compteur<nb_iteration : # test d arret : on itere la boucle si l ecart entre xn et x(n+1) est grand et si on a fait moins de 100 iterations
        u0=u1
        u1=u1-f(u1)/fprime(u1)
        compteur=compteur+1
    return(u1)  

#methode 2
def Newton2Bis(f,fprime,u0,epsilon):
    u=float(u0)
    compteur=0
    while abs(f(u)/fprime(u))>epsilon and compteur<nb_iteration : # l ecart entre xn et x(n+1) est f(xn)/fprime(xn)
        u=u-f(u)/fprime(u)
        compteur=compteur+1
    return(u)     
    
#print(Newton2(sin,cos,2,1e-3)-pi)  # la difference est bien inferieure a epsilon
                                   # elle est meme tres inferieure, car l algorithme est tres rapide     

#==============================================================================
# Exerice 6 : comparaison methode de Newton et dichotomie
#==============================================================================
def dicho_comparaison(f,a,b,eps):
    t=time()             # donne le temps de calcul
    compteur=0           # va compter le nombre d'iterations                
    if f(a)*f(b)>0:
        return('nous ne savons pas si f s annule entre a et b')
    while (b-a)>2*eps:
        compteur=compteur+1
        c=(float(a)+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c     
    return((a+b)/2,time()-t,compteur)

def Newton_comparaison(f,fprime,u0,epsilon):
    t=time()             # donne le temps de calcul
    compteur=0           # va compter le nombre d'iterations        
    u0=float(u0)
    u1=u0-f(u0)/fprime(u0)
    while abs(u1-u0)>epsilon and compteur<nb_iteration : # test d arret : on itere la boucle si l ecart entre xn et x(n+1) est grand et si on a fait moins de 100 iterations
        u0=u1
        u1=u1-f(u1)/fprime(u1)
        compteur=compteur+1
    return(u1,time()-t,compteur)      

#print(Newton_comparaison(carre,carre_prime,2,1e-15))
#print(dicho_comparaison(carre,0,2,1e-15))

    
    
#==============================================================================
# Exerice 7 : methode de Newton sans la derivee, critere d arret : ecart
#==============================================================================
          
nb_iteration=1000 # pour stopper la boucle meme si la suite diverge
def Newton3(f,h,u0,epsilon):
    u0=float(u0)
    derivee=(f(u0+h)-f(u0))/h
    u1=u0-f(u0)/derivee
    compteur=0
    while abs(u1-u0)>epsilon and compteur<nb_iteration:
        u0=u1
        derivee=(f(u1+h)-f(u1))/h
        u1=u1-f(u1)/derivee
        compteur=compteur+1
    return(u1,compteur)     

#==============================================================================
# Exercice 8 : Methode de la secante
#==============================================================================

def secante(f,u0,u1,eps):
    u0=float(u0)
    u1=float(u1)
    compteur=0
    while abs(u0-u1)>eps and compteur<nb_iteration:
        temp=u1
        u1=u1-f(u1)*(u1-u0)/(f(u1)-f(u0))
        u0=temp
        compteur=compteur+1
    return(u1,compteur)     

 

#==============================================================================
# Exercice : Newton en complexe     
#==============================================================================

def Newtoncx(f,fprime,u0,nb_iteration):
    u=u0
    for i in range(nb_iteration):
        u=u-f(u)/fprime(u)
    return(u) 

def t(x):
    return(x**2+1)
def tprime(x):
    return(2*x)    
    
#print(Newtoncx(t,tprime,2.+1j,100)) 


    
def g(x):
    return(x**3-1)
def gprime(x):
    return(3*x**2)    

print(Newtoncx(g,gprime,1.+1J,100))    
print(Newtoncx(g,gprime,1.-10J,100)) 
print(Newtoncx(g,gprime,-1.+1J,10)) 
print(Newtoncx(g,gprime,-1.-1J,10))    